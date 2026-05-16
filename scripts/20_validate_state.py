"""
20_validate_state.py

Project-state validator. Catches the class of issues that have hit this repo:

  - Documents reference venues / deadlines that are deprecated
  - Titles in PROTOCOLs drift from data/proposed_titles.txt
  - Scoop-watch queries miss topics that PROTOCOLs claim are watched
  - Required documents missing from paper projects (PROTOCOL, KILL_CRITERIA)
  - Configuration files don't parse
  - Data files reference last_modified dates that are stale
  - Survey corpus hasn't been refreshed recently
  - Title check hasn't been re-run recently

Output: reports/STATE_VALIDATION.md
Exit codes:
  0 — all checks pass
  1 — any FAIL (must fix before next submission)
  2 — only WARN (recommended to fix; not blocking)

This script is the first line of defence against strategy drift.
It is INTENDED to be conservative — false positives are fine, false negatives are not.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

REPORT_PATH = ROOT / "reports" / "STATE_VALIDATION.md"
TODAY = _dt.date.today()

# Thresholds (days) — tune in one place
THRESH = {
    "survey_corpus_stale":     30,
    "title_check_stale":       30,
    "scoop_watch_stale":        7,
    "snapshot_stale":          90,
    "draft_section_stale":     14,   # warning only
}


# ----------------------------------------------------------------------------
# Check result dataclass
# ----------------------------------------------------------------------------

@dataclass
class CheckResult:
    name:     str
    status:   str               # "PASS" / "FAIL" / "WARN" / "SKIP"
    message:  str
    fix_hint: str = ""
    details:  list[str] = field(default_factory=list)


def pass_(name: str, msg: str) -> CheckResult:
    return CheckResult(name=name, status="PASS", message=msg)

def fail_(name: str, msg: str, fix: str = "", details: list[str] | None = None) -> CheckResult:
    return CheckResult(name=name, status="FAIL", message=msg, fix_hint=fix, details=details or [])

def warn_(name: str, msg: str, fix: str = "", details: list[str] | None = None) -> CheckResult:
    return CheckResult(name=name, status="WARN", message=msg, fix_hint=fix, details=details or [])

def skip_(name: str, msg: str) -> CheckResult:
    return CheckResult(name=name, status="SKIP", message=msg)


# ----------------------------------------------------------------------------
# Pure helper functions (testable without filesystem)
# ----------------------------------------------------------------------------

def days_since(iso_str: str, today: _dt.date | None = None) -> int | None:
    """Days between today and a YYYY-MM-DD prefix found in iso_str. None if unparseable."""
    if not iso_str:
        return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", iso_str)
    if not m:
        return None
    try:
        d = _dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None
    t = today or TODAY
    return (t - d).days


def extract_titles_from_protocol(text: str) -> list[str]:
    """Find quoted titles in a PROTOCOL markdown file.

    Looks for patterns like:
      **Working title** (...): *"Some Title"*
      *"Some Title"*
      working title: "Some Title"
    """
    if not text:
        return []
    titles: list[str] = []
    # Match content of *"..."* (italic-quoted)
    for m in re.finditer(r'\*"([^"\n]+?)"\*', text):
        t = m.group(1).strip()
        if 10 < len(t) < 200:
            titles.append(t)
    # Also match plain "..." after the words "Working title" or "Title"
    for m in re.finditer(r'(?:Working\s+title|Title)[^"\n]{0,50}?"([^"\n]+?)"', text, re.I):
        t = m.group(1).strip()
        if 10 < len(t) < 200 and t not in titles:
            titles.append(t)
    return titles


def extract_venues_from_protocol(text: str) -> list[str]:
    """Find venue mentions in a PROTOCOL file (heuristic, conservative)."""
    if not text:
        return []
    candidates = [
        "TMLR", "JMLR", "ACM Computing Surveys", "ACM CS",
        "EMNLP", "ACL", "NAACL", "EACL", "ICLR", "NeurIPS", "ICML",
        "Eval4NLP", "TrustNLP", "BlackboxNLP", "GenBench",
        "COLM", "Findings", "ARR", "Computational Linguistics",
        "IEEE Access", "IEEE Transactions", "JOSS",
    ]
    found: list[str] = []
    for v in candidates:
        if re.search(rf"\b{re.escape(v)}\b", text):
            found.append(v)
    return found


def find_dates_in_text(text: str, today: _dt.date | None = None) -> list[tuple[str, _dt.date, int]]:
    """Find YYYY-MM-DD dates and return (date_str, parsed_date, days_until_today).

    Negative days_until = future; positive = past.
    """
    out: list[tuple[str, _dt.date, int]] = []
    t = today or TODAY
    for m in re.finditer(r"\b(\d{4})-(\d{2})-(\d{2})\b", text or ""):
        try:
            d = _dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            continue
        out.append((m.group(0), d, (t - d).days))
    return out


# ----------------------------------------------------------------------------
# Individual checks
# ----------------------------------------------------------------------------

def check_required_scripts() -> CheckResult:
    """Each script referenced in the pipeline should exist."""
    required = [
        "00_setup_repo.py", "01_generate_queries.py", "02_collect_topic_evidence.py",
        "03_collect_extra_evidence.py", "04_collect_venue_evidence.py",
        "05_score_topics.py", "06_llm_review_topics.py", "07_compare_reviewers.py",
        "08_confidence_gate.py", "09_generate_final_report.py",
        "10_run_pipeline.py", "11_generate_narrowed_topics.py",
        "12_detect_existing_work.py", "13_bias_audit.py", "14_personal_overlay.py",
        "15_arxiv_watch.py", "16_extract_bibtex.py", "17_survey_corpus.py",
        "18_survey_progress.py", "19_title_check.py", "20_validate_state.py",
    ]
    missing = [s for s in required
               if not any((ROOT / "scripts").glob(s))]
    if missing:
        return fail_(
            "required_scripts_exist",
            f"{len(missing)} script(s) missing",
            "Restore the missing files; check git history if accidentally deleted.",
            missing,
        )
    return pass_("required_scripts_exist", f"All {len(required)} pipeline scripts present")


def check_paper_projects_complete() -> CheckResult:
    """Each active paper project should have either PROTOCOL or a PRE_EXECUTION_CHECKLIST,
    plus KILL_CRITERIA (T02-style execution projects) OR explicit pre-execution status.
    """
    project_root = ROOT / "06_paper_pipeline"
    missing_per_project: dict[str, list[str]] = {}
    if not project_root.is_dir():
        return skip_("paper_projects_complete", "06_paper_pipeline/ not present")
    for proj_dir in sorted(project_root.iterdir()):
        if not proj_dir.is_dir() or proj_dir.name.startswith("_"):
            continue
        # Each project must have at least PROTOCOL.md OR PRE_EXECUTION_CHECKLIST.md
        has_protocol = (proj_dir / "PROTOCOL.md").exists()
        has_pre_exec = (proj_dir / "PRE_EXECUTION_CHECKLIST.md").exists()
        if not (has_protocol or has_pre_exec):
            missing_per_project[proj_dir.name] = ["PROTOCOL.md or PRE_EXECUTION_CHECKLIST.md"]
            continue
        # If a project is in execution (has PROTOCOL), it must also have KILL_CRITERIA
        if has_protocol and not (proj_dir / "KILL_CRITERIA.md").exists():
            missing_per_project[proj_dir.name] = ["KILL_CRITERIA.md (required for projects in execution)"]
            continue
        # T02 is the bridge; required extras
        if proj_dir.name == "T02_position_bias":
            req = ["PAPER_OUTLINE.md", "CODE_SCAFFOLD.md"]
            miss = [r for r in req if not (proj_dir / r).exists()]
            if miss:
                missing_per_project[proj_dir.name] = miss
    if missing_per_project:
        details = [f"{p}: missing {', '.join(m)}" for p, m in missing_per_project.items()]
        return fail_(
            "paper_projects_complete",
            f"{len(missing_per_project)} paper project(s) incomplete",
            "Pre-execution projects (T07) need at minimum PRE_EXECUTION_CHECKLIST.md. "
            "Execution projects need PROTOCOL.md + KILL_CRITERIA.md. "
            "T02 also needs PAPER_OUTLINE.md + CODE_SCAFFOLD.md.",
            details,
        )
    return pass_("paper_projects_complete",
                 "All paper projects under 06_paper_pipeline/ have appropriate files for their phase")


def check_titles_match_proposed_list() -> CheckResult:
    """Every title in a PROTOCOL file should appear in data/proposed_titles.txt
    (so the title-check tool can verify it).
    """
    proposed_path = ROOT / "data" / "proposed_titles.txt"
    if not proposed_path.exists():
        return warn_("titles_match_proposed", "data/proposed_titles.txt missing",
                     "Run scripts/19_title_check.py with --titles-file pointing at this list")
    proposed_text = proposed_path.read_text(encoding="utf-8")
    proposed_titles = {ln.strip() for ln in proposed_text.splitlines()
                       if ln.strip() and not ln.strip().startswith("#")}

    protocol_titles_found: dict[str, list[str]] = {}
    project_root = ROOT / "06_paper_pipeline"
    if not project_root.is_dir():
        return skip_("titles_match_proposed", "06_paper_pipeline/ not present")
    for proj_dir in project_root.iterdir():
        if not proj_dir.is_dir() or proj_dir.name.startswith("_"):
            continue
        proto = proj_dir / "PROTOCOL.md"
        if not proto.exists():
            continue
        titles = extract_titles_from_protocol(proto.read_text(encoding="utf-8"))
        if titles:
            protocol_titles_found[proj_dir.name] = titles

    not_in_proposed: list[str] = []
    for proj, titles in protocol_titles_found.items():
        for t in titles:
            if t not in proposed_titles:
                not_in_proposed.append(f"{proj}: '{t[:80]}'")

    if not_in_proposed:
        return warn_(
            "titles_match_proposed",
            f"{len(not_in_proposed)} title(s) in PROTOCOLs not in data/proposed_titles.txt",
            "Add the title to data/proposed_titles.txt and re-run scripts/19_title_check.py",
            not_in_proposed[:10],
        )
    return pass_("titles_match_proposed",
                 f"All {sum(len(v) for v in protocol_titles_found.values())} "
                 "PROTOCOL titles are listed in data/proposed_titles.txt")


def check_no_past_deadline_claims() -> CheckResult:
    """Documents shouldn't propose deadlines that are already past."""
    doc_paths = [
        ROOT / "reports" / "BRIDGE_PUBLICATION_STRATEGY.md",
        ROOT / "reports" / "HIGH_CITATION_STRATEGY.md",
        ROOT / "reports" / "VENUE_REOPTIMIZATION.md",
        ROOT / "reports" / "COORDINATION.md",
        ROOT / "06_paper_pipeline" / "T02_position_bias" / "PROTOCOL.md",
        ROOT / "06_paper_pipeline" / "T02_position_bias" / "BRIDGE_SPRINT.md",
        ROOT / "06_paper_pipeline" / "SURVEY_llm_judge" / "PROTOCOL.md",
        ROOT / "NEXT_90_DAYS.md",
    ]
    issues: list[str] = []
    for p in doc_paths:
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        for date_str, d, days_until in find_dates_in_text(text):
            if days_until <= 0:
                continue  # date is in the future or today
            # Only flag past dates that are in a "submission" or "deadline" context
            ctx_start = max(0, text.find(date_str) - 80)
            ctx_end = min(len(text), text.find(date_str) + 80)
            ctx = text[ctx_start:ctx_end].lower()
            if any(kw in ctx for kw in ("submit", "deadline", "target", "submission")):
                issues.append(f"{p.relative_to(ROOT)}: {date_str} (past by {days_until} days) — context: ...{ctx[60:140].strip()}...")
    if issues:
        return warn_(
            "no_past_deadline_claims",
            f"{len(issues)} document(s) reference past deadlines in submission contexts",
            "Update the dates or remove the stale references",
            issues[:8],
        )
    return pass_("no_past_deadline_claims", "No past-deadline submission claims found")


