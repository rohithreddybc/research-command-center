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

Gate triggers (written to data/existing_work/<topic_id>.json):
  go_blocked = True          → DIRECT_OVERLAP found AND differentiator_strength in {"weak","none"}
  requires_differentiator    → any DIRECT_OVERLAP OR ≥2 PARTIAL_OVERLAP from papers

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
DIRECT_REL_THRESHOLD  = 0.50   # paper relevance ≥ this → candidate for DIRECT
PARTIAL_REL_THRESHOLD = 0.35   # paper relevance ≥ this → PARTIAL_OVERLAP
ADJACENT_REL_THRESHOLD = 0.20  # paper relevance ≥ this → ADJACENT

GITHUB_DIRECT_STARS  = 100     # repo stars ≥ this + keyword match → DIRECT candidate
GITHUB_PARTIAL_STARS = 30      # repo stars ≥ this + keyword match → PARTIAL
HF_DIRECT_DOWNLOADS  = 100     # HF downloads ≥ this + keyword match → DIRECT candidate
HF_PARTIAL_DOWNLOADS = 20      # HF downloads ≥ this + keyword match → PARTIAL

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


def _differentiator_strength(n_direct: int) -> str:
    if n_direct == 0:
        return "strong"
    if n_direct == 1:
        return "moderate"
    if n_direct == 2:
        return "weak"
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
) -> list[dict[str, Any]]:
    """Classify pre-scored papers from papers_dedup/<id>.csv."""
    tid = topic["topic_id"]
    csv_path = DEDUP_DIR / f"{tid}.csv"
    if not csv_path.exists():
        return []

    rows = read_csv(csv_path)
    kws = _keywords(topic)
    primary = kws[0] if kws else ""
    all_kws = kws + _synonyms(topic)
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

        title   = (r.get("title") or "").strip()
        abstract = (r.get("abstract") or "").strip()
        year_raw = r.get("year", "")
        try:
            year = int(year_raw)
        except (ValueError, TypeError):
            year = 0
        venue   = (r.get("venue") or r.get("journal") or "").strip()
        doi     = (r.get("doi") or "").strip()
        url_raw = doi if doi.startswith("http") else (f"https://doi.org/{doi}" if doi else r.get("url", ""))
        matched_kws = (r.get("matched_keywords") or "").strip()

        contrib_type = _contribution_type(title, abstract)
        has_artifact_match = _artifact_matches(contrib_type, target_types)

        # classify
        if score >= DIRECT_REL_THRESHOLD and has_artifact_match and year >= 2022:
            overlap = "DIRECT_OVERLAP"
        elif score >= PARTIAL_REL_THRESHOLD or (score >= DIRECT_REL_THRESHOLD and not has_artifact_match):
            overlap = "PARTIAL_OVERLAP"
        else:
            overlap = "ADJACENT"

        why = _why_paper(title, score, contrib_type, topic.get("target_artifact", "?"), matched_kws)
        how = _how_we_differ(topic_title, narrowing_note)
        # individual paper strength will be aggregated later
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
            "differentiator_strength": "",  # filled after counting
        })

    return findings


def classify_github(
    topic: dict[str, Any],
) -> list[dict[str, Any]]:
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
    target_types = _target_types(topic)

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
            topics_list = [t.lower() for t in (repo.get("topics") or [])]
            stars = repo.get("stars", 0) or 0
            url = repo.get("url", "") or f"https://github.com/{name}"
            repo_text = _norm(name.replace("/", " ").replace("-", " ").replace("_", " ")) + " " + desc

            # Skip obvious collection repos
            if _COLLECTION_PATTERNS.search(desc) or "awesome" in name.lower():
                continue

            # Must contain primary keyword somewhere meaningful
            if not _keyword_in_text([primary], repo_text) and not _keyword_in_text(all_kws[:3], repo_text):
                continue

            # Determine overlap class
            has_artifact_kw = any(a in repo_text for a in ["benchmark", "evaluation", "dataset", "corpus", "leaderboard"])
            if stars >= GITHUB_DIRECT_STARS and has_artifact_kw and _keyword_in_text([primary], repo_text):
                overlap = "DIRECT_OVERLAP"
                contrib_type = "benchmark" if "benchmark" in repo_text else "tool"
            elif stars >= GITHUB_PARTIAL_STARS:
                overlap = "PARTIAL_OVERLAP"
                contrib_type = "tool"
            else:
                overlap = "ADJACENT"
                contrib_type = "tool"

            # Only include DIRECT/PARTIAL (ADJACENT github repos are very noisy)
            if overlap == "ADJACENT":
                continue

            why = _why_github(name, stars, desc, primary)
            how = _how_we_differ(topic_title, narrowing_note)
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
                "why_overlaps": why,
                "how_we_differ": how,
                "differentiator_strength": "",
            })
    return findings


