"""
18_survey_progress.py

Track progress on the LLM-as-Judge survey project against PROTOCOL.md targets.

Outputs:
  reports/SURVEY_PROGRESS.md

What it measures
----------------
1. Corpus size vs target (PROTOCOL.md §5.1: ≥200 papers indexed by month 1)
2. Coverage per survey section (SURVEY_STRUCTURE.md)
3. Read status distribution (unread / skimmed / read / deep)
4. Section drafts: word count vs target pages (assumes 250 words/page)
5. QUALITY_RUBRIC checklist completion (parses checkbox states from rubric file)
6. KILL_CRITERIA status (parses sign-off table)

Usage
-----
  python scripts/18_survey_progress.py
  python scripts/18_survey_progress.py --out reports/SURVEY_PROGRESS.md
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

CORPUS_PATH    = ROOT / "data" / "survey_corpus.csv"
PROJECT_DIR    = ROOT / "06_paper_pipeline" / "SURVEY_llm_judge"
RUBRIC_PATH    = PROJECT_DIR / "QUALITY_RUBRIC.md"
KILL_PATH      = PROJECT_DIR / "KILL_CRITERIA.md"
STRUCTURE_PATH = PROJECT_DIR / "SURVEY_STRUCTURE.md"
PROTOCOL_PATH  = PROJECT_DIR / "PROTOCOL.md"
DRAFT_DIR      = PROJECT_DIR / "drafts"
OUT_PATH       = ROOT / "reports" / "SURVEY_PROGRESS.md"

CORPUS_TARGETS = {
    "month_1_indexed":     150,
    "month_1_stretch":     200,
    "month_6_deeply_read": 150,
    "submission_cited":    150,
}

# Page targets per section from SURVEY_STRUCTURE.md
SECTION_PAGE_TARGETS = {
    "1_introduction":     5,
    "2_foundations":      7,
    "3_methods":         10,
    "4_failure_modes":   12,
    "5_defences":         9,
    "6_empirical":        9,
    "7_evaluation":       5,
    "8_open_problems":    5,
    "9_discussion":       4,
    "10_conclusion":      1.5,
}

WORDS_PER_PAGE = 250  # journal-style estimate


# ----------------------------------------------------------------------------
# Pure helpers (testable)
# ----------------------------------------------------------------------------

def count_checkboxes(markdown: str) -> tuple[int, int]:
    """Return (n_checked, n_total) from a markdown file's `- [ ]` / `- [x]` syntax."""
    if not markdown:
        return (0, 0)
    checked = len(re.findall(r"^\s*-\s*\[[xX]\]", markdown, re.MULTILINE))
    unchecked = len(re.findall(r"^\s*-\s*\[\s\]", markdown, re.MULTILINE))
    return (checked, checked + unchecked)


def word_count(text: str) -> int:
    """Count words excluding code blocks and markdown front-matter."""
    if not text:
        return 0
    # Strip fenced code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    # Strip inline code
    text = re.sub(r"`[^`]*`", "", text)
    # Strip URLs
    text = re.sub(r"https?://\S+", "", text)
    # Strip markdown link syntax: keep text portion only
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Strip headings markers
    text = re.sub(r"^#+\s*", "", text, flags=re.MULTILINE)
    # Tokenise
    tokens = re.findall(r"\b[\w'-]+\b", text)
    return len(tokens)


def summarise_corpus(rows: list[dict]) -> dict[str, Any]:
    n = len(rows)
    by_in_scope: dict[str, int] = {}
    by_section:  dict[str, int] = {}
    by_read:     dict[str, int] = {}
    by_year:     dict[str, int] = {}
    n_with_code = 0
    n_with_data = 0
    failure_modes: dict[str, int] = {}
    for r in rows:
        by_in_scope[r.get("in_scope", "UNKNOWN")] = by_in_scope.get(r.get("in_scope", "UNKNOWN"), 0) + 1
        by_section [r.get("section",  "UNCLASSIFIED")] = by_section.get(r.get("section",  "UNCLASSIFIED"), 0) + 1
        by_read    [r.get("read_status", "unread") or "unread"] = by_read.get(r.get("read_status", "unread") or "unread", 0) + 1
        yr = (r.get("year") or "").strip()
        if yr:
            by_year[yr] = by_year.get(yr, 0) + 1
        if (r.get("has_code") or "").lower() == "yes":
            n_with_code += 1
        if (r.get("has_dataset") or "").lower() == "yes":
            n_with_data += 1
        for tag in (r.get("failure_mode_addressed") or "").split(";"):
            t = tag.strip()
            if t:
                failure_modes[t] = failure_modes.get(t, 0) + 1
    return {
        "n_total":       n,
        "by_in_scope":   by_in_scope,
        "by_section":    by_section,
        "by_read":       by_read,
        "by_year":       by_year,
        "n_with_code":   n_with_code,
        "n_with_data":   n_with_data,
        "failure_modes": failure_modes,
    }


