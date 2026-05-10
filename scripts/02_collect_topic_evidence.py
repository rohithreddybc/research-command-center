"""
02_collect_topic_evidence.py

Pull primary literature evidence per topic from:
- Semantic Scholar Graph API
- OpenAlex
- Crossref
- arXiv API (Atom XML)

Writes data/evidence/<topic_id>/{semantic_scholar,openalex,crossref,arxiv}.json
And a deduplicated paper list at data/papers_dedup/<topic_id>.csv
"""
from __future__ import annotations
import argparse
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.http import get_json, get  # noqa: E402
from common.io_utils import read_json, write_json, write_csv, log, evidence_dir  # noqa: E402
from common.relevance import filter_by_relevance  # noqa: E402

QUERIES_DIR = ROOT / "data" / "queries"
DEDUP_DIR = ROOT / "data" / "papers_dedup"

S2_BASE = "https://api.semanticscholar.org/graph/v1/paper/search"
OPENALEX_BASE = "https://api.openalex.org/works"
CROSSREF_BASE = "https://api.crossref.org/works"
ARXIV_BASE = "http://export.arxiv.org/api/query"


def _norm_title(t: str) -> str:
    t = re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()
    return re.sub(r"\s+", " ", t)


def fetch_semantic_scholar(query: str, year_range: str = "2022-2026", limit: int = 50) -> dict[str, Any]:
    params = {
        "query": query,
        "limit": limit,
        "year": year_range,
        "fields": "paperId,title,year,venue,authors.name,citationCount,influentialCitationCount,abstract,externalIds",
    }
    status, body = get_json(S2_BASE, params, min_interval=1.2)
    if not body or "data" not in body:
        return {"query": query, "results": [], "status": status, "error": str(body)[:200] if status >= 400 else None}
    return {"query": query, "results": body.get("data", []), "status": status}


def fetch_openalex(query: str, year_range: str = "2022-2026", limit: int = 50) -> dict[str, Any]:
    yfrom, yto = year_range.split("-")
    params = {
        "search": query,
        "per-page": limit,
        "filter": f"from_publication_date:{yfrom}-01-01,to_publication_date:{yto}-12-31",
        "select": "id,title,publication_year,host_venue,authorships,cited_by_count,abstract_inverted_index,doi",
    }
    status, body = get_json(OPENALEX_BASE, params, min_interval=0.5)
    if not body:
        return {"query": query, "results": [], "status": status}
    return {"query": query, "results": body.get("results", []), "status": status}


def fetch_crossref(query: str, year_range: str = "2022-2026", limit: int = 50) -> dict[str, Any]:
    yfrom, yto = year_range.split("-")
    params = {
        "query": query,
        "rows": limit,
        "filter": f"from-pub-date:{yfrom}-01-01,until-pub-date:{yto}-12-31",
        "select": "DOI,title,issued,container-title,is-referenced-by-count,author,subject,abstract",
    }
    status, body = get_json(CROSSREF_BASE, params, min_interval=0.4)
    if not body or "message" not in body:
        return {"query": query, "results": [], "status": status}
    return {"query": query, "results": body.get("message", {}).get("items", []), "status": status}


