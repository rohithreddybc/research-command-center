"""
13_bias_audit.py

Anti-bias audit layer for the research-topic selection pipeline.

Does NOT modify the existing pipeline. Reads scores/decisions/seeds and
recomputes rankings under multiple weighting profiles. Identifies topics
whose rank is sensitive to assumption shifts (NIW, healthcare boost,
LLM-eval anchor, artifact preference, etc.) and topics that remain
robust across profiles.

Outputs:
- data/bias_audit/seed_distribution.json
- data/bias_audit/query_audit.json
- data/bias_audit/reviewer_prompt_audit.json
- data/bias_audit/profile_rankings.csv
- data/bias_audit/rank_stability.csv
- data/bias_audit/robust_topics.json
- data/bias_audit/biased_topics.json
- data/bias_audit/negative_control_results.json
- data/topics_seed_balanced.csv
- reports/BIAS_AUDIT_REPORT.md  (written by separate function)

Usage:
    python scripts/13_bias_audit.py
    python scripts/13_bias_audit.py --profiles current_strategy,blind_citation
    python scripts/13_bias_audit.py --negative-control-only
"""
from __future__ import annotations
import argparse
import csv
import json
import math
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

CONFIG_FILE     = ROOT / "config" / "bias_profiles.yaml"
SCORES_DIR      = ROOT / "data" / "scores"
QUERIES_DIR     = ROOT / "data" / "queries"
DECISIONS_DIR   = ROOT / "data" / "decisions"
EW_DIR          = ROOT / "data" / "existing_work"
SEED_FULL       = ROOT / "data" / "topics_seed_full_75.csv"
SEED_MAIN       = ROOT / "data" / "topics_seed.csv"
LLM_PANEL_FILE  = ROOT / "scripts" / "common" / "llm_panel.py"
SCORE_FILE      = ROOT / "scripts" / "05_score_topics.py"
GENERATE_QUERY  = ROOT / "scripts" / "01_generate_queries.py"
OUT_DIR         = ROOT / "data" / "bias_audit"
OUT_DIR.mkdir(parents=True, exist_ok=True)
BALANCED_SEED   = ROOT / "data" / "topics_seed_balanced.csv"


# ---------------------------------------------------------------------------
# Minimal flat-YAML loader (no PyYAML dep) — supports nested 2-level only
# ---------------------------------------------------------------------------

def load_yaml(path: Path) -> dict[str, Any]:
    """Best-effort YAML loader for the simple structure used in bias_profiles.yaml."""
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except ImportError:
        pass
    # Hand-rolled fallback: parse the specific structure we wrote
    text = path.read_text(encoding="utf-8")
    profiles: dict[str, Any] = {}
    cur_profile: str | None = None
    cur_section: str | None = None
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        s = line.strip()
        if indent == 0 and s.endswith(":"):
            cur_profile = s[:-1].strip()
            profiles[cur_profile] = {}
            cur_section = None
        elif indent == 2 and s.endswith(":") and cur_profile:
            cur_section = s[:-1].strip()
            if cur_section in ("weights", "penalties", "signal_weights",
                               "category_filters", "downweight_keywords"):
                profiles[cur_profile][cur_section] = {}
            elif cur_section == "ignore":
                profiles[cur_profile][cur_section] = []
        elif indent == 2 and ":" in s and cur_profile:
            k, _, v = s.partition(":")
            profiles[cur_profile][k.strip()] = _yaml_value(v.strip())
            cur_section = None
        elif indent == 4 and ":" in s and cur_profile and cur_section in (
            "weights", "penalties", "signal_weights",
            "category_filters", "downweight_keywords"
        ):
            k, _, v = s.partition(":")
            profiles[cur_profile][cur_section][k.strip().strip('"')] = _yaml_value(v.strip())
        elif indent in (4, 6) and s.startswith("-") and cur_profile and cur_section == "ignore":
            profiles[cur_profile]["ignore"].append(s.lstrip("- ").strip())
    return profiles


