"""
Tiny YAML-subset loader — flat key:value lines only, no nesting, no PyYAML dep.

Type inference: int, float, bool (true/false), null, quoted strings, bare strings.
Lines starting with # are comments. Blank lines ignored.
"""
from __future__ import annotations
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "config.yaml"

DEFAULTS: dict[str, Any] = {
    "year_range": "2022-2026",
    "limit_per_query": 12,
    "max_rounds": 3,
    "relevance_min": 0.20,
    "relevance_keep_max": 80,
    "relevance_w_primary_title": 4.0,
    "relevance_w_primary_abstract": 1.5,
    "relevance_w_keyword_title": 2.0,
    "relevance_w_keyword_abstract": 0.8,
    "relevance_w_synonym_title": 1.0,
    "relevance_w_synonym_abstract": 0.4,
    "relevance_normalize_denom": 8.0,
    "artifact_density_high": 0.7,
    "artifact_density_med": 0.4,
    "differentiator_required_threshold": 0.5,
    "gate_overall_min_for_go": 14,
    "gate_citation_min_for_go": 3,
    "gate_artifact_min_for_go": 3,
    "gate_venue_min_for_go": 2,
    "gate_ip_max_for_go": 1,
    "gate_saturation_max_for_go": 4,
    "gate_min_evidence_sources": 2,
    "gate_min_review_decision_score": 2.0,
    "gate_high_disagreement_score_stdev": 1.2,
    "gate_force_low_when_no_reviews": True,
    "gate_require_llm_for_go": True,
    "tiebreaker_top_n": 4,
    "openai_budget_default": 8,
    "claude_cli_model": "haiku",
    "claude_cli_timeout_sec": 180,
}


def _coerce(v: str) -> Any:
    s = v.strip()
    if not s:
        return s
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    low = s.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if low in ("null", "none", "~"):
        return None
    try:
        if "." in s or "e" in low:
            return float(s)
        return int(s)
    except ValueError:
        return s


def load(path: Path | None = None) -> dict[str, Any]:
    p = path or CONFIG_PATH
    out = dict(DEFAULTS)
    if not p.exists():
        return out
    for raw in p.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip() or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        if not key:
            continue
        out[key] = _coerce(val)
    return out


CFG = load()
