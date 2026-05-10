"""
11_generate_narrowed_topics.py

Algorithmic narrowing pass: generate evidence-driven topic variants from pipeline outputs.

For every topic with decision=NARROW, this script:
  1. Loads the dedup paper corpus for that topic
  2. Separates high-relevance (score >= 0.5) from noise (score <= 0.25) papers
  3. Extracts high-signal title n-grams from hi papers
  4. Identifies "noisy" secondary keywords (predominantly match lo papers)
  5. Generates up to 5 narrowed topic variants per parent topic via four strategies:
       A) primary-anchor: append top anchor term to primary keyword
       B) noise-pruned: drop noisy secondaries, move to negative_keywords
       C) synonym-promoted: promote a synonym that appears in hi papers to primary
       D) compound-pivot: use most common hi-paper title term as new primary + restrict domain
  6. Simulates the relevance filter on each variant against the existing paper corpus
  7. Estimates signals (relevance_purity, citation_signal, artifact_opportunity, etc.)
  8. Selects the top --top-n variants by composite score
  9. Writes data/topics_seed_narrowed.csv (drop-in for 10_run_pipeline.py --topics)
 10. Writes reports/narrowing_report.md
 11. Unless --no-autorun: launches pipeline on narrowed topics

Anti-anchoring principle: every direction is a candidate; the algorithm ranks by
estimated composite score derived from evidence alone — no topic is manually favoured.

Usage:
  python scripts/11_generate_narrowed_topics.py [--no-autorun] [--top-n 12]
  python scripts/11_generate_narrowed_topics.py --no-autorun --top-n 15 --hi-threshold 0.45
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from collections import Counter
from pathlib import Path
from statistics import median
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from common.io_utils import read_csv, read_json, write_csv, write_json, log  # noqa: E402
from common.relevance import score_paper  # noqa: E402
from common.config import CFG  # noqa: E402

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
DATA = ROOT / "data"
DECISIONS_DIR = DATA / "decisions"
DEDUP_DIR = DATA / "papers_dedup"
SCORES_DIR = DATA / "scores"
AGREEMENT_DIR = DATA / "agreement"
REPORTS_DIR = ROOT / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

OUT_CSV = DATA / "topics_seed_narrowed.csv"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
STOPWORDS = {
    "the", "a", "an", "of", "in", "for", "to", "and", "or", "is",
    "on", "at", "by", "with", "as", "its", "from", "via", "using",
    "based", "new", "large", "across", "over", "between", "more",
    "this", "that", "their", "we", "our", "how", "are", "were",
    "does", "do", "not", "no", "vs", "can", "be", "has", "have",
    "it", "into", "than", "about", "study", "paper", "approach",
    "toward", "towards", "when", "where", "what", "which", "who",
    "without", "beyond", "through", "under", "up", "out", "whether",
}

# Relevance tiers
HI_THRESHOLD_DEFAULT = 0.45   # hi-relevance papers: clear primary-keyword hit
MID_THRESHOLD = 0.30          # mid-relevance papers
LO_THRESHOLD = 0.25           # lo-relevance: often single noisy keyword match

# Variant generation
MAX_VARIANTS_PER_TOPIC = 5
MIN_ANCHOR_COUNT = 2          # anchor term must appear in >= N hi papers
MAX_ANCHOR_TERMS = 6          # consider top-6 anchor terms per topic

# Composite weighting for variant ranking
W_REL_PURITY = 0.35
W_CITATION = 0.15
W_ARTIFACT = 0.15
W_NIW = 0.10
W_EB1A = 0.10
W_CAREER = 0.15


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _split(s: str, sep: str) -> list[str]:
    return [t.strip() for t in (s or "").split(sep) if t.strip()]


def _kws(s: str) -> list[str]:
    return _split(s, "|")


def _syns(s: str) -> list[str]:
    return _split(s, ";")


def _negs(s: str) -> list[str]:
    return _split(s, ";")


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").lower().strip())


def _tokenise(title: str) -> list[str]:
    """Lower-case, strip punctuation (keep hyphens), split on whitespace."""
    t = re.sub(r"[^\w\s-]", " ", title.lower())
    return [w for w in t.split() if w not in STOPWORDS and len(w) > 2]


def _float(x: Any, default: float = 0.0) -> float:
    try:
        return float(x)
    except Exception:
        return default


def _int(x: Any, default: int = 0) -> int:
    try:
        return int(float(x))
    except Exception:
        return default


# ---------------------------------------------------------------------------
# Step 1 — Load input data
# ---------------------------------------------------------------------------

def load_narrow_topics(decisions_dir: Path, dedup_dir: Path,
                       scores_dir: Path, topics_csv: Path) -> list[dict[str, Any]]:
    """Return list of NARROW topic records, enriched with papers and scores."""
    seed_rows = read_csv(topics_csv)
    seed_map = {r["topic_id"]: r for r in seed_rows}

    results = []
    decisions_csv = decisions_dir / "decisions.csv"
    if not decisions_csv.exists():
        log("11_narrow", "decisions.csv not found — run 08_confidence_gate first")
        return []

    rows = read_csv(decisions_csv)
    for row in rows:
        if row.get("final_decision") != "NARROW":
            continue
        tid = row["topic_id"]
        seed = seed_map.get(tid)
        if not seed:
            log("11_narrow", f"WARN: {tid} in decisions but not in seed CSV — skipping")
            continue

        papers = []
        dedup_f = dedup_dir / f"{tid}.csv"
        if dedup_f.exists():
            papers = read_csv(dedup_f)

        score_json = read_json(scores_dir / f"{tid}.json", {})
        agree_json = read_json(ROOT / "data" / "agreement" / f"{tid}.json", {})
        decision_json = read_json(decisions_dir / f"{tid}.json", {})

        results.append({
            "seed": seed,
            "decision_row": row,
            "decision_json": decision_json,
            "score_json": score_json,
            "agree_json": agree_json,
            "papers": papers,
        })
        log("11_narrow", f"Loaded {tid}: {len(papers)} papers, decision=NARROW")

    return results


# ---------------------------------------------------------------------------
# Step 2 — Term extraction
# ---------------------------------------------------------------------------

def split_by_tier(papers: list[dict], hi_threshold: float) -> tuple[list, list, list]:
    """Split papers into hi / mid / lo relevance tiers."""
    hi, mid, lo = [], [], []
    for p in papers:
        s = _float(p.get("relevance_score", 0))
        if s >= hi_threshold:
            hi.append(p)
        elif s >= MID_THRESHOLD:
            mid.append(p)
        else:
            lo.append(p)
    return hi, mid, lo


def extract_title_ngrams(papers: list[dict],
                         n_range: tuple[int, int] = (2, 4),
                         min_count: int = MIN_ANCHOR_COUNT) -> list[str]:
    """
    Extract frequent n-grams from paper titles.
    Returns grams ordered by frequency, filtered to min_count occurrences.
    """
    counter: Counter = Counter()
    for p in papers:
        tokens = _tokenise(p.get("title", ""))
        for n in range(n_range[0], n_range[1] + 1):
            for i in range(len(tokens) - n + 1):
                gram = " ".join(tokens[i : i + n])
                counter[gram] += 1
    return [gram for gram, cnt in counter.most_common(MAX_ANCHOR_TERMS * 4)
            if cnt >= min_count]


def find_noisy_keywords(hi: list[dict], lo: list[dict],
                        secondaries: list[str]) -> list[str]:
    """
    Identify secondary keywords that match predominantly in lo-relevance papers.
    A keyword is "noisy" if:
      lo_matches >= hi_matches * 2  AND  lo_matches >= 2
    """
    noisy = []
    for kw in secondaries:
        kw_l = kw.lower()
        hi_m = sum(
            1 for p in hi
            if kw_l in _norm(p.get("title", ""))
            or kw_l in (p.get("matched_keywords", "") or "").lower()
        )
        lo_m = sum(
            1 for p in lo
            if kw_l in _norm(p.get("title", ""))
            or kw_l in (p.get("matched_keywords", "") or "").lower()
        )
        if lo_m >= 2 and lo_m >= hi_m * 2:
            noisy.append(kw)
            log("11_narrow",
                f"  noisy keyword '{kw}': hi_matches={hi_m}, lo_matches={lo_m}")
    return noisy


def find_synonym_anchors(hi: list[dict], synonyms: list[str]) -> list[str]:
    """Return synonyms that actually appear in hi-paper titles (best candidates to promote)."""
    found = []
    for syn in synonyms:
        syn_l = syn.lower()
        if any(syn_l in _norm(p.get("title", "")) for p in hi):
            found.append(syn)
    return found


# ---------------------------------------------------------------------------
# Step 3 — Variant generation (strategy A/B/C/D)
# ---------------------------------------------------------------------------

_VARIANT_COUNTER: dict[str, int] = {}


def _next_id(parent_id: str) -> str:
    _VARIANT_COUNTER[parent_id] = _VARIANT_COUNTER.get(parent_id, 0) + 1
    return f"{parent_id}_N{_VARIANT_COUNTER[parent_id]}"


def _make_variant(parent: dict, topic_id: str, title: str, keywords: str,
                  synonyms: str, negative_keywords: str,
                  narrowing_type: str, narrowing_note: str) -> dict:
    seed = parent["seed"]
    return {
        # Standard pipeline columns
        "topic_id": topic_id,
        "title": title,
        "category": seed["category"],
        "keywords": keywords,
        "synonyms": synonyms,
        "negative_keywords": negative_keywords,
        "target_artifact": seed["target_artifact"],
        "prelim_priority": seed["prelim_priority"],
        # Provenance (ignored by pipeline; useful for report)
        "parent_topic_id": seed["topic_id"],
        "narrowing_type": narrowing_type,
        "narrowing_note": narrowing_note,
    }


def _anchors_overlap(anchor: str, primary: str) -> bool:
    """Return True if the anchor shares too many words with the primary keyword."""
    a_words = set(_tokenise(anchor))
    p_words = set(_tokenise(primary))
    if not a_words:
        return True
    overlap = a_words & p_words
    # Reject if more than 25% of anchor words are already in primary (stricter than before)
    return len(overlap) / len(a_words) > 0.25


# Generic n-grams that appear in virtually all LLM papers — useless as anchors
_GENERIC_ANCHORS = {
    "language models", "large language", "large language models",
    "language model", "llm evaluation", "llm evaluations",
    "language model evaluation", "natural language", "pre-trained",
    "based approach", "proposed method", "empirical study",
    "benchmark evaluation", "evaluation benchmark",
}


def generate_variants(parent: dict, hi: list[dict], lo: list[dict],
                      hi_threshold: float) -> list[dict]:
    """
    Generate up to MAX_VARIANTS_PER_TOPIC narrowed variants for one NARROW topic.

    Strategies (applied in order; stops at MAX_VARIANTS_PER_TOPIC):
      A) primary-anchor: compound primary keyword + most frequent hi-paper anchor term
      B) noise-pruned:   drop noisy secondary keywords; add them to negative_keywords
      C) synonym-promoted: promote a synonym (>=4 chars) that appears in hi papers to primary
      D) compound-pivot: pivot to a frequent hi-paper bigram/trigram as new primary
    """
    seed = parent["seed"]
    kws = _kws(seed["keywords"])
    syns = _syns(seed["synonyms"])
    negs = _negs(seed["negative_keywords"])

    primary = kws[0] if kws else ""
    secondaries = kws[1:]

    all_papers = parent["papers"]
    log("11_narrow",
        f"  {seed['topic_id']}: hi={len(hi)}, lo={len(lo)}, papers={len(all_papers)}")

    anchor_terms = extract_title_ngrams(hi, n_range=(2, 4), min_count=MIN_ANCHOR_COUNT)
    # Filter: skip anchors that:
    #   (a) are essentially the primary keyword or a substring of it
    #   (b) have significant word overlap with the primary (degenerate compounds)
    #   (c) are known-generic ML terms (appear in almost every LLM paper)
    #   (d) appear in >70% of hi papers (too ubiquitous to be a narrowing signal)
    #   (e) are shorter than 8 chars
    primary_l = primary.lower()
    n_hi = max(1, len(hi))
    raw_counter: Counter = Counter()
    for p in hi:
        tokens = _tokenise(p.get("title", ""))
        for n in range(2, 5):
            for i in range(len(tokens) - n + 1):
                raw_counter[" ".join(tokens[i:i+n])] += 1
    too_frequent = {g for g, cnt in raw_counter.items() if cnt / n_hi > 0.70}

    anchor_terms = [
        a for a in anchor_terms
        if not _anchors_overlap(a, primary)
        and primary_l not in a
        and a not in primary_l
        and a not in _GENERIC_ANCHORS
        and a not in too_frequent
        and len(a) >= 8  # at least 8 chars to avoid single-word anchors
    ][:MAX_ANCHOR_TERMS]

    noisy_sec = find_noisy_keywords(hi, lo, secondaries)
    clean_sec = [k for k in secondaries if k not in noisy_sec]
    syn_anchors = find_synonym_anchors(hi, syns)

    variants: list[dict] = []

    # ---- Strategy A: primary-anchor variants ---------------------------------
    for anchor in anchor_terms:
        if len(variants) >= MAX_VARIANTS_PER_TOPIC:
            break
        # Skip if anchor already fully contained in primary or vice-versa
        if _norm(anchor) == _norm(primary):
            continue
        # Compound: "primary anchor"
        compound = f"{primary} {anchor}"
        new_kws = [compound] + clean_sec[:2]
        new_negs = negs + [n for n in noisy_sec if n not in negs]
        tid = _next_id(seed["topic_id"])
        variants.append(_make_variant(
            parent, tid,
            title=f"{seed['title']} — focused on {anchor}",
            keywords="|".join(new_kws),
            synonyms=seed["synonyms"],
            negative_keywords=";".join(new_negs),
            narrowing_type="primary_anchor",
            narrowing_note=f"compound primary='{compound}'; dropped noisy={noisy_sec}",
        ))

    # ---- Strategy B: noise-pruned -------------------------------------------
    if len(variants) < MAX_VARIANTS_PER_TOPIC and noisy_sec:
        new_kws = [primary] + clean_sec
        new_negs = negs + [n for n in noisy_sec if n not in negs]
        tid = _next_id(seed["topic_id"])
        variants.append(_make_variant(
            parent, tid,
            title=f"{seed['title']} — noise-pruned",
            keywords="|".join(new_kws) if new_kws else primary,
            synonyms=seed["synonyms"],
            negative_keywords=";".join(new_negs),
            narrowing_type="noise_pruned",
            narrowing_note=f"removed noisy secondaries={noisy_sec}; added to negatives",
        ))

    # ---- Strategy C: synonym-promoted ----------------------------------------
    for syn in syn_anchors:
        if len(variants) >= MAX_VARIANTS_PER_TOPIC:
            break
        # Skip very short synonyms (likely abbreviations that match non-domain text)
        if len(syn) < 5:
            continue
        # Don't duplicate if already have a variant with same effective primary
        if any(_norm(syn) in _norm(v["keywords"].split("|")[0]) for v in variants):
            continue
        new_kws = [syn, primary] + clean_sec[:1]
        new_negs = negs + [n for n in noisy_sec if n not in negs]
        tid = _next_id(seed["topic_id"])
        variants.append(_make_variant(
            parent, tid,
            title=f"{seed['title']} — via {syn}",
            keywords="|".join(new_kws),
            synonyms="|".join([k for k in (clean_sec + syns) if k != syn][:6]),
            negative_keywords=";".join(new_negs),
            narrowing_type="synonym_promoted",
            narrowing_note=f"promoted synonym '{syn}' to primary",
        ))

    # ---- Strategy D: compound-pivot (anchor as new primary) ------------------
    for anchor in anchor_terms:
        if len(variants) >= MAX_VARIANTS_PER_TOPIC:
            break
        # Only pivot if anchor is meaningfully different from primary
        if _norm(anchor) in {_norm(v["keywords"].split("|")[0]) for v in variants}:
            continue
        if len(anchor.split()) < 2:
            continue
        new_kws = [anchor, primary] + clean_sec[:1]
        new_negs = negs + [n for n in noisy_sec if n not in negs]
        tid = _next_id(seed["topic_id"])
        variants.append(_make_variant(
            parent, tid,
            title=f"{seed['title']} — pivoted to '{anchor}'",
            keywords="|".join(new_kws),
            synonyms=seed["synonyms"],
            negative_keywords=";".join(new_negs),
            narrowing_type="compound_pivot",
            narrowing_note=f"pivoted primary to hi-paper anchor '{anchor}'",
        ))

    # ---- Fallback: if no variants generated, create a minimal noise-pruned ---
    if not variants:
        tid = _next_id(seed["topic_id"])
        new_negs = negs + [n for n in noisy_sec if n not in negs]
        variants.append(_make_variant(
            parent, tid,
            title=f"{seed['title']} — tightened",
            keywords=seed["keywords"],
            synonyms=seed["synonyms"],
            negative_keywords=";".join(new_negs) if new_negs else seed["negative_keywords"],
            narrowing_type="tightened_negatives",
            narrowing_note="fallback: added noisy terms to negative_keywords only",
        ))

    return variants[:MAX_VARIANTS_PER_TOPIC]


# ---------------------------------------------------------------------------
# Step 4 — Signal simulation and estimation
# ---------------------------------------------------------------------------

def simulate_relevance(papers: list[dict], variant_topic: dict,
                       threshold: float) -> list[dict]:
    """
    Run relevance scoring using the variant's keyword/synonym definition
    against the existing paper corpus. Returns papers that pass the threshold.
    """
    # Build a topic dict matching the relevance.score_paper() interface
    sim_topic = {
        "keywords": variant_topic["keywords"],
        "synonyms": variant_topic["synonyms"],
        "negative_keywords": variant_topic["negative_keywords"],
    }
    passing = []
    for p in papers:
        rel, matched, reason = score_paper(p, sim_topic)
        if rel >= threshold:
            enriched = dict(p)
            enriched["_sim_relevance"] = rel
            enriched["_sim_matched"] = matched
            passing.append(enriched)
    return passing


def estimate_signals(passing: list[dict], parent: dict,
                     hi_threshold: float) -> dict[str, Any]:
    """
    Estimate pipeline signals for a variant, based on its simulated paper set
    and the parent topic's original scores.
    """
    parent_score = parent.get("score_json", {})
    parent_decision = parent.get("decision_json", {})

    # Relevance purity: median relevance of simulated passing papers
    rels = sorted(_float(p.get("_sim_relevance", 0)) for p in passing)
    n = len(rels)
    if n == 0:
        est_purity = 0.0
    elif n == 1:
        est_purity = rels[0]
    else:
        mid = n // 2
        est_purity = round((rels[mid] if n % 2 else (rels[mid - 1] + rels[mid]) / 2), 3)

    # Citation signal: based on citations of passing papers
    cits = sorted(_int(p.get("citations", 0)) for p in passing if p.get("citations"))
    top_cit = max(cits) if cits else 0
    if top_cit >= 200 or (cits and len([c for c in cits if c >= 50]) >= 3):
        est_cit = 4
    elif top_cit >= 50 or (cits and len([c for c in cits if c >= 10]) >= 5):
        est_cit = 3
    elif top_cit >= 20 or len(cits) >= 3:
        est_cit = 2
    elif cits:
        est_cit = 1
    else:
        est_cit = 0

    # Artifact opportunity: maintain parent signal, bump if purity improves
    parent_art = _int(parent_score.get("artifact", {}).get("artifact_opportunity_0to5", 0))
    purity_gain = max(0.0, est_purity - _float(parent_decision.get("relevance_purity", 0.25)))
    if purity_gain >= 0.15 and parent_art >= 2:
        est_art = min(5, parent_art + 1)  # purity improvement unlocks more signal
    else:
        est_art = parent_art

    # NIW/EB1A/Career: inherit from parent (same research category and keywords)
    est_niw = _int(parent_score.get("niw_0to5", 0))
    est_eb1a = _int(parent_score.get("eb1a_0to5", 0))
    est_career = _int(parent_score.get("career_0to5", 0))

    # Saturation: narrower topic → lower saturation expected
    parent_sat = _int(parent_score.get("saturation", {}).get("saturation_score_0to5", 3))
    est_sat = max(0, parent_sat - 1) if n < len(parent.get("papers", [])) * 0.6 else parent_sat

    # Evidence quality: based on simulated passing paper count
    est_eq = min(4, max(1, (1 if n >= 5 else 0) + (1 if n >= 10 else 0)
                         + (1 if est_purity >= 0.4 else 0)
                         + (1 if top_cit >= 50 else 0)))

    # Novelty risk: LOW if < 5 hi papers (underexplored), MED if 5-20, HIGH if > 20
    hi_count = sum(1 for p in passing if _float(p.get("_sim_relevance", 0)) >= hi_threshold)
    if hi_count <= 4:
        novelty_risk = "LOW"
    elif hi_count <= 15:
        novelty_risk = "MEDIUM"
    else:
        novelty_risk = "HIGH"

    # Composite score for ranking.
    # Note: primary-anchor and compound-pivot variants may show est_purity=0 on the
    # *existing* corpus because the compound phrase doesn't appear in current papers.
    # That is expected — on a fresh pipeline run they'll pull focused papers.
    # We credit them with the parent's purity as a conservative floor so they're
    # not completely invisible in the ranking.
    parent_purity = _float(parent_decision.get("relevance_purity", 0.25))
    effective_purity = max(est_purity, parent_purity * 0.8)  # conservative floor

    composite = (
        W_REL_PURITY * effective_purity
        + W_CITATION * (est_cit / 5.0)
        + W_ARTIFACT * (est_art / 5.0)
        + W_NIW * (est_niw / 5.0)
        + W_EB1A * (est_eb1a / 5.0)
        + W_CAREER * (est_career / 5.0)
    )

    return {
        "est_relevance_purity": round(est_purity, 3),
        "est_kept_papers": n,
        "est_hi_papers": hi_count,
        "est_citation_signal": est_cit,
        "est_artifact": est_art,
        "est_saturation": est_sat,
        "est_evidence_quality": est_eq,
        "est_niw": est_niw,
        "est_eb1a": est_eb1a,
        "est_career": est_career,
        "est_novelty_risk": novelty_risk,
        "est_exec_feasibility": "HIGH",  # all use same public APIs
        "composite_score": round(composite, 4),
        "purity_gain_vs_parent": round(purity_gain, 3),
    }


# ---------------------------------------------------------------------------
# Step 5 — Full pipeline per topic
# ---------------------------------------------------------------------------

def process_topic(parent: dict, hi_threshold: float,
                  rel_threshold: float) -> list[dict]:
    """
    Run the full narrowing pipeline for one NARROW topic.
    Returns list of variant dicts, each enriched with estimated signals.
    """
    seed = parent["seed"]
    tid = seed["topic_id"]
    all_papers = parent["papers"]

    log("11_narrow", f"Processing {tid}: {seed['title']}")

    hi, mid, lo = split_by_tier(all_papers, hi_threshold)

    # Generate candidate variants
    variants = generate_variants(parent, hi, lo, hi_threshold)
    log("11_narrow", f"  Generated {len(variants)} variants for {tid}")

    # Simulate relevance and estimate signals for each variant
    enriched = []
    for v in variants:
        passing = simulate_relevance(all_papers, v, rel_threshold)
        signals = estimate_signals(passing, parent, hi_threshold)
        v.update(signals)
        enriched.append(v)
        log("11_narrow",
            f"  {v['topic_id']}: purity={signals['est_relevance_purity']}, "
            f"kept={signals['est_kept_papers']}, "
            f"composite={signals['composite_score']}, "
            f"type={v['narrowing_type']}")

    return enriched


# ---------------------------------------------------------------------------
# Step 6 — Select top N
# ---------------------------------------------------------------------------

def select_top_variants(all_variants: list[dict], top_n: int,
                        max_per_parent: int = 2) -> list[dict]:
    """
    Rank all variants by composite_score (desc) and select top_n.
    Tie-break: higher est_relevance_purity → higher est_citation_signal → strategy priority.
    Diversity constraint: at most max_per_parent variants per parent topic.
    Within each parent, prefer the highest-scoring *distinct* narrowing type.
    """
    # Strategy priority for tie-breaking (lower = preferred)
    STRATEGY_PRIORITY = {
        "noise_pruned": 0,
        "synonym_promoted": 1,
        "primary_anchor": 2,
        "compound_pivot": 3,
        "tightened_negatives": 4,
    }

    ranked = sorted(
        all_variants,
        key=lambda v: (
            -v["composite_score"],
            -v["est_relevance_purity"],
            -v["est_citation_signal"],
            STRATEGY_PRIORITY.get(v["narrowing_type"], 9),
        ),
    )

    selected: list[dict] = []
    parent_counts: dict[str, int] = {}
    seen_types: dict[str, set] = {}  # parent_id → {narrowing_types already selected}

    for v in ranked:
        pid = v["parent_topic_id"]
        if parent_counts.get(pid, 0) >= max_per_parent:
            continue
        # Prefer different narrowing types within a parent (avoid 5 identical primary_anchor)
        if v["narrowing_type"] in seen_types.get(pid, set()) and parent_counts.get(pid, 0) >= 1:
            continue
        selected.append(v)
        parent_counts[pid] = parent_counts.get(pid, 0) + 1
        seen_types.setdefault(pid, set()).add(v["narrowing_type"])
        if len(selected) >= top_n:
            break

    # If we have room and some parents are under-represented, fill remaining slots
    if len(selected) < top_n:
        selected_ids = {v["topic_id"] for v in selected}
        for v in ranked:
            if v["topic_id"] in selected_ids:
                continue
            pid = v["parent_topic_id"]
            if parent_counts.get(pid, 0) >= max_per_parent:
                continue
            selected.append(v)
            parent_counts[pid] = parent_counts.get(pid, 0) + 1
            selected_ids.add(v["topic_id"])
            if len(selected) >= top_n:
                break

    log("11_narrow", f"Selected top {len(selected)} variants from {len(all_variants)} candidates")
    for v in selected:
        log("11_narrow",
            f"  → {v['topic_id']} (parent={v['parent_topic_id']}) "
            f"purity={v['est_relevance_purity']} composite={v['composite_score']}")
    return selected


# ---------------------------------------------------------------------------
# Step 7 — Write outputs
# ---------------------------------------------------------------------------

# Columns in the same order as topics_seed.csv (pipeline-compatible) + provenance
_CSV_FIELDNAMES = [
    "topic_id", "title", "category", "keywords", "synonyms",
    "negative_keywords", "target_artifact", "prelim_priority",
    # provenance / estimation (ignored by pipeline, used in report)
    "parent_topic_id", "narrowing_type", "narrowing_note",
    "est_relevance_purity", "est_kept_papers", "est_hi_papers",
    "est_citation_signal", "est_artifact", "est_saturation",
    "est_evidence_quality", "est_niw", "est_eb1a", "est_career",
    "est_novelty_risk", "est_exec_feasibility", "composite_score",
    "purity_gain_vs_parent",
]


def write_narrowed_csv(selected: list[dict]) -> None:
    write_csv(OUT_CSV, selected, header=_CSV_FIELDNAMES)
    log("11_narrow", f"Wrote {OUT_CSV}")


def write_narrowing_report(selected: list[dict], all_variants: list[dict],
                           narrow_topics: list[dict]) -> None:
    """Write reports/narrowing_report.md."""
    path = REPORTS_DIR / "narrowing_report.md"
    lines = []
    a = lines.append

    ts = time.strftime("%Y-%m-%d %H:%M:%S")
    a(f"# Narrowing Report — {ts}")
    a("")
    a("## Overview")
    a("")
    a(f"- Parent NARROW topics processed: **{len(narrow_topics)}**")
    a(f"- Total candidate variants generated: **{len(all_variants)}**")
    a(f"- Variants selected for re-run: **{len(selected)}**")
    a(f"- Selection criterion: top by composite score "
      f"(w_purity={W_REL_PURITY}, w_cit={W_CITATION}, w_art={W_ARTIFACT}, "
      f"w_niw={W_NIW}, w_eb1a={W_EB1A}, w_career={W_CAREER})")
    a("")

    a("## Selected Variants (ranked by composite score)")
    a("")
    a("| # | Variant ID | Parent | Narrowing type | Est. purity | Purity gain | "
      "Est. kept | Est. cit | Est. art | Composite |")
    a("|---|------------|--------|----------------|-------------|-------------|"
      "-----------|----------|----------|-----------|")
    for i, v in enumerate(selected, 1):
        a(f"| {i} | {v['topic_id']} | {v['parent_topic_id']} | {v['narrowing_type']} "
          f"| {v['est_relevance_purity']:.3f} | {v['purity_gain_vs_parent']:+.3f} "
          f"| {v['est_kept_papers']} | {v['est_citation_signal']} "
          f"| {v['est_artifact']} | {v['composite_score']:.4f} |")
    a("")

    a("## Per-Parent Analysis")
    a("")
    parent_ids = sorted({v["parent_topic_id"] for v in selected})
    all_by_parent: dict[str, list[dict]] = {}
    for v in all_variants:
        all_by_parent.setdefault(v["parent_topic_id"], []).append(v)

    for pid in sorted({p["seed"]["topic_id"] for p in narrow_topics}):
        parent_data = next(p for p in narrow_topics if p["seed"]["topic_id"] == pid)
        seed = parent_data["seed"]
        p_purity = _float(parent_data["decision_json"].get("relevance_purity", 0))
        p_art = _int(parent_data["score_json"].get("artifact", {}).get("artifact_opportunity_0to5", 0))
        p_cit = _int(parent_data["score_json"].get("citation_signal_0to5", 0))
        variants_all = all_by_parent.get(pid, [])
        variants_sel = [v for v in selected if v["parent_topic_id"] == pid]

        a(f"### {pid}: {seed['title']}")
        a("")
        a(f"**Original signals**: purity={p_purity}, citation={p_cit}, artifact={p_art}")
        a(f"**Original keywords**: `{seed['keywords']}`")
        a(f"**Original synonyms**: `{seed['synonyms']}`")
        a(f"**Original negatives**: `{seed['negative_keywords']}`")
        a(f"**Reason NARROW**: {parent_data['decision_json'].get('reasoning_summary', 'N/A')}")
        a("")
        a(f"Candidates generated: {len(variants_all)} | Selected: {len(variants_sel)}")
        a("")

        if variants_all:
            a("| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |")
            a("|------------|------|--------------------------|-------------|-------------|------|")
            for v in sorted(variants_all, key=lambda x: -x["composite_score"]):
                kw_short = v["keywords"][:60] + ("…" if len(v["keywords"]) > 60 else "")
                sel_marker = "✓" if v in variants_sel else ""
                a(f"| {v['topic_id']} | {v['narrowing_type']} | `{kw_short}` "
                  f"| {v['est_relevance_purity']:.3f} | {v['purity_gain_vs_parent']:+.3f} "
                  f"| {sel_marker} |")
            a("")
            a("**Selected variant details:**")
            a("")
            for v in variants_sel:
                a(f"#### {v['topic_id']} — {v['narrowing_type']}")
                a(f"- **Title**: {v['title']}")
                a(f"- **Keywords**: `{v['keywords']}`")
                a(f"- **Synonyms**: `{v['synonyms']}`")
                a(f"- **Negatives**: `{v['negative_keywords']}`")
                a(f"- **Narrowing note**: {v['narrowing_note']}")
                a(f"- **Est. relevance purity**: {v['est_relevance_purity']:.3f} "
                  f"(parent: {p_purity:.3f}, gain: {v['purity_gain_vs_parent']:+.3f})")
                a(f"- **Est. kept papers**: {v['est_kept_papers']} "
                  f"(hi-relevance: {v['est_hi_papers']})")
                a(f"- **Est. citation_signal**: {v['est_citation_signal']}/5")
                a(f"- **Est. artifact_opportunity**: {v['est_artifact']}/5")
                a(f"- **Est. NIW/EB1A/Career**: {v['est_niw']}/{v['est_eb1a']}/{v['est_career']}")
                a(f"- **Est. novelty risk**: {v['est_novelty_risk']}")
                a(f"- **Composite score**: {v['composite_score']:.4f}")
                a("")
        else:
            a("*(no variants generated — check dedup data)*")
            a("")

    a("## Notes")
    a("")
    a("- All estimates are simulated against the *existing* dedup paper corpus.")
    a("  A full re-run with `10_run_pipeline.py` will re-collect evidence with the")
    a("  narrowed queries and produce authoritative scores.")
    a("- Variants with `est_relevance_purity < 0.25` are still included if the")
    a("  composite score is competitive; they may benefit from expanded evidence.")
    a("- GO gate still requires: purity>=0.4, artifact>=3, citation>=3, overall>=14,")
    a("  venue>=2, n_reviews>0, reviewer dec_score>=2.0 after the real pipeline run.")

    path.write_text("\n".join(lines), encoding="utf-8")
    log("11_narrow", f"Wrote {path}")


# ---------------------------------------------------------------------------
# Step 8 — Auto-run pipeline
# ---------------------------------------------------------------------------

def autorun_pipeline(topics_csv: str, venues_csv: str, max_rounds: int = 3) -> int:
    """Launch 10_run_pipeline.py on the narrowed topics CSV."""
    import subprocess
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "10_run_pipeline.py"),
        "--topics", topics_csv,
        "--venues", venues_csv,
        "--max-rounds", str(max_rounds),
    ]
    log("11_narrow", f"autorun: {' '.join(cmd)}")
    print(f"\n{'='*60}")
    print(f"Auto-running pipeline on narrowed topics:")
    print(f"  {' '.join(cmd)}")
    print(f"{'='*60}\n")
    result = subprocess.run(cmd)
    return result.returncode


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--no-autorun", action="store_true",
                    help="Skip auto-running the pipeline after generating the CSV")
    ap.add_argument("--top-n", type=int, default=12,
                    help="Maximum number of narrowed variants to select (default: 12)")
    ap.add_argument("--hi-threshold", type=float, default=HI_THRESHOLD_DEFAULT,
                    help=f"Relevance score threshold for 'hi-relevance' papers (default: {HI_THRESHOLD_DEFAULT})")
    ap.add_argument("--topics", default=str(DATA / "topics_seed.csv"),
                    help="Parent topics seed CSV (default: data/topics_seed.csv)")
    ap.add_argument("--venues", default=str(DATA / "venues_seed.csv"),
                    help="Venues seed CSV (passed to pipeline, default: data/venues_seed.csv)")
    ap.add_argument("--max-rounds", type=int, default=3,
                    help="Max pipeline rounds for the auto-run (default: 3)")
    ap.add_argument("--max-per-parent", type=int, default=2,
                    help="Max variants selected per parent topic (default: 2, ensures diversity)")
    args = ap.parse_args(argv)

    rel_threshold = float(CFG.get("relevance_min", 0.20))
    log("11_narrow",
        f"START top_n={args.top_n}, hi_threshold={args.hi_threshold}, "
        f"rel_threshold={rel_threshold}, autorun={not args.no_autorun}")

    # ---- Load NARROW topics
    narrow_topics = load_narrow_topics(
        DECISIONS_DIR, DEDUP_DIR, SCORES_DIR, Path(args.topics)
    )
    if not narrow_topics:
        print("No NARROW topics found. Run 08_confidence_gate.py first.")
        return 1

    print(f"Found {len(narrow_topics)} NARROW topics: "
          f"{[p['seed']['topic_id'] for p in narrow_topics]}")

    # ---- Generate variants
    all_variants: list[dict] = []
    for parent in narrow_topics:
        variants = process_topic(parent, args.hi_threshold, rel_threshold)
        all_variants.extend(variants)

    print(f"\nGenerated {len(all_variants)} candidate variants total.")

    if not all_variants:
        print("No variants generated. Check dedup data exists in data/papers_dedup/")
        return 1

    # ---- Select top N (with diversity across parent topics)
    selected = select_top_variants(all_variants, args.top_n, args.max_per_parent)
    print(f"Selected top {len(selected)} variants.")

    # ---- Write outputs
    write_narrowed_csv(selected)
    write_narrowing_report(selected, all_variants, narrow_topics)

    print(f"\nOutputs:")
    print(f"  Narrowed topics CSV: {OUT_CSV}")
    print(f"  Narrowing report:    {REPORTS_DIR / 'narrowing_report.md'}")

    # ---- Print summary table
    print(f"\n{'':=<80}")
    print(f"{'Variant ID':<14} {'Parent':<8} {'Type':<18} {'Est.Purity':>10} "
          f"{'Gain':>7} {'Kept':>5} {'Composite':>10}")
    print(f"{'-'*14} {'-'*8} {'-'*18} {'-'*10} {'-'*7} {'-'*5} {'-'*10}")
    for v in selected:
        print(f"{v['topic_id']:<14} {v['parent_topic_id']:<8} {v['narrowing_type']:<18} "
              f"{v['est_relevance_purity']:>10.3f} {v['purity_gain_vs_parent']:>+7.3f} "
              f"{v['est_kept_papers']:>5} {v['composite_score']:>10.4f}")
    print(f"{'':=<80}")

    # ---- Auto-run pipeline
    if not args.no_autorun:
        rc = autorun_pipeline(str(OUT_CSV), args.venues, args.max_rounds)
        if rc != 0:
            log("11_narrow", f"pipeline autorun exited with code {rc}")
            return rc
    else:
        print(f"\nSkipping auto-run (--no-autorun). To run manually:")
        print(f"  python scripts/10_run_pipeline.py --topics {OUT_CSV} "
              f"--venues {args.venues} --max-rounds {args.max_rounds}")

    log("11_narrow", "DONE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
