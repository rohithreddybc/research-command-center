# Bridge Publication Strategy
*Derived from blind_citation pipeline run — commit c805933 (2026-05-11)*
*Cross-referenced with: PERSONAL_OVERLAY_REPORT, GO_READINESS_DOSSIERS, final_decision_report*

---

## 0. Design Constraints

This strategy optimises for:
- **Legitimacy** over speed — no predatory venues, no exploitative open-access journals
- **Research identity alignment** — every candidate must deepen the AI evaluation / LLM reliability / reproducibility cluster
- **Solo execution** — scope calibrated to single author in 3–6 months
- **Complementarity** — must not scoop JudgeSense (NeurIPS), the survey (ACM), or the clinical paper (in progress)
- **NIW/EB1A usability** — peer-reviewed, DBLP-indexed, independently citable
- **No personal-goal-only topics** — only bc_acceptable topics are in scope

Topics from the current pipeline that FAIL the blind_citation gate are **excluded even if they have high NIW/career scores**. This is the exact rule the pipeline enforces.

---

## 1. Candidate Identification Methodology

The candidate pool derives from the 6 topics that passed `blind_citation_acceptable=True`
in the balanced neutral pipeline run (36 topics, blind_citation profile, LLM panel of 8 neutral reviewers):

| Topic | Title | bc_score | Paper Direct | Artifact Direct | EW Status | Personal-profile safe |
|---|---|---|---|---|---|---|
| **B05** | Synthetic data quality evaluation metrics | 26.50 | 0 | 5 | Clean | 3 of 4 profiles |
| **B12** | Multi-lingual factuality benchmark for low-resource languages | 24.00 | 1 | 29 | Moderate diff required | 0 of 4 profiles |
| **T07** | Judge robustness to candidate-side prompt injection | 23.80 | 0 | 12 | Artifact diff required | **4 of 4 profiles** |
| **T01** | Cross-judge agreement on long-context QA | 23.46 | 0 | 3 | Clean | 3 of 4 profiles |
| **B11** | Distribution-shift detection for production ML | 23.00 | 0 | 1 | Clean | 0 of 4 profiles |
| **T02** | Position-bias quantification across judge models | 22.16 | 0 | **0** | **Cleanest** | 1 of 4 profiles |

All 6 have: `go_blocked=False`, `decision=NARROW`, `confidence=MEDIUM`.

**B12 is eliminated from bridge consideration** immediately: 29 direct artifacts (high_artifact_overlap=True),
1 direct peer-reviewed paper, and moderate-only differentiator — creating a benchmark here requires
substantial low-resource language resources that are not feasible for a solo author in 3–6 months.
It is catalogued below but not recommended.

**B11 is de-prioritised** as a bridge candidate because: (1) the research identity is ML-systems /
production ML, which is adjacent to but not core to the evaluation/LLM-judge cluster; (2) it has
0 overlap in personal-goal profiles — which means it is pure academic but does not strengthen
any immigration or career narrative; (3) a "framework" artifact target requires more engineering.
It is catalogued as a long-term candidate only.

**Remaining bridge candidates: T02, T01, T07, B05.**

---

## 2. Candidate Scoring Matrix (Bridge-Specific Criteria)

| Criterion | T02 | T01 | T07 | B05 | B11 | B12 |
|---|---|---|---|---|---|---|
| **bc_score (pipeline)** | 22.16 | 23.46 | 23.80 | 26.50 | 23.00 | 24.00 |
| **EW: paper_direct** | **0** | 0 | 0 | 0 | 0 | 1 |
| **EW: artifact_direct** | **0** | 3 | 12 | 5 | 1 | 29 |
| **EW: diff_strength (paper)** | strong | strong | strong | strong | strong | moderate |
| **EW: diff_strength (artifact)** | **strong** | moderate | moderate | moderate | moderate | moderate |
| **Citation signal (0–5)** | 4 | 5 | 5 | 5 | 4 | 5 |
| **Saturation (0–5, high=good)** | 3 | 3 | 3 | 3 | 3 | 4 |
| **Venue signal (0–5)** | 2 | 2 | 2 | 4 | 4 | 4 |
| **Evidence quality (0–5)** | 4 | 3 | 4 | 5 | 5 | 5 |
| **Kept papers** | 17 | 12 | 38 | 80 | 39 | 80 |
| **NIW (0–5)** | 2 | 2 | 4 | 2 | 2 | 2 |
| **EB-1A (0–5)** | 4 | 5 | 5 | 5 | 4 | 4 |
| **Career/FAANG (0–5)** | 3 | 4 | 5 | 3 | 3 | 3 |
| **Solo executability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| **JudgeSense synergy** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐ | ⭐ |
| **arXiv preprint advisable** | No (no urgency) | No | **YES (urgent)** | No | No | No |
| **Workshop-first makes sense** | Yes | Yes | Yes | No | No | No |
| **Fastest realistic submission** | **3–4 months** | 4–5 months | 5–7 months | 5–7 months | 6–9 months | 9–12 months |

