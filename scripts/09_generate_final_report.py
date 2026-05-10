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
