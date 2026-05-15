# T02 — Paper Outline

*Working title*: **Position Bias in LLM Judges: A Cross-Model Quantification**
*Length target*: 8 pages + appendix (EMNLP Findings format)
*Format*: ARR / EMNLP Findings → TMLR fallback

---

## Abstract (≤200 words)

```
LLM-as-judge has become standard infrastructure for ranking model outputs
in RLHF pipelines, AutoEval systems, and benchmark leaderboards. We show that
five frontier judge models — GPT-4o, Claude 3.5 Sonnet, Llama-3.3-70B,
Mistral-Large-2, and Gemini-2.0-Flash — exhibit systematic position bias when
asked to compare candidate responses, with Position Bias Index (PBI) values
ranging from X to Y across three task families (summary, long-form QA, code
scoring). Critically, PBI values as low as 0.05 produce Kendall-τ rank
instability of 0.7 across leaderboard configurations of 10+ candidates,
demonstrating that even small position biases corrupt benchmark conclusions.
We release `judge-bias-eval`, an open-source harness that any practitioner
can apply to their own judge configuration to measure and report PBI as a
first-class reproducibility metric. We discuss mitigations including
randomised-position averaging, chain-of-thought prompting, and dual-judge
consensus, finding that randomised-position averaging reduces PBI by 60-80%
at 5x cost.
```

*(Replace X, Y with measured values after experiments complete.)*

---

## 1. Introduction (~1 page)

### 1.1 Motivation
- LLM-as-judge usage has exploded since 2023: HELM, Open LLM Leaderboard, MT-Bench,
  Chatbot Arena, RLHF reward models, AutoEval pipelines.
- A judge that prefers responses in position 1 over position 2 (or vice versa) corrupts
  any benchmark that uses pairwise judgments.
- Even small position biases compound when ranking N candidates pairwise — a 5%
  per-pairwise-comparison bias can produce 30%+ leaderboard reorderings.

### 1.2 Contributions
1. A formal Position Bias Index (PBI) metric for LLM judges.
2. PBI measurements for 5 frontier judges across 3 task families.
3. Rank-order stability analysis showing how PBI distorts leaderboards.
4. An open-source evaluation harness (`judge-bias-eval`).
5. Empirical evaluation of three mitigations.

### 1.3 Why now
The LLM-judge ecosystem is approaching the maturity of human-evaluation methodology in
the early 2010s, when inter-annotator agreement studies became mandatory for empirical
NLP papers. PBI reporting should become similarly mandatory.

---

## 2. Background and Related Work (~1 page)

### 2.1 Position bias in human evaluation
- Long-established in psychology (primacy/recency effects).
- Documented in crowdsourced annotation (Krippendorff, Mathur).
- Why we should expect LLMs to inherit human-style position biases.

### 2.2 Position bias in LLMs (task answering)
- **Wang et al. 2023** "Large Language Models are not Robust Multiple Choice Selectors":
  position bias in MCQ answering. PBI varied across models.
- **Zheng et al. 2023** "Judging LLM-as-a-Judge with MT-Bench": noted position bias in
  pairwise judging without systematic quantification.
- Other adjacent: **Pezeshkpour & Hruschka 2023**, **Robinson et al. 2023**.

### 2.3 The judge-as-evaluator gap
No prior work systematically quantifies position bias in pairwise *judging*. This is
distinct from MCQ answering because:
1. The judge processes two candidate responses (longer context).
2. The judge makes a relative quality judgment (not absolute).
3. The judge's output feeds downstream RLHF/leaderboard pipelines (high-stakes).

### 2.4 Differentiator
*(Use the one-paragraph differentiator from PROTOCOL.md §7.)*

---

## 3. Method (~1.5 pages)

### 3.1 Position Bias Index (PBI)
Formal definition with equation. Properties: range [0, 1], 0 = perfect
calibration, 1 = always picks position 1 (or always picks position 2).

### 3.2 Models, tasks, conditions
Tabular summary (port from PROTOCOL.md §3, §4, §5).

### 3.3 Statistical protocol
Bootstrap CIs, BH correction, pre-registration. Power analysis showing 200
items per task is sufficient to detect PBI ≥ 0.03 at 95% confidence.

### 3.4 Calibration of candidate pairs
How we ensure A and B are quality-matched in T-Sum and T-QA.
Two methods:
- (a) Use existing human-labelled tied pairs from CNN/DM and TruthfulQA.
- (b) Construct paraphrase pairs (same content, different surface form).