def progress_against_targets(corpus_summary: dict, targets: dict) -> list[dict]:
    """Compute per-target % done."""
    n_in_scope = corpus_summary["by_in_scope"].get("yes", 0)
    n_deeply   = (corpus_summary["by_read"].get("deep", 0)
                  + corpus_summary["by_read"].get("read", 0))
    out = []
    for name, target in targets.items():
        if "deeply" in name:
            actual = n_deeply
        elif "indexed" in name or "stretch" in name or "cited" in name:
            actual = n_in_scope
        else:
            actual = corpus_summary["n_total"]
        pct = min(100, int(100 * actual / target)) if target else 0
        out.append({
            "name":   name,
            "target": target,
            "actual": actual,
            "pct":    pct,
        })
    return out


def scan_draft_sections(draft_dir: Path,
                        targets: dict = SECTION_PAGE_TARGETS) -> list[dict]:
    """For each expected section file, report word count and approximate pages."""
    out = []
    for section_id, target_pages in targets.items():
        # Try multiple naming conventions
        candidates = [
            draft_dir / f"{section_id}.md",
            draft_dir / f"section_{section_id}.md",
            draft_dir / f"{section_id.replace('_', '-')}.md",
        ]
        path = next((p for p in candidates if p.exists()), None)
        text = path.read_text(encoding="utf-8") if path else ""
        words = word_count(text)
        pages = round(words / WORDS_PER_PAGE, 1)
        pct = min(100, int(100 * pages / target_pages)) if target_pages else 0
        if path:
            try:
                disp = str(path.relative_to(ROOT))
            except ValueError:
                disp = str(path)
        else:
            disp = "(missing)"
        out.append({
            "section":      section_id,
            "target_pages": target_pages,
            "actual_pages": pages,
            "words":        words,
            "pct":          pct,
            "path":         disp,
        })
    return out


def parse_kill_signoff(kill_md: str) -> list[dict]:
    """Extract sign-off table rows from KILL_CRITERIA.md."""
    if not kill_md:
        return []
    # Find the sign-off table — looks for "| Checkpoint |"
    rows = []
    in_table = False
    for line in kill_md.splitlines():
        if "Checkpoint" in line and "K1" in line and "K2" in line:
            in_table = True
            continue
        if in_table:
            if line.startswith("|---"):
                continue
            if not line.strip().startswith("|"):
                if rows:  # we've started; blank line ends the table
                    break
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 6:
                rows.append({
                    "checkpoint": cells[0],
                    "date":       cells[1],
                    "k1":         cells[2],
                    "k2":         cells[3],
                    "k3":         cells[4],
                    "k4":         cells[5],
                    "action":     cells[6] if len(cells) > 6 else "",
                })
    return rows


# ----------------------------------------------------------------------------
# Report rendering
# ----------------------------------------------------------------------------