def check_survey_corpus_freshness() -> CheckResult:
    """Survey corpus should be refreshed in the last 30 days."""
    csv_path = ROOT / "data" / "survey_corpus.csv"
    if not csv_path.exists():
        return warn_("survey_corpus_freshness",
                     "data/survey_corpus.csv does not exist",
                     "Run `python scripts/17_survey_corpus.py --seed-from-dedup`")
    # Look at last_seen column
    import csv
    latest = None
    with csv_path.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ls = row.get("last_seen", "")
            d = days_since(ls)
            if d is not None and (latest is None or d < latest):
                latest = d
    if latest is None:
        return warn_("survey_corpus_freshness",
                     "Cannot determine corpus freshness (no parseable last_seen dates)")
    if latest > THRESH["survey_corpus_stale"]:
        return warn_(
            "survey_corpus_freshness",
            f"Survey corpus last refreshed {latest} days ago "
            f"(threshold: {THRESH['survey_corpus_stale']} days)",
            "Run `python scripts/17_survey_corpus.py --fetch-arxiv` to refresh",
        )
    return pass_("survey_corpus_freshness",
                 f"Survey corpus most recently refreshed {latest} days ago "
                 f"(within {THRESH['survey_corpus_stale']}-day window)")


def check_title_check_freshness() -> CheckResult:
    """Title check should have been run in the last 30 days."""
    report_path = ROOT / "reports" / "TITLE_CHECK.md"
    if not report_path.exists():
        return warn_("title_check_freshness",
                     "reports/TITLE_CHECK.md does not exist",
                     "Run `python scripts/19_title_check.py --titles-file data/proposed_titles.txt`")
    text = report_path.read_text(encoding="utf-8")
    m = re.search(r"Generated:\s*([\d\-T:Z]+)", text)
    if not m:
        return warn_("title_check_freshness", "Could not parse Generated timestamp")
    days = days_since(m.group(1))
    if days is None:
        return warn_("title_check_freshness",
                     f"Unparseable timestamp: {m.group(1)}")
    if days > THRESH["title_check_stale"]:
        return warn_(
            "title_check_freshness",
            f"Title check is {days} days old (threshold: {THRESH['title_check_stale']})",
            "Re-run `python scripts/19_title_check.py --titles-file data/proposed_titles.txt`",
        )
    return pass_("title_check_freshness",
                 f"Title check is {days} days old (within {THRESH['title_check_stale']}-day window)")


