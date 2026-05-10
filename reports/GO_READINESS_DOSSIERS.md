# GO Readiness Dossiers
*Generated: 2026-05-10 — post source-type existing-work fix (commit 1784f47)*
*Scope: four strongest candidates after paper-vs-artifact overlap disambiguation*
*Judgment standard: strict — GO requires citation thesis, clear differentiator, relevant evidence, real artifact value, realistic venue.*

---

## Ranking Context

| Rank | Topic | Overall | Paper Direct | Artifact Direct | go_blocked | Recommendation |
|------|-------|---------|-------------|----------------|-----------|----------------|
| 1 | T11 | 12.51 | 0 | 0 | No | NARROW MORE |
| 2 | T74_N1 | 12.46 | 0 | 0 | No | NEEDS MORE EVIDENCE |
| 3 | T43 | 12.03 | 0 | 2 | No | NARROW MORE |
| — | T10 | 11.73 | 3 | 3 | **YES** | *(blocked — skip)* |
| 4 | T07 | 11.63 | 0 | 16 | No | NARROW MORE |

No topic currently meets the strict GO threshold. Reasons are itemized per dossier.

---

---

## Dossier 1 of 4 — T74\_N1

### Identity

| Field | Value |
|---|---|
| **topic_id** | T74\_N1 |
| **title** | Open structured-metadata dataset of LLM-eval papers — noise-pruned |
| **parent topic** | T74 — Open structured-metadata dataset of LLM-eval papers |
| **narrowing type** | Noise-pruned: removed `metadata` + `systematic mapping` from keywords → negatives |
| **category** | meta |
| **target artifact** | dataset |

### Pipeline Scores

| Signal | Value |
|---|---|
| **Overall score** | 12.46 / ~20 |
| **Citation signal** | 5 / 5 |
| **Artifact score** | 4 / 5 |
| **Saturation** | 3 / 5 (moderate competition) |
| **Venue signal** | 2 / 5 *(weak)* |
| **Career (FAANG)** | 5 / 5 |
| **EB-1A** | 5 / 5 |
| **NIW** | 2 / 5 *(weak)* |
| **IP risk** | 0 |
| **Relevance purity** | 0.50 (best available — noise-pruned) |
| **Evidence quality** | 3 / 5 |
| **Kept papers** | **1** *(critically thin corpus)* |
| **LLM reviewer plurality** | NARROW |
| **High-confidence DROPs** | 2 (brutal\_skeptic score=1, career\_faang score=1) |
| **High disagreement** | No |

### Existing Work

| Dimension | Count |
|---|---|
| Paper direct overlaps (rel ≥ 0.65) | **0** |
| Artifact direct (GitHub / HF / PWC) | **0 / 0 / 0** |
| Partial overlaps | 2 (1 paper, 1 GitHub) |
| go\_blocked | **No** |
| paper\_differentiator\_strength | `strong` |
| artifact\_differentiator\_strength | `strong` |

**Closest existing entry:** "Magic Sequence: LLM evaluation methodology…" (GACLM 2025, relevance 0.50 — partial only). Scope is a puzzle-solving application of evaluation methodology, not a structured metadata corpus of evaluation papers.

**GitHub partial:** `aws-samples/llm-evaluation-methodology` (47 stars) — tutorial repo, not a structured metadata corpus.

### Citation Thesis

Researchers building new LLM benchmarks need to cite prior methodology choices (evaluator type, dataset disclosure practices, statistical protocols). A structured-metadata corpus of LLM evaluation papers would enable: (a) meta-analyses of evaluation practice trends, (b) automated audit of whether new papers disclose required fields, (c) a reference corpus for evaluation governance bodies (NIST, EU AI Act). The citing audience is anyone who writes about *how to evaluate LLMs*, not just what the results are.

### Future Citing Audience

Benchmark designers, reproducibility auditors, AI evaluation governance bodies (NIST AI RMF, EU AI Office), authors of survey papers on LLM evaluation, meta-analysis researchers in ML.

### Expected Citation Horizon

| Window | Assessment |
|---|---|
| Short-term (0–18 mo) | Weak — field still forming; few meta-analysis papers yet |
| Medium-term (18 mo–4 yr) | Strong — governance demand for evaluation standards is rising |
| Long-term (4 yr+) | Strong if it becomes the canonical metadata corpus for LLM eval |

### One-Sentence Contribution

A hand-curated, field-level structured-metadata corpus cataloguing evaluation methodology choices across peer-reviewed LLM evaluation papers (evaluator type, dataset disclosure, code availability, statistical protocol, venue).

### One-Sentence Differentiator vs Closest Existing Work

