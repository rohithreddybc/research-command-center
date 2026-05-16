"""
19_title_check.py

Check whether a proposed paper title is already used by other published or
preprinted papers.

Why this exists
---------------
Title clashes (or near-clashes) are a real problem:
  - Reviewers notice and flag as unoriginal
  - Citations to the new paper leak to the old paper and vice versa
  - Google Scholar may merge or de-rank
  - The wider community thinks you don't know the field

Senior reviewers verify titles before locking. This script automates the check
against three free public APIs:
  - Semantic Scholar Graph (paper search by title)
  - arXiv (recent preprints)
  - OpenAlex (broad coverage)

Output
------
For each proposed title:
  - Top 10 most-similar existing papers (with citation counts and similarity scores)
  - Verdict: CLEAR / NEAR-MATCH / LIKELY-TAKEN / SCRAMBLE-NEEDED
  - Suggested rephrasings if collision detected

Usage
-----
  python scripts/19_title_check.py --title "Judging the Judges: A Comprehensive Survey of LLM-as-a-Judge"
  python scripts/19_title_check.py --titles-file data/proposed_titles.txt
  python scripts/19_title_check.py --title "X" --source arxiv --source openalex
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

OUT_DIR = ROOT / "reports"
ATOM_NS = "{http://www.w3.org/2005/Atom}"

S2_API = "https://api.semanticscholar.org/graph/v1/paper/search"
ARXIV_API = "http://export.arxiv.org/api/query"
OPENALEX_API = "https://api.openalex.org/works"

USER_AGENT = ("research-command-center/title-check/1.0 "
              "(mailto:rohithreddybc@gmail.com)")


# ----------------------------------------------------------------------------
# Pure helpers (testable without network)
# ----------------------------------------------------------------------------

STOPWORDS = {
    "a", "an", "the", "of", "for", "on", "in", "and", "or", "to", "with",
    "from", "by", "at", "as", "is", "are", "was", "were", "be",
    "this", "that", "these", "those",
}


def normalize_title(s: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace. Used for similarity."""
    s = (s or "").lower()
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def tokenize(title: str) -> set[str]:
    """Token set with stopwords removed."""
    return {w for w in normalize_title(title).split() if w and w not in STOPWORDS}


def jaccard_similarity(a: str, b: str) -> float:
    """Token-level Jaccard similarity in [0,1]. 0 = disjoint, 1 = identical token sets."""
    ta, tb = tokenize(a), tokenize(b)
    if not ta and not tb:
        return 1.0
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def normalized_overlap(query: str, candidate: str) -> float:
    """How many query tokens appear in candidate, normalised. Useful when
    candidate is much longer than query (e.g., "<our title>: with extra subtitle")."""
    tq = tokenize(query)
    tc = tokenize(candidate)
    if not tq:
        return 0.0
    return len(tq & tc) / len(tq)


def verdict(top_similarity: float, top_overlap: float, n_above_05: int) -> str:
    """Categorise a search result by similarity statistics."""
    if top_similarity >= 0.85:
        return "TAKEN"
    if top_similarity >= 0.70:
        return "LIKELY-TAKEN"
    if top_overlap >= 0.85 and top_similarity >= 0.55:
        return "STRONG-ECHO"          # query is a substring of candidate
    if top_similarity >= 0.55 or n_above_05 >= 3:
        return "NEAR-MATCH"
    if top_similarity >= 0.35 or n_above_05 >= 1:
        return "WEAK-ECHO"
    return "CLEAR"


def suggest_rephrasings(title: str, conflicts: list[dict]) -> list[str]:
    """Generate basic rephrasing suggestions when collisions found."""
    out: list[str] = []
    base = title.rstrip(".").rstrip()
    # If there's a colon, split title:subtitle
    if ":" in title:
        head, _, tail = title.partition(":")
        head = head.strip()
        tail = tail.strip()
        out.append(f"Rethinking {head}: {tail}")
        out.append(f"{head} Revisited: {tail}")
        out.append(f"{head}, Year {_dt.date.today().year}: {tail}")
    out.append(f"Beyond {base}: ...")
    out.append(f"Towards {base}: ...")
    out.append(f"A New Look at {base}: ...")
    if "Survey" in title or "survey" in title:
        out.append(title.replace("Survey", "Systematic Review"))
        out.append(title.replace("Survey", "Comprehensive Analysis"))
        out.append(title.replace("Survey", "Taxonomy"))
    return out[:5]


# ----------------------------------------------------------------------------
# API search adapters
# ----------------------------------------------------------------------------

