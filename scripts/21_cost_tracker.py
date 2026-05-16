"""
21_cost_tracker.py

Track API spend on T02 experiments (and any other future projects that log
JSON-line judge calls).

Background
----------
T02 PROTOCOL §3 budgets ~$1,500 for API calls. KILL_CRITERIA K3 fires if cost
exceeds $1,500 with <80% complete. This script:

  1. Reads data/runs/*.jsonl (or any directory of judge-call logs)
  2. Aggregates spend per model / task / day
  3. Compares vs the budget cap
  4. Projects spend at current daily rate
  5. Writes reports/T02_COST.md

Per-call JSON schema (per T02 CODE_SCAFFOLD.md)
-----------------------------------------------
  {
    "call_id":   str,
    "timestamp": iso8601,
    "model":     str,
    "task":      str,
    "condition": str,
    "item_id":   str,
    "cost_usd":  float,
    ...
  }

This script is robust to: missing fields, malformed lines, lines without cost.

Usage
-----
  python scripts/21_cost_tracker.py
  python scripts/21_cost_tracker.py --runs-dir data/runs --budget-usd 1500
  python scripts/21_cost_tracker.py --json   # machine-readable output
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

DEFAULT_RUNS_DIR = ROOT / "data" / "runs"
DEFAULT_REPORT   = ROOT / "reports" / "T02_COST.md"
DEFAULT_BUDGET   = 1500.0   # USD; from T02 PROTOCOL §3
WARN_THRESHOLD   = 0.80     # warn at 80% of budget
FAIL_THRESHOLD   = 1.00     # hard fail at 100%


# ----------------------------------------------------------------------------
# Pure helpers (testable without filesystem)
# ----------------------------------------------------------------------------

def parse_jsonl_line(line: str) -> dict | None:
    """Parse one JSONL line. Returns None for blank / unparseable."""
    line = line.strip()
    if not line:
        return None
    try:
        return json.loads(line)
    except json.JSONDecodeError:
        return None


def aggregate_calls(records: list[dict]) -> dict[str, Any]:
    """Aggregate judge-call records into spend summaries."""
    per_model:     dict[str, float] = defaultdict(float)
    per_task:      dict[str, float] = defaultdict(float)
    per_day:       dict[str, float] = defaultdict(float)
    per_condition: dict[str, float] = defaultdict(float)
    n_calls = 0
    n_with_cost = 0
    n_with_no_cost = 0
    n_zero_cost = 0
    total_usd = 0.0

    for rec in records:
        if not isinstance(rec, dict):
            continue
        n_calls += 1
        cost = rec.get("cost_usd")
        if cost is None:
            n_with_no_cost += 1
            continue
        try:
            cost_f = float(cost)
        except (TypeError, ValueError):
            n_with_no_cost += 1
            continue
        n_with_cost += 1
        if cost_f == 0:
            n_zero_cost += 1
        total_usd += cost_f

        model = (rec.get("model") or "unknown").strip()
        task  = (rec.get("task")  or "unknown").strip()
        cond  = (rec.get("condition") or "unknown").strip()
        per_model[model] += cost_f
        per_task[task]   += cost_f
        per_condition[cond] += cost_f

        ts = rec.get("timestamp") or ""
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", str(ts))
        day = m.group(0) if m else "unknown"
        per_day[day] += cost_f

    return {
        "n_calls":         n_calls,
        "n_with_cost":     n_with_cost,
        "n_with_no_cost":  n_with_no_cost,
        "n_zero_cost":     n_zero_cost,
        "total_usd":       round(total_usd, 4),
        "per_model":       dict(per_model),
        "per_task":        dict(per_task),
        "per_day":         dict(per_day),
        "per_condition":   dict(per_condition),
    }


def daily_rate_and_projection(per_day: dict[str, float],
                              today: _dt.date | None = None) -> dict:
    """Compute average daily spend (over days with non-zero spend),
    and project N days forward at that rate."""
    days_with_spend = [(d, c) for d, c in per_day.items()
                       if d != "unknown" and c > 0]
    if not days_with_spend:
        return {"days_active": 0, "avg_daily_usd": 0.0,
                "first_day": None, "last_day": None,
                "projected_30d_usd": 0.0, "projected_60d_usd": 0.0}
    days_with_spend.sort()
    first_day = days_with_spend[0][0]
    last_day  = days_with_spend[-1][0]
    total_in_window = sum(c for _, c in days_with_spend)
    days_active = len(days_with_spend)
    avg_daily = total_in_window / max(1, days_active)
    return {
        "days_active":   days_active,
        "avg_daily_usd": round(avg_daily, 4),
        "first_day":     first_day,
        "last_day":      last_day,
        "projected_30d_usd": round(avg_daily * 30, 2),
        "projected_60d_usd": round(avg_daily * 60, 2),
    }


def status_vs_budget(total_usd: float, budget_usd: float) -> tuple[str, float]:
    """Return ('OK'/'WARN'/'FAIL', fraction_of_budget)."""
    if budget_usd <= 0:
        return ("WARN", 0.0)
    frac = total_usd / budget_usd
    if frac >= FAIL_THRESHOLD:
        return ("FAIL", frac)
    if frac >= WARN_THRESHOLD:
        return ("WARN", frac)
    return ("OK", frac)


# ----------------------------------------------------------------------------
# IO
# ----------------------------------------------------------------------------

def load_runs(runs_dir: Path) -> list[dict]:
    """Load all JSONL files in runs_dir; return concatenated records."""
    out: list[dict] = []
    if not runs_dir.exists():
        return out
    for f in sorted(runs_dir.glob("*.jsonl")):
        with f.open(encoding="utf-8") as fp:
            for line in fp:
                rec = parse_jsonl_line(line)
                if rec is not None:
                    out.append(rec)
    return out


def render_report(agg: dict, proj: dict, budget_usd: float,
                  status: str, frac: float) -> str:
    now = _dt.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    md: list[str] = ["# T02 API Cost Tracker", ""]
    md.append(f"*Generated: {now}*")
    md.append(f"*Source: `scripts/21_cost_tracker.py`*")
    md.append("")
    md.append("## Headline")
    md.append("")
    md.append(f"- **Total spend**: ${agg['total_usd']:.2f}")
    md.append(f"- **Budget cap**: ${budget_usd:.2f}")
    md.append(f"- **Fraction used**: {frac*100:.1f}%")
    md.append(f"- **Status**: **{status}**")
    md.append("")
    if status == "FAIL":
        md.append("> 🚨 **BUDGET BREACHED** — re-evaluate per `KILL_CRITERIA.md` K3.")
        md.append("")
    elif status == "WARN":
        md.append("> ⚠️ Spend ≥80% of budget — drop a model or task per "
                  "`PROTOCOL.md` §8 scope reductions.")
        md.append("")
    md.append("## Call totals")
    md.append("")
    md.append(f"- Total calls: {agg['n_calls']}")
    md.append(f"- Calls with cost field: {agg['n_with_cost']}")
    md.append(f"- Calls missing cost: {agg['n_with_no_cost']}")
    md.append(f"- Calls with zero cost: {agg['n_zero_cost']}")
    md.append("")
    md.append("## Spend per model")
    md.append("")
    md.append("| Model | USD |")
    md.append("|---|---|")
    for model, usd in sorted(agg["per_model"].items(), key=lambda x: -x[1]):
        md.append(f"| {model} | ${usd:.2f} |")
    md.append("")
    md.append("## Spend per task")
    md.append("")
    md.append("| Task | USD |")
    md.append("|---|---|")
    for task, usd in sorted(agg["per_task"].items(), key=lambda x: -x[1]):
        md.append(f"| {task} | ${usd:.2f} |")
    md.append("")
    md.append("## Spend per condition")
    md.append("")
    md.append("| Condition | USD |")
    md.append("|---|---|")
    for cond, usd in sorted(agg["per_condition"].items(), key=lambda x: -x[1]):
        md.append(f"| {cond} | ${usd:.2f} |")
    md.append("")
    md.append("## Spend timeline")
    md.append("")
    md.append(f"- Active days: {proj['days_active']}")
    md.append(f"- First day with spend: {proj['first_day'] or 'n/a'}")
    md.append(f"- Last day with spend: {proj['last_day'] or 'n/a'}")
    md.append(f"- Avg daily spend: ${proj['avg_daily_usd']:.2f}")
    md.append(f"- Projected 30-day spend (at current rate): ${proj['projected_30d_usd']:.2f}")
    md.append(f"- Projected 60-day spend (at current rate): ${proj['projected_60d_usd']:.2f}")
    md.append("")
    md.append("## Per-day breakdown")
    md.append("")
    md.append("| Day | USD |")
    md.append("|---|---|")
    for day, usd in sorted(agg["per_day"].items()):
        md.append(f"| {day} | ${usd:.2f} |")
    md.append("")
    return "\n".join(md) + "\n"


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--runs-dir", default=str(DEFAULT_RUNS_DIR),
                   help="Directory of JSONL run logs (default: data/runs/)")
    p.add_argument("--budget-usd", type=float, default=DEFAULT_BUDGET,
                   help=f"Budget cap in USD (default: {DEFAULT_BUDGET})")
    p.add_argument("--out", default=str(DEFAULT_REPORT))
    p.add_argument("--json", action="store_true",
                   help="Emit a JSON summary on stdout instead of markdown")
    args = p.parse_args(argv)

    runs_dir = Path(args.runs_dir)
    records = load_runs(runs_dir)
    agg = aggregate_calls(records)
    proj = daily_rate_and_projection(agg["per_day"])
    status, frac = status_vs_budget(agg["total_usd"], args.budget_usd)

    if args.json:
        out = {**agg, "projection": proj,
               "budget_usd": args.budget_usd,
               "status": status,
               "fraction_used": frac}
        print(json.dumps(out, indent=2))
        return (1 if status == "FAIL" else (2 if status == "WARN" else 0))

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    report = render_report(agg, proj, args.budget_usd, status, frac)
    out_path.write_text(report, encoding="utf-8")
    print(f"[cost-tracker] total ${agg['total_usd']:.2f} of ${args.budget_usd:.2f} ({frac*100:.1f}%) — {status}")
    print(f"Wrote {out_path}")

    return (1 if status == "FAIL" else (2 if status == "WARN" else 0))


if __name__ == "__main__":
    sys.exit(main())
