"""
12_detect_existing_work.py

For each topic, detect existing work that overlaps with the proposed contribution.

Sources (pre-collected — no new API calls):
  1. data/papers_dedup/<id>.csv              — primary corpus (scored papers)
  2. data/evidence/<id>/github.json          — GitHub repos
  3. data/evidence/<id>/huggingface.json     — HuggingFace datasets/spaces
  4. data/evidence/<id>/paperswithcode.json  — Papers With Code tasks/datasets

Overlap classes:
  DIRECT_OVERLAP  — existing work covers same contribution type AND same research question
  PARTIAL_OVERLAP — same research area, different artifact type or narrower/broader scope
  ADJACENT        — same broad domain; useful context but not blocking
  NOT_RELEVANT    — below relevance threshold (excluded from output)

Paper vs Artifact overlap distinction
--------------------------------------
This module separately tracks *peer-reviewed / paper* overlap from
*artifact* overlap (GitHub repos, HuggingFace datasets, PWC entries).

  peer_reviewed_direct_overlap — at least one DIRECT paper overlap
  artifact_direct_overlap      — at least one DIRECT GitHub/HF/PWC artifact

A topic can still be publishable if artifact overlap is high but paper overlap is
absent, provided the proposed contribution is clearly differentiated (e.g. peer-
reviewed protocol, domain-specific focus, systematic robustness evaluation).

Gate triggers (written to data/existing_work/<topic_id>.json):
  go_blocked = True
      IF high_peer_reviewed_overlap AND paper_diff_strength in {weak, none}
      OR  peer_reviewed_direct AND artifact_direct AND paper_diff_strength in {weak, none}
      OR  high_artifact_overlap AND artifact_diff_strength in {weak, none}
  requires_differentiator = True   → any DIRECT overlap or ≥2 PARTIAL papers
  artifact_differentiator_required → any artifact DIRECT overlap

Outputs:
  data/existing_work/<topic_id>.json                   — JSON summary consumed by 08_confidence_gate
  data/existing_work/<topic_id>_existing_work.csv      — flat CSV for human review
  reports/topic_reports/<topic_id>_existing_work.md    — per-topic markdown report
  data/existing_work/_summary.json                     — cross-topic summary consumed by 09
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.io_utils import read_csv, read_json, write_json, write_csv, log  # noqa: E402

# ── directories ───────────────────────────────────────────────────────────────
QUERIES_DIR  = ROOT / "data" / "queries"
DEDUP_DIR    = ROOT / "data" / "papers_dedup"
EVIDENCE_DIR = ROOT / "data" / "evidence"
OUT_DIR      = ROOT / "data" / "existing_work"
REPORTS_DIR  = ROOT / "reports" / "topic_reports"
OUT_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# ── classification thresholds ─────────────────────────────────────────────────
DIRECT_REL_THRESHOLD   = 0.65   # paper relevance ≥ this → DIRECT_OVERLAP (override via --min-direct-score)
PARTIAL_REL_THRESHOLD  = 0.35   # paper relevance in [0.35, DIRECT_REL_THRESHOLD) → PARTIAL_OVERLAP
ADJACENT_REL_THRESHOLD = 0.20   # paper relevance ≥ this → ADJACENT

GITHUB_DIRECT_STARS  = 100      # repo stars ≥ this + keyword + artifact kw → DIRECT candidate
GITHUB_PARTIAL_STARS = 30       # repo stars ≥ this + keyword → PARTIAL
HF_DIRECT_DOWNLOADS  = 100      # HF downloads ≥ this + keyword → DIRECT candidate
HF_PARTIAL_DOWNLOADS = 20       # HF downloads ≥ this + keyword → PARTIAL

HIGH_ARTIFACT_OVERLAP_THRESHOLD = 8   # artifact_direct_count ≥ this → high_artifact_overlap
HIGH_PAPER_OVERLAP_THRESHOLD    = 3   # direct_paper_count ≥ this → high_peer_reviewed_overlap

# generic repo patterns that are always ADJACENT, never DIRECT/PARTIAL
_COLLECTION_PATTERNS = re.compile(
    r"\bawesome\b|\bcollection\b|\bcurated\b|\bresources\b|\bcheatsheet\b",
    re.IGNORECASE,
)

CSV_FIELDS = [
    "topic_id", "source", "name", "url", "doi", "year", "venue",
    "contribution_type", "overlap_class",
    "relevance_score", "stars_or_downloads",
    "why_overlaps", "how_we_differ", "differentiator_strength",
]


# ── helpers ───────────────────────────────────────────────────────────────────

def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").lower().strip())


def _keywords(topic: dict[str, Any]) -> list[str]:
    """Return [primary, ...secondary] keywords (lowercased)."""
    return [k.strip().lower() for k in topic.get("keywords", "").split("|") if k.strip()]


def _synonyms(topic: dict[str, Any]) -> list[str]:
    return [s.strip().lower() for s in topic.get("synonyms", "").split(";") if s.strip()]


def _target_types(topic: dict[str, Any]) -> set[str]:
    """Parse target_artifact 'benchmark+tool' → {'benchmark', 'tool'}."""
    raw = topic.get("target_artifact", "")
    return {t.strip().lower() for t in raw.split("+") if t.strip()}


def _contribution_type(title: str, abstract: str = "") -> str:
    text = _norm(title + " " + (abstract or ""))
    if any(w in text for w in ["benchmark", "leaderboard", "challenge", "competition"]):
        return "benchmark"
    if any(w in text for w in ["dataset", "corpus", "collection", "annotations"]):
        return "dataset"
    if any(w in text for w in ["survey", "review", "overview", "taxonomy", "systematic mapping"]):
        return "survey"
    if any(w in text for w in ["framework", "toolkit", "library", "tool", "system", "platform"]):
        return "tool"
    if any(w in text for w in ["study", "analysis", "audit", "empirical", "investigation"]):
        return "empirical"
    if any(w in text for w in ["database", "repository", "catalogue", "catalog"]):
        return "database"
    return "paper"


_CONTRIB_ALIASES: dict[str, set[str]] = {
    "benchmark":   {"benchmark", "tool", "evaluation"},
    "dataset":     {"dataset", "database", "corpus"},
    "survey":      {"survey", "taxonomy", "paper", "review"},
    "tool":        {"tool", "framework", "benchmark"},
    "empirical":   {"empirical", "paper", "study", "analysis"},
    "database":    {"database", "dataset"},
    "paper":       {"paper", "empirical", "analysis"},
    "evaluation":  {"benchmark", "tool"},
}


def _artifact_matches(contrib_type: str, target_types: set[str]) -> bool:
    """True if contribution type is compatible with the topic's target artifact(s)."""
    if contrib_type in target_types:
        return True
    for alias_ct, aliases in _CONTRIB_ALIASES.items():
        if contrib_type == alias_ct and target_types & aliases:
            return True
    return False


