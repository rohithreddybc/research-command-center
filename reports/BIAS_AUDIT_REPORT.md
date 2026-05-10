# Bias Audit Report
*Generated: 2026-05-10 by `scripts/13_bias_audit.py`*
*Mode: read-only audit over existing pipeline outputs (no LLM re-run)*

---

## POST-TIER-1-FIX VERIFICATION (added 2026-05-10)

The Tier 1 architecture fixes from §K have been implemented in commit (this
commit). The audit was rerun against the fixed codebase. Key verifications:

| Tier-1 Item | Implemented | Verification |
|---|---|---|
| Default reviewer panel academically neutral (8 roles) | ✅ | `scripts/common/llm_panel.py` `NEUTRAL_REVIEWER_ROLES`; `niw_eb1a` and `career_faang` removed from default. Test `TestNeutralReviewerPanel.test_default_panel_excludes_personal_goal_reviewers` passes. |
| `--include-personal-goals` adds personal-goal reviewers | ✅ | `scripts/06_llm_review_topics.py --include-personal-goals` flag wired. Test `test_include_personal_goals_adds_them` passes. |
| Default scoring profile = `blind_citation` | ✅ | `scripts/common/profiles.py` `DEFAULT_PROFILE = "blind_citation"`; `05_score_topics.py` and `08_confidence_gate.py` both use this default. Test `test_default_profile_is_blind_citation` passes. |
| Personal-goal weights = 0 in `blind_citation` | ✅ | `config/weight_profiles.yaml` `blind_citation` block has `niw_value=0, eb1a_value=0, faang_career_value=0, healthcare_relevance=0, high_stakes_relevance=0, free_publication=0, publication_speed=0`. Test `test_blind_citation_zeros_personal_goals` passes. |
| Forced query-axis injection removed | ✅ | `scripts/01_generate_queries.py:_conditional_axis_terms()` returns `[]` for `target_artifact='paper'` or empty. Tests `test_paper_target_gets_no_axis_injection` and `test_benchmark_target_gets_benchmark_axis` pass. |
| Seed keyword cap warning | ✅ | `scripts/common/seed_audit.py` (KEYWORD_CAP=3); writes `reports/seed_bias_warnings.md`. Test `test_keyword_cap_warning_fires` passes. |
| Negative-control sentinel blocks GO | ✅ | `scripts/08_confidence_gate.py:_negative_control_sentinel()` reads `data/bias_audit/negative_control_results.json`; sets `negative_control_blocked_go=True` if active profile is in `leaky_profiles`. Test `test_nc_top_half_blocks_go` passes. |
| Personal-goal-only weak topic flag | ✅ | `08_confidence_gate.py` checks `bc_acceptable` against blind_citation gate; sets `personal_goal_only_weak_topic=True` and prepends `PERSONAL_GOAL_ONLY_WEAK_TOPIC` reason. Tests `test_personal_goal_only_warning` and `test_blind_citation_failure_blocks_go` pass. |

### Post-fix top-5 ranking shift (validates the fix)

Under the new default profile `blind_citation`:

| Old rank (current_strategy) | New rank (blind_citation) | Topic |
|---|---|---|
| #1 | **#9** | T11 (Format sensitivity benchmark) — was the previous favorite; correctly demoted because it relied on artifact-target boost + LLM-eval anchoring |
| #2 | #5 | T74_N1 — drops slightly; honest given thin corpus |
| #6 | **#10** | T07 (Judge prompt injection) — drops because LLM-eval anchor is removed |
| not in top-5 | **#1** | T10 — paper-merit driven; *but* `go_blocked=True` from existing-work overlap, so cannot become GO |
| not in top-5 | #2 | T43 — most cross-profile-stable topic now correctly recognised |

### Post-fix negative-control sentinel result

All 12 real profiles return `verdict=TIGHT` (no NC topic in top half).
The sole `LEAKY` verdict is the `custom` profile because its weights
default to 0 — this is by design (warns user that custom requires
explicit weights).

### Outstanding (not Tier 1)

- Seed-bias warning still fires for `topics_seed_full_75.csv` and
  `topics_seed_balanced.csv` (`llm judge` × 9). These are warnings,
  not errors. Reduce by curating the seeds before next pipeline run.