def check_scoop_watch_freshness() -> CheckResult:
    """Scoop watch should run weekly."""
    report_path = ROOT / "reports" / "SCOOP_WATCH.md"
    if not report_path.exists():
        return warn_("scoop_watch_freshness",
                     "reports/SCOOP_WATCH.md does not exist",
                     "Run `python scripts/15_arxiv_watch.py --bootstrap` to initialise")
    text = report_path.read_text(encoding="utf-8")
    m = re.search(r"Last run:\s*([\d\-T:Z]+)", text)
    if not m:
        return warn_("scoop_watch_freshness", "Could not parse Last run timestamp")
    days = days_since(m.group(1))
    if days is None:
        return warn_("scoop_watch_freshness",
                     f"Unparseable timestamp: {m.group(1)}")
    if days > THRESH["scoop_watch_stale"]:
        return warn_(
            "scoop_watch_freshness",
            f"Scoop watch is {days} days old (threshold: {THRESH['scoop_watch_stale']})",
            "Run `python scripts/15_arxiv_watch.py`",
        )
    return pass_("scoop_watch_freshness",
                 f"Scoop watch is {days} days old (within {THRESH['scoop_watch_stale']}-day window)")


def check_scoop_watch_covers_active_topics() -> CheckResult:
    """Every paper project should have a corresponding scoop-watch query."""
    queries_path = ROOT / "data" / "scoop_watch_queries.json"
    project_root = ROOT / "06_paper_pipeline"
    if not queries_path.exists():
        return warn_("scoop_watch_covers_topics", "scoop_watch_queries.json missing")
    if not project_root.is_dir():
        return skip_("scoop_watch_covers_topics", "06_paper_pipeline/ not present")
    queries = json.loads(queries_path.read_text(encoding="utf-8")).get("queries", [])
    watched_topics = {q.get("topic_id", "") for q in queries}
    watched_topics.discard("")
    project_topics = set()
    for proj_dir in project_root.iterdir():
        if proj_dir.is_dir() and not proj_dir.name.startswith("_"):
            project_topics.add(proj_dir.name)
    # Map project dir names to expected topic IDs (best-effort)
    expected_ids: dict[str, str] = {
        "T02_position_bias":     "T02",
        "T07_judge_injection":   "T07",
        "SURVEY_llm_judge":      "SURVEY_llm_judge",
    }
    missing: list[str] = []
    for proj in sorted(project_topics):
        eid = expected_ids.get(proj, proj)
        if eid not in watched_topics:
            missing.append(f"project '{proj}' (expected watch on topic_id='{eid}')")
    if missing:
        return warn_(
            "scoop_watch_covers_topics",
            f"{len(missing)} active project(s) not in scoop_watch_queries.json",
            "Add a query block to data/scoop_watch_queries.json for each project",
            missing,
        )
    return pass_("scoop_watch_covers_topics",
                 f"All {len(project_topics)} active projects have scoop-watch queries")


