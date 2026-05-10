"""
08_confidence_gate.py

Combine evidence-based scores (05) and reviewer agreement (07) into a final
GO / NARROW / DROP / NEEDS_MORE_EVIDENCE decision per topic.

Decision rules (from PHASE 6 spec):

GO if:
  - Overall priority high (>=14)
  - citation_signal_0to5 >= 3
  - artifact_opportunity_0to5 >= 3
  - venue_signal_0to5 >= 2 (path exists/likely)
  - ip_risk_0to5 <= 1
  - saturation_0to5 <= 4 (not extreme)
  - reviewer plurality decision GO and decision_score_mean >= 2.0
  - >=2 evidence sources contributed papers

DROP if:
  - citation_signal_0to5 == 0
  - artifact_opportunity_0to5 <= 1
  - saturation_0to5 == 5 with no differentiator (artifact <= 2)
  - venue_signal_0to5 == 0 after rounds
  - ip_risk_0to5 >= 4
  - reviewer plurality DROP with high confidence drops >= 2

NARROW if:
  - saturation high (>=4) but artifact_opportunity_0to5 >= 3
  - audience good (citation_signal >=3) but novelty weak (P high)
  - venue path exists but topic too broad

NEEDS_MORE_EVIDENCE otherwise (or on disagreement / unclear venues).
If NEEDS_MORE_EVIDENCE and rounds_remaining > 0, the orchestrator (10) will
re-run extra evidence with expanded queries.

Outputs:
- data/decisions/<topic_id>.json
- data/decisions/decisions.csv
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.io_utils import read_csv, read_json, write_json, write_csv, log  # noqa: E402
from common.config import CFG  # noqa: E402

QUERIES_DIR    = ROOT / "data" / "queries"
DEDUP_DIR      = ROOT / "data" / "papers_dedup"
SCORES_DIR     = ROOT / "data" / "scores"
AGREE_DIR      = ROOT / "data" / "agreement"
DECISIONS_DIR  = ROOT / "data" / "decisions"
EW_DIR         = ROOT / "data" / "existing_work"   # from 12_detect_existing_work
DECISIONS_DIR.mkdir(parents=True, exist_ok=True)


def n_sources(topic_id: str) -> int:
    rows = read_csv(DEDUP_DIR / f"{topic_id}.csv") if (DEDUP_DIR / f"{topic_id}.csv").exists() else []
    src = set()
    for r in rows:
        for s in (r.get("sources", "") or "").split("|"):
            if s.strip():
                src.add(s.strip())
    return len(src)


def completeness(topic_id: str, n_reviews: int) -> dict[str, bool]:
    edir = ROOT / "data" / "evidence" / topic_id
    return {
        "evidence_collected": (edir / "semantic_scholar.json").exists() or (edir / "openalex.json").exists(),
        "extra_evidence_collected": (edir / "github.json").exists() or (edir / "doaj.json").exists(),
        "venue_checked": (edir / "venues.json").exists(),
        "llm_review_completed": n_reviews > 0,
        "confidence_gate_completed": True,
        "final_report_ready": True,  # 09 will only run if 08 succeeds
    }


def evidence_quality_0to5(topic_id: str, sources: int) -> int:
    """Per-topic evidence quality based on source diversity, kept-paper count, and median relevance."""
    rows = read_csv(DEDUP_DIR / f"{topic_id}.csv") if (DEDUP_DIR / f"{topic_id}.csv").exists() else []
    n_kept = len(rows)
    rels = []
    for r in rows:
        try:
            rels.append(float(r.get("relevance_score") or 0))
        except Exception:
            pass
    rels.sort()
    median_rel = rels[len(rels) // 2] if rels else 0.0
    score = 0
    score += min(2, sources)              # 0..2: API source diversity
    score += 1 if n_kept >= 10 else 0     # enough kept papers
    score += 1 if n_kept >= 25 else 0
    score += 1 if median_rel >= 0.4 else 0
    return min(5, score)


def gate_topic(topic_id: str, allow_go_without_llm: bool = False) -> dict[str, Any]:
    score = read_json(SCORES_DIR / f"{topic_id}.json", {})
    agree = read_json(AGREE_DIR / f"{topic_id}.json", {})
    overall = score.get("rubric", {}).get("composites", {}).get("Overall", 0)
    cit = score.get("citation_signal_0to5", 0)
    art = score.get("artifact", {}).get("artifact_opportunity_0to5", 0)
    art_density = score.get("artifact", {}).get("existing_artifact_density", 0)
    differentiator_required = score.get("artifact", {}).get("differentiator_required", False)
    sat = score.get("saturation", {}).get("saturation_score_0to5", 0)
    ven = score.get("venue", {}).get("venue_signal_0to5", 0)
    ip_risk = score.get("risk", {}).get("ip_risk_0to5", 0)
    relevance_purity = score.get("relevance_purity", 0)
    kept_papers = score.get("kept_papers", 0)

    plurality = agree.get("plurality_decision", "NEEDS_MORE_EVIDENCE")
    dscore = agree.get("decision_score_mean_0to3", 0)
    high_drops = agree.get("high_confidence_drops", 0)
    disagree = agree.get("high_disagreement_flag", False)
    n_revs = agree.get("n_reviews", 0)

    sources = n_sources(topic_id)
    comp = completeness(topic_id, n_revs)
    eq = evidence_quality_0to5(topic_id, sources)

    # ---- Existing-work signals (from 12_detect_existing_work, if run) ----------
    ew = read_json(EW_DIR / f"{topic_id}.json", {}) or {}
    ew_go_blocked          = bool(ew.get("go_blocked", False))
    ew_requires_diff       = bool(ew.get("requires_differentiator", False))
    ew_diff_strength       = ew.get("differentiator_strength", "strong")   # default: assume clear
    ew_n_direct            = int(ew.get("n_direct", 0))
    ew_n_partial           = int(ew.get("n_partial", 0))
    ew_available           = bool(ew)

    reasons: list[str] = []
    extra_needed: list[str] = []
    manual_checks: list[str] = []

    # Propagate existing-work manual checks
    if ew_available and ew_go_blocked:
        manual_checks.append(
            f"Existing-work detection blocked GO: {ew_n_direct} direct overlap(s), "
            f"differentiator_strength={ew_diff_strength}. "
            f"See reports/topic_reports/{topic_id}_existing_work.md"
        )
    elif ew_available and ew_requires_diff:
        manual_checks.append(
            f"Existing-work: {ew_n_direct} direct + {ew_n_partial} partial overlaps — "
            f"articulate differentiator before GO. "
            f"See reports/topic_reports/{topic_id}_existing_work.md"
        )

    decision = "NEEDS_MORE_EVIDENCE"

    # ---- DROP rules
    if cit == 0 and score.get("paper", {}).get("n_papers", 0) < 5:
        decision = "DROP"; reasons.append("Citation signal 0 with <5 papers found.")
    elif art <= 1 and cit <= 2:
        decision = "DROP"; reasons.append("Low artifact opportunity and weak citation audience.")
    elif sat == 5 and art <= 2:
        decision = "DROP"; reasons.append("Topic saturated (sat=5) with no differentiator (art<=2).")
    elif ip_risk >= 4:
        decision = "DROP"; reasons.append("High IP/employer risk flags.")
    elif n_revs >= 4 and plurality == "DROP" and high_drops >= 2:
        decision = "DROP"; reasons.append("Reviewer panel plurality DROP with multiple high-confidence drops.")

    # ---- GO rules: require LLM unless explicit override
    require_llm = bool(CFG.get("gate_require_llm_for_go", True)) and not allow_go_without_llm
    if decision != "DROP":
        go_conditions = [
            overall >= int(CFG["gate_overall_min_for_go"]),
            cit >= int(CFG["gate_citation_min_for_go"]),
            art >= int(CFG["gate_artifact_min_for_go"]),
            ven >= int(CFG["gate_venue_min_for_go"]),
            ip_risk <= int(CFG["gate_ip_max_for_go"]),
            sat <= int(CFG["gate_saturation_max_for_go"]),
            sources >= int(CFG["gate_min_evidence_sources"]),
            relevance_purity >= 0.4,
            eq >= 3,
            not ew_go_blocked,   # existing-work gate: block if DIRECT_OVERLAP + weak diff
        ]
        reviewer_go = (n_revs > 0 and plurality == "GO" and dscore >= float(CFG["gate_min_review_decision_score"]))
        llm_ok = (n_revs > 0) or not require_llm
        if all(go_conditions) and llm_ok and (reviewer_go or not require_llm) and not disagree:
            decision = "GO"
            reasons.append(f"Overall={overall} and signals meet GO thresholds; LLM={'panel-go' if reviewer_go else 'override'}.")

    # ---- NARROW rules
    if decision not in ("GO", "DROP"):
        if sat >= 4 and art >= 3:
            decision = "NARROW"
            reasons.append("Crowded broad topic, but artifact opportunity exists in a sub-gap.")
        elif cit >= 3 and overall < int(CFG["gate_overall_min_for_go"]) and ven >= 2:
            decision = "NARROW"
            reasons.append("Audience exists; framing too broad for current venue path.")
        elif differentiator_required and art >= 3:
            decision = "NARROW"
            reasons.append("Existing artifact density is high; topic must commit to a clear differentiator.")

    # ---- NEEDS_MORE_EVIDENCE: emit specific extra steps
    if decision == "NEEDS_MORE_EVIDENCE":
        if sources < 2:
            extra_needed.append("Re-run 02_collect_topic_evidence with expanded synonyms/year-range.")
        if ven == 0:
            extra_needed.append("Re-run 04_collect_venue_evidence with expanded venue candidates.")
            manual_checks.append("Visit candidate venue official site to confirm APC + indexing.")
        if disagree:
            extra_needed.append("Re-run 06_llm_review with refreshed packet (more papers, more venue evidence).")
        if kept_papers < 10:
            extra_needed.append("Expand keyword set; relevance filter dropped most candidates.")
        if relevance_purity < 0.3:
            extra_needed.append("Tighten queries: median relevance below 0.3 — too many off-topic results.")
        if not comp["llm_review_completed"]:
            manual_checks.append("Run `claude auth login` once, then re-run scripts/06_llm_review_topics.py.")

    # ---- Confidence rules
    # Hard rule: if no LLM reviews ran, can't be MEDIUM/HIGH.
    raw_conf = (
        "HIGH" if (decision in ("GO", "DROP") and not disagree and n_revs >= 6)
        else "MEDIUM" if (decision in ("GO", "DROP", "NARROW") and not disagree)
        else "LOW"
    )
    if bool(CFG.get("gate_force_low_when_no_reviews", True)) and n_revs == 0:
        final_confidence = "LOW"
    else:
        final_confidence = raw_conf

    status = "PRELIMINARY_HEURISTIC_ONLY" if n_revs == 0 else "FULL_REVIEW_COMPLETE"

    payload = {
        "topic_id": topic_id,
        "final_decision": decision,
        "final_confidence": final_confidence,
        "status": status,
        "reasoning_summary": "; ".join(reasons) or "Insufficient evidence to commit.",
        "manual_checks_required": manual_checks,
        "extra_verification_needed": extra_needed,
        "completeness": comp,
        "evidence_quality_0to5": eq,
        "relevance_purity": relevance_purity,
        "differentiator_required": differentiator_required,
        "existing_artifact_density": art_density,
        "existing_work": {
            "available": ew_available,
            "n_direct": ew_n_direct,
            "n_partial": ew_n_partial,
            "differentiator_strength": ew_diff_strength,
            "go_blocked": ew_go_blocked,
            "requires_differentiator": ew_requires_diff,
        },
        "signals": {
            "Overall": overall,
            "citation_signal_0to5": cit,
            "artifact_0to5": art,
            "saturation_0to5": sat,
            "venue_signal_0to5": ven,
            "ip_risk_0to5": ip_risk,
            "niw_0to5": score.get("niw_0to5"),
            "eb1a_0to5": score.get("eb1a_0to5"),
            "career_0to5": score.get("career_0to5"),
            "plurality": plurality,
            "decision_score_mean_0to3": dscore,
            "high_confidence_drops": high_drops,
            "high_disagreement_flag": disagree,
            "evidence_sources": sources,
            "kept_papers": kept_papers,
            "n_reviews": n_revs,
        },
    }
    log("08_gate", f"{topic_id} decision={decision} conf={final_confidence} status={status}")
    return payload


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--topic", default=None)
    p.add_argument("--allow-go-without-llm", action="store_true",
                    help="Override: permit GO when the LLM panel did not run.")
    args = p.parse_args(argv)

    files = sorted(QUERIES_DIR.glob("*.json"))
    if args.topic:
        files = [f for f in files if f.stem == args.topic]
    rows = []
    for f in files:
        q = read_json(f)
        if not q:
            continue
        d = gate_topic(q["topic"]["topic_id"], allow_go_without_llm=args.allow_go_without_llm)
        write_json(DECISIONS_DIR / f"{d['topic_id']}.json", d)
        flat = {
            "topic_id": d["topic_id"],
            "final_decision": d["final_decision"],
            "final_confidence": d["final_confidence"],
            "status": d["status"],
            "Overall": d["signals"]["Overall"],
            "citation_signal": d["signals"]["citation_signal_0to5"],
            "artifact": d["signals"]["artifact_0to5"],
            "differentiator_required": d["differentiator_required"],
            "existing_artifact_density": d["existing_artifact_density"],
            "saturation": d["signals"]["saturation_0to5"],
            "venue_signal": d["signals"]["venue_signal_0to5"],
            "ip_risk": d["signals"]["ip_risk_0to5"],
            "niw": d["signals"]["niw_0to5"],
            "eb1a": d["signals"]["eb1a_0to5"],
            "career": d["signals"]["career_0to5"],
            "evidence_sources": d["signals"]["evidence_sources"],
            "kept_papers": d["signals"]["kept_papers"],
            "evidence_quality_0to5": d["evidence_quality_0to5"],
            "relevance_purity": d["relevance_purity"],
            "n_reviews": d["signals"]["n_reviews"],
            "high_disagreement": d["signals"]["high_disagreement_flag"],
            "reasoning_summary": d["reasoning_summary"],
        }
        rows.append(flat)
    rows.sort(key=lambda r: ({"GO": 0, "NARROW": 1, "NEEDS_MORE_EVIDENCE": 2, "DROP": 3}[r["final_decision"]], -r["Overall"]))
    write_csv(DECISIONS_DIR / "decisions.csv", rows)
    print(json.dumps(rows, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