- The Tier-2 fixes (decouple NIW from healthcare keywords, decouple
  Career from LLM keywords, decouple EB-1A from artifact-type strings)
  are NOT yet implemented. The keyword-based scoring in
  `05_score_topics.py:niw_score(), career_score(), eb1a_score()` still
  uses the original heuristics. The new `weight_profiles.yaml` system
  *applies different weights* to those signals, but the underlying 0–5
  signals themselves are unchanged.

### Recommended next steps

1. Decide whether to curate the balanced seed further to drop `llm judge`
   to ≤ 3 occurrences before the next pipeline run.
2. With Tier 1 in place, the system is now safe to run `06_llm_review_topics`
   on the balanced seed under the default `blind_citation` profile.
3. After that re-run, regenerate `BIAS_AUDIT_REPORT.md` and `GO_READINESS_DOSSIERS.md`
   based on the new neutral evidence.

---

## A. Executive Summary

**Verdict: NEEDS MAJOR REDESIGN.** The current pipeline's top-ranked topics
are not robust to assumption changes. Across 8 weighting profiles, **0 of 14
topics remain in the top 6 in every profile**, and the four candidates from
the GO Readiness Dossiers all swing by **8–12 ranks** depending on which
biases are present.

**Concrete evidence of bias amplification:**

1. **Seed bias**: 33% of the 75-topic seed file is healthcare-tagged; the
   single most common keyword is `llm judge` (9 occurrences) — 4× the next
   most common.
2. **Query bias**: 60.7% of all generated search queries contain
   `benchmark/evaluation/reproducibility/robustness`. Every topic gets these
   axis terms forcibly appended regardless of whether the contribution is
   actually a benchmark.
3. **Scoring bias**: ImmigrationValue gets 20% explicit weight in the Overall
   formula. The NIW score function awards +1.5 per healthcare-keyword hit;
   the Career score function rewards +0.6 per LLM-keyword hit and penalizes
   −0.6 for healthcare. EB-1A awards +1.0 for dataset/benchmark/tool target
   artifacts. These are not academic merit signals.
4. **Reviewer bias**: 2 of 8 reviewer roles (`niw_eb1a`, `career_faang`) are
   structurally non-neutral — 25% of plurality voting is non-academic.
5. **Rank instability**: T11 ranks **#1** under `current_strategy` but
   **#13** under `blind_citation`. T74_N1 swings from #1 to #10. This
   instability cannot be explained by data quality — it is profile-driven.
6. **Negative-control leakage**: Under `immigration_only`, the dummy topic
   "Machine learning for healthcare" scores 20.8 — *within the real-topic
   range* (15–26). The pure NIW-driven scoring is so generous that
   intentionally vague topics are competitive.

**Top topics that survive scrutiny (rank ≤ 6 in 6+ of 8 profiles):**
- **T43** (Reproducibility audit of clinical LLM papers) — 6/8 profiles in top 6
- **T74\_N1** (Open structured-metadata dataset, narrowed) — 5/8 profiles in top 6

**Top topics that survive ONLY under biased assumptions:**
- **T11** (Format sensitivity benchmark) — #1 under current strategy but #13
  under blind citation. Heavily dependent on artifact-target and
  LLM-keyword boosts.
- **T07_N1** (Judge prompt-injection, narrowed) — never ranks better than #6,
  bottom-half in 6/8 profiles. Should be deprioritized.

---

## B. Bias Risks Found

### B.1 Seed-topic bias

| Risk | Distortion | Current code? | Worsened by? | Proposed fix |
|---|---|---|---|---|
| 33% healthcare in 75-topic seed | NIW formula then auto-boosts these by +1.5–4.5 | No mitigation | Compounds: seed bias × score bias = doubled effect | Cap healthcare at ≤ 15% in any seed |
| 9× "llm judge" keyword | Query generator pairs it with axis terms → 36 LLM-judge searches per pipeline run | No mitigation | Query generator amplifies | Cap any single keyword at ≤ 3 occurrences in seed |
| 70% of main seed targets `dataset/benchmark/tool` | EB-1A formula awards +1.0 for these targets → ImmigrationValue inflated | No mitigation | EB-1A formula amplifies | Mix in `paper`, `survey`, `database` targets at ≥ 30% |

### B.2 Query-generation bias

