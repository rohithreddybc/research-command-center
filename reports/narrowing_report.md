# Narrowing Report — 2026-05-09 23:51:49

## Overview

- Parent NARROW topics processed: **10**
- Total candidate variants generated: **22**
- Variants selected for re-run: **12**
- Selection criterion: top by composite score (w_purity=0.35, w_cit=0.15, w_art=0.15, w_niw=0.1, w_eb1a=0.1, w_career=0.15)

## Selected Variants (ranked by composite score)

| # | Variant ID | Parent | Narrowing type | Est. purity | Purity gain | Est. kept | Est. cit | Est. art | Composite |
|---|------------|--------|----------------|-------------|-------------|-----------|----------|----------|-----------|
| 1 | T04_N1 | T04 | noise_pruned | 0.500 | +0.250 | 11 | 2 | 3 | 0.6750 |
| 2 | T10_N1 | T10 | noise_pruned | 0.500 | +0.250 | 12 | 4 | 3 | 0.6650 |
| 3 | T07_N2 | T07 | synonym_promoted | 0.250 | +0.000 | 15 | 4 | 2 | 0.6500 |
| 4 | T37_N2 | T37 | noise_pruned | 0.500 | +0.250 | 9 | 4 | 3 | 0.6250 |
| 5 | T53_N5 | T53 | noise_pruned | 0.500 | +0.000 | 34 | 4 | 2 | 0.6250 |
| 6 | T07_N1 | T07 | noise_pruned | 0.500 | +0.000 | 14 | 2 | 2 | 0.6250 |
| 7 | T11_N1 | T11 | tightened_negatives | 0.250 | +0.000 | 3 | 2 | 4 | 0.5575 |
| 8 | T10_N2 | T10 | synonym_promoted | 0.250 | +0.000 | 17 | 4 | 2 | 0.5475 |
| 9 | T74_N1 | T74 | noise_pruned | 0.500 | +0.250 | 1 | 1 | 3 | 0.5350 |
| 10 | T37_N3 | T37 | compound_pivot | 0.250 | +0.000 | 9 | 4 | 2 | 0.5075 |
| 11 | T53_N1 | T53 | primary_anchor | 0.250 | +0.000 | 1 | 1 | 2 | 0.5000 |
| 12 | T25_N1 | T25 | noise_pruned | 0.500 | +0.250 | 2 | 1 | 3 | 0.4850 |

## Per-Parent Analysis

### T04: Prompt-template sensitivity benchmark for clinical-domain LLM judges

**Original signals**: purity=0.25, citation=5, artifact=2
**Original keywords**: `LLM judge|prompt template sensitivity|clinical NLP|robustness`
**Original synonyms**: `clinical question answering;medical QA;judge prompt;evaluator prompt`
**Original negatives**: `general chatbot`
**Reason NARROW**: Audience exists; framing too broad for current venue path.

Candidates generated: 1 | Selected: 1

| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |
|------------|------|--------------------------|-------------|-------------|------|
| T04_N1 | noise_pruned | `LLM judge|prompt template sensitivity` | 0.500 | +0.250 | ✓ |

**Selected variant details:**

#### T04_N1 — noise_pruned
- **Title**: Prompt-template sensitivity benchmark for clinical-domain LLM judges — noise-pruned
- **Keywords**: `LLM judge|prompt template sensitivity`
- **Synonyms**: `clinical question answering;medical QA;judge prompt;evaluator prompt`
- **Negatives**: `general chatbot;clinical NLP;robustness`
- **Narrowing note**: removed noisy secondaries=['clinical NLP', 'robustness']; added to negatives
- **Est. relevance purity**: 0.500 (parent: 0.250, gain: +0.250)
- **Est. kept papers**: 11 (hi-relevance: 11)
- **Est. citation_signal**: 2/5
- **Est. artifact_opportunity**: 3/5
- **Est. NIW/EB1A/Career**: 5/5/5
- **Est. novelty risk**: MEDIUM
- **Composite score**: 0.6750

### T07: Judge robustness to candidate-side prompt injection

**Original signals**: purity=0.5, citation=5, artifact=2
**Original keywords**: `prompt injection|LLM judge|adversarial robustness`
**Original synonyms**: `jailbreak;evaluator manipulation`
**Original negatives**: `general red teaming`
**Reason NARROW**: Audience exists; framing too broad for current venue path.