---

## 3. Deep Dives: Bridge Candidates

---

### 3.1  T02 — Position-Bias Quantification Across Judge Models

**Title**: *Position-bias quantification across judge models*
**Target artifact**: Empirical study + evaluation harness (Python package)
**Category**: eval
**JudgeSense synergy**: DIRECT — position bias is one of the core failure modes JudgeSense addresses.
This paper can be framed as a companion empirical study that characterises the problem JudgeSense solves.

#### Why selected
- **Cleanest existing-work profile in the entire pipeline**: 0 paper direct, 0 artifact direct, 10 partial papers only.
  Paper and artifact differentiator strength both = `strong`. No competitor benchmark exists.
- Fastest solo execution: the experiment is a controlled empirical study — take 3–5 judge models,
  swap response ordering, measure score distributions. No new dataset collection. No clinical domain access.
  No low-resource language resources. No adversarial attack implementation.
- Directly extends the JudgeSense citation cluster: a reader of your NeurIPS paper who wants to understand
  position bias in depth will naturally cite this paper. It creates a citation loop around your identity.
- `citation_signal=4`, `eb1a=4`, `career=3` — solid across all three immigration/career dimensions.
- Existing partial papers (Wang et al. 2023 "Large Language Models are not Robust Multiple Choice Selectors"
  is the canonical adjacent work) study position bias in *task answering*, not in *judging*. The judge-specific
  angle is the precise differentiator. No paper has run a multi-judge, multi-task, multi-ordering study
  with a released harness.

#### Venue type: Empirical NLP / Benchmark Track
**Primary**: ACL Rolling Review (ARR) → EMNLP 2026 Findings or Main
- Free to submit, free to publish (no APC), DBLP indexed, Google Scholar indexed, ACL Anthology.
- Highly respected. No predatory concerns. Strengthens reviewer/collaboration opportunities directly.
- Preprints allowed (encouraged): post to arXiv before or concurrent with submission.
- Review difficulty: Medium. Reviewers will ask for broader model coverage and more tasks.
- Reviewer skepticism risk: Low-medium. The topic is well-understood; reviewers may say
  "Wang et al. 2023 already covers this" — rebuttal is: judge-specific quantification + released harness.

**Alternative**: TMLR (Transactions on Machine Learning Research)
- No APC. Rolling submission. ~3–5 month review. DBLP, Google Scholar indexed.
- Accepted by immigration authorities as peer-reviewed publication.
- Allows and encourages arXiv preprints.
- Review difficulty: Medium-high (TMLR reviewers are thorough; expect 2 rounds).
- Why TMLR is preferred over a lower-tier conference: it is continuously indexed and more prestigious
  than many mid-tier venues. For NIW/EB1A, a TMLR publication is stronger than an EMNLP Findings
  rejection-and-revise cycle.

**Workshop first**: Eval4NLP (Evaluation & Comparison of NLP Systems) at EMNLP 2026.
- Peer-reviewed workshop with proceedings in ACL Anthology.
- Provides early community feedback before TMLR/EMNLP submission.
- No APC. Timeline: submit ~August 2026 if EMNLP 2026 Eval4NLP schedule holds.
- Risk: workshop venue does not count as main publication for NIW; use it as a stepping stone only.

**Not recommended**: IEEE Access (APC ~$1,995; lower prestige for this topic). PLOS ONE
(APC applies; not the right venue for NLP evaluation). Any predatory journal.

#### Execution scope (minimum viable paper)
- 4–5 judge models: GPT-4o, Claude 3.5 Sonnet, Llama-3-70B-Instruct, Mistral-Large, Gemini Flash
- 3 tasks: pairwise preference rating (summary quality), pairwise preference rating (QA), pointwise scoring (code)
- 4 position conditions: [A, B], [B, A], randomised 5×, position-masked (with score normalisation)
- Metrics: position bias index (PBI), rank-order consistency under swapping, Kendall-τ agreement across conditions
- Artifact: Python evaluation harness (`judge-bias-eval` pip package) + result logs + leaderboard template
- Length: 8 pages + appendix, EMNLP Findings format

#### Fastest credible path
Submit to ARR June 2026 → commitment deadline August 2026 → EMNLP 2026 Findings (December 2026).
Total calendar time: ~7 months from now to publication.

#### Strongest long-term path
Submit to TMLR after arXiv preprint. If accepted, cite in future JudgeSense follow-up.
Create a leaderboard on the HuggingFace Space for ongoing community tracking.
This becomes a reference point for anyone deploying LLM judges.

#### Best bridge path
ARR → EMNLP 2026 Findings. Post arXiv preprint at submission time to establish priority.
Cite in the JudgeSense paper if NeurIPS review allows author response with new citations.

#### Review timeline estimate
- ARR → EMNLP 2026: submit June/July → decision October → camera-ready November → published December 2026
- TMLR: submit anytime → 3–5 month review → published 1–2 months after acceptance
- Eval4NLP workshop: submit August → decision September → published November 2026

