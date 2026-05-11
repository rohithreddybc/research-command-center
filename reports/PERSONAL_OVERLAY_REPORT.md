# Personal-Goal Overlay Report

*Generated: 2026-05-10 by `scripts/14_personal_overlay.py`*


---

## Design principle

Personal-goal overlays **do NOT change the academic (blind_citation) ranking**. They only help select among topics that already pass the blind_citation acceptability gate.

- **Safe choice** = the topic is `blind_citation_acceptable=True` AND ranks top-8 under a personal-goal profile.
- **Risky choice** (`PERSONAL_GOAL_ONLY_WEAK_TOPIC`) = the topic ranks top-8 under a personal profile but FAILS `blind_citation_acceptable`. These should NOT be promoted to GO.

## Topics that pass blind_citation acceptability

| Topic | bc_score | Decision | Conf | Title |
|---|---|---|---|---|
| **B05** | 26.50 | NARROW | MEDIUM | Synthetic data quality evaluation metrics |
| **B12** | 24.00 | NARROW | MEDIUM | Multi-lingual factuality benchmark for low-resource languages |
| **T07** | 23.80 | NARROW | MEDIUM | Judge robustness to candidate-side prompt injection |
| **T01** | 23.46 | NARROW | MEDIUM | Cross-judge agreement on long-context QA |
| **B11** | 23.00 | NARROW | MEDIUM | Distribution-shift detection methods for production ML |
| **T02** | 22.16 | NARROW | MEDIUM | Position-bias quantification across judge models |


## Overlay: NIW (national interest waiver)  (`niw_optimized`)

### Top 8 under niw_optimized

| Rank | Topic | Score | bc_acc? | EW-blocked? | Decision | Title |
|---|---|---|---|---|---|---|
| 1 | **T22** | 28.42 | ❌ | — | NARROW | Clinical-guideline RAG eval benchmark |
| 2 | **T04** | 28.10 | ❌ | — | NARROW | Prompt-template sensitivity benchmark for clinical-domain LL |
| 3 | **T14** | 25.65 | ❌ | — | NARROW | Few-shot order effects on healthcare-domain prompts |
| 4 | **B15** | 23.35 | ❌ | ⛔ | NARROW | Clinical decision support: alert fatigue measurement |
| 5 | **T07** | 22.85 | ✅ | — | NARROW | Judge robustness to candidate-side prompt injection |
| 6 | **B08** | 22.81 | ❌ | ⛔ | NARROW | Public health informatics: outbreak signal detection |
| 7 | **B16** | 22.21 | ❌ | — | NARROW | Reproducibility in healthcare AI deployment studies |
| 8 | **T10** | 21.20 | ❌ | ⛔ | NARROW | Reproducibility audit of LLM-judge papers |

### Safe choices for NIW (national interest waiver)

_(bc_acceptable=True AND top-8 under niw_optimized AND not EW-blocked)_