| Risk | Distortion | Current code? | Worsened by? | Proposed fix |
|---|---|---|---|---|
| Auto-appended `benchmark/evaluation/robustness/reproducibility` (60.7% of queries) | Retrieval favors benchmark/eval-style papers; non-benchmark contributions invisible | No mitigation | Active code: `01_generate_queries.py:67-69` | Make axis-term injection conditional on `target_artifact`; do not inject for `paper/survey/methodology` topics |
| GitHub queries always append "benchmark in:name,description" | Non-benchmark repos hidden | No mitigation | Active code: `01_generate_queries.py:81-84` | Drop the auto-append; query keywords only |
| `AXIS_TERMS` list is hardcoded | Same 10 axis terms applied to all topics across all categories | No mitigation | Hardcoded constant | Per-category axis term lists, or remove entirely |

### B.3 Scoring-weight bias

| Risk | Distortion | Current code? | Worsened by? | Proposed fix |
|---|---|---|---|---|
| ImmigrationValue gets explicit 20% in Overall | A topic with weak academic merit but strong NIW signal scores high | No mitigation | Active code: `05_score_topics.py:332-339` | Make profile selectable at config; default profile should weight ImmigrationValue ≤ 5% |
| `niw_score()` awards +1.5 per healthcare keyword hit | Healthcare topics auto-promoted regardless of actual research merit | No mitigation | Active code: `05_score_topics.py:226-237` | Tie NIW boost to evidence (e.g., FDA/HHS citation, IRB-relevant data), not keywords |
| `career_score()` awards +0.6 per LLM-keyword hit, penalizes −0.6 for healthcare | LLM-eval topics auto-promoted; healthcare auto-demoted in career signal | No mitigation | Active code: `05_score_topics.py:253-271` | Career score should reflect job-market evidence (job listings count), not keyword presence |
| `eb1a_score()` awards +1.0 for dataset/benchmark/tool/database/framework targets | All paper-only contributions scored lower regardless of citation potential | No mitigation | Active code: `05_score_topics.py:240-250` | EB-1A boost should require evidence of artifact reuse (downloads, citations of artifact), not just `target_artifact` field |

### B.4 Reviewer-prompt bias

| Risk | Distortion | Current code? | Worsened by? | Proposed fix |
|---|---|---|---|---|
| 2/8 reviewer roles explicitly framed around immigration/FAANG | 25% of plurality voting structurally non-academic | No mitigation | Active code: `llm_panel.py:121-124` | Demote `niw_eb1a` and `career_faang` to optional reviewers, not part of plurality |
| Reviewer focus strings inject `NIW prong-2/3`, `EB-1A`, `high-paying` anchor terms | Models prime on user-specific career goals rather than topic merit | No mitigation | Active code: `llm_panel.py:121-124` | Add a NEUTRAL_REVIEWER_ROLES set — see §E for proposed neutral prompts |
| SYSTEM_PROMPT does say "use only evidence packet" | Partial mitigation | Partial mitigation | — | Strengthen by explicitly forbidding favoring any field, venue, or career goal |

### B.5 Existing-work detection bias

| Risk | Distortion | Current code? | Worsened by? | Proposed fix |
|---|---|---|---|---|
| `_artifact_differentiator_strength` rewards "domain_specific" via clinical/medical keywords | Healthcare topics get higher artifact-differentiator scores → fewer GO blocks | Recently added (commit 1784f47) | New code | Make domain-specific differentiator agnostic to which domain; reward ANY narrow domain (clinical, legal, financial, scientific) equally |

### B.6 Healthcare/NIW bias (compound effect)

| Risk | Distortion |
|---|---|
| Triple amplification | (a) seed has 33% healthcare → (b) queries find more healthcare papers → (c) NIW formula awards healthcare keywords → ImmigrationValue inflated → (d) Overall inflated by 20% weight on Immigration. **A topic about "robustness in clinical NLP" gets boosts at 4 separate stages**, none of which reflect academic novelty. |

### B.7 LLM-evaluation anchoring bias

| Risk | Distortion |
|---|---|
| Triple amplification | (a) seed has 9× "llm judge" → (b) queries pair llm-judge with benchmark/eval axes (36 per topic) → (c) Career formula awards LLM-keyword hits → (d) Career inflates Overall via 10% weight. **The system structurally cannot rank a non-LLM topic in the top 5**. |

### B.8 Artifact-preference bias

| Risk | Distortion |
|---|---|
| Triple amplification | (a) 70% of seed has dataset/benchmark/tool target → (b) queries auto-append "benchmark" → (c) EB-1A awards +1.0 for these targets → (d) tool_potential reinforces. **A pure conceptual paper cannot rank highly**, even with citation potential. |