def _keyword_in_text(keywords: list[str], text: str) -> bool:
    return any(k in text for k in keywords if k)


def _paper_differentiator_strength(n_direct_papers: int) -> str:
    """Peer-reviewed paper differentiator strength based on paper-sourced DIRECT_OVERLAP count."""
    if n_direct_papers == 0:
        return "strong"
    if n_direct_papers == 1:
        return "moderate"
    if n_direct_papers == 2:
        return "weak"
    return "none"


# Backward-compat alias (used by existing tests)
def _differentiator_strength(n_direct: int) -> str:
    return _paper_differentiator_strength(n_direct)


def _artifact_differentiator_strength(
    topic: dict[str, Any],
    peer_reviewed_direct: int,
    artifact_direct_count: int,
) -> str:
    """Estimate differentiator strength for artifact-overlap scenarios.

    When peer-reviewed paper overlap is absent/low but artifact (GitHub/HF/PWC) overlap
    is high, asks whether the topic has built-in differentiators from existing repos/datasets.

    The six key questions (per design spec):
    1. Peer-reviewed vs repo? → inherent advantage (always true for our proposed paper)
    2. Systematic protocol vs raw dataset? → check for benchmark/protocol/audit keywords
    3. Clinical/domain-specific vs general? → check for domain keywords
    4. LLM-judge-specific vs general injection? → topic-specific keyword check
    5. Robustness/evaluation vs data collection? → check for robustness/evaluation keywords
    6. Reproducible harness + paper? → always true for our proposed contribution
    """
    if artifact_direct_count == 0:
        return "strong"   # No artifact overlap at all

    topic_text = _norm(
        topic.get("title", "") + " " +
        topic.get("keywords", "") + " " +
        topic.get("category", "")
    )

    # Differentiating factors that make our work clearly distinct from existing repos/datasets
    domain_specific = any(w in topic_text for w in [
        "clinical", "medical", "healthcare", "health", "legal", "finance",
        "domain-specific", "clinical-domain", "biomedical",
    ])
    systematic_method = any(w in topic_text for w in [
        "benchmark", "protocol", "audit", "systematic", "reproducib",
        "harness", "methodology", "framework",
    ])
    eval_focused = any(w in topic_text for w in [
        "robustness", "sensitivity", "variance", "calibration", "bias",
        "evaluation methodology", "format sensitivity",
    ])

    n_diff = sum([domain_specific, systematic_method, eval_focused])

    # Case 1: No peer-reviewed paper directly overlaps — artifact-only scenario.
    # Our proposed peer-reviewed contribution is inherently differentiated from repos/datasets.
    if peer_reviewed_direct == 0:
        if n_diff >= 2:
            return "strong"    # Domain + method differentiators clear
        if n_diff >= 1:
            return "strong" if artifact_direct_count < 5 else "moderate"
        # Generic topic with many artifacts
        return "moderate" if artifact_direct_count < HIGH_ARTIFACT_OVERLAP_THRESHOLD else "weak"

    # Case 2: Low peer-reviewed overlap (1–2 papers)
    if peer_reviewed_direct <= 2:
        if n_diff >= 1:
            return "moderate"
        return "weak"

    # Case 3: High peer-reviewed overlap (≥3) — very hard to differentiate
    return "none"


def _why_paper(title: str, score: float, contrib_type: str, target_artifact: str,
               matched_kws: str) -> str:
    return (
        f"Relevance {score:.2f}: paper titled '{title[:100]}' contributes a "
        f"'{contrib_type}' matching target artifact '{target_artifact}'. "
        f"Matched keywords: {matched_kws or 'n/a'}."
    )


def _why_github(name: str, stars: int, desc: str, primary: str) -> str:
    return (
        f"GitHub repo '{name}' ({stars:,} stars) provides an implementation of "
        f"'{primary}'. Description: {desc[:120] or 'n/a'}."
    )