#### Citation upside
Medium-high. Position bias in judges is a growing concern. Anyone building LLM judge pipelines
(RLHF teams, evaluation researchers, AutoEval practitioners) will want a systematic reference.
Expected citations in 3 years: 50–150 if released with a usable harness.

#### NIW/EB1A usefulness
**NIW**: Moderate (2/5 raw NIW signal). Arguable under "substantial merit" — LLM judge reliability
affects AI system trustworthiness broadly. Not primarily healthcare or safety, but arguable.
**EB-1A**: Strong (4/5). Evidence of original scholarly contribution with a released benchmark.
Peer-reviewed publication at EMNLP or TMLR is a credible EB-1A exhibit.

#### FAANG/career signaling
Moderate (3/5). Shows empirical rigor, benchmark-building skills, familiarity with frontier models.
Not a systems paper, so less direct for FAANG engineering roles, but strong for FAANG research roles
(Google Brain, DeepMind, OpenAI, Anthropic, Meta FAIR).

#### Hidden overlap risk
**Low**. Wang et al. 2023 is the closest but covers task-answering, not judging.
No artifact or paper directly covers the judge-specific + multi-model + harness angle.
Risk: a preprint on this exact topic could appear on arXiv during your execution window.
Mitigation: post arXiv preprint as soon as experiments are complete (month 3).

---

### 3.2  T01 — Cross-Judge Agreement on Long-Context QA

**Title**: *Cross-judge agreement on long-context QA*
**Target artifact**: Benchmark (agreement study + dataset)
**Category**: eval
**JudgeSense synergy**: HIGH — inter-judge agreement is the core reliability question that
JudgeSense addresses. A cross-judge agreement study on a specific, underserved domain
(long-context QA) is a natural companion.

#### Why selected
- 0 paper direct overlaps, 3 artifact direct (all moderate differentiator strength).
  The long-context-specific scoping is the differentiator: general inter-judge agreement
  is studied, but cross-judge agreement specifically on long-context QA (multi-document,
  long-passage) is not systematically characterised.
- `citation_signal=5` — the highest citation signal, tied with T07 and B05.
- `eb1a=5` — strongest EB-1A signal among the bridge candidates.
- `career=4` — good career alignment (long-context models are active at Google, Meta, OpenAI).
- Thin evidence corpus (12 kept papers, 1 evidence source) is a risk signal but also suggests
  the specific angle is underserved.

#### Why it is ranked #2 (not #1) for bridge
- Evidence corpus is the thinnest of any bc_acceptable topic (12 papers, 1 source).
  This implies either genuine novelty or inadequate query coverage. Pipeline cannot distinguish.
- Execution requires access to long-context benchmarks (e.g. QuALITY, SCROLLS, Loong) and
  2–3 judge APIs — feasible but more infrastructure than T02.
- The "cross-judge" angle is less differentiated than "position-bias" — there are more papers
  on judge agreement in general, even if long-context-specific work is sparse.

#### Venue type: NLP Benchmark / Empirical
**Primary**: ARR → ACL 2026 Findings (if timeline permits) or EMNLP 2026 Findings
**Alternative**: TMLR (rolling)
**Workshop**: LongContext workshop (EMNLP 2026 if scheduled) or Eval4NLP

#### Execution scope (minimum viable paper)
- 3 long-context QA benchmarks: QuALITY, SCROLLS-QASPER, NarrativeQA (or equivalent)
- 4 judge models: GPT-4o, Claude Sonnet, Llama-3-70B-Instruct, Gemini Pro
- Metrics: pairwise inter-judge agreement (Cohen's κ, Krippendorff's α), disagreement pattern analysis
  (where do judges diverge: long-context retrieval vs reasoning vs factuality)
- Artifact: agreement study dataset + scoring harness

#### Review timeline estimate
ARR → EMNLP 2026: submit June/July → December 2026 publication.
TMLR: 5–7 months from submission.

#### Citation upside
High (5/5 citation signal). Long-context evaluation is a hot area. Results would be cited by
anyone building long-context QA systems or judge pipelines for document-level tasks.

#### NIW/EB1A usefulness
EB-1A: Strong (5/5). NIW: Weak (2/5) — not healthcare-adjacent.

#### FAANG signaling
Good (4/5). Long-context is a key area for Google Gemini, Anthropic Claude, Meta Llama.

#### Hidden overlap risk
Medium. The long-context QA space is growing rapidly. Risk that a paper on judge agreement
in long-context settings appears on arXiv before submission. Mitigate by posting arXiv preprint
concurrent with submission.

---

### 3.3  T07 — Judge Robustness to Candidate-Side Prompt Injection

