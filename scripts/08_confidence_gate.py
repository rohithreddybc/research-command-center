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
from common.profiles import (  # noqa: E402
    add_profile_args, resolve_profile, load_profiles, DEFAULT_PROFILE,
)

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


def _blind_citation_acceptable(topic_id: str, score: dict[str, Any],
                               ew: dict[str, Any], ranking_below_median: bool) -> tuple[bool, list[str]]:
    """Check whether a topic is "acceptable under blind_citation".

    Required for GO when active profile is a personal-goal profile.
    Returns (acceptable: bool, reasons_failed: [str])."""
    failed: list[str] = []
    if ranking_below_median:
        failed.append("topic ranks in the bottom half under blind_citation")
    if bool(ew.get("go_blocked", False)):
        failed.append("blocked by existing-work direct overlap")
    bc_score = float(score.get("profile_scores", {}).get(DEFAULT_PROFILE, {}).get("score", 0))
    if bc_score <= 0:
        failed.append(f"blind_citation score is non-positive ({bc_score})")
    rel_purity = float(score.get("relevance_purity", 0))
    if rel_purity < 0.3:
        failed.append(f"evidence quality too low (relevance_purity={rel_purity:.2f} < 0.30)")
    return (len(failed) == 0, failed)


def _negative_control_sentinel() -> dict[str, Any]:
    """Returns negative-control sentinel status from data/bias_audit/."""
    nc_file = ROOT / "data" / "bias_audit" / "negative_control_results.json"
    if not nc_file.exists():
        return {"available": False, "leak_detected": False, "leaky_profiles": []}
    try:
        data = json.loads(nc_file.read_text(encoding="utf-8"))
    except Exception:
        return {"available": False, "leak_detected": False, "leaky_profiles": []}
    leaky = []
    for prof_name, prof_result in (data.get("profiles") or {}).items():
        if prof_result.get("verdict") == "LEAKY":
            leaky.append(prof_name)
        elif prof_result.get("n_fail", 0) > 0:
            leaky.append(prof_name)
    return {
        "available":      True,
        "leak_detected":  bool(leaky),
        "leaky_profiles": leaky,
    }