def _why_hf(hf_id: str, downloads: int, query: str) -> str:
    return (
        f"HuggingFace dataset/space '{hf_id}' ({downloads:,} downloads) matched "
        f"'{query}' — provides similar data/evaluation assets."
    )


def _how_we_differ(topic_title: str, narrowing_note: str = "") -> str:
    note = f" Narrowing note: {narrowing_note}." if narrowing_note else ""
    return (
        f"Our proposed work focuses specifically on '{topic_title}'.{note} "
        "Articulate a concrete contribution gap versus this existing work "
        "before promoting to GO (see §6 verification log)."
    )


# ── per-source classifiers ────────────────────────────────────────────────────

def classify_papers(
    topic: dict[str, Any],
    min_direct_score: float = DIRECT_REL_THRESHOLD,
) -> list[dict[str, Any]]:
    """Classify pre-scored papers from papers_dedup/<id>.csv.

    DIRECT_OVERLAP  ← relevance ≥ min_direct_score AND artifact-type match AND year ≥ 2022
    PARTIAL_OVERLAP ← relevance ≥ PARTIAL_REL_THRESHOLD (or high score without artifact match)
    ADJACENT        ← relevance ≥ ADJACENT_REL_THRESHOLD
    """
    tid = topic["topic_id"]
    csv_path = DEDUP_DIR / f"{tid}.csv"
    if not csv_path.exists():
        return []

    rows = read_csv(csv_path)
    target_types = _target_types(topic)
    topic_title = topic.get("title", "")
    narrowing_note = topic.get("narrowing_note", "")

    findings: list[dict[str, Any]] = []
    for r in rows:
        try:
            score = float(r.get("relevance_score") or 0)
        except (ValueError, TypeError):
            score = 0.0

        if score < ADJACENT_REL_THRESHOLD:
            continue

        title    = (r.get("title") or "").strip()
        abstract = (r.get("abstract") or "").strip()
        year_raw = r.get("year", "")
        try:
            year = int(year_raw)
        except (ValueError, TypeError):
            year = 0
        venue       = (r.get("venue") or r.get("journal") or "").strip()
        doi         = (r.get("doi") or "").strip()
        url_raw     = doi if doi.startswith("http") else (f"https://doi.org/{doi}" if doi else r.get("url", ""))
        matched_kws = (r.get("matched_keywords") or "").strip()

        contrib_type = _contribution_type(title, abstract)
        has_artifact_match = _artifact_matches(contrib_type, target_types)

        if score >= min_direct_score and has_artifact_match and year >= 2022:
            overlap = "DIRECT_OVERLAP"
        elif score >= PARTIAL_REL_THRESHOLD or (score >= min_direct_score and not has_artifact_match):
            overlap = "PARTIAL_OVERLAP"
        else:
            overlap = "ADJACENT"

        why = _why_paper(title, score, contrib_type, topic.get("target_artifact", "?"), matched_kws)
        how = _how_we_differ(topic_title, narrowing_note)
        findings.append({
            "topic_id": tid,
            "source": "paper",
            "name": title[:200],
            "url": url_raw[:300],
            "doi": doi[:120],
            "year": year,
            "venue": venue[:120],
            "contribution_type": contrib_type,
            "overlap_class": overlap,
            "relevance_score": round(score, 3),
            "stars_or_downloads": "",
            "why_overlaps": why,
            "how_we_differ": how,
            "differentiator_strength": "",   # back-filled after counting
        })
    return findings


def classify_github(topic: dict[str, Any]) -> list[dict[str, Any]]:
    """Classify GitHub repos from evidence/<id>/github.json."""
    tid = topic["topic_id"]
    gh_path = EVIDENCE_DIR / tid / "github.json"
    if not gh_path.exists():
        return []

    data = read_json(gh_path, [])
    kws = _keywords(topic)
    primary = kws[0] if kws else ""
    all_kws = kws + _synonyms(topic)
    topic_title = topic.get("title", "")
    narrowing_note = topic.get("narrowing_note", "")

    seen: set[str] = set()
    findings: list[dict[str, Any]] = []

    for entry in (data or []):
        results = entry.get("results", []) if isinstance(entry, dict) else []
        for repo in results:
            name = repo.get("name", "")
            if name in seen:
                continue
            seen.add(name)
            desc = _norm(repo.get("description", "") or "")
            stars = repo.get("stars", 0) or 0
            url = repo.get("url", "") or f"https://github.com/{name}"
            repo_text = _norm(name.replace("/", " ").replace("-", " ").replace("_", " ")) + " " + desc

            # Skip obvious collection repos
            if _COLLECTION_PATTERNS.search(desc) or "awesome" in name.lower():
                continue

            # Must contain primary keyword or close synonym
            if not _keyword_in_text([primary], repo_text) and not _keyword_in_text(all_kws[:3], repo_text):
                continue

            has_artifact_kw = any(
                a in repo_text for a in ["benchmark", "evaluation", "dataset", "corpus", "leaderboard"]
            )
            if stars >= GITHUB_DIRECT_STARS and has_artifact_kw and _keyword_in_text([primary], repo_text):
                overlap = "DIRECT_OVERLAP"
                contrib_type = "benchmark" if "benchmark" in repo_text else "tool"
            elif stars >= GITHUB_PARTIAL_STARS:
                overlap = "PARTIAL_OVERLAP"
                contrib_type = "tool"
            else:
                overlap = "ADJACENT"
                contrib_type = "tool"

            # Only include DIRECT/PARTIAL (ADJACENT GitHub repos are very noisy)
            if overlap == "ADJACENT":
                continue

            findings.append({
                "topic_id": tid,
                "source": "github",
                "name": name,
                "url": url,
                "doi": "",
                "year": "",
                "venue": "GitHub",
                "contribution_type": contrib_type,
                "overlap_class": overlap,
                "relevance_score": "",
                "stars_or_downloads": stars,
                "why_overlaps": _why_github(name, stars, desc, primary),
                "how_we_differ": _how_we_differ(topic_title, narrowing_note),
                "differentiator_strength": "",
            })
    return findings