def classify_huggingface(
    topic: dict[str, Any],
) -> list[dict[str, Any]]:
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
            tags = [t.lower() for t in (item.get("tags") or [])]
            downloads = item.get("downloads", 0) or 0
            url = f"https://huggingface.co/datasets/{hf_id}"
            item_text = _norm(hf_id.replace("/", " ").replace("-", " ")) + " " + desc

            # Must match primary or close synonyms
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

            why = _why_hf(hf_id, downloads, query or primary)
            how = _how_we_differ(topic_title, narrowing_note)
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
                "why_overlaps": why,
                "how_we_differ": how,
                "differentiator_strength": "",
            })
    return findings


def classify_pwc(
    topic: dict[str, Any],
) -> list[dict[str, Any]]:
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

                # Only include if primary keyword present
                if not _keyword_in_text([primary], item_text) and not _keyword_in_text(all_kws[:3], item_text):
                    continue

                url = item.get("url") or item.get("paper_url") or ""
                overlap = "DIRECT_OVERLAP" if kind == "datasets" else "PARTIAL_OVERLAP"
                why = (
                    f"Papers With Code {kind[:-1]} '{name}' (query: '{query}') "
                    f"is indexed under topic '{primary}' — indicates established task/benchmark coverage."
                )
                how = _how_we_differ(topic_title, narrowing_note)
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
                    "how_we_differ": how,
                    "differentiator_strength": "",
                })
    return findings


# ── topic-level analysis ──────────────────────────────────────────────────────

def analyze_topic(topic: dict[str, Any]) -> dict[str, Any]:
    """Run all classifiers for a topic; compute summary + gate triggers."""
    tid = topic["topic_id"]
    log("12_existing", f"Analyzing {tid}")

    all_findings: list[dict[str, Any]] = []
    all_findings.extend(classify_papers(topic))
    all_findings.extend(classify_github(topic))
    all_findings.extend(classify_huggingface(topic))
    all_findings.extend(classify_pwc(topic))

    # Deduplicate by normalised name (title-like)
    seen_names: set[str] = set()
    deduped: list[dict[str, Any]] = []
    for f in all_findings:
        key = re.sub(r"\s+", " ", (f["name"] or "").lower().strip())[:100]
        if key not in seen_names:
            seen_names.add(key)
            deduped.append(f)
    all_findings = deduped

    # Count by class
    n_direct  = sum(1 for f in all_findings if f["overlap_class"] == "DIRECT_OVERLAP")
    n_partial = sum(1 for f in all_findings if f["overlap_class"] == "PARTIAL_OVERLAP")
    n_adjacent = sum(1 for f in all_findings if f["overlap_class"] == "ADJACENT")

    diff_strength = _differentiator_strength(n_direct)

    # Back-fill differentiator_strength per finding
    for f in all_findings:
        if f["overlap_class"] == "DIRECT_OVERLAP":
            f["differentiator_strength"] = diff_strength
        elif f["overlap_class"] == "PARTIAL_OVERLAP":
            f["differentiator_strength"] = "moderate" if n_direct == 0 else "weak"
        else:
            f["differentiator_strength"] = "strong"

    # Gate triggers
    go_blocked = diff_strength in ("weak", "none")
    requires_differentiator = (n_direct >= 1) or (n_partial >= 2)

    # Top items for JSON summary (most severe first)
    severity_order = {"DIRECT_OVERLAP": 0, "PARTIAL_OVERLAP": 1, "ADJACENT": 2}
    top_findings = sorted(
        [f for f in all_findings if f["overlap_class"] in ("DIRECT_OVERLAP", "PARTIAL_OVERLAP")],
        key=lambda x: (severity_order.get(x["overlap_class"], 9), -(float(x["relevance_score"] or 0) if x["relevance_score"] != "" else 0)),
    )[:10]

    summary = {
        "topic_id": tid,
        "topic_title": topic.get("title", ""),
        "target_artifact": topic.get("target_artifact", ""),
        "n_direct": n_direct,
        "n_partial": n_partial,
        "n_adjacent": n_adjacent,
        "n_total": len(all_findings),
        "differentiator_strength": diff_strength,
        "go_blocked": go_blocked,
        "requires_differentiator": requires_differentiator,
        "top_findings": top_findings,
    }

    return {"summary": summary, "all_findings": all_findings}