Candidates generated: 2 | Selected: 2

| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |
|------------|------|--------------------------|-------------|-------------|------|
| T07_N2 | synonym_promoted | `jailbreak|prompt injection` | 0.250 | +0.000 | ✓ |
| T07_N1 | noise_pruned | `prompt injection` | 0.500 | +0.000 | ✓ |

**Selected variant details:**

#### T07_N2 — synonym_promoted
- **Title**: Judge robustness to candidate-side prompt injection — via jailbreak
- **Keywords**: `jailbreak|prompt injection`
- **Synonyms**: `evaluator manipulation`
- **Negatives**: `general red teaming;LLM judge;adversarial robustness`
- **Narrowing note**: promoted synonym 'jailbreak' to primary
- **Est. relevance purity**: 0.250 (parent: 0.500, gain: +0.000)
- **Est. kept papers**: 15 (hi-relevance: 2)
- **Est. citation_signal**: 4/5
- **Est. artifact_opportunity**: 2/5
- **Est. NIW/EB1A/Career**: 4/5/5
- **Est. novelty risk**: LOW
- **Composite score**: 0.6500

#### T07_N1 — noise_pruned
- **Title**: Judge robustness to candidate-side prompt injection — noise-pruned
- **Keywords**: `prompt injection`
- **Synonyms**: `jailbreak;evaluator manipulation`
- **Negatives**: `general red teaming;LLM judge;adversarial robustness`
- **Narrowing note**: removed noisy secondaries=['LLM judge', 'adversarial robustness']; added to negatives
- **Est. relevance purity**: 0.500 (parent: 0.500, gain: +0.000)
- **Est. kept papers**: 14 (hi-relevance: 14)
- **Est. citation_signal**: 2/5
- **Est. artifact_opportunity**: 2/5
- **Est. NIW/EB1A/Career**: 4/5/5
- **Est. novelty risk**: MEDIUM
- **Composite score**: 0.6250

### T10: Reproducibility audit of LLM-judge papers

**Original signals**: purity=0.25, citation=5, artifact=2
**Original keywords**: `LLM-as-a-judge|reproducibility|methodology disclosure|evaluation`
**Original synonyms**: `LLM judge;automatic evaluator;LLM evaluator;model-based evaluation`
**Original negatives**: `tutorial;workshop summary`
**Reason NARROW**: Audience exists; framing too broad for current venue path.

Candidates generated: 2 | Selected: 2

| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |
|------------|------|--------------------------|-------------|-------------|------|
| T10_N1 | noise_pruned | `LLM-as-a-judge|methodology disclosure` | 0.500 | +0.250 | ✓ |
| T10_N2 | synonym_promoted | `LLM judge|LLM-as-a-judge|methodology disclosure` | 0.250 | +0.000 | ✓ |

**Selected variant details:**

#### T10_N1 — noise_pruned
- **Title**: Reproducibility audit of LLM-judge papers — noise-pruned
- **Keywords**: `LLM-as-a-judge|methodology disclosure`
- **Synonyms**: `LLM judge;automatic evaluator;LLM evaluator;model-based evaluation`
- **Negatives**: `tutorial;workshop summary;reproducibility;evaluation`
- **Narrowing note**: removed noisy secondaries=['reproducibility', 'evaluation']; added to negatives
- **Est. relevance purity**: 0.500 (parent: 0.250, gain: +0.250)
- **Est. kept papers**: 12 (hi-relevance: 8)
- **Est. citation_signal**: 4/5
- **Est. artifact_opportunity**: 3/5
- **Est. NIW/EB1A/Career**: 3/5/4
- **Est. novelty risk**: MEDIUM
- **Composite score**: 0.6650

#### T10_N2 — synonym_promoted
- **Title**: Reproducibility audit of LLM-judge papers — via LLM judge
- **Keywords**: `LLM judge|LLM-as-a-judge|methodology disclosure`
- **Synonyms**: `methodology disclosure|automatic evaluator|LLM evaluator|model-based evaluation`
- **Negatives**: `tutorial;workshop summary;reproducibility;evaluation`
- **Narrowing note**: promoted synonym 'LLM judge' to primary
- **Est. relevance purity**: 0.250 (parent: 0.250, gain: +0.000)
- **Est. kept papers**: 17 (hi-relevance: 7)
- **Est. citation_signal**: 4/5
- **Est. artifact_opportunity**: 2/5
- **Est. NIW/EB1A/Career**: 3/5/4
- **Est. novelty risk**: MEDIUM
- **Composite score**: 0.5475