- **T07**: Judge robustness to candidate-side prompt injection (rank #5, profile_score=22.85, bc_score=23.80)

### Risky choices (PERSONAL_GOAL_ONLY_WEAK_TOPIC) for NIW (national interest waiver)

_(top under personal profile but FAILS blind_citation gate — DO NOT promote to GO)_

- ⚠️ **T22**: Clinical-guideline RAG eval benchmark (rank #1 under niw_optimized, score=28.42; bc_score=18.95 FAILS gate)
- ⚠️ **T04**: Prompt-template sensitivity benchmark for clinical-domain LLM judges (rank #2 under niw_optimized, score=28.10; bc_score=21.80 FAILS gate)
- ⚠️ **T14**: Few-shot order effects on healthcare-domain prompts (rank #3 under niw_optimized, score=25.65; bc_score=15.86 FAILS gate)
- ⚠️ **B15**: Clinical decision support: alert fatigue measurement (rank #4 under niw_optimized, score=23.35; bc_score=19.46 FAILS gate)
- ⚠️ **B08**: Public health informatics: outbreak signal detection (rank #6 under niw_optimized, score=22.81; bc_score=22.50 FAILS gate)
- ⚠️ **B16**: Reproducibility in healthcare AI deployment studies (rank #7 under niw_optimized, score=22.21; bc_score=21.07 FAILS gate)
- ⚠️ **T10**: Reproducibility audit of LLM-judge papers (rank #8 under niw_optimized, score=21.20; bc_score=24.30 FAILS gate)


## Overlay: EB-1A (extraordinary ability)  (`eb1a_optimized`)

### Top 8 under eb1a_optimized

| Rank | Topic | Score | bc_acc? | EW-blocked? | Decision | Title |
|---|---|---|---|---|---|---|
| 1 | **B05** | 33.00 | ✅ | — | NARROW | Synthetic data quality evaluation metrics |
| 2 | **T10** | 31.55 | ❌ | ⛔ | NARROW | Reproducibility audit of LLM-judge papers |
| 3 | **T07** | 31.43 | ✅ | — | NARROW | Judge robustness to candidate-side prompt injection |
| 4 | **T01** | 30.22 | ✅ | — | NARROW | Cross-judge agreement on long-context QA |
| 5 | **T04** | 30.21 | ❌ | — | NARROW | Prompt-template sensitivity benchmark for clinical-domain LL |
| 6 | **B08** | 29.41 | ❌ | ⛔ | NARROW | Public health informatics: outbreak signal detection |
| 7 | **T22** | 29.40 | ❌ | — | NARROW | Clinical-guideline RAG eval benchmark |
| 8 | **B13** | 28.80 | ❌ | — | NARROW | Citation-context mining for scientific literature |

### Safe choices for EB-1A (extraordinary ability)

_(bc_acceptable=True AND top-8 under eb1a_optimized AND not EW-blocked)_

- **B05**: Synthetic data quality evaluation metrics (rank #1, profile_score=33.00, bc_score=26.50)
- **T07**: Judge robustness to candidate-side prompt injection (rank #3, profile_score=31.43, bc_score=23.80)
- **T01**: Cross-judge agreement on long-context QA (rank #4, profile_score=30.22, bc_score=23.46)

### Risky choices (PERSONAL_GOAL_ONLY_WEAK_TOPIC) for EB-1A (extraordinary ability)

_(top under personal profile but FAILS blind_citation gate — DO NOT promote to GO)_

- ⚠️ **T10**: Reproducibility audit of LLM-judge papers (rank #2 under eb1a_optimized, score=31.55; bc_score=24.30 FAILS gate)
- ⚠️ **T04**: Prompt-template sensitivity benchmark for clinical-domain LLM judges (rank #5 under eb1a_optimized, score=30.21; bc_score=21.80 FAILS gate)
- ⚠️ **B08**: Public health informatics: outbreak signal detection (rank #6 under eb1a_optimized, score=29.41; bc_score=22.50 FAILS gate)
- ⚠️ **T22**: Clinical-guideline RAG eval benchmark (rank #7 under eb1a_optimized, score=29.40; bc_score=18.95 FAILS gate)
- ⚠️ **B13**: Citation-context mining for scientific literature (rank #8 under eb1a_optimized, score=28.80; bc_score=21.82 FAILS gate)


## Overlay: FAANG / industry career  (`faang_career`)

### Top 8 under faang_career

| Rank | Topic | Score | bc_acc? | EW-blocked? | Decision | Title |
|---|---|---|---|---|---|---|
| 1 | **T07** | 31.35 | ✅ | — | NARROW | Judge robustness to candidate-side prompt injection |
| 2 | **T04** | 29.88 | ❌ | — | NARROW | Prompt-template sensitivity benchmark for clinical-domain LL |
| 3 | **T10** | 29.70 | ❌ | ⛔ | NARROW | Reproducibility audit of LLM-judge papers |
| 4 | **T01** | 29.48 | ✅ | — | NARROW | Cross-judge agreement on long-context QA |
| 5 | **B05** | 29.20 | ✅ | — | NARROW | Synthetic data quality evaluation metrics |
| 6 | **B01** | 28.64 | ❌ | — | NARROW | Tool-calling reliability benchmark for autonomous agents |
| 7 | **B13** | 28.14 | ❌ | — | NARROW | Citation-context mining for scientific literature |
| 8 | **T02** | 27.48 | ✅ | — | NARROW | Position-bias quantification across judge models |

### Safe choices for FAANG / industry career

_(bc_acceptable=True AND top-8 under faang_career AND not EW-blocked)_

- **T07**: Judge robustness to candidate-side prompt injection (rank #1, profile_score=31.35, bc_score=23.80)
- **T01**: Cross-judge agreement on long-context QA (rank #4, profile_score=29.48, bc_score=23.46)
- **B05**: Synthetic data quality evaluation metrics (rank #5, profile_score=29.20, bc_score=26.50)
- **T02**: Position-bias quantification across judge models (rank #8, profile_score=27.48, bc_score=22.16)

### Risky choices (PERSONAL_GOAL_ONLY_WEAK_TOPIC) for FAANG / industry career

_(top under personal profile but FAILS blind_citation gate — DO NOT promote to GO)_

- ⚠️ **T04**: Prompt-template sensitivity benchmark for clinical-domain LLM judges (rank #2 under faang_career, score=29.88; bc_score=21.80 FAILS gate)
- ⚠️ **T10**: Reproducibility audit of LLM-judge papers (rank #3 under faang_career, score=29.70; bc_score=24.30 FAILS gate)
- ⚠️ **B01**: Tool-calling reliability benchmark for autonomous agents (rank #6 under faang_career, score=28.64; bc_score=23.24 FAILS gate)
- ⚠️ **B13**: Citation-context mining for scientific literature (rank #7 under faang_career, score=28.14; bc_score=21.82 FAILS gate)


## Overlay: Balanced personal strategy  (`balanced_personal_strategy`)

### Top 8 under balanced_personal_strategy

| Rank | Topic | Score | bc_acc? | EW-blocked? | Decision | Title |
|---|---|---|---|---|---|---|
| 1 | **T04** | 30.81 | ❌ | — | NARROW | Prompt-template sensitivity benchmark for clinical-domain LL |
| 2 | **B05** | 30.60 | ✅ | — | NARROW | Synthetic data quality evaluation metrics |
| 3 | **T07** | 30.52 | ✅ | — | NARROW | Judge robustness to candidate-side prompt injection |
| 4 | **T22** | 30.00 | ❌ | — | NARROW | Clinical-guideline RAG eval benchmark |
| 5 | **T10** | 29.75 | ❌ | ⛔ | NARROW | Reproducibility audit of LLM-judge papers |
| 6 | **B08** | 29.09 | ❌ | ⛔ | NARROW | Public health informatics: outbreak signal detection |
| 7 | **B01** | 28.26 | ❌ | — | NARROW | Tool-calling reliability benchmark for autonomous agents |
| 8 | **T01** | 28.22 | ✅ | — | NARROW | Cross-judge agreement on long-context QA |

### Safe choices for Balanced personal strategy

_(bc_acceptable=True AND top-8 under balanced_personal_strategy AND not EW-blocked)_

- **B05**: Synthetic data quality evaluation metrics (rank #2, profile_score=30.60, bc_score=26.50)
- **T07**: Judge robustness to candidate-side prompt injection (rank #3, profile_score=30.52, bc_score=23.80)
- **T01**: Cross-judge agreement on long-context QA (rank #8, profile_score=28.22, bc_score=23.46)

### Risky choices (PERSONAL_GOAL_ONLY_WEAK_TOPIC) for Balanced personal strategy

_(top under personal profile but FAILS blind_citation gate — DO NOT promote to GO)_

- ⚠️ **T04**: Prompt-template sensitivity benchmark for clinical-domain LLM judges (rank #1 under balanced_personal_strategy, score=30.81; bc_score=21.80 FAILS gate)
- ⚠️ **T22**: Clinical-guideline RAG eval benchmark (rank #4 under balanced_personal_strategy, score=30.00; bc_score=18.95 FAILS gate)
- ⚠️ **T10**: Reproducibility audit of LLM-judge papers (rank #5 under balanced_personal_strategy, score=29.75; bc_score=24.30 FAILS gate)
- ⚠️ **B08**: Public health informatics: outbreak signal detection (rank #6 under balanced_personal_strategy, score=29.09; bc_score=22.50 FAILS gate)
- ⚠️ **B01**: Tool-calling reliability benchmark for autonomous agents (rank #7 under balanced_personal_strategy, score=28.26; bc_score=23.24 FAILS gate)


## Diagnostic: extreme profiles (top-5)

These are extreme weighting profiles for audit comparison. Topics that win here but not under any non-extreme personal profile are bias-driven outliers.

| Profile | #1 | #2 | #3 | #4 | #5 |
|---|---|---|---|---|---|
| `immigration_only` | T22(29.9❌) | T04(27.9❌) | T14(26.9❌) | T07(22.5✅) | B15(21.7❌) |
| `career_only` | T04(16.8❌) | T07(16.8✅) | T01(14.0✅) | B01(13.8❌) | B04(13.8❌) |


## Cross-overlay summary: topics safe under ≥ 2 personal profiles

| Topic | # personal profiles where safe | Profiles |
|---|---|---|
| **T07** | 4 | niw_optimized, eb1a_optimized, faang_career, balanced_personal_strategy |
| **B05** | 3 | eb1a_optimized, faang_career, balanced_personal_strategy |
| **T01** | 3 | eb1a_optimized, faang_career, balanced_personal_strategy |


## Final note

The blind_citation baseline (committed in c805933) remains the canonical academic-merit ranking. This overlay report is a **selection aid**, not a re-ranking. Any topic considered for GO must:

1. Pass `blind_citation_acceptable=True` (bc_score above gate, EW-not-blocked, purity ≥ 0.30)

2. Not be flagged `personal_goal_only_weak_topic`

3. Not be flagged `negative_control_blocked_go`

4. Have a clear citation thesis (see GO_READINESS_DOSSIERS for template)


No topic in this run currently meets all 4 criteria for GO. The 6 bc_acceptable topics are the candidate pool.