def classify_huggingface(topic: dict[str, Any]) -> list[dict[str, Any]]:
    """Classify HuggingFace datasets from evidence/<id>/huggingface.json."""
    tid = topic["topic_id"]
    hf_path = EVIDENCE_DIR / tid / "huggingface.json"
    if not hf_path.exists():
        return []

    data = read_json(hf_path, [])
    kws = _keywords(topic)
    primary = kws[0] if kws else ""
    all_kws = kws + _synonyms(topic)
    topic_title = topic.get("title", "")
    narrowing_note = topic.get("narrowing_note", "")

    seen: set[str] = set()
    findings: list[dict[str, Any]] = []

    for entry in (data or []):
        query = entry.get("query", "") if isinstance(entry, dict) else ""
        results = entry.get("results", []) if isinstance(entry, dict) else []
        for item in results:
            hf_id = item.get("id", "")
            if hf_id in seen:
                continue
            seen.add(hf_id)
            desc = _norm(item.get("description", "") or "")
            downloads = item.get("downloads", 0) or 0
            url = f"https://huggingface.co/datasets/{hf_id}"
            item_text = _norm(hf_id.replace("/", " ").replace("-", " ")) + " " + desc

            if not _keyword_in_text([primary], item_text) and not _keyword_in_text(all_kws[:3], item_text):
                continue

            if downloads >= HF_DIRECT_DOWNLOADS:
                overlap = "DIRECT_OVERLAP"
            elif downloads >= HF_PARTIAL_DOWNLOADS:
                overlap = "PARTIAL_OVERLAP"
            else:
                overlap = "ADJACENT"

            if overlap == "ADJACENT":
                continue

            findings.append({
                "topic_id": tid,
                "source": "huggingface",
                "name": hf_id,
                "url": url,
                "doi": "",
                "year": "",
                "venue": "HuggingFace",
                "contribution_type": "dataset",
                "overlap_class": overlap,
                "relevance_score": "",
                "stars_or_downloads": downloads,
                "why_overlaps": _why_hf(hf_id, downloads, query or primary),
                "how_we_differ": _how_we_differ(topic_title, narrowing_note),
                "differentiator_strength": "",
            })
    return findings


def classify_pwc(topic: dict[str, Any]) -> list[dict[str, Any]]:
    """Classify Papers With Code papers/datasets."""
    tid = topic["topic_id"]
    pwc_path = EVIDENCE_DIR / tid / "paperswithcode.json"
    if not pwc_path.exists():
        return []

    data = read_json(pwc_path, [])
    kws = _keywords(topic)
    primary = kws[0] if kws else ""
    all_kws = kws + _synonyms(topic)
    topic_title = topic.get("title", "")
    narrowing_note = topic.get("narrowing_note", "")

    seen: set[str] = set()
    findings: list[dict[str, Any]] = []

    for entry in (data or []):
        if not isinstance(entry, dict):
            continue
        query = entry.get("query", "")
        for kind, contrib_type in [("papers", "paper"), ("datasets", "dataset")]:
            for item in (entry.get(kind) or []):
                if not isinstance(item, dict):
                    continue
                name = item.get("title") or item.get("name") or item.get("id", "")
                if not name or name in seen:
                    continue
                seen.add(name)
                item_text = _norm(name + " " + (item.get("abstract") or item.get("description") or ""))

                if not _keyword_in_text([primary], item_text) and not _keyword_in_text(all_kws[:3], item_text):
                    continue

                url = item.get("url") or item.get("paper_url") or ""
                overlap = "DIRECT_OVERLAP" if kind == "datasets" else "PARTIAL_OVERLAP"
                why = (
                    f"Papers With Code {kind[:-1]} '{name}' (query: '{query}') "
                    f"indexed under topic '{primary}' — indicates established task/benchmark coverage."
                )
                findings.append({
                    "topic_id": tid,
                    "source": f"pwc_{kind}",
                    "name": name[:200],
                    "url": url[:300],
                    "doi": "",
                    "year": item.get("year") or item.get("published") or "",
                    "venue": "Papers With Code",
                    "contribution_type": contrib_type,
                    "overlap_class": overlap,
                    "relevance_score": "",
                    "stars_or_downloads": "",
                    "why_overlaps": why,
                    "how_we_differ": _how_we_differ(topic_title, narrowing_note),
                    "differentiator_strength": "",
                })
    return findings


# ── topic-level analysis ──────────────────────────────────────────────────────