**Title**: *Judge robustness to candidate-side prompt injection*
**Target artifact**: Benchmark (injection test suite + evaluation harness)
**Category**: eval + safety
**JudgeSense synergy**: VERY HIGH — this extends JudgeSense into adversarial settings.
The combination of JudgeSense + this paper establishes a two-paper cluster on judge reliability,
which is a strong EB-1A narrative: original contribution (JudgeSense) + systematic study of
a specific failure mode (T07).

#### Why selected
- **Safe under all 4 personal-goal profiles** — unique in the entire pipeline.
  `bc_score=23.8`, `citation=5`, `NIW=4`, `EB-1A=5`, `career=5`.
- 0 peer-reviewed direct papers. The judge-as-target threat model is absent from existing
  peer-reviewed work (all existing prompt injection benchmarks target assistant models,
  not evaluator LLMs).
- Distinct from JudgeSense: JudgeSense evaluates judge reliability under normal conditions;
  T07 studies adversarial manipulation of judges. No overlap in scope.

#### Why it is ranked #1 for LONG-TERM but #3 for bridge
- Execution is more complex: requires building an injection attack taxonomy,
  running attacks across 3+ judge models × 4+ injection types × 3+ tasks.
  Realistic execution time: 5–7 months.
- 12 direct artifacts (high_artifact_overlap=True). Artifact differentiator is `moderate`.
  The paper must be very explicit about the judge-target framing in abstract/intro.
  Reviewers who skim will misfile this as another prompt injection paper.
- A critical blocking paper must be read first: "Red Teaming the Mind of the Machine"
  (arXiv 2025, relevance 0.625 in pipeline). If that paper covers judge models as targets,
  scope must narrow further before any work begins.
- **arXiv preprint is URGENT**: post a technical report / position paper establishing the
  judge-target threat model AS SOON AS the blocking paper is cleared (within 2 weeks of
  verifying the gap). This establishes priority against the growing artifact ecosystem.

#### Venue type: Security + NLP intersection / Safety track
**Primary**: EMNLP 2026 Main or ACL 2026 Main (if timing permits)
**Security angle**: IEEE S&P 2027 Workshop on LLM Security (if framed as security paper)
**Alternative**: NeurIPS 2026 Safety Track
**Rolling fallback**: TMLR
**Workshop first**: TrustNLP or LLM Safety workshop at ACL/EMNLP 2026

#### Execution scope (minimum viable paper)
- Attack taxonomy: 5 injection types (score override instruction, role confusion, distractor injection,
  format hijacking, confidence override)
- Judge models: GPT-4o, Claude 3.5 Sonnet, Llama-3-70B-Instruct (3 is sufficient for MVP)
- Tasks: pairwise preference rating (3 tasks: summary, QA, code)
- Metrics: injection success rate, score distortion magnitude, judge rank-order corruption
- Defense baselines: system prompt hardening, dual-judge consensus
- Artifact: injection test suite + harness (pytest-compatible)

#### arXiv strategy
Post within 2 weeks of clearing the "Red Teaming" paper risk. Frame as a technical report
establishing the threat model, even before experiments are complete. This is the one topic
in the candidate pool where arXiv-first is NOT optional — it is strategically necessary
given the active artifact ecosystem (12 direct, 25 partial artifacts from the community).

#### Review timeline estimate
ARR → EMNLP 2026: submit July/August → decision October → December 2026 (tight).
More realistic: ARR → ACL 2027 or EMNLP 2027 → July/December 2027.
TMLR: submit anytime, 5–7 months review.

#### Citation upside
Very high. RLHF practitioners, safety researchers, red teams at model providers.
50–200+ citations expected in 3 years if paper is published at a top venue.

#### NIW/EB1A usefulness
**NIW**: Strong (4/5). Judge robustness is a national interest argument —
LLM judges are used in AI safety evaluation, hiring, medical information triage.
Adversarial manipulation of these systems is a public safety concern.
**EB-1A**: Very strong (5/5). Original contribution (judge-as-target threat model),
released benchmark, top-venue publication. Most compelling EB-1A exhibit of any candidate.

#### FAANG signaling
Very high (5/5). OpenAI, Anthropic, Google DeepMind, and Meta all deploy LLM judges
in their RLHF pipelines. Security of these pipelines is an active concern.

#### Hidden overlap risk
High (relative to T02). The 2025 arXiv paper "Red Teaming the Mind of the Machine"
is the single key risk. **Read it before starting any execution work on T07.**
Secondary risk: one of the 12 artifact teams publishes a companion paper.

---

### 3.4  B05 — Synthetic Data Quality Evaluation Metrics

**Title**: *Synthetic data quality evaluation metrics*
**Target artifact**: Framework (evaluation toolkit)
**Category**: data-centric
**JudgeSense synergy**: Moderate — synthetic data evaluation is adjacent to LLM evaluation
but is a different subdomain. Does not directly strengthen the JudgeSense citation cluster.