def gate_topic(topic_id: str,
               allow_go_without_llm: bool = False,
               active_profile_name: str = DEFAULT_PROFILE,
               active_profile_is_personal_goal: bool = False,
               blind_citation_median: float | None = None,
               nc_sentinel: dict[str, Any] | None = None) -> dict[str, Any]:
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
    ew_go_blocked             = bool(ew.get("go_blocked", False))
    ew_requires_diff          = bool(ew.get("requires_differentiator", False))
    ew_diff_strength          = ew.get("differentiator_strength", "strong")   # paper diff (backward compat)
    ew_n_direct               = int(ew.get("n_direct", 0))
    ew_n_partial              = int(ew.get("n_partial", 0))
    ew_available              = bool(ew)
    # per-source fields (populated by updated 12_detect_existing_work)
    ew_peer_reviewed_direct   = bool(ew.get("peer_reviewed_direct_overlap", False))
    ew_artifact_direct        = bool(ew.get("artifact_direct_overlap", False))
    ew_high_artifact          = bool(ew.get("high_artifact_overlap", False))
    ew_artifact_diff_req      = bool(ew.get("artifact_differentiator_required", False))
    ew_artifact_diff_strength = ew.get("artifact_differentiator_strength", "strong")
    ew_direct_paper_count     = int(ew.get("direct_paper_count", 0))
    ew_artifact_direct_count  = int(ew.get("artifact_direct_count", 0))

    reasons: list[str] = []
    extra_needed: list[str] = []
    manual_checks: list[str] = []

    # Propagate existing-work manual checks — distinguish paper vs artifact overlap
    if ew_available and ew_go_blocked and ew_peer_reviewed_direct:
        manual_checks.append(
            f"Existing-work: {ew_direct_paper_count} peer-reviewed DIRECT overlap(s), "
            f"paper_diff_strength={ew_diff_strength}. "
            f"See reports/topic_reports/{topic_id}_existing_work.md"
        )
    elif ew_available and ew_go_blocked and not ew_peer_reviewed_direct:
        manual_checks.append(
            f"Existing-work: GO blocked by artifact overlap only "
            f"({ew_artifact_direct_count} direct artifacts, artifact_diff={ew_artifact_diff_strength}). "
            f"Complete artifact differentiator checklist — "
            f"see reports/topic_reports/{topic_id}_existing_work.md"
        )
    elif ew_available and ew_artifact_diff_req and not ew_peer_reviewed_direct:
        manual_checks.append(
            f"Existing-work: {ew_artifact_direct_count} direct artifacts "
            f"(no peer-reviewed paper overlap). "
            f"Complete artifact differentiator checklist — "
            f"see reports/topic_reports/{topic_id}_existing_work.md"
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

    # ---- BLIND-CITATION GATE: a personal-goal profile cannot promote to GO
    # unless the topic is also acceptable under blind_citation.
    nc = nc_sentinel or _negative_control_sentinel()
    bc_score_for_topic = float(score.get("profile_scores", {}).get(
        DEFAULT_PROFILE, {}).get("score", 0))

    ranking_below_median = False
    if blind_citation_median is not None:
        ranking_below_median = bc_score_for_topic < float(blind_citation_median)

    bc_acceptable, bc_failed = _blind_citation_acceptable(
        topic_id, score, ew, ranking_below_median,
    )

    personal_goal_only_weak = False
    nc_block_go = False

    # Flag "personal-goal-only-weak" if the active profile is a personal-goal
    # profile, the topic's personal-profile score is well above blind_citation
    # score, AND the blind_citation gate fails. This flag is set INDEPENDENTLY
    # of the current decision so a topic flagged here cannot later be promoted
    # to GO.
    if active_profile_is_personal_goal and not bc_acceptable:
        # Compare personal vs blind_citation score
        ps = float(score.get("profile_scores", {}).get(
            active_profile_name, {}).get("score", 0))
        if ps > bc_score_for_topic + 1.0:  # personal score notably higher
            personal_goal_only_weak = True
            if decision == "GO":
                decision = "NARROW"
            reasons.append(
                "PERSONAL_GOAL_ONLY_WEAK_TOPIC: rank under personal-goal profile "
                f"({active_profile_name}, score={ps:.2f}) is high but "
                f"blind_citation gate failed (BC score={bc_score_for_topic:.2f}): "
                + "; ".join(bc_failed)
            )

    # Negative-control sentinel: no GO if NC topics ranked in the top half
    # under the active profile.
    if (nc.get("available")
            and active_profile_name in (nc.get("leaky_profiles") or [])):
        nc_block_go = True
        if decision == "GO":
            decision = "NARROW"
            reasons.append(
                f"SCORING_LEAK_DETECTED: negative-control topics rank in top half "
                f"under profile '{active_profile_name}'. GO is blocked. See "
                f"data/bias_audit/negative_control_results.json"
            )

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
        elif (ew_available and ew_artifact_diff_req
              and not ew_peer_reviewed_direct
              and ew_high_artifact
              and ew_artifact_diff_strength not in ("weak", "none")):
            decision = "NARROW"
            reasons.append(
                f"High artifact overlap ({ew_artifact_direct_count} direct GitHub/HF/PWC artifacts), "
                "no peer-reviewed paper directly covers this — publishable with explicit artifact differentiator."
            )

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
        "active_profile":                 active_profile_name,
        "active_profile_is_personal_goal": active_profile_is_personal_goal,
        "blind_citation_acceptable":      bc_acceptable,
        "blind_citation_failed_reasons":  bc_failed,
        "blind_citation_score":           bc_score_for_topic,
        "personal_goal_only_weak_topic":  personal_goal_only_weak,
        "negative_control_sentinel":      nc,
        "negative_control_blocked_go":    nc_block_go,
        "profile_scores":                 score.get("profile_scores", {}),
        "existing_work": {
            "available":                   ew_available,
            "n_direct":                    ew_n_direct,
            "n_partial":                   ew_n_partial,
            "direct_paper_count":          ew_direct_paper_count,
            "artifact_direct_count":       ew_artifact_direct_count,
            "peer_reviewed_direct_overlap": ew_peer_reviewed_direct,
            "artifact_direct_overlap":     ew_artifact_direct,
            "high_artifact_overlap":       ew_high_artifact,
            "differentiator_strength":     ew_diff_strength,
            "artifact_differentiator_strength": ew_artifact_diff_strength,
            "artifact_differentiator_required": ew_artifact_diff_req,
            "go_blocked":                  ew_go_blocked,
            "requires_differentiator":     ew_requires_diff,
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
    add_profile_args(p)
    args = p.parse_args(argv)

    all_profiles = load_profiles()
    active_profile_name, active_profile = resolve_profile(args, all_profiles)
    is_personal = bool(active_profile.get("is_personal_goal", False))
    log("08_gate", f"Active profile: {active_profile_name} "
                   f"(personal_goal={is_personal})")

    files = sorted(QUERIES_DIR.glob("*.json"))
    if args.topic:
        files = [f for f in files if f.stem == args.topic]

    # Compute blind_citation median across all topics for the gate rule
    bc_scores: list[float] = []
    for f in files:
        s = read_json(SCORES_DIR / f"{f.stem}.json", {})
        bc = s.get("profile_scores", {}).get(DEFAULT_PROFILE, {}).get("score")
        if bc is not None:
            bc_scores.append(float(bc))
    bc_scores.sort()
    bc_median = bc_scores[len(bc_scores) // 2] if bc_scores else None
    nc_sentinel = _negative_control_sentinel()

    rows = []
    for f in files:
        q = read_json(f)
        if not q:
            continue
        d = gate_topic(q["topic"]["topic_id"],
                       allow_go_without_llm=args.allow_go_without_llm,
                       active_profile_name=active_profile_name,
                       active_profile_is_personal_goal=is_personal,
                       blind_citation_median=bc_median,
                       nc_sentinel=nc_sentinel)
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
