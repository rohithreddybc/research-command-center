"""
06_llm_review_topics.py

8-reviewer panel.

Default provider: Claude Code CLI (`claude -p`). Uses the user's Max plan, no API key.
  Requirement: run `claude auth login` once from PowerShell on this machine.
  Set CLAUDE_CLI_PATH if claude.exe is not auto-detected.

OpenAI is strictly opt-in and bounded:
  - --use-openai-tiebreaker: enable
  - Only invoked for the top --tiebreaker-top-n topics (default 4)
  - Only for the brutal_skeptic and novelty_saturation roles
  - Only if Claude reviewers disagree on the topic's plurality decision
  - Bounded by data/cache/openai_budget.json (default 8 calls/run)

If no provider works, prompts are written to data/reviews/_inbox/ for manual paste.

Outputs:
- data/reviews/<topic_id>/<provider>_<role>.json
- data/reviews/<topic_id>/_packet.json   (the exact packet, for traceability)
"""
from __future__ import annotations
import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.io_utils import read_csv, read_json, write_json, log, evidence_dir, topic_dir  # noqa: E402
from common.llm_panel import (  # noqa: E402
    REVIEWER_ROLES, review_claude_cli, review_openai,
    have_claude_cli, have_openai_key, write_inbox_prompt,
    read_inbox_reply, reset_openai_budget, openai_budget_status,
    ERRORS as PANEL_ERRORS,
)

REPORTS = ROOT / "reports"
REPORTS.mkdir(parents=True, exist_ok=True)


def _flush_errors() -> bool:
    """Write reports/llm_review_errors.md if any provider error was recorded.
    Returns True if file was written."""
    if not PANEL_ERRORS:
        # If a previous run left a file but this run was clean, blank it out so the report
        # banner doesn't keep warning.
        p = REPORTS / "llm_review_errors.md"
        if p.exists():
            p.write_text("# LLM review errors\n\n_None recorded in latest run._\n", encoding="utf-8")
        return False
    lines = ["# LLM review errors", "",
             f"Errors recorded: **{len(PANEL_ERRORS)}**", ""]
    by_provider: dict[str, list[dict[str, Any]]] = {}
    for e in PANEL_ERRORS:
        by_provider.setdefault(e["provider"], []).append(e)
    for prov, items in by_provider.items():
        lines.append(f"## {prov} ({len(items)})")
        lines.append("")
        lines.append("| Topic | Role | Message |")
        lines.append("|---|---|---|")
        for e in items[:200]:
            msg = e["message"].replace("|", "/")[:200]
            lines.append(f"| {e['topic_id']} | {e['role']} | {msg} |")
        lines.append("")
    if any(("Not logged in" in e["message"]) for e in PANEL_ERRORS):
        lines.append("## Common fix")
        lines.append("")
        lines.append("Run **`claude auth login`** once from PowerShell, then re-run "
                     "`python scripts/06_llm_review_topics.py` (cached HTTP / packets are reused).")
        lines.append("")
    (REPORTS / "llm_review_errors.md").write_text("\n".join(lines), encoding="utf-8")
    return True

QUERIES_DIR = ROOT / "data" / "queries"
DEDUP_DIR = ROOT / "data" / "papers_dedup"
SCORES_DIR = ROOT / "data" / "scores"
REVIEWS_DIR = ROOT / "data" / "reviews"

TIEBREAKER_ROLES = {"brutal_skeptic", "novelty_saturation"}


def assemble_packet(topic_id: str, topic: dict[str, Any]) -> dict[str, Any]:
    edir = evidence_dir(topic_id)
    score = read_json(SCORES_DIR / f"{topic_id}.json", {})
    dedup = read_csv(DEDUP_DIR / f"{topic_id}.csv") if (DEDUP_DIR / f"{topic_id}.csv").exists() else []
    def _ci(x):
        try:
            return int(x.get("citations", 0) or 0)
        except Exception:
            return 0
    top_papers = sorted(dedup, key=_ci, reverse=True)[:25]
    venues = read_json(edir / "venues.json", {})
    doaj = read_json(edir / "doaj.json", [])
    gh = read_json(edir / "github.json", [])
    hf = read_json(edir / "huggingface.json", [])
    pwc = read_json(edir / "paperswithcode.json", [])
    return {
        "topic": topic,
        "metrics": score,
        "top_papers": [{
            "title": p["title"], "year": p.get("year"), "venue": p.get("venue"),
            "citations": p.get("citations"), "sources": p.get("sources"),
            "doi": p.get("doi"),
        } for p in top_papers],
        "venue_evidence": {
            "venues": (venues or {}).get("venues", []),
            "doaj_no_apc_count": sum(1 for batch in doaj for r in batch.get("results", []) or [] if r.get("no_apc")),
            "doaj_examples": [
                {"title": r.get("title"), "no_apc": r.get("no_apc"), "license": r.get("license")}
                for batch in doaj[:2] for r in (batch.get("results", []) or [])[:5]
            ],
        },
        "tools_and_datasets": {
            "github_top": [
                {"name": r.get("name"), "stars": r.get("stars"), "description": (r.get("description") or "")[:200]}
                for batch in gh for r in sorted(batch.get("results", []) or [], key=lambda x: x.get("stars", 0), reverse=True)[:5]
            ][:10],
            "huggingface_top": [
                {"id": r.get("id"), "downloads": r.get("downloads")}
                for batch in hf for r in sorted(batch.get("results", []) or [], key=lambda x: x.get("downloads", 0), reverse=True)[:5]
            ][:10],
            "pwc_datasets": [
                {"name": d.get("name"), "introduced": d.get("introduced_date")}
                for batch in pwc for d in (batch.get("datasets") or [])[:5]
            ][:10],
        },
    }