#### Why selected
- **Highest bc_score** in the entire pipeline (26.5). Citation=5, EB-1A=5, venue=4.
- 0 paper direct overlaps, 5 artifact direct (not high_artifact). Strong paper differentiator.
- `venue_signal=4` — the broadest venue fit of all candidates.
- The data-centric AI space is active and growing. Synthetic data quality evaluation is a
  recognised gap: frameworks exist for specific domains (tabular, image) but cross-domain
  systematic evaluation is underserved.
- Evidence quality=5, kept_papers=80 — the strongest evidence corpus in the pool.

#### Why it is ranked #4 for bridge (not #2 or #3)
- Target artifact = **framework** — this requires building an evaluation toolkit, not just
  running experiments. Framework papers require more engineering time and scope than empirical studies.
  Solo execution in 3–4 months is hard; 5–7 months is realistic.
- Research identity alignment is **moderate**, not strong. B05 is data-centric AI,
  not LLM evaluation or judge reliability. Publishing here does not deepen the JudgeSense
  citation cluster. It establishes you in a *different* subfield.
- Not in personal-goal top-8 under NIW (too low NIW signal).
- Recommended as a **second or third paper**, not the bridge paper, unless your pivot is
  toward data-centric AI.

#### Venue type: Data-Centric / Benchmark Track
**Primary**: NeurIPS 2026 Datasets & Benchmarks Track (deadline ~May/June 2026 — check)
**Alternative**: TMLR (rolling, no APC)
**Journal**: JMLR (prestigious, no APC, but 12–18 month timeline)
**Workshop**: DMLR (Data-centric Machine Learning Research) workshop

#### Review timeline estimate
NeurIPS D&B: deadline June 2026 → decision August → camera-ready October → December 2026.
TMLR: rolling, 4–6 months from submission.

#### Citation upside
Very high (5/5 citation signal). Synthetic data is becoming infrastructure for LLM training.
A framework paper here could accumulate 100–300+ citations over 5 years.

---

### 3.5  B11 — Distribution-Shift Detection for Production ML

**Title**: *Distribution-shift detection methods for production ML*
**Target artifact**: Framework
**Category**: ml-systems

#### Why de-prioritised
- Personal profiles: 0 of 4 safe. NIW=2, career=3 — weaker alignment than other candidates.
- Research identity mismatch: production ML monitoring is a different area from LLM evaluation.
  Publishing here creates a split identity, which is harmful for NIW/EB-1A (requires a coherent
  research narrative).
- Framework artifact target: harder to scope for solo execution.
- Venue signal=4 but venue fit is for MLSys, ICLR, or NeurIPS — highly competitive venues
  where a single-author paper without institutional affiliation faces bias.
- Recommended only if you have a strong pre-existing interest in ML systems / deployment.

**Not recommended as a bridge publication.**

---

### 3.6  B12 — Multi-Lingual Factuality Benchmark for Low-Resource Languages

**Title**: *Multi-lingual factuality benchmark for low-resource languages*
**Category**: eval (multilingual NLP)

#### Why eliminated
- 29 direct artifact overlaps (high_artifact_overlap=True, moderate differentiator).
  The multilingual factuality benchmark space is crowded at the artifact level.
- 1 direct peer-reviewed paper (relevance ≥ 0.65) — only bc_acceptable topic with any direct paper overlap.
- Building a credible low-resource language benchmark requires native speaker annotation,
  specialized datasets, and domain expertise that is hard to acquire solo.
- Research identity: multilingual NLP is a separate community from LLM evaluation / judge reliability.
- Safe in 0 of 4 personal profiles — weakest personal-goal alignment of all bc_acceptable topics.
- NIW=2, career=3, EB-1A=4 — middle of the road on everything.

**Eliminated from bridge consideration. Catalogue as a long-term collaboration opportunity.**

---

## 4. Venue Catalog

### 4.1 No-APC Venues (strongly preferred)

| Venue | Type | Review model | Timeline | Indexed | Preprints | Prestige | Notes |
|---|---|---|---|---|---|---|---|
| **TMLR** | ML journal | Open, rolling | 3–6 mo | DBLP, GS | Yes (encouraged) | High | Best free path for T02, T01, T07 |
| **ARR → ACL/EMNLP Findings** | NLP conference | Double-blind rolling | 4–7 mo | ACL Anthology, DBLP | Yes | High | Highly respected; no APC; Findings are peer-reviewed |
| **ARR → ACL/EMNLP Main** | NLP conference | Double-blind rolling | 4–7 mo | ACL Anthology, DBLP | Yes | Very high | Harder to get; same no-APC policy |
| **NeurIPS D&B Track** | Conference (benchmark) | Double-blind | 5–6 mo | DBLP, GS | Yes | Very high | Annual; deadline ~May/June; best for B05 |
| **ICLR** | Conference | Open review | 4–5 mo | DBLP, GS | Yes | Very high | Annual; challenging without institutional affiliation |
| **EACL / NAACL** | NLP conference | Double-blind | 4–6 mo | ACL Anthology | Yes | High | ACL-family; no APC |
| **JMLR** | ML journal | Single-blind | 12–24 mo | DBLP, GS | Very high | Very high | No APC; slow but most prestigious free path |
| **COLM** | Conference | Double-blind | 4–5 mo | DBLP (growing) | Yes | Medium-high | Annual; "Conference on Language Modeling"; newer |