Unlike general paper-metadata systems (Semantic Scholar, OpenAlex), this corpus specifically extracts structured evaluation-methodology fields not captured by standard bibliographic APIs, enabling reproducibility auditing at field scale.

### Minimum Viable Paper

Corpus of 200+ LLM evaluation papers (2020–2025); schema of 8–10 metadata fields (evaluator type, dataset disclosed, code link, statistical method, number of runs, prompt disclosed); descriptive statistics; reproducibility audit findings; dataset released under CC-BY.

### Strongest Version of the Paper

Corpus of 1,000+ papers with ML-assisted extraction; trend analysis across years and venues; reproducibility score per paper; integration with OpenReview for live updates; benchmark for auto-extractors; collaboration with NeurIPS D&B or TMLR editors.

### Required Artifact

Structured CSV/JSON dataset + extraction schema + validation protocol + extraction code. Artifact is the primary contribution; paper is the vehicle.

### Likely Venue Path

NeurIPS 2026 Datasets & Benchmarks Track → TMLR (continuous) → JMLR special issue on evaluation methodology.

### No-APC / Free Path

- **TMLR** — no APC, DBLP/Google Scholar indexed, open review. Primary free path.
- **JMLR** — no APC, fully indexed. Slower but authoritative.
- NeurIPS D&B registration fee is a cost but no per-paper APC.

### Main Failure Risk

**Corpus viability**: only 1 paper survived the noise-pruned query. This is the single largest risk. It could mean: (a) the topic is genuinely novel with sparse literature (good), OR (b) removing `metadata` + `systematic mapping` over-pruned the query and killed the evidence base (bad). We cannot distinguish these without re-running the parent query T74 and manually inspecting which of T74's 16 papers are actually on-topic.

Secondary risk: if OpenAlex / Semantic Scholar already expose structured evaluation metadata fields via their APIs (paper types, dataset links, code links), the "structured" differentiator weakens considerably.

### Exact Next Verification Needed

1. **Re-run T74 query without narrowing** and manually label each of the 16 kept T74 papers as "in-scope for metadata corpus" or "off-topic." If fewer than 10 are in-scope, reconsider whether the corpus is feasible.
2. **Check existing metadata APIs**: Query Semantic Scholar `/paper` endpoint for `openAccessPdf`, `tldr`, `fieldsOfStudy`; check if these already expose the fields we intend to catalog.
3. **Search OpenReview** for accepted papers on "evaluation methodology" at NeurIPS/ICLR 2023–2025 to find the closest existing structured corpus.
4. **Validate artifact feasibility**: Can metadata fields be reliably extracted by a single author from 200 papers in 4–6 weeks?

### Final Recommendation

> **NEEDS MORE EVIDENCE**

The existing-work profile is the cleanest in the entire candidate set (0 direct papers, 0 direct artifacts) and the citation signal is strong. However, **1 kept paper is not a sufficient evidence base for a GO decision**. The query over-pruning may have eliminated valid evidence. We cannot assess whether a 200-paper corpus is even constructible until the parent T74 papers are manually labeled. Promote to NARROW MORE only after re-running T74 and confirming ≥10 in-scope papers exist.

---

---

## Dossier 2 of 4 — T11

### Identity

| Field | Value |
|---|---|
| **topic_id** | T11 |
| **title** | Format sensitivity benchmark on LLM evaluations |
| **parent topic** | *(original; not a narrowed variant)* |
| **category** | prompt |
| **target artifact** | benchmark |

### Pipeline Scores

| Signal | Value |
|---|---|
| **Overall score** | **12.51** *(highest in dataset)* |
| **Citation signal** | 4 / 5 |
| **Artifact score** | 4 / 5 |
| **Saturation** | 3 / 5 (moderate) |
| **Venue signal** | 2 / 5 *(weak)* |
| **Career (FAANG)** | 5 / 5 |
| **EB-1A** | 5 / 5 |
| **NIW** | 2 / 5 *(weak)* |
| **IP risk** | 0 |
| **Relevance purity** | 0.25 *(low — format sensitivity leaks into unrelated output-format work)* |
| **Evidence quality** | **2 / 5** *(very low)* |
| **Kept papers** | **3** *(very thin corpus)* |
| **LLM reviewer plurality** | NARROW |
| **High-confidence DROPs** | 0 |
| **High disagreement** | No |
| **Decision score (mean)** | 1.88 / 3 *(highest of the four topics)* |

### Existing Work