def topic_overall(topic_id: str) -> float:
    s = read_json(SCORES_DIR / f"{topic_id}.json", {})
    return float(s.get("rubric", {}).get("composites", {}).get("Overall", 0) or 0)


def claude_disagreement(reviews: list[dict[str, Any]]) -> bool:
    """High disagreement = no plurality > 50% across decisions."""
    decs = [r.get("decision") for r in reviews if r.get("provider") == "claude_cli"]
    if len(decs) < 4:
        return True
    counts = Counter(decs)
    top, top_n = counts.most_common(1)[0]
    return (top_n / len(decs)) < 0.5


def review_one_topic(
    topic_id: str, topic: dict[str, Any],
    use_openai_tiebreaker: bool, is_top_n: bool,
) -> dict[str, Any]:
    out_dir = topic_dir("data/reviews", topic_id)
    packet = assemble_packet(topic_id, topic)
    write_json(out_dir / "_packet.json", packet)

    primary_provider = "claude_cli" if have_claude_cli() else "inbox"

    reviews: list[dict[str, Any]] = []

    # Pass 1: Claude CLI for all 8 roles
    cli_failed = False
    if primary_provider == "claude_cli":
        for role in REVIEWER_ROLES:
            r = review_claude_cli(role, topic, packet)
            if r is None:
                cli_failed = True
                continue
            reviews.append(r)
            write_json(out_dir / f"claude_cli_{role['role']}.json", r)
        if cli_failed and not reviews:
            # Auth or transport failure: drop inbox prompts so user can run reviews via
            # `claude auth login` then rerun, or paste into another Claude/ChatGPT session.
            for role in REVIEWER_ROLES:
                p = write_inbox_prompt(role, topic, packet)
                stub = {
                    "reviewer_role": role["role"], "score": 0,
                    "decision": "NEEDS_MORE_EVIDENCE", "confidence": "LOW",
                    "evidence_used": [],
                    "evidence_missing": [f"awaiting reviewer; prompt at {p.name}"],
                    "biggest_risk": "no automated reviewer ran (claude CLI not authed)",
                    "recommendation": "Run `claude auth login` once from PowerShell, then re-run scripts/06_llm_review_topics.py",
                    "provider": "inbox_pending",
                }
                reviews.append(stub)
                write_json(out_dir / f"inbox_pending_{role['role']}.json", stub)
    else:
        # Inbox fallback: drop prompts for manual paste
        for role in REVIEWER_ROLES:
            existing = read_inbox_reply(role, topic, packet)
            if existing:
                existing["provider"] = "inbox_manual"
                reviews.append(existing)
                write_json(out_dir / f"inbox_{role['role']}.json", existing)
            else:
                p = write_inbox_prompt(role, topic, packet)
                stub = {
                    "reviewer_role": role["role"],
                    "score": 0,
                    "decision": "NEEDS_MORE_EVIDENCE",
                    "confidence": "LOW",
                    "evidence_used": [],
                    "evidence_missing": [f"awaiting manual reply at {p.name}"],
                    "biggest_risk": "no automated provider available",
                    "recommendation": "Run `claude auth login` and rerun, or paste the prompt into a Claude/ChatGPT session and save as .reply.json next to the prompt.",
                    "provider": "inbox_pending",
                }
                reviews.append(stub)
                write_json(out_dir / f"inbox_pending_{role['role']}.json", stub)

    # Pass 2: OpenAI tiebreaker, strictly bounded
    if use_openai_tiebreaker and is_top_n and have_openai_key():
        if claude_disagreement(reviews):
            for role in REVIEWER_ROLES:
                if role["role"] not in TIEBREAKER_ROLES:
                    continue
                r = review_openai(role, topic, packet)
                if r:
                    reviews.append(r)
                    write_json(out_dir / f"openai_{role['role']}.json", r)

    log("06_llm",
        f"{topic_id} reviews={len(reviews)} provider={primary_provider} "
        f"openai_budget={openai_budget_status()}")
    return {"topic_id": topic_id, "reviews": reviews}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", default=None)
    ap.add_argument("--use-openai-tiebreaker", action="store_true",
                    help="Spend bounded OpenAI calls on top-N topics with Claude disagreement.")
    ap.add_argument("--tiebreaker-top-n", type=int, default=4)
    ap.add_argument("--reset-openai-budget", action="store_true")
    ap.add_argument("--openai-budget", type=int, default=8)
    args = ap.parse_args(argv)

    if args.reset_openai_budget:
        reset_openai_budget(args.openai_budget)

    files = sorted(QUERIES_DIR.glob("*.json"))
    if args.topic:
        files = [f for f in files if f.stem == args.topic]

    # Determine top-N by Overall to gate tiebreaker spending
    overalls = [(f.stem, topic_overall(f.stem)) for f in files]
    overalls.sort(key=lambda x: x[1], reverse=True)
    top_n_set = set(tid for tid, _ in overalls[: args.tiebreaker_top_n])

    summary = []
    for f in files:
        q = read_json(f)
        if not q:
            continue
        topic = q["topic"]
        is_top_n = topic["topic_id"] in top_n_set
        s = review_one_topic(topic["topic_id"], topic,
                              use_openai_tiebreaker=args.use_openai_tiebreaker,
                              is_top_n=is_top_n)
        summary.append({"topic_id": s["topic_id"], "n_reviews": len(s["reviews"]),
                        "is_top_n": is_top_n})
    wrote_err = _flush_errors()
    print(json.dumps({
        "summary": summary,
        "openai_budget": openai_budget_status(),
        "errors_recorded": len(PANEL_ERRORS),
        "errors_file": str(REPORTS / "llm_review_errors.md") if wrote_err else None,
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