def render_report(corpus_summary: dict,
                  target_progress: list[dict],
                  section_drafts: list[dict],
                  rubric_checked: int,
                  rubric_total: int,
                  kill_rows: list[dict]) -> str:
    now = _dt.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    md: list[str] = []
    md.append("# Survey Progress Report — LLM-as-Judge")
    md.append("")
    md.append(f"*Generated: {now}*")
    md.append(f"*Source: `scripts/18_survey_progress.py`*")
    md.append("*Project: `06_paper_pipeline/SURVEY_llm_judge/`*")
    md.append("")

    # ---- 1. Headline
    md.append("## 1. Headline")
    md.append("")
    md.append(f"- Corpus size: **{corpus_summary['n_total']}** papers")
    md.append(f"- In scope (yes): **{corpus_summary['by_in_scope'].get('yes', 0)}**")
    md.append(f"- Deeply read: **{corpus_summary['by_read'].get('deep', 0) + corpus_summary['by_read'].get('read', 0)}**")
    md.append(f"- Draft pages (total across sections): **{sum(s['actual_pages'] for s in section_drafts):.1f}** / target {sum(s['target_pages'] for s in section_drafts):.1f}")
    md.append(f"- Quality rubric: **{rubric_checked}/{rubric_total}** items checked")
    md.append("")

    # ---- 2. Corpus vs targets
    md.append("## 2. Corpus targets")
    md.append("")
    md.append("| Target | Required | Current | Progress |")
    md.append("|---|---|---|---|")
    for t in target_progress:
        bar = _bar(t["pct"])
        md.append(f"| {t['name']} | {t['target']} | {t['actual']} | {bar} {t['pct']}% |")
    md.append("")

    # ---- 3. Corpus composition
    md.append("## 3. Corpus composition")
    md.append("")
    md.append("### 3.1 By in-scope label")
    md.append("")
    md.append("| Label | Count |")
    md.append("|---|---|")
    for label in ("yes", "partial", "no", "UNKNOWN", ""):
        cnt = corpus_summary["by_in_scope"].get(label, 0)
        if cnt:
            md.append(f"| {label or '(blank)'} | {cnt} |")
    md.append("")

    md.append("### 3.2 By survey section (auto-classified)")
    md.append("")
    md.append("| Section | Count |")
    md.append("|---|---|")
    for sec in (
        "3_methods", "4_failure_modes", "5_defences",
        "6_empirical", "7_evaluation", "8_open_problems",
        "UNCLASSIFIED",
    ):
        cnt = corpus_summary["by_section"].get(sec, 0)
        md.append(f"| {sec} | {cnt} |")
    md.append("")

    md.append("### 3.3 By read status")
    md.append("")
    md.append("| Status | Count |")
    md.append("|---|---|")
    for status in ("unread", "skimmed", "read", "deep"):
        cnt = corpus_summary["by_read"].get(status, 0)
        md.append(f"| {status} | {cnt} |")
    md.append("")

    md.append("### 3.4 Failure-mode coverage")
    md.append("")
    if corpus_summary["failure_modes"]:
        md.append("| Failure mode | Papers tagged |")
        md.append("|---|---|")
        for mode in sorted(corpus_summary["failure_modes"].keys()):
            md.append(f"| {mode} | {corpus_summary['failure_modes'][mode]} |")
    else:
        md.append("_No failure modes tagged yet._")
    md.append("")

    md.append(f"### 3.5 Artifact availability")
    md.append("")
    md.append(f"- Papers with code: **{corpus_summary['n_with_code']}** / {corpus_summary['n_total']}")
    md.append(f"- Papers with dataset: **{corpus_summary['n_with_data']}** / {corpus_summary['n_total']}")
    md.append("")

    # ---- 4. Draft section progress
    md.append("## 4. Draft sections")
    md.append("")
    md.append("| Section | Target pages | Drafted pages | Words | Progress | File |")
    md.append("|---|---|---|---|---|---|")
    for s in section_drafts:
        bar = _bar(s["pct"])
        md.append(f"| {s['section']} | {s['target_pages']} | {s['actual_pages']} | "
                  f"{s['words']} | {bar} {s['pct']}% | `{s['path']}` |")
    md.append("")

    # ---- 5. Quality rubric
    md.append("## 5. Quality rubric (60-item)")
    md.append("")
    if rubric_total:
        pct = int(100 * rubric_checked / rubric_total)
        md.append(f"**{rubric_checked} / {rubric_total} ({pct}%)** items checked in QUALITY_RUBRIC.md")
        md.append("")
        md.append(_bar(pct, width=40))
    else:
        md.append("_Rubric file not found; cannot count._")
    md.append("")

    # ---- 6. Kill-criteria sign-off
    md.append("## 6. KILL_CRITERIA sign-off")
    md.append("")
    if kill_rows:
        md.append("| Checkpoint | Date | K1 | K2 | K3 | K4 | Action |")
        md.append("|---|---|---|---|---|---|---|")
        for r in kill_rows:
            md.append(f"| {r['checkpoint']} | {r['date']} | {r['k1']} | {r['k2']} | "
                      f"{r['k3']} | {r['k4']} | {r['action']} |")
    else:
        md.append("_No checkpoints filled yet._")
    md.append("")

    md.append("---")
    md.append("")
    md.append("## Suggested next actions")
    md.append("")

    # Auto-derived advice
    actions = derive_actions(corpus_summary, target_progress, section_drafts,
                             rubric_checked, rubric_total)
    for a in actions:
        md.append(f"- {a}")
    md.append("")

    return "\n".join(md) + "\n"