| Dimension | Count |
|---|---|
| Paper direct overlaps (rel ≥ 0.65) | **0** |
| Artifact direct (GitHub / HF / PWC) | **0 / 0 / 0** |
| Partial overlaps | 1 paper |
| Adjacent | 2 papers |
| go\_blocked | **No** |
| paper\_differentiator\_strength | `strong` |
| artifact\_differentiator\_strength | `strong` |

**Closest existing entry (partial, 0.50):** "Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure" (2026). This paper studies whether format sensitivity confounds evaluation-awareness probes — adjacent but framed around probe-based interpretability, not a benchmark for systematic format-induced variance. **Must read in full before proceeding.**

**Adjacent:**
- "BenchING: A Benchmark for Evaluating LLMs in Following Structured Output Format Instruction in Text-Based Games" (IEEE Transactions on Games, 2025, relevance 0.25) — evaluates format instruction following, not format-induced score variance in evaluations.
- "Quantifying the Impact of Structured Output Format on LLMs" (EACL 2026, relevance 0.25) — this is the most relevant adjacent paper and may be closer to our scope than the pipeline scored it. Read before proceeding.

### Citation Thesis

Output format (JSON vs YAML vs Markdown vs plain prose) is a systematic, underreported confound in LLM benchmark results. Models that excel at structured output may artificially dominate leaderboards on benchmarks requiring structured responses, and vice versa. A format sensitivity benchmark exposes this confound: any practitioner who runs an evaluation pipeline choosing an output format needs to cite this to justify their format choice. Benchmark designers building new evaluations need it as a calibration reference. The citation audience is large and growing as structured LLM outputs become standard.

### Future Citing Audience

LLM API users choosing between JSON/YAML/prose, benchmark designers, evaluation practitioners, AutoEval pipeline builders (LangChain, LMQL, Instructor users), LLM leaderboard maintainers (HELM, LMSYS Chatbot Arena, Open LLM Leaderboard).

### Expected Citation Horizon

| Window | Assessment |
|---|---|
| Short-term (0–18 mo) | **Strong** — format sensitivity is actively studied right now (2025–2026 adjacent papers) |
| Medium-term (18 mo–4 yr) | **Strong** — structured output is becoming infrastructure-level; the benchmark becomes a reference |
| Long-term (4 yr+) | Moderate — may be superseded if LLMs become format-agnostic |

### One-Sentence Contribution

A systematic benchmark quantifying how output format choice (JSON, YAML, Markdown, plain prose, mixed) induces variance in LLM task performance scores across models, benchmarks, and prompt templates.

### One-Sentence Differentiator vs Closest Existing Work

Unlike "Is Evaluation Awareness Just Format Sensitivity?" (2026) which uses probe-based evidence to study interpretability confounds, this work provides a standalone benchmark harness that any evaluation practitioner can apply to any task to measure and report format-induced score variance as a first-class reproducibility metric.

### Minimum Viable Paper

- 3–5 LLMs (GPT-4o, Claude Sonnet, Llama 3.x, Mistral, Gemini Pro)
- 3–4 tasks (question answering, summarization, code generation, factual extraction)
- 4 output formats (JSON, YAML, Markdown structured, plain prose)
- Metrics: variance in task score across formats; rank-order stability across format conditions
- Released as benchmark harness + results dataset + leaderboard template
- Target length: ~8 pages + appendix, EMNLP Findings or ARR short paper

### Strongest Version of the Paper

Full combinatorial study (10+ models × 5+ tasks × 6+ formats × 3 prompt templates); statistical bootstrap for confidence intervals; analysis of which model architectures are most/least format-sensitive; interaction analysis with chain-of-thought formatting; reproducibility package as a pip-installable tool for future evaluations; leaderboard submission to HELM or Open LLM Leaderboard.

### Required Artifact

Benchmark suite: format-matched test sets for each task + evaluation harness (Python package) + model output logs + leaderboard template. Artifact must be independently runnable. This is the primary deliverable; the paper is a methods/findings companion.

### Likely Venue Path

1. **Primary**: ARR cycle → EMNLP 2026 Findings (systematic benchmark paper, well-suited to EMNLP)
2. **Secondary**: NeurIPS 2026 Datasets & Benchmarks Track
3. **Fallback**: COLM 2026 (conference on language models)

### No-APC / Free Path

- **TMLR** — no APC, continuous publication, peer-reviewed, indexed. Best free path if venue signal stays weak.
- **EMNLP/ACL** — registration fee for presenting author only; no per-paper APC.
- **arXiv preprint first** — establish priority, get community feedback before formal submission.

### Main Failure Risk

