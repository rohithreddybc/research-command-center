"""
23_venue_verify.py

Verify documented venue claims against canonical sources, so we don't repeat
the "IEEE Access is free" or "ARR June deadline" class of mistake.

Reads:
  data/venue_registry.json
    A hand-maintained registry of venues we consider, with claims:
      - has_apc (true/false)
      - apc_usd (number or null)
      - typical_review_time_months
      - URL where claim was verified
      - last_verified_iso

For each venue, checks:
  1. last_verified_iso is within 180 days (claims drift; APCs change)
  2. URL is well-formed (basic check; not a live HTTP probe)
  3. If has_apc=false, apc_usd should be null/0
  4. Required fields populated

Output: reports/VENUE_VERIFICATION.md
Exit 0 if all venues recent and consistent; 1 if any fails; 2 if warnings.

This script does NOT make HTTP calls to venue sites — that's intentional
to avoid being blocked. Instead, it enforces that you re-checked each venue
within 180 days and updated the registry.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

REGISTRY_PATH = ROOT / "data" / "venue_registry.json"
REPORT_PATH   = ROOT / "reports" / "VENUE_VERIFICATION.md"

STALENESS_THRESHOLD_DAYS = 180


# ----------------------------------------------------------------------------
# Pure helpers (testable)
# ----------------------------------------------------------------------------

REQUIRED_FIELDS = [
    "name", "has_apc", "free_for_author", "typical_review_time_months",
    "url", "last_verified_iso",
]


def is_valid_url(url: str) -> bool:
    if not url:
        return False
    return bool(re.match(r"^https?://[^\s]+\.[^\s]+", url))


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


@dataclass
class VenueIssue:
    venue: str
    field: str
    severity: str   # FAIL / WARN
    message:  str


def validate_venue(v: dict, today: _dt.date | None = None) -> list[VenueIssue]:
    name = v.get("name", "?")
    issues: list[VenueIssue] = []

    for f in REQUIRED_FIELDS:
        if f not in v:
            issues.append(VenueIssue(name, f, "FAIL", f"missing required field '{f}'"))

    url = v.get("url", "")
    if url and not is_valid_url(url):
        issues.append(VenueIssue(name, "url", "FAIL", f"malformed URL: {url[:60]}"))

    has_apc = v.get("has_apc")
    apc_usd = v.get("apc_usd")
    free = v.get("free_for_author")
    if has_apc is False and apc_usd not in (None, 0, 0.0):
        issues.append(VenueIssue(name, "apc_usd", "FAIL",
                                  f"has_apc=false but apc_usd={apc_usd}"))
    if has_apc is True and (apc_usd is None or apc_usd == 0):
        issues.append(VenueIssue(name, "apc_usd", "WARN",
                                  "has_apc=true but apc_usd not set"))
    if free is True and has_apc is True and apc_usd and apc_usd > 0:
        issues.append(VenueIssue(name, "free_for_author", "FAIL",
                                  f"free_for_author=true contradicts apc_usd=${apc_usd}"))

    lv = v.get("last_verified_iso", "")
    ds = days_since(lv, today)
    if ds is None and lv:
        issues.append(VenueIssue(name, "last_verified_iso", "WARN",
                                  f"unparseable date: {lv}"))
    elif ds is not None and ds > STALENESS_THRESHOLD_DAYS:
        issues.append(VenueIssue(name, "last_verified_iso", "WARN",
                                  f"claims are {ds} days old (>{STALENESS_THRESHOLD_DAYS}) — re-verify on venue's official site"))

    return issues


def summarise(issues: list[VenueIssue]) -> dict:
    n_fail = sum(1 for i in issues if i.severity == "FAIL")
    n_warn = sum(1 for i in issues if i.severity == "WARN")
    by_venue: dict[str, list[VenueIssue]] = {}
    for i in issues:
        by_venue.setdefault(i.venue, []).append(i)
    return {"n_fail": n_fail, "n_warn": n_warn, "by_venue": by_venue}


def render_report(registry: dict, all_issues: list[VenueIssue]) -> str:
    now = _dt.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    md: list[str] = ["# Venue Verification Report", ""]
    md.append(f"*Generated: {now}*")
    md.append(f"*Source: `scripts/23_venue_verify.py`*")
    md.append(f"*Registry: `data/venue_registry.json`*")
    md.append("")
    venues = registry.get("venues", [])
    n_total = len(venues)
    summary = summarise(all_issues)
    md.append(f"**Summary**: {n_total} venues registered · "
              f"{summary['n_fail']} FAIL · {summary['n_warn']} WARN")
    md.append("")
    md.append("## Venue registry (current claims)")
    md.append("")
    md.append("| Venue | Free? | APC (USD) | Review (mo) | Last verified | Source |")
    md.append("|---|---|---|---|---|---|")
    today = _dt.date.today()
    for v in venues:
        free_disp = "✅ Yes" if v.get("free_for_author") else "❌ No"
        apc = v.get("apc_usd")
        apc_disp = f"${apc}" if apc else "—"
        rt = v.get("typical_review_time_months", "?")
        lv = v.get("last_verified_iso", "?")
        ds = days_since(lv, today)
        if ds is not None and ds > STALENESS_THRESHOLD_DAYS:
            lv_disp = f"⚠️ {lv} ({ds}d old)"
        else:
            lv_disp = f"{lv}"
        url = v.get("url", "")
        md.append(f"| {v.get('name', '?')} | {free_disp} | {apc_disp} | {rt} | "
                  f"{lv_disp} | {url[:60]} |")
    md.append("")
    if all_issues:
        md.append("## Issues to fix")
        md.append("")
        md.append("| Severity | Venue | Field | Message |")
        md.append("|---|---|---|---|")
        for i in all_issues:
            icon = "🚫" if i.severity == "FAIL" else "⚠️"
            md.append(f"| {icon} {i.severity} | {i.venue} | `{i.field}` | {i.message} |")
        md.append("")
    return "\n".join(md) + "\n"


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--registry", default=str(REGISTRY_PATH))
    p.add_argument("--out", default=str(REPORT_PATH))
    args = p.parse_args(argv)

    reg_path = Path(args.registry)
    if not reg_path.exists():
        print(f"Registry not found: {reg_path}", file=sys.stderr)
        return 1
    registry = json.loads(reg_path.read_text(encoding="utf-8"))
    venues = registry.get("venues", [])
    all_issues: list[VenueIssue] = []
    for v in venues:
        all_issues.extend(validate_venue(v))

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render_report(registry, all_issues), encoding="utf-8")
    print(f"Wrote {out_path}")
    n_fail = sum(1 for i in all_issues if i.severity == "FAIL")
    n_warn = sum(1 for i in all_issues if i.severity == "WARN")
    if n_fail:
        print(f"FAIL: {n_fail} venue issue(s)")
        return 1
    if n_warn:
        print(f"WARN: {n_warn} venue issue(s)")
        return 2
    print(f"All {len(venues)} venues consistent and within the {STALENESS_THRESHOLD_DAYS}-day verification window.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