### B.9 Venue bias

| Risk | Distortion |
|---|---|
| `venue_signal` rewards no-APC journals (DOAJ open-access) | Pulls topics toward open-access ML venues; closed-access flagship journals (Nature, NEJM) underweighted | No mitigation | Could add: weight venue prestige (impact factor, h-index) alongside no-APC |

### B.10 Execution-speed bias

| Risk | Distortion |
|---|---|
| `ExecFeasibility` formula rewards low risk + low IP issues | Topics requiring data-use agreements, IRB, or industry partnerships are penalized; long-term, high-impact topics suppressed | No mitigation | Add an "ExecHorizon" factor that does NOT penalize 12-month projects |

---

## C. Seed-Topic Distribution Audit

### Main seed (`data/topics_seed.csv`, 10 topics)

| Metric | Value | Healthy threshold |
|---|---|---|
| Healthcare-tagged | 20% | ≤ 15% |
| Eval-category tagged | 30% | ≤ 25% |
| Artifact-target tagged | **70%** | ≤ 50% |
| Most common keyword | `llm judge` (2×) | No keyword > 1× |
| Distinct categories | 8 | ≥ 8 |

### Full seed (`data/topics_seed_full_75.csv`, 75 topics)

| Metric | Value | Healthy threshold |
|---|---|---|
| Healthcare-tagged | **33.3%** | ≤ 15% |
| Eval-category tagged | 13.3% | ≤ 25% |
| Artifact-target tagged | 36% | ≤ 50% |
| Most common keyword | `llm judge` (9×) | ≤ 3× |
| Distinct categories | 27 | ≥ 15 |

### Overrepresented categories
- `eval` (9 topics, 12%)
- `healthcare` (9 topics, 12%) + healthcare combinations (16 more) → **33% total healthcare**
- `meta` (7 topics, 9%) — many are LLM-eval methodology
- `prompt` (5 topics, 7%) — all LLM-eval adjacent

### Underrepresented categories
- **agents**: 3 topics (4%) — given agent-LLM is one of the largest 2025 research areas
- **data-centric AI**: 0 topics
- **causal inference**: 1 topic (in `healthcare+causal` combo)
- **synthetic data**: 0 topics
- **ML systems**: 0 topics
- **scientific literature mining**: 4 topics — adequate
- **public health informatics**: 0 explicit
- **AI safety** (non-LLM): 3 topics — adequate
- **NLP eval (non-LLM-judge)**: 0 topics

### Findings
**The seed is not a neutral population sample of "credible research topics".**
It is a sample of *the user's pre-existing intuitions about LLM evaluation
and healthcare AI*, with three keyword clusters (`llm judge`, `clinical`,
`reproducibility`) collectively representing 40%+ of the corpus. Any
ranking exercise over this seed is sampling its own bias.

---

## D. Query-Generation Bias Findings

| Finding | Severity | Evidence |
|---|---|---|
| `AXIS_TERMS` constant baked into all queries | MEDIUM | `01_generate_queries.py:31-35` defines 10 axis terms applied universally |
| Top-3 keywords × 4 axis terms forcibly paired | **HIGH** | `01_generate_queries.py:67-69` |
| GitHub queries auto-append `benchmark` and `evaluation` to every keyword | MEDIUM | `01_generate_queries.py:81-84` |
| **60.7% of all 567 generated queries contain benchmark/eval/repro/robustness** | **HIGH** | Empirical measurement across all 14 active topics |

### Concrete example
For T11 ("Format sensitivity benchmark on LLM evaluations"), the generator
produced these searches:
- `format sensitivity benchmark` ✓ on-topic
- `format sensitivity evaluation` ✓ on-topic
- `format sensitivity robustness` (forced)
- `format sensitivity reproducibility` (forced — narrows search away from
  generalization, calibration, theoretical analyses)

For a topic like "AI agents for autonomous web tasks" (NOT in current
seed, hypothetical), the same generator would produce:
- `AI agents benchmark` (forced — but the contribution might be a
  protocol, not a benchmark)
- `AI agents evaluation`
- `AI agents robustness`
- `AI agents reproducibility`

This suppresses the discovery of pure-paper or theoretical work.