def _yaml_value(s: str) -> Any:
    s = s.strip().strip('"').strip("'")
    if s == "true":
        return True
    if s == "false":
        return False
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1]
        return [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
    try:
        if "." in s:
            return float(s)
        return int(s)
    except ValueError:
        return s


# ---------------------------------------------------------------------------
# Load per-topic scores
# ---------------------------------------------------------------------------

def load_topic_scores() -> dict[str, dict[str, Any]]:
    """Returns {topic_id: signal_dict} merging score + ew + decision data."""
    out: dict[str, dict[str, Any]] = {}
    for f in sorted(SCORES_DIR.glob("*.json")):
        if f.name == "scores.csv":
            continue
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if "topic_id" not in d:
            continue
        tid = d["topic_id"]
        comp = d.get("rubric", {}).get("composites", {})
        sat = d.get("saturation", {})
        art = d.get("artifact", {})
        ven = d.get("venue", {})
        out[tid] = {
            "topic_id":             tid,
            "title":                d.get("topic_title", ""),
            "CitationPotential":    float(comp.get("CitationPotential", 0)),
            "ExecFeasibility":      float(comp.get("ExecFeasibility", 0)),
            "ImmigrationValue":     float(comp.get("ImmigrationValue", 0)),
            "CareerValue":          float(comp.get("CareerValue", 0)),
            "PublicationPath":      float(comp.get("PublicationPath", 0)),
            "RiskPenalty":          float(comp.get("RiskPenalty", 0)),
            "Overall":              float(comp.get("Overall", 0)),
            "citation_signal_0to5": int(d.get("citation_signal_0to5", 0)),
            "artifact_0to5":        int(art.get("artifact_opportunity_0to5", 0)),
            "saturation_0to5":      int(sat.get("saturation_score_0to5", 0)),
            "venue_signal_0to5":    int(ven.get("venue_signal_0to5", 0)),
            "niw_0to5":             int(d.get("niw_0to5", 0)),
            "eb1a_0to5":            int(d.get("eb1a_0to5", 0)),
            "career_0to5":          int(d.get("career_0to5", 0)),
            "relevance_purity":     float(d.get("relevance_purity", 0)),
            "kept_papers":          int(d.get("kept_papers", 0)),
        }
    # merge query metadata for category filtering
    for tid, sc in out.items():
        qf = QUERIES_DIR / f"{tid}.json"
        if qf.exists():
            try:
                q = json.loads(qf.read_text(encoding="utf-8"))
                sc["category"]        = q.get("topic", {}).get("category", "")
                sc["target_artifact"] = q.get("topic", {}).get("target_artifact", "")
                sc["keywords"]        = q.get("topic", {}).get("keywords", "")
                sc["synonyms"]        = q.get("topic", {}).get("synonyms", "")
            except Exception:
                pass
    return out


# ---------------------------------------------------------------------------
# Profile scoring — applies one weighting profile to all topics
# ---------------------------------------------------------------------------

HEALTHCARE_TERMS = ["clinical", "health", "medical", "patient", "ehr",
                    "guideline", "icu", "discharge", "medqa", "pubmed"]
LLM_EVAL_TERMS   = ["llm", "rag", "agent", "evaluation", "benchmark",
                    "judge", "tokeniz", "alignment", "prompt"]
ARTIFACT_TARGETS = ["dataset", "benchmark", "tool", "database", "framework"]


def _has_healthcare_signal(sc: dict) -> int:
    text = " ".join([
        str(sc.get("category", "")), str(sc.get("keywords", "")),
        str(sc.get("synonyms", "")), str(sc.get("title", "")),
    ]).lower()
    return sum(1 for t in HEALTHCARE_TERMS if t in text)


def _has_llm_eval_signal(sc: dict) -> int:
    text = " ".join([
        str(sc.get("category", "")), str(sc.get("keywords", "")),
        str(sc.get("synonyms", "")), str(sc.get("title", "")),
    ]).lower()
    return sum(1 for t in LLM_EVAL_TERMS if t in text)


def _has_artifact_target(sc: dict) -> bool:
    target = str(sc.get("target_artifact", "")).lower()
    return any(w in target for w in ARTIFACT_TARGETS)


def score_under_profile(sc: dict, profile: dict[str, Any]) -> dict[str, float]:
    """Compute one topic's score under one profile. Returns {raw, adjusted, components}."""
    weights   = profile.get("weights", {}) or {}
    penalties = profile.get("penalties", {}) or {}
    signal_w  = profile.get("signal_weights", {}) or {}
    cat_filt  = profile.get("category_filters", {}) or {}
    downwt    = profile.get("downweight_keywords", {}) or {}
    ignore    = profile.get("ignore", []) or []

    # Strip components if listed in ignore
    base = 0.0
    components: dict[str, float] = {}
    for comp, w in weights.items():
        if comp in ignore:
            continue
        v = float(sc.get(comp, 0))
        contribution = v * float(w)
        base += contribution
        components[comp] = round(contribution, 3)

    # Apply penalties (subtract)
    for comp, w in penalties.items():
        v = float(sc.get(comp, 0))
        contribution = v * float(w)
        base -= contribution
        components[f"-{comp}"] = round(-contribution, 3)

    # Apply signal_weights — these handle finer signals + bias-strip ops
    for sig, w in signal_w.items():
        if sig == "niw_healthcare_strip":
            # subtract 1.5 per healthcare keyword hit, removing the NIW boost
            n = _has_healthcare_signal(sc)
            stripped = n * 1.5 * float(w)
            base -= stripped
            components["healthcare_strip"] = round(-stripped, 3)
        elif sig == "career_llm_strip":
            n = _has_llm_eval_signal(sc)
            stripped = n * 0.6 * float(w)
            base -= stripped
            components["llm_strip"] = round(-stripped, 3)
        elif sig == "kept_papers_log":
            v = math.log1p(float(sc.get("kept_papers", 0))) * float(w)
            base += v
            components["kept_papers_log"] = round(v, 3)
        elif sig == "saturation_0to5":
            v = float(sc.get("saturation_0to5", 0)) * float(w)
            base += v
            components["saturation"] = round(v, 3)
        else:
            v = float(sc.get(sig, 0)) * float(w)
            base += v
            components[sig] = round(v, 3)

    # Category filters — neutralize boosts that are baked into the score
    if cat_filt.get("healthcare_neutral"):
        # If healthcare boost wasn't already stripped, strip it from immig now
        if "ImmigrationValue" in weights and "healthcare_strip" not in components:
            n = _has_healthcare_signal(sc)
            adj = n * 1.5 * float(weights.get("ImmigrationValue", 0)) * 0.5  # 50% strip
            base -= adj
            components["hc_neutral_adj"] = round(-adj, 3)
    if cat_filt.get("artifact_neutral"):
        # Strip the +1.0 EB-1A artifact boost from ImmigrationValue
        if "ImmigrationValue" in weights and _has_artifact_target(sc):
            adj = 1.0 * 1.5 * float(weights.get("ImmigrationValue", 0))
            base -= adj
            components["artifact_neutral_adj"] = round(-adj, 3)
    if cat_filt.get("llm_eval_neutral") and "career_llm_strip" not in components:
        if "CareerValue" in weights:
            n = _has_llm_eval_signal(sc)
            adj = n * 0.6 * float(weights.get("CareerValue", 0))
            base -= adj
            components["llm_neutral_adj"] = round(-adj, 3)

    # Keyword downweighting
    if downwt:
        text = (str(sc.get("title", "")) + " " + str(sc.get("keywords", ""))).lower()
        for kw, factor in downwt.items():
            if kw in text:
                base *= float(factor)
                components[f"downwt_{kw}"] = round(float(factor), 3)

    return {"score": round(base, 3), "components": components}


def rank_topics(scores: dict[str, dict], profile: dict[str, Any]) -> list[dict]:
    rows = []
    for tid, sc in scores.items():
        out = score_under_profile(sc, profile)
        rows.append({
            "topic_id":   tid,
            "title":      sc.get("title", ""),
            "category":   sc.get("category", ""),
            "score":      out["score"],
            "components": out["components"],
            "is_healthcare":  _has_healthcare_signal(sc) > 0,
            "is_llm_eval":    _has_llm_eval_signal(sc) > 0,
            "is_artifact":    _has_artifact_target(sc),
        })
    rows.sort(key=lambda r: r["score"], reverse=True)
    for i, r in enumerate(rows, 1):
        r["rank"] = i
    return rows


# ---------------------------------------------------------------------------
# 1. Seed-topic distribution audit
# ---------------------------------------------------------------------------

def audit_seed_distribution() -> dict[str, Any]:
    out: dict[str, Any] = {}
    for label, path in [("main_seed", SEED_MAIN), ("full_seed", SEED_FULL)]:
        if not path.exists():
            out[label] = {"error": "missing"}
            continue
        rows = list(csv.DictReader(path.open(encoding="utf-8")))
        cats = Counter(r.get("category", "?") for r in rows)
        kw_all: list[str] = []
        for r in rows:
            for k in r.get("keywords", "").lower().replace("|", ";").split(";"):
                k = k.strip()
                if k:
                    kw_all.append(k)
        kw_counter = Counter(kw_all)

        # Count category bias dimensions
        n_health = sum(1 for r in rows if "health" in r.get("category", "").lower()
                       or "clinical" in r.get("category", "").lower())
        n_eval   = sum(1 for r in rows if any(w in r.get("category", "").lower()
                                              for w in ["eval", "llm", "judge"]))
        n_eval_kw = sum(1 for r in rows if any(w in r.get("keywords", "").lower()
                                                for w in ["llm judge", "llm-as-a-judge", "evaluation",
                                                          "benchmark"]))
        n_artifact = sum(1 for r in rows if any(w in r.get("target_artifact", "").lower()
                                                 for w in ARTIFACT_TARGETS))

        out[label] = {
            "n_topics":                   len(rows),
            "categories":                 dict(cats.most_common()),
            "top_keywords":               dict(kw_counter.most_common(20)),
            "healthcare_tagged":          n_health,
            "healthcare_pct":             round(100 * n_health / max(1, len(rows)), 1),
            "eval_category_tagged":       n_eval,
            "eval_category_pct":          round(100 * n_eval / max(1, len(rows)), 1),
            "eval_keyword_tagged":        n_eval_kw,
            "artifact_target_tagged":     n_artifact,
            "artifact_target_pct":        round(100 * n_artifact / max(1, len(rows)), 1),
        }
    return out


# ---------------------------------------------------------------------------
# 2. Query-generation bias audit — read 01_generate_queries.py
# ---------------------------------------------------------------------------

def audit_query_generation() -> dict[str, Any]:
    """Inspect the actual query-generation code AND the generated queries."""
    code = GENERATE_QUERY.read_text(encoding="utf-8") if GENERATE_QUERY.exists() else ""

    findings: list[dict[str, Any]] = []

    # Detect AXIS_TERMS — words always added to every query
    if "AXIS_TERMS" in code:
        m = re.search(r"AXIS_TERMS\s*=\s*\[(.*?)\]", code, re.DOTALL)
        if m:
            terms = re.findall(r'"([^"]+)"', m.group(1))
            findings.append({
                "issue":    "axis_terms_baked_in",
                "evidence": f"AXIS_TERMS = {terms}",
                "severity": "MEDIUM",
                "explanation": ("Every topic is implicitly framed against this fixed axis list. "
                                "If the topic isn't a benchmark/eval/repro paper, the search "
                                "still steers toward those framings."),
            })

    # Detect auto-appended axis words in paired queries
    if 'paired.append(f"{k} ' in code or '"benchmark", "evaluation", "robustness", "reproducibility"' in code:
        findings.append({
            "issue":    "auto_appended_benchmark_evaluation",
            "evidence": ('paired.append(f"{k} {axis}") with axis in '
                         '["benchmark","evaluation","robustness","reproducibility"]'),
            "severity": "HIGH",
            "explanation": ("Top-3 keywords × 4 axis terms = 12 forced 'X benchmark', "
                            "'X evaluation', 'X robustness', 'X reproducibility' searches "
                            "per topic. This biases retrieval toward benchmark/eval framings "
                            "regardless of whether the topic is genuinely about a benchmark."),
        })

    # Detect GitHub query bias
    if "benchmark in:name,description" in code:
        findings.append({
            "issue":    "github_queries_assume_benchmark",
            "evidence": '"{k} benchmark in:name,description"',
            "severity": "MEDIUM",
            "explanation": ("GitHub search auto-appends 'benchmark' and 'evaluation'. "
                            "Repos that aren't benchmarks won't surface even when relevant."),
        })

    # Sample actual generated queries — count axis-term contamination
    sample_axis_count = 0
    sample_total      = 0
    sample_topics: list[str] = []
    for qf in QUERIES_DIR.glob("*.json"):
        try:
            q = json.loads(qf.read_text(encoding="utf-8"))
        except Exception:
            continue
        sample_topics.append(qf.stem)
        for src in ("semantic_scholar", "openalex", "github", "huggingface"):
            for query in q.get("queries", {}).get(src, []) or []:
                sample_total += 1
                qs = str(query).lower()
                if any(t in qs for t in ["benchmark", "evaluation", "reproducibility", "robustness"]):
                    sample_axis_count += 1

    findings.append({
        "issue":    "axis_term_contamination_in_actual_queries",
        "evidence": (f"{sample_axis_count}/{sample_total} ({100*sample_axis_count/max(1,sample_total):.1f}%) "
                     f"of queries across {len(sample_topics)} topics contain "
                     f"benchmark/evaluation/reproducibility/robustness"),
            "severity": "HIGH" if sample_axis_count / max(1, sample_total) > 0.40 else "MEDIUM",
            "explanation": ("This is the empirical impact of the axis-term injection. If above 40%, "
                            "evidence retrieval is systematically biased toward benchmark/eval papers."),
    })

    return {
        "code_inspected": str(GENERATE_QUERY),
        "findings":       findings,
        "n_queries_sampled": sample_total,
        "n_topics_sampled":  len(sample_topics),
    }


# ---------------------------------------------------------------------------
# 3. Reviewer prompt audit — read llm_panel.py
# ---------------------------------------------------------------------------

def audit_reviewer_prompts() -> dict[str, Any]:
    code = LLM_PANEL_FILE.read_text(encoding="utf-8") if LLM_PANEL_FILE.exists() else ""
    findings: list[dict[str, Any]] = []

    # Detect explicit immigration / FAANG framings
    if '"niw_eb1a"' in code or '"role": "niw_eb1a"' in code:
        findings.append({
            "issue":    "explicit_immigration_reviewer_role",
            "evidence": '{"role": "niw_eb1a", "focus": "Does this build NIW prong-2/3 evidence ..."}',
            "severity": "HIGH",
            "explanation": ("One of 8 reviewers is explicitly framed around NIW/EB-1A immigration "
                            "evidence. This contributes 1/8 = 12.5% of reviewer plurality voting "
                            "with an immigration-biased lens. Healthcare/clinical topics will get "
                            "systematic upvotes from this reviewer."),
        })
    if '"career_faang"' in code:
        findings.append({
            "issue":    "explicit_faang_reviewer_role",
            "evidence": '{"role": "career_faang", "focus": "high-paying ML/data-science roles"}',
            "severity": "HIGH",
            "explanation": ("One of 8 reviewers explicitly framed around FAANG hiring. LLM/eval "
                            "topics will get systematic upvotes; healthcare/clinical will be "
                            "downvoted by this reviewer regardless of academic merit."),
        })

    # Detect rubric prompts
    n_reviewers = code.count('"role":')
    findings.append({
        "issue": "reviewer_count_and_balance",
        "evidence": f"{n_reviewers} reviewer roles defined in REVIEWER_ROLES",
        "severity": "INFO",
        "explanation": ("8 reviewers means each has 12.5% voting weight on plurality. "
                        "If 2 are explicitly biased (niw_eb1a, career_faang), 25% of the "
                        "panel's vote is structurally non-neutral."),
    })

    # Check SYSTEM_PROMPT for neutrality cues
    if "Use ONLY the evidence packet" in code:
        findings.append({
            "issue":    "system_prompt_has_evidence_only_clause",
            "evidence": '"Use ONLY the evidence packet provided. Do NOT use any prior knowledge..."',
            "severity": "INFO",
            "explanation": ("Mitigation present: the system prompt forces evidence-only "
                            "reasoning. But the per-role focus strings still inject bias "
                            "(see niw_eb1a and career_faang above)."),
        })

    # Check for anchor language
    anchor_terms = ["NIW", "EB-1A", "FAANG", "high-paying", "immigration"]
    found_anchors = [t for t in anchor_terms if t in code]
    if found_anchors:
        findings.append({
            "issue":    "anchor_language_in_prompts",
            "evidence": f"Found anchor terms: {found_anchors}",
            "severity": "MEDIUM",
            "explanation": ("These terms in reviewer prompts prime the model toward "
                            "user-specific career/immigration objectives rather than "
                            "academic merit."),
        })

    return {
        "code_inspected": str(LLM_PANEL_FILE),
        "n_reviewers":    n_reviewers,
        "findings":       findings,
    }


# ---------------------------------------------------------------------------
# 4. Profile recomputation + rank stability
# ---------------------------------------------------------------------------

def run_profile_audit(profiles: dict[str, dict]) -> tuple[dict, list[dict], list[dict]]:
    scores = load_topic_scores()
    if not scores:
        return {}, [], []

    profile_rankings: dict[str, list[dict]] = {}
    for prof_name, prof_def in profiles.items():
        ranking = rank_topics(scores, prof_def)
        profile_rankings[prof_name] = ranking

    # Build cross-profile rank table
    all_topics = sorted(scores.keys())
    table_rows = []
    for tid in all_topics:
        row: dict[str, Any] = {"topic_id": tid, "title": scores[tid].get("title", "")}
        for prof_name, ranking in profile_rankings.items():
            for r in ranking:
                if r["topic_id"] == tid:
                    row[f"rank_{prof_name}"]  = r["rank"]
                    row[f"score_{prof_name}"] = r["score"]
                    break
        # Compute rank-stability stats
        ranks = [v for k, v in row.items() if k.startswith("rank_")]
        if ranks:
            row["rank_min"] = min(ranks)
            row["rank_max"] = max(ranks)
            row["rank_range"] = max(ranks) - min(ranks)
            row["rank_mean"] = round(sum(ranks) / len(ranks), 2)
        table_rows.append(row)
    table_rows.sort(key=lambda r: r.get("rank_mean", 99))

    # Identify robust vs biased topics
    robust = [r for r in table_rows
              if r.get("rank_max", 99) <= 6 and r.get("rank_range", 99) <= 4]
    biased = [r for r in table_rows
              if r.get("rank_range", 0) >= 6]

    return profile_rankings, table_rows, {"robust": robust, "biased": biased}


# ---------------------------------------------------------------------------
# 5. Negative-control test — synthetic topics that should rank LOW
# ---------------------------------------------------------------------------

NEGATIVE_CONTROL_TOPICS = [
    {"topic_id": "NC01", "title": "Machine learning for healthcare",
     "category": "healthcare", "keywords": "machine learning|healthcare",
     "synonyms": "ml medicine", "target_artifact": "paper", "type": "vague_broad"},
    {"topic_id": "NC02", "title": "AI in finance",
     "category": "applied", "keywords": "AI|finance",
     "synonyms": "fintech", "target_artifact": "paper", "type": "vague_broad"},
    {"topic_id": "NC03", "title": "LLMs for education",
     "category": "applied", "keywords": "LLM|education",
     "synonyms": "edtech", "target_artifact": "paper", "type": "vague_broad"},
    {"topic_id": "NC04", "title": "Data science dashboards",
     "category": "applied", "keywords": "data science|dashboard",
     "synonyms": "BI", "target_artifact": "tool", "type": "implementation_only"},
    {"topic_id": "NC05", "title": "AI for business analytics",
     "category": "applied", "keywords": "AI|business analytics",
     "synonyms": "BI", "target_artifact": "framework", "type": "vague_broad"},
    {"topic_id": "NC06", "title": "Predictive modeling in healthcare",
     "category": "healthcare", "keywords": "predictive|healthcare",
     "synonyms": "risk score", "target_artifact": "paper", "type": "vague_broad"},
    {"topic_id": "NC07", "title": "RAG for question answering",
     "category": "rag", "keywords": "RAG|question answering",
     "synonyms": "retrieval QA", "target_artifact": "framework", "type": "saturated_generic"},
]


def negative_control_test(profiles: dict[str, dict]) -> dict[str, Any]:
    """Score the negative-control topics under each profile.

    These are intentionally vague/saturated/un-novel topics. A working scoring
    system should rank them at the BOTTOM. If any rank in the top half, the
    scoring system is too generous to broad framings.
    """
    # Build synthetic signal records — assume neutral signals (no corpus to score)
    nc_scores: dict[str, dict] = {}
    for t in NEGATIVE_CONTROL_TOPICS:
        # Synthetic signals chosen to mirror what the pipeline would assign:
        # - vague broad topics get HIGH NIW (healthcare keyword) + HIGH career (LLM keyword)
        #   even though they have no real contribution. This is the test.
        text = " ".join(str(v) for v in t.values()).lower()
        is_health = any(k in text for k in HEALTHCARE_TERMS)
        is_llm    = any(k in text for k in LLM_EVAL_TERMS)
        is_art    = any(k in t.get("target_artifact", "").lower() for k in ARTIFACT_TARGETS)
        nc_scores[t["topic_id"]] = {
            "topic_id":             t["topic_id"],
            "title":                t["title"],
            "category":             t["category"],
            "keywords":             t["keywords"],
            "synonyms":             t["synonyms"],
            "target_artifact":      t["target_artifact"],
            # Pretend the pipeline ran on these — give them median signals
            "CitationPotential":    8.0,    # mid
            "ExecFeasibility":      6.0,
            "ImmigrationValue":     14.0 if is_health else 8.0,   # health auto-boost via NIW
            "CareerValue":          10.0 if is_llm else 6.0,      # LLM auto-boost
            "PublicationPath":      4.0,
            "RiskPenalty":          5.0,
            "Overall":              0,
            "citation_signal_0to5": 2,
            "artifact_0to5":        3 if is_art else 2,
            "saturation_0to5":      4,                             # all are saturated
            "venue_signal_0to5":    2,
            "niw_0to5":             5 if is_health else 2,
            "eb1a_0to5":            3,
            "career_0to5":          4 if is_llm else 2,
            "relevance_purity":     0.20,                          # vague topics → low purity
            "kept_papers":          5,
        }

    out: dict[str, Any] = {"profiles": {}}
    real_scores = load_topic_scores()
    for prof_name, prof_def in profiles.items():
        nc_ranks: list[dict] = []
        for tid, sc in nc_scores.items():
            res = score_under_profile(sc, prof_def)
            nc_ranks.append({
                "topic_id":  tid,
                "title":     sc["title"],
                "type":      next((t["type"] for t in NEGATIVE_CONTROL_TOPICS
                                  if t["topic_id"] == tid), ""),
                "score":     res["score"],
            })
        # Compare to REAL topics under same profile
        real_ranks = rank_topics(real_scores, prof_def)
        real_scores_only = [r["score"] for r in real_ranks]
        if not real_scores_only:
            continue
        median_real = sorted(real_scores_only)[len(real_scores_only) // 2]
        max_real    = max(real_scores_only)
        min_real    = min(real_scores_only)
        nc_ranks.sort(key=lambda r: r["score"], reverse=True)

        # Verdict per NC topic
        verdicts: list[dict[str, Any]] = []
        for nc in nc_ranks:
            if nc["score"] >= median_real:
                verdict = "FAIL_above_real_median"
            elif nc["score"] >= min_real:
                verdict = "WEAK_within_real_range"
            else:
                verdict = "PASS_below_real_range"
            verdicts.append({**nc, "verdict": verdict})
        n_fail = sum(1 for v in verdicts if v["verdict"] == "FAIL_above_real_median")
        out["profiles"][prof_name] = {
            "negative_controls": verdicts,
            "real_min":          round(min_real, 2),
            "real_median":       round(median_real, 2),
            "real_max":          round(max_real, 2),
            "n_fail":            n_fail,
            "verdict":           ("LEAKY" if n_fail >= 3
                                  else "BORDERLINE" if n_fail >= 1
                                  else "TIGHT"),
        }
    return out


# ---------------------------------------------------------------------------
# 6. Balanced seed generation
# ---------------------------------------------------------------------------

def generate_balanced_seed() -> dict[str, Any]:
    """Build data/topics_seed_balanced.csv with broader category coverage.

    Strategy:
    - Cap healthcare/clinical at 15% of total
    - Cap LLM-judge keyword at 5% of total
    - Add topics from underrepresented categories
    - Include negative-control topics labeled as such for sanity testing
    """
    balanced: list[dict[str, Any]] = []

    # Selected from existing full seed (drop healthcare-overconcentration)
    existing = list(csv.DictReader(SEED_FULL.open(encoding="utf-8"))) if SEED_FULL.exists() else []
    existing_by_cat: dict[str, list[dict]] = defaultdict(list)
    for r in existing:
        existing_by_cat[r.get("category", "?")].append(r)

    # Cap healthcare-tagged at max 5 topics; favor non-healthcare from existing
    nonhealth = [r for r in existing
                 if "health" not in r.get("category", "").lower()
                 and "clinical" not in r.get("category", "").lower()]
    healthlist = [r for r in existing
                  if "health" in r.get("category", "").lower()
                  or "clinical" in r.get("category", "").lower()]

    # Add diverse new topics in categories that are under-represented
    new_topics = [
        # AI agents
        {"topic_id": "B01", "title": "Tool-calling reliability benchmark for autonomous agents",
         "category": "agents", "keywords": "tool calling|reliability|autonomous agents",
         "synonyms": "function calling;agent benchmark", "negative_keywords": "robotics",
         "target_artifact": "benchmark", "prelim_priority": "4"},
        {"topic_id": "B02", "title": "Long-horizon agent planning failure modes",
         "category": "agents", "keywords": "long-horizon planning|agent failure|task decomposition",
         "synonyms": "multi-step agent;planner errors", "negative_keywords": "robotics",
         "target_artifact": "paper", "prelim_priority": "3"},
        # Data-centric AI
        {"topic_id": "B03", "title": "Data-centric AI: dataset auditing methodology",
         "category": "data-centric", "keywords": "dataset audit|data quality|data-centric",
         "synonyms": "data cards;datasheet", "negative_keywords": "image only",
         "target_artifact": "framework", "prelim_priority": "4"},
        # Causal inference
        {"topic_id": "B04", "title": "Causal inference benchmarks for ML evaluation",
         "category": "causal", "keywords": "causal inference|benchmark|ATE estimation",
         "synonyms": "causal benchmark;treatment effect", "negative_keywords": "epidemiology only",
         "target_artifact": "benchmark", "prelim_priority": "4"},
        # Synthetic data
        {"topic_id": "B05", "title": "Synthetic data quality evaluation metrics",
         "category": "data-centric", "keywords": "synthetic data|quality evaluation|fidelity",
         "synonyms": "data synthesis;tabular synthesis", "negative_keywords": "image only",
         "target_artifact": "framework", "prelim_priority": "4"},
        # Benchmark contamination
        {"topic_id": "B06", "title": "Cross-task contamination in foundation model benchmarks",
         "category": "eval", "keywords": "benchmark contamination|data leakage|test set overlap",
         "synonyms": "training-test overlap", "negative_keywords": "drug docking",
         "target_artifact": "paper", "prelim_priority": "4"},
        # ML systems
        {"topic_id": "B07", "title": "ML serving system latency-quality tradeoff benchmark",
         "category": "ml-systems", "keywords": "ML serving|latency|quality tradeoff",
         "synonyms": "model serving;production ML", "negative_keywords": "training only",
         "target_artifact": "benchmark", "prelim_priority": "3"},
        # Public health informatics
        {"topic_id": "B08", "title": "Public health informatics: outbreak signal detection",
         "category": "public-health", "keywords": "outbreak detection|public health|surveillance",
         "synonyms": "syndromic surveillance", "negative_keywords": "individual diagnosis",
         "target_artifact": "framework", "prelim_priority": "3"},
        # Human-AI decision support
        {"topic_id": "B09", "title": "Human-AI decision support: confidence calibration in interfaces",
         "category": "hci", "keywords": "human-AI|decision support|confidence calibration",
         "synonyms": "AI explanations;decision aid", "negative_keywords": "robotics",
         "target_artifact": "paper", "prelim_priority": "3"},
        # Responsible AI / fairness
        {"topic_id": "B10", "title": "Responsible AI: counterfactual fairness audit toolkit",
         "category": "fairness", "keywords": "counterfactual fairness|audit|bias",
         "synonyms": "algorithmic fairness", "negative_keywords": "philosophy only",
         "target_artifact": "tool", "prelim_priority": "4"},
        # Model monitoring
        {"topic_id": "B11", "title": "Distribution-shift detection methods for production ML",
         "category": "ml-systems", "keywords": "distribution shift|monitoring|production ML",
         "synonyms": "drift detection;data drift", "negative_keywords": "anomaly only",
         "target_artifact": "framework", "prelim_priority": "4"},
        # NLP eval (one only — capped)
        {"topic_id": "B12", "title": "Multi-lingual factuality benchmark for low-resource languages",
         "category": "eval", "keywords": "multilingual|factuality|low-resource",
         "synonyms": "low-resource NLP", "negative_keywords": "translation only",
         "target_artifact": "benchmark", "prelim_priority": "4"},
        # Scientific literature mining
        {"topic_id": "B13", "title": "Citation-context mining for scientific literature",
         "category": "litmining", "keywords": "citation context|literature mining|scholarly NLP",
         "synonyms": "scientific NLP", "negative_keywords": "patents",
         "target_artifact": "dataset", "prelim_priority": "3"},
        # AI safety
        {"topic_id": "B14", "title": "Refusal behavior consistency across LLM updates",
         "category": "safety", "keywords": "refusal|safety|model updates",
         "synonyms": "alignment drift", "negative_keywords": "general red teaming",
         "target_artifact": "paper", "prelim_priority": "4"},
        # Healthcare (capped at 3 not 30)
        {"topic_id": "B15", "title": "Clinical decision support: alert fatigue measurement",
         "category": "healthcare", "keywords": "alert fatigue|clinical decision support",
         "synonyms": "CDS;clinical workflow", "negative_keywords": "general usability",
         "target_artifact": "paper", "prelim_priority": "3"},
        {"topic_id": "B16", "title": "Reproducibility in healthcare AI deployment studies",
         "category": "healthcare+meta", "keywords": "healthcare AI|deployment|reproducibility",
         "synonyms": "real-world ML", "negative_keywords": "drug docking",
         "target_artifact": "database", "prelim_priority": "4"},
        # Reproducibility (broad)
        {"topic_id": "B17", "title": "Reproducibility of LLM training: hyperparameter sensitivity",
         "category": "methodology", "keywords": "training reproducibility|hyperparameter|seed sensitivity",
         "synonyms": "ML reproducibility", "negative_keywords": "tutorial",
         "target_artifact": "paper", "prelim_priority": "4"},
    ]
    balanced.extend(new_topics)

    # Add a small selection of existing non-healthcare topics for continuity
    seen_titles = {t["title"] for t in balanced}
    diverse_existing = []
    for r in nonhealth:
        if r["title"] not in seen_titles and len(diverse_existing) < 10:
            diverse_existing.append(r)
    balanced.extend(diverse_existing)

    # Add 2 healthcare topics for representation (not 30)
    balanced.extend(healthlist[:2])

    # Tag negative controls (for testing)
    for nc in NEGATIVE_CONTROL_TOPICS:
        balanced.append({
            "topic_id":          nc["topic_id"] + "_NC",
            "title":             nc["title"] + " [NEGATIVE_CONTROL]",
            "category":          nc["category"],
            "keywords":          nc["keywords"],
            "synonyms":          nc["synonyms"],
            "negative_keywords": "",
            "target_artifact":   nc["target_artifact"],
            "prelim_priority":   "1",
        })

    # Write CSV
    fields = ["topic_id", "title", "category", "keywords", "synonyms",
              "negative_keywords", "target_artifact", "prelim_priority"]
    with BALANCED_SEED.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in balanced:
            w.writerow({k: row.get(k, "") for k in fields})

    cats = Counter(r.get("category", "?") for r in balanced)
    return {
        "path":            str(BALANCED_SEED),
        "n_topics":        len(balanced),
        "categories":      dict(cats.most_common()),
        "n_healthcare":    sum(1 for r in balanced
                              if "health" in r.get("category", "").lower()
                              or "clinical" in r.get("category", "").lower()),
        "n_llm_eval":      sum(1 for r in balanced
                              if any(w in r.get("category", "").lower()
                                     for w in ["eval", "llm"])),
        "n_negative_control": sum(1 for r in balanced if "_NC" in r.get("topic_id", "")),
    }


# ---------------------------------------------------------------------------
# 7. Write CSV / JSON outputs
# ---------------------------------------------------------------------------

def write_outputs(seed_audit, query_audit, prompt_audit,
                  profile_rankings, rank_table, robust_biased,
                  negative_control, balanced_info) -> None:
    (OUT_DIR / "seed_distribution.json").write_text(
        json.dumps(seed_audit, indent=2), encoding="utf-8")
    (OUT_DIR / "query_audit.json").write_text(
        json.dumps(query_audit, indent=2), encoding="utf-8")
    (OUT_DIR / "reviewer_prompt_audit.json").write_text(
        json.dumps(prompt_audit, indent=2), encoding="utf-8")
    (OUT_DIR / "negative_control_results.json").write_text(
        json.dumps(negative_control, indent=2), encoding="utf-8")
    (OUT_DIR / "balanced_seed_info.json").write_text(
        json.dumps(balanced_info, indent=2), encoding="utf-8")
    (OUT_DIR / "robust_topics.json").write_text(
        json.dumps(robust_biased.get("robust", []), indent=2), encoding="utf-8")
    (OUT_DIR / "biased_topics.json").write_text(
        json.dumps(robust_biased.get("biased", []), indent=2), encoding="utf-8")

    # profile_rankings.csv: one row per topic, one column per profile
    if rank_table:
        with (OUT_DIR / "profile_rankings.csv").open("w", newline="", encoding="utf-8") as f:
            fields = list(rank_table[0].keys())
            w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            for r in rank_table:
                w.writerow({k: r.get(k, "") for k in fields})

    # rank_stability.csv: condensed view
    if rank_table:
        with (OUT_DIR / "rank_stability.csv").open("w", newline="", encoding="utf-8") as f:
            fields = ["topic_id", "title", "rank_min", "rank_max",
                      "rank_range", "rank_mean"]
            w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
            w.writeheader()
            for r in rank_table:
                w.writerow({k: r.get(k, "") for k in fields})

    # Per-profile top-10 dumps for the report
    for prof_name, ranking in profile_rankings.items():
        (OUT_DIR / f"top10_{prof_name}.json").write_text(
            json.dumps(ranking[:10], indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profiles", default=None,
                    help="Comma-separated profile names; default = all")
    ap.add_argument("--negative-control-only", action="store_true")
    args = ap.parse_args(argv)

    profiles = load_yaml(CONFIG_FILE)
    if args.profiles:
        wanted = set(args.profiles.split(","))
        profiles = {k: v for k, v in profiles.items() if k in wanted}

    print(f"[13_bias_audit] Loaded {len(profiles)} profile(s): {list(profiles.keys())}")

    if args.negative_control_only:
        nc = negative_control_test(profiles)
        print(json.dumps(nc, indent=2))
        return 0

    print("[13_bias_audit] 1/6 Auditing seed distribution...")
    seed_audit = audit_seed_distribution()

    print("[13_bias_audit] 2/6 Auditing query generation...")
    query_audit = audit_query_generation()

    print("[13_bias_audit] 3/6 Auditing reviewer prompts...")
    prompt_audit = audit_reviewer_prompts()

    print("[13_bias_audit] 4/6 Recomputing rankings under all profiles...")
    profile_rankings, rank_table, robust_biased = run_profile_audit(profiles)

    print("[13_bias_audit] 5/6 Running negative-control test...")
    negative_control = negative_control_test(profiles)

    print("[13_bias_audit] 6/6 Generating balanced seed...")
    balanced_info = generate_balanced_seed()

    print("[13_bias_audit] Writing outputs...")
    write_outputs(seed_audit, query_audit, prompt_audit,
                  profile_rankings, rank_table, robust_biased,
                  negative_control, balanced_info)

    print(f"[13_bias_audit] Done. Outputs in {OUT_DIR}")
    print(f"  - {len(rank_table)} topics scored across {len(profile_rankings)} profiles")
    print(f"  - {len(robust_biased.get('robust', []))} robust topics, "
          f"{len(robust_biased.get('biased', []))} bias-sensitive topics")
    print(f"  - balanced seed: {balanced_info.get('n_topics')} topics -> "
          f"{BALANCED_SEED}")
    print(f"  - Next: run scripts/13_bias_audit.py write-report (or call write_bias_report)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
