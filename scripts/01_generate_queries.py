"""
01_generate_queries.py

Reads data/topics_seed.csv and generates per-topic, per-source queries
including synonym expansion. Writes data/queries/<topic_id>.json.

Each topic_id gets a queries dict with these keys:
- semantic_scholar: list of query strings
- openalex:        list of query strings
- crossref:        list of query strings
- arxiv:           list of query strings (arXiv API search format)
- github:          list of query strings
- huggingface:     list of query strings
- doaj:            list of query strings
- pwc:             list of query strings
- google_scholar_manual: list of (manual fallback) URLs
"""
from __future__ import annotations
import argparse
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.io_utils import read_csv, write_json, log  # noqa: E402

QUERIES_DIR = ROOT / "data" / "queries"

# Cross-cutting axes that often differentiate or bound research topics
AXIS_TERMS = [
    "benchmark", "dataset", "evaluation", "reproducibility",
    "survey", "taxonomy", "robustness", "calibration",
    "limitations", "future work",
]


def _expand(keywords: str, synonyms: str) -> list[str]:
    base = [k.strip() for k in keywords.split("|") if k.strip()]
    syn = [s.strip() for s in synonyms.split(";") if s.strip()]
    return base + syn


def _arxiv_query(terms: list[str], categories: list[str]) -> str:
    cat = "+OR+".join(f"cat:{c}" for c in categories)
    quoted = [urllib.parse.quote('"' + t + '"') for t in terms[:3]]
    body = "+AND+".join(f"all:{q}" for q in quoted)
    return f"({cat})+AND+({body})"


def build_queries(topic: dict[str, str]) -> dict[str, list[str] | list[dict[str, str]]]:
    keys = _expand(topic["keywords"], topic.get("synonyms", ""))
    cat = topic.get("category", "").lower()
    is_health = ("health" in cat) or ("clinical" in cat) or ("medical" in (topic["keywords"] + topic.get("synonyms", "")).lower())
    is_nlp = any(w in cat for w in ["nlp", "eval", "prompt", "llm", "rag"]) or True  # default-include NLP for LLM topics

    arxiv_cats = []
    if is_nlp:
        arxiv_cats += ["cs.CL", "cs.LG"]
    if is_health:
        arxiv_cats += ["cs.AI"]
    arxiv_cats = arxiv_cats or ["cs.CL", "cs.LG"]

    # Generate primary phrase queries; pair top-3 keywords with axis terms
    primary = [keys[0]] if keys else []
    paired = []
    for k in keys[:3]:
        for axis in ["benchmark", "evaluation", "robustness", "reproducibility"]:
            paired.append(f"{k} {axis}")

    s2_queries = list(dict.fromkeys(primary + keys[:5] + paired[:6]))
    oa_queries = list(dict.fromkeys(primary + keys[:5] + paired[:6]))
    crossref_queries = list(dict.fromkeys(primary + keys[:4]))

    arxiv_queries = [_arxiv_query(keys[:3], arxiv_cats)]
    # Backup arxiv query: simple keyword
    if keys:
        arxiv_queries.append("all:" + urllib.parse.quote(keys[0]))

    github_queries = []
    for k in keys[:3]:
        github_queries.append(f"{k} in:readme,description")
        github_queries.append(f"{k} benchmark in:name,description")
        github_queries.append(f"{k} evaluation in:name,description")

    hf_queries = list(dict.fromkeys(keys[:5] + [f"{k} benchmark" for k in keys[:2]]))
    doaj_queries = list(dict.fromkeys(keys[:3]))
    pwc_queries = list(dict.fromkeys(keys[:3]))

    gs_manual = [
        {"label": k, "url": "https://scholar.google.com/scholar?q="
            + urllib.parse.quote(f'"{k}" 2024..2026')}
        for k in keys[:5]
    ]

    return {
        "semantic_scholar": s2_queries,
        "openalex": oa_queries,
        "crossref": crossref_queries,
        "arxiv": arxiv_queries,
        "github": github_queries,
        "huggingface": hf_queries,
        "doaj": doaj_queries,
        "pwc": pwc_queries,
        "google_scholar_manual": gs_manual,
        "axis_terms": AXIS_TERMS,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--seed", default=str(ROOT / "data" / "topics_seed.csv"))
    p.add_argument("--out", default=str(QUERIES_DIR))
    args = p.parse_args(argv)

    topics = read_csv(Path(args.seed))
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for t in topics:
        q = build_queries(t)
        write_json(out / f"{t['topic_id']}.json", {"topic": t, "queries": q})
        log("01_queries", f"{t['topic_id']} queries written")
    print(f"Generated queries for {len(topics)} topics -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