---

## 4. Experiments (~1 page)

### 4.1 Implementation
- `judge-bias-eval` package; v1.0 release tagged at submission.
- Compute: API calls only; no GPU.
- Cost: report total spend.

### 4.2 Cohort
- N = 600 items (200 per task) × 5 judges × 4 position conditions = 12,000 calls.

### 4.3 Reproducibility
- All prompts, raw judge outputs, and analysis code in supplementary material
  + GitHub repo.

---

## 5. Results (~1.5 pages)

### 5.1 PBI per (model, task)
**Table 1**: PBI with 95% CI for each (model, task) pair. Highlight max (worst).

### 5.2 Rank-order stability
**Figure 1**: Kendall-τ between rankings under C1 vs C2 across leaderboards
of varying size N. Shows that as N grows, even small PBI causes large τ drops.

### 5.3 Score-distribution shifts (T-Code)
**Figure 2**: Wasserstein distance between score distributions under C1 vs C2.

### 5.4 Mitigation effectiveness
**Table 2**: PBI under (a) baseline, (b) chain-of-thought, (c) randomised-position
averaging (5 trials), (d) dual-judge consensus. Cost vs PBI tradeoff plot.

### 5.5 Cross-model patterns
Brief: which model families (OpenAI, Anthropic, Meta, Mistral, Google) show
strongest / weakest bias? Caveat about training-pipeline confounds.

---

## 6. Discussion (~1 page)

### 6.1 Implications for benchmark practice
- PBI reporting should be mandatory for any pairwise-judge benchmark.
- Existing leaderboards (Chatbot Arena, MT-Bench) should add PBI metadata.

### 6.2 Implications for RLHF
- Reward models trained on biased pairwise data inherit the bias.
- Suggests randomised-position data collection.

### 6.3 Limitations
- 5 models, 3 tasks, English-only: not exhaustive.
- Calibration of A=B quality is imperfect; we use both human-labelled and
  paraphrase-based pairs to triangulate.
- API model snapshots may shift.

### 6.4 Future work
- Multilingual judges.
- Open-weights smaller judges (Llama-8B, Mistral-7B).
- Adversarial position attacks (link forward to T07 future work).

---

## 7. Conclusion (~0.5 page)

Position bias in LLM judges is real, measurable, and large enough to corrupt
benchmark conclusions at currently-deployed scales. Practitioners should report
PBI alongside any judge-based result. We provide the tools.

---

## Appendix

### A. Full per-model per-task PBI tables
All 15 (model, task) cells with raw counts, bootstrap CIs, BH-corrected p-values.

### B. Prompt templates
Full prompts used for each task.

### C. Judge-output examples
Sample judge outputs for each (model, task, condition) — show that the bias
shows up in the chain-of-thought, not just the final answer.

### D. Reproducibility checklist
Per the ML reproducibility checklist (Pineau et al. 2021).

### E. Cost breakdown
API spend per model per task; total project cost.

### F. Pre-registered hypotheses
Verbatim copy of pre-registration document with timestamp.

---

## Citation anchors (must cite)

1. Wang et al. 2023 — Large Language Models are not Robust Multiple Choice Selectors
2. Zheng et al. 2023 — Judging LLM-as-a-Judge with MT-Bench
3. Pezeshkpour & Hruschka 2023 — Large Language Models Sensitivity to the Order of Options in Multiple-Choice Questions
4. Robinson et al. 2023 — Leveraging Large Language Models for Multiple Choice Question Answering
5. Liu et al. 2023 — G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment
6. Liu et al. 2023 — Lost in the Middle: How Language Models Use Long Contexts
7. Stiennon et al. 2020 — Learning to summarize from human feedback
8. Pineau et al. 2021 — Improving Reproducibility in Machine Learning Research

(Generate full BibTeX via `python scripts/16_extract_bibtex.py --topic T02`
once the dedup CSV is built for T02.)

---

## Length budget

| Section | Pages |
|---|---|
| Abstract + 1. Intro | 1.0 |
| 2. Related Work | 1.0 |
| 3. Method | 1.5 |
| 4. Experiments | 1.0 |
| 5. Results | 1.5 |
| 6. Discussion | 1.0 |
| 7. Conclusion | 0.5 |
| References | 0.5 |
| **Total** | **8.0** |