### Recommended neutral query templates
```python
# Replace lines 65-71 of 01_generate_queries.py with:
def _conditional_axis(target_artifact: str) -> list[str]:
    t = target_artifact.lower()
    if "benchmark" in t or "dataset" in t:
        return ["benchmark", "evaluation"]
    if "tool" in t or "framework" in t:
        return ["framework", "implementation"]
    if "survey" in t or "taxonomy" in t:
        return ["survey", "taxonomy"]
    if "paper" in t:
        return []  # no axis injection for pure-paper topics
    return ["evaluation"]  # safe default
```

---

## E. Reviewer-Prompt Bias Findings

### Current structure
- 8 reviewer roles in `REVIEWER_ROLES`
- 2 are explicitly biased: `niw_eb1a`, `career_faang`
- Plurality voting weights all 8 equally → 25% of plurality vote is structurally non-neutral

### Per-role bias scoring
| Role | Bias | Justification |
|---|---|---|
| `citation_potential` | LOW | Asks about audience, gap, reusability — academic-relevant |
| `novelty_saturation` | LOW | Asks about gap and saturation — academic-relevant |
| `venue_publication` | LOW | Includes "no-APC realistic" which biases away from prestigious closed-access |
| `artifact_reproducibility` | MEDIUM | Frames "artifact reusable" as central — biases toward artifact contributions |
| `niw_eb1a` | **HIGH** | Explicit immigration framing |
| `career_faang` | **HIGH** | Explicit FAANG hiring framing |
| `risk_ip` | LOW | Risk assessment is neutral |
| `brutal_skeptic` | LOW | Adversarial role; counterbalances optimism |

### Proposed neutral reviewer prompt set
Replace `REVIEWER_ROLES` with the following 6 academic-neutral roles. Move
the 2 personal-goal reviewers behind an opt-in flag.

```python
NEUTRAL_REVIEWER_ROLES = [
    {"role": "citation_potential",
     "focus": "Audience size, gap clarity, reusability. Do not favor any field."},
    {"role": "novelty_saturation",
     "focus": "Gap is real and unfilled. Saturation is bounded. Do not infer novelty from absence of search results — absence may be query bias."},
    {"role": "venue_credibility",
     "focus": "Venue is credible (peer-reviewed, indexed in DBLP/PubMed/Scopus). Do not favor open-access or no-APC venues over high-prestige closed venues."},
    {"role": "evidence_quality",
     "focus": "Retrieved evidence supports the claimed contribution. Flag if evidence is thin or if relevance purity < 0.40."},
    {"role": "differentiator_clarity",
     "focus": "Topic states a one-sentence contribution that is verifiably distinct from named existing work. Reject if differentiator is generic or vague."},
    {"role": "brutal_skeptic",
     "focus": "Strongest reason this topic will fail. Do not favor topics in any specific field, methodology, or artifact type."},
]

# Optional, behind --include-personal-goals flag
PERSONAL_GOAL_REVIEWERS = [
    {"role": "niw_eb1a", ...},   # immigration-relevant
    {"role": "career_faang", ...},
]
```

Add to SYSTEM_PROMPT:
> "Do not favor any field (no preference for healthcare, finance, NLP, vision,
> or any domain). Do not favor any contribution type (no preference for
> benchmarks over theory papers). Judge only from retrieved evidence. If the
> evidence is biased toward one framing, say so in `evidence_missing`."

---

## F. Scoring-Weight Sensitivity Table

Top-5 ranking under each profile:

| Profile | #1 | #2 | #3 | #4 | #5 |
|---|---|---|---|---|---|
| `current_strategy` | T11 | T74\_N1 | T43 | T04 | T10 |
| `blind_citation` | T10 | T43 | T17 | T74 | T53 |
| `academic_long_term` | T74\_N1 | T10 | T43 | T17 | T04 |
| `career_only` | T11 | T74\_N1 | T04 | T07 | T10 |
| `immigration_only` | T04 | T43 | T53\_N4 | T07 | T37 |
| `artifact_neutral` | T11 | T74\_N1 | T10 | T43 | T04 |
| `healthcare_neutral` | T11 | T74\_N1 | T10 | T07 | T74 |
| `llm_eval_neutral` | T43 | T37\_N1 | T37 | T25 | T53\_N4 |

