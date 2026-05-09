"""
04_collect_venue_evidence.py

For each topic, collect venue signal:
- DOAJ open-access candidate journals (already from 03 — re-uses)
- Crossref recent issues (proxy for indexing/active publication) for venues in venue_master.csv
- OpenReview note-search counts for selected ML venues

Writes data/evidence/<topic_id>/venues.json
Each entry includes: venue, score-axes, notes, VERIFY flags, automated_next_step.
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.http import get_json  # noqa: E402
from common.io_utils import read_csv, read_json, write_json, log, evidence_dir  # noqa: E402

QUERIES_DIR = ROOT / "data" / "queries"
VENUE_MASTER_CSV = ROOT / "05_venue_selection" / "venue_master.csv"

CROSSREF_JOURNALS = "https://api.crossref.org/journals"
OPENREVIEW_NOTES = "https://api2.openreview.net/notes/search"


def crossref_journal_check(name: str) -> dict[str, Any]:
    params = {"query": name, "rows": 5}
    status, body = get_json(CROSSREF_JOURNALS, params, min_interval=0.4)
    if not body:
        return {"name": name, "ok": False, "status": status, "results": []}
    items = body.get("message", {}).get("items", []) or []
    return {
        "name": name,
        "ok": bool(items),
        "results": [{
            "title": it.get("title"),
            "publisher": it.get("publisher"),
            "issn": it.get("ISSN"),
            "counts": it.get("counts"),
            "last-status-check-time": it.get("last-status-check-time"),
        } for it in items[:3]],
        "status": status,
    }


def openreview_notes(query: str, max_results: int = 25) -> dict[str, Any]:
    """OpenReview public note search. May not always be reliable; degrade gracefully."""
    params = {"term": query, "limit": max_results, "type": "all", "source": "all"}
    status, body = get_json(OPENREVIEW_NOTES, params, min_interval=2.0)
    notes = []
    if isinstance(body, dict):
        for n in (body.get("notes") or [])[:max_results]:
            content = n.get("content", {}) if isinstance(n.get("content"), dict) else {}
            title = content.get("title") if isinstance(content.get("title"), str) else (content.get("title", {}) or {}).get("value", "") if isinstance(content.get("title"), dict) else ""
            venue = content.get("venue") if isinstance(content.get("venue"), str) else (content.get("venue", {}) or {}).get("value", "") if isinstance(content.get("venue"), dict) else ""
            notes.append({"title": title, "venue": venue, "id": n.get("id")})
    return {"query": query, "results": notes, "status": status}


def collect_for_topic(topic_id: str, queries: dict[str, Any]) -> dict[str, Any]:
    edir = evidence_dir(topic_id)

    venues = read_csv(VENUE_MASTER_CSV) if VENUE_MASTER_CSV.exists() else []

    cross_checks: list[dict[str, Any]] = []
    for v in venues:
        cross_checks.append(crossref_journal_check(v["venue"]))

    or_checks: list[dict[str, Any]] = []
    for q in (queries.get("semantic_scholar") or [])[:2]:
        or_checks.append(openreview_notes(q, max_results=15))

    # Build per-venue evidence record
    venue_records = []
    for v in venues:
        cc = next((c for c in cross_checks if c["name"] == v["venue"]), {})
        verify_flags = []
        next_steps = []
        for k in ("apc_status_VERIFY", "timeline_VERIFY"):
            if str(v.get(k, "")).endswith("VERIFY") or "VERIFY" in str(v.get(k, "")):
                verify_flags.append(k)
                next_steps.append(
                    f"Fetch official site at {v.get('source_url','')} and DOAJ; if APC info absent, mark MANUAL."
                )
        venue_records.append({
            "venue": v["venue"],
            "type": v.get("type"),
            "credibility_prelim": v.get("credibility_prelim"),
            "fit": v.get("fit"),
            "source_url": v.get("source_url", ""),
            "crossref_active": bool(cc.get("ok")),
            "crossref_top": cc.get("results"),
            "verify_flags": verify_flags,
            "automated_next_step": next_steps,
        })

    payload = {
        "topic_id": topic_id,
        "venues": venue_records,
        "openreview_signal": or_checks,
    }
    write_json(edir / "venues.json", payload)
    log("04_venues", f"{topic_id}: venues={len(venue_records)} or_checks={len(or_checks)}")
    return {"topic_id": topic_id, "venues": len(venue_records)}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--topic", default=None)
    args = p.parse_args(argv)

    files = sorted(QUERIES_DIR.glob("*.json"))
    if args.topic:
        files = [f for f in files if f.stem == args.topic]

    summary = []
    for f in files:
        q = read_json(f)
        if not q:
            continue
        s = collect_for_topic(q["topic"]["topic_id"], q["queries"])
        summary.append(s)
    print({"summary": summary})
    return 0


if __name__ == "__main__":
    sys.exit(main())