1. **The EACL 2026 paper "Quantifying the Impact of Structured Output Format on LLMs"** — if this paper already delivers a systematic cross-format benchmark with released code, T11 may be scooped. This is the top risk. The pipeline scored it at 0.25 (adjacent) but title alignment is high.
2. **The 2026 "Is Evaluation Awareness Just Format Sensitivity?" paper** — if it includes a benchmark component, scope overlap is substantial.
3. **Evidence corpus depth**: 3 papers is insufficient. If 10+ papers emerge in a broader search, some may be direct competitors not yet captured.
4. **Format-agnostic LLMs**: if frontier models become fully format-agnostic by 2026–2027, the benchmark becomes historical artifact rather than reference tool.

### Exact Next Verification Needed

1. **Read "Quantifying the Impact of Structured Output Format on LLMs" (EACL 2026)** — determine: does it include a benchmark harness? Multi-model? Multi-task? Released code?
2. **Read "Is Evaluation Awareness Just Format Sensitivity?" (2026)** — does it include a standalone reusable benchmark or only probe-based experiments?
3. **Run broader arXiv search**: `format sensitivity LLM benchmark` and `structured output format variance evaluation` for 2024–2026 — target 15+ total papers before proceeding.
4. **Check Papers With Code** for "format sensitivity" and "structured output benchmark" to find released artifacts.
5. If neither EACL nor the 2026 probe paper includes a reusable cross-format harness, write the one-paragraph differentiator and lock in the scope.

### Final Recommendation

> **NARROW MORE**

T11 has the highest overall pipeline score (12.51) and the cleanest existing-work profile (0 direct papers, 0 direct artifacts). The citation thesis is real — format sensitivity is an active pain point for evaluation practitioners. However, **three critical blockers must resolve before GO**: (1) The EACL 2026 paper needs full-text characterization — if it already delivers a reusable benchmark, T11's scope must move to something that paper doesn't cover; (2) The corpus must grow from 3 to 15+ papers via a broader query; (3) The venue signal (2/5) must improve — a 6-page EMNLP short paper with released code is the right format but needs a clear acceptance-worthy framing. Do not promote to GO until (1) is resolved.

---

---

## Dossier 3 of 4 — T07

### Identity

| Field | Value |
|---|---|
| **topic_id** | T07 |
| **title** | Judge robustness to candidate-side prompt injection |
| **parent topic** | *(original; T07\_N1 is noise-pruned variant)* |
| **category** | eval + safety |
| **target artifact** | benchmark |

### Pipeline Scores

| Signal | Value |
|---|---|
| **Overall score** | 11.63 |
| **Citation signal** | 5 / 5 |
| **Artifact score** | 2 / 5 *(low — high existing HF artifact density)* |
| **Saturation** | 3 / 5 |
| **Venue signal** | 2 / 5 *(weak)* |
| **Career (FAANG)** | 5 / 5 |
| **EB-1A** | 5 / 5 |
| **NIW** | 4 / 5 *(second-highest NIW in dataset)* |
| **IP risk** | 0 |
| **Relevance purity** | 0.25 *(low — "adversarial robustness" leaks into non-judge contexts)* |
| **Evidence quality** | 4 / 5 |
| **Kept papers** | 31 *(good volume; but purity problem)* |
| **LLM reviewer plurality** | **NEEDS\_MORE\_EVIDENCE** *(not NARROW — reviewers are uncertain)* |
| **High-confidence DROPs** | 0 |
| **High disagreement** | No |
| **Decision score (mean)** | 1.50 / 3 |

### Existing Work

| Dimension | Count |
|---|---|
| Paper direct overlaps (rel ≥ 0.65) | **0** |
| Artifact direct: GitHub | 5 |
| Artifact direct: HuggingFace | 11 |
| Artifact direct: PWC | 0 |
| **Total artifact direct** | **16** |
| Partial overlaps | 18 (14 papers, 2 GH, 2 HF) |
| Adjacent | 17 papers |
| go\_blocked | **No** |
| peer\_reviewed\_direct\_overlap | **No** |
| high\_artifact\_overlap | **Yes (≥8)** |
| paper\_differentiator\_strength | `strong` |
| artifact\_differentiator\_strength | `moderate` |
| artifact\_differentiator\_required | **Yes** |

**Top paper (relevance 0.625 — highest in dataset for T07):**
"Red Teaming the Mind of the Machine: A Systematic Evaluation of Prompt Injection" (arXiv 2025). This is the single most dangerous competitor. Title overlap with our scope is high. **Must read immediately.**

**Direct artifact examples:**
- `liu00222/Open-Prompt-Injection` (438 stars) — general prompt injection benchmark
- `lakeraai/pint-benchmark` (184 stars) — injection benchmark
- `microsoft/BIPIA` (124 stars) — Microsoft's benchmark on indirect prompt injection
- `deepset/prompt-injections` HF dataset (5,438 downloads) — general injection examples
- `rogue-security/prompt-injections-benchmark` (933 downloads) — red-team dataset