**Observations:**
- `current_strategy` and `llm_eval_neutral` produce **completely disjoint top-5** sets except for T43.
- T11 ("Format sensitivity benchmark") drops from **#1 → #9** when the LLM-eval keyword boost is removed and from **#1 → #13** under `blind_citation`.
- T43 ("Reproducibility audit of clinical LLM papers") is the **most cross-profile-stable top topic**: appears in the top 5 of 6 of 8 profiles.
- T07_N1 (currently the noise-pruned variant of T07) **never makes top-5** in any profile — should be deprioritized.

### Profile-specific anomalies
- Under `immigration_only`, T04 jumps to #1 — driven entirely by NIW=5 + EB1A=5 (clinical+benchmark double boost).
- Under `llm_eval_neutral`, T37/T37_N1 jump into top 3 — they were previously held back by *less* LLM-eval boosting than competitors. Their signal is more grounded in actual evidence.
- Under `healthcare_neutral`, T74 (parent of T74\_N1) climbs to #5 because the narrowed variant's NIW boost was reduced.

---

## G. Rank Stability Table

Sorted by mean rank across 8 profiles. **`rank_range`** is the spread between
best and worst ranking — high values indicate the topic's apparent quality
is bias-dependent.

| Topic | rank min | rank max | rank range | rank mean | Diagnosis |
|---|---|---|---|---|---|
| T74\_N1 | 1 | 10 | 9 | 4.50 | Bias-sensitive but mostly top-half |
| T43 | 1 | 12 | 11 | 4.62 | **Robust top candidate** (top-5 in 6/8 profiles) |
| T10 | 1 | 11 | 10 | 4.75 | Strong on paper merit; **go_blocked** by EW |
| T11 | 1 | 13 | **12** | 5.62 | **Severely bias-sensitive** — looks #1 only with biases on |
| T04 | 1 | 13 | **12** | 6.00 | Severely bias-sensitive |
| T07 | 4 | 12 | 8 | 6.50 | Mid-tier; never #1 but always somewhat present |
| T17 | 3 | 12 | 9 | 7.50 | Mid-tier; **go_blocked** by EW |
| T37 | 3 | 13 | 10 | 7.50 | Mid-lower tier |
| T37\_N1 | 2 | 14 | 12 | 8.75 | Bias-sensitive, mostly bottom |
| T53\_N4 | 3 | 13 | 10 | 8.88 | Lower tier |
| T74 | 4 | 14 | 10 | 9.00 | Lower tier; parent has wider scope |
| T25 | 4 | 13 | 9 | 9.38 | Lower tier |
| T53 | 5 | 14 | 9 | 10.38 | Bottom tier |
| T07\_N1 | 6 | 14 | 8 | 11.62 | **Bottom tier across all profiles** — drop |

**Stability rule applied:** A topic is "robust" if `rank_max ≤ 6 AND rank_range ≤ 4`.
- **0 of 14 topics meet this criterion.** No topic survives an honest cross-bias test.
- Loosening to `rank_max ≤ 6 in ≥ 6 profiles`: T43 (top-5 in 6/8), T74_N1 (top-5 in 5/8). These are the two most defensible candidates.

---

## H. Topics Robust Across Modes

By the strict criterion (rank ≤ 6 in all 8 profiles), **no topic is robust**.

By the relaxed criterion (rank ≤ 6 in ≥ 6 of 8 profiles, AND not go_blocked):

| Topic | Profiles where top-6 | Excluded from top-6 by |
|---|---|---|
| **T43** (Reproducibility audit of clinical LLM papers) | 6/8 | `career_only` (FAANG penalizes healthcare); `llm_eval_neutral` (no LLM boost) — wait, T43 is #1 in `llm_eval_neutral` — so really only `career_only` excludes it |
| **T74\_N1** (Open structured-metadata dataset, narrowed) | 5/8 | `blind_citation`, `immigration_only`, `llm_eval_neutral` — drops because thin corpus (1 kept paper) is a real evidence weakness, not a bias artifact |

**T43 is the single most cross-profile-defensible topic.** Its strong NIW+EB-1A
profile is a real consequence of the topic (clinical reproducibility is genuinely
national-importance), not a keyword artifact. It also ranks #1 in
`llm_eval_neutral` and top-3 in `blind_citation`/`academic_long_term` — meaning
its strength is largely independent of LLM-eval keyword anchoring.

**T74_N1's instability is honest.** Its rank drops in academically-strict profiles
because 1 kept paper is genuinely too thin. The earlier dossier flagged this.

---

## I. Topics That Rank High ONLY Under Biased Assumptions

