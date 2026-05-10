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

# Cross-cutting axes that often differentiate or bound research topics.
# Kept as documentation only — the generator no longer injects every axis term
# into every query. Use _conditional_axis_terms() to derive a topic-appropriate
# subset based on target_artifact.
AXIS_TERMS = [
    "benchmark", "dataset", "evaluation", "reproducibility",
    "survey", "taxonomy", "robustness", "calibration",
    "limitations", "future work",
]


def _conditional_axis_terms(target_artifact: str) -> list[str]:
    """Pick axis-term injection set based on the topic's stated artifact target.

    A pure 'paper' or empty target gets NO injection. This prevents the
    pipeline from forcing benchmark/eval framing on topics that aren't
    benchmarks. See reports/BIAS_AUDIT_REPORT.md §D for the rationale.
    """
    t = (target_artifact or "").lower()
    if not t or t == "paper":
        return []
    if "benchmark" in t:
        return ["benchmark", "evaluation"]
    if "dataset" in t:
        return ["dataset", "evaluation"]
    if "tool" in t or "software" in t or "framework" in t:
        return ["framework", "implementation"]
    if "survey" in t or "review" in t or "taxonomy" in t:
        return ["survey", "taxonomy"]
    if "audit" in t or "reproducibility" in t or "database" in t:
        return ["reproducibility", "audit"]
    return []  # default: no injection


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

    # Generate primary phrase queries.
    # Axis-term pairing is now CONDITIONAL on target_artifact — see
    # _conditional_axis_terms(). For target_artifact='paper' or empty, no axis
    # terms are injected, so the search isn't pushed toward benchmark/eval
    # framings.
    target_artifact = topic.get("target_artifact", "")
    axis_terms_to_inject = _conditional_axis_terms(target_artifact)

    primary = [keys[0]] if keys else []
    paired: list[str] = []
    for k in keys[:3]:
        for axis in axis_terms_to_inject:
            paired.append(f"{k} {axis}")

    s2_queries = list(dict.fromkeys(primary + keys[:5] + paired[:6]))
    oa_queries = list(dict.fromkeys(primary + keys[:5] + paired[:6]))
    crossref_queries = list(dict.fromkeys(primary + keys[:4]))

    arxiv_queries = [_arxiv_query(keys[:3], arxiv_cats)]
    # Backup arxiv query: simple keyword
    if keys:
        arxiv_queries.append("all:" + urllib.parse.quote(keys[0]))

    github_queries: list[str] = []
    for k in keys[:3]:
        github_queries.append(f"{k} in:readme,description")
        # Only append axis-specific GitHub queries if the topic's target
        # artifact justifies them.
        for axis in axis_terms_to_inject[:2]:
            github_queries.append(f"{k} {axis} in:name,description")

    hf_queries_extra = []
    if "benchmark" in axis_terms_to_inject or "dataset" in axis_terms_to_inject:
        hf_queries_extra = [f"{k} benchmark" for k in keys[:2]]
    hf_queries = list(dict.fromkeys(keys[:5] + hf_queries_extra))
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