None of these are specifically scoped to **judge models as the target**. The threat model in these artifacts is: attacker injects into tool input, output, or user message — not into a candidate response evaluated by a judge LLM. The judge-target distinction is the core differentiator.

### Citation Thesis

LLM-as-judge is now standard infrastructure in RLHF pipelines, safety evaluations, and open-ended AutoEval systems (GPT-4 as judge, Claude as judge). A candidate model can embed prompt injections in its output that are invisible to human readers but manipulate the judge's scoring. No peer-reviewed systematic benchmark exists specifically for this threat model. Any team deploying LLM-as-judge in a safety-critical setting (medical, legal, hiring) would need to cite a rigorous characterization of this vulnerability.

### Future Citing Audience

RLHF practitioners (OpenAI, Anthropic, DeepMind), AI safety researchers, red teams at model providers, enterprise teams deploying AutoEval pipelines, IEEE/ACM security conference attendees, LLM evaluation framework authors (HELM, LM-Eval-Harness, LMQL).

### Expected Citation Horizon

| Window | Assessment |
|---|---|
| Short-term (0–18 mo) | **Very strong** — LLM-as-judge is peak adoption now; the vulnerability is immediate |
| Medium-term (18 mo–4 yr) | **Strong** — RLHF pipelines will scale; judge robustness becomes an audit requirement |
| Long-term (4 yr+) | Moderate — may be superseded by adversarially-trained judges |

### One-Sentence Contribution

The first systematic benchmark characterizing prompt injection attacks specifically targeting LLM judge models (evaluator LLMs) from within candidate responses, including attack taxonomy, injection success rates across judge models, and defenses.

### One-Sentence Differentiator vs Closest Existing Work

Unlike existing prompt injection benchmarks (Open-Prompt-Injection, BIPIA, PINT) which target assistant models in tool-use contexts, this benchmark focuses exclusively on the judge model as attack surface — where the attacker controls the candidate output and the judge is the victim, a threat model absent from all existing peer-reviewed work.

### Minimum Viable Paper

- Attack taxonomy: 4–6 injection types (score override, role confusion, distractor injection, meta-instruction injection, format hijacking, confidence manipulation)
- 3+ judge models tested (GPT-4o, Claude Sonnet, Llama judge)
- 3+ task types (QA scoring, summarization rating, code review scoring)
- Metrics: injection success rate, score distortion magnitude, judge agreement under attack
- Defenses tested: system prompt hardening, sandboxing, dual-judge consensus
- Released: injection test suite + evaluation harness

### Strongest Version of the Paper

Full taxonomy (10+ injection types) × 6+ judge models × 5+ tasks; white-box and black-box attack scenarios; formal adversarial model definition; detection methods; responsible disclosure to OpenAI/Anthropic; published at IEEE S&P, ACL, or NeurIPS.

### Required Artifact

Benchmark dataset of injection templates (with ground-truth scores + injected scores) + evaluation harness (pytest-based or HELM plugin) + result logs + leaderboard. The artifact must be able to reproduce all paper figures from scratch.

### Likely Venue Path

1. **Primary**: EMNLP 2026 (security + eval intersection) or ACL 2026
2. **Secondary**: IEEE S&P 2026 or USENIX Security 2026 (if framed as security paper)
3. **Alternative**: NeurIPS 2026 Main Track (AI safety framing)

### No-APC / Free Path

- **TMLR** — no APC; best free option
- **ACL Anthology papers** — conference fee for presenting author, no per-paper APC
- **arXiv preprint** — establish priority claim against arXiv 2025 "Red Teaming" paper immediately

### Main Failure Risk

1. **"Red Teaming the Mind of the Machine" (arXiv 2025, relevance 0.625)** — this is the top risk. If this paper includes judge models as explicit targets, T07 is scooped at the paper level. Pipeline scored it as partial (not direct) but relevance is 0.625. **Read this paper first.**
2. **Artifact differentiator is moderate, not strong** — 16 direct artifacts with `moderate` differentiator means the paper must be very explicit about the judge-target threat model in the abstract and intro. If reviewers see "prompt injection benchmark" without reading the judge-specificity, they will reject.
3. **Reviewer uncertainty** — plurality is NEEDS\_MORE\_EVIDENCE, not NARROW. This reflects genuine uncertainty about whether the scope is sufficiently narrow and differentiated. Likely cause: reviewers did not see evidence of judge-specific injection attacks in the kept papers.