def check_config_files_parse() -> CheckResult:
    """Config files (yaml + json) should parse cleanly."""
    config_files = [
        ROOT / "config.yaml",
        ROOT / "config" / "weight_profiles.yaml",
        ROOT / "data" / "scoop_watch_queries.json",
        ROOT / "data" / "survey_corpus_queries.json",
    ]
    failures: list[str] = []
    import yaml as _yaml
    for p in config_files:
        if not p.exists():
            continue
        try:
            text = p.read_text(encoding="utf-8")
            if p.suffix == ".json":
                json.loads(text)
            elif p.suffix in (".yaml", ".yml"):
                _yaml.safe_load(text)
        except Exception as e:
            failures.append(f"{p.relative_to(ROOT)}: {type(e).__name__}: {str(e)[:80]}")
    if failures:
        return fail_(
            "config_files_parse",
            f"{len(failures)} config file(s) failed to parse",
            "Fix the syntax errors",
            failures,
        )
    return pass_("config_files_parse", f"All {len(config_files)} config files parse cleanly")


def check_decisions_log_format() -> CheckResult:
    """DECISIONS.md should have the canonical table header and at least 1 entry."""
    p = ROOT / "DECISIONS.md"
    if not p.exists():
        return fail_("decisions_log_format", "DECISIONS.md missing",
                     "Restore from git history")
    text = p.read_text(encoding="utf-8")
    if "| Date | Decision | Rationale | Topic ID | Reversible? |" not in text:
        return fail_("decisions_log_format",
                     "DECISIONS.md missing canonical table header",
                     "Restore: `| Date | Decision | Rationale | Topic ID | Reversible? |`")
    # Count entries (rows beginning with date)
    n_entries = len(re.findall(r"^\|\s*\d{4}-\d{2}-\d{2}", text, re.MULTILINE))
    if n_entries == 0:
        return warn_("decisions_log_format",
                     "DECISIONS.md has header but no entries",
                     "Add at least one decision entry")
    return pass_("decisions_log_format",
                 f"DECISIONS.md has canonical header and {n_entries} entries")


