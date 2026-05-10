"""
Topic-conditioned paper relevance scoring.

Each paper is scored against the topic's keywords and synonyms.
Returns (score in [0,1], matched_terms list, reason string).
"""
from __future__ import annotations
import re
from typing import Any

from .config import CFG


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").lower())


def _split_keywords(s: str) -> list[str]:
    return [k.strip().lower() for k in (s or "").split("|") if k.strip()]


def _split_synonyms(s: str) -> list[str]:
    return [k.strip().lower() for k in (s or "").split(";") if k.strip()]


def _split_negatives(s: str) -> list[str]:
    return [k.strip().lower() for k in (s or "").split(";") if k.strip()]


def score_paper(paper: dict[str, Any], topic: dict[str, Any]) -> tuple[float, list[str], str]:
    title = _norm(paper.get("title", ""))
    abstract = _norm((paper.get("abstract") or "")[:5000])
    keywords = _split_keywords(topic.get("keywords", ""))
    synonyms = _split_synonyms(topic.get("synonyms", ""))
    negatives = _split_negatives(topic.get("negative_keywords", ""))

    if not keywords:
        return 0.0, [], "no topic keywords configured"

    score = 0.0
    matched: list[str] = []

    primary = keywords[0]
    if primary and primary in title:
        score += float(CFG["relevance_w_primary_title"])
        matched.append(f"primary:title:{primary}")
    elif primary and primary in abstract:
        score += float(CFG["relevance_w_primary_abstract"])
        matched.append(f"primary:abstract:{primary}")

    for k in keywords[1:]:
        if not k:
            continue
        if k in title:
            score += float(CFG["relevance_w_keyword_title"])
            matched.append(f"kw:title:{k}")
        elif k in abstract:
            score += float(CFG["relevance_w_keyword_abstract"])
            matched.append(f"kw:abstract:{k}")

    for s in synonyms:
        if not s:
            continue
        if s in title:
            score += float(CFG["relevance_w_synonym_title"])
            matched.append(f"syn:title:{s}")
        elif s in abstract:
            score += float(CFG["relevance_w_synonym_abstract"])
            matched.append(f"syn:abstract:{s}")

    # Hard requirement: at least one keyword/synonym match
    if not matched:
        return 0.0, [], "no keyword/synonym match"

    # Penalize on negative keywords
    for n in negatives:
        if n and n in (title + " " + abstract):
            score *= 0.4
            matched.append(f"-neg:{n}")
            break

    rel = max(0.0, min(1.0, score / float(CFG["relevance_normalize_denom"])))
    primary_in = (primary in title) or (primary in abstract)
    reason = (
        f"matched {len([m for m in matched if not m.startswith('-')])} term(s); "
        f"primary_in_title_or_abstract={primary_in}; "
        f"raw_score={round(score,2)}"
    )
    return round(rel, 3), matched[:8], reason


def filter_by_relevance(
    papers: list[dict[str, Any]],
    topic: dict[str, Any],
    threshold: float | None = None,
    keep_max: int | None = None,
) -> list[dict[str, Any]]:
    th = float(CFG["relevance_min"]) if threshold is None else threshold
    cap = int(CFG["relevance_keep_max"]) if keep_max is None else keep_max
    enriched = []
    for p in papers:
        rel, matched, reason = score_paper(p, topic)
        q = dict(p)
        q["relevance_score"] = rel
        q["matched_keywords"] = "|".join(matched)
        q["reason_included"] = reason
        enriched.append(q)
    enriched.sort(
        key=lambda x: (
            x.get("relevance_score", 0),
            int(x.get("citations") or 0),
        ),
        reverse=True,
    )
    kept = [p for p in enriched if p.get("relevance_score", 0) >= th]
    return kept[:cap]


def median_relevance(papers: list[dict[str, Any]]) -> float:
    vals = [float(p.get("relevance_score", 0) or 0) for p in papers]
    if not vals:
        return 0.0
    vals.sort()
    n = len(vals)
    mid = n // 2
    return round((vals[mid] if n % 2 else (vals[mid - 1] + vals[mid]) / 2), 3)