### Exact Next Verification Needed

1. **Read "Red Teaming the Mind of the Machine" (arXiv 2025)** — check: (a) do they test judge LLMs as targets? (b) do they include candidate-side injections specifically? If yes → pivot to a narrower angle (e.g., judges in RLHF pipelines only; or defenses only). If no → write the one-paragraph differentiator and proceed.
2. **Inspect the 5 GitHub direct repos** (Open-Prompt-Injection, PINT, BIPIA, HacxGPT, spikee) — do any include judge-specific test cases? Document absences explicitly.
3. **Check HF datasets** (deepset/prompt-injections, rogue-security/prompt-injections-benchmark) — filter for examples where the judge is the target, not an assistant.
4. **Write the artifact differentiator paragraph** per the T07\_existing\_work.md checklist before any further pipeline steps.
5. **Narrow the query** to explicitly include "LLM judge" or "evaluator LLM" to improve relevance purity from 0.25.

### Final Recommendation

> **NARROW MORE**

T07 has a real, unoccupied thesis (judge-as-target prompt injection) with 0 peer-reviewed direct overlaps and strong citation potential (citation=5, NIW=4, career=5, EB-1A=5). The threat model is genuinely novel. However, **three things must happen before GO**: (1) The arXiv 2025 "Red Teaming" paper must be read and cleared — if it covers judge targets, the scope must tighten further; (2) The artifact differentiator paragraph must be written and confirmed — with 16 artifacts and only `moderate` strength, this is a mandatory pre-submission step; (3) The query must be narrowed to improve purity above 0.35. The paper is directionally strong; the blocking work is characterization and scoping, not idea quality.

---

---

## Dossier 4 of 4 — T43

*4th candidate by overall score (12.03) among non-blocked topics. T10 (11.73) is go\_blocked=True with paper\_diff=`none` and is excluded.*

### Identity

| Field | Value |
|---|---|
| **topic_id** | T43 |
| **title** | Reproducibility audit of clinical LLM papers |
| **parent topic** | *(original; no narrowed variant run yet)* |
| **category** | meta + healthcare |
| **target artifact** | database + paper |

### Pipeline Scores

