"""
16_extract_bibtex.py

Convert a topic's deduplicated paper list into BibTeX entries for paper writing.

Reads:  data/papers_dedup/<topic_id>.csv
Writes: references/<topic_id>.bib

Why this exists
---------------
When you start writing T02 (or any other paper), you need a clean BibTeX file
with all the closest related work. This script generates one from the pipeline's
already-collected and de-duplicated paper corpus, so you don't have to manually
look up each citation.

Citation key strategy
---------------------
- Primary: first author last name + year + first significant word of title
  (e.g. "wang2023position")
- If DOI is available, also includes the DOI field
- If arXiv ID detectable in URL, also includes eprint + archivePrefix

Usage
-----
  # One topic
  python scripts/16_extract_bibtex.py --topic T02

  # All topics with dedup CSVs
  python scripts/16_extract_bibtex.py --all

  # Filter by minimum relevance score
  python scripts/16_extract_bibtex.py --topic T02 --min-relevance 0.4
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DEDUP_DIR  = ROOT / "data" / "papers_dedup"
OUT_DIR    = ROOT / "references"

STOPWORDS = {
    "a", "an", "the", "of", "for", "on", "in", "and", "or", "to", "with",
    "from", "by", "at", "as", "is", "are", "was", "were", "be", "been",
    "this", "that", "these", "those",
}


# ----------------------------------------------------------------------------
# Pure helpers (testable)
# ----------------------------------------------------------------------------

def _normalise(s: str) -> str:
    """Lowercase, alnum-only, no spaces."""
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def _first_significant_word(title: str) -> str:
    for word in (title or "").split():
        w = re.sub(r"[^A-Za-z0-9]", "", word).lower()
        if w and w not in STOPWORDS and len(w) >= 3:
            return w
    return "paper"


def _split_authors(authors: str) -> list[str]:
    """Split an author string on the first separator that appears.

    Pipeline CSVs commonly use '|', ';', ' and ', or ',' depending on source.
    """
    if not authors or not authors.strip():
        return []
    for sep in ("|", ";", " and "):
        if sep in authors:
            return [a.strip() for a in authors.split(sep) if a.strip()]
    if "," in authors and authors.count(",") >= 2:
        # Likely a comma-separated list; if only one comma, could be "Last, First"
        return [a.strip() for a in authors.split(",") if a.strip()]
    s = authors.strip()
    return [s] if s else []


def _first_author_lastname(authors: str) -> str:
    parts_list = _split_authors(authors)
    if not parts_list:
        return "anonymous"
    first = parts_list[0]
    tokens = first.split()
    if not tokens:
        return "anonymous"
    return _normalise(tokens[-1]) or "anonymous"


def cite_key(authors: str, year: str, title: str) -> str:
    surname = _first_author_lastname(authors)
    yr = re.search(r"\d{4}", str(year or ""))
    yr_str = yr.group(0) if yr else "nd"
    word = _first_significant_word(title)
    key = f"{surname}{yr_str}{word}"
    # Cap length
    return key[:40]


def _arxiv_id_from_url(url: str) -> str | None:
    if not url:
        return None
    m = re.search(r"arxiv\.org/(?:abs|pdf)/([\w.\-]+?)(?:v\d+)?(?:\.pdf)?$", url)
    return m.group(1) if m else None


def _bibtex_escape(s: str) -> str:
    """Escape characters BibTeX cares about. Keep readable."""
    if not s:
        return ""
    s = s.replace("\\", r"\textbackslash{}")
    for ch in ("&", "%", "$", "#", "_", "{", "}"):
        s = s.replace(ch, "\\" + ch)
    # Strip newlines
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _entry_type(venue: str, url: str, doi: str) -> str:
    v = (venue or "").lower()
    if "arxiv" in v or _arxiv_id_from_url(url):
        return "misc"
    if "journal" in v or "transactions" in v or "letters" in v:
        return "article"
    if "proceedings" in v or "conference" in v or "workshop" in v:
        return "inproceedings"
    if doi:
        # Default to article when we have a DOI but no venue clue
        return "article"
    return "misc"


def to_bibtex(row: dict) -> str:
    """Convert one dedup CSV row into a BibTeX entry string."""
    title    = (row.get("title") or "").strip()
    authors  = (row.get("authors") or "").strip()
    year     = (row.get("year") or "").strip()
    venue    = (row.get("venue") or "").strip()
    doi      = (row.get("doi") or "").strip()
    url      = (row.get("url") or "").strip()

    key = cite_key(authors, year, title)
    etype = _entry_type(venue, url, doi)

    # Convert authors to BibTeX " and "-separated form
    author_list = _split_authors(authors)
    author_field = " and ".join(author_list) if author_list else ""

    fields: list[tuple[str, str]] = []
    fields.append(("title", _bibtex_escape(title)))
    if author_field:
        fields.append(("author", _bibtex_escape(author_field)))
    if year:
        m = re.search(r"\d{4}", year)
        if m:
            fields.append(("year", m.group(0)))
    if venue:
        if etype == "article":
            fields.append(("journal", _bibtex_escape(venue)))
        elif etype == "inproceedings":
            fields.append(("booktitle", _bibtex_escape(venue)))
        else:
            fields.append(("howpublished", _bibtex_escape(venue)))
    if doi:
        fields.append(("doi", _bibtex_escape(doi)))
    if url:
        fields.append(("url", _bibtex_escape(url)))
    arxiv_id = _arxiv_id_from_url(url)
    if arxiv_id:
        fields.append(("eprint", arxiv_id))
        fields.append(("archivePrefix", "arXiv"))

    rel = row.get("relevance_score") or row.get("relevance") or ""
    note_parts = []
    if rel:
        note_parts.append(f"relevance={rel}")
    cit = row.get("citations") or ""
    if cit:
        note_parts.append(f"citations={cit}")
    if note_parts:
        fields.append(("note", _bibtex_escape("; ".join(note_parts))))

    body = ",\n  ".join(f"{k:>13s} = {{{v}}}" for k, v in fields)
    return f"@{etype}{{{key},\n  {body}\n}}\n"


def deduplicate_keys(entries: list[str]) -> list[str]:
    """If two entries share the same key, append a/b/c suffix."""
    seen: dict[str, int] = {}
    out: list[str] = []
    for e in entries:
        m = re.match(r"^@\w+\{([^,]+),", e)
        if not m:
            out.append(e)
            continue
        key = m.group(1)
        n = seen.get(key, 0)
        if n == 0:
            seen[key] = 1
            out.append(e)
        else:
            suffix = chr(ord("a") + n - 1)
            new_key = f"{key}{suffix}"
            seen[key] = n + 1
            out.append(re.sub(r"^@(\w+)\{[^,]+,",
                              rf"@\1{{{new_key},", e, count=1))
    return out


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def process_topic(topic_id: str, *,
                  min_relevance: float = 0.0,
                  out_dir: Path = OUT_DIR) -> tuple[int, Path]:
    src = DEDUP_DIR / f"{topic_id}.csv"
    if not src.exists():
        raise FileNotFoundError(f"No dedup CSV for topic {topic_id} at {src}")
    rows: list[dict] = []
    with src.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rel = 0.0
            try:
                rel = float(r.get("relevance_score") or 0)
            except Exception:
                pass
            if rel < min_relevance:
                continue
            rows.append(r)

    # Sort by relevance then citations desc
    def _ci(x: dict) -> int:
        try:
            return int(x.get("citations") or 0)
        except Exception:
            return 0
    def _rel(x: dict) -> float:
        try:
            return float(x.get("relevance_score") or 0)
        except Exception:
            return 0.0
    rows.sort(key=lambda r: (_rel(r), _ci(r)), reverse=True)

    entries = [to_bibtex(r) for r in rows]
    entries = deduplicate_keys(entries)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{topic_id}.bib"
    header = (
        f"% References for topic {topic_id}\n"
        f"% Generated by scripts/16_extract_bibtex.py from data/papers_dedup/{topic_id}.csv\n"
        f"% min_relevance filter: {min_relevance}\n"
        f"% n_entries: {len(entries)}\n\n"
    )
    out_path.write_text(header + "\n".join(entries), encoding="utf-8")
    return (len(entries), out_path)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--topic", help="Topic ID (e.g. T02)")
    g.add_argument("--all", action="store_true",
                   help="Process every dedup CSV in data/papers_dedup/")
    p.add_argument("--min-relevance", type=float, default=0.0,
                   help="Skip rows with relevance below this threshold")
    p.add_argument("--out-dir", default=str(OUT_DIR),
                   help="Output directory (default references/)")
    args = p.parse_args(argv)

    out_dir = Path(args.out_dir)

    if args.all:
        csvs = sorted(DEDUP_DIR.glob("*.csv"))
        if not csvs:
            print("No dedup CSVs found.", file=sys.stderr)
            return 1
        total = 0
        for c in csvs:
            tid = c.stem
            try:
                n, out_path = process_topic(tid,
                                            min_relevance=args.min_relevance,
                                            out_dir=out_dir)
                print(f"[{tid}] {n} entries -> {out_path}")
                total += n
            except FileNotFoundError as e:
                print(f"[{tid}] skipped: {e}", file=sys.stderr)
        print(f"Total entries written: {total}")
        return 0

    try:
        n, out_path = process_topic(args.topic,
                                    min_relevance=args.min_relevance,
                                    out_dir=out_dir)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        return 1
    print(f"[{args.topic}] {n} entries -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