def analyze_topic(
    topic: dict[str, Any],
    min_direct_score: float = DIRECT_REL_THRESHOLD,
) -> dict[str, Any]:
    """Run all classifiers; compute per-source counts, booleans, and gate triggers."""
    tid = topic["topic_id"]
    log("12_existing", f"Analyzing {tid}")

    all_findings: list[dict[str, Any]] = []
    all_findings.extend(classify_papers(topic, min_direct_score=min_direct_score))
    all_findings.extend(classify_github(topic))
    all_findings.extend(classify_huggingface(topic))
    all_findings.extend(classify_pwc(topic))

    # Deduplicate by normalised name
    seen_names: set[str] = set()
    deduped: list[dict[str, Any]] = []
    for f in all_findings:
        key = re.sub(r"\s+", " ", (f["name"] or "").lower().strip())[:100]
        if key not in seen_names:
            seen_names.add(key)
            deduped.append(f)
    all_findings = deduped

    # ── per-source direct counts ──────────────────────────────────────────────
    def _cnt(cls: str, src_prefix: str) -> int:
        return sum(1 for f in all_findings
                   if f["overlap_class"] == cls and f["source"].startswith(src_prefix))

    direct_paper_count  = _cnt("DIRECT_OVERLAP", "paper")
    direct_github_count = _cnt("DIRECT_OVERLAP", "github")
    direct_hf_count     = _cnt("DIRECT_OVERLAP", "huggingface")
    direct_pwc_count    = _cnt("DIRECT_OVERLAP", "pwc")
    artifact_direct_count = direct_github_count + direct_hf_count + direct_pwc_count
    direct_total_count    = direct_paper_count + artifact_direct_count

    partial_paper_count  = _cnt("PARTIAL_OVERLAP", "paper")
    partial_github_count = _cnt("PARTIAL_OVERLAP", "github")
    partial_hf_count     = _cnt("PARTIAL_OVERLAP", "huggingface")
    partial_pwc_count    = _cnt("PARTIAL_OVERLAP", "pwc")
    n_partial = partial_paper_count + partial_github_count + partial_hf_count + partial_pwc_count

    n_adjacent = sum(1 for f in all_findings if f["overlap_class"] == "ADJACENT")

    # ── boolean indicators ────────────────────────────────────────────────────
    peer_reviewed_direct_overlap = direct_paper_count > 0
    artifact_direct_overlap      = artifact_direct_count > 0
    high_artifact_overlap        = artifact_direct_count >= HIGH_ARTIFACT_OVERLAP_THRESHOLD
    high_peer_reviewed_overlap   = direct_paper_count >= HIGH_PAPER_OVERLAP_THRESHOLD

    # ── differentiator strengths ──────────────────────────────────────────────
    paper_diff_strength    = _paper_differentiator_strength(direct_paper_count)
    artifact_diff_strength = _artifact_differentiator_strength(
        topic, direct_paper_count, artifact_direct_count
    )

    # ── gate triggers ─────────────────────────────────────────────────────────
    go_blocked = (
        (high_peer_reviewed_overlap and paper_diff_strength in ("weak", "none"))
        or (peer_reviewed_direct_overlap and artifact_direct_overlap
            and paper_diff_strength in ("weak", "none"))
        or (high_artifact_overlap and artifact_diff_strength in ("weak", "none"))
    )
    # Note: pure artifact overlap (no papers) does NOT auto-block GO unless artifact
    # differentiator is weak/none — the gate will push to NARROW instead.

    requires_differentiator = (
        direct_paper_count >= 1
        or direct_total_count >= 2
        or partial_paper_count >= 2
    )
    artifact_differentiator_required = artifact_direct_overlap

    # ── back-fill per-finding differentiator_strength ─────────────────────────
    for f in all_findings:
        if f["overlap_class"] == "DIRECT_OVERLAP":
            f["differentiator_strength"] = (
                artifact_diff_strength if f["source"] != "paper" else paper_diff_strength
            )
        elif f["overlap_class"] == "PARTIAL_OVERLAP":
            f["differentiator_strength"] = "moderate" if direct_paper_count == 0 else "weak"
        else:
            f["differentiator_strength"] = "strong"

    # ── top items for JSON summary ────────────────────────────────────────────
    severity_order = {"DIRECT_OVERLAP": 0, "PARTIAL_OVERLAP": 1, "ADJACENT": 2}
    top_findings = sorted(
        [f for f in all_findings if f["overlap_class"] in ("DIRECT_OVERLAP", "PARTIAL_OVERLAP")],
        key=lambda x: (
            severity_order.get(x["overlap_class"], 9),
            -(float(x["relevance_score"] or 0) if x["relevance_score"] != "" else 0),
        ),
    )[:10]

    summary = {
        "topic_id": tid,
        "topic_title": topic.get("title", ""),
        "target_artifact": topic.get("target_artifact", ""),
        # ── per-source direct counts
        "direct_paper_count":    direct_paper_count,
        "direct_github_count":   direct_github_count,
        "direct_hf_count":       direct_hf_count,
        "direct_pwc_count":      direct_pwc_count,
        "artifact_direct_count": artifact_direct_count,
        "direct_total_count":    direct_total_count,
        # ── per-source partial counts
        "partial_paper_count":   partial_paper_count,
        "partial_github_count":  partial_github_count,
        "partial_hf_count":      partial_hf_count,
        "partial_pwc_count":     partial_pwc_count,
        # ── backward-compat aggregate counts
        "n_direct":  direct_total_count,
        "n_partial": n_partial,
        "n_adjacent": n_adjacent,
        "n_total": len(all_findings),
        # ── boolean indicators
        "peer_reviewed_direct_overlap": peer_reviewed_direct_overlap,
        "artifact_direct_overlap":      artifact_direct_overlap,
        "high_artifact_overlap":        high_artifact_overlap,
        "high_peer_reviewed_overlap":   high_peer_reviewed_overlap,
        # ── differentiator signals
        "differentiator_strength":          paper_diff_strength,   # backward compat
        "paper_differentiator_strength":    paper_diff_strength,
        "artifact_differentiator_strength": artifact_diff_strength,
        "artifact_differentiator_required": artifact_differentiator_required,
        # ── gate triggers
        "go_blocked":             go_blocked,
        "requires_differentiator": requires_differentiator,
        "top_findings": top_findings,
    }
    return {"summary": summary, "all_findings": all_findings}


