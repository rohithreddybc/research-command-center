"""
03_collect_extra_evidence.py

Pulls auxiliary evidence per topic from:
- GitHub Search API (repos)
- Hugging Face datasets API
- Papers With Code (datasets, methods, papers)
- DOAJ (open-access journal index)

Writes to data/evidence/<topic_id>/{github,huggingface,paperswithcode,doaj}.json
"""
from __future__ import annotations
import argparse
import os
import sys
import urllib.parse
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.http import get_json  # noqa: E402
from common.io_utils import read_json, write_json, log, evidence_dir  # noqa: E402

QUERIES_DIR = ROOT / "data" / "queries"

GITHUB_SEARCH = "https://api.github.com/search/repositories"
HF_DATASETS = "https://huggingface.co/api/datasets"
PWC_PAPERS = "https://paperswithcode.com/api/v1/papers/"
PWC_DATASETS = "https://paperswithcode.com/api/v1/datasets/"
DOAJ_API = "https://doaj.org/api/search/journals"


def fetch_github(query: str, max_results: int = 20) -> dict[str, Any]:
    headers: dict[str, str] = {"Accept": "application/vnd.github+json"}
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        headers["Authorization"] = f"Bearer {tok}"
    params = {"q": query, "sort": "stars", "order": "desc", "per_page": max_results}
    status, body = get_json(GITHUB_SEARCH, params, headers, min_interval=2.5)
    if not body:
        return {"query": query, "results": [], "status": status}
    items = body.get("items") or []
    out = [{
        "name": i.get("full_name"),
        "stars": i.get("stargazers_count", 0),
        "forks": i.get("forks_count", 0),
        "description": i.get("description") or "",
        "url": i.get("html_url"),
        "topics": i.get("topics") or [],
        "pushed_at": i.get("pushed_at"),
        "updated_at": i.get("updated_at"),
    } for i in items[:max_results]]
    return {"query": query, "results": out, "status": status, "total": body.get("total_count", 0)}


def fetch_huggingface(query: str, max_results: int = 25) -> dict[str, Any]:
    params = {"search": query, "limit": max_results, "full": "true"}
    status, body = get_json(HF_DATASETS, params, min_interval=1.5)
    if not body:
        return {"query": query, "results": [], "status": status}
    out = [{
        "id": d.get("id"),
        "downloads": d.get("downloads", 0),
        "likes": d.get("likes", 0),
        "tags": d.get("tags") or [],
        "description": (d.get("description") or "")[:500],
    } for d in (body if isinstance(body, list) else [])][:max_results]
    return {"query": query, "results": out, "status": status}


def fetch_pwc(query: str, max_results: int = 20) -> dict[str, Any]:
    params_p = {"q": query, "items_per_page": max_results}
    sp, papers = get_json(PWC_PAPERS, params_p, min_interval=1.5)
    sd, datasets = get_json(PWC_DATASETS, {"q": query, "items_per_page": max_results}, min_interval=1.5)

    out_papers = []
    if isinstance(papers, dict):
        for p in (papers.get("results") or [])[:max_results]:
            out_papers.append({
                "id": p.get("id"),
                "title": p.get("title"),
                "abstract": (p.get("abstract") or "")[:600],
                "published": p.get("published"),
                "url_pdf": p.get("url_pdf"),
                "url_abs": p.get("url_abs"),
            })

    out_ds = []
    if isinstance(datasets, dict):
        for d in (datasets.get("results") or [])[:max_results]:
            out_ds.append({
                "id": d.get("id"),
                "name": d.get("name"),
                "description": (d.get("description") or "")[:500],
                "introduced_date": d.get("introduced_date"),
                "url": d.get("url"),
                "tasks": d.get("tasks") or [],
            })

    return {"query": query, "papers": out_papers, "datasets": out_ds, "status_p": sp, "status_d": sd}


def fetch_doaj(query: str, max_results: int = 25) -> dict[str, Any]:
    """DOAJ: free open access journals (no APC for many)."""
    q = urllib.parse.quote(query)
    url = f"{DOAJ_API}/{q}"
    params = {"pageSize": max_results}
    status, body = get_json(url, params, min_interval=1.5)
    if not body or "results" not in body:
        return {"query": query, "results": [], "status": status}
    out = []
    for r in (body.get("results") or [])[:max_results]:
        b = r.get("bibjson") or {}
        apc_charges = b.get("apc", {}).get("max", []) or []
        no_apc = b.get("apc", {}).get("has_apc") is False
        out.append({
            "title": b.get("title"),
            "issn": [i.get("id") for i in (b.get("identifier") or []) if i.get("type") in ("eissn", "pissn")],
            "publisher": b.get("publisher", {}).get("name"),
            "subject": [s.get("term") for s in (b.get("subject") or [])],
            "no_apc": no_apc,
            "apc_charges": apc_charges,
            "license": [l.get("type") for l in (b.get("license") or [])],
            "url": b.get("ref", {}).get("journal"),
            "country": b.get("publisher", {}).get("country"),
        })
    return {"query": query, "results": out, "status": status}


def collect_for_topic(topic_id: str, queries: dict[str, Any]) -> dict[str, Any]:
    edir = evidence_dir(topic_id)

    gh = []
    for q in (queries.get("github") or [])[:3]:
        gh.append(fetch_github(q, max_results=15))
    write_json(edir / "github.json", gh)

    hf = []
    for q in (queries.get("huggingface") or [])[:3]:
        hf.append(fetch_huggingface(q, max_results=20))
    write_json(edir / "huggingface.json", hf)

    pwc = []
    for q in (queries.get("pwc") or [])[:2]:
        pwc.append(fetch_pwc(q, max_results=15))
    write_json(edir / "paperswithcode.json", pwc)

    doaj = []
    for q in (queries.get("doaj") or [])[:3]:
        doaj.append(fetch_doaj(q, max_results=15))
    write_json(edir / "doaj.json", doaj)

    counts = {
        "github": sum(len(g.get("results", [])) for g in gh),
        "huggingface": sum(len(h.get("results", [])) for h in hf),
        "paperswithcode_papers": sum(len(p.get("papers", [])) for p in pwc),
        "paperswithcode_datasets": sum(len(p.get("datasets", [])) for p in pwc),
        "doaj": sum(len(d.get("results", [])) for d in doaj),
    }
    log("03_extra", f"{topic_id}: counts={counts}")
    return {"topic_id": topic_id, "counts": counts}


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