### 4.2 Venues with APC (acceptable in specific cases)

| Venue | APC | Notes |
|---|---|---|
| PLOS ONE | ~$2,000+ | Waiver available; not recommended for first paper |
| IEEE Access | ~$1,995 | Lower prestige for NLP/eval topics; avoid |
| Frontiers in AI | ~$2,500 | Lower prestige; avoid |
| JAMIA | Optional | Only for T43 (clinical audit); strong fit; waiver possible |

### 4.3 Workshop Venues (stepping stone, not primary)

| Workshop | Parent venue | Indexed | APC | Notes |
|---|---|---|---|---|
| Eval4NLP | EMNLP | ACL Anthology | No | Best fit for T02, T01; peer-reviewed |
| TrustNLP | NAACL/ACL | ACL Anthology | No | Good for T07 (security/trust framing) |
| LLM Safety Workshop | NeurIPS | Workshop proceedings | No | T07 safety framing |
| DMLR | ICML/NeurIPS | Workshop proceedings | No | B05 data-centric |
| BioNLP | ACL | ACL Anthology | No | T43 clinical framing |

**Note on workshops for NIW/EB-1A**: Workshop papers are peer-reviewed and in ACL Anthology,
but immigration petitions are stronger with full conference or journal papers. Use workshops
as a stepping stone to generate community feedback, then submit the strengthened version to
a full venue. A workshop paper alone is a weak exhibit unless the workshop is highly selective.

---

## 5. Shortlist by Objective

| Objective | Best Candidate | Second Best | Rationale |
|---|---|---|---|
| **Best bridge publication** | **T02** | T01 | Cleanest EW (0/0), fastest execution, direct JudgeSense synergy, empirical scope |
| **Best long-term citation candidate** | **T07** | B05 | NIW=4, EB-1A=5, career=5; judge security is a growing area; 200+ citation potential |
| **Best NIW/EB1A-aligned** | **T07** | T01 | Only topic with NIW=4 that is bc_acceptable; judge-target threat model is a public interest argument |
| **Best FAANG/research-career** | **T07** | T01 | career=5; safety + evaluation intersection is exactly what OpenAI/Anthropic/Google DeepMind hire for |
| **Safest first publication** | **T02** | T01 | 0/0 EW, established methodology, no adversarial component, empirical study, TMLR submission |
| **Highest risk** | **B12** | T07 | 29 direct artifacts, multilingual resource barrier, moderate differentiator; eliminated from bridge |

---

## 6. Recommended First-Paper Strategy

### The Recommended Bridge Paper: **T02 (Position-Bias Quantification)**

**Why T02 and not T07:**
T07 is the stronger long-term paper, but it is NOT the right bridge paper. The reasons:

1. **T07 requires a blocking check first.** The arXiv 2025 "Red Teaming the Mind of the Machine" paper
   must be read and cleared before any execution work begins. If that paper covers judge models as targets,
   T07's scope must be renegotiated — wasting weeks of setup work.

2. **T07 requires adversarial infrastructure.** Building an injection attack taxonomy and running
   experiments across 3+ judge models × 5+ injection types × 3 tasks is a 5–7 month project.
   A bridge paper must land faster.

3. **T02 creates NO competition with T07.** T02 (position bias) and T07 (prompt injection) are
   different topics. Publish T02 first, then T07. The two papers together form a coherent
   "judge reliability" cluster alongside JudgeSense.

4. **T02 executes in 3–4 months.** The experiment design is simple: swap response order,
   measure judge score change, repeat across models and tasks. No new dataset. No adversarial attacks.
   No clinical domain. API access + a Python harness is sufficient.

5. **T02's 0/0 EW profile means no scoop risk.** You can start writing the paper and
   running experiments with full confidence. No blocking papers need to be read first.

**The recommended strategy is a two-paper bridge:**

| Priority | Paper | Submission window | Target venue | Expected publication |
|---|---|---|---|---|
| **1 (bridge)** | T02: Position-bias quantification | June/July 2026 | ARR → EMNLP 2026 Findings | December 2026 |
| **2 (parallel start)** | T07: Judge prompt injection | Post arXiv immediately after clearing "Red Teaming" paper | TMLR or ARR → EMNLP 2027 | Q2–Q3 2027 |

---

## 7. Recommended Submission Order

