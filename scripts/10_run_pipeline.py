"""
10_run_pipeline.py

Orchestrate the iterative verification pipeline.

Steps:
  1) generate_queries (01)
  2) collect_topic_evidence (02)
  3) collect_extra_evidence (03)
  4) collect_venue_evidence (04)
  5) score (05)
  6) llm_review (06)         [skipped if --no-llm]
  7) compare_reviewers (07)
  8) confidence_gate (08)
  9) if any topic NEEDS_MORE_EVIDENCE and rounds remain -> expand queries and re-run 02-08 for those topics
 10) generate_final_report (09)

Per-topic round logs: data/round_log/<topic_id>.json
"""
from __future__ import annotations
import argparse
import importlib.util
import json
import sys
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.io_utils import read_json, write_json, log, read_csv  # noqa: E402

QUERIES_DIR = ROOT / "data" / "queries"
DECISIONS_DIR = ROOT / "data" / "decisions"
ROUND_LOG_DIR = ROOT / "data" / "round_log"
ROUND_LOG_DIR.mkdir(parents=True, exist_ok=True)


def _load(stem: str):
    """Dynamically load a sibling script with a numeric prefix (e.g. 01_generate_queries)."""
    matches = list((ROOT / "scripts").glob(f"{stem}*.py"))
    if not matches:
        raise FileNotFoundError(f"No script for {stem}")
    path = matches[0]
    spec = importlib.util.spec_from_file_location(f"_pipe_{stem}", path)
    mod = importlib.util.module_from_spec(spec)  # type: ignore
    assert spec and spec.loader
    spec.loader.exec_module(mod)  # type: ignore
    return mod


def expand_queries_for_topic(topic_id: str) -> bool:
    """Add fallback synonyms / axis pairings to a topic's queries.json. Returns True if expanded."""
    qf = QUERIES_DIR / f"{topic_id}.json"
    q = read_json(qf, {})
    if not q:
        return False
    base_kws = q["topic"].get("keywords", "").split("|")
    syns = q["topic"].get("synonyms", "").split(";")
    axes = ["limitations", "open problems", "review", "evaluation"]
    extra_s2 = []
    for k in [w for w in (base_kws + syns) if w and w.strip()]:
        for a in axes:
            extra_s2.append(f"{k.strip()} {a}")
    queries = q["queries"]
    queries["semantic_scholar"] = list(dict.fromkeys((queries.get("semantic_scholar") or []) + extra_s2[:8]))
    queries["openalex"] = list(dict.fromkeys((queries.get("openalex") or []) + extra_s2[:6]))
    write_json(qf, q)
    return True


def run_single_topic_collection(stem: str, topic_id: str) -> None:
    mod = _load(stem)
    sys.argv = [stem, "--topic", topic_id]
    mod.main()


def run_full_collection(stem: str) -> None:
    mod = _load(stem)
    sys.argv = [stem]
    mod.main()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--max-rounds", type=int, default=2)
    ap.add_argument("--year-range", default="2022-2026")
    ap.add_argument("--limit-per-query", type=int, default=15)
    ap.add_argument("--skip-collect", action="store_true",
                    help="Skip 02/03/04 (evidence already collected)")
    ap.add_argument("--skip-llm", action="store_true",
                    help="Alias for --no-llm")
    args = ap.parse_args(argv)
    if args.skip_llm:
        args.no_llm = True

    t0 = time.time()
    log("10_pipe", f"START rounds<= {args.max_rounds}, no_llm={args.no_llm}")

    # 01 queries
    print("[1/9] generate queries")
    mod = _load("01_generate_queries")
    sys.argv = ["01"]
    mod.main()

    # initial round 02-04
    if not args.skip_collect:
        print("[2/9] collect topic evidence")
        mod = _load("02_collect_topic_evidence")
        sys.argv = ["02", "--year-range", args.year_range, "--limit-per-query", str(args.limit_per_query)]
        mod.main()

        print("[3/9] collect extra evidence")
        run_full_collection("03_collect_extra_evidence")

        print("[4/9] collect venue evidence")
        run_full_collection("04_collect_venue_evidence")

    # iterative loop
    for round_idx in range(1, args.max_rounds + 1):
        print(f"--- round {round_idx} ---")
        print("[5/9] score topics")
        run_full_collection("05_score_topics")

        if not args.no_llm:
            print("[6/9] llm review panel")
            run_full_collection("06_llm_review_topics")
        else:
            print("[6/9] llm review SKIPPED")

        print("[7/9] compare reviewers")
        run_full_collection("07_compare_reviewers")

        print("[8/9] confidence gate")
        run_full_collection("08_confidence_gate")

        # who needs another round?
        decisions_csv = DECISIONS_DIR / "decisions.csv"
        if not decisions_csv.exists():
            break
        rows = read_csv(decisions_csv)
        nme = [r for r in rows if r.get("final_decision") == "NEEDS_MORE_EVIDENCE"]
        log("10_pipe", f"round {round_idx} NME={[r['topic_id'] for r in nme]}")
        if not nme:
            break
        if round_idx >= args.max_rounds:
            log("10_pipe", "max_rounds reached; remaining NME topics will be reported as such")
            break

        # expand queries + re-collect just for NME topics
        for r in nme:
            tid = r["topic_id"]
            expand_queries_for_topic(tid)
            run_single_topic_collection("02_collect_topic_evidence", tid)
            run_single_topic_collection("03_collect_extra_evidence", tid)
            run_single_topic_collection("04_collect_venue_evidence", tid)
            write_json(ROUND_LOG_DIR / f"{tid}.json", {
                "topic_id": tid,
                "round_completed": round_idx,
                "expanded": True,
                "ts": int(time.time()),
            })

    # 09 final report
    print("[9/9] final report")
    mod = _load("09_generate_final_report")
    sys.argv = ["09"]
    mod.main()

    dt = time.time() - t0
    log("10_pipe", f"DONE in {dt:.1f}s")
    print(f"Pipeline done in {dt:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