# ── output writers ────────────────────────────────────────────────────────────

def write_topic_json(summary: dict[str, Any]) -> None:
    write_json(OUT_DIR / f"{summary['topic_id']}.json", summary)


def write_topic_csv(tid: str, findings: list[dict[str, Any]]) -> None:
    write_csv(OUT_DIR / f"{tid}_existing_work.csv", findings, header=CSV_FIELDS)


def write_topic_report(summary: dict[str, Any], findings: list[dict[str, Any]]) -> None:  # noqa: C901
    tid   = summary["topic_id"]
    title = summary["topic_title"]
    n_d, n_p, n_a = summary["n_direct"], summary["n_partial"], summary["n_adjacent"]
    paper_strength    = summary["paper_differentiator_strength"]
    artifact_strength = summary["artifact_differentiator_strength"]
    go_blocked = summary["go_blocked"]
    req_diff   = summary["requires_differentiator"]
    art_diff_req = summary["artifact_differentiator_required"]

    dpc  = summary["direct_paper_count"]
    adc  = summary["artifact_direct_count"]
    ghc  = summary["direct_github_count"]
    hfc  = summary["direct_hf_count"]
    pwcc = summary["direct_pwc_count"]
    peer_direct = summary["peer_reviewed_direct_overlap"]
    high_art = summary["high_artifact_overlap"]

    lines: list[str] = []
    lines.append(f"# Existing Work Report — {tid}: {title}\n")

    # ── status banner
    if go_blocked and peer_direct:
        lines.append(
            f"> ⛔ **GO BLOCKED (peer-reviewed overlap)** — {dpc} peer-reviewed DIRECT overlap(s); "
            f"paper_diff_strength=`{paper_strength}`. "
            f"Must articulate a clear differentiator before proceeding.\n"
        )
    elif go_blocked and not peer_direct:
        lines.append(
            f"> ⛔ **GO BLOCKED (artifact overlap)** — {adc} direct artifact(s) "
            f"(GitHub={ghc}, HF={hfc}, PWC={pwcc}); artifact_diff_strength=`{artifact_strength}`. "
            f"No peer-reviewed paper directly covers this — but artifact overlap is high and "
            f"differentiator is weak. Narrow before GO.\n"
        )
    elif art_diff_req and not peer_direct and high_art:
        lines.append(
            f"> ⚠️ **ARTIFACT DIFFERENTIATOR REQUIRED** — {adc} direct artifact(s) "
            f"(GitHub={ghc}, HF={hfc}, PWC={pwcc}), no peer-reviewed paper overlap. "
            f"artifact_diff_strength=`{artifact_strength}`. "
            f"Our peer-reviewed contribution is inherently different, but must be explicit.\n"
        )
    elif req_diff:
        lines.append(
            f"> ⚠️ **DIFFERENTIATOR REQUIRED** — paper_direct={dpc}, artifact_direct={adc}; "
            f"paper_strength=`{paper_strength}`, artifact_strength=`{artifact_strength}`.\n"
        )
    else:
        lines.append(
            f"> ✅ **Clear to proceed** — no blocking overlaps (paper_direct={dpc}, artifact_direct={adc}).\n"
        )

    # ── T07-like special note: high artifact, no peer-reviewed
    if not peer_direct and high_art:
        lines.append(
            "> 📌 **Note (artifact-only overlap):** Academic/paper overlap appears low, but artifact "
            f"overlap is high ({adc} direct artifacts). This topic may still be publishable — "
            "a peer-reviewed benchmark/protocol with a clear domain or methodological focus is "
            "inherently differentiated from GitHub repos and HuggingFace datasets. "
            "Explicitly state: (1) peer-reviewed systematic protocol vs existing repos; "
            "(2) specific domain/use-case vs general artifacts; "
            "(3) evaluation harness + reproducibility package vs raw data.\n"
        )

    # ── summary table
    lines.append("## Summary\n")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| **Paper direct overlaps** | {dpc} |")
    lines.append(f"| Paper diff strength | `{paper_strength}` |")
    lines.append(f"| GitHub direct artifacts | {ghc} |")
    lines.append(f"| HuggingFace direct artifacts | {hfc} |")
    lines.append(f"| PWC direct artifacts | {pwcc} |")
    lines.append(f"| **Artifact direct count** | {adc} |")
    lines.append(f"| Artifact diff strength | `{artifact_strength}` |")
    lines.append(f"| Partial overlaps (total) | {n_p} |")
    lines.append(f"| Adjacent | {n_a} |")
    lines.append(f"| Total findings | {summary['n_total']} |")
    lines.append(f"| peer_reviewed_direct | {'✅ Yes' if peer_direct else 'No'} |")
    lines.append(f"| high_artifact_overlap | {'⚠️ Yes' if high_art else 'No'} |")
    lines.append(f"| GO blocked | {'**YES**' if go_blocked else 'No'} |")
    lines.append(f"| Differentiator required | {'Yes' if req_diff else 'No'} |")
    lines.append(f"| Artifact differentiator required | {'Yes' if art_diff_req else 'No'} |")
    lines.append("")

    # ── separation: paper vs artifact findings
    paper_directs    = [f for f in findings if f["overlap_class"] == "DIRECT_OVERLAP"  and f["source"] == "paper"]
    artifact_directs = [f for f in findings if f["overlap_class"] == "DIRECT_OVERLAP"  and f["source"] != "paper"]
    partials         = [f for f in findings if f["overlap_class"] == "PARTIAL_OVERLAP"]
    adjacents        = [f for f in findings if f["overlap_class"] == "ADJACENT"]

    def _table_row(i: int, f: dict[str, Any]) -> str:
        score_disp = f["relevance_score"] if f["relevance_score"] != "" else f["stars_or_downloads"]
        name_disp  = (f["name"] or "")[:80]
        url        = f["url"] or ""
        name_link  = f"[{name_disp}]({url})" if url else name_disp
        return (
            f"| {i} | {f['source']} | {name_link} | {f['year']} | "
            f"{(f['venue'] or '')[:40]} | {f['contribution_type']} | "
            f"{score_disp} | {f['differentiator_strength']} |"
        )

    def _finding_block(fs: list[dict[str, Any]], label: str) -> list[str]:
        out: list[str] = [f"## {label}\n"]
        if not fs:
            out.append("_None._\n")
            return out
        out.append("| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |")
        out.append("|---|---|---|---|---|---|---|---|")
        for i, f in enumerate(fs, 1):
            out.append(_table_row(i, f))
        out.append("")
        for i, f in enumerate(fs, 1):
            out.append(f"### {i}. {(f['name'] or '')[:120]}")
            out.append(f"- **Source**: {f['source']}  **URL**: {f['url'] or 'n/a'}")
            out.append(f"- **Year/Venue**: {f['year']} / {f['venue'] or 'n/a'}")
            out.append(f"- **Contribution type**: {f['contribution_type']}")
            out.append(f"- **Why it overlaps**: {f['why_overlaps']}")
            out.append(f"- **How we differ**: {f['how_we_differ']}")
            out.append(f"- **Differentiator strength**: `{f['differentiator_strength']}`")
            out.append("")
        return out

    lines.extend(_finding_block(paper_directs, "Peer-Reviewed Direct Overlaps"))
    lines.extend(_finding_block(artifact_directs, "Artifact Direct Overlaps (GitHub / HF / PWC)"))
    lines.extend(_finding_block(partials, "Partial Overlaps"))
    lines.extend(_finding_block(adjacents, "Adjacent Work (context only)"))

    # ── artifact differentiator questions
    if art_diff_req:
        lines.append("## Artifact Differentiator Checklist\n")
        lines.append("Answer each question to establish whether our proposed contribution is distinct:\n")
        lines.append("- [ ] **Peer-reviewed vs repo**: Is our contribution a peer-reviewed paper (not just a code dump)?")
        lines.append("- [ ] **Systematic protocol**: Does our benchmark/dataset follow a documented, reproducible protocol unlike existing repos?")
        lines.append("- [ ] **Domain-specific**: Does our work target a specific domain (clinical, legal, finance) while existing artifacts are general?")
        lines.append("- [ ] **Evaluation focus**: Are we *evaluating behavior* (robustness, bias, sensitivity) rather than merely collecting prompts?")
        lines.append("- [ ] **LLM-judge-specific**: Do we target LLM-as-a-judge specifically, not general prompt injection?")
        lines.append("- [ ] **Reproducibility harness**: Do we release evaluation code + results, not just raw data?")
        lines.append("")

    lines.append("## Recommended Actions\n")
    if go_blocked and peer_direct:
        lines.append(f"1. **Do not promote {tid} to GO** — {dpc} peer-reviewed paper(s) directly cover this.")
        lines.append("2. For each DIRECT paper, fill 'how_we_differ' in the CSV with a specific contribution claim.")
        lines.append("3. If no differentiator: consider DROP or further narrowing.")
    elif go_blocked and not peer_direct:
        lines.append(f"1. **GO blocked by artifact overlap** — {adc} direct artifacts, artifact_diff=`{artifact_strength}`.")
        lines.append("2. Complete the Artifact Differentiator Checklist above.")
        lines.append("3. If differentiator becomes clear (≥ 3 checklist items): update this JSON manually and re-run gate.")
    elif art_diff_req and not peer_direct:
        lines.append(f"1. Complete the Artifact Differentiator Checklist above ({adc} artifacts found).")
        lines.append(f"2. This topic can proceed to GO if artifact differentiator is articulated explicitly.")
        lines.append("3. Write one paragraph for §6 verification log explaining differentiation from top artifacts.")
    elif req_diff:
        lines.append(f"1. Document a clear differentiator before GO (partial overlaps: {n_p}).")
    else:
        lines.append("1. No blocking overlaps. Proceed with normal GO gate checks.")
        if n_a > 0:
            lines.append(f"2. Review {n_a} adjacent item(s) for citation and framing.")
    lines.append("")

    path = REPORTS_DIR / f"{tid}_existing_work.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    log("12_existing", f"  report → {path.name}")