| Signal | Value |
|---|---|
| **Overall score** | 12.03 |
| **Citation signal** | 5 / 5 |
| **Artifact score** | 2 / 5 *(low)* |
| **Saturation** | 3 / 5 |
| **Venue signal** | 3 / 5 *(best of the four; clinical informatics venues exist)* |
| **Career (FAANG)** | **2 / 5** *(weakest of the four — clinical domain doesn't map to FAANG)* |
| **EB-1A** | 5 / 5 |
| **NIW** | **5 / 5** *(highest NIW in entire candidate set)* |
| **IP risk** | 0 |
| **Relevance purity** | 0.25 *(low — "reproducibility" leaks into ML/energy/chemistry papers)* |
| **Evidence quality** | 4 / 5 |
| **Kept papers** | 29 *(good volume)* |
| **LLM reviewer plurality** | NARROW |
| **High-confidence DROPs** | 2 (brutal\_skeptic score=1, career\_faang score=2) |
| **High disagreement** | No |
| **Decision score (mean)** | 1.50 / 3 |

### Existing Work

| Dimension | Count |
|---|---|
| Paper direct overlaps (rel ≥ 0.65) | **0** |
| Artifact direct: GitHub | 0 |
| Artifact direct: HuggingFace | 2 |
| Artifact direct: PWC | 0 |
| **Total artifact direct** | **2** |
| Partial overlaps | 3 (all HF) |
| Adjacent | 29 papers |
| go\_blocked | **No** |
| peer\_reviewed\_direct\_overlap | **No** |
| high\_artifact\_overlap | No |
| paper\_differentiator\_strength | `strong` |
| artifact\_differentiator\_strength | `strong` |
| artifact\_differentiator\_required | Yes |

**Direct HF artifacts:**
1. `AI-EcoNet/HUGO-Bench-Paper-Reproducibility` (261 downloads) — general ML reproducibility benchmark, not clinical LLM specific.
2. `zyzhou110/Squidiff_reproducibility` (106 downloads) — a single paper's reproducibility package for a diffusion model. Entirely different scope.

Neither artifact covers clinical LLM papers specifically. The clinical specificity IS the differentiator.

**Adjacent papers (sample):**
- "Leakage and the reproducibility crisis in machine-learning-based science" (Patterns 2023) — general ML, not clinical LLM.
- "A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility" (arXiv 2025) — LLM reasoning reproducibility, not clinical domain.
- "Reproducibility in Machine Learning-based Research: Overview, Barriers and Drivers" (The AI Magazine 2024) — broad overview, not domain-specific audit.

These adjacent papers validate the citation audience but do not cover the specific contribution.

### Citation Thesis

Clinical LLM papers (GPT-4 clinical QA, LLaMA clinical summarization, benchmark on MedQA) routinely lack reproducibility disclosures: prompts are not published, datasets are not licensed for reuse, code is not released, statistical protocols are underdescribed. A systematic audit creates a reproducibility baseline that clinical informaticists, journal editors (JAMIA, NEJM AI), and regulators (FDA Software as a Medical Device guidance) can use to set and enforce disclosure standards. This is a public-good research contribution with a clear national interest argument.

### Future Citing Audience

Clinical NLP researchers, clinical AI teams at hospitals and health systems, JAMIA/NEJM AI editors and reviewers, FDA SaMD reviewers, IRBs evaluating AI-assisted clinical studies, EU AI Act conformity assessors, health AI governance researchers.

### Expected Citation Horizon

| Window | Assessment |
|---|---|
| Short-term (0–18 mo) | Moderate — regulatory pressure is building but standards are not yet codified |
| Medium-term (18 mo–4 yr) | **Strong** — FDA SaMD guidance for AI/ML will require reproducibility documentation |
| Long-term (4 yr+) | **Strong** — becomes the baseline audit study; cited by policy documents |

### One-Sentence Contribution

A systematic reproducibility audit of 100–500 peer-reviewed clinical LLM papers (2018–2025), scoring each against a rubric of 8–12 disclosure fields (prompt, dataset, code, statistical method, number of runs, IRB, license), with results published as an open database.

### One-Sentence Differentiator vs Closest Existing Work

Unlike general ML reproducibility audits (Patterns 2023, AI Magazine 2024), this audit is the first to apply a clinical-domain–specific reproducibility rubric to LLM papers in healthcare settings, where non-disclosure carries patient safety and regulatory consequences, not merely scientific inconvenience.

### Minimum Viable Paper

- Rubric: 8–10 fields covering code, prompt, dataset, statistical design, IRB, license
- Corpus: 100 clinical LLM papers (2020–2025) sampled from JAMIA, NEJM AI, Lancet Digital Health, arXiv cs.CL/cs.AI with clinical MeSH terms
- Results: field-by-field disclosure rates, trend over time, correlation with venue prestige
- Artifact: database (CSV/JSON) + rubric + annotation guidelines
- Target: JAMIA Research Article (8,000–10,000 words) or NeurIPS D&B

### Strongest Version of the Paper

Corpus of 500+ papers across all major clinical AI venues (2018–2025); ML-assisted rubric annotation; reproducibility score per paper per year per venue; dashboard for live scoring of new papers; journal partnership (JAMIA editorial note); policy brief for FDA or EU AI Office.

### Required Artifact

Reproducibility database (CSV/JSON) + annotation rubric (PDF + machine-readable schema) + annotation code + inter-annotator agreement stats. The database is the primary contribution and must be publicly released (Zenodo + GitHub).

### Likely Venue Path

1. **Primary**: JAMIA (Journal of the American Medical Informatics Association) — directly on-scope, indexed, impact factor ~7, no mandatory APC (open access optional).
2. **Secondary**: NeurIPS 2026 Datasets & Benchmarks Track (if corpus is large enough)
3. **Alternative**: ACL BioNLP Workshop + extended journal version; PLOS ONE (fully open, no APC rejection for methodologically sound work)

### No-APC / Free Path

- **JAMIA** — submission fee waiver available; no mandatory APC for standard articles (only for open access option). Verify at jamia.oxfordjournals.org.
- **TMLR** — no APC, indexed; works if framed as an ML methodology paper.
- **PLOS ONE** — APC applies but fee waivers available for low-income authors; fully open.
- **arXiv preprint** — free; establish priority before journal submission.

### Main Failure Risk

1. **Data access**: most clinical LLM papers are behind paywalls (Elsevier, Springer, Oxford). A single-author can access ~200 papers via institutional access + interlibrary loan, but 500+ is a multi-month project. Scope must be calibrated to realistic access.
2. **Career signal is weak (2/5)**: brutal\_skeptic and career\_faang both gave DROP. This topic is a strong academic/policy contribution but does not demonstrate FAANG-relevant technical skills (no model training, no large-scale engineering). If the primary goal is FAANG career, this is the wrong topic. If the goal is NIW/EB-1A (NIW=5) and academic publication, it is excellent.
3. **Relevance purity (0.25)**: "reproducibility" pulls in battery chemistry, radiomics, and ML reasoning papers. The audit corpus must be constructed manually from clinical AI venues, not from keyword search alone.
4. **Scope creep**: distinguishing "clinical LLM" from "clinical ML" from "clinical AI" in the audit corpus requires a precise inclusion/exclusion rubric. Without it, the corpus becomes heterogeneous and the conclusions weaken.

### Exact Next Verification Needed

1. **Search JAMIA, NEJM AI, Lancet Digital Health, and npj Digital Medicine** for existing reproducibility audits of clinical LLM papers. If any exists (post-2023), read it and confirm the scope gap before proceeding.
2. **Manually sample 20 clinical LLM papers** from the 29 kept papers and apply the preliminary rubric — confirm that disclosure rates are actually low enough to be noteworthy (if 80%+ already disclose code and prompts, the audit finding is weak).
3. **Verify JAMIA submission requirements**: word limit, data availability policy, whether structured databases qualify as primary contributions.
4. **Verify IRB requirements**: auditing published papers is typically IRB-exempt, but confirm with institution before beginning if any patient-linked metadata is extracted.
5. **Assess data access realistically**: check how many of the 29 kept papers are open access and estimate the effort to access the remaining papers.

### Final Recommendation

> **NARROW MORE**

T43 is the strongest topic for an NIW/EB-1A immigration case (NIW=5, EB-1A=5) and has the best venue fit of the four (venue=3/5, JAMIA is a natural home). The citation thesis is real and the existing-work profile is clean (0 direct papers, 2 minor HF artifacts). However, **three things must resolve before GO**: (1) Confirm no clinical-LLM–specific reproducibility audit already exists in JAMIA or NPJ Digital Medicine (the adjacent papers found are all general ML — that gap may be real or may be a search artifact); (2) Validate the finding is actually noteworthy by sampling 20 papers — if disclosure rates are already high, there is no story; (3) Confirm data access is feasible for a single author. Do not promote to GO until (1) and (2) are resolved. Career-path alignment is a real constraint: if FAANG hire is the near-term goal, T11 or T07 are better choices; if immigration petition or academic publishing is the goal, T43 is the strongest path.

---

---

## Cross-Topic Summary

| Topic | Best Signal | Weakest Signal | Blocking Condition |
|---|---|---|---|
| T74\_N1 | EW profile (cleanest) | Corpus (1 paper), NIW=2, 2 expert DROPs | Corpus too thin — cannot evaluate |
| T11 | Overall score (highest), 0 EW | Evidence quality=2, venue=2, corpus=3 | EACL 2026 paper unread |
| T07 | NIW=4, career=5, real threat model | Plurality=NEEDS\_MORE\_EVIDENCE, artifact diff=moderate | arXiv 2025 "Red Teaming" paper unread |
| T43 | NIW=5 (best), venue=3, EB-1A=5 | Career=2, purity=0.25, data access unknown | Clinical audit scope unvalidated |

### Ordered Action List (do these before any GO decision)

1. **Read "Quantifying the Impact of Structured Output Format on LLMs" (EACL 2026)** — T11 blocker.
2. **Read "Is Evaluation Awareness Just Format Sensitivity?" (2026)** — T11 secondary blocker.
3. **Read "Red Teaming the Mind of the Machine" (arXiv 2025)** — T07 blocker.
4. **Re-run T74 parent query; manually label 16 papers** — T74\_N1 blocker.
5. **Manually sample 20 clinical LLM papers + apply rubric** — T43 blocker.
6. **Search JAMIA/NPJ Digital Medicine for clinical LLM reproducibility audits** — T43 blocker.
7. Once blockers clear: write one-paragraph differentiators for T07 and T43 per the existing-work checklist.
8. Broaden queries for T11 and T74\_N1 — target ≥15 kept papers before next pipeline run.

### Why No Topic Gets GO Today

The pipeline has done its job: it has identified four plausible candidates and ruled out all others. But the pre-GO blockers are not pipeline-resolvable — they require reading specific papers and making human judgment calls. The pipeline cannot read EACL 2026 or arXiv 2025 papers. These are 2–4 hours of reading, after which at least one of T11 or T07 should become a confident NARROW MORE → GO decision.

**If forced to rank by GO probability after blockers clear:**
1. **T11** — if the EACL/2026 papers don't deliver a reusable harness, T11 has the clearest path.
2. **T07** — if the arXiv paper doesn't cover judge targets, T07 has the most underserved real-world need.
3. **T43** — if corpus sampling confirms low disclosure rates, T43 has the strongest policy and immigration impact.
4. **T74\_N1** — last; depends entirely on rebuilding the corpus.
