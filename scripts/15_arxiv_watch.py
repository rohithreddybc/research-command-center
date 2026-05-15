"""
15_arxiv_watch.py

Daily / weekly arXiv scoop watch.

For each query in `data/scoop_watch_queries.json`, fetch new arXiv papers
since the last run, score them by keyword relevance, and emit a markdown
alert (`reports/SCOOP_WATCH.md`) when potential scoops appear.

Why this exists
---------------
The bridge publication strategy (`reports/BRIDGE_PUBLICATION_STRATEGY.md`)
depends on no scoop appearing on T02, T07, T01, or B05 during execution.
Manual checking of arXiv each week is brittle. This script automates the
detection and produces an actionable diff.

State tracking
--------------
`data/scoop_watch/_state.json` records, per query:
  - last_run_iso8601
  - seen_arxiv_ids (so we only flag NEW papers, not re-runs)
  - n_new_last_run

First run with no state: bootstraps with the most recent N papers per query
(default 25), marks them all as "baseline" (not new), and seeds the state.
Subsequent runs only report papers added since the last run that exceed the
relevance threshold.

Relevance scoring
-----------------
Simple keyword-overlap score in [0,1]:
  score = (# matched keywords in title+abstract) / max(1, # keywords)

Plus a `kill_signal` boolean if any of the kill-threshold keywords appear
(e.g., for T02 a paper that has both "position bias" AND "released harness"
is a stronger scoop signal than one that only has "position bias").

Usage
-----
  # Normal: report what's new since last run
  python scripts/15_arxiv_watch.py

  # First-time bootstrap (or rebuild state):
  python scripts/15_arxiv_watch.py --bootstrap

  # Look back N days (overrides state):
  python scripts/15_arxiv_watch.py --days 14

  # Dry run (no API calls; uses cached results if available):
  python scripts/15_arxiv_watch.py --dry-run
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

QUERIES_FILE  = ROOT / "data" / "scoop_watch_queries.json"
STATE_DIR     = ROOT / "data" / "scoop_watch"
STATE_FILE    = STATE_DIR / "_state.json"
RAW_DIR       = STATE_DIR / "raw"
REPORT_FILE   = ROOT / "reports" / "SCOOP_WATCH.md"

ARXIV_API = "http://export.arxiv.org/api/query"
ATOM_NS = "{http://www.w3.org/2005/Atom}"
ARXIV_NS = "{http://arxiv.org/schemas/atom}"


# ----------------------------------------------------------------------------
# Pure helpers (testable without network)
# ----------------------------------------------------------------------------

def relevance_score(title: str, summary: str, keywords: list[str]) -> float:
    """Simple keyword-overlap score in [0,1]. Case-insensitive substring match."""
    if not keywords:
        return 0.0
    text = f"{title}\n{summary}".lower()
    n_match = sum(1 for kw in keywords if kw.lower() in text)
    return n_match / max(1, len(keywords))


def kill_signal(title: str, summary: str,
                kill_keywords: list[str]) -> tuple[bool, list[str]]:
    """Return (any kill keyword present, list of which keywords matched)."""
    if not kill_keywords:
        return (False, [])
    text = f"{title}\n{summary}".lower()
    matched = [kw for kw in kill_keywords if kw.lower() in text]
    return (bool(matched), matched)


def diff_new_ids(current_ids: list[str],
                 seen_ids: list[str]) -> list[str]:
    """Return arXiv IDs in current_ids but not in seen_ids."""
    seen = set(seen_ids)
    return [aid for aid in current_ids if aid not in seen]


def parse_atom_feed(xml_text: str) -> list[dict]:
    """Parse an arXiv Atom feed into a list of paper dicts.

    Each dict: {arxiv_id, title, summary, published, updated, authors, categories, link}
    """
    root = ET.fromstring(xml_text)
    out: list[dict] = []
    for entry in root.findall(f"{ATOM_NS}entry"):
        eid = (entry.findtext(f"{ATOM_NS}id") or "").strip()
        # arXiv ids look like: http://arxiv.org/abs/2501.01234v1
        m = re.search(r"abs/([\w.\-]+?)(?:v\d+)?$", eid)
        arxiv_id = m.group(1) if m else eid

        title = " ".join((entry.findtext(f"{ATOM_NS}title") or "").split())
        summary = " ".join((entry.findtext(f"{ATOM_NS}summary") or "").split())
        published = (entry.findtext(f"{ATOM_NS}published") or "").strip()
        updated   = (entry.findtext(f"{ATOM_NS}updated") or "").strip()

        authors = []
        for author in entry.findall(f"{ATOM_NS}author"):
            name = (author.findtext(f"{ATOM_NS}name") or "").strip()
            if name:
                authors.append(name)

        categories = []
        for cat in entry.findall(f"{ATOM_NS}category"):
            term = cat.attrib.get("term", "").strip()
            if term:
                categories.append(term)

        link = ""
        for ln in entry.findall(f"{ATOM_NS}link"):
            if ln.attrib.get("rel") == "alternate":
                link = ln.attrib.get("href", "")
                break
        if not link:
            link = f"https://arxiv.org/abs/{arxiv_id}"

        out.append({
            "arxiv_id": arxiv_id,
            "title":     title,
            "summary":   summary,
            "published": published,
            "updated":   updated,
            "authors":   authors,
            "categories": categories,
            "link":      link,
        })
    return out


# ----------------------------------------------------------------------------
# Network
# ----------------------------------------------------------------------------

def fetch_arxiv(arxiv_query: str, categories: list[str],
                max_results: int = 50,
                start: int = 0,
                timeout: float = 30.0) -> str:
    """Fetch raw Atom feed from arXiv API. Returns XML text."""
    cat_filter = " OR ".join(f"cat:{c}" for c in categories)
    if cat_filter:
        full_query = f"({arxiv_query}) AND ({cat_filter})"
    else:
        full_query = arxiv_query
    params = {
        "search_query": full_query,
        "start": str(start),
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "research-command-center/scoop-watch/1.0 (mailto:rohithreddybc@gmail.com)",
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


# ----------------------------------------------------------------------------
# State
# ----------------------------------------------------------------------------

def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"queries": {}, "_format_version": 1}


def save_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


# ----------------------------------------------------------------------------
# Main flow
# ----------------------------------------------------------------------------

def process_query(qspec: dict, state: dict, *,
                  bootstrap: bool = False,
                  dry_run: bool = False,
                  max_results: int = 50) -> dict:
    """Process one watch query. Returns a result dict for the report.

    Result schema:
      {
        query_id, topic_id, title, watch_priority,
        n_fetched, n_new, n_relevant, n_kill_signal,
        new_papers: [{arxiv_id, title, summary, published, link, score, kill_keywords}],
        kill_papers: [...],   # subset of new_papers with kill_signal=True
        error: str | None,
      }
    """
    query_id = qspec["id"]
    qstate = state.setdefault("queries", {}).setdefault(query_id, {})
    seen_ids: list[str] = qstate.get("seen_arxiv_ids", [])

    result: dict[str, Any] = {
        "query_id":       query_id,
        "topic_id":       qspec.get("topic_id", ""),
        "title":          qspec.get("title", ""),
        "watch_priority": qspec.get("watch_priority", "MEDIUM"),
        "n_fetched":      0,
        "n_new":          0,
        "n_relevant":     0,
        "n_kill_signal":  0,
        "new_papers":     [],
        "kill_papers":    [],
        "error":          None,
    }

    if dry_run:
        # Use cached raw if available
        raw_path = RAW_DIR / f"{query_id}_latest.xml"
        if not raw_path.exists():
            result["error"] = "dry-run requested but no cached raw feed available"
            return result
        xml_text = raw_path.read_text(encoding="utf-8")
    else:
        try:
            xml_text = fetch_arxiv(qspec["arxiv_query"],
                                   qspec.get("categories", []),
                                   max_results=max_results)
            RAW_DIR.mkdir(parents=True, exist_ok=True)
            (RAW_DIR / f"{query_id}_latest.xml").write_text(xml_text, encoding="utf-8")
        except Exception as e:
            result["error"] = f"fetch failed: {e}"
            return result

    try:
        papers = parse_atom_feed(xml_text)
    except Exception as e:
        result["error"] = f"parse failed: {e}"
        return result

    result["n_fetched"] = len(papers)
    current_ids = [p["arxiv_id"] for p in papers]

    if bootstrap:
        # Treat all current as baseline; do not flag as new.
        qstate["seen_arxiv_ids"] = list(set(seen_ids) | set(current_ids))
        qstate["last_run_iso8601"] = _dt.datetime.utcnow().isoformat() + "Z"
        qstate["n_new_last_run"] = 0
        return result

    new_ids = diff_new_ids(current_ids, seen_ids)
    result["n_new"] = len(new_ids)

    relevance_keywords = qspec.get("relevance_keywords", [])
    kill_keywords      = qspec.get("kill_threshold_keywords", [])
    min_rel            = float(qspec.get("min_relevance", 0.3))

    by_id = {p["arxiv_id"]: p for p in papers}
    for aid in new_ids:
        p = by_id[aid]
        score = relevance_score(p["title"], p["summary"], relevance_keywords)
        kill, kill_kws = kill_signal(p["title"], p["summary"], kill_keywords)
        if score < min_rel and not kill:
            continue
        entry = {
            "arxiv_id":       p["arxiv_id"],
            "title":          p["title"],
            "summary":        p["summary"][:400],
            "published":      p["published"],
            "link":           p["link"],
            "authors":        p["authors"][:5],
            "categories":     p["categories"],
            "relevance_score": round(score, 3),
            "kill_signal":    kill,
            "kill_keywords":  kill_kws,
        }
        result["new_papers"].append(entry)
        result["n_relevant"] += 1
        if kill:
            result["kill_papers"].append(entry)
            result["n_kill_signal"] += 1

    # Update state
    qstate["seen_arxiv_ids"] = list(set(seen_ids) | set(current_ids))
    qstate["last_run_iso8601"] = _dt.datetime.utcnow().isoformat() + "Z"
    qstate["n_new_last_run"] = result["n_new"]

    return result


def render_report(results: list[dict]) -> str:
    """Render the SCOOP_WATCH.md content."""
    now = _dt.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    md: list[str] = []
    md.append("# arXiv Scoop Watch")
    md.append("")
    md.append(f"*Last run: {now}*")
    md.append(f"*Source: `scripts/15_arxiv_watch.py` (config: `data/scoop_watch_queries.json`)*")
    md.append("")
    total_new = sum(r["n_new"] for r in results)
    total_relevant = sum(r["n_relevant"] for r in results)
    total_kill = sum(r["n_kill_signal"] for r in results)
    md.append(f"## Summary")
    md.append("")
    md.append(f"- Queries run: **{len(results)}**")
    md.append(f"- New papers fetched (across all queries): **{total_new}**")
    md.append(f"- Relevant new papers: **{total_relevant}**")
    md.append(f"- ⚠️ Papers with kill-signal keywords: **{total_kill}**")
    md.append("")

    # Errors first
    errored = [r for r in results if r.get("error")]
    if errored:
        md.append("## ⚠️ Errors")
        md.append("")
        for r in errored:
            md.append(f"- **{r['query_id']}**: {r['error']}")
        md.append("")

    # Kill signals upfront
    if total_kill > 0:
        md.append("## 🚨 KILL SIGNAL — read these papers within 48 hours")
        md.append("")
        for r in results:
            for p in r["kill_papers"]:
                md.append(f"### {r['query_id']} — `{p['arxiv_id']}`")
                md.append(f"**{p['title']}**")
                md.append("")
                md.append(f"- Published: {p['published']}")
                md.append(f"- Authors: {', '.join(p['authors'])}")
                md.append(f"- Link: {p['link']}")
                md.append(f"- Relevance score: {p['relevance_score']}")
                md.append(f"- Kill keywords matched: {', '.join(p['kill_keywords'])}")
                md.append("")
                md.append(f"> {p['summary']}")
                md.append("")
                md.append("**Action**: see `06_paper_pipeline/<topic>/KILL_CRITERIA.md`")
                md.append("")

    # Per-query sections
    md.append("## Per-query results")
    md.append("")
    for r in results:
        if r.get("error"):
            continue
        md.append(f"### {r['query_id']} ({r['watch_priority']})")
        md.append(f"_{r['title']}_")
        md.append("")
        md.append(f"- Fetched: {r['n_fetched']}, New: {r['n_new']}, Relevant: {r['n_relevant']}, Kill: {r['n_kill_signal']}")
        md.append("")
        if not r["new_papers"]:
            md.append("_No new relevant papers since last run._")
            md.append("")
            continue
        md.append("| arXiv ID | Score | Kill | Title | Published |")
        md.append("|---|---|---|---|---|")
        for p in r["new_papers"]:
            kill_mark = "⚠️" if p["kill_signal"] else "—"
            md.append(f"| [{p['arxiv_id']}]({p['link']}) | {p['relevance_score']} | {kill_mark} | "
                      f"{p['title'][:80]} | {p['published'][:10]} |")
        md.append("")

    md.append("---")
    md.append("")
    md.append("## How to act")
    md.append("")
    md.append("- **Kill signal**: read the paper within 48 hours, run KILL_CRITERIA decision tree.")
    md.append("- **Relevant non-kill**: skim abstract, decide if it changes related-work landscape.")
    md.append("- **No new papers**: keep working.")
    return "\n".join(md) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--bootstrap", action="store_true",
                   help="Mark all current papers as baseline (do not alert).")
    p.add_argument("--dry-run", action="store_true",
                   help="Use cached raw feeds; no network calls.")
    p.add_argument("--max-results", type=int, default=50,
                   help="Max results per query (default 50).")
    p.add_argument("--queries-file", default=str(QUERIES_FILE),
                   help="Path to queries config (default data/scoop_watch_queries.json).")
    p.add_argument("--out", default=str(REPORT_FILE),
                   help="Output report path (default reports/SCOOP_WATCH.md).")
    p.add_argument("--query", default=None,
                   help="Run only one query by id.")
    p.add_argument("--sleep", type=float, default=3.0,
                   help="Seconds between arXiv API calls (default 3.0; arXiv asks for >=3s).")
    args = p.parse_args(argv)

    qfile = Path(args.queries_file)
    if not qfile.exists():
        print(f"Queries file not found: {qfile}", file=sys.stderr)
        return 2

    config = json.loads(qfile.read_text(encoding="utf-8"))
    queries = config.get("queries", [])
    if args.query:
        queries = [q for q in queries if q.get("id") == args.query]
        if not queries:
            print(f"No query with id={args.query}", file=sys.stderr)
            return 2

    state = load_state()
    results: list[dict] = []
    for i, qspec in enumerate(queries):
        if i > 0 and not args.dry_run:
            time.sleep(args.sleep)
        try:
            r = process_query(qspec, state,
                              bootstrap=args.bootstrap,
                              dry_run=args.dry_run,
                              max_results=args.max_results)
        except Exception as e:
            r = {
                "query_id": qspec.get("id", "?"),
                "topic_id": qspec.get("topic_id", ""),
                "title":    qspec.get("title", ""),
                "watch_priority": qspec.get("watch_priority", "MEDIUM"),
                "n_fetched": 0, "n_new": 0, "n_relevant": 0, "n_kill_signal": 0,
                "new_papers": [], "kill_papers": [],
                "error": f"{type(e).__name__}: {e}",
            }
        results.append(r)
        kill_str = f" ⚠️{r['n_kill_signal']} kill" if r['n_kill_signal'] else ""
        err_str = f" ERROR: {r['error']}" if r.get("error") else ""
        print(f"[{r['query_id']}] fetched={r['n_fetched']} new={r['n_new']} "
              f"relevant={r['n_relevant']}{kill_str}{err_str}")

    save_state(state)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(render_report(results), encoding="utf-8")
    print(f"Wrote {args.out}")

    # Exit code: 0 normal, 3 if any kill signal (so cron can alert)
    if any(r["n_kill_signal"] > 0 for r in results):
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
