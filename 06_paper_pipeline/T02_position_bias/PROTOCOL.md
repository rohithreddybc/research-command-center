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

## 8. Timeline (13 weeks → workshop submission — re-targeted 2026-05-16)

**Bridge metric is sub→pub time.** The user clarified (2026-05-16) the bridge's
optimization target: shortest time from submission to peer-reviewed publication
at a free venue. Re-analysis in `reports/VENUE_REOPTIMIZATION.md` ranked free
venues on this metric; the winner for an empirical paper is a top-conference
workshop.

**Venue change**: TMLR-direct → **EMNLP 2026 Workshop** (Eval4NLP target).
- TMLR sub→pub: 3–5 months
- EMNLP workshop sub→pub: ~3.5 months
- Workshop also requires shorter draft (8 pages, hard limit) — less drafting effort
- Both publish December 2026 — same calendar outcome with lower drafting cost
- TMLR remains backup if workshop deadline missed

Tightened plan to hit 2026-08-15 EMNLP workshop deadline:

| Week | Date | Milestone | Deliverable |
|---|---|---|---|
| 1 | May 16–22 | Sprint kickoff | Protocol re-signed; code scaffold started (clients/, judge.py, conditions.py) |
| 2 | May 23–29 | Dataset prep + API keys | 200 items × 3 tasks loaded; OpenAI + Anthropic + Together + Google keys verified |
| 3 | May 30 – Jun 5 | Pilot | 50 items × 2 judges × 1 task = 100 calls; outputs manually inspected; protocol refined if needed |
| 4 | Jun 6–12 | Data collection part 1 | T-Sum cohort: 200 × 5 × 4 = 4,000 calls completed |
| 5 | Jun 13–19 | Data collection part 2 | T-QA + T-Code cohorts: 8,000 calls completed |
| 6 | Jun 20–26 | Cleaning + initial analysis | PBI per (model, task); Kendall τ; bootstrap CIs |
| 7 | Jun 27 – Jul 3 | Draft v1 | §1 Intro + §2 Related + §3 Method + §4 Experiments + §5 Results (first pass) |
| 8 | Jul 4–10 | Draft v2 + figures | §6 Discussion + §7 Conclusion; all figures finalised; tables resolved |
| 9 | Jul 11–17 | Internal critique | Self-review; 1 external reader if possible; address blockers |
| 10 | Jul 18–24 | Revisions | Address self-review notes; tighten claims |
| 11 | Jul 25–31 | Format polish | EMNLP workshop LaTeX template; 8-page hard limit check |
| 12 | Aug 1–7 | Final pass + figures | Final figure regeneration; reproducibility appendix; companion repo public |
| 13 | Aug 8–15 | **Submit** | arXiv preprint + EMNLP 2026 Workshop submission by 2026-08-15 |

**Total elapsed**: 13 weeks (91 days) from re-plan to submission.
**Decision date**: ~2026-10-15 (workshop notification typically 8 weeks).
**Camera-ready**: ~2026-11-15.
**Publication**: December 2026 (at EMNLP).
**Sub → Pub time**: ~3.5 months (the user's bridge metric).

**Hard kill date**: if no workshop submission by 2026-08-15:
- Fall back to TMLR direct (submit Aug 20–30; publish Jan–Feb 2027)
- Or wait for ICLR 2027 workshop (submit ~Feb 2027; publish Apr 2027)
- Trigger KILL_CRITERIA K4 review either way

### Scope reductions if behind

If at week 5 (Jun 19) data collection is < 60% done:
- Drop T-Code task (the pointwise one) → 8,000 calls instead of 12,000
- Drop Mistral-Large-2 → 4 models instead of 5
- Combined: 6,400 calls instead of 12,000 — still publishable, less comprehensive

Document any scope reduction in `06_paper_pipeline/T02_position_bias/CHANGES.md`.

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

## 11. Submission Strategy (updated 2026-05-16 — EMNLP workshop is now primary)

**Primary**: **EMNLP 2026 Workshop** (Eval4NLP target; alternatives: BlackboxNLP,
GenBench, TrustNLP, Workshop on Bias in NLP)
- Submission deadline: ~2026-08-15
- Notification: ~2026-10-15
- Camera-ready: ~2026-11-15
- Conference / publication: December 2026
- **Sub → Pub time**: ~3.5 months (fastest free peer-reviewed for empirical work)
- 8-page hard limit (long paper) or 4-page (short paper); we target long
- $0 APC; peer-reviewed; ACL Anthology indexed; USCIS-recognised
- arXiv preprint posted concurrent with submission

**Backup 1**: NeurIPS 2026 Safety / Evaluation Workshop
- Submission ~September 2026; publication December 2026
- Similar timeline; alternative venue if Eval4NLP rejected

**Backup 2**: TMLR direct
- No deadline; submit anytime
- 3–5 months sub→pub
- Higher per-paper prestige; slightly longer review
- Backup if both workshops reject or deadlines missed

**Backup 3**: ICLR 2027 workshop
- Submission ~February 2027; publication April 2027
- Total elapsed longer, but useful if everything 2026 misses

**Backup 4**: NAACL 2027 / EACL 2027 (via later ARR cycles)
- Pushes publication to mid-2027

**Never**: IEEE Access, PLOS ONE, Frontiers, MDPI, any Springer paid-OA route.

### Why workshop over TMLR for the bridge (post 2026-05-16 user clarification)
- ~1 month faster sub→pub (3.5 vs 3-5 mo)
- 8-page hard limit → less drafting time vs 12-page TMLR
- Same publication month (Dec 2026)
- ACL Anthology indexed → equivalent NIW/EB-1A weight
- Trade-off accepted: ~50 fewer expected citations on T02 (workshop ceiling 80,
  TMLR ceiling 150) — but T02's citations come from the survey §6.1 reference
  loop regardless
- See `reports/VENUE_REOPTIMIZATION.md` for the full analysis

### Why NOT TMLR for the bridge
- The user's bridge metric is sub→pub time. TMLR loses on that metric.
- The user's high-citation paper is the SURVEY at TMLR. T02 doesn't need to
  carry citation weight; the survey does.
- Workshop publication is recognised by USCIS as peer-reviewed (criterion vi).

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
| Protocol version | 1.2 (venue re-optimized 2026-05-16 second pass) |
| Protocol date | 2026-05-12 (v1.0); 2026-05-16 (v1.1, v1.2) |
| Author | rohithreddybc |
| Reviewer | (none — single-author project) |
| Pre-registration link | TBD (OSF pending) |
| Repo | TBD (`github.com/rohithreddybc/judge-bias-eval`) |
| Primary venue | **EMNLP 2026 Workshop** (Eval4NLP) |
| Backup venues | NeurIPS 2026 Safety Workshop → TMLR → ICLR 2027 Workshop |
| Submission target | 2026-08-15 |
| Publication target | December 2026 |
| Sub→Pub target | ~3.5 months |