```
Month 1-2 (May-June 2026):
  [T02] Design experiments: 4-5 judge models × 4 position conditions × 3 tasks
  [T07] READ: "Red Teaming the Mind of the Machine" (arXiv 2025) — clear or pivot
  [T07] IF cleared: post 1-page arXiv technical report establishing judge-target threat model

Month 2-3 (June-July 2026):
  [T02] Run experiments via API (GPT-4o, Claude, Llama, Mistral, Gemini Flash)
  [T02] Analyse: PBI scores, rank-order consistency, inter-model comparison
  [T07] IF cleared: begin attack taxonomy and experimental design

Month 3-4 (July-August 2026):
  [T02] Write paper (8 pages + appendix)
  [T02] Release: judge-bias-eval Python harness + result logs on GitHub + HuggingFace
  [T02] Submit to ARR (July cycle) + post arXiv preprint
  [T07] IF experiments underway: continue execution

Month 5-6 (September-October 2026):
  [T02] Respond to ARR reviews (if revisions requested)
  [T07] Complete experiments and write paper
  [JudgeSense] Monitor NeurIPS review cycle

Month 6-7 (November-December 2026):
  [T02] Camera-ready for EMNLP 2026 (if accepted) OR resubmit to TMLR
  [T07] Submit to TMLR (rolling) or ARR (November cycle)
  [Survey] Continue ACM rolling review

Month 8-12 (2027):
  [T07] TMLR review cycle
  [JudgeSense] NeurIPS published (if accepted)
  [Clinical paper] Finalise with collaborators
  [T01] Begin if T02 is published and bandwidth allows
```

---

## 8. Venue Shortlist Per Candidate

### T02 (Bridge paper — position bias)
| Priority | Venue | APC | Preprints | Timeline | Why |
|---|---|---|---|---|---|
| 1st | ARR → EMNLP 2026 Findings | No | Yes | ~7 mo | Best prestige/speed balance; ACL Anthology indexed |
| 2nd | TMLR | No | Yes | ~5 mo | Rolling review; no APC; prestigious; strongest if EMNLP rejects |
| 3rd | ARR → NAACL 2026 | No | Yes | ~5 mo | If EMNLP timeline is too tight |
| Workshop | Eval4NLP @ EMNLP 2026 | No | Yes | ~4 mo | Early feedback before main venue submission |
| Avoid | IEEE Access, PLOS ONE | APC | — | — | Lower prestige; wrong venue for NLP eval |

### T07 (Long-term paper — prompt injection)
| Priority | Venue | APC | Preprints | Timeline | Why |
|---|---|---|---|---|---|
| 1st | TMLR | No | Yes | ~6 mo | Rolling; no deadline pressure; strong for safety paper |
| 2nd | ARR → EMNLP 2027 | No | Yes | ~8 mo | Prestige; eval+safety intersection |
| 3rd | ARR → ACL 2027 | No | Yes | ~8 mo | Security-inclined reviewers |
| Parallel | arXiv preprint | No | — | Immediate | Priority claim — do this FIRST |
| Workshop | TrustNLP @ ACL/NAACL | No | Yes | ~4 mo | Early peer feedback + community exposure |
| Later | IEEE S&P Workshop | No | Yes | ~6 mo | If security framing is primary |

### T01 (Third paper — cross-judge agreement, long-context)
| Priority | Venue | APC | Preprints | Timeline | Why |
|---|---|---|---|---|---|
| 1st | ARR → ACL 2027 | No | Yes | ~8 mo | Natural fit for agreement study |
| 2nd | TMLR | No | Yes | ~6 mo | Rolling review; strong alternative |
| Workshop | Eval4NLP or LongContext Workshop | No | Yes | ~4 mo | Early feedback |

---

## 9. APC / No-APC / Indexing / Preprint Status Summary

| Venue | APC | DBLP | GS | OpenAlex | Preprints | Reviewer opportunities |
|---|---|---|---|---|---|---|
| TMLR | **No** | ✅ | ✅ | ✅ | ✅ (required) | Medium (TMLR reviewer community) |
| EMNLP / ACL Findings | **No** | ✅ | ✅ | ✅ | ✅ | High (ACL community) |
| EMNLP / ACL Main | **No** | ✅ | ✅ | ✅ | ✅ | Very high |
| NeurIPS D&B | **No** | ✅ | ✅ | ✅ | ✅ | Very high |
| ICLR | **No** | ✅ | ✅ | ✅ | ✅ | Very high |
| JMLR | **No** | ✅ | ✅ | ✅ | ✅ | High |
| IEEE Access | ~$1,995 | ✅ | ✅ | ✅ | Case-by-case | Low |
| PLOS ONE | ~$2,000 | ✅ | ✅ | ✅ | Yes | Low for ML |

**For NIW/EB1A**: TMLR, EMNLP Main/Findings, NeurIPS, ICLR, and JMLR are all accepted as
credible peer-reviewed venues by immigration attorneys. The key requirements are: double-blind
or open peer review, DBLP/Google Scholar indexing, and independent editorial control.
IEEE Access qualifies technically but is weaker in prestige arguments.

---

## 10. Risk Analysis

### Publication risks by candidate