| Topic | Under biased profile | Under neutral profile | Diagnosis |
|---|---|---|---|
| **T11** (Format sensitivity benchmark) | #1 in `current_strategy`, `career_only`, `artifact_neutral`, `healthcare_neutral` | #13 in `blind_citation`, #10 in `academic_long_term`, #9 in `llm_eval_neutral` | **Heavily LLM-keyword + artifact-target dependent**. Drops sharply when benchmark/LLM keyword boost is removed. The 3 kept papers are insufficient evidence for a #1 ranking under any neutral standard. |
| **T04** (Prompt-template sensitivity, clinical LLM judges) | #1 in `immigration_only` (NIW=5+EB1A=5) | #8 in `blind_citation` | Triple-boosted by clinical+LLM-judge+benchmark; under blind academic merit it's mid-tier |
| **T07** (Judge prompt injection) | #4 in `current_strategy`, `career_only` | #10 in `blind_citation`, #12 in `llm_eval_neutral` | Held up by LLM-eval anchoring; drops sharply under llm_eval_neutral. The reviewer plurality was already NEEDS_MORE_EVIDENCE — this is consistent |

---

## J. Topics To Re-Test Using Balanced Seeds

The current 14 active topics are themselves a biased sample. Even the most
robust (T43, T74_N1) only stand out because they are compared against
13 other topics that share the same biases.

The newly generated `data/topics_seed_balanced.csv` (36 topics, 19% healthcare,
includes 7 negative controls) should be run through the full pipeline to
test:

| Hypothesis | Test |
|---|---|
| The current top topics dominate because of true merit | Top-3 in current 14 should remain top-3 in the new 36-topic run |
| The current top topics dominate because of seed bias | Top-3 will shift to topics from underrepresented categories (agents, data-centric, ML systems, causal inference) |
| The negative controls are correctly rejected | All 7 NC topics should rank in the bottom 10 — if any rank in the top half, the scoring system is leaky |

**Recommended priority topics from the balanced seed for next pipeline run:**
- B01 (Tool-calling reliability for autonomous agents)
- B03 (Data-centric AI: dataset auditing)
- B06 (Cross-task contamination in foundation model benchmarks)
- B10 (Counterfactual fairness audit toolkit)
- B11 (Distribution-shift detection for production ML)
- B14 (Refusal behavior consistency across LLM updates)

If any of these outranks the current top-4 (T11, T74_N1, T43, T07) under
`blind_citation` profile, the current rankings are seed-biased.

---

## K. Recommended Architecture Changes

### Tier 1 — Critical (do before next pipeline run)
1. **Replace `niw_eb1a` and `career_faang` reviewers** with 2 academic-neutral reviewers. Move the personal-goal reviewers behind an `--include-personal-goals` CLI flag.
2. **Make Overall scoring profile-selectable.** Default to `blind_citation` weighting; expose `--profile {current_strategy,blind_citation,academic,...}` as a CLI flag.
3. **Cap any single keyword at ≤ 3 occurrences in any seed file.** Reject `data/topics_seed_full_75.csv` until "llm judge" is reduced from 9× to ≤ 3×.
4. **Remove auto-axis-term injection from `01_generate_queries.py`.** Replace with conditional injection based on `target_artifact`.

### Tier 2 — Important (before any GO promotion)
5. **Decouple NIW boost from healthcare keywords.** Tie NIW to evidence (FDA citations, IRB-relevant data) rather than category strings.
6. **Decouple Career boost from LLM keywords.** Replace with job-listings evidence or remove entirely.
7. **Decouple EB-1A boost from artifact-type strings.** Tie EB-1A to artifact reuse evidence (downloads, citations).
8. **Add a "negative-control sentinel" requirement to the gate.** Before promoting any topic to GO, the scoring system must pass: "all 7 NC topics rank in bottom-third under the chosen profile."

### Tier 3 — Refinement (next 1-2 sprints)
9. **Implement multi-profile reporting** in `09_generate_final_report.py`. Show every topic's rank under all profiles; highlight topics that survive ≥ 6 profiles.
10. **Audit `12_detect_existing_work.py`** for the domain-specific clinical/medical bias in `_artifact_differentiator_strength`.
11. **Strengthen SYSTEM_PROMPT** with explicit anti-favoritism clause.
12. **Re-run the existing 14 topics** under the corrected scoring AND the balanced seed.

---

