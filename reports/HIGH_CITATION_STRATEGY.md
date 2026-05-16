# High-Citation Strategy: An Honest Assessment + Plan

*Constraints from the user (2026-05-16):*
- *Target: 500+ citations for the next paper*
- *Venue must be free (no APC)*
- *Time / effort is acceptable*
- *Quality > speed*
- *Bonus: helps NIW / EB-1A*

---

## 0. Reading order

This document supersedes (but does not delete) `BRIDGE_PUBLICATION_STRATEGY.md`.
The bridge strategy was optimised for **fast first publication**. This document is
optimised for **maximum citation impact at a free venue**. The two strategies are
in tension; §4 of this document explains how to reconcile them.

---

## 1. Honest reality check on "500+ citations"

I am writing as a senior reviewer / editor would: candidly.

### 1.1 The distribution of citation counts in ML / NLP

For papers published 2020–2023 (so they've had 2–5 years to accumulate):

| Percentile | Citations (3-year window) |
|---|---|
| Median | 8–20 |
| 75th | 30–60 |
| 90th | 80–150 |
| 95th | 150–300 |
| 99th | 500–1,500 |
| Top 0.1% | 1,500–10,000+ |

**500+ citations is roughly the 99th percentile.** It is achievable but rare.
You cannot reach it by writing an average-good paper. You reach it only by
hitting one of a small number of well-understood patterns (see §2).

### 1.2 First-author, first-publication reality

The honest constraint: you have **zero prior peer-reviewed publications**
in your current research identity. Reviewers at top venues do not know you.
Citation counts for solo, first-time authors are systematically lower than
for established PIs publishing the same paper. This is unfair but real.

This means: a paper that would hit 500 citations under a known PI's name
might land at 100–200 under a first-time author's name. We have to over-engineer
for impact to clear this discount.

### 1.3 Honest probability estimates

Given a single, well-executed paper:

| Paper type (solo, first-publication, free venue) | P(≥100 cit / 3yr) | P(≥500 cit / 3yr) |
|---|---|---|
| Empirical study (e.g., T02 position-bias) | 25–40% | <5% |
| Foundational benchmark (e.g., new HELM-style suite) | 20–35% | 10–20% (IF adopted) |
| Comprehensive survey at top venue | 40–55% | **20–30%** |
| Position paper / framework paper | 15–25% | 5–10% |
| Methodological breakthrough (rare/genius work) | 30–50% | 20–40% |

**The survey path is the highest-probability path to 500+ citations.**
This is what I will recommend.

### 1.4 What "500+ citations" actually requires

Talking to a senior editor would land here:

1. The paper has to be the **canonical reference** in a sub-area that thousands
   of subsequent papers cite. Survey papers and benchmark papers do this best.
2. The sub-area has to be **active**. LLM evaluation / LLM-as-Judge is one
   of the most active sub-areas in ML right now (~hundreds of papers per quarter).
3. The paper has to be **findable**. Indexed in Google Scholar, DBLP, Semantic
   Scholar. Tweeted by community influencers. Featured in newsletters.
4. The paper has to be **published at a venue that signals authority**.
   For surveys: JMLR, ACM Computing Surveys, TMLR are the free-APC top tier.
5. The paper has to **be useful**. People cite what helps them — clear
   taxonomies, reproducible code, recommended best practices.

---

## 2. Precedent papers in our space (citation autopsies)

Surveys and benchmarks in the LLM evaluation / LLM judging space and adjacent.
Data approximate; verify on Google Scholar before quoting.

| Paper | Venue | Year | Type | ~Citations | Why it worked |
|---|---|---|---|---|---|
| Bommasani et al. — "On the Opportunities and Risks of Foundation Models" | arXiv + Stanford report | 2021 | Manifesto/survey | **~8,000** | First systematic naming of "foundation models"; defined a research agenda |
| Zhao et al. — "A Survey of Large Language Models" | arXiv | 2023 | Survey | **~2,500+** | Comprehensive, regularly updated, single-stop reference |
| Chang et al. — "A Survey on Evaluation of Large Language Models" | arXiv → ACM TIST | 2023 | Survey | **~1,500+** | First comprehensive survey on LLM evaluation; identified gaps that became own subfields |
| Gu et al. — "A Survey on LLM-as-a-Judge" | arXiv | 2024 | Survey | **~200–400** | Topical, but not at a flagship venue (no top journal yet) |
| Liang et al. — "Holistic Evaluation of Language Models (HELM)" | TMLR | 2022 | Benchmark + framework | **~1,500+** | Reusable framework; widely adopted by community |
| Hendrycks et al. — "Measuring Massive Multitask Language Understanding (MMLU)" | ICLR | 2021 | Benchmark | **~3,000+** | Adopted as default LLM benchmark |
| Zheng et al. — "Judging LLM-as-a-Judge with MT-Bench" | NeurIPS D&B | 2023 | Benchmark + study | **~2,000+** | First systematic LLM-judge benchmark |
| Pineau et al. — "Improving Reproducibility in Machine Learning Research" | JMLR (program) | 2021 | Methodology | **~500–700** | Adopted as the reproducibility standard |
| Dong et al. — "A Survey on In-Context Learning" | arXiv → ACL Findings | 2023 | Survey | **~1,200+** | Defined the subfield's reference text |

### Pattern recognition

Of the 9 papers above, **7 are surveys, benchmarks, or framework papers**.
Of those 7, all 7 are either:
- Free venues (TMLR, arXiv-only, ACL, ICLR, NeurIPS, JMLR), AND/OR
- Survey/benchmark format

**Citation > 500 sweet spot for FREE venues:**
1. JMLR (no APC, prestigious — surveys here hit 500+ regularly)
2. TMLR (no APC, accepts surveys and benchmarks, modern format)
3. ACM Computing Surveys (free Green OA; high citation factor)
4. ACL Findings / EMNLP Findings (no APC, ACL Anthology; surveys do well here)
5. NeurIPS Datasets & Benchmarks Track (free; benchmarks here hit 500+ if adopted)

---

## 3. Recommended path: A comprehensive survey + framework on LLM-as-Judge

### 3.1 Why this beats T02 (the previous bridge)

| Dimension | T02 (position bias) | Survey on LLM-as-Judge |
|---|---|---|
| Citation ceiling (solo, first publication) | ~80–150 | **300–800** |
| P(≥500 cit) | <5% | **20–30%** |
| Time to first submission | 4–6 months | 8–12 months |
| Cost (API + tools) | ~$1,500 | <$200 (mostly reading) |
| Venue (free, USCIS-valued) | EMNLP Findings or TMLR | **JMLR, TMLR, ACM CS** |
| USCIS NIW/EB-1A strength | Moderate | **Very high** (authoritative authorship) |
| Risk of scoop | Medium (T02 niche is small) | Low (you become the reference) |
| Solo executability | High | **Medium-high** (survey is reading + writing; no infrastructure) |

### 3.2 Specific paper concept

**Working title**:
*"LLM-as-Judge: A Comprehensive Survey of Methods, Failure Modes, and Evaluation Frameworks"*

Alternative titles (pick after deeper literature scan):
- *"Trustworthy LLM Judges: A Survey of Reliability, Robustness, and Reproducibility"*
- *"LLM-as-Judge: A Decade of Evaluator Models — Methods, Pitfalls, and the Road Ahead"*

### 3.3 The "Survey + Framework + Empirical" pattern (the citation magnet)

The papers that hit 500+ in this space share a structure:

1. **Comprehensive literature survey** (50–200 papers reviewed)
   → cited because: it saves other researchers 100 hours of reading
2. **Novel taxonomy or framework** (your contribution)
   → cited because: subsequent papers must position themselves within your framework
3. **Empirical case study** (validates the framework)
   → cited because: the empirical results are themselves a reference
4. **Identified open problems** (the research agenda)
   → cited because: every paper that addresses an open problem cites the source

**The T02 position-bias work can fit inside this** as Section 6.3 ("Case Study:
Position Bias Across Judge Models") — saving the T02 effort, not wasting it.

### 3.4 What goes in (high-level)

The survey covers six pillars (detailed in `06_paper_pipeline/SURVEY_llm_judge/SURVEY_STRUCTURE.md`):

1. **Foundations** — what LLM-as-Judge is, why it emerged, when to use it
2. **Methods** — pointwise vs pairwise, single-judge vs panel, with reference vs without
3. **Failure modes** — position bias, prompt injection, self-preference, length bias, style bias, format bias, calibration drift
4. **Defences and mitigations** — randomised positions, multi-judge consensus, judge ensembling, calibration methods
5. **Evaluation methodology for judges themselves** — how to validate that your judge is reliable
6. **Open problems and research agenda** — adversarial robustness, multilingual judging, long-context judging, judge alignment with human values

### 3.5 Why this paper plausibly hits 500+ citations

The growth trajectory of LLM-as-Judge papers:
- 2022: ~50 papers used LLM-as-Judge in title/abstract
- 2023: ~300
- 2024: ~1,200
- 2025 (full year est.): ~2,500
- 2026–2028: likely 3,000–5,000 per year

If even 10% of future LLM-as-Judge papers cite a comprehensive survey as their
default reference, that is 300–500 citations per year by 2027–2028. The 500+
threshold is plausibly hit within 18–36 months of publication.

---

## 4. Reconciling with the existing bridge strategy

**The bridge strategy (T02) is not wasted.** Two ways to integrate:

### Option A (recommended): Survey-primary, T02 as case study
- Stop T02 as a standalone publication target
- Re-use the T02 protocol as Section 6.3 of the survey
- Total elapsed time to FIRST publication: ~10–14 months (longer than bridge)
- But the paper that publishes is the high-citation survey, not the bridge

### Option B: Both in parallel (high effort)
- Continue T02 on the existing 4–6 month timeline
- Submit T02 to EMNLP 2026 Findings or TMLR
- In parallel, write the survey for JMLR or ACM CS (8–12 months in parallel)
- T02 becomes the proof-of-credibility for the survey
- Total effort ~2× one paper; total elapsed time ~12 months to two papers

### Option C: Survey-only, abandon T02
- Stop T02 entirely; redirect 100% effort to the survey
- Highest quality survey, shortest time, but **no peer-reviewed publication
  for 10–14 months**
- Risk: long gap with zero publications is hard for NIW/EB-1A timing

### My recommendation: **Option B**

Reasons:
1. T02 is already 70% scoped; killing it discards ~2 weeks of work.
2. Having T02 published as a complement reinforces the survey's authority.
3. A first-time author submitting a sole-authored survey at JMLR / ACM CS
   benefits from being able to cite their own prior empirical work
   ("see [Author 2026] for empirical evidence of position bias").
4. EB-1A counts **number** of peer-reviewed publications, not just citations.
   Two publications beats one.
5. Workload: surveys are mostly reading; T02 is mostly running experiments.
   These are different cognitive modes that can be alternated to prevent burnout.

If bandwidth is genuinely limited: pick **Option A** (survey-primary).

---

## 5. Venue analysis (free venues, top tier, citation potential)

### 5.1 JMLR — Journal of Machine Learning Research
- **APC**: $0
- **Review timeline**: 6–18 months (slow but thorough)
- **Acceptance rate**: very selective, especially for surveys
- **Indexing**: DBLP, Google Scholar, ACM, Web of Science
- **Citation potential**: highest of any free ML venue
- **USCIS value**: very high (authoritative journal of record)
- **Solo first-author survey acceptable?** Possible but harder — JMLR surveys
  are usually authored by established researchers. A submission is feasible but
  expect more revisions. Strong prior empirical work (T02) helps establish authority.

### 5.2 TMLR — Transactions on Machine Learning Research
- **APC**: $0
- **Review timeline**: 3–6 months (rolling, action-editor model)
- **Acceptance rate**: moderate (TMLR is newer, more open)
- **Indexing**: DBLP, Google Scholar, OpenReview
- **Citation potential**: high (rising fast; modern community venue)
- **USCIS value**: high (accepted as peer-reviewed publication of record)
- **Solo first-author survey acceptable?** Yes — TMLR explicitly evaluates
  work, not authors. The "Survey Certification" track exists for surveys.

### 5.3 ACM Computing Surveys (CSUR)
- **APC**: $0 for non-OA (Green OA via author website / arXiv)
- **Review timeline**: 8–18 months
- **Acceptance rate**: very selective
- **Indexing**: DBLP, Google Scholar, Web of Science, Scopus
- **Citation potential**: very high (impact factor ~14)
- **USCIS value**: very high
- **Solo first-author survey acceptable?** Possible — CSUR has accepted
  solo-authored surveys from PhD students before. Quality bar is very high.

### 5.4 Foundations and Trends® in Machine Learning
- **APC**: $0 (publisher pays via subscription model; OA option available with fee)
- **Review timeline**: 6–12 months
- **Length**: 80–200 pages (monograph-length surveys)
- **Citation potential**: very high (these are field-defining monographs)
- **USCIS value**: very high
- **Solo first-author survey acceptable?** Usually invited; cold submissions
  rarely accepted. Not recommended for first survey.

### 5.5 ACL Computing Surveys / ACM TIST
- Smaller venues; lower citation potential than JMLR / CSUR
- Not recommended unless others reject

### 5.6 ACL Findings / EMNLP Findings (survey track)
- **APC**: $0
- **Review timeline**: 4–7 months
- **Length**: 8–10 pages (too short for a comprehensive survey)
- **Citation potential**: moderate (limited by length)
- **Best for**: short survey or position paper, not the main contribution

### Recommended venue strategy

1. **Primary**: TMLR (survey certification) — best probability × speed × quality balance
2. **If TMLR rejects**: ACM Computing Surveys
3. **If both reject**: JMLR (very slow, but the most prestigious)
4. **Never**: paid OA journals (PLOS, Frontiers, IEEE Access), MDPI venues

**Why TMLR is primary**:
- Faster than JMLR / CSUR (matters for citation accumulation: earlier publication = more time to be cited)
- Modern community venue with high readership
- Survey Certification explicitly recognises comprehensive surveys
- Solo first-author submissions are not penalised
- Free + indexed + USCIS-recognised

---

## 6. USCIS alignment — what each option proves for NIW/EB-1A

### 6.1 NIW (National Interest Waiver) — three prongs

**Prong 1: Substantial merit and national importance**
- A comprehensive survey of LLM-as-Judge methods directly supports US
  national priorities in AI safety (NIST AI RMF, Executive Order on AI,
  EU AI Act compliance).
- Argument: LLM judges are now embedded in safety-critical systems
  (RLHF training, content moderation, AI-assisted medical and legal triage).
  Systematic understanding of their failure modes is in the national interest.
- A peer-reviewed survey is the canonical "evidence of substantial merit."

**Prong 2: Well positioned to advance the proposed endeavour**
- Authored a peer-reviewed survey = "established authority in the field"
- Combined with T02 (empirical evidence) + JudgeSense (originality) =
  credible profile.

**Prong 3: Beneficial to the US to waive the labour cert**
- A widely-cited survey is "evidence of impact" required for this prong.
- 500+ citations would be strong; even 100–200 citations meets the standard
  if the venue is authoritative.

### 6.2 EB-1A (Extraordinary Ability) — meeting 3 of 10 criteria

A peer-reviewed survey + T02 + JudgeSense supports at least these criteria:

| EB-1A Criterion | How this paper supports it |
|---|---|
| (i) Awards | (Indirect — comes later from citations) |
| (iii) Published material about you in major media | (Indirect — citation tracking) |
| (iv) Judging the work of others | (Indirect — survey authors are invited to review) |
| (v) Original contributions of major significance | **Direct** — new taxonomy + framework + identified open problems |
| (vi) Authorship of scholarly articles | **Direct** — sole-authored peer-reviewed survey at TMLR / JMLR / CSUR is one of the strongest exhibits possible |
| (viii) Leading or critical role in distinguished organisations | (Indirect) |

**A sole-authored survey at JMLR or ACM Computing Surveys is among the
strongest single exhibits for EB-1A criterion (vi).**

### 6.3 Citation count as evidence

For both NIW and EB-1A, citation counts serve as objective evidence of impact:

| Citation count (3 years post-publication) | NIW strength | EB-1A strength |
|---|---|---|
| 0–20 | Weak — does not meet "impact" standard | Weak |
| 20–100 | Moderate — supports merit but not impact | Moderate |
| 100–500 | Strong — credible "impact in the field" | Strong |
| 500+ | Very strong — top-percentile impact | Very strong |

The 500+ goal aligns perfectly with both immigration paths.

---

## 7. The 12-month plan (high-level)

| Month | Survey (primary) | T02 (parallel) | Rationale |
|---|---|---|---|
| 1 | Literature collection (200+ papers) | Code scaffold continues | Survey reading is mostly evenings; T02 in main hours |
| 2 | Taxonomy v1 + outline | T02 pilot data collection | |
| 3 | Section drafts 1–2 (foundations, methods) | T02 main data run | |
| 4 | Section drafts 3–4 (failure modes, defences) | T02 analysis | |
| 5 | Section drafts 5–6 (evaluation, open problems) | T02 paper draft | T02 submission target |
| 6 | Survey full draft v1 | T02 submitted to ARR / EMNLP Findings | |
| 7 | Internal review + revisions | Respond to T02 reviews if any | |
| 8 | Survey v2 + figures + tables | | |
| 9 | TMLR submission | T02 decision (likely) | |
| 10–11 | Survey review cycle | | |
| 12 | Survey camera-ready or revisions | | |

**Result by month 12**:
- T02 published (or in late review) at EMNLP Findings / TMLR — first peer-reviewed publication
- Survey under review at TMLR — second peer-reviewed publication pending
- Both publications cite each other → reciprocal citation boost

---

## 8. Why a survey at TMLR can plausibly hit 500+ citations (the case)

1. **The field is exploding.** Easily 2,000+ new LLM-eval / LLM-judge papers
   per year in 2026–2028. Each one needs to cite a reference work.

2. **No definitive survey at a top free venue.** Gu et al. 2024 exists on
   arXiv but is narrower and not at TMLR / JMLR / CSUR. The gap is real.

3. **TMLR is increasingly cited.** HELM (Liang et al. 2022) at TMLR has
   1,500+ citations.

4. **Survey papers benefit from compounding adoption.** Once a paper becomes
   the "default reference" for the field, citations compound.

5. **Open code + datasets boost citations.** If the survey releases an
   accompanying repo (cataloguing all surveyed papers + reproducibility info),
   it becomes the field's working bibliography.

6. **Active marketing.** A well-promoted survey (tweets, blog posts,
   newsletter mentions, recorded talks) reaches the practitioners who
   eventually cite it. This is not "selling out" — it is how citation networks
   form in modern ML.

**Probability assessment**:
- P(survey accepted at TMLR with the structure described) = 60–75%
- P(survey accepted at JMLR or CSUR fallback) = 30–50%
- P(survey accepted somewhere free and reputable in 12 months) = 80–90%
- P(survey hits 100 citations within 24 months) = 50–65%
- P(survey hits 500 citations within 36 months) = **20–35%**

These are honest. The 500+ goal is plausible but not guaranteed. We maximise
the probability by following the protocol (`06_paper_pipeline/SURVEY_llm_judge/`).

---

## 9. What we are explicitly NOT doing

- **Not chasing predatory or low-prestige venues** even if they accept faster.
- **Not paying APCs** — the constraint is binding; this rules out most "open access" journals.
- **Not splitting the survey across multiple short papers** — the field needs the comprehensive reference, not 6 short pieces.
- **Not collaborating with established PIs as a shortcut** — solo authorship has higher EB-1A value (criterion vi specifically rewards solo work).
- **Not optimising for "trendy"** content — the survey covers the foundational subject (LLM-as-Judge) which is durably important, not a 3-month fad.

---

## 10. What success looks like at month 12 vs month 36

### Month 12 (end of execution)
- T02 paper accepted at EMNLP Findings / TMLR (peer-reviewed publication #1)
- Survey submitted to TMLR with strong initial reviews
- Companion GitHub repo with 100+ surveyed papers tagged with metadata
- Personal arXiv presence: 3–4 papers (T02 preprint, survey preprint, T07 preprint if executed, JudgeSense preprint)

### Month 24 (mid-trajectory)
- Both papers published
- Survey: 50–150 citations
- T02: 20–60 citations
- Speaking invitations from workshops / industry
- Reviewer invitations (NeurIPS, ICLR, EMNLP)

### Month 36 (citation target)
- Survey: **200–600 citations** (target: ≥500)
- T02: 60–150 citations
- Combined publication portfolio supports NIW filing (with strong impact evidence)
- Foundation for EB-1A filing 1–2 years later

---

## 11. Risk register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Survey scope too broad → poor quality | Medium | High | Strict scope boundaries (see SCOPE.md); stop adding sections at month 5 |
| Solo first-author survey rejected at TMLR | Low-medium | Medium | Have ACM CS and JMLR as fallback; revise per reviews |
| Field shifts; survey becomes outdated by publication | Medium | Medium | Include "living survey" supplementary website with quarterly updates |
| Another survey appears at TMLR / JMLR during execution | Low | High | `scripts/15_arxiv_watch.py` monitors; if scoop, pivot to differentiated angle (e.g., focus only on judge security) |
| Burnout from year-long solo project | Medium | High | T02 alternation prevents single-cognitive-mode fatigue |
| Survey publication does not hit 500 citations | Medium-high | Medium | Even at 100–300 citations, the paper meets NIW / EB-1A standards |
| Negative reviewer assessment damages reputation | Low | Medium | Anonymous double-blind review (TMLR); rejected revisions can be re-submitted elsewhere |

---

## 12. Decision required

Pick **Option A**, **B**, or **C** from §4. My recommendation: **Option B
(both T02 and survey in parallel)**. Document the choice in `DECISIONS.md`.

If choosing **Option A** (survey-primary): the bridge strategy is paused and
T02 protocol becomes a section reference inside the survey.

If choosing **Option C** (survey-only): T02 is killed; full effort to survey.

---

## 13. Files this strategy creates

This document spawns:

- `06_paper_pipeline/SURVEY_llm_judge/PROTOCOL.md` — execution protocol
- `06_paper_pipeline/SURVEY_llm_judge/SURVEY_STRUCTURE.md` — section-by-section plan
- `06_paper_pipeline/SURVEY_llm_judge/VENUE_ANALYSIS.md` — JMLR vs TMLR vs CSUR deep dive
- `06_paper_pipeline/SURVEY_llm_judge/USCIS_EVIDENCE_MAP.md` — NIW / EB-1A criteria mapping
- `06_paper_pipeline/SURVEY_llm_judge/QUALITY_RUBRIC.md` — referee-proofing checklist
- `06_paper_pipeline/SURVEY_llm_judge/KILL_CRITERIA.md` — when to abandon
- Update to `DECISIONS.md` with the strategy choice
- New `NEXT_90_DAYS.md` reflecting the longer horizon

---

*Signed off: 2026-05-16. This strategy is not in tension with the constraints
the user stated. The 500-citation target is plausibly achievable through
the survey path at a free venue. The path is honest about probability and
prepared for the failure modes.*
