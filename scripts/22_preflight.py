"""
22_preflight.py

Pre-submission preflight checker. Run before clicking 'Submit' on any paper.

Gates (in order):
  1. State validator passes (scripts/20_validate_state.py exit 0 or 2)
  2. Test suite passes (subprocess pytest)
  3. Title check verdict for the paper's title is CLEAR
  4. Scoop watch has NO kill signals
  5. Required protocol files complete (PROTOCOL, KILL_CRITERIA)
  6. Reproducibility manifest exists (data/_snapshots/*)
  7. References .bib file exists for the topic
  8. If T02-style: cost tracker shows within budget

Output: reports/PREFLIGHT.md
Exit 0 ONLY if every gate passes.
Exit 1 if any FAIL.
Exit 2 if only WARN.

Usage
-----
  # Preflight for the survey
  python scripts/22_preflight.py --project SURVEY_llm_judge --title "Trustworthy LLM-as-a-Judge: A Comprehensive Survey of Methods, Failure Modes, and Defences"

  # Preflight for T02 bridge
  python scripts/22_preflight.py --project T02_position_bias --title "Position Bias in LLM Judges: A Cross-Model Quantification"
"""
from __future__ import annotations

import argparse
import datetime as _dt
import importlib.util
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

REPORT_PATH = ROOT / "reports" / "PREFLIGHT.md"


@dataclass
class Gate:
    name:     str
    status:   str               # "PASS" / "FAIL" / "WARN" / "SKIP"
    message:  str
    fix_hint: str = ""


def pass_(name: str, msg: str) -> Gate:
    return Gate(name=name, status="PASS", message=msg)

def fail_(name: str, msg: str, fix: str = "") -> Gate:
    return Gate(name=name, status="FAIL", message=msg, fix_hint=fix)

def warn_(name: str, msg: str, fix: str = "") -> Gate:
    return Gate(name=name, status="WARN", message=msg, fix_hint=fix)

def skip_(name: str, msg: str) -> Gate:
    return Gate(name=name, status="SKIP", message=msg)


# ----------------------------------------------------------------------------
# Pure helpers (testable)
# ----------------------------------------------------------------------------

def title_check_status(title: str, report_md: str) -> tuple[str, float] | None:
    """Find the verdict for the given title in TITLE_CHECK.md.

    Returns (verdict, top_similarity) or None if not found.
    """
    if not report_md or not title:
        return None
    # Section headers look like "## <title>"
    pattern = re.compile(
        rf"^##\s+{re.escape(title)}\s*$",
        re.MULTILINE,
    )
    m = pattern.search(report_md)
    if not m:
        return None
    section_start = m.end()
    # Find next section or EOF
    next_m = re.search(r"^##\s+", report_md[section_start:], re.MULTILINE)
    section_text = report_md[section_start:
                              (section_start + next_m.start()) if next_m else len(report_md)]
    # Parse "Verdict: **X**" and "Top similarity: Y"
    v_m = re.search(r"Verdict:\s*\*\*([A-Z\-]+)\*\*", section_text)
    s_m = re.search(r"Top similarity:\s*([\d\.]+)", section_text)
    verdict = v_m.group(1) if v_m else "UNKNOWN"
    sim = float(s_m.group(1)) if s_m else 0.0
    return (verdict, sim)


def scoop_kill_count(report_md: str) -> int | None:
    """Find 'Papers with kill-signal keywords' count in SCOOP_WATCH.md."""
    if not report_md:
        return None
    m = re.search(r"Papers with kill-signal keywords:\s*\*\*(\d+)\*\*", report_md)
    if not m:
        return None
    return int(m.group(1))


def days_since(iso_str: str, today: _dt.date | None = None) -> int | None:
    if not iso_str:
        return None
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", iso_str)
    if not m:
        return None
    try:
        d = _dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None
    t = today or _dt.date.today()
    return (t - d).days


# ----------------------------------------------------------------------------
# Gates
# ----------------------------------------------------------------------------

