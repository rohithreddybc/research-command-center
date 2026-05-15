# T02 — Position-Bias Quantification Across Judge Models
## Execution Protocol

*Project status: Bridge publication candidate (selected per `reports/BRIDGE_PUBLICATION_STRATEGY.md`)*
*Pipeline source: blind_citation profile, run c805933 (2026-05-11)*
*EW profile: 0 paper direct / 0 artifact direct — strongest in pool*

---

## 1. Goal

Produce a peer-reviewed publication that systematically quantifies position bias in
LLM judge models — the tendency of an LLM acting as judge to prefer responses based
on their position in the prompt rather than their substantive quality.

Deliverables:
1. An **8-page paper** (EMNLP Findings format) submitted to ARR.
2. An **open-source evaluation harness** (`judge-bias-eval` Python package).
3. An **arXiv preprint** posted concurrently with submission.

---

## 2. Hypotheses

### H1 (primary)
For a fixed pair of candidate responses {A, B}, the probability that an LLM judge
prefers the response in position 1 differs significantly from 0.5, after controlling
for response quality.

**Operationalisation**: For each judge model j and task t, compute the Position
Bias Index (PBI):

```
PBI(j, t) = | P(judge prefers position 1 | A=B in quality) - 0.5 | × 2
```

Range: [0, 1]. PBI > 0.05 is operationally significant. PBI > 0.20 is severe.

### H2 (secondary)
Rank-order over a leaderboard of N candidates is unstable under position permutation.
Specifically, Kendall's τ between rankings under different position orderings is < 0.85
for at least one judge model on at least one task.

### H3 (exploratory)
Position bias magnitude is correlated with (a) judge model size, (b) judge model
training family, and (c) task complexity (defined as median response length).

---

## 3. Models Under Test

| Judge Model | API | Cost / 1M tokens (input/output) | Why included |
|---|---|---|---|
| **GPT-4o-2024-08-06** | OpenAI | $2.50 / $10.00 | Industry-standard judge; mandatory |
| **Claude 3.5 Sonnet (claude-sonnet-4-5)** | Anthropic | $3.00 / $15.00 | Industry-standard judge; mandatory |
| **Llama-3.3-70B-Instruct** | Together AI / Groq | ~$0.60 / $0.60 | Open-weights frontier judge |
| **Mistral-Large-2** | Mistral / Together | ~$2.00 / $6.00 | Diversifies model family |
| **Gemini-2.0-Flash** | Google AI Studio | ~$0.075 / $0.30 | Cost-efficient frontier; family diversity |

**Why 5 (not 3)**: Reviewers will ask "does this generalise?". 5 models from 5 different
training pipelines (OpenAI, Anthropic, Meta, Mistral, Google) is the minimum to claim a
cross-family pattern.

**Why not include open small judges (Llama-8B, Mistral-7B)?**
Optional — include in extended version. For MVP, the 5 frontier models above are sufficient
and cheaper to run at scale than a long-tail of small judges.

---

## 4. Tasks

| Task | Source dataset | Format | Why |
|---|---|---|---|
| **T-Sum**: Pairwise summary preference | CNN/DailyMail (validation) | Pick A or B | Standard summarisation eval; Wang et al. 2023 used this |
| **T-QA**: Pairwise long-form QA preference | TruthfulQA (open-ended) or NaturalQuestions (long-form) | Pick A or B | Tests judge robustness on open-ended factual answers |
| **T-Code**: Pointwise code-quality scoring | HumanEval reference solutions + perturbed alternates | Score 1-5 | Tests pointwise (not just pairwise) judging |

**Sample size per task**: 200 unique input items × 5 judges × 4 position conditions
= 4,000 judge calls per task. Total ≈ 12,000 calls across 3 tasks.

**Cost estimate** (worst-case Claude / GPT-4o pricing, ~500-token prompts + 50-token answers):
~$60 per 1,000 calls × 12 = **~$720 total API budget**. Add 30% buffer = **$950**.

If budget-constrained: drop to 100 items per task → ~$500.

---

## 5. Position Conditions

For each (model, task, item) triple, run all four conditions:

| Code | Description |
|---|---|
| **C1: A_first** | Candidate A appears first |
| **C2: B_first** | Candidate B appears first (swap) |
| **C3: random** | Position randomised per call (5 trials, majority vote) |
| **C4: blinded** | Both candidates labelled "Response 1" and "Response 2" with no other position cue (test of whether the bias persists when the model is asked to be position-aware) |

**Critical**: For pairwise tasks (T-Sum, T-QA), candidates A and B come from a pool
where ground-truth quality is **calibrated** — either via human annotation
(use existing benchmark labels) or by deliberately constructing AB pairs of equal
quality (e.g., paraphrases of the same answer).

For T-Code, since it's pointwise, position bias measures the difference in score
when the same item is scored after seeing different "preceding" examples in the prompt.

---

## 6. Metrics

### Primary
- **PBI** (Position Bias Index): see §2.H1
- **Kendall's τ**: rank-order consistency between C1 and C2 conditions
- **Score-distribution distance**: Wasserstein-1 distance between score distributions
  under C1 and C2 (for T-Code)

### Secondary
- **Inter-judge agreement** (Cohen's κ) under each position condition — does position
  bias also affect cross-judge consensus?
- **Position-bias decay**: does PBI decrease with chain-of-thought prompting,
  explicit position-bias warnings, or randomised-position averaging?

### Statistical protocol
- **95% CIs**: bootstrap (1000 resamples) for PBI per (model, task).
- **Multiple comparisons**: Benjamini-Hochberg correction at q=0.05 across 5 models × 3 tasks = 15 tests.
- **Pre-registration**: hypotheses + analysis plan committed to OSF before running experiments.
  Even if not formally pre-registered, the protocol is committed in this file before code is written.

---

## 7. Differentiator vs Existing Work

| Closest existing work | What we add |
|---|---|
| Wang et al. 2023 "Large Language Models are not Robust Multiple Choice Selectors" | Studies position bias in **task answering**, not in **judging**. We focus on the judge-as-evaluator setting. |
| Zheng et al. 2023 "Judging LLM-as-a-Judge with MT-Bench" | Acknowledges position bias but doesn't quantify it across models systematically. We provide PBI scores for 5 frontier models on 3 tasks. |
| MTRAG / G-EVAL papers | Use LLM judges but don't characterise bias. We provide a tool (`judge-bias-eval`) for any future judge user to quantify their pipeline's bias. |

**One-paragraph differentiator** (use in intro and rebuttal):

> While prior work has documented position bias in LLM multiple-choice answering
> (Wang et al. 2023) and noted its presence in pairwise judging (Zheng et al. 2023),
> no systematic cross-model quantification has been published. This paper provides
> (a) a Position Bias Index (PBI) metric, (b) PBI measurements for 5 frontier judge
> models across 3 task families, (c) rank-order stability analyses showing that
> small PBI values can produce large leaderboard reorderings, and (d) an open-source
> evaluation harness (`judge-bias-eval`) that any practitioner can apply to
> their own judge configuration. We do not propose a new judge architecture; we
> provide a calibration tool for the judges that already exist in production.

---

## 8. Timeline (16 weeks → submission)

| Week | Milestone | Deliverable |
|---|---|---|
| 1 | Literature lock + protocol freeze | This document signed off; pre-registration on OSF |
| 1 | Code scaffold | `judge-bias-eval` repo skeleton (see CODE_SCAFFOLD.md) |
| 2 | Dataset preparation | 200 items × 3 tasks loaded with calibration metadata |
| 2 | API key acquisition | OpenAI, Anthropic, Together, Google AI Studio keys obtained |
| 3 | Pilot: 50 items × 2 judges × 1 task | Pilot results inspected; protocol refined if needed |
| 4–6 | Full data collection | All 12,000 judge calls completed; raw logs in `data/runs/` |
| 7 | Cleaning + initial analysis | Cleaned data; PBI computed per (model, task) |
| 8 | Statistical analysis | Bootstrap CIs, Kendall τ, BH correction; tables and plots |
| 9–10 | Paper draft v1 | Sections 1–5 (intro, related, method, results) |
| 11 | Paper draft v2 | Sections 6–7 (discussion, conclusion); figures finalised |
| 12 | Internal review | Send to 1–2 trusted readers for feedback |
| 13 | Revisions | Address feedback; tighten claims; finalise abstract |
| 14 | arXiv preprint | Submit to arXiv (cs.CL primary, cs.AI secondary) |
| 15 | ARR submission | Submit to current ARR cycle |
| 16 | Buffer | Slack for unexpected delays |

**Total elapsed**: 4 months (16 weeks) from week-1 commit to ARR submission.
**Realistic with daytime job**: 5–6 months. Add 2-month buffer.

**Hard kill date**: if no submission by week 24 (6 months), reassess (see KILL_CRITERIA.md).

---

## 9. Reproducibility Plan

- **Code**: MIT license, GitHub repo `judge-bias-eval`, version-tagged release per result figure
- **Data**: All judge calls logged with prompt + raw response in `data/runs/<run_id>.jsonl`
- **Random seeds**: Fixed seed 42 for all sampling steps; documented per result
- **API versions**: Pinned model snapshot dates (e.g., `gpt-4o-2024-08-06` not `gpt-4o`)
- **Compute environment**: `requirements.txt` + Dockerfile; results runnable in single container
- **Replication budget**: A reviewer can replicate any single (model, task) result
  for ~$50; full paper for ~$1,000

---

## 10. Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| New paper on identical topic appears on arXiv | Medium | High | `scripts/15_arxiv_watch.py` runs weekly; if scoop appears, see KILL_CRITERIA.md |
| API model versions change mid-run | Low | Medium | Pin model snapshot dates; re-run any partial cohort |
| API costs exceed budget | Low | Medium | Hard cap $1,500; dynamic per-task spending limit in code |
| Effect sizes too small to publish | Low | High | Pilot in week 3 will detect; if PBI < 0.02 across all judges, expand to higher-stakes tasks |
| Reviewer rejection at ARR | Medium | Medium | Have TMLR submission ready as alternative; same paper, different format |
| Single-author bias / blind spots | Medium | Low | Internal review in week 12; pre-registration of hypotheses |
| ARR cycle deadline missed | Medium | Low | Submit to next ARR cycle (rolling, no penalty) or directly to TMLR |

---

## 11. Submission Strategy

**Primary**: ARR → EMNLP 2026 Findings
- Deadline: per ARR rolling cycle (check `05_venue_selection/SUBMISSION_CALENDAR_2026-2027.md`)
- Format: 8 pages + unlimited references + appendix
- Anonymous

**If ARR rejects or timeline slips**: Submit directly to **TMLR**
- Rolling submission, no deadline
- Open review (less anonymous but faster turnaround)
- Same paper, slight format adjustment (TMLR allows up to 12 pages)

**If both decline**: Submit to **NAACL 2027** or **EACL 2027** (whichever is next).
Avoid: IEEE Access, PLOS ONE, any Springer/Frontiers journal — APC + reviewer skepticism risk.

---

## 12. Definition of Success

| Metric | Threshold | Stretch |
|---|---|---|
| Paper accepted at peer-reviewed venue | At least 1 of {ARR/EMNLP, TMLR, NAACL, EACL} | EMNLP Main or TMLR |
| arXiv preprint posted | By week 14 | By week 12 |
| `judge-bias-eval` released on GitHub | By submission | 50+ stars within 6 months |
| Total cost | Under $2,000 | Under $1,000 |
| Calendar time to submission | Under 6 months | Under 4 months |
| Citations within 2 years (post-publication) | 10+ | 30+ |

---

## 13. Sign-Off

This protocol is committed before code is written. Changes after pilot
(week 3) require an explicit ADR (Architecture Decision Record) appended to
this file or in `06_paper_pipeline/T02_position_bias/CHANGES.md`.

| Field | Value |
|---|---|
| Protocol version | 1.0 |
| Protocol date | 2026-05-12 |
| Author | rohithreddybc |
| Reviewer | (none — single-author project) |
| Pre-registration link | TBD (OSF pending) |
| Repo | TBD (`github.com/rohithreddybc/judge-bias-eval`) |