def search_semantic_scholar(title: str, limit: int = 20, timeout: float = 20.0) -> list[dict]:
    """Search Semantic Scholar by title. Returns list of paper dicts.

    Each dict: {title, year, venue, authors, citations, url, source: 's2'}
    """
    params = {
        "query":   title,
        "limit":   str(min(limit, 100)),
        "fields":  "title,year,venue,authors.name,citationCount,externalIds,openAccessPdf,url",
    }
    url = f"{S2_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    out: list[dict] = []
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read())
    except Exception as e:
        return [{"_error": f"semantic-scholar: {e}"}]
    for p in data.get("data", []):
        author_names = [a.get("name", "") for a in (p.get("authors") or [])][:5]
        out.append({
            "title":      (p.get("title") or "").strip(),
            "year":       p.get("year"),
            "venue":      p.get("venue") or "",
            "authors":    "; ".join(author_names),
            "citations":  p.get("citationCount") or 0,
            "url":        p.get("url") or "",
            "source":     "s2",
        })
    return out


def search_arxiv(title: str, limit: int = 20, timeout: float = 20.0) -> list[dict]:
    """Search arXiv by title (uses ti: prefix). Returns list of paper dicts."""
    q = f'ti:"{title}"'
    params = {
        "search_query": q,
        "start":        "0",
        "max_results":  str(min(limit, 100)),
        "sortBy":       "relevance",
        "sortOrder":    "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    out: list[dict] = []
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            xml_text = r.read().decode("utf-8", errors="replace")
    except Exception as e:
        return [{"_error": f"arxiv: {e}"}]
    try:
        root = ET.fromstring(xml_text)
    except Exception as e:
        return [{"_error": f"arxiv-parse: {e}"}]
    for entry in root.findall(f"{ATOM_NS}entry"):
        t = " ".join((entry.findtext(f"{ATOM_NS}title") or "").split())
        published = (entry.findtext(f"{ATOM_NS}published") or "").strip()
        year = published[:4] if published else None
        authors = []
        for a in entry.findall(f"{ATOM_NS}author"):
            name = (a.findtext(f"{ATOM_NS}name") or "").strip()
            if name:
                authors.append(name)
        link = ""
        for ln in entry.findall(f"{ATOM_NS}link"):
            if ln.attrib.get("rel") == "alternate":
                link = ln.attrib.get("href", "")
                break
        out.append({
            "title":     t,
            "year":      year,
            "venue":     "arXiv",
            "authors":   "; ".join(authors[:5]),
            "citations": None,         # arXiv API doesn't expose citation counts
            "url":       link,
            "source":    "arxiv",
        })
    return out


def search_openalex(title: str, limit: int = 20, timeout: float = 20.0) -> list[dict]:
    """Search OpenAlex by title. Returns list of paper dicts."""
    params = {
        "search":    title,
        "per-page":  str(min(limit, 50)),
    }
    url = f"{OPENALEX_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    out: list[dict] = []
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read())
    except Exception as e:
        return [{"_error": f"openalex: {e}"}]
    for w in data.get("results", []):
        primary_loc = w.get("primary_location") or {}
        loc_source = primary_loc.get("source") or {}
        venue = (
            (w.get("host_venue") or {}).get("display_name")
            or loc_source.get("display_name")
            or ""
        )
        author_names = [
            (au.get("author") or {}).get("display_name", "")
            for au in (w.get("authorships") or [])
        ][:5]
        out.append({
            "title":     (w.get("display_name") or w.get("title") or "").strip(),
            "year":      w.get("publication_year"),
            "venue":     venue,
            "authors":   "; ".join(author_names),
            "citations": w.get("cited_by_count"),
            "url":       w.get("doi") or w.get("id") or "",
            "source":    "openalex",
        })
    return out


SOURCE_FNS = {
    "s2":       search_semantic_scholar,
    "arxiv":    search_arxiv,
    "openalex": search_openalex,
}


# ----------------------------------------------------------------------------
# Aggregation + scoring
# ----------------------------------------------------------------------------

def score_results(query_title: str, results: list[dict]) -> list[dict]:
    """Annotate each result with similarity + overlap; sort descending."""
    out: list[dict] = []
    seen_titles: set[str] = set()
    for r in results:
        if r.get("_error"):
            out.append(r)
            continue
        t = r.get("title", "")
        if not t:
            continue
        norm = normalize_title(t)
        if norm in seen_titles:
            continue   # de-duplicate across sources
        seen_titles.add(norm)
        sim     = jaccard_similarity(query_title, t)
        overlap = normalized_overlap(query_title, t)
        out.append({**r,
                    "similarity":         round(sim, 3),
                    "normalized_overlap": round(overlap, 3)})
    out.sort(key=lambda r: (
        -(r.get("similarity") or 0),
        -(r.get("normalized_overlap") or 0),
        -(r.get("citations") or 0),
    ))
    return out