def gate_state_validator() -> Gate:
    script = ROOT / "scripts" / "20_validate_state.py"
    if not script.exists():
        return skip_("state_validator", "scripts/20_validate_state.py missing")
    try:
        r = subprocess.run([sys.executable, str(script), "--quiet"],
                           capture_output=True, text=True, timeout=120)
    except Exception as e:
        return fail_("state_validator",
                     f"could not invoke 20_validate_state.py: {e}")
    if r.returncode == 0:
        return pass_("state_validator", "All state-validation checks pass")
    if r.returncode == 2:
        return warn_("state_validator",
                     "State validator reports warnings (non-blocking)",
                     "Read reports/STATE_VALIDATION.md and fix warnings")
    return fail_("state_validator",
                 "State validator failed",
                 "Read reports/STATE_VALIDATION.md and fix failures")


def gate_tests_pass() -> Gate:
    test_path = ROOT / "scripts" / "tests" / "test_pipeline.py"
    if not test_path.exists():
        return fail_("tests_pass", "Test file missing")
    try:
        r = subprocess.run([sys.executable, "-m", "pytest", str(test_path), "-q"],
                           capture_output=True, text=True, timeout=300)
    except Exception as e:
        return fail_("tests_pass", f"could not invoke pytest: {e}")
    if r.returncode != 0:
        # Extract last few lines of output
        tail = "\n".join(r.stdout.strip().splitlines()[-4:])
        return fail_("tests_pass",
                     f"pytest failed: {tail[:200]}",
                     "Fix failing tests")
    # Extract pass count
    m = re.search(r"(\d+) passed", r.stdout)
    n = m.group(1) if m else "?"
    return pass_("tests_pass", f"{n} tests pass")


def gate_title_clear(title: str | None) -> Gate:
    if not title:
        return skip_("title_clear", "No --title provided; skipping check")
    report = ROOT / "reports" / "TITLE_CHECK.md"
    if not report.exists():
        return fail_("title_clear",
                     "reports/TITLE_CHECK.md missing",
                     f"Run: python scripts/19_title_check.py --title \"{title}\"")
    text = report.read_text(encoding="utf-8")
    result = title_check_status(title, text)
    if result is None:
        return fail_("title_clear",
                     f"No title-check result found for '{title[:60]}…'",
                     f"Run: python scripts/19_title_check.py --title \"{title}\"")
    verdict, sim = result
    if verdict == "CLEAR":
        return pass_("title_clear",
                     f"Title verdict: CLEAR (top sim {sim})")
    if verdict in ("WEAK-ECHO",):
        return warn_("title_clear",
                     f"Title verdict: {verdict} (top sim {sim}) — acceptable but watch",
                     "Consider a fallback title")
    return fail_("title_clear",
                 f"Title verdict: {verdict} (top sim {sim}) — DO NOT SUBMIT",
                 f"Rotate to a fallback title and re-run title check")


def gate_scoop_no_kill() -> Gate:
    report = ROOT / "reports" / "SCOOP_WATCH.md"
    if not report.exists():
        return fail_("scoop_no_kill",
                     "reports/SCOOP_WATCH.md missing",
                     "Run: python scripts/15_arxiv_watch.py")
    text = report.read_text(encoding="utf-8")
    # Last-run staleness
    m = re.search(r"Last run:\s*([\d\-T:Z]+)", text)
    if m:
        ds = days_since(m.group(1))
        if ds is not None and ds > 7:
            return warn_("scoop_no_kill",
                         f"Scoop watch is {ds} days old (>7) — refresh first",
                         "Run: python scripts/15_arxiv_watch.py")
    n_kill = scoop_kill_count(text)
    if n_kill is None:
        return warn_("scoop_no_kill",
                     "Could not parse kill-signal count from SCOOP_WATCH.md")
    if n_kill > 0:
        return fail_("scoop_no_kill",
                     f"{n_kill} kill-signal paper(s) in SCOOP_WATCH.md — DO NOT SUBMIT",
                     "Read each kill-signal paper; pivot or differentiate per KILL_CRITERIA")
    return pass_("scoop_no_kill", "No kill signals in scoop watch")


