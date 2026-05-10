"""
Profile-based topic scoring.

Default profile: blind_citation (pure academic merit, no personal-goal weights).
Personal-goal profiles are subject to the blind_citation gate enforced in
08_confidence_gate.py.

This module:
- Loads weight profiles from config/weight_profiles.yaml
- Maps per-topic raw signals (from data/scores/<id>.json) to the 18 weight
  components defined in the YAML
- Computes per-profile Overall scores
- Provides CLI flag parsing for --profile and --weight-* overrides

Used by: 05_score_topics.py, 08_confidence_gate.py, 09_generate_final_report.py,
13_bias_audit.py.
"""
from __future__ import annotations

import math
import re
import warnings
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PROFILE_FILE = ROOT / "config" / "weight_profiles.yaml"

DEFAULT_PROFILE = "blind_citation"

# Canonical 18 weight components — every profile MUST list all of these
WEIGHT_COMPONENTS = [
    "citation_potential",
    "topic_momentum",
    "gap_clarity",
    "novelty",
    "saturation_penalty",
    "existing_work_penalty",
    "artifact_value",
    "venue_credibility",
    "free_publication",
    "publication_speed",
    "methodological_rigor",
    "healthcare_relevance",
    "high_stakes_relevance",
    "niw_value",
    "eb1a_value",
    "faang_career_value",
    "execution_feasibility",
    "ip_risk_penalty",
]

# Components that represent personal goals — must be 0 in blind_citation
PERSONAL_GOAL_COMPONENTS = {
    "healthcare_relevance",
    "high_stakes_relevance",
    "niw_value",
    "eb1a_value",
    "faang_career_value",
    "free_publication",
    "publication_speed",
}

# Keyword sets used for component derivation (transparent, auditable)
HEALTHCARE_KEYWORDS = ["clinical", "health", "medical", "patient", "ehr",
                       "guideline", "icu", "discharge", "medqa", "pubmed"]
HIGH_STAKES_KEYWORDS = ["clinical", "medical", "legal", "financial",
                        "regulatory", "safety-critical", "fda"]
LLM_EVAL_KEYWORDS = ["llm", "rag", "agent", "judge", "tokeniz",
                     "alignment", "prompt", "llm-as-a-judge"]
ARTIFACT_TARGETS = ["dataset", "benchmark", "tool", "database", "framework"]
SURVEY_TARGETS = ["survey", "taxonomy", "review"]


# ---------------------------------------------------------------------------
# YAML loader (no PyYAML dependency required; tries PyYAML first then falls back)
# ---------------------------------------------------------------------------

def load_profiles(path: Path = PROFILE_FILE) -> dict[str, dict[str, Any]]:
    """Returns {profile_name: {description, is_personal_goal, weights{...}, modifiers{...}}}."""
    if not path.exists():
        raise FileNotFoundError(f"weight_profiles.yaml not found at {path}")
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except ImportError:
        return _hand_yaml_loader(path)


def _hand_yaml_loader(path: Path) -> dict[str, dict[str, Any]]:
    """Minimal YAML parser for the specific structure of weight_profiles.yaml."""
    profiles: dict[str, dict[str, Any]] = {}
    cur_profile: str | None = None
    cur_section: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        stripped = line.strip()

        if indent == 0 and stripped.endswith(":"):
            cur_profile = stripped[:-1].strip()
            profiles[cur_profile] = {"weights": {}, "modifiers": {}}
            cur_section = None
        elif cur_profile and indent == 2 and stripped.endswith(":"):
            cur_section = stripped[:-1].strip()
            if cur_section in ("weights", "modifiers"):
                profiles[cur_profile][cur_section] = {}
            else:
                cur_section = None
        elif cur_profile and indent == 2 and ":" in stripped:
            k, _, v = stripped.partition(":")
            profiles[cur_profile][k.strip()] = _yaml_val(v.strip())
            cur_section = None
        elif cur_profile and indent == 4 and ":" in stripped and cur_section in ("weights", "modifiers"):
            k, _, v = stripped.partition(":")
            profiles[cur_profile][cur_section][k.strip().strip('"')] = _yaml_val(v.strip())
    return profiles


