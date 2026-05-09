"""
05_score_topics.py

Compute evidence-based signals per topic and an Overall priority score.

Signals derived from collected evidence:
- topic_volume_24mo, topic_volume_12mo
- median_citations, top_citation, growth_yoy
- saturation_score (papers + dominant tools/datasets)
- gap_phrase_hits (limitations/future-work language in abstracts)
- artifact_opportunity (lack of public bench/dataset/tool but evidence of demand)
- venue_signal (active venues in DOAJ + Crossref + OpenReview hits)
- risk_signal (PHI / proprietary / employer keywords detected)

Outputs:
- data/scores/<topic_id>.json   (per-topic detailed)
- data/scores/scores.csv        (per-topic summary)
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
from statistics import median
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.io_utils import read_csv, read_json, write_json, write_csv, log, evidence_dir  # noqa: E402

QUERIES_DIR = ROOT / "data" / "queries"
DEDUP_DIR = ROOT / "data" / "papers_dedup"
SCORES_DIR = ROOT / "data" / "scores"
SCORES_DIR.mkdir(parents=True, exist_ok=True)

GAP_PHRASES = [
    "future work", "limitation", "limited to",
    "do not generalize", "not robust", "remains an open",
    "remains unclear", "open question", "no benchmark exists",
    "no standard", "no consensus", "lack of", "insufficient",
    "we leave", "out of scope", "as future",
]

RISK_KEYWORDS_IP = [
    "PHI", "protected health information", "EHR access",
    "proprietary", "internal-only", "employer-confidential",
    "claims database (private)", "vendor data",
]


def _now_year() -> int:
    from datetime import date
    return date.today().year


def _to_int(x: Any) -> int:
    try:
        return int(float(x))
    except Exception:
        return 0


def compute_paper_signals(papers: list[dict[str, Any]]) -> dict[str, Any]:
    cy = _now_year()
    last24 = [p for p in papers if (_to_int(p.get("year")) or 0) >= cy - 2]
    last12 = [p for p in papers if (_to_int(p.get("year")) or 0) >= cy - 1]
    cits = [_to_int(p.get("citations")) for p in papers if p.get("citations") is not None]
    top_cit = max(cits) if cits else 0
    med_cit = int(median(cits)) if cits else 0
    yoy = 0.0
    if last24:
        prev = [p for p in last24 if (_to_int(p.get("year")) or 0) == cy - 2]
        cur = [p for p in last24 if (_to_int(p.get("year")) or 0) >= cy - 1]
        yoy = (len(cur) - len(prev)) / max(1, len(prev))
    return {
        "n_papers": len(papers),
        "n_papers_24mo": len(last24),
        "n_papers_12mo": len(last12),
        "median_citations": med_cit,
        "top_citation": top_cit,
        "growth_yoy_proxy": round(yoy, 3),
    }


def gap_phrase_hits(papers: list[dict[str, Any]]) -> int:
    hits = 0
    for p in papers:
        ab = (p.get("abstract") or "").lower()
        for ph in GAP_PHRASES:
            if ph in ab:
                hits += 1
                break
    return hits


def saturation(papers: list[dict[str, Any]], gh: list[dict[str, Any]], hf: list[dict[str, Any]]) -> dict[str, Any]:
    n = len(papers)
    dominant_tools = 0
    for batch in gh:
        for r in batch.get("results", []) or []:
            if r.get("stars", 0) >= 1500:
                dominant_tools += 1
    big_datasets = 0
    for batch in hf:
        for r in batch.get("results", []) or []:
            if r.get("downloads", 0) >= 5000:
                big_datasets += 1
    score = 0
    if n > 200:
        score += 2
    elif n > 80:
        score += 1
    if dominant_tools >= 2:
        score += 2
    elif dominant_tools == 1:
        score += 1
    if big_datasets >= 2:
        score += 1
    score = min(5, score)
    return {"saturation_score_0to5": score, "n_papers": n,
            "dominant_tools": dominant_tools, "big_datasets": big_datasets}


def artifact_opportunity(papers: list[dict[str, Any]], pwc_records: list[dict[str, Any]],
                         hf_records: list[dict[str, Any]]) -> dict[str, Any]:
    n_pwc_datasets = sum(len(r.get("datasets", [])) for r in pwc_records)
    n_hf = sum(len(r.get("results", [])) for r in hf_records)
    gap_signal = gap_phrase_hits(papers)
    score = 0
    if gap_signal >= 5 and n_pwc_datasets <= 2 and n_hf <= 5:
        score = 5
    elif gap_signal >= 3 and n_pwc_datasets <= 5 and n_hf <= 10:
        score = 4
    elif gap_signal >= 1:
        score = 3
    else:
        score = 2
    return {
        "artifact_opportunity_0to5": score,
        "gap_phrase_hits": gap_signal,
        "n_existing_pwc_datasets": n_pwc_datasets,
        "n_existing_hf_datasets": n_hf,
    }


def venue_signal(doaj_records: list[dict[str, Any]], venues_payload: dict[str, Any] | None) -> dict[str, Any]:
    no_apc = 0
    for batch in doaj_records:
        for r in batch.get("results", []) or []:
            if r.get("no_apc"):
                no_apc += 1
    cross_active = 0
    or_hits = 0
    if venues_payload:
        for v in venues_payload.get("venues") or []:
            if v.get("crossref_active"):
                cross_active += 1
        for orc in venues_payload.get("openreview_signal") or []:
            or_hits += len(orc.get("results") or [])
    score = 0
    if cross_active >= 4:
        score += 2
    elif cross_active >= 2:
        score += 1
    if no_apc >= 2:
        score += 2
    elif no_apc >= 1:
        score += 1
    if or_hits >= 5:
        score += 1
    score = min(5, score)
    return {
        "venue_signal_0to5": score,
        "doaj_no_apc_journals": no_apc,
        "crossref_active_venues": cross_active,
        "openreview_hits": or_hits,
    }


def risk_signal(topic: dict[str, Any]) -> dict[str, Any]:
    text = " ".join(str(v) for v in topic.values()).lower()
    flags = [k for k in RISK_KEYWORDS_IP if k.lower() in text]
    return {"ip_risk_flags": flags, "ip_risk_0to5": min(5, len(flags) * 2)}


def citation_signal_score(p: dict[str, Any]) -> int:
    """0..5 from paper signals."""
    if p["n_papers_24mo"] == 0:
        return 0
    s = 0
    if p["n_papers_24mo"] >= 80:
        s += 2
    elif p["n_papers_24mo"] >= 25:
        s += 1
    if p["top_citation"] >= 200:
        s += 2
    elif p["top_citation"] >= 50:
        s += 1
    if p["growth_yoy_proxy"] > 0.2:
        s += 1
    return min(5, s)


def heuristic_overall(metrics: dict[str, Any]) -> float:
    """
    Map evidence-derived signals into the rubric A..X (heuristic, transparent).
    All factors 1..5; missing -> 2 as neutral default.
    """
    A = max(1, min(5, 2 + (1 if metrics["paper"]["growth_yoy_proxy"] > 0.0 else 0) + (1 if metrics["paper"]["n_papers_12mo"] > 30 else 0)))
    B = max(1, min(5, 2 + (1 if metrics["paper"]["n_papers"] > 50 else 0) + (1 if metrics["paper"]["top_citation"] >= 100 else 0) + (1 if metrics["paper"]["top_citation"] >= 500 else 0)))
    C = 5 - min(4, metrics["saturation"]["saturation_score_0to5"])
    D = metrics["artifact"]["artifact_opportunity_0to5"]
    E = max(1, min(5, 5 - metrics["artifact"]["n_existing_pwc_datasets"]))
    F = 3
    G = 3
    H = max(1, metrics["venue"]["venue_signal_0to5"])
    I = 3
    J = max(1, min(5, 1 + metrics["venue"]["doaj_no_apc_journals"]))
    K = 3
    L = 3
    M = 3
    N = 3
    O = max(1, metrics["saturation"]["saturation_score_0to5"])
    P = max(1, min(5, 3 - (1 if metrics["artifact"]["gap_phrase_hits"] > 3 else 0) + (1 if metrics["saturation"]["dominant_tools"] >= 2 else 0)))
    Q = 1
    R = max(1, metrics["risk"]["ip_risk_0to5"]) if metrics["risk"]["ip_risk_0to5"] > 0 else 1
    S = 4
    T = 2
    U = 4
    V = max(1, metrics["artifact"]["artifact_opportunity_0to5"])
    W = 1
    X = max(1, min(5, 2 + (1 if metrics["paper"]["n_papers_24mo"] > 50 else 0) + (1 if metrics["paper"]["growth_yoy_proxy"] > 0 else 0)))

    citation_pot = 1.5 * A + 1.5 * B + 2 * C + 1.5 * D + X
    exec_feas = 2 * I + 1.5 * K + 1.5 * S + U - 1.5 * Q - 1.5 * T
    immig = 1.5 * L + 1.5 * M + 1.2 * V + 0.5 * D
    career = 1.5 * N + V + 0.5 * F + 0.5 * D
    pub_path = 1.5 * H + 1.5 * J + I - P
    risk_penalty = O + P + 1.5 * Q + 2 * R + 0.5 * W + 0.5 * T
    overall = (
        0.30 * citation_pot
        + 0.20 * exec_feas
        + 0.20 * immig
        + 0.10 * career
        + 0.20 * pub_path
        - 0.40 * risk_penalty
    )
    return {
        "factors": {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H, "I": I, "J": J,
                    "K": K, "L": L, "M": M, "N": N, "O": O, "P": P, "Q": Q, "R": R, "S": S, "T": T,
                    "U": U, "V": V, "W": W, "X": X},
        "composites": {
            "CitationPotential": round(citation_pot, 2),
            "ExecFeasibility": round(exec_feas, 2),
            "ImmigrationValue": round(immig, 2),
            "CareerValue": round(career, 2),
            "PublicationPath": round(pub_path, 2),
            "RiskPenalty": round(risk_penalty, 2),
            "Overall": round(overall, 2),
        },
    }


def score_topic(topic_id: str, topic_meta: dict[str, Any]) -> dict[str, Any]:
    edir = evidence_dir(topic_id)
    dedup_csv = DEDUP_DIR / f"{topic_id}.csv"
    papers = read_csv(dedup_csv) if dedup_csv.exists() else []
    # parse abstracts back from raw evidence (deduped CSV doesn't carry abstracts)
    raw = []
    for src in ("semantic_scholar", "openalex", "crossref", "arxiv"):
        d = read_json(edir / f"{src}.json", [])
        for batch in d or []:
            for p in batch.get("results", []) or []:
                ab = ""
                if src == "semantic_scholar":
                    ab = p.get("abstract") or ""
                elif src == "arxiv":
                    ab = p.get("summary") or ""
                elif src == "crossref":
                    ab = p.get("abstract") or ""
                elif src == "openalex":
                    inv = p.get("abstract_inverted_index")
                    if isinstance(inv, dict):
                        positions = []
                        for w, idxs in inv.items():
                            for i in idxs:
                                positions.append((i, w))
                        ab = " ".join(w for _, w in sorted(positions))
                year = p.get("year") or p.get("publication_year") or 0
                if src == "arxiv" and p.get("published"):
                    try:
                        year = int(p["published"][:4])
                    except Exception:
                        year = 0
                if src == "crossref":
                    iss = p.get("issued", {}) or {}
                    dp = iss.get("date-parts") if isinstance(iss, dict) else None
                    if isinstance(dp, list) and dp and isinstance(dp[0], list) and dp[0]:
                        try:
                            year = int(dp[0][0])
                        except Exception:
                            year = 0
                    if not year:
                        # fall back to created/published-print
                        for k in ("created", "published-print", "published-online"):
                            v = p.get(k)
                            if isinstance(v, dict):
                                vdp = v.get("date-parts")
                                if isinstance(vdp, list) and vdp and isinstance(vdp[0], list) and vdp[0]:
                                    try:
                                        year = int(vdp[0][0])
                                        break
                                    except Exception:
                                        pass
                cit = p.get("citationCount") or p.get("cited_by_count") or p.get("is-referenced-by-count") or 0
                raw.append({"abstract": ab, "year": year, "citations": cit})

    paper_sig = compute_paper_signals(raw)

    gh = read_json(edir / "github.json", [])
    hf = read_json(edir / "huggingface.json", [])
    pwc = read_json(edir / "paperswithcode.json", [])
    doaj = read_json(edir / "doaj.json", [])
    venues = read_json(edir / "venues.json", {})

    sat = saturation(raw, gh, hf)
    art = artifact_opportunity(raw, pwc, hf)
    ven = venue_signal(doaj, venues)
    risk = risk_signal(topic_meta)

    metrics = {
        "paper": paper_sig,
        "saturation": sat,
        "artifact": art,
        "venue": ven,
        "risk": risk,
        "citation_signal_0to5": citation_signal_score(paper_sig),
    }
    rubric = heuristic_overall(metrics)
    metrics["rubric"] = rubric
    metrics["topic_id"] = topic_id
    metrics["topic_title"] = topic_meta.get("title", "")
    return metrics


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--topic", default=None)
    args = p.parse_args(argv)

    files = sorted(QUERIES_DIR.glob("*.json"))
    if args.topic:
        files = [f for f in files if f.stem == args.topic]
    summary_rows: list[dict[str, Any]] = []
    for f in files:
        q = read_json(f)
        if not q:
            continue
        topic_id = q["topic"]["topic_id"]
        m = score_topic(topic_id, q["topic"])
        write_json(SCORES_DIR / f"{topic_id}.json", m)
        log("05_score", f"{topic_id} Overall={m['rubric']['composites']['Overall']}")
        summary_rows.append({
            "topic_id": topic_id,
            "title": m["topic_title"],
            "n_papers": m["paper"]["n_papers"],
            "n_papers_24mo": m["paper"]["n_papers_24mo"],
            "top_citation": m["paper"]["top_citation"],
            "growth_yoy": m["paper"]["growth_yoy_proxy"],
            "citation_signal_0to5": m["citation_signal_0to5"],
            "saturation_0to5": m["saturation"]["saturation_score_0to5"],
            "artifact_0to5": m["artifact"]["artifact_opportunity_0to5"],
            "venue_signal_0to5": m["venue"]["venue_signal_0to5"],
            "ip_risk_0to5": m["risk"]["ip_risk_0to5"],
            "Overall": m["rubric"]["composites"]["Overall"],
            "CitationPotential": m["rubric"]["composites"]["CitationPotential"],
            "ExecFeasibility": m["rubric"]["composites"]["ExecFeasibility"],
            "PublicationPath": m["rubric"]["composites"]["PublicationPath"],
            "RiskPenalty": m["rubric"]["composites"]["RiskPenalty"],
        })
    summary_rows.sort(key=lambda r: r["Overall"], reverse=True)
    write_csv(SCORES_DIR / "scores.csv", summary_rows)
    print(json.dumps(summary_rows, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
