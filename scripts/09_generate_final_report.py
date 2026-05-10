"""
09_generate_final_report.py

Render reports/final_decision_report.md with:
- top-level status banner (FULL_REVIEW_COMPLETE | PRELIMINARY_HEURISTIC_ONLY)
- explicit warning when LLM panel did not run
- evidence-quality + relevance-purity surfaced for top 3
- per-topic completeness + manual checks remaining
"""
from __future__ import annotations
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.io_utils import read_csv, read_json  # noqa: E402

DECISIONS_DIR = ROOT / "data" / "decisions"
SCORES_DIR    = ROOT / "data" / "scores"
AGREE_DIR     = ROOT / "data" / "agreement"
QUERIES_DIR   = ROOT / "data" / "queries"
DEDUP_DIR     = ROOT / "data" / "papers_dedup"
EW_DIR        = ROOT / "data" / "existing_work"   # from 12_detect_existing_work
REPORT_PATH   = ROOT / "reports" / "final_decision_report.md"
LLM_ERRORS_PATH = ROOT / "reports" / "llm_review_errors.md"


def _topics() -> list[dict[str, Any]]:
    out = []
    for f in sorted(QUERIES_DIR.glob("*.json")):
        q = read_json(f)
        if q:
            out.append(q["topic"])
    return out


def _decision(tid: str) -> dict[str, Any]:
    return read_json(DECISIONS_DIR / f"{tid}.json", {}) or {}


def _score(tid: str) -> dict[str, Any]:
    return read_json(SCORES_DIR / f"{tid}.json", {}) or {}


def _agree(tid: str) -> dict[str, Any]:
    return read_json(AGREE_DIR / f"{tid}.json", {}) or {}


def _ew(tid: str) -> dict[str, Any]:
    """Load existing-work summary for topic (from 12_detect_existing_work)."""
    return read_json(EW_DIR / f"{tid}.json", {}) or {}


def _section_top_papers(tid: str, k: int = 5) -> str:
    rows = read_csv(DEDUP_DIR / f"{tid}.csv") if (DEDUP_DIR / f"{tid}.csv").exists() else []
    def _rel(x):
        try:
            return float(x.get("relevance_score") or 0)
        except Exception:
            return 0.0
    def _ci(x):
        try:
            return int(x.get("citations") or 0)
        except Exception:
            return 0
    rows.sort(key=lambda r: (_rel(r), _ci(r)), reverse=True)
    if not rows:
        return "_(no relevant papers kept after relevance filter)_"
    out = ["| Rel | Year | Cit | Title | Venue | DOI | Why included |",
           "|---|---|---|---|---|---|---|"]
    for r in rows[:k]:
        title = (r.get("title") or "").replace("|", "/")[:120]
        venue = (r.get("venue") or "").replace("|", "/")[:60]
        doi = (r.get("doi") or "").replace("|", "/")[:60]
        why = (r.get("reason_included") or "").replace("|", "/")[:120]
        out.append(f"| {r.get('relevance_score','-')} | {r.get('year','')} | {r.get('citations',0)} | "
                   f"{title} | {venue} | {doi} | {why} |")
    return "\n".join(out)