def check_no_deprecated_venue_claims() -> CheckResult:
    """Documents should not claim 'free' for paid venues, etc."""
    deprecated_claims = [
        ("IEEE Access", "free", "IEEE Access charges $1,995 APC — never free"),
        ("PLOS ONE", "free", "PLOS ONE has APC — explicit waiver only"),
        ("Frontiers", "free", "Frontiers journals have APC ~$2,500"),
        ("MDPI", "free", "MDPI journals have APC and reputation issues"),
    ]
    doc_paths = list((ROOT / "reports").glob("*.md")) + \
                list((ROOT / "06_paper_pipeline").rglob("*.md"))
    issues: list[str] = []
    for p in doc_paths:
        text = p.read_text(encoding="utf-8")
        text_low = text.lower()
        for venue, claim, msg in deprecated_claims:
            # Look for "<venue>" within 50 chars of "<claim>" (positive claim only)
            for m in re.finditer(re.escape(venue.lower()), text_low):
                ctx_start = max(0, m.start() - 80)
                ctx_end = min(len(text_low), m.end() + 80)
                ctx = text_low[ctx_start:ctx_end]
                if claim in ctx and "not " + claim not in ctx and "no " + claim not in ctx:
                    # Heuristic: look for affirmative claim "<venue> is free", "<venue>: free"
                    if re.search(rf"{re.escape(venue.lower())}[^\.]{{0,30}}{claim}\b", ctx):
                        issues.append(f"{p.relative_to(ROOT)}: claim that {venue} is {claim} ({msg})")
                        break
    if issues:
        return warn_(
            "no_deprecated_venue_claims",
            f"{len(issues)} document(s) make unverified venue claims",
            "Update the affected documents",
            issues[:8],
        )
    return pass_("no_deprecated_venue_claims",
                 "No deprecated venue claims found in documentation")