def fetch_arxiv(search_query: str, max_results: int = 50) -> dict[str, Any]:
    params = {"search_query": search_query, "start": 0, "max_results": max_results, "sortBy": "submittedDate", "sortOrder": "descending"}
    status, body = get(ARXIV_BASE, params, min_interval=3.0)
    if status >= 400 or not body:
        return {"query": search_query, "results": [], "status": status}
    try:
        ns = {"a": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
        root = ET.fromstring(body)
        out = []
        for entry in root.findall("a:entry", ns):
            title = (entry.findtext("a:title", default="", namespaces=ns) or "").strip()
            published = (entry.findtext("a:published", default="", namespaces=ns) or "").strip()
            summary = (entry.findtext("a:summary", default="", namespaces=ns) or "").strip()
            id_ = (entry.findtext("a:id", default="", namespaces=ns) or "").strip()
            authors = [a.findtext("a:name", default="", namespaces=ns) or ""
                       for a in entry.findall("a:author", ns)]
            cats = [c.attrib.get("term", "") for c in entry.findall("a:category", ns)]
            out.append({
                "id": id_, "title": title, "published": published,
                "summary": summary, "authors": authors, "categories": cats,
            })
        return {"query": search_query, "results": out, "status": status}
    except Exception as e:
        return {"query": search_query, "results": [], "status": status, "error": str(e)}


def _s2_to_paper(p: dict[str, Any]) -> dict[str, Any]:
    return {
        "source": "semantic_scholar",
        "id": p.get("paperId") or (p.get("externalIds") or {}).get("DOI"),
        "doi": (p.get("externalIds") or {}).get("DOI"),
        "title": p.get("title", ""),
        "year": p.get("year"),
        "venue": p.get("venue") or "",
        "citations": p.get("citationCount") or 0,
        "influential_citations": p.get("influentialCitationCount") or 0,
        "authors": [a.get("name", "") for a in (p.get("authors") or [])],
        "abstract": p.get("abstract") or "",
    }


def _oa_to_paper(p: dict[str, Any]) -> dict[str, Any]:
    venue = ""
    hv = p.get("host_venue") or {}
    if isinstance(hv, dict):
        venue = hv.get("display_name") or hv.get("publisher") or ""
    abstract = ""
    inv = p.get("abstract_inverted_index")
    if isinstance(inv, dict):
        # invert
        positions: list[tuple[int, str]] = []
        for word, idxs in inv.items():
            for i in idxs:
                positions.append((i, word))
        abstract = " ".join(w for _, w in sorted(positions))
    return {
        "source": "openalex",
        "id": p.get("id"),
        "doi": p.get("doi"),
        "title": p.get("title") or "",
        "year": p.get("publication_year"),
        "venue": venue,
        "citations": p.get("cited_by_count") or 0,
        "influential_citations": 0,
        "authors": [a.get("author", {}).get("display_name", "") for a in (p.get("authorships") or [])],
        "abstract": abstract,
    }


def _cr_to_paper(p: dict[str, Any]) -> dict[str, Any]:
    issued = p.get("issued", {}).get("date-parts", [[None]])
    year = None
    if isinstance(issued, list) and issued and isinstance(issued[0], list) and issued[0]:
        year = issued[0][0]
    return {
        "source": "crossref",
        "id": p.get("DOI"),
        "doi": p.get("DOI"),
        "title": (p.get("title") or [""])[0] if isinstance(p.get("title"), list) else (p.get("title") or ""),
        "year": year,
        "venue": (p.get("container-title") or [""])[0] if isinstance(p.get("container-title"), list) else "",
        "citations": p.get("is-referenced-by-count") or 0,
        "influential_citations": 0,
        "authors": [f"{a.get('given','')} {a.get('family','')}".strip() for a in (p.get("author") or [])],
        "abstract": p.get("abstract") or "",
    }


def _arxiv_to_paper(p: dict[str, Any]) -> dict[str, Any]:
    year = None
    if p.get("published"):
        try:
            year = int(p["published"][:4])
        except Exception:
            pass
    return {
        "source": "arxiv",
        "id": p.get("id"),
        "doi": "",
        "title": p.get("title", ""),
        "year": year,
        "venue": "arXiv",
        "citations": 0,
        "influential_citations": 0,
        "authors": p.get("authors", []),
        "abstract": p.get("summary", ""),
    }


def deduplicate(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Dedupe by DOI when present; merge with title-match when DOI absent or unmatched."""
    by_doi: dict[str, dict[str, Any]] = {}
    by_title: dict[str, dict[str, Any]] = {}

    def _merge(target: dict[str, Any], p: dict[str, Any]) -> None:
        target["sources"] = list(set((target.get("sources") or []) + [p.get("source")]))
        target["citations"] = max(target.get("citations") or 0, p.get("citations") or 0)
        target["influential_citations"] = max(
            target.get("influential_citations") or 0,
            p.get("influential_citations") or 0,
        )
        if len(p.get("abstract") or "") > len(target.get("abstract") or ""):
            target["abstract"] = p["abstract"]
        if not target.get("doi") and p.get("doi"):
            target["doi"] = p["doi"]

    for p in papers:
        doi = (p.get("doi") or "").lower().strip()
        title_key = _norm_title(p.get("title", ""))
        if not doi and not title_key:
            continue
        if doi and doi in by_doi:
            _merge(by_doi[doi], p)
            if title_key:
                by_title[title_key] = by_doi[doi]
            continue
        if title_key and title_key in by_title:
            existing = by_title[title_key]
            _merge(existing, p)
            if doi:
                by_doi[doi] = existing
            continue
        new = dict(p)
        new["sources"] = [p.get("source")]
        if doi:
            by_doi[doi] = new
        if title_key:
            by_title[title_key] = new
    seen_ids: set[int] = set()
    out: list[dict[str, Any]] = []
    for d in list(by_doi.values()) + list(by_title.values()):
        if id(d) in seen_ids:
            continue
        seen_ids.add(id(d))
        out.append(d)
    return out


def _doi_url(doi: str | None) -> str:
    if not doi:
        return ""
    return f"https://doi.org/{doi.strip().lstrip('https://doi.org/').lstrip('http://doi.org/')}"


def _abstract_snippet(s: str | None, n: int = 240) -> str:
    if not s:
        return ""
    s = re.sub(r"\s+", " ", s).strip()
    return (s[:n] + "...") if len(s) > n else s


def collect_for_topic(topic_id: str, topic_meta: dict[str, Any], queries: dict[str, Any],
                      year_range: str = "2022-2026", limit_per_query: int = 25) -> dict[str, Any]:
    edir = evidence_dir(topic_id)

    s2_all: list[dict[str, Any]] = []
    for q in (queries.get("semantic_scholar") or [])[:6]:
        r = fetch_semantic_scholar(q, year_range, limit_per_query)
        s2_all.append(r)
    write_json(edir / "semantic_scholar.json", s2_all)

    oa_all: list[dict[str, Any]] = []
    for q in (queries.get("openalex") or [])[:5]:
        r = fetch_openalex(q, year_range, limit_per_query)
        oa_all.append(r)
    write_json(edir / "openalex.json", oa_all)

    cr_all: list[dict[str, Any]] = []
    for q in (queries.get("crossref") or [])[:4]:
        r = fetch_crossref(q, year_range, limit_per_query)
        cr_all.append(r)
    write_json(edir / "crossref.json", cr_all)

    ax_all: list[dict[str, Any]] = []
    for q in (queries.get("arxiv") or [])[:2]:
        r = fetch_arxiv(q, max_results=limit_per_query)
        ax_all.append(r)
    write_json(edir / "arxiv.json", ax_all)

    # build deduped list
    papers: list[dict[str, Any]] = []
    for r in s2_all:
        for p in r.get("results", []) or []:
            papers.append(_s2_to_paper(p))
    for r in oa_all:
        for p in r.get("results", []) or []:
            papers.append(_oa_to_paper(p))
    for r in cr_all:
        for p in r.get("results", []) or []:
            papers.append(_cr_to_paper(p))
    for r in ax_all:
        for p in r.get("results", []) or []:
            papers.append(_arxiv_to_paper(p))

    dedup = deduplicate(papers)
    # Relevance filter against the topic
    filtered = filter_by_relevance(dedup, topic_meta)
    DEDUP_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(
        DEDUP_DIR / f"{topic_id}.csv",
        [{
            "title": p.get("title", "")[:300],
            "abstract_snippet": _abstract_snippet(p.get("abstract"), 240),
            "year": p.get("year") or "",
            "venue": p.get("venue", "")[:200],
            "citations": p.get("citations", 0),
            "influential_citations": p.get("influential_citations", 0),
            "doi": p.get("doi") or "",
            "url": _doi_url(p.get("doi")) or (p.get("id") if isinstance(p.get("id"), str) and p.get("id", "").startswith("http") else ""),
            "sources": "|".join(p.get("sources", [p.get("source", "")])),
            "authors": "|".join(p.get("authors", []) or [])[:300],
            "relevance_score": p.get("relevance_score", 0),
            "matched_keywords": p.get("matched_keywords", ""),
            "reason_included": p.get("reason_included", ""),
        } for p in filtered],
        header=["title", "abstract_snippet", "year", "venue", "citations", "influential_citations",
                "doi", "url", "sources", "authors",
                "relevance_score", "matched_keywords", "reason_included"],
    )
    log("02_evidence", f"{topic_id}: deduped {len(dedup)} from {len(papers)} raw; kept {len(filtered)} after relevance filter")
    return {"topic_id": topic_id, "raw": len(papers), "deduped": len(dedup), "kept": len(filtered)}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--year-range", default="2022-2026")
    p.add_argument("--limit-per-query", type=int, default=25)
    p.add_argument("--topic", default=None, help="Run a single topic id")
    args = p.parse_args(argv)

    files = sorted(QUERIES_DIR.glob("*.json"))
    if args.topic:
        files = [f for f in files if f.stem == args.topic]
    if not files:
        print("No queries found. Run scripts/01_generate_queries.py first.")
        return 1
    summary = []
    for f in files:
        q = read_json(f)
        if not q:
            continue
        topic_id = q["topic"]["topic_id"]
        s = collect_for_topic(topic_id, q["topic"], q["queries"], args.year_range, args.limit_per_query)
        summary.append(s)
    print({"summary": summary})
    return 0


if __name__ == "__main__":
    sys.exit(main())