def _yaml_val(s: str) -> Any:
    s = s.strip().strip('"').strip("'")
    if s == "true":
        return True
    if s == "false":
        return False
    try:
        if "." in s or "e" in s.lower():
            return float(s)
        return int(s)
    except ValueError:
        return s


# ---------------------------------------------------------------------------
# Profile validation
# ---------------------------------------------------------------------------

def validate_profile(name: str, profile: dict[str, Any]) -> list[str]:
    """Returns list of warning strings (empty if profile is valid)."""
    warnings_list: list[str] = []
    weights = profile.get("weights", {}) or {}
    missing = [c for c in WEIGHT_COMPONENTS if c not in weights]
    if missing:
        warnings_list.append(f"Profile '{name}' missing components (defaulting to 0): {missing}")

    if name == DEFAULT_PROFILE:
        for c in PERSONAL_GOAL_COMPONENTS:
            if abs(float(weights.get(c, 0))) > 0.001:
                warnings_list.append(
                    f"Profile '{name}' is the DEFAULT (academic-neutral) but "
                    f"personal-goal weight '{c}' is non-zero ({weights.get(c)}). "
                    f"This violates the design contract."
                )
    return warnings_list


# ---------------------------------------------------------------------------
# Map raw 0–5 signals to weight-component values
# ---------------------------------------------------------------------------