def gate_protocol_files(project: str | None) -> Gate:
    if not project:
        return skip_("protocol_files", "No --project provided")
    proj_dir = ROOT / "06_paper_pipeline" / project
    if not proj_dir.is_dir():
        return fail_("protocol_files",
                     f"Project dir not found: {proj_dir.relative_to(ROOT)}",
                     "Verify --project name (e.g., T02_position_bias / SURVEY_llm_judge)")
    required = ["PROTOCOL.md", "KILL_CRITERIA.md"]
    missing = [r for r in required if not (proj_dir / r).exists()]
    if missing:
        return fail_("protocol_files",
                     f"Missing required files in {project}: {', '.join(missing)}")
    return pass_("protocol_files",
                 f"All required files present in {project}/")


def gate_reproducibility_snapshot() -> Gate:
    snap_dir = ROOT / "data" / "_snapshots"
    if not snap_dir.is_dir():
        return warn_("reproducibility_snapshot",
                     "data/_snapshots/ not present",
                     "Create a snapshot before submission")
    snaps = list(snap_dir.glob("*.json"))
    if not snaps:
        return warn_("reproducibility_snapshot",
                     "No snapshots found",
                     "Generate a snapshot of pipeline state at submission")
    return pass_("reproducibility_snapshot",
                 f"{len(snaps)} snapshot file(s) present in data/_snapshots/")


def gate_references_bib(project: str | None) -> Gate:
    if not project:
        return skip_("references_bib", "No --project provided")
    # Map project dir name -> bibtex stem
    bib_stem = {
        "T02_position_bias":     "T02",
        "T07_judge_injection":   "T07",
        "T01_cross_judge":       "T01",
        "SURVEY_llm_judge":      None,   # survey draws from many topics
    }.get(project, None)
    if bib_stem is None:
        return skip_("references_bib", "No expected single .bib for this project")
    bib = ROOT / "references" / f"{bib_stem}.bib"
    if not bib.exists():
        return fail_("references_bib",
                     f"references/{bib_stem}.bib missing",
                     f"Run: python scripts/16_extract_bibtex.py --topic {bib_stem}")
    n = bib.read_text(encoding="utf-8").count("@")
    if n < 5:
        return warn_("references_bib",
                     f"references/{bib_stem}.bib has only {n} entries",
                     "Consider lowering --min-relevance to include more")
    return pass_("references_bib",
                 f"references/{bib_stem}.bib has {n} entries")


def gate_cost_within_budget() -> Gate:
    script = ROOT / "scripts" / "21_cost_tracker.py"
    if not script.exists():
        return skip_("cost_within_budget", "21_cost_tracker.py missing")
    runs_dir = ROOT / "data" / "runs"
    if not runs_dir.exists() or not list(runs_dir.glob("*.jsonl")):
        return skip_("cost_within_budget",
                     "No data/runs/*.jsonl yet (no experiments executed)")
    try:
        r = subprocess.run([sys.executable, str(script), "--json"],
                           capture_output=True, text=True, timeout=60)
    except Exception as e:
        return warn_("cost_within_budget", f"could not invoke cost tracker: {e}")
    if r.returncode == 1:
        return fail_("cost_within_budget",
                     "Cost exceeds budget cap",
                     "See reports/T02_COST.md")
    if r.returncode == 2:
        return warn_("cost_within_budget",
                     "Cost at >=80% of budget",
                     "Consider scope reductions per PROTOCOL.md §8")
    # Parse total from JSON
    try:
        data = json.loads(r.stdout)
        total = data.get("total_usd", 0)
        budget = data.get("budget_usd", 0)
    except Exception:
        total, budget = 0, 0
    return pass_("cost_within_budget",
                 f"Spend ${total:.2f} of ${budget:.2f} budget (within limits)")