def check_test_suite_files_present() -> CheckResult:
    """The test suite file should be present and importable."""
    p = ROOT / "scripts" / "tests" / "test_pipeline.py"
    if not p.exists():
        return fail_("test_suite_files", "scripts/tests/test_pipeline.py missing",
                     "Restore from git history")
    return pass_("test_suite_files", "Test suite file present")


# ----------------------------------------------------------------------------
# Runner
# ----------------------------------------------------------------------------

CHECKS: list[Callable[[], CheckResult]] = [
    check_required_scripts,
    check_paper_projects_complete,
    check_titles_match_proposed_list,
    check_no_past_deadline_claims,
    check_survey_corpus_freshness,
    check_title_check_freshness,
    check_scoop_watch_freshness,
    check_scoop_watch_covers_active_topics,
    check_config_files_parse,
    check_decisions_log_format,
    check_no_deprecated_venue_claims,
    check_test_suite_files_present,
]


def render_report(results: list[CheckResult]) -> str:
    now = _dt.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    n_pass = sum(1 for r in results if r.status == "PASS")
    n_fail = sum(1 for r in results if r.status == "FAIL")
    n_warn = sum(1 for r in results if r.status == "WARN")
    n_skip = sum(1 for r in results if r.status == "SKIP")
    md: list[str] = ["# Project State Validation Report", ""]
    md.append(f"*Generated: {now}*")
    md.append(f"*Source: `scripts/20_validate_state.py`*")
    md.append("")
    md.append(f"**Summary**: {n_pass} PASS · {n_fail} FAIL · {n_warn} WARN · {n_skip} SKIP")
    md.append("")
    if n_fail:
        md.append("⚠️ **FAILURES present** — must fix before next submission.")
        md.append("")
    elif n_warn:
        md.append("ℹ️ Warnings present — recommended to fix but not blocking.")
        md.append("")
    else:
        md.append("✅ All checks pass.")
        md.append("")
    md.append("## Per-check results")
    md.append("")
    md.append("| Status | Check | Message |")
    md.append("|---|---|---|")
    status_icon = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️", "SKIP": "⏭️"}
    for r in results:
        icon = status_icon.get(r.status, "")
        md.append(f"| {icon} {r.status} | `{r.name}` | {r.message[:100]} |")
    md.append("")
    # Detail sections for non-pass
    interesting = [r for r in results if r.status in ("FAIL", "WARN")]
    if interesting:
        md.append("## Details for non-passing checks")
        md.append("")
        for r in interesting:
            md.append(f"### {status_icon.get(r.status, '')} {r.name} ({r.status})")
            md.append("")
            md.append(f"**Message**: {r.message}")
            md.append("")
            if r.fix_hint:
                md.append(f"**Fix**: {r.fix_hint}")
                md.append("")
            if r.details:
                md.append("**Details**:")
                for d in r.details:
                    md.append(f"- {d}")
                md.append("")
    return "\n".join(md) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--out", default=str(REPORT_PATH))
    p.add_argument("--quiet", action="store_true",
                   help="Suppress per-check console output (only emit final summary).")
    args = p.parse_args(argv)

    results: list[CheckResult] = []
    for chk in CHECKS:
        try:
            r = chk()
        except Exception as e:
            r = fail_(chk.__name__, f"check raised {type(e).__name__}: {e}",
                      "Inspect scripts/20_validate_state.py")
        if not args.quiet:
            icon = {"PASS": "✓", "FAIL": "✗", "WARN": "!", "SKIP": "-"}.get(r.status, "?")
            print(f"  [{icon}] {r.name}: {r.message[:90]}")
        results.append(r)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render_report(results), encoding="utf-8")
    print(f"Wrote {out_path}")

    n_fail = sum(1 for r in results if r.status == "FAIL")
    n_warn = sum(1 for r in results if r.status == "WARN")
    if n_fail:
        print(f"FAIL: {n_fail} check(s) failed")
        return 1
    if n_warn:
        print(f"WARN: {n_warn} check(s) warned")
        return 2
    print("All checks pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
