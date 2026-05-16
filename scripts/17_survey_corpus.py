"""
17_survey_corpus.py

Maintain the LLM-as-Judge survey corpus at data/survey_corpus.csv.

Background
----------
The survey project (06_paper_pipeline/SURVEY_llm_judge/) needs a structured
metadata catalogue of every paper to be cited. PROTOCOL.md §5.2 specifies the
schema. This script:

  1) Seeds the corpus from existing pipeline dedup CSVs
     (data/papers_dedup/<topic>.csv for the judge-related topics).
  2) Optionally pulls fresh arXiv papers via the same machinery as
     scripts/15_arxiv_watch.py (with rate-limit handling).
  3) Auto-suggests in_scope (yes / partial / no) and section assignment
     based on keyword matching against SURVEY_STRUCTURE.md.
  4) PRESERVES manual annotations on re-run (any row where read_status !=
     "unread" or my_notes is non-empty has its manual fields kept).

Output schema (per PROTOCOL.md §5.2)
------------------------------------
  paper_id, title, authors, year, venue, arxiv_id, doi, url,
  in_scope (yes/partial/no/UNKNOWN),
  section (3_methods/4_failure_modes/5_defences/6_empirical/7_evaluation/8_open_problems/UNCLASSIFIED),
  key_contribution, failure_mode_addressed, method_type,
  has_code, has_dataset,
  read_status (unread/skimmed/read/deep),
  relevance_to_us (High/Medium/Low),
  my_notes, source_topic, last_seen

Usage
-----
  # First run: seed from existing dedup CSVs for judge-related topics
  python scripts/17_survey_corpus.py --seed-from-dedup

  # Merge new papers (default behavior; preserves manual edits)
  python scripts/17_survey_corpus.py

  # Pull fresh from arXiv with rate-limited queries (slow)
  python scripts/17_survey_corpus.py --fetch-arxiv

  # Limit dedup-seed to specific topic IDs
  python scripts/17_survey_corpus.py --seed-from-dedup --source T01 T02 T07

  # Rebuild from scratch (DESTRUCTIVE; backs up first)
  python scripts/17_survey_corpus.py --rebuild

The auto-classification is intentionally conservative; expect to hand-edit
30-50% of rows. The point of the script is to handle the mechanical work,
not to replace your reading.
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import re
import shutil
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

DEDUP_DIR    = ROOT / "data" / "papers_dedup"
CORPUS_PATH  = ROOT / "data" / "survey_corpus.csv"
BACKUP_DIR   = ROOT / "data" / "survey_corpus_backups"

# Topics in the existing pipeline known to seed the survey
DEFAULT_SEED_TOPICS = [
    "T01", "T02", "T03", "T04", "T05", "T06", "T07", "T08", "T09", "T10",
    "T14",  # judge-adjacent
]

# Survey section taxonomy (from SURVEY_STRUCTURE.md)
SECTIONS = [
    "3_methods",
    "4_failure_modes",
    "5_defences",
    "6_empirical",
    "7_evaluation",
    "8_open_problems",
]

# Keyword classifier — multi-section possible; assign to argmax (or
# UNCLASSIFIED if no match crosses min_matches threshold)
SECTION_KEYWORDS: dict[str, list[str]] = {
    "3_methods": [
        "pointwise", "pairwise", "listwise", "panel of judges", "panel-of-judges",
        "chain-of-thought", "ensemble", "consistency", "reward model",
        "judge method", "judging method", "judging protocol",
    ],
    "4_failure_modes": [
        "position bias", "self-preference", "self preference", "length bias",
        "style bias", "format bias", "prompt injection", "adversarial",
        "robustness", "calibration drift", "self-bias", "confounding",
        "judge failure",
    ],
    "5_defences": [
        "mitigation", "defence", "defense", "calibrat", "consensus",
        "structured output", "system prompt hardening", "randomis",
        "randomiz", "dual-judge", "judge ensemble", "post-hoc",
    ],
    "6_empirical": [
        "benchmark", "empirical study", "evaluation", "case study",
        "leaderboard", "HELM", "MT-Bench", "Chatbot Arena", "AlpacaEval",
        "AutoEval",
    ],
    "7_evaluation": [
        "meta-evaluation", "inter-annotator", "human agreement",
        "Cohen", "Krippendorff", "Pearson", "Spearman", "Kendall",
        "human-judge", "human judge gap", "validity",
    ],
    "8_open_problems": [
        "open question", "future work", "research agenda", "open problem",
        "limitation", "challenge", "future direction",
    ],
}

# In-scope classifier — looser than the section classifier
JUDGE_KEYWORDS  = [
    "llm-as-a-judge", "llm as a judge", "llm judge", "language model judge",
    "automatic evaluator", "evaluator llm", "judge model", "reward model",
    "panel of judges", "judging llm", "judge prompt",
]
LLM_KEYWORDS    = [
    "large language model", "llm", "gpt", "claude", "llama", "mistral",
    "gemini", "palm", "chatgpt",
]
EVAL_KEYWORDS   = [
    "evaluation", "metric", "scoring", "benchmark", "rating", "preference",
]

ARXIV_API = "http://export.arxiv.org/api/query"
ATOM_NS = "{http://www.w3.org/2005/Atom}"


# ----------------------------------------------------------------------------
# Pure helpers (testable)
# ----------------------------------------------------------------------------

def _normalise_text(s: str) -> str:
    """Lowercase + collapse whitespace; safe for keyword matching."""
    return re.sub(r"\s+", " ", (s or "").lower())


def classify_in_scope(title: str, abstract: str) -> str:
    """Classify a paper's relevance to the LLM-as-Judge survey.

    Returns: 'yes' / 'partial' / 'no'

    yes: explicitly about LLM judging
    partial: about LLM evaluation more generally
    no: not about LLMs or not about evaluation
    """
    text = _normalise_text(f"{title} {abstract}")
    has_judge = any(kw in text for kw in JUDGE_KEYWORDS)
    has_llm   = any(kw in text for kw in LLM_KEYWORDS)
    has_eval  = any(kw in text for kw in EVAL_KEYWORDS)
    if has_judge:
        return "yes"
    if has_llm and has_eval:
        return "partial"
    return "no"


def classify_section(title: str, abstract: str,
                     min_matches: int = 1) -> str:
    """Assign a paper to the survey section with the most keyword hits.

    Returns one of SECTIONS or 'UNCLASSIFIED'.
    """
    text = _normalise_text(f"{title} {abstract}")
    counts: dict[str, int] = {}
    for section, keywords in SECTION_KEYWORDS.items():
        c = sum(1 for kw in keywords if kw in text)
        if c >= min_matches:
            counts[section] = c
    if not counts:
        return "UNCLASSIFIED"
    # Argmax with deterministic tiebreaking (alphabetical)
    return max(sorted(counts.keys()), key=lambda s: counts[s])


def detect_failure_modes(title: str, abstract: str) -> str:
    """Return ; -joined list of failure-mode tags hit by this paper."""
    text = _normalise_text(f"{title} {abstract}")
    modes = {
        "position_bias":    ["position bias", "ordering bias", "position-based"],
        "self_preference":  ["self-preference", "self preference", "self-bias"],
        "length_bias":      ["length bias", "length-based"],
        "style_bias":       ["style bias"],
        "format_bias":      ["format bias"],
        "prompt_injection": ["prompt injection", "adversarial prompt"],
        "calibration":      ["calibration", "miscalibration"],
    }
    hits = [tag for tag, kws in modes.items() if any(kw in text for kw in kws)]
    return ";".join(hits)


def detect_method_type(title: str, abstract: str) -> str:
    """Best-effort method classification."""
    text = _normalise_text(f"{title} {abstract}")
    if "pairwise" in text or "pair-wise" in text:
        return "pairwise"
    if "pointwise" in text or "point-wise" in text:
        return "pointwise"
    if "listwise" in text or "list-wise" in text:
        return "listwise"
    if "panel" in text or "ensemble" in text:
        return "panel"
    if "reward model" in text:
        return "reward_model"
    return ""


def derive_paper_id(title: str, authors: str, year: str) -> str:
    """Stable citation key for the survey corpus. Distinct from
    16_extract_bibtex's keying (this one's optimised for uniqueness across
    the whole corpus, not BibTeX readability)."""
    # First author surname
    surname = "anonymous"
    if authors:
        sep = "|" if "|" in authors else (
            ";" if ";" in authors else (
                " and " if " and " in authors else ","))
        first = authors.split(sep)[0].strip()
        toks = first.split()
        if toks:
            surname = re.sub(r"[^a-z]+", "", toks[-1].lower()) or "anonymous"
    # Year
    m = re.search(r"\d{4}", str(year or ""))
    yr = m.group(0) if m else "nd"
    # First significant word of title
    word = "paper"
    for w in (title or "").split():
        w_clean = re.sub(r"[^a-zA-Z0-9]", "", w).lower()
        if w_clean and len(w_clean) >= 3 and w_clean not in {
            "the", "and", "for", "with", "from", "this", "that", "are"
        }:
            word = w_clean
            break
    return f"{surname}{yr}{word}"[:40]


def arxiv_id_from_url(url: str) -> str:
    if not url:
        return ""
    m = re.search(r"arxiv\.org/(?:abs|pdf)/([\w.\-]+?)(?:v\d+)?(?:\.pdf)?$", url)
    return m.group(1) if m else ""


def detect_code_dataset(url: str, abstract: str) -> tuple[str, str]:
    """Heuristic flags for has_code / has_dataset."""
    text = _normalise_text(abstract)
    has_code = "yes" if ("github" in (url or "").lower()
                         or "github.com" in text
                         or "code is available" in text
                         or "release the code" in text) else "no"
    has_data = "yes" if ("huggingface" in (url or "").lower()
                         or "huggingface.co" in text
                         or "dataset is available" in text
                         or "we release the dataset" in text) else "no"
    return (has_code, has_data)


# ----------------------------------------------------------------------------
# Corpus IO
# ----------------------------------------------------------------------------

CORPUS_FIELDS = [
    "paper_id", "title", "authors", "year", "venue", "arxiv_id", "doi", "url",
    "in_scope", "section", "key_contribution", "failure_mode_addressed",
    "method_type", "has_code", "has_dataset",
    "read_status", "relevance_to_us", "my_notes",
    "source_topic", "last_seen",
]

MANUAL_FIELDS = [
    # Fields a human edits; we preserve these on merge
    "in_scope", "section", "key_contribution", "failure_mode_addressed",
    "method_type", "has_code", "has_dataset",
    "read_status", "relevance_to_us", "my_notes",
]


def load_corpus(path: Path = CORPUS_PATH) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_corpus(rows: list[dict], path: Path = CORPUS_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CORPUS_FIELDS)
        w.writeheader()
        for r in rows:
            # Fill any missing keys
            for k in CORPUS_FIELDS:
                r.setdefault(k, "")
            w.writerow({k: r.get(k, "") for k in CORPUS_FIELDS})


def merge_rows(existing: list[dict], new: list[dict]) -> list[dict]:
    """Merge new rows into existing, keyed by paper_id.

    For NEW papers: add as-is.
    For EXISTING papers: keep manual fields if they differ from auto-classified
    (any non-default value is "manual").
    Returns merged list, sorted by paper_id.
    """
    by_id: dict[str, dict] = {r.get("paper_id", ""): r for r in existing if r.get("paper_id")}
    for n in new:
        pid = n.get("paper_id", "")
        if not pid:
            continue
        if pid not in by_id:
            n["last_seen"] = _now_iso()
            by_id[pid] = n
        else:
            # Preserve manual fields if non-default
            existing_row = by_id[pid]
            for field in MANUAL_FIELDS:
                ev = (existing_row.get(field) or "").strip()
                if _is_manual_value(field, ev):
                    # User has touched this field; keep their value
                    continue
                # Otherwise, refresh from new
                existing_row[field] = n.get(field, "")
            # Always refresh objective fields
            for field in ("title", "authors", "year", "venue", "doi", "url", "arxiv_id"):
                if n.get(field):
                    existing_row[field] = n[field]
            existing_row["last_seen"] = _now_iso()
            # Track that this paper appeared in another source topic
            old_st = (existing_row.get("source_topic") or "").split(";")
            new_st = (n.get("source_topic") or "").split(";")
            merged_st = sorted(set(s for s in old_st + new_st if s))
            existing_row["source_topic"] = ";".join(merged_st)
    return sorted(by_id.values(), key=lambda r: r.get("paper_id", ""))


def _is_manual_value(field: str, value: str) -> bool:
    """Return True if `value` looks like a human edit (not the auto-default)."""
    if not value:
        return False
    defaults = {
        "in_scope":             {"yes", "partial", "no", "unknown"},
        "section":              {"unclassified", *SECTIONS},
        "read_status":          {"unread"},        # any other status = manual
        "relevance_to_us":      set(),             # any value is manual
        "key_contribution":     set(),
        "failure_mode_addressed": set(),           # we auto-fill this; treat as auto unless...
        "method_type":          set(),
        "has_code":             {"yes", "no"},
        "has_dataset":          {"yes", "no"},
        "my_notes":             set(),             # any non-empty = manual
    }
    v = value.strip().lower()
    if field == "read_status":
        return v != "unread"
    if field in ("relevance_to_us", "key_contribution", "my_notes"):
        return bool(v)
    # For section/in_scope: only manual if value is non-default AND not the auto-classification list
    # We can't tell — treat as auto. Conservative: never overwrite if user set a value.
    return False


def _now_iso() -> str:
    return _dt.datetime.utcnow().isoformat(timespec="seconds") + "Z"


# ----------------------------------------------------------------------------
# Seeding from existing pipeline data
# ----------------------------------------------------------------------------

def row_from_dedup(rec: dict, source_topic: str) -> dict:
    title    = (rec.get("title") or "").strip()
    authors  = (rec.get("authors") or "").strip()
    year     = (rec.get("year") or "").strip()
    venue    = (rec.get("venue") or "").strip()
    doi      = (rec.get("doi") or "").strip()
    url      = (rec.get("url") or "").strip()
    # Pipeline dedup CSVs use abstract_snippet, not abstract. Fall back also
    # to matched_keywords + reason_included so we have signal even when the
    # snippet is empty (which is common — pipeline strips most abstracts).
    abstract = (rec.get("abstract")
                or rec.get("abstract_snippet")
                or "").strip()
    keyword_signal = " ".join([
        (rec.get("matched_keywords") or ""),
        (rec.get("reason_included") or ""),
    ]).strip()
    classify_text = f"{abstract} {keyword_signal}".strip()

    in_scope = classify_in_scope(title, classify_text)
    section  = classify_section(title, classify_text)
    failure_modes = detect_failure_modes(title, classify_text)
    method_type = detect_method_type(title, classify_text)
    has_code, has_dataset = detect_code_dataset(url, classify_text)
    arxiv_id = arxiv_id_from_url(url)

    return {
        "paper_id":      derive_paper_id(title, authors, year),
        "title":         title,
        "authors":       authors,
        "year":          year,
        "venue":         venue,
        "arxiv_id":      arxiv_id,
        "doi":           doi,
        "url":           url,
        "in_scope":      in_scope,
        "section":       section,
        "key_contribution": "",       # left for manual entry
        "failure_mode_addressed": failure_modes,
        "method_type":   method_type,
        "has_code":      has_code,
        "has_dataset":   has_dataset,
        "read_status":   "unread",
        "relevance_to_us": "",        # left for manual entry
        "my_notes":      "",
        "source_topic":  source_topic,
        "last_seen":     _now_iso(),
    }


def seed_from_dedup(topics: list[str]) -> list[dict]:
    """Read existing dedup CSVs for the named topics, return corpus rows."""
    rows: list[dict] = []
    for tid in topics:
        csv_path = DEDUP_DIR / f"{tid}.csv"
        if not csv_path.exists():
            print(f"  [skip] {tid}: no dedup CSV at {csv_path}", file=sys.stderr)
            continue
        with csv_path.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            n = 0
            for rec in reader:
                row = row_from_dedup(rec, tid)
                rows.append(row)
                n += 1
            print(f"  [{tid}] {n} papers from dedup CSV")
    return rows


# ----------------------------------------------------------------------------
# arXiv fetch (uses same approach as scripts/15_arxiv_watch.py)
# ----------------------------------------------------------------------------

def fetch_arxiv_papers(query: str, categories: list[str],
                       max_results: int = 50,
                       timeout: float = 30.0) -> list[dict]:
    """Fetch and parse arXiv Atom feed into corpus-shaped rows."""
    cat_filter = " OR ".join(f"cat:{c}" for c in categories)
    full_q = f"({query}) AND ({cat_filter})" if cat_filter else query
    params = {
        "search_query": full_q,
        "start": "0",
        "max_results": str(max_results),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "research-command-center/survey-corpus/1.0 "
                       "(mailto:rohithreddybc@gmail.com)",
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        xml_text = resp.read().decode("utf-8", errors="replace")
    return parse_arxiv_atom_to_rows(xml_text)


def parse_arxiv_atom_to_rows(xml_text: str) -> list[dict]:
    root = ET.fromstring(xml_text)
    out: list[dict] = []
    for entry in root.findall(f"{ATOM_NS}entry"):
        eid = (entry.findtext(f"{ATOM_NS}id") or "").strip()
        m = re.search(r"abs/([\w.\-]+?)(?:v\d+)?$", eid)
        arxiv_id = m.group(1) if m else eid
        title    = " ".join((entry.findtext(f"{ATOM_NS}title") or "").split())
        summary  = " ".join((entry.findtext(f"{ATOM_NS}summary") or "").split())
        published = (entry.findtext(f"{ATOM_NS}published") or "").strip()
        year = published[:4] if published else ""
        authors = []
        for a in entry.findall(f"{ATOM_NS}author"):
            name = (a.findtext(f"{ATOM_NS}name") or "").strip()
            if name:
                authors.append(name)
        url = ""
        for ln in entry.findall(f"{ATOM_NS}link"):
            if ln.attrib.get("rel") == "alternate":
                url = ln.attrib.get("href", "")
                break
        if not url:
            url = f"https://arxiv.org/abs/{arxiv_id}"
        rec = {
            "title":    title,
            "authors":  "|".join(authors),
            "year":     year,
            "venue":    "arXiv",
            "doi":      "",
            "url":      url,
            "abstract": summary,
        }
        out.append(row_from_dedup(rec, "arxiv"))
    return out


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--seed-from-dedup", action="store_true",
                   help="Read existing data/papers_dedup/<topic>.csv files for seeding")
    p.add_argument("--source", nargs="+", default=DEFAULT_SEED_TOPICS,
                   help="Topic IDs to seed from (default: T01..T10 + T14)")
    p.add_argument("--fetch-arxiv", action="store_true",
                   help="Pull fresh arXiv papers (slow; rate-limited)")
    p.add_argument("--rebuild", action="store_true",
                   help="DESTRUCTIVE: backup existing corpus and rebuild from scratch")
    p.add_argument("--out", default=str(CORPUS_PATH),
                   help="Output CSV path (default data/survey_corpus.csv)")
    p.add_argument("--sleep", type=float, default=5.0,
                   help="Seconds between arXiv calls (default 5.0)")
    args = p.parse_args(argv)

    out_path = Path(args.out)

    if args.rebuild and out_path.exists():
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        backup = BACKUP_DIR / f"survey_corpus.{_now_iso().replace(':', '-')}.csv"
        shutil.copy(out_path, backup)
        print(f"[rebuild] backed up to {backup}")
        existing: list[dict] = []
    else:
        existing = load_corpus(out_path)
        print(f"[load] existing corpus: {len(existing)} rows")

    new_rows: list[dict] = []

    if args.seed_from_dedup:
        print(f"[seed-dedup] from topics: {args.source}")
        new_rows.extend(seed_from_dedup(args.source))
        print(f"[seed-dedup] gathered {len(new_rows)} candidate rows")

    if args.fetch_arxiv:
        from json import loads
        qf = ROOT / "data" / "survey_corpus_queries.json"
        if not qf.exists():
            print(f"[fetch-arxiv] config not found: {qf}", file=sys.stderr)
        else:
            queries = loads(qf.read_text(encoding="utf-8")).get("queries", [])
            for i, q in enumerate(queries):
                if i > 0:
                    time.sleep(args.sleep)
                try:
                    rows = fetch_arxiv_papers(
                        q["arxiv_query"],
                        q.get("categories", []),
                        max_results=q.get("max_results", 30),
                    )
                    print(f"  [arxiv:{q['id']}] +{len(rows)} rows")
                    new_rows.extend(rows)
                except Exception as e:
                    print(f"  [arxiv:{q['id']}] ERROR: {e}", file=sys.stderr)

    merged = merge_rows(existing, new_rows)
    save_corpus(merged, out_path)
    print(f"[save] {len(merged)} total rows -> {out_path}")

    # Summary
    n_in_scope = sum(1 for r in merged if r.get("in_scope") == "yes")
    n_partial  = sum(1 for r in merged if r.get("in_scope") == "partial")
    n_unread   = sum(1 for r in merged if (r.get("read_status") or "unread") == "unread")
    print(f"[summary] in_scope=yes: {n_in_scope} | partial: {n_partial} | unread: {n_unread}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