# ----------------------------------------------------------------------------
# Runner
# ----------------------------------------------------------------------------

def render_report(gates: list[Gate], project: str | None, title: str | None) -> str:
    now = _dt.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    n_pass = sum(1 for g in gates if g.status == "PASS")
    n_fail = sum(1 for g in gates if g.status == "FAIL")
    n_warn = sum(1 for g in gates if g.status == "WARN")
    n_skip = sum(1 for g in gates if g.status == "SKIP")
    md: list[str] = ["# Preflight Report", ""]
    md.append(f"*Generated: {now}*")
    md.append(f"*Project: `{project or '(none)'}`*")
    md.append(f"*Title: `{(title or '(none)')[:100]}`*")
    md.append("")
    md.append(f"**Summary**: {n_pass} PASS · {n_fail} FAIL · {n_warn} WARN · {n_skip} SKIP")
    md.append("")
    if n_fail:
        md.append("🚫 **DO NOT SUBMIT** — preflight failed.")
    elif n_warn:
        md.append("⚠️ Warnings present. Submit only after reviewing each warning.")
    else:
        md.append("✅ All gates pass. Cleared for submission.")
    md.append("")
    md.append("## Gates")
    md.append("")
    icon = {"PASS": "✅", "FAIL": "🚫", "WARN": "⚠️", "SKIP": "⏭️"}
    md.append("| Status | Gate | Message |")
    md.append("|---|---|---|")
    for g in gates:
        md.append(f"| {icon.get(g.status, '')} {g.status} | `{g.name}` | {g.message[:100]} |")
    md.append("")
    # Detail blocks for non-pass
    non_pass = [g for g in gates if g.status in ("FAIL", "WARN")]
    if non_pass:
        md.append("## Action items")
        md.append("")
        for g in non_pass:
            md.append(f"### {icon.get(g.status, '')} {g.name}")
            md.append("")
            md.append(f"**Status**: {g.status}")
            md.append(f"**Message**: {g.message}")
            if g.fix_hint:
                md.append(f"**Fix**: {g.fix_hint}")
            md.append("")
    return "\n".join(md) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--project", required=False,
                   help="Project directory name under 06_paper_pipeline/")
    p.add_argument("--title", required=False,
                   help="Final paper title (must appear in TITLE_CHECK.md)")
    p.add_argument("--out", default=str(REPORT_PATH))
    args = p.parse_args(argv)

    gates: list[Gate] = []
    print("[preflight] Running gates...")
    gates.append(gate_state_validator());                  print(f"  - state_validator: {gates[-1].status}")
    gates.append(gate_tests_pass());                       print(f"  - tests_pass: {gates[-1].status}")
    gates.append(gate_title_clear(args.title));            print(f"  - title_clear: {gates[-1].status}")
    gates.append(gate_scoop_no_kill());                    print(f"  - scoop_no_kill: {gates[-1].status}")
    gates.append(gate_protocol_files(args.project));       print(f"  - protocol_files: {gates[-1].status}")
    gates.append(gate_reproducibility_snapshot());         print(f"  - reproducibility_snapshot: {gates[-1].status}")
    gates.append(gate_references_bib(args.project));       print(f"  - references_bib: {gates[-1].status}")
    gates.append(gate_cost_within_budget());               print(f"  - cost_within_budget: {gates[-1].status}")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render_report(gates, args.project, args.title), encoding="utf-8")
    print(f"Wrote {out_path}")

    n_fail = sum(1 for g in gates if g.status == "FAIL")
    n_warn = sum(1 for g in gates if g.status == "WARN")
    if n_fail:
        print(f"DO NOT SUBMIT — {n_fail} gate(s) failed.")
        return 1
    if n_warn:
        print(f"Submit with caution — {n_warn} warning(s).")
        return 2
    print("CLEARED — all gates pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