### T11: Format sensitivity benchmark on LLM evaluations

**Original signals**: purity=0.25, citation=4, artifact=4
**Original keywords**: `format sensitivity|JSON YAML prose|benchmark variance`
**Original synonyms**: `output format;structured output`
**Original negatives**: `unrelated UI`
**Reason NARROW**: Audience exists; framing too broad for current venue path.

Candidates generated: 1 | Selected: 1

| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |
|------------|------|--------------------------|-------------|-------------|------|
| T11_N1 | tightened_negatives | `format sensitivity|JSON YAML prose|benchmark variance` | 0.250 | +0.000 | ✓ |

**Selected variant details:**

#### T11_N1 — tightened_negatives
- **Title**: Format sensitivity benchmark on LLM evaluations — tightened
- **Keywords**: `format sensitivity|JSON YAML prose|benchmark variance`
- **Synonyms**: `output format;structured output`
- **Negatives**: `unrelated UI`
- **Narrowing note**: fallback: added noisy terms to negative_keywords only
- **Est. relevance purity**: 0.250 (parent: 0.250, gain: +0.000)
- **Est. kept papers**: 3 (hi-relevance: 1)
- **Est. citation_signal**: 2/5
- **Est. artifact_opportunity**: 4/5
- **Est. NIW/EB1A/Career**: 2/5/5
- **Est. novelty risk**: LOW
- **Composite score**: 0.5575

### T17: Tokenization-induced leaderboard variance

**Original signals**: purity=0.5, citation=5, artifact=2
**Original keywords**: `tokenizer|BPE|leaderboard variance|evaluation noise`
**Original synonyms**: `subword;encoding effects`
**Original negatives**: `compiler tokenizers`
**Reason NARROW**: Audience exists; framing too broad for current venue path.

Candidates generated: 5 | Selected: 0

| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |
|------------|------|--------------------------|-------------|-------------|------|
| T17_N1 | primary_anchor | `tokenizer visual generation|leaderboard variance|evaluation …` | 0.000 | +0.000 |  |
| T17_N2 | primary_anchor | `tokenizer unified image|leaderboard variance|evaluation nois…` | 0.000 | +0.000 |  |
| T17_N3 | primary_anchor | `tokenizer multimodal understanding|leaderboard variance|eval…` | 0.000 | +0.000 |  |
| T17_N4 | primary_anchor | `tokenizer understanding generation|leaderboard variance|eval…` | 0.000 | +0.000 |  |
| T17_N5 | primary_anchor | `tokenizer multimodal understanding generation|leaderboard va…` | 0.000 | +0.000 |  |

**Selected variant details:**

### T25: Hallucination taxonomy: RAG vs no-RAG

**Original signals**: purity=0.25, citation=2, artifact=2
**Original keywords**: `retrieval augmented generation|hallucination taxonomy|faithfulness`
**Original synonyms**: `grounded generation;citation correctness`
**Original negatives**: `unrelated retrieval`
**Reason NARROW**: Audience exists; framing too broad for current venue path.

Candidates generated: 1 | Selected: 1

| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |
|------------|------|--------------------------|-------------|-------------|------|
| T25_N1 | noise_pruned | `retrieval augmented generation|hallucination taxonomy` | 0.500 | +0.250 | ✓ |

**Selected variant details:**

#### T25_N1 — noise_pruned
- **Title**: Hallucination taxonomy: RAG vs no-RAG — noise-pruned
- **Keywords**: `retrieval augmented generation|hallucination taxonomy`
- **Synonyms**: `grounded generation;citation correctness`
- **Negatives**: `unrelated retrieval;faithfulness`
- **Narrowing note**: removed noisy secondaries=['faithfulness']; added to negatives
- **Est. relevance purity**: 0.500 (parent: 0.250, gain: +0.250)
- **Est. kept papers**: 2 (hi-relevance: 2)
- **Est. citation_signal**: 1/5
- **Est. artifact_opportunity**: 3/5
- **Est. NIW/EB1A/Career**: 2/3/3
- **Est. novelty risk**: LOW
- **Composite score**: 0.4850