def derive_components(metrics: dict[str, Any], topic: dict[str, Any] | None = None) -> dict[str, float]:
    """Map raw signals from data/scores/<id>.json to the 18 weight components.

    Each component returns a 0..5 (or comparable) signal value.
    Penalties are computed as positive signals here and applied as negative
    weights at scoring time (the YAML weights for *_penalty are already
    negative).
    """
    topic = topic or {}
    paper = metrics.get("paper", {}) or {}
    sat   = metrics.get("saturation", {}) or {}
    art   = metrics.get("artifact", {}) or {}
    ven   = metrics.get("venue", {}) or {}
    risk  = metrics.get("risk", {}) or {}

    # --- citation potential (paper signals)
    citation_potential = float(metrics.get("citation_signal_0to5", 0))

    # --- topic momentum (yoy growth, recent paper count)
    yoy = float(paper.get("growth_yoy_proxy", 0))
    n12 = int(paper.get("n_papers_12mo", 0))
    momentum = 0.0
    momentum += min(2.0, max(0.0, yoy * 4))      # yoy 0.5 → 2.0
    momentum += min(2.0, n12 / 25)                # 50 papers → 2.0
    momentum += 1.0 if n12 >= 10 else 0.0
    topic_momentum = round(min(5.0, momentum), 2)

    # --- gap clarity (gap-phrase hits in abstracts)
    gap_hits = int(art.get("gap_phrase_hits", 0))
    gap_clarity = float(min(5.0, gap_hits / 2.0))

    # --- novelty (inverse of saturation)
    sat_score = int(sat.get("saturation_score_0to5", 0))
    novelty = float(max(0.0, 5 - sat_score))

    # --- saturation penalty (positive number; applied with negative weight)
    saturation_penalty = float(sat_score)

    # --- existing-work penalty (paper-direct overlap from EW module)
    # 0 if no EW data available; else signal proportional to direct paper count
    ew_paper_direct = int(metrics.get("ew_direct_paper_count", 0))
    ew_artifact_direct = int(metrics.get("ew_artifact_direct_count", 0))
    existing_work_penalty = float(min(5.0,
        ew_paper_direct * 1.5 + min(2.0, ew_artifact_direct / 8.0)
    ))

    # --- artifact value (artifact opportunity score after density penalty)
    artifact_value = float(art.get("artifact_opportunity_0to5", 0))

    # --- venue credibility (composite of venue_signal + DOAJ + crossref active)
    venue_credibility = float(ven.get("venue_signal_0to5", 0))

    # --- free publication (DOAJ no-APC count cap at 5)
    free_publication = float(min(5.0, ven.get("doaj_no_apc_journals", 0)))

    # --- publication speed (heuristic: high if no IP risk + good venue + small kept_papers)
    n_kept = int(metrics.get("kept_papers", 0))
    pub_speed = 0.0
    pub_speed += 2.0 if int(risk.get("ip_risk_0to5", 0)) == 0 else 0.0
    pub_speed += 2.0 if ven.get("venue_signal_0to5", 0) >= 2 else 0.0
    pub_speed += 1.0 if n_kept >= 10 else 0.0
    publication_speed = float(min(5.0, pub_speed))

    # --- methodological rigor (relevance purity × kept_papers heuristic)
    purity = float(metrics.get("relevance_purity", 0))
    rigor = (purity * 5.0) * min(1.0, n_kept / 25.0)
    methodological_rigor = float(min(5.0, rigor))

    # --- healthcare relevance (keyword-based; explicitly auditable)
    text = " ".join([
        str(topic.get("category", "")), str(topic.get("title", "")),
        str(topic.get("keywords", "")), str(topic.get("synonyms", "")),
    ]).lower()
    n_health = sum(1 for k in HEALTHCARE_KEYWORDS if k in text)
    healthcare_relevance = float(min(5.0, n_health * 1.5))

    # --- high-stakes relevance (broader: clinical + legal + financial + regulatory)
    n_stakes = sum(1 for k in HIGH_STAKES_KEYWORDS if k in text)
    high_stakes_relevance = float(min(5.0, n_stakes * 1.2))

    # --- niw / eb1a / faang signals (kept from existing pipeline; treated as personal goals)
    niw_value          = float(metrics.get("niw_0to5", 0))
    eb1a_value         = float(metrics.get("eb1a_0to5", 0))
    faang_career_value = float(metrics.get("career_0to5", 0))

    # --- execution feasibility (low IP risk + good venue + decent corpus)
    exec_feas = 0.0
    exec_feas += 2.0 if int(risk.get("ip_risk_0to5", 0)) <= 1 else 0.0
    exec_feas += 1.0 if n_kept >= 10 else 0.0
    exec_feas += 1.0 if ven.get("venue_signal_0to5", 0) >= 2 else 0.0
    exec_feas += 1.0 if purity >= 0.4 else 0.0
    execution_feasibility = float(min(5.0, exec_feas))

    # --- IP-risk penalty
    ip_risk_penalty = float(risk.get("ip_risk_0to5", 0))

    return {
        "citation_potential":    citation_potential,
        "topic_momentum":        topic_momentum,
        "gap_clarity":           gap_clarity,
        "novelty":               novelty,
        "saturation_penalty":    saturation_penalty,
        "existing_work_penalty": existing_work_penalty,
        "artifact_value":        artifact_value,
        "venue_credibility":     venue_credibility,
        "free_publication":      free_publication,
        "publication_speed":     publication_speed,
        "methodological_rigor":  methodological_rigor,
        "healthcare_relevance":  healthcare_relevance,
        "high_stakes_relevance": high_stakes_relevance,
        "niw_value":             niw_value,
        "eb1a_value":            eb1a_value,
        "faang_career_value":    faang_career_value,
        "execution_feasibility": execution_feasibility,
        "ip_risk_penalty":       ip_risk_penalty,
    }


# ---------------------------------------------------------------------------
# Score under profile
# ---------------------------------------------------------------------------

def score_under_profile(metrics: dict[str, Any],
                        profile: dict[str, Any],
                        topic: dict[str, Any] | None = None) -> dict[str, Any]:
    """Returns {score, components, applied_weights, modifiers}."""
    components = derive_components(metrics, topic)
    weights = profile.get("weights", {}) or {}
    modifiers = profile.get("modifiers", {}) or {}

    contributions: dict[str, float] = {}
    total = 0.0
    for c in WEIGHT_COMPONENTS:
        w = float(weights.get(c, 0))
        v = float(components.get(c, 0))
        contrib = w * v
        contributions[c] = round(contrib, 3)
        total += contrib

    # Apply modifiers (e.g., llm_eval_downweight)
    if "llm_eval_downweight" in modifiers and topic is not None:
        factor = float(modifiers["llm_eval_downweight"])
        text = " ".join([
            str(topic.get("category", "")), str(topic.get("title", "")),
            str(topic.get("keywords", "")), str(topic.get("synonyms", "")),
        ]).lower()
        n_hits = sum(1 for k in LLM_EVAL_KEYWORDS if k in text)
        if n_hits > 0:
            penalty = total * factor * min(1.0, n_hits / 3.0)
            total -= penalty
            contributions["_llm_eval_downweight"] = round(-penalty, 3)

    return {
        "score":        round(total, 3),
        "components":   components,
        "contributions": contributions,
        "applied_weights": {c: float(weights.get(c, 0)) for c in WEIGHT_COMPONENTS},
        "modifiers":    modifiers,
    }