| Risk | T02 | T01 | T07 | B05 |
|---|---|---|---|---|
| Scoop risk (pre-existing paper covers it) | Low | Medium | **High** | Medium |
| Reviewer rejection (scope too narrow) | Low | Medium | Medium | Low |
| Reviewer rejection (scope too broad) | Low | Low | Low | Medium |
| Solo execution not feasible in time | Low | Low-med | Medium | Medium |
| Venue signal weakness | Low | Low | Low | Low |
| Identity fragmentation risk | Very low | Very low | Very low | **Medium** |
| arXiv preprint required urgently | No | No | **YES** | No |

### Meta-risks

**Risk: You submit T02 and a position-bias paper appears on arXiv first.**
Mitigation: Post arXiv concurrent with ARR submission. If the competing paper appears after
your arXiv, priority is established. If it appears before your submission — read it carefully.
If it does not include the cross-model + judge-specific + released harness angle, proceed.
If it does — pivot to T01 or file T02 as a replication + extension study.

**Risk: NeurIPS rejects JudgeSense and T02 is submitted to the same venue.**
No conflict. T02 is not the same paper as JudgeSense. Submit T02 to EMNLP or TMLR regardless.

**Risk: T07 is scooped by the "Red Teaming" arXiv paper.**
If that paper covers judge models as targets: narrow T07 to RLHF pipeline judges specifically
(OpenAI-style reward models as judge targets), which is a distinct and smaller target than
general judge models. The threat model still exists and is underserved.

**Risk: Publications at EMNLP Findings are seen as "second tier".**
They are not. EMNLP Findings are peer-reviewed, published in ACL Anthology, and DBLP indexed.
They are accepted by NIW petition attorneys as credible peer-reviewed publications.
The prestige difference between Main and Findings is negligible for an early-career publication.

**Risk: TMLR is too slow to be a bridge.**
TMLR reviews average 3–5 months. A June 2026 submission can realistically be accepted
by October–November 2026. This is comparable to EMNLP Findings and faster than ICLR or NeurIPS.

---

## 11. Why T02 Is the Best Bridge-Paper Tradeoff

The bridge publication serves one specific function: it establishes that you have at least
one peer-reviewed publication as a solo author in your core research area, while you wait
for the longer-timeline papers (JudgeSense at NeurIPS, survey at ACM, clinical paper with
collaborators) to land.

T02 wins this function because:

1. **Zero blocking conditions.** No papers need to be read and cleared. No artifact gap needs
   to be verified. No clinical domain. No adversarial implementation. Start experiments now.

2. **Research identity lock-in.** Position bias in judge models is squarely in the LLM evaluation
   cluster. Every future paper you write — JudgeSense, T07, the survey — will have a companion
   to cite. The citation network strengthens.

3. **Fastest credible path.** 3–4 months to submission. 7 months to EMNLP Findings publication.
   No other candidate in this pool can match this without sacrificing legitimacy.

4. **Artifact is small but real.** A Python harness with released result logs is an independently
   citable artifact. It gives reviewers something concrete to evaluate. It gives the community
   a tool to build on. For EB-1A, it demonstrates "original contributions to the field."

5. **No JudgeSense interference.** Position bias is a distinct contribution from whatever
   JudgeSense measures. If JudgeSense is about X, T02 is about a specific, systematic characterisation
   of one bias type in judge models — complementary, not competitive.

6. **Low APC cost.** TMLR and ARR/EMNLP are both free venues. The only cost is API credits
   (< $200 for a 5-model × 3-task × 4-condition study with GPT-4o at current pricing).

**The only reason to NOT do T02 first** is if you have strong pre-existing data or experiments
on T07 that can be turned into a paper faster. If you already have judge models running injection
tests, skip to T07. Otherwise, T02 is the rational bridge.

---

## 12. Final Summary Table

| Shortlist role | Candidate | Venue | Timeline | APC | Risk level |
|---|---|---|---|---|---|
| **Best bridge** | **T02** — Position-bias quantification | TMLR or ARR→EMNLP 2026 | **7 months** | None | Low |
| **Best long-term citation** | **T07** — Judge prompt injection | TMLR or ARR→EMNLP 2027 | 12–15 months | None | Medium |
| **Best NIW/EB1A** | **T07** | TMLR or EMNLP 2027 | 12–15 months | None | Medium |
| **Best FAANG/research-career** | **T07** | TMLR or EMNLP 2027 | 12–15 months | None | Medium |
| **Safest first publication** | **T02** | TMLR | 5–7 months | None | **Low** |
| **Best 3rd paper** | **T01** | ARR→ACL/EMNLP 2027 | 14–18 months | None | Medium |
| **Highest risk** | B12 — Multilingual factuality | — | Not recommended | — | Very high |
| **Long-term only** | B05 — Synthetic data quality | NeurIPS D&B or TMLR | 8–12 months | None | Medium |

---

*Report generated: 2026-05-12*
*Inputs: pipeline run c805933, PERSONAL_OVERLAY_REPORT, GO_READINESS_DOSSIERS*
*Author: research-command-center pipeline + manual analysis*