### T37: Clinical-guideline consistency across LLM versions over time

**Original signals**: purity=0.25, citation=5, artifact=2
**Original keywords**: `clinical guideline|model drift|LLM versioning|longitudinal evaluation`
**Original synonyms**: `USPSTF;CDC guidelines;NICE;medical advice consistency`
**Original negatives**: `drug discovery`
**Reason NARROW**: Audience exists; framing too broad for current venue path.

Candidates generated: 3 | Selected: 2

| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |
|------------|------|--------------------------|-------------|-------------|------|
| T37_N2 | noise_pruned | `clinical guideline|LLM versioning` | 0.500 | +0.250 | ✓ |
| T37_N3 | compound_pivot | `diagnosis management|clinical guideline|LLM versioning` | 0.250 | +0.000 | ✓ |
| T37_N1 | primary_anchor | `clinical guideline diagnosis management|LLM versioning` | 0.000 | +0.000 |  |

**Selected variant details:**

#### T37_N2 — noise_pruned
- **Title**: Clinical-guideline consistency across LLM versions over time — noise-pruned
- **Keywords**: `clinical guideline|LLM versioning`
- **Synonyms**: `USPSTF;CDC guidelines;NICE;medical advice consistency`
- **Negatives**: `drug discovery;model drift;longitudinal evaluation`
- **Narrowing note**: removed noisy secondaries=['model drift', 'longitudinal evaluation']; added to negatives
- **Est. relevance purity**: 0.500 (parent: 0.250, gain: +0.250)
- **Est. kept papers**: 9 (hi-relevance: 9)
- **Est. citation_signal**: 4/5
- **Est. artifact_opportunity**: 3/5
- **Est. NIW/EB1A/Career**: 5/4/2
- **Est. novelty risk**: MEDIUM
- **Composite score**: 0.6250

#### T37_N3 — compound_pivot
- **Title**: Clinical-guideline consistency across LLM versions over time — pivoted to 'diagnosis management'
- **Keywords**: `diagnosis management|clinical guideline|LLM versioning`
- **Synonyms**: `USPSTF;CDC guidelines;NICE;medical advice consistency`
- **Negatives**: `drug discovery;model drift;longitudinal evaluation`
- **Narrowing note**: pivoted primary to hi-paper anchor 'diagnosis management'
- **Est. relevance purity**: 0.250 (parent: 0.250, gain: +0.000)
- **Est. kept papers**: 9 (hi-relevance: 0)
- **Est. citation_signal**: 4/5
- **Est. artifact_opportunity**: 2/5
- **Est. NIW/EB1A/Career**: 5/4/2
- **Est. novelty risk**: LOW
- **Composite score**: 0.5075

### T43: Reproducibility audit of clinical LLM papers

**Original signals**: purity=0.25, citation=5, artifact=2
**Original keywords**: `clinical LLM|reproducibility|methodology disclosure`
**Original synonyms**: `medical NLP;clinical NLP`
**Original negatives**: `drug docking`
**Reason NARROW**: Audience exists; framing too broad for current venue path.

Candidates generated: 1 | Selected: 0

| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |
|------------|------|--------------------------|-------------|-------------|------|
| T43_N1 | noise_pruned | `clinical LLM|methodology disclosure` | 0.000 | +0.000 |  |

**Selected variant details:**

### T53: Test-set contamination audit of healthcare LLM benchmarks

**Original signals**: purity=0.5, citation=4, artifact=2
**Original keywords**: `data contamination|benchmark leakage|MedQA|PubMedQA|MMLU clinical`
**Original synonyms**: `training data leakage;memorization;n-gram overlap`
**Original negatives**: `unrelated NLP`
**Reason NARROW**: Audience exists; framing too broad for current venue path.

Candidates generated: 5 | Selected: 2

| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |
|------------|------|--------------------------|-------------|-------------|------|
| T53_N5 | noise_pruned | `data contamination|benchmark leakage|PubMedQA|MMLU clinical` | 0.500 | +0.000 | ✓ |
| T53_N1 | primary_anchor | `data contamination reinforcement learning|benchmark leakage|…` | 0.250 | +0.000 | ✓ |
| T53_N2 | primary_anchor | `data contamination static dynamic|benchmark leakage|PubMedQA` | 0.250 | +0.000 |  |
| T53_N3 | primary_anchor | `data contamination dynamic evaluation|benchmark leakage|PubM…` | 0.250 | +0.000 |  |
| T53_N4 | primary_anchor | `data contamination static dynamic evaluation|benchmark leaka…` | 0.250 | +0.000 |  |

**Selected variant details:**

#### T53_N5 — noise_pruned
- **Title**: Test-set contamination audit of healthcare LLM benchmarks — noise-pruned
- **Keywords**: `data contamination|benchmark leakage|PubMedQA|MMLU clinical`
- **Synonyms**: `training data leakage;memorization;n-gram overlap`
- **Negatives**: `unrelated NLP;MedQA`
- **Narrowing note**: removed noisy secondaries=['MedQA']; added to negatives
- **Est. relevance purity**: 0.500 (parent: 0.500, gain: +0.000)
- **Est. kept papers**: 34 (hi-relevance: 33)
- **Est. citation_signal**: 4/5
- **Est. artifact_opportunity**: 2/5
- **Est. NIW/EB1A/Career**: 5/4/3
- **Est. novelty risk**: HIGH
- **Composite score**: 0.6250

#### T53_N1 — primary_anchor
- **Title**: Test-set contamination audit of healthcare LLM benchmarks — focused on reinforcement learning
- **Keywords**: `data contamination reinforcement learning|benchmark leakage|PubMedQA`
- **Synonyms**: `training data leakage;memorization;n-gram overlap`
- **Negatives**: `unrelated NLP;MedQA`
- **Narrowing note**: compound primary='data contamination reinforcement learning'; dropped noisy=['MedQA']
- **Est. relevance purity**: 0.250 (parent: 0.500, gain: +0.000)
- **Est. kept papers**: 1 (hi-relevance: 0)
- **Est. citation_signal**: 1/5
- **Est. artifact_opportunity**: 2/5
- **Est. NIW/EB1A/Career**: 5/4/3
- **Est. novelty risk**: LOW
- **Composite score**: 0.5000

### T74: Open structured-metadata dataset of LLM-eval papers

**Original signals**: purity=0.25, citation=3, artifact=2
**Original keywords**: `LLM evaluation methodology|metadata|systematic mapping`
**Original synonyms**: `evaluation survey;benchmarking practices`
**Original negatives**: `tutorial`
**Reason NARROW**: Audience exists; framing too broad for current venue path.

Candidates generated: 1 | Selected: 1

| Variant ID | Type | New keywords (truncated) | Est. purity | Purity gain | Sel? |
|------------|------|--------------------------|-------------|-------------|------|
| T74_N1 | noise_pruned | `LLM evaluation methodology` | 0.500 | +0.250 | ✓ |

**Selected variant details:**

#### T74_N1 — noise_pruned
- **Title**: Open structured-metadata dataset of LLM-eval papers — noise-pruned
- **Keywords**: `LLM evaluation methodology`
- **Synonyms**: `evaluation survey;benchmarking practices`
- **Negatives**: `tutorial;metadata;systematic mapping`
- **Narrowing note**: removed noisy secondaries=['metadata', 'systematic mapping']; added to negatives
- **Est. relevance purity**: 0.500 (parent: 0.250, gain: +0.250)
- **Est. kept papers**: 1 (hi-relevance: 1)
- **Est. citation_signal**: 1/5
- **Est. artifact_opportunity**: 3/5
- **Est. NIW/EB1A/Career**: 2/4/4
- **Est. novelty risk**: LOW
- **Composite score**: 0.5350

## Notes

- All estimates are simulated against the *existing* dedup paper corpus.
  A full re-run with `10_run_pipeline.py` will re-collect evidence with the
  narrowed queries and produce authoritative scores.
- Variants with `est_relevance_purity < 0.25` are still included if the
  composite score is competitive; they may benefit from expanded evidence.
- GO gate still requires: purity>=0.4, artifact>=3, citation>=3, overall>=14,
  venue>=2, n_reviews>0, reviewer dec_score>=2.0 after the real pipeline run.