def derive_actions(corpus_summary: dict,
                   target_progress: list[dict],
                   section_drafts: list[dict],
                   rubric_checked: int,
                   rubric_total: int) -> list[str]:
    out: list[str] = []
    n_in_scope = corpus_summary["by_in_scope"].get("yes", 0)
    n_unread   = corpus_summary["by_read"].get("unread", 0)

    if n_in_scope < 150:
        out.append(f"Corpus is below month-1 target — add {150 - n_in_scope} more in-scope papers via "
                   f"`python scripts/17_survey_corpus.py --fetch-arxiv`")
    if corpus_summary["by_section"].get("UNCLASSIFIED", 0) > 20:
        out.append(f"{corpus_summary['by_section']['UNCLASSIFIED']} papers are UNCLASSIFIED — "
                   f"hand-edit section assignment in `data/survey_corpus.csv`")
    if n_unread > 50 and (corpus_summary["by_read"].get("deep", 0) +
                          corpus_summary["by_read"].get("read", 0)) < 30:
        out.append("Reading is behind the corpus — read 10 priority (Tier 1) papers this week")
    sec_zero = [s["section"] for s in section_drafts if s["actual_pages"] == 0]
    if len(sec_zero) >= 8:
        out.append("All sections empty — begin writing §1 Introduction (5 pages target)")
    elif len(sec_zero) >= 4:
        out.append(f"{len(sec_zero)} sections still empty — focus on: {', '.join(sec_zero[:3])}")
    if rubric_total and (rubric_checked / rubric_total) < 0.30:
        out.append("Quality rubric < 30% — review `06_paper_pipeline/SURVEY_llm_judge/QUALITY_RUBRIC.md`")
    if not out:
        out.append("All targets on track — continue per `NEXT_90_DAYS.md`")
    return out


def _bar(pct: int, width: int = 20) -> str:
    pct = max(0, min(100, int(pct)))
    filled = round(width * pct / 100)
    return "`[" + ("=" * filled) + (" " * (width - filled)) + "]`"


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=str(OUT_PATH),
                   help="Output report path (default reports/SURVEY_PROGRESS.md)")
    p.add_argument("--corpus", default=str(CORPUS_PATH),
                   help="Corpus CSV path (default data/survey_corpus.csv)")
    args = p.parse_args(argv)

    corpus_path = Path(args.corpus)
    if corpus_path.exists():
        with corpus_path.open(encoding="utf-8") as f:
            corpus_rows = list(csv.DictReader(f))
    else:
        corpus_rows = []
        print(f"[warn] no corpus at {corpus_path}; run "
              "scripts/17_survey_corpus.py first", file=sys.stderr)

    corpus_summary = summarise_corpus(corpus_rows)
    target_progress = progress_against_targets(corpus_summary, CORPUS_TARGETS)
    section_drafts = scan_draft_sections(DRAFT_DIR)

    rubric_text = RUBRIC_PATH.read_text(encoding="utf-8") if RUBRIC_PATH.exists() else ""
    rubric_checked, rubric_total = count_checkboxes(rubric_text)

    kill_text = KILL_PATH.read_text(encoding="utf-8") if KILL_PATH.exists() else ""
    kill_rows = parse_kill_signoff(kill_text)

    report = render_report(corpus_summary, target_progress, section_drafts,
                            rubric_checked, rubric_total, kill_rows)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(report, encoding="utf-8")
    print(f"Wrote {out_path}")
    print(f"  corpus: {corpus_summary['n_total']} papers "
          f"({corpus_summary['by_in_scope'].get('yes', 0)} in-scope)")
    print(f"  drafts: {sum(s['actual_pages'] for s in section_drafts):.1f} pages")
    print(f"  rubric: {rubric_checked}/{rubric_total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