## L. Final Judgment

> **Current system: NOT TRUSTWORTHY without major redesign.**

### Specific rationale
1. **Profile sensitivity**: 0 of 14 topics survive a strict cross-profile stability test. The top-3 ranking changes completely between `current_strategy` and `blind_citation`.
2. **Compound bias**: Healthcare and LLM-eval anchoring are reinforced at 4 separate stages each (seed, query, scoring, reviewer). The Overall score is not measuring research quality — it is measuring agreement with the user's prior assumptions.
3. **Negative-control leakage**: Under `immigration_only`, vague topics ("ML for healthcare") score within the real-topic range. Under `current_strategy`, they correctly fail — but only because the 8 weighted components partially cancel each other, not because the system has principled noise rejection.
4. **The 4 dossier candidates are a biased sample of a biased seed**: T11 (current #1) drops to #13 under blind citation. T74_N1 has only 1 kept paper. T07 is held up by LLM-eval anchoring. Only T43 remains defensible under multiple profiles — and even that is partly a pun (clinical reproducibility genuinely is national-interest, but the score formula triple-boosts it for the wrong reasons).

### Should we re-run topic discovery with balanced seeds?
**Yes — and with the bias fixes from Tier 1.** Specifically:
- Apply Tier 1 fixes (#1–#4) to the codebase.
- Run the pipeline on `data/topics_seed_balanced.csv` (36 topics).
- Compare new top-5 to current top-5.
- If new top-5 is largely from underrepresented categories (agents, data-centric, fairness, ML systems), the current rankings are a seed artifact.
- If T43 and T74_N1 still appear in top-5 of the balanced run, they have real merit.

### Are the current top topics robust?
**Partially. T43 yes; T74_N1 conditionally; T11 and T07 are bias-dependent.**

| Topic | Verdict |
|---|---|
| **T43** | Robust. Top-3 across 5 of 8 profiles, including the most academically-strict ones (`blind_citation`, `academic_long_term`, `llm_eval_neutral`). |
| **T74\_N1** | Conditionally robust. Top-2 across 5 profiles, but rank drops under academically-strict scoring. The 1-kept-paper evidence problem is real, not bias. |
| **T11** | NOT robust. #1 only under biased profiles; drops to #13 under `blind_citation`. Heavily dependent on artifact-target boost. |
| **T07** | NOT robust as #4-tier. Drops to #10–#12 under neutral profiles. The LLM-eval anchor is doing most of the lifting. |

### What needs to change before any topic gets a GO recommendation?
1. **Replace the reviewer prompts** with the 6-role neutral set (Tier 1.1).
2. **Re-run the LLM panel** on the current 4 candidates with neutral reviewers.
3. **Re-run the pipeline** on `topics_seed_balanced.csv`.
4. **Compare**: only topics that rank top-5 under both `blind_citation` AND `current_strategy` are GO-eligible.
5. **Verify negative-control sentinel**: confirm all 7 NC topics rank bottom-third under chosen profile.

If, after all of the above, T43 and T74_N1 still rank top-5, then they have
earned the right to be considered for GO. None of the current 14 topics has
earned that right yet.

---

## Appendix: Files Generated

- `data/bias_audit/seed_distribution.json`
- `data/bias_audit/query_audit.json`
- `data/bias_audit/reviewer_prompt_audit.json`
- `data/bias_audit/profile_rankings.csv`
- `data/bias_audit/rank_stability.csv`
- `data/bias_audit/robust_topics.json`
- `data/bias_audit/biased_topics.json`
- `data/bias_audit/negative_control_results.json`
- `data/bias_audit/balanced_seed_info.json`
- `data/bias_audit/top10_<profile>.json` (8 files, one per profile)
- `data/topics_seed_balanced.csv` (36 topics, 7 negative controls)
- `config/bias_profiles.yaml` (8 weighting profiles)

## Appendix: Reproducing this audit

```powershell
cd "C:\Users\rohit\Documents\Research Papers\research-command-center"
python scripts/13_bias_audit.py                                        # full audit
python scripts/13_bias_audit.py --profiles current_strategy,blind_citation  # subset
python scripts/13_bias_audit.py --negative-control-only                # NC test only
```

The audit makes no LLM calls and does not modify the existing pipeline.
All conclusions are derived from `data/scores/<topic_id>.json`,
`data/decisions/<topic_id>.json`, and the seed CSVs.
