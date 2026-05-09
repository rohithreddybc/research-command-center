"""
07_compare_reviewers.py

Compare 8-reviewer panel outputs (and across providers) for each topic.
- score variance and provider disagreement
- decision plurality (mode) and confidence distribution
- per-role disagreement flagged

Output: data/agreement/<topic_id>.json
"""
from __future__ import annotations
import argparse
import json
import statistics as st
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from common.io_utils import read_json, write_json, log  # noqa: E402

REVIEWS_DIR = ROOT / "data" / "reviews"
AGREE_DIR = ROOT / "data" / "agreement"
AGREE_DIR.mkdir(parents=True, exist_ok=True)


def _gather(topic_id: str) -> list[dict[str, Any]]:
    d = REVIEWS_DIR / topic_id
    if not d.exists():
        return []
    out = []
    for f in d.glob("*.json"):
        if f.name.startswith("_") or f.name.startswith("inbox_pending"):
            continue
        obj = read_json(f, {})
        if not obj:
            continue
        # Skip pending placeholders even if filename was clobbered
        if obj.get("provider") == "inbox_pending":
            continue
        out.append(obj)
    return out


def _decision_score(d: str) -> int:
    return {"GO": 3, "NARROW": 2, "NEEDS_MORE_EVIDENCE": 1, "DROP": 0}.get(d, 1)


def compare_topic(topic_id: str) -> dict[str, Any]:
    reviews = _gather(topic_id)
    if not reviews:
        return {"topic_id": topic_id, "reviews": 0, "no_reviews": True}

    scores = [r.get("score", 0) for r in reviews if isinstance(r.get("score"), int) and r.get("score") > 0]
    decisions = [r.get("decision", "NEEDS_MORE_EVIDENCE") for r in reviews]
    confidences = [r.get("confidence", "LOW") for r in reviews]
    providers = [r.get("provider", "unknown") for r in reviews]

    decision_counts = Counter(decisions)
    plurality_decision, plurality_count = decision_counts.most_common(1)[0]
    decision_score_mean = sum(_decision_score(d) for d in decisions) / max(1, len(decisions))

    score_mean = st.mean(scores) if scores else 0
    score_stdev = st.pstdev(scores) if len(scores) >= 2 else 0

    # cross-provider per-role disagreement
    by_role: dict[str, list[dict[str, Any]]] = {}
    for r in reviews:
        by_role.setdefault(r.get("reviewer_role", ""), []).append(r)
    disagreements = []
    for role, items in by_role.items():
        if len(items) < 2:
            continue
        decs = {i.get("decision") for i in items}
        if len(decs) > 1:
            disagreements.append({
                "role": role,
                "decisions": [{"provider": i.get("provider"), "decision": i.get("decision"), "confidence": i.get("confidence")} for i in items],
            })

    # high-confidence-DROP votes carry more weight (skeptic signal)
    hard_drops = [r for r in reviews if r.get("decision") == "DROP" and r.get("confidence") == "HIGH"]

    payload = {
        "topic_id": topic_id,
        "n_reviews": len(reviews),
        "providers": dict(Counter(providers)),
        "scores": {"mean": round(score_mean, 2), "stdev": round(score_stdev, 2), "n": len(scores)},
        "decisions": dict(decision_counts),
        "plurality_decision": plurality_decision,
        "plurality_count": plurality_count,
        "decision_score_mean_0to3": round(decision_score_mean, 2),
        "confidences": dict(Counter(confidences)),
        "high_confidence_drops": len(hard_drops),
        "per_role_disagreements": disagreements,
        "high_disagreement_flag": (len(disagreements) >= 3) or (score_stdev >= 1.2),
    }
    log("07_compare", f"{topic_id} plurality={plurality_decision} stdev={round(score_stdev,2)}")
    return payload


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--topic", default=None)
    args = p.parse_args(argv)

    if args.topic:
        topics = [args.topic]
    else:
        topics = [d.name for d in REVIEWS_DIR.iterdir() if d.is_dir()]

    out_summary = []
    for tid in topics:
        a = compare_topic(tid)
        write_json(AGREE_DIR / f"{tid}.json", a)
        out_summary.append({k: a[k] for k in (
            "topic_id", "n_reviews", "plurality_decision", "decision_score_mean_0to3",
            "high_confidence_drops", "high_disagreement_flag"
        ) if k in a})
    print(json.dumps(out_summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