def write_cross_topic_summary(results: list[dict[str, Any]]) -> None:
    """Write data/existing_work/_summary.json for 09_generate_final_report."""
    summaries = [r["summary"] for r in results]
    cross = {
        "topics_analyzed": len(summaries),
        "go_blocked_topics":               [s["topic_id"] for s in summaries if s["go_blocked"]],
        "requires_differentiator_topics":  [s["topic_id"] for s in summaries if s["requires_differentiator"] and not s["go_blocked"]],
        "clean_topics":                    [s["topic_id"] for s in summaries if not s["requires_differentiator"] and not s["go_blocked"]],
        "artifact_only_high_overlap_topics": [
            s["topic_id"] for s in summaries
            if s["artifact_direct_overlap"] and not s["peer_reviewed_direct_overlap"] and s["high_artifact_overlap"]
        ],
        "by_topic": {
            s["topic_id"]: {
                # backward compat
                "n_direct":               s["n_direct"],
                "n_partial":              s["n_partial"],
                "differentiator_strength": s["differentiator_strength"],
                "go_blocked":             s["go_blocked"],
                "requires_differentiator": s["requires_differentiator"],
                # new source-type fields
                "direct_paper_count":        s["direct_paper_count"],
                "direct_github_count":       s["direct_github_count"],
                "direct_hf_count":           s["direct_hf_count"],
                "direct_pwc_count":          s["direct_pwc_count"],
                "artifact_direct_count":     s["artifact_direct_count"],
                "n_adjacent":                s["n_adjacent"],
                "peer_reviewed_direct_overlap":   s["peer_reviewed_direct_overlap"],
                "artifact_direct_overlap":        s["artifact_direct_overlap"],
                "high_artifact_overlap":          s["high_artifact_overlap"],
                "high_peer_reviewed_overlap":     s["high_peer_reviewed_overlap"],
                "paper_differentiator_strength":    s["paper_differentiator_strength"],
                "artifact_differentiator_strength": s["artifact_differentiator_strength"],
                "artifact_differentiator_required": s["artifact_differentiator_required"],
            }
            for s in summaries
        },
    }
    write_json(OUT_DIR / "_summary.json", cross)
    log("12_existing", (
        f"Cross-topic summary → {len(cross['go_blocked_topics'])} blocked, "
        f"{len(cross['requires_differentiator_topics'])} need diff, "
        f"{len(cross['clean_topics'])} clean, "
        f"{len(cross['artifact_only_high_overlap_topics'])} artifact-only-high"
    ))