def check_title(title: str, sources: list[str], limit: int = 20,
                sleep: float = 1.0) -> dict:
    """End-to-end check: query each source, aggregate, classify."""
    all_results: list[dict] = []
    errors: list[str] = []
    for i, src in enumerate(sources):
        if i > 0:
            time.sleep(sleep)
        fn = SOURCE_FNS.get(src)
        if not fn:
            errors.append(f"unknown source: {src}")
            continue
        rs = fn(title, limit=limit)
        for r in rs:
            if r.get("_error"):
                errors.append(r["_error"])
        all_results.extend(rs)
    scored = score_results(title, [r for r in all_results if not r.get("_error")])
    top10 = scored[:10]
    top_sim = top10[0]["similarity"] if top10 else 0.0
    top_overlap = top10[0]["normalized_overlap"] if top10 else 0.0
    n_above_05 = sum(1 for r in top10 if r.get("similarity", 0) >= 0.5)
    v = verdict(top_sim, top_overlap, n_above_05)
    return {
        "query":       title,
        "verdict":     v,
        "top_similarity":         top_sim,
        "top_normalized_overlap": top_overlap,
        "n_above_05":  n_above_05,
        "n_results":   len(scored),
        "top10":       top10,
        "errors":      errors,
        "rephrasings": suggest_rephrasings(title, top10) if v != "CLEAR" else [],
        "checked_at":  _dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }


# ----------------------------------------------------------------------------
# Report rendering
# ----------------------------------------------------------------------------

def render_report(checks: list[dict]) -> str:
    md: list[str] = ["# Title Check Report", ""]
    md.append(f"*Generated: {_dt.datetime.utcnow().isoformat(timespec='seconds')}Z*")
    md.append(f"*Source: `scripts/19_title_check.py`*")
    md.append("")
    md.append("## Summary")
    md.append("")
    md.append("| Title | Verdict | Top sim | Hits ≥0.5 |")
    md.append("|---|---|---|---|")
    for c in checks:
        md.append(f"| {c['query'][:70]} | **{c['verdict']}** | {c['top_similarity']} | {c['n_above_05']} |")
    md.append("")
    md.append("**Verdict scale**: CLEAR < WEAK-ECHO < NEAR-MATCH < STRONG-ECHO < LIKELY-TAKEN < TAKEN")
    md.append("")
    for c in checks:
        md.append(f"## {c['query']}")
        md.append("")
        md.append(f"- Verdict: **{c['verdict']}**")
        md.append(f"- Top similarity: {c['top_similarity']} (overlap {c['top_normalized_overlap']})")
        md.append(f"- Results ≥ 0.5 similarity: {c['n_above_05']} / {c['n_results']}")
        if c["errors"]:
            md.append(f"- Errors: {'; '.join(c['errors'])}")
        md.append("")
        md.append("### Top 10 closest existing titles")
        md.append("")
        md.append("| Sim | Overlap | Year | Cit | Source | Title | Venue |")
        md.append("|---|---|---|---|---|---|---|")
        for r in c["top10"]:
            md.append(f"| {r.get('similarity', '-')} | {r.get('normalized_overlap', '-')} | "
                      f"{r.get('year', '-')} | {r.get('citations', '-')} | {r.get('source', '-')} | "
                      f"{(r.get('title') or '')[:80]} | {(r.get('venue') or '')[:50]} |")
        md.append("")
        if c["rephrasings"]:
            md.append("### Suggested rephrasings")
            md.append("")
            for s in c["rephrasings"]:
                md.append(f"- {s}")
            md.append("")
    return "\n".join(md) + "\n"


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--title", help="A single title to check")
    g.add_argument("--titles-file", help="Newline-separated file of titles")
    p.add_argument("--source", action="append", default=None,
                   choices=list(SOURCE_FNS.keys()),
                   help="Repeat to use multiple. Default: s2 + arxiv + openalex")
    p.add_argument("--limit", type=int, default=20,
                   help="Max results per source (default 20)")
    p.add_argument("--out", default=str(OUT_DIR / "TITLE_CHECK.md"),
                   help="Output report path")
    p.add_argument("--sleep", type=float, default=1.0,
                   help="Seconds between API calls per source (default 1.0)")
    args = p.parse_args(argv)

    sources = args.source or list(SOURCE_FNS.keys())

    titles: list[str] = []
    if args.title:
        titles = [args.title]
    elif args.titles_file:
        with open(args.titles_file, encoding="utf-8") as f:
            titles = [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]

    checks: list[dict] = []
    for i, t in enumerate(titles):
        if i > 0:
            time.sleep(args.sleep)
        print(f"[{i+1}/{len(titles)}] {t[:70]}")
        c = check_title(t, sources, limit=args.limit, sleep=args.sleep)
        checks.append(c)
        print(f"  -> {c['verdict']} (top sim {c['top_similarity']}, "
              f"n>=0.5: {c['n_above_05']})")

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render_report(checks), encoding="utf-8")
    print(f"Wrote {out_path}")

    # Exit code: 0 if all CLEAR/WEAK-ECHO; 2 if any NEAR-MATCH or worse
    if any(c["verdict"] in ("NEAR-MATCH", "STRONG-ECHO", "LIKELY-TAKEN", "TAKEN") for c in checks):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