# ---------------------------------------------------------------------------
# CLI helpers
# ---------------------------------------------------------------------------

CLI_WEIGHT_FLAGS = [
    ("--weight-citation",            "citation_potential"),
    ("--weight-topic-momentum",      "topic_momentum"),
    ("--weight-gap",                 "gap_clarity"),
    ("--weight-novelty",             "novelty"),
    ("--weight-saturation-penalty",  "saturation_penalty"),
    ("--weight-existing-work-penalty","existing_work_penalty"),
    ("--weight-artifact",            "artifact_value"),
    ("--weight-venue",               "venue_credibility"),
    ("--weight-free-publication",    "free_publication"),
    ("--weight-speed",               "publication_speed"),
    ("--weight-methodological-rigor","methodological_rigor"),
    ("--weight-healthcare",          "healthcare_relevance"),
    ("--weight-high-stakes",         "high_stakes_relevance"),
    ("--weight-niw",                 "niw_value"),
    ("--weight-eb1a",                "eb1a_value"),
    ("--weight-faang",               "faang_career_value"),
    ("--weight-execution",           "execution_feasibility"),
    ("--weight-ip-risk",             "ip_risk_penalty"),
]


def add_profile_args(parser):
    """Add --profile and all --weight-* flags to an argparse parser."""
    parser.add_argument(
        "--profile", default=DEFAULT_PROFILE,
        help=("Scoring profile name. Default: blind_citation. "
              "Supported: blind_citation, academic_long_term, artifact_neutral, "
              "healthcare_neutral, llm_eval_neutral, niw_optimized, eb1a_optimized, "
              "faang_career, balanced_personal_strategy, immigration_only, "
              "career_only, current_strategy, custom"),
    )
    for flag, _ in CLI_WEIGHT_FLAGS:
        parser.add_argument(flag, type=float, default=None,
                            help=f"Override weight for {flag.replace('--weight-', '')}")
    return parser


def resolve_profile(args, profiles: dict[str, dict] | None = None) -> tuple[str, dict[str, Any]]:
    """Resolve the active profile from CLI args.

    Returns (profile_name, profile_dict).

    For --profile custom, populate weights from --weight-* flags. Missing
    weights default to 0 with a warning.
    """
    profiles = profiles if profiles is not None else load_profiles()
    name = getattr(args, "profile", DEFAULT_PROFILE) or DEFAULT_PROFILE

    if name not in profiles:
        raise ValueError(f"Unknown profile '{name}'. Available: {list(profiles.keys())}")

    profile = dict(profiles[name])
    profile["weights"] = dict(profile.get("weights", {}))

    # CLI overrides
    overrides: dict[str, float] = {}
    for flag, key in CLI_WEIGHT_FLAGS:
        val = getattr(args, flag.replace("--", "").replace("-", "_"), None)
        if val is not None:
            overrides[key] = float(val)

    if name == "custom":
        if not overrides:
            warnings.warn("--profile custom selected but no --weight-* flags given; "
                          "all weights default to 0.")
        # Fill missing with 0 + warning
        for c in WEIGHT_COMPONENTS:
            if c not in overrides:
                profile["weights"][c] = 0.0
            else:
                profile["weights"][c] = overrides[c]
    else:
        # Apply per-flag overrides on top of named profile
        for k, v in overrides.items():
            profile["weights"][k] = v

    # Validate
    for w in validate_profile(name, profile):
        warnings.warn(w)

    return name, profile


def list_profiles() -> list[str]:
    return list(load_profiles().keys())
