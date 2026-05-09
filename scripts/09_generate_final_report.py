"""
09_generate_final_report.py

Render reports/final_decision_report.md from data/decisions, data/scores,
data/agreement, and the evidence directories.

The report is structured to satisfy PHASE 7 of the user spec.
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
SCORES_DIR = ROOT / "data" / "scores"
AGREE_DIR = ROOT / "data" / "agreement"
QUERIES_DIR = ROOT / "data" / "queries"
DEDUP_DIR = ROOT / "data" / "papers_dedup"
REPORT_PATH = ROOT / "reports" / "final_decision_report.md"


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


def _section_top_papers(tid: str, k: int = 5) -> str:
    rows = read_csv(DEDUP_DIR / f"{tid}.csv") if (DEDUP_DIR / f"{tid}.csv").exists() else []
    def _ci(x):
        try:
            return int(x.get("citations") or 0)
        except Exception:
            return 0
    rows.sort(key=_ci, reverse=True)
    if not rows:
        return "_(no papers found)_"
    out = ["| Year | Citations | Title | Venue | DOI |", "|---|---|---|---|---|"]
    for r in rows[:k]:
        title = (r.get("title") or "").replace("|", "/")[:120]
        venue = (r.get("venue") or "").replace("|", "/")[:60]
        doi = (r.get("doi") or "").replace("|", "/")[:60]
        out.append(f"| {r.get('year','')} | {r.get('citations',0)} | {title} | {venue} | {doi} |")
    return "\n".join(out)


def _bucket(decisions: list[tuple[dict[str, Any], dict[str, Any]]], target: str) -> list[tuple[dict[str, Any], dict[str, Any]]]:
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

    md: list[str] = []
    md.append(f"# Final decision report\n\nGenerated: {datetime.utcnow().isoformat()}Z\n")
    md.append("All claims drawn from automated evidence collection. Items still requiring human judgment are listed in section 18.\n")

    # 1. Executive summary
    counts = {k: len(_bucket(decisions, k)) for k in ("GO", "NARROW", "NEEDS_MORE_EVIDENCE", "DROP")}
    md.append("## 1. Executive summary\n")
    md.append(f"- Topics evaluated: **{len(decisions)}**")
    md.append(f"- GO: **{counts['GO']}**  NARROW: **{counts['NARROW']}**  NEEDS_MORE_EVIDENCE: **{counts['NEEDS_MORE_EVIDENCE']}**  DROP: **{counts['DROP']}**")
    md.append("")

    # 2. Final ranked topics
    md.append("## 2. Final ranked topics\n")
    md.append("| Rank | Topic | Decision | Confidence | Overall | Cit | Art | Sat | Ven | IP | Sources | n_reviews | Disagree |")
    md.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, (t, d) in enumerate(decisions, 1):
        s = d.get("signals", {})
        md.append(
            f"| {i} | {t['topic_id']}: {t['title'][:80]} | **{d.get('final_decision','-')}** | {d.get('final_confidence','-')} | "
            f"{s.get('Overall','-')} | {s.get('citation_signal_0to5','-')} | {s.get('artifact_0to5','-')} | {s.get('saturation_0to5','-')} | "
            f"{s.get('venue_signal_0to5','-')} | {s.get('ip_risk_0to5','-')} | {s.get('evidence_sources','-')} | "
            f"{s.get('n_reviews','-')} | {'Y' if s.get('high_disagreement_flag') else 'N'} |"
        )
    md.append("")

    # 3-6 buckets
    for label in ("GO", "NARROW", "DROP", "NEEDS_MORE_EVIDENCE"):
        md.append(f"## {3 + ['GO','NARROW','DROP','NEEDS_MORE_EVIDENCE'].index(label)}. {label} topics\n")
        bucket = _bucket(decisions, label)
        if not bucket:
            md.append("_None._\n")
            continue
        for t, d in bucket:
            md.append(f"### {t['topic_id']} — {t['title']}")
            md.append(f"- Confidence: **{d.get('final_confidence','-')}**")
            md.append(f"- Reasoning: {d.get('reasoning_summary','')}")
            if d.get("manual_checks_required"):
                md.append("- Manual checks required:")
                for m in d["manual_checks_required"]:
                    md.append(f"  - {m}")
            if d.get("extra_verification_needed"):
                md.append("- Automated next-step suggestions:")
                for m in d["extra_verification_needed"]:
                    md.append(f"  - {m}")
            md.append("")

    # 7 rejected and why = same as DROP, already covered. Skip duplicate.

    # 8. Top 3 recommended (GO if any; else top NARROW; else top NEEDS_MORE_EVIDENCE)
    top3: list[tuple[dict[str, Any], dict[str, Any]]] = []
    for label in ("GO", "NARROW", "NEEDS_MORE_EVIDENCE"):
        for t, d in _bucket(decisions, label):
            if len(top3) < 3:
                top3.append((t, d))
    md.append("## 8. Top 3 recommended topics\n")
    if not top3:
        md.append("_None — every topic was DROPped. Re-seed `data/topics_seed.csv` and rerun._\n")
    else:
        for i, (t, d) in enumerate(top3, 1):
            md.append(f"### #{i} {t['topic_id']} — {t['title']}")
            s = _score(t["topic_id"])
            md.append(f"- Decision/confidence: **{d.get('final_decision','-')} / {d.get('final_confidence','-')}**")
            md.append(f"- Overall priority: **{s.get('rubric',{}).get('composites',{}).get('Overall','-')}**")
            md.append(f"- Citation signal {s.get('citation_signal_0to5','-')}, artifact {s.get('artifact',{}).get('artifact_opportunity_0to5','-')}, saturation {s.get('saturation',{}).get('saturation_score_0to5','-')}, venue {s.get('venue',{}).get('venue_signal_0to5','-')}.")
            md.append("")

    # 9. Evidence table for top 3
    md.append("## 9. Evidence table for top 3 (top 5 papers per topic)\n")
    for t, _ in top3:
        md.append(f"### {t['topic_id']} — {t['title']}")
        md.append(_section_top_papers(t["topic_id"], k=5))
        md.append("")

    # 10. Citation evidence summary
    md.append("## 10. Citation evidence summary\n")
    md.append("| Topic | n_papers | n_24mo | n_12mo | top_cit | growth_yoy | cit_signal |")
    md.append("|---|---|---|---|---|---|---|")
    for t, d in decisions:
        s = _score(t["topic_id"])
        ps = s.get("paper", {})
        md.append(f"| {t['topic_id']} | {ps.get('n_papers','-')} | {ps.get('n_papers_24mo','-')} | {ps.get('n_papers_12mo','-')} | {ps.get('top_citation','-')} | {ps.get('growth_yoy_proxy','-')} | {s.get('citation_signal_0to5','-')} |")
    md.append("")

    # 11. Novelty/saturation
    md.append("## 11. Novelty / saturation evidence\n")
    md.append("| Topic | sat_0to5 | dominant_tools | big_datasets | gap_phrase_hits |")
    md.append("|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        sa = s.get("saturation", {})
        ar = s.get("artifact", {})
        md.append(f"| {t['topic_id']} | {sa.get('saturation_score_0to5','-')} | {sa.get('dominant_tools','-')} | {sa.get('big_datasets','-')} | {ar.get('gap_phrase_hits','-')} |")
    md.append("")

    # 12. Venue / free-publication evidence
    md.append("## 12. Venue / free-publication evidence\n")
    md.append("| Topic | venue_signal | doaj_no_apc | crossref_active | openreview_hits |")
    md.append("|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        v = s.get("venue", {})
        md.append(f"| {t['topic_id']} | {v.get('venue_signal_0to5','-')} | {v.get('doaj_no_apc_journals','-')} | {v.get('crossref_active_venues','-')} | {v.get('openreview_hits','-')} |")
    md.append("")

    # 13. Artifact / reproducibility
    md.append("## 13. Artifact / reproducibility evidence\n")
    md.append("| Topic | artifact_0to5 | gap_phrase_hits | existing_pwc_datasets | existing_hf_datasets |")
    md.append("|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        a = s.get("artifact", {})
        md.append(f"| {t['topic_id']} | {a.get('artifact_opportunity_0to5','-')} | {a.get('gap_phrase_hits','-')} | {a.get('n_existing_pwc_datasets','-')} | {a.get('n_existing_hf_datasets','-')} |")
    md.append("")

    # 14. NIW/EB1A
    md.append("## 14. NIW / EB-1A evidence summary\n")
    md.append("Heuristic from rubric (L=NIW, M=EB-1A, V=public-artifact). Manual judgment still required for criterion-specific weight; see §18.\n")
    md.append("| Topic | NIW(L) | EB1A(M) | Artifact(V) | ImmigrationValue |")
    md.append("|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        f = s.get("rubric", {}).get("factors", {})
        c = s.get("rubric", {}).get("composites", {})
        md.append(f"| {t['topic_id']} | {f.get('L','-')} | {f.get('M','-')} | {f.get('V','-')} | {c.get('ImmigrationValue','-')} |")
    md.append("")

    # 15. Career / FAANG
    md.append("## 15. Career / FAANG evidence summary\n")
    md.append("| Topic | Career(N) | Tool(F) | Artifact(V) | CareerValue |")
    md.append("|---|---|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        f = s.get("rubric", {}).get("factors", {})
        c = s.get("rubric", {}).get("composites", {})
        md.append(f"| {t['topic_id']} | {f.get('N','-')} | {f.get('F','-')} | {f.get('V','-')} | {c.get('CareerValue','-')} |")
    md.append("")

    # 16. IP risk
    md.append("## 16. IP / employer-risk summary\n")
    md.append("| Topic | ip_risk_0to5 | flags |")
    md.append("|---|---|---|")
    for t, _ in decisions:
        s = _score(t["topic_id"])
        r = s.get("risk", {})
        md.append(f"| {t['topic_id']} | {r.get('ip_risk_0to5','-')} | {', '.join(r.get('ip_risk_flags', [])) or '-'} |")
    md.append("")

    # 17. LLM reviewer agreement / disagreement
    md.append("## 17. LLM reviewer agreement / disagreement\n")
    md.append("| Topic | n_reviews | plurality | dec_score | high_drops | disagree | per-role disagreements |")
    md.append("|---|---|---|---|---|---|---|")
    for t, _ in decisions:
        a = _agree(t["topic_id"])
        roles = ", ".join(d.get("role", "") for d in (a.get("per_role_disagreements") or [])) or "-"
        md.append(f"| {t['topic_id']} | {a.get('n_reviews','-')} | {a.get('plurality_decision','-')} | {a.get('decision_score_mean_0to3','-')} | {a.get('high_confidence_drops','-')} | {'Y' if a.get('high_disagreement_flag') else 'N'} | {roles} |")
    md.append("")

    # 18. Remaining manual checks
    md.append("## 18. Remaining manual checks\n")
    md.append("These cannot be automated and require human/legal judgment or a manual site visit.\n")
    manual: dict[str, list[str]] = {}
    for t, d in decisions:
        if d.get("manual_checks_required"):
            manual[t["topic_id"]] = d["manual_checks_required"]
    if not manual:
        manual_general = [
            "Verify TMLR no-APC + indexing on jmlr.org/tmlr (visible HTML; not via API).",
            "Verify employer IP / moonlighting clause (legal interpretation).",
            "Verify dataset DUA terms permit your specific use (legal/contractual).",
            "Cross-check candidate venues against Think.Check.Submit. (form-based site).",
        ]
        for m in manual_general:
            md.append(f"- {m}")
    else:
        for tid, items in manual.items():
            md.append(f"### {tid}")
            for m in items:
                md.append(f"- {m}")
    md.append("")

    # 19. Final recommendation
    md.append("## 19. Final recommendation\n")
    if top3:
        primary, ddec = top3[0]
        md.append(f"**Today**: open `data/decisions/{primary['topic_id']}.json` and the top-papers for that topic; write a one-paragraph differentiator vs the 5 top-cited prior works (templates/08_proposal_one_pager.md).")
        md.append(f"**This week**: complete §6 verification log for the top {min(3, len(top3))} topics; commit primary + secondary in `DECISIONS.md` with kill criteria.")
        first_artifact = (read_json(SCORES_DIR / f"{primary['topic_id']}.json", {}) or {}).get("artifact", {}).get("artifact_opportunity_0to5", 0)
        if first_artifact >= 4:
            md.append("**Mode**: artifact-first (benchmark/dataset/database) paired with one paper.")
        elif first_artifact == 3:
            md.append("**Mode**: empirical paper with light reproducibility package.")
        else:
            md.append("**Mode**: paper-first; minimal scripts only.")
    else:
        md.append("**Do not start writing.** Re-seed topics or expand evidence rounds; current pipeline yielded no GO/NARROW/NEEDS_MORE_EVIDENCE topics.")

    md.append("")
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