# ── main ──────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Detect existing work overlapping with each proposed topic.")
    p.add_argument("--topic", default=None, help="Run for a single topic ID only.")
    p.add_argument("--no-report", action="store_true", help="Skip writing per-topic markdown reports.")
    p.add_argument(
        "--min-direct-score",
        type=float,
        default=DIRECT_REL_THRESHOLD,
        metavar="SCORE",
        help=(
            f"Minimum relevance score to classify a paper as DIRECT_OVERLAP "
            f"(default: {DIRECT_REL_THRESHOLD}). Papers in "
            f"[{PARTIAL_REL_THRESHOLD}, SCORE) become PARTIAL_OVERLAP."
        ),
    )
    args = p.parse_args(argv)

    query_files = sorted(QUERIES_DIR.glob("*.json"))
    if args.topic:
        query_files = [f for f in query_files if f.stem == args.topic]

    results: list[dict[str, Any]] = []
    for qf in query_files:
        qdata = read_json(qf, {})
        if not qdata:
            continue
        topic = qdata.get("topic", {})
        if not topic.get("topic_id"):
            continue

        result  = analyze_topic(topic, min_direct_score=args.min_direct_score)
        results.append(result)
        summary = result["summary"]
        tid     = summary["topic_id"]

        write_topic_json(summary)
        write_topic_csv(tid, result["all_findings"])
        if not args.no_report:
            write_topic_report(summary, result["all_findings"])

        log("12_existing", (
            f"{tid}: paper_direct={summary['direct_paper_count']} "
            f"artifact_direct={summary['artifact_direct_count']} "
            f"(gh={summary['direct_github_count']} hf={summary['direct_hf_count']} "
            f"pwc={summary['direct_pwc_count']}) "
            f"go_blocked={summary['go_blocked']} "
            f"paper_diff={summary['paper_differentiator_strength']} "
            f"artifact_diff={summary['artifact_differentiator_strength']}"
        ))

    write_cross_topic_summary(results)

    out_rows = [
        {
            "topic_id":                  r["summary"]["topic_id"],
            "direct_paper_count":        r["summary"]["direct_paper_count"],
            "artifact_direct_count":     r["summary"]["artifact_direct_count"],
            "direct_total_count":        r["summary"]["direct_total_count"],
            "n_partial":                 r["summary"]["n_partial"],
            "peer_reviewed_direct":      r["summary"]["peer_reviewed_direct_overlap"],
            "artifact_direct":           r["summary"]["artifact_direct_overlap"],
            "high_artifact_overlap":     r["summary"]["high_artifact_overlap"],
            "paper_diff":                r["summary"]["paper_differentiator_strength"],
            "artifact_diff":             r["summary"]["artifact_differentiator_strength"],
            "artifact_diff_required":    r["summary"]["artifact_differentiator_required"],
            "go_blocked":                r["summary"]["go_blocked"],
        }
        for r in results
    ]
    print(json.dumps(out_rows, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