# ── output writers ────────────────────────────────────────────────────────────

def write_topic_json(summary: dict[str, Any]) -> None:
    tid = summary["topic_id"]
    write_json(OUT_DIR / f"{tid}.json", summary)


def write_topic_csv(tid: str, findings: list[dict[str, Any]]) -> None:
    path = OUT_DIR / f"{tid}_existing_work.csv"
    write_csv(path, findings, header=CSV_FIELDS)


def write_topic_report(summary: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    tid = summary["topic_id"]
    title = summary["topic_title"]
    n_d, n_p, n_a = summary["n_direct"], summary["n_partial"], summary["n_adjacent"]
    strength = summary["differentiator_strength"]
    go_blocked = summary["go_blocked"]
    req_diff = summary["requires_differentiator"]

    lines: list[str] = []
    lines.append(f"# Existing Work Report — {tid}: {title}\n")

    # Status banner
    if go_blocked:
        lines.append(f"> ⛔ **GO BLOCKED** — {n_d} direct overlap(s) found; differentiator strength = `{strength}`.\n")
    elif req_diff:
        lines.append(f"> ⚠️ **DIFFERENTIATOR REQUIRED** — {n_d} direct + {n_p} partial overlap(s); strength = `{strength}`.\n")
    else:
        lines.append(f"> ✅ **Clear to proceed** — no blocking overlaps (direct={n_d}, partial={n_p}).\n")

    lines.append("## Summary\n")
    lines.append(f"| Metric | Value |")
    lines.append(f"|---|---|")
    lines.append(f"| Direct overlaps | {n_d} |")
    lines.append(f"| Partial overlaps | {n_p} |")
    lines.append(f"| Adjacent | {n_a} |")
    lines.append(f"| Total findings | {summary['n_total']} |")
    lines.append(f"| Differentiator strength | `{strength}` |")
    lines.append(f"| GO blocked | {'**YES**' if go_blocked else 'No'} |")
    lines.append(f"| Differentiator required | {'Yes' if req_diff else 'No'} |")
    lines.append("")

    # Direct overlaps detail
    directs = [f for f in findings if f["overlap_class"] == "DIRECT_OVERLAP"]
    partials = [f for f in findings if f["overlap_class"] == "PARTIAL_OVERLAP"]
    adjacents = [f for f in findings if f["overlap_class"] == "ADJACENT"]

    def _finding_block(fs: list[dict[str, Any]], label: str) -> list[str]:
        out: list[str] = [f"## {label}\n"]
        if not fs:
            out.append("_None._\n")
            return out
        out.append("| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |")
        out.append("|---|---|---|---|---|---|---|---|")
        for i, f in enumerate(fs, 1):
            score_disp = f["relevance_score"] if f["relevance_score"] != "" else f['stars_or_downloads']
            name_disp = (f["name"] or "")[:80]
            url = f["url"] or ""
            name_link = f"[{name_disp}]({url})" if url else name_disp
            out.append(
                f"| {i} | {f['source']} | {name_link} | {f['year']} | {(f['venue'] or '')[:40]} | "
                f"{f['contribution_type']} | {score_disp} | {f['differentiator_strength']} |"
            )
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

    lines.extend(_finding_block(directs, "Direct Overlaps (GO-blocking)"))
    lines.extend(_finding_block(partials, "Partial Overlaps (differentiator required)"))
    lines.extend(_finding_block(adjacents, "Adjacent Work (context only)"))

    lines.append("## Recommended Actions\n")
    if go_blocked:
        lines.append(f"1. **Do not promote {tid} to GO** until you have articulated a concrete differentiator vs the {n_d} direct overlap(s) above.")
        lines.append("2. For each DIRECT_OVERLAP, fill in the 'how_we_differ' column in the CSV with a specific contribution claim.")
        lines.append("3. If a differentiator cannot be found, consider DROPping or NARROWING further.")
    elif req_diff:
        lines.append(f"1. Document a clear differentiator before promoting to GO (partial overlaps: {n_p}).")
        lines.append("2. Update `data/existing_work/" + tid + ".json` → `requires_differentiator: true` acknowledged.")
    else:
        lines.append(f"1. No blocking overlaps found. Proceed with normal GO gate checks.")
        if n_a > 0:
            lines.append(f"2. Review {n_a} adjacent work item(s) for citation and framing purposes.")
    lines.append("")

    path = REPORTS_DIR / f"{tid}_existing_work.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    log("12_existing", f"  report → {path.name}")


def write_cross_topic_summary(results: list[dict[str, Any]]) -> None:
    """Write data/existing_work/_summary.json for 09_generate_final_report."""
    summaries = [r["summary"] for r in results]
    cross = {
        "topics_analyzed": len(summaries),
        "go_blocked_topics": [s["topic_id"] for s in summaries if s["go_blocked"]],
        "requires_differentiator_topics": [s["topic_id"] for s in summaries if s["requires_differentiator"] and not s["go_blocked"]],
        "clean_topics": [s["topic_id"] for s in summaries if not s["requires_differentiator"] and not s["go_blocked"]],
        "by_topic": {s["topic_id"]: {
            "n_direct": s["n_direct"],
            "n_partial": s["n_partial"],
            "differentiator_strength": s["differentiator_strength"],
            "go_blocked": s["go_blocked"],
            "requires_differentiator": s["requires_differentiator"],
        } for s in summaries},
    }
    write_json(OUT_DIR / "_summary.json", cross)
    log("12_existing", f"Cross-topic summary → {len(cross['go_blocked_topics'])} blocked, "
                       f"{len(cross['requires_differentiator_topics'])} need diff, "
                       f"{len(cross['clean_topics'])} clean")


# ── main ──────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Detect existing work overlapping with each proposed topic.")
    p.add_argument("--topic", default=None, help="Run for a single topic ID only.")
    p.add_argument("--no-report", action="store_true", help="Skip writing per-topic markdown reports.")
    args = p.parse_args(argv)

    # Load topics from query files
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

        result = analyze_topic(topic)
        results.append(result)
        summary = result["summary"]
        findings = result["all_findings"]
        tid = summary["topic_id"]

        write_topic_json(summary)
        write_topic_csv(tid, findings)
        if not args.no_report:
            write_topic_report(summary, findings)

        log("12_existing", (
            f"{tid}: direct={summary['n_direct']} partial={summary['n_partial']} "
            f"adjacent={summary['n_adjacent']} go_blocked={summary['go_blocked']} "
            f"diff_strength={summary['differentiator_strength']}"
        ))

    write_cross_topic_summary(results)

    # Print compact JSON output (mirrors other pipeline scripts)
    out_rows = [
        {
            "topic_id": r["summary"]["topic_id"],
            "n_direct": r["summary"]["n_direct"],
            "n_partial": r["summary"]["n_partial"],
            "n_adjacent": r["summary"]["n_adjacent"],
            "go_blocked": r["summary"]["go_blocked"],
            "requires_differentiator": r["summary"]["requires_differentiator"],
            "differentiator_strength": r["summary"]["differentiator_strength"],
        }
        for r in results
    ]
    print(json.dumps(out_rows, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