def _bucket(decisions: list[tuple[dict[str, Any], dict[str, Any]]], target: str):
    return [(t, d) for t, d in decisions if d.get("final_decision") == target]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=str(REPORT_PATH))
    args = p.parse_args(argv)

    topics = _topics()
    decisions = [(t, _decision(t["topic_id"])) for t in topics]
    decisions = [(t, d) for t, d in decisions if d]
    decisions.sort(key=lambda td: (
        {"GO": 0, "NARROW": 1, "NEEDS_MORE_EVIDENCE": 2, "DROP": 3}.get(td[1].get("final_decision", "NEEDS_MORE_EVIDENCE"), 4),
        -td[1].get("signals", {}).get("Overall", 0),
    ))

    # ---- status banner
    statuses = [d.get("status", "PRELIMINARY_HEURISTIC_ONLY") for _, d in decisions]
    n_full = sum(1 for s in statuses if s == "FULL_REVIEW_COMPLETE")
    n_prelim = sum(1 for s in statuses if s == "PRELIMINARY_HEURISTIC_ONLY")
    overall_status = "FULL_REVIEW_COMPLETE" if n_prelim == 0 and n_full > 0 else "PRELIMINARY_HEURISTIC_ONLY"
    llm_ran_anywhere = any((d.get("signals", {}).get("n_reviews", 0) or 0) > 0 for _, d in decisions)

    md: list[str] = []
    md.append(f"# Final decision report\n")
    md.append(f"Generated: {datetime.utcnow().isoformat()}Z\n")
    md.append(f"**Report status: `{overall_status}`**\n")
    if not llm_ran_anywhere:
        md.append(
            "> ⚠️ **WARNING — LLM REVIEW NOT RUN.** "
            "All decisions in this report come from heuristic / evidence-only signals. "
            "No topic can be promoted to GO until the Claude CLI panel runs (or `--allow-go-without-llm` is passed). "
            f"See `reports/llm_review_errors.md` (exists: {LLM_ERRORS_PATH.exists()}).\n"
        )
    else:
        md.append(f"- Topics with full LLM review: **{n_full}** / {len(decisions)}")
        md.append(f"- Topics still PRELIMINARY: **{n_prelim}** / {len(decisions)}\n")

    # ---- 1. Executive summary
    counts = {k: len(_bucket(decisions, k)) for k in ("GO", "NARROW", "NEEDS_MORE_EVIDENCE", "DROP")}
    md.append("## 1. Executive summary\n")
    md.append(f"- Topics evaluated: **{len(decisions)}**")
    md.append(f"- GO: **{counts['GO']}**  NARROW: **{counts['NARROW']}**  "
              f"NEEDS_MORE_EVIDENCE: **{counts['NEEDS_MORE_EVIDENCE']}**  DROP: **{counts['DROP']}**\n")

    # ---- 2. Final ranked topics
    md.append("## 2. Final ranked topics\n")
    md.append("| Rank | Topic | Decision | Conf | Status | Overall | Cit | Art | Sat | Ven | IP | NIW | EB1A | Carr | EvQ | RelP | Sources | n_reviews | Disagree |")
    md.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, (t, d) in enumerate(decisions, 1):
        s = d.get("signals", {})
        md.append(
            f"| {i} | {t['topic_id']}: {t['title'][:70]} | **{d.get('final_decision','-')}** | "
            f"{d.get('final_confidence','-')} | {d.get('status','-').replace('_',' ')[:12]} | "
            f"{s.get('Overall','-')} | {s.get('citation_signal_0to5','-')} | {s.get('artifact_0to5','-')} | "
            f"{s.get('saturation_0to5','-')} | {s.get('venue_signal_0to5','-')} | {s.get('ip_risk_0to5','-')} | "
            f"{s.get('niw_0to5','-')} | {s.get('eb1a_0to5','-')} | {s.get('career_0to5','-')} | "
            f"{d.get('evidence_quality_0to5','-')} | {d.get('relevance_purity','-')} | "
            f"{s.get('evidence_sources','-')} | {s.get('n_reviews','-')} | "
            f"{'Y' if s.get('high_disagreement_flag') else 'N'} |"
        )
    md.append("")

    # ---- 2.5 Active scoring profile + negative-control sentinel banner
    active_profile_name = "blind_citation"
    personal_goals_included = False
    nc_sentinel_status = {"available": False}
    if decisions:
        first_d = decisions[0][1]
        active_profile_name = first_d.get("active_profile", "blind_citation")
        nc_sentinel_status = first_d.get("negative_control_sentinel", {"available": False})
    # Detect personal-goal reviewer inclusion by inspecting one packet
    packets_dir = ROOT / "data" / "reviews"
    if packets_dir.exists():
        for sub in packets_dir.iterdir():
            if sub.is_dir() and (sub / "claude_cli_niw_eb1a.json").exists():
                personal_goals_included = True
                break

    md.append("## 2.5 Scoring Configuration\n")
    profile_yaml = ROOT / "config" / "weight_profiles.yaml"
    md.append(f"- **Active scoring profile**: `{active_profile_name}`")
    md.append(f"- **Personal-goal LLM reviewers (niw_eb1a, career_faang) included**: "
              f"{'YES' if personal_goals_included else 'NO (default)'}")
    md.append(f"- **Profile config**: `{profile_yaml.relative_to(ROOT)}`")
    if nc_sentinel_status.get("available"):
        leaky = nc_sentinel_status.get("leaky_profiles") or []
        if active_profile_name in leaky:
            md.append(f"- **Negative-control sentinel**: ⚠️ **SCORING_LEAK_DETECTED** "
                      f"(NC topics rank in top half under `{active_profile_name}`)")
        else:
            md.append(f"- **Negative-control sentinel**: ✅ TIGHT under `{active_profile_name}` "
                      f"(no NC topic in top half)")
    else:
        md.append(f"- **Negative-control sentinel**: not yet computed "
                  f"(run `python scripts/13_bias_audit.py`)")

    # Active-profile weights table
    try:
        from common.profiles import load_profiles
        all_profiles = load_profiles()
        active_weights = (all_profiles.get(active_profile_name) or {}).get("weights") or {}
        if active_weights:
            md.append("\n#### Active profile weights\n")
            md.append("| Component | Weight | Status |")
            md.append("|---|---|---|")
            for c, w in active_weights.items():
                status_label = "🟢 active" if abs(float(w)) > 0.001 else "⚪ disabled"
                md.append(f"| `{c}` | {w} | {status_label} |")
            md.append("")
    except Exception:
        pass

    # ---- 2.6 Profile Comparison Table (across all 13 profiles)
    pr_csv = ROOT / "data" / "bias_audit" / "profile_rankings.csv"
    if pr_csv.exists():
        import csv as _csv
        rows = list(_csv.DictReader(pr_csv.open(encoding="utf-8")))
        if rows:
            md.append("\n## 2.6 Profile Comparison Table\n")
            md.append("Each topic's rank under each weighting profile. "
                      "`rank_range` = max-min across profiles "
                      "(high values = bias-sensitive ranking).\n")
            profile_cols = [k for k in rows[0].keys() if k.startswith("rank_") and not k in ("rank_min","rank_max","rank_range","rank_mean")]
            short = {p: p.replace("rank_", "")[:8] for p in profile_cols}
            header = ["Topic"] + [short[p] for p in profile_cols] + ["min","max","range"]
            md.append("| " + " | ".join(header) + " |")
            md.append("|" + "|".join(["---"] * len(header)) + "|")
            rows.sort(key=lambda r: float(r.get("rank_mean") or 99))
            for r in rows:
                vals = [r["topic_id"]]
                for p in profile_cols:
                    vals.append(str(r.get(p, "-")))
                vals.append(str(r.get("rank_min", "-")))
                vals.append(str(r.get("rank_max", "-")))
                vals.append(str(r.get("rank_range", "-")))
                md.append("| " + " | ".join(vals) + " |")
            md.append("")

            # Robustness sub-sections
            robust = [r for r in rows
                      if int(r.get("rank_max", 99)) <= 6 and int(r.get("rank_range", 99)) <= 6]
            collapse_bc = [r for r in rows
                           if int(r.get("rank_blind_citation", 99)) > len(rows) // 2]
            personal_only = [r for r in rows
                             if int(r.get("rank_blind_citation", 99)) > len(rows) // 2
                             and (int(r.get("rank_niw_optimized", 99)) <= 5
                                  or int(r.get("rank_eb1a_optimized", 99)) <= 5
                                  or int(r.get("rank_faang_career", 99)) <= 5)]
            strong_both = [r for r in rows
                           if int(r.get("rank_blind_citation", 99)) <= 5
                           and (int(r.get("rank_niw_optimized", 99)) <= 8
                                or int(r.get("rank_eb1a_optimized", 99)) <= 8
                                or int(r.get("rank_faang_career", 99)) <= 8)]

            md.append("### 2.6a Topics robust across profiles (rank ≤ 6 in all profiles)\n")
            md.append(", ".join(r["topic_id"] for r in robust) or "_None._")
            md.append("\n### 2.6b Topics that rank high only under personal-goal profiles\n")
            md.append(", ".join(r["topic_id"] for r in personal_only) or "_None._")
            md.append("\n### 2.6c Topics that collapse under blind_citation\n")
            md.append(", ".join(r["topic_id"] for r in collapse_bc) or "_None._")
            md.append("\n### 2.6d Topics strong academically AND useful for personal goals\n")
            md.append(", ".join(r["topic_id"] for r in strong_both) or "_None._")
            md.append("\n### 2.6e Topics to ignore (only win under biased weighting)\n")
            md.append(", ".join(r["topic_id"] for r in personal_only) or "_None._")
            md.append("")

    # ---- 2.7 Personal-goal overlay (after neutral ranking; does not change rank)
    md.append("\n## 2.7 Personal-goal Overlay\n")
    md.append("This section applies AFTER the neutral blind_citation ranking. "
              "Personal-goal overlays do NOT change the academic ranking — they "
              "help select among already-academically-acceptable topics.\n")
    # Get topics acceptable under blind_citation
    bc_acceptable_topics = []
    for t, d in decisions:
        if d.get("blind_citation_acceptable", False):
            bc_acceptable_topics.append((t, d))

    md.append(f"### Best neutral topics ({len(bc_acceptable_topics)} acceptable under blind_citation)\n")
    if not bc_acceptable_topics:
        md.append("_No topic is currently acceptable under blind_citation._\n")
    else:
        # Sort by blind_citation score
        bc_acceptable_topics.sort(key=lambda td: -float(td[1].get("blind_citation_score", 0)))
        for t, d in bc_acceptable_topics[:8]:
            md.append(f"- **{t['topic_id']}**: {t['title']}  (BC score: {d.get('blind_citation_score', 0):.2f})")

        md.append("\n#### Among those, helpful for NIW")
        for t, d in bc_acceptable_topics:
            niw = float(d.get("signals", {}).get("niw_0to5", 0) or 0)
            if niw >= 4:
                md.append(f"- {t['topic_id']}: NIW={niw}")
        md.append("\n#### Among those, helpful for EB1A")
        for t, d in bc_acceptable_topics:
            eb1a = float(d.get("signals", {}).get("eb1a_0to5", 0) or 0)
            if eb1a >= 4:
                md.append(f"- {t['topic_id']}: EB1A={eb1a}")
        md.append("\n#### Among those, helpful for FAANG/career")
        for t, d in bc_acceptable_topics:
            cv = float(d.get("signals", {}).get("career_0to5", 0) or 0)
            if cv >= 4:
                md.append(f"- {t['topic_id']}: career={cv}")
        md.append("\n#### Among those, fit healthcare/high-stakes domains")
        for t, d in bc_acceptable_topics:
            cat = (t.get("category", "") or "").lower()
            if "health" in cat or "clinical" in cat:
                md.append(f"- {t['topic_id']}: category={cat}")
        md.append("\n#### Among those, with strong artifact potential")
        for t, d in bc_acceptable_topics:
            art = float(d.get("signals", {}).get("artifact_0to5", 0) or 0)
            if art >= 4:
                md.append(f"- {t['topic_id']}: artifact={art}")
        md.append("")

    # ---- 3-6 buckets
    for label in ("GO", "NARROW", "DROP", "NEEDS_MORE_EVIDENCE"):
        md.append(f"## {3 + ['GO','NARROW','DROP','NEEDS_MORE_EVIDENCE'].index(label)}. {label} topics\n")
        bucket = _bucket(decisions, label)
        if not bucket:
            md.append("_None._\n")
            continue
        for t, d in bucket:
            md.append(f"### {t['topic_id']} — {t['title']}")
            md.append(f"- Confidence: **{d.get('final_confidence','-')}**  ·  Status: **{d.get('status','-')}**")
            md.append(f"- Reasoning: {d.get('reasoning_summary','')}")
            comp = d.get("completeness", {})
            md.append(f"- Completeness: evidence={comp.get('evidence_collected', False)}, "
                      f"extra={comp.get('extra_evidence_collected', False)}, "
                      f"venue={comp.get('venue_checked', False)}, "
                      f"llm={comp.get('llm_review_completed', False)}, "
                      f"gate={comp.get('confidence_gate_completed', False)}")
            if d.get("manual_checks_required"):
                md.append("- Manual checks required:")
                for m in d["manual_checks_required"]:
                    md.append(f"  - {m}")
            if d.get("extra_verification_needed"):
                md.append("- Automated next-step suggestions:")
                for m in d["extra_verification_needed"]:
                    md.append(f"  - {m}")
            md.append("")

    # ---- 7 (omit, dup of DROP)

    # ---- 8. Top 3 recommended
    top3: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for label in ("GO", "NARROW", "NEEDS_MORE_EVIDENCE"):
        for t, d in _bucket(decisions, label):
            if len(top3) < 3:
                top3.append((t, d))
    md.append("## 8. Top 3 recommended topics\n")
    if not top3:
        md.append("_None — every topic was DROPped. Re-seed and rerun._\n")
    else:
        md.append("| # | Topic | Decision | Conf | Status | EvQ | RelP | Manual checks remaining |")
        md.append("|---|---|---|---|---|---|---|---|")
        for i, (t, d) in enumerate(top3, 1):
            mcr = "; ".join(d.get("manual_checks_required") or []) or "-"
            md.append(f"| {i} | {t['topic_id']}: {t['title'][:70]} | "
                      f"**{d.get('final_decision','-')}** | {d.get('final_confidence','-')} | "
                      f"{d.get('status','-')} | {d.get('evidence_quality_0to5','-')} | "
                      f"{d.get('relevance_purity','-')} | {mcr[:140]} |")
        md.append("")

    # ---- 9. Top-3 evidence (relevance-aware)
    md.append("## 9. Evidence table for top 3 (top 5 papers per topic, by relevance)\n")
    for t, _ in top3:
        md.append(f"### {t['topic_id']} — {t['title']}")
        md.append(_section_top_papers(t["topic_id"], k=5))
        md.append("")

    # ---- 10. Citation evidence
    md.append("## 10. Citation evidence summary\n")
    md.append("| Topic | n_papers | n_24mo | n_12mo | top_cit | growth_yoy | cit_signal |")
    md.append("|---|---|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        ps = s.get("paper", {})
        md.append(f"| {t['topic_id']} | {ps.get('n_papers','-')} | {ps.get('n_papers_24mo','-')} | "
                  f"{ps.get('n_papers_12mo','-')} | {ps.get('top_citation','-')} | "
                  f"{ps.get('growth_yoy_proxy','-')} | {s.get('citation_signal_0to5','-')} |")
    md.append("")

    # ---- 11. Novelty / saturation / artifact density
    md.append("## 11. Novelty / saturation / artifact density\n")
    md.append("| Topic | sat | dom_tools | big_ds | gap_hits | art | density | diff_required |")
    md.append("|---|---|---|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        sa = s.get("saturation", {})
        ar = s.get("artifact", {})
        md.append(f"| {t['topic_id']} | {sa.get('saturation_score_0to5','-')} | {sa.get('dominant_tools','-')} | "
                  f"{sa.get('big_datasets','-')} | {ar.get('gap_phrase_hits','-')} | "
                  f"{ar.get('artifact_opportunity_0to5','-')} | {ar.get('existing_artifact_density','-')} | "
                  f"{ar.get('differentiator_required','-')} |")
    md.append("")

    # ---- 12. Venue / no-APC
    md.append("## 12. Venue / no-APC evidence\n")
    md.append("| Topic | venue_signal | doaj_no_apc | crossref_active | openreview_hits |")
    md.append("|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        v = s.get("venue", {})
        md.append(f"| {t['topic_id']} | {v.get('venue_signal_0to5','-')} | {v.get('doaj_no_apc_journals','-')} | "
                  f"{v.get('crossref_active_venues','-')} | {v.get('openreview_hits','-')} |")
    md.append("")

    # ---- 13. Artifact / reproducibility
    md.append("## 13. Artifact / reproducibility evidence\n")
    md.append("| Topic | art | gap_hits | pwc_datasets | hf_datasets | density |")
    md.append("|---|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        a = s.get("artifact", {})
        md.append(f"| {t['topic_id']} | {a.get('artifact_opportunity_0to5','-')} | {a.get('gap_phrase_hits','-')} | "
                  f"{a.get('n_existing_pwc_datasets','-')} | {a.get('n_existing_hf_datasets','-')} | "
                  f"{a.get('existing_artifact_density','-')} |")
    md.append("")

    # ---- 14 NIW / EB1A
    md.append("## 14. NIW / EB-1A evidence summary\n")
    md.append("| Topic | NIW | EB1A | Career | ImmigrationValue | CareerValue |")
    md.append("|---|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        c = s.get("rubric", {}).get("composites", {})
        md.append(f"| {t['topic_id']} | {s.get('niw_0to5','-')} | {s.get('eb1a_0to5','-')} | "
                  f"{s.get('career_0to5','-')} | {c.get('ImmigrationValue','-')} | {c.get('CareerValue','-')} |")
    md.append("")

    # ---- 15 Career
    md.append("## 15. Career / FAANG evidence summary\n")
    md.append("| Topic | Career | Tool | Artifact | CareerValue |")
    md.append("|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        c = s.get("rubric", {}).get("composites", {})
        md.append(f"| {t['topic_id']} | {s.get('career_0to5','-')} | {s.get('tool_potential_0to5','-')} | "
                  f"{s.get('artifact', {}).get('artifact_opportunity_0to5','-')} | {c.get('CareerValue','-')} |")
    md.append("")

    # ---- 16 IP risk
    md.append("## 16. IP / employer-risk summary\n")
    md.append("| Topic | ip_risk | flags |")
    md.append("|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        r = s.get("risk", {})
        md.append(f"| {t['topic_id']} | {r.get('ip_risk_0to5','-')} | {', '.join(r.get('ip_risk_flags', [])) or '-'} |")
    md.append("")

    # ---- 17 LLM agreement
    md.append("## 17. LLM reviewer agreement\n")
    md.append("| Topic | n_reviews | plurality | dec_score | high_drops | disagree | per-role disagreements |")
    md.append("|---|---|---|---|---|---|---|")
    for t, _ in decisions:
        a = _agree(t["topic_id"])
        roles = ", ".join(d.get("role", "") for d in (a.get("per_role_disagreements") or [])) or "-"
        md.append(f"| {t['topic_id']} | {a.get('n_reviews','-')} | {a.get('plurality_decision','-')} | "
                  f"{a.get('decision_score_mean_0to3','-')} | {a.get('high_confidence_drops','-')} | "
                  f"{'Y' if a.get('high_disagreement_flag') else 'N'} | {roles} |")
    md.append("")

    # ---- 18. Existing Work Summary (from 12_detect_existing_work, if run)
    ew_summary_path = EW_DIR / "_summary.json"
    ew_summary = read_json(ew_summary_path, {}) or {}
    ew_by_topic: dict[str, Any] = ew_summary.get("by_topic", {})
    ew_ran = bool(ew_summary)

    md.append("## 18. Existing Work Detection\n")
    if not ew_ran:
        md.append(
            "> ℹ️ **Existing Work Detection not run** — `data/existing_work/_summary.json` missing. "
            "Run `python scripts/12_detect_existing_work.py` to populate this section.\n"
        )
    else:
        # Source-type breakdown table
        md.append("| Topic | Paper Direct | Artifact Direct | (GH / HF / PWC) | Peer-Rev? | High-Art? | Art-Diff-Req | Art-Diff | Paper-Diff | GO Blocked |")
        md.append("|---|---|---|---|---|---|---|---|---|---|")
        for t, _ in decisions:
            tid = t["topic_id"]
            ew_t = ew_by_topic.get(tid, {})
            if not ew_t:
                md.append(f"| {tid} | — | — | — | — | — | — | — | — | — |")
                continue
            peer_rev  = "✅" if ew_t.get("peer_reviewed_direct_overlap") else "—"
            high_art  = "⚠️" if ew_t.get("high_artifact_overlap") else "—"
            art_diff_req = "Yes" if ew_t.get("artifact_differentiator_required") else "—"
            blocked_disp = "⛔ YES" if ew_t.get("go_blocked") else "No"
            gh  = ew_t.get("direct_github_count", "—")
            hf  = ew_t.get("direct_hf_count", "—")
            pwc = ew_t.get("direct_pwc_count", "—")
            md.append(
                f"| {tid} "
                f"| {ew_t.get('direct_paper_count', '—')} "
                f"| {ew_t.get('artifact_direct_count', '—')} "
                f"| {gh}/{hf}/{pwc} "
                f"| {peer_rev} "
                f"| {high_art} "
                f"| {art_diff_req} "
                f"| `{ew_t.get('artifact_differentiator_strength', '—')}` "
                f"| `{ew_t.get('paper_differentiator_strength', ew_t.get('differentiator_strength', '—'))}` "
                f"| {blocked_disp} |"
            )
        md.append("")

        # §18a — Direct Overlap Risks
        blocked = ew_summary.get("go_blocked_topics", [])
        md.append("### 18a. Direct Overlap Risks (GO-blocked topics)\n")
        if not blocked:
            md.append("_No topics blocked by existing-work gate._\n")
        else:
            for tid in blocked:
                ew_t = ew_by_topic.get(tid, {})
                peer_rev_direct = ew_t.get("direct_paper_count", 0)
                art_direct      = ew_t.get("artifact_direct_count", 0)
                report_link = f"reports/topic_reports/{tid}_existing_work.md"
                if peer_rev_direct > 0:
                    md.append(
                        f"- **{tid}** — {peer_rev_direct} peer-reviewed DIRECT paper(s), "
                        f"paper_diff=`{ew_t.get('paper_differentiator_strength', '?')}`. "
                        f"Details: `{report_link}`"
                    )
                else:
                    md.append(
                        f"- **{tid}** — 0 peer-reviewed papers, {art_direct} direct artifacts, "
                        f"artifact_diff=`{ew_t.get('artifact_differentiator_strength', '?')}`. "
                        f"Details: `{report_link}`"
                    )
            md.append("")

        # §18b — Differentiator Required
        need_diff = ew_summary.get("requires_differentiator_topics", [])
        md.append("### 18b. Differentiator Required Topics\n")
        if not need_diff:
            md.append("_No additional topics require a differentiator._\n")
        else:
            for tid in need_diff:
                ew_t = ew_by_topic.get(tid, {})
                md.append(
                    f"- **{tid}** — paper_direct={ew_t.get('direct_paper_count', 0)}, "
                    f"artifact_direct={ew_t.get('artifact_direct_count', 0)}. "
                    f"Articulate gap before GO."
                )
            md.append("")

        # §18c — Recommended DROP / NARROW from paper overlap
        md.append("### 18c. Recommended action based on existing-work findings\n")
        drop_candidates = [
            tid for tid in blocked
            if ew_by_topic.get(tid, {}).get("paper_differentiator_strength",
               ew_by_topic.get(tid, {}).get("differentiator_strength", "strong")) == "none"
            and ew_by_topic.get(tid, {}).get("peer_reviewed_direct_overlap", False)
        ]
        narrow_candidates = [tid for tid in (blocked + need_diff) if tid not in drop_candidates]
        if drop_candidates:
            md.append(f"**Consider DROP** (peer-reviewed overlap, paper_diff=`none`): {', '.join(drop_candidates)}")
        if narrow_candidates:
            md.append(f"**Consider additional NARROW** (overlaps found, but may be salvageable): {', '.join(narrow_candidates)}")
        if not drop_candidates and not narrow_candidates:
            md.append("_No DROP/NARROW recommendations from existing-work analysis._")
        md.append("")

        # §18d — Artifact-only high-overlap topics
        art_only_topics = ew_summary.get("artifact_only_high_overlap_topics", [])
        md.append("### 18d. Artifact-Only High-Overlap Topics\n")
        if not art_only_topics:
            md.append("_No topics with high artifact overlap and zero peer-reviewed paper overlap._\n")
        else:
            md.append(
                "> 📌 **For these topics:** Academic/paper overlap is absent, but GitHub/HF artifact "
                "overlap is high. They may still be publishable — a peer-reviewed benchmark/protocol "
                "with a clear domain or methodological focus is inherently different from repos/datasets. "
                "Each topic must explicitly state: (1) peer-reviewed systematic protocol vs existing repos; "
                "(2) specific domain/use-case vs general artifacts; (3) evaluation harness + paper.\n"
            )
            md.append("| Topic | Artifact Direct | Art-Diff | Artifact Differentiator Required |")
            md.append("|---|---|---|---|")
            for tid in art_only_topics:
                ew_t = ew_by_topic.get(tid, {})
                ew_full = _ew(tid)   # read full per-topic JSON for richer data
                md.append(
                    f"| **{tid}** "
                    f"| {ew_t.get('artifact_direct_count', '?')} "
                    f"| `{ew_t.get('artifact_differentiator_strength', '?')}` "
                    f"| {'Yes — see checklist in per-topic report' if ew_t.get('artifact_differentiator_required') else 'No'} |"
                )
            md.append("")

    # ---- 19 Manual checks remaining
    md.append("## 19. Remaining manual checks\n")
    manual: dict[str, list[str]] = {}
    for t, d in decisions:
        if d.get("manual_checks_required"):
            manual[t["topic_id"]] = d["manual_checks_required"]
    if not manual:
        md.append("_None per-topic. Universal manual items remain:_")
        md.append("- Verify TMLR no-APC + indexing on jmlr.org/tmlr (HTML, not API).")
        md.append("- Verify employer IP / moonlighting clause (legal).")
        md.append("- Verify any clinical dataset DUA permits your specific use (legal/contractual).")
        md.append("- Cross-check candidate venues against Think.Check.Submit.")
    else:
        for tid, items in manual.items():
            md.append(f"### {tid}")
            for m in items:
                md.append(f"- {m}")
    md.append("")

    # ---- 20 Final recommendation
    md.append("## 20. Final recommendation\n")
    if not llm_ran_anywhere:
        md.append("**Do not promote any topic to GO yet.** Run `claude auth login` once from PowerShell, then:\n")
        md.append("```\npython scripts/06_llm_review_topics.py\npython scripts/07_compare_reviewers.py\npython scripts/08_confidence_gate.py\npython scripts/09_generate_final_report.py\n```\n")
        md.append("If you must commit before LLM review (not recommended), pass `--allow-go-without-llm` to `08_confidence_gate.py` and document the override in `DECISIONS.md`.\n")
    elif top3:
        primary, ddec = top3[0]
        md.append(f"**Today**: open `data/decisions/{primary['topic_id']}.json` and `data/papers_dedup/{primary['topic_id']}.csv`; write a one-paragraph differentiator vs the 5 top-cited prior works (templates/08_proposal_one_pager.md).")
        md.append(f"**This week**: complete §6 verification log for the top {min(3, len(top3))} topics; commit primary + secondary in `DECISIONS.md` with kill criteria.")
        first_artifact = (read_json(SCORES_DIR / f"{primary['topic_id']}.json", {}) or {}).get("artifact", {}).get("artifact_opportunity_0to5", 0)
        if first_artifact >= 4:
            md.append("**Mode**: artifact-first (benchmark/dataset/database) paired with one paper.")
        elif first_artifact == 3:
            md.append("**Mode**: empirical paper with light reproducibility package.")
        else:
            md.append("**Mode**: paper-first; minimal scripts only.")
    else:
        md.append("**Do not start writing yet.** Re-seed topics or expand evidence rounds.")

    md.append("")
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote {args.out}  ({overall_status})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
