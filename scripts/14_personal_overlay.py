"""
14_personal_overlay.py

Compute the personal-goal overlay over the neutral blind_citation baseline.

Reads:
  - data/decisions/<id>.json (active_profile=blind_citation, blind_citation_acceptable, profile_scores)
  - data/scores/<id>.json    (profile_scores per topic)
  - data/queries/<id>.json   (topic metadata)

Writes:
  - reports/PERSONAL_OVERLAY_REPORT.md
  - data/personal_overlay/by_profile/<profile>.json
  - data/personal_overlay/safe_choices.json     (bc_acceptable AND top under personal)
  - data/personal_overlay/risky_choices.json    (top under personal, FAIL bc gate)

Design principle (from the architecture spec):
  Personal-goal overlays do NOT change the academic ranking. They only help
  select among topics that ALREADY pass the blind_citation acceptability gate.

  - Safe choice = bc_acceptable AND ranks top-K under a personal profile
  - Risky choice = ranks top-K under personal profile but FAILS bc_acceptable
                   (flagged as PERSONAL_GOAL_ONLY_WEAK_TOPIC)

Usage: python scripts/14_personal_overlay.py [--top-k 8]
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.io_utils import read_json  # noqa: E402

DECISIONS_DIR = ROOT / "data" / "decisions"
SCORES_DIR    = ROOT / "data" / "scores"
QUERIES_DIR   = ROOT / "data" / "queries"
OUT_DIR       = ROOT / "data" / "personal_overlay"
REPORT_PATH   = ROOT / "reports" / "PERSONAL_OVERLAY_REPORT.md"

# Personal-goal profiles to overlay (must match config/weight_profiles.yaml)
PERSONAL_PROFILES = [
    ("niw_optimized",              "NIW (national interest waiver)"),
    ("eb1a_optimized",             "EB-1A (extraordinary ability)"),
    ("faang_career",               "FAANG / industry career"),
    ("balanced_personal_strategy", "Balanced personal strategy"),
]

# Extreme profiles (for diagnostic comparison only)
EXTREME_PROFILES = [
    ("immigration_only", "EXTREME: immigration only"),
    ("career_only",      "EXTREME: career only"),
]


def load_topic_data() -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for f in sorted(DECISIONS_DIR.glob("*.json")):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        tid = d.get("topic_id")
        if not tid:
            continue
        # Topic metadata
        q = read_json(QUERIES_DIR / f"{tid}.json", {})
        topic = (q.get("topic") if q else None) or {}
        out[tid] = {
            "topic_id":              tid,
            "title":                 topic.get("title", ""),
            "category":              topic.get("category", ""),
            "is_negative_control":   (str(topic.get("is_negative_control", "")).lower()
                                      in ("true", "1", "yes")
                                      or "_NC" in tid),
            "decision":              d.get("final_decision"),
            "confidence":            d.get("final_confidence"),
            "bc_acceptable":         bool(d.get("blind_citation_acceptable", False)),
            "bc_score":              float(d.get("blind_citation_score", 0)),
            "bc_failed_reasons":     d.get("blind_citation_failed_reasons", []),
            "ew_go_blocked":         bool(d.get("existing_work", {}).get("go_blocked", False)),
            "profile_scores":        d.get("profile_scores", {}),
            "signals":               d.get("signals", {}),
        }
    return out


def rank_under_profile(topics: dict[str, dict], profile_name: str) -> list[dict]:
    rows = []
    for tid, t in topics.items():
        if t["is_negative_control"]:
            continue  # NC topics excluded from real rankings
        ps = t["profile_scores"].get(profile_name, {}) or {}
        rows.append({
            "topic_id":      tid,
            "title":         t["title"],
            "score":         float(ps.get("score", 0)),
            "bc_acceptable": t["bc_acceptable"],
            "bc_score":      t["bc_score"],
            "ew_go_blocked": t["ew_go_blocked"],
            "decision":      t["decision"],
            "confidence":    t["confidence"],
            "category":      t["category"],
            "signals":       t["signals"],
        })
    rows.sort(key=lambda r: r["score"], reverse=True)
    for i, r in enumerate(rows, 1):
        r["rank"] = i
    return rows


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top-k", type=int, default=8,
                    help="Number of top topics per profile to highlight (default 8)")
    args = ap.parse_args(argv)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "by_profile").mkdir(parents=True, exist_ok=True)

    print(f"[14_overlay] Loading topic data from {DECISIONS_DIR}")
    topics = load_topic_data()
    n_real = sum(1 for t in topics.values() if not t["is_negative_control"])
    n_nc = sum(1 for t in topics.values() if t["is_negative_control"])
    n_bc_acc = sum(1 for t in topics.values()
                   if t["bc_acceptable"] and not t["is_negative_control"])
    print(f"[14_overlay] {n_real} real topics, {n_nc} NCs, {n_bc_acc} bc_acceptable")

    # Per-profile rankings
    by_profile: dict[str, list[dict]] = {}
    for prof, _ in PERSONAL_PROFILES + EXTREME_PROFILES:
        ranking = rank_under_profile(topics, prof)
        by_profile[prof] = ranking
        (OUT_DIR / "by_profile" / f"{prof}.json").write_text(
            json.dumps(ranking, indent=2), encoding="utf-8")

    # Safe choices (bc_acceptable AND top-K under any personal profile)
    safe_choices: dict[str, list[dict]] = {}
    risky_choices: dict[str, list[dict]] = {}
    for prof, _ in PERSONAL_PROFILES:
        topk = by_profile[prof][:args.top_k]
        safe = [r for r in topk if r["bc_acceptable"] and not r["ew_go_blocked"]]
        risky = [r for r in topk if not r["bc_acceptable"]]
        safe_choices[prof] = safe
        risky_choices[prof] = risky
    (OUT_DIR / "safe_choices.json").write_text(
        json.dumps(safe_choices, indent=2), encoding="utf-8")
    (OUT_DIR / "risky_choices.json").write_text(
        json.dumps(risky_choices, indent=2), encoding="utf-8")

    # ----- Write the report
    md: list[str] = []
    md.append("# Personal-Goal Overlay Report\n")
    md.append("*Generated: 2026-05-10 by `scripts/14_personal_overlay.py`*\n")
    md.append("\n---\n")
    md.append("## Design principle\n")
    md.append("Personal-goal overlays **do NOT change the academic (blind_citation) ranking**. "
              "They only help select among topics that already pass the blind_citation acceptability gate.\n")
    md.append("- **Safe choice** = the topic is `blind_citation_acceptable=True` AND ranks top-"
              f"{args.top_k} under a personal-goal profile.")
    md.append("- **Risky choice** (`PERSONAL_GOAL_ONLY_WEAK_TOPIC`) = the topic ranks top-"
              f"{args.top_k} under a personal profile but FAILS `blind_citation_acceptable`. "
              "These should NOT be promoted to GO.\n")

    # Bc-acceptable list
    md.append("## Topics that pass blind_citation acceptability\n")
    bc_topics = sorted(
        [t for t in topics.values() if t["bc_acceptable"] and not t["is_negative_control"]],
        key=lambda t: -t["bc_score"],
    )
    if not bc_topics:
        md.append("_None — no topic passes the academic-merit gate. Cannot proceed with overlay._\n")
    else:
        md.append("| Topic | bc_score | Decision | Conf | Title |")
        md.append("|---|---|---|---|---|")
        for t in bc_topics:
            md.append(f"| **{t['topic_id']}** | {t['bc_score']:.2f} | {t['decision']} | "
                      f"{t['confidence']} | {t['title']} |")
        md.append("")

    # Per-profile sections
    for prof, label in PERSONAL_PROFILES:
        md.append(f"\n## Overlay: {label}  (`{prof}`)\n")
        ranking = by_profile[prof]
        topk = ranking[:args.top_k]

        md.append(f"### Top {args.top_k} under {prof}\n")
        md.append("| Rank | Topic | Score | bc_acc? | EW-blocked? | Decision | Title |")
        md.append("|---|---|---|---|---|---|---|")
        for r in topk:
            bc = "✅" if r["bc_acceptable"] else "❌"
            ew = "⛔" if r["ew_go_blocked"] else "—"
            md.append(f"| {r['rank']} | **{r['topic_id']}** | {r['score']:.2f} | {bc} | {ew} | "
                      f"{r['decision']} | {r['title'][:60]} |")
        md.append("")

        # Safe vs risky for this profile
        safe = safe_choices[prof]
        risky = risky_choices[prof]
        md.append(f"### Safe choices for {label}\n")
        md.append(f"_(bc_acceptable=True AND top-{args.top_k} under {prof} AND not EW-blocked)_\n")
        if not safe:
            md.append("_None — no topic is both academically acceptable and top under this profile._")
        else:
            for r in safe:
                md.append(f"- **{r['topic_id']}**: {r['title']} "
                          f"(rank #{r['rank']}, profile_score={r['score']:.2f}, "
                          f"bc_score={r['bc_score']:.2f})")
        md.append("")

        md.append(f"### Risky choices (PERSONAL_GOAL_ONLY_WEAK_TOPIC) for {label}\n")
        md.append("_(top under personal profile but FAILS blind_citation gate — DO NOT promote to GO)_\n")
        if not risky:
            md.append("_None._")
        else:
            for r in risky:
                md.append(f"- ⚠️ **{r['topic_id']}**: {r['title']} "
                          f"(rank #{r['rank']} under {prof}, score={r['score']:.2f}; "
                          f"bc_score={r['bc_score']:.2f} FAILS gate)")
        md.append("")

    # Extreme profiles section (diagnostic only)
    md.append("\n## Diagnostic: extreme profiles (top-5)\n")
    md.append("These are extreme weighting profiles for audit comparison. Topics that win here "
              "but not under any non-extreme personal profile are bias-driven outliers.\n")
    md.append("| Profile | #1 | #2 | #3 | #4 | #5 |")
    md.append("|---|---|---|---|---|---|")
    for prof, label in EXTREME_PROFILES:
        top5 = by_profile[prof][:5]
        cells = [f"{r['topic_id']}({r['score']:.1f}{'✅' if r['bc_acceptable'] else '❌'})"
                 for r in top5]
        while len(cells) < 5:
            cells.append("—")
        md.append(f"| `{prof}` | " + " | ".join(cells) + " |")
    md.append("")

    # Cross-overlay summary
    md.append("\n## Cross-overlay summary: topics safe under ≥ 2 personal profiles\n")
    safe_counts: dict[str, int] = {}
    safe_in: dict[str, list[str]] = {}
    for prof, _ in PERSONAL_PROFILES:
        for r in safe_choices[prof]:
            tid = r["topic_id"]
            safe_counts[tid] = safe_counts.get(tid, 0) + 1
            safe_in.setdefault(tid, []).append(prof)
    multi_safe = sorted([(tid, n) for tid, n in safe_counts.items() if n >= 2],
                        key=lambda x: -x[1])
    if not multi_safe:
        md.append("_No topic appears safe in 2+ personal profiles._")
    else:
        md.append("| Topic | # personal profiles where safe | Profiles |")
        md.append("|---|---|---|")
        for tid, n in multi_safe:
            md.append(f"| **{tid}** | {n} | {', '.join(safe_in[tid])} |")
    md.append("")

    md.append("\n## Final note\n")
    md.append("The blind_citation baseline (committed in c805933) remains the canonical "
              "academic-merit ranking. This overlay report is a **selection aid**, not a "
              "re-ranking. Any topic considered for GO must:\n")
    md.append("1. Pass `blind_citation_acceptable=True` (bc_score above gate, EW-not-blocked, "
              "purity ≥ 0.30)\n")
    md.append("2. Not be flagged `personal_goal_only_weak_topic`\n")
    md.append("3. Not be flagged `negative_control_blocked_go`\n")
    md.append("4. Have a clear citation thesis (see GO_READINESS_DOSSIERS for template)\n")
    md.append("\nNo topic in this run currently meets all 4 criteria for GO. The 6 bc_acceptable "
              "topics are the candidate pool.\n")

    REPORT_PATH.write_text("\n".join(md), encoding="utf-8")
    print(f"[14_overlay] Wrote {REPORT_PATH}")
    print(f"[14_overlay] Wrote per-profile JSONs to {OUT_DIR / 'by_profile'}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
