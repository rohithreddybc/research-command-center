# Survey on LLM-as-Judge — Execution Protocol

*Source strategy*: `reports/HIGH_CITATION_STRATEGY.md`
*Status*: Primary high-citation paper. Execution begins month 1.
*Citation target*: 500+ within 36 months of publication.
*Venue*: TMLR (primary) → ACM Computing Surveys → JMLR (fallbacks).

---

## 1. The deliverable

**Working title** (updated 2026-05-16 — citation-optimised):
*"Judging the Judges: A Comprehensive Survey of LLM-as-a-Judge"*

Title rationale (`reports/VENUE_REOPTIMIZATION.md` §Part 2 — Title re-optimization):
- "Judging the Judges" is a memorable hook (alliteration + concept inversion)
  → quoted and shared more easily → higher citation discovery
- "Comprehensive Survey" signals completeness → reviewers and readers expect a definitive reference
- 11 words → fits citation manager truncation behaviour
- Topic keyword "LLM-as-a-Judge" present → search discoverability

Fallback title if reviewers object to the catchy phrasing as unscientific:
*"On the Reliability of LLM-as-a-Judge: A Comprehensive Survey"*

Previous working title (now deprecated):
*"LLM-as-Judge: A Comprehensive Survey of Methods, Failure Modes, and Evaluation Frameworks"*

**Format**: 60–100 page comprehensive survey + companion GitHub repo + supplementary website

**Length budget by venue**:
- TMLR survey certification: 60–80 pages
- ACM Computing Surveys: 50–80 pages
- JMLR survey: 60–120 pages

**Companion artifacts** (cited from the paper, raise citation count):
- `llm-judge-survey` GitHub repo: structured metadata for every surveyed paper
- Live updating website (Quarto or MkDocs): citation tracker, updated annually
- Reproducibility appendix: every claim traceable to a primary source

---

## 2. Why this paper, why now

**The opportunity** (from `HIGH_CITATION_STRATEGY.md` §2 and §8):
- No comprehensive peer-reviewed survey of LLM-as-Judge exists at TMLR / JMLR / CSUR
- The field is producing ~2,500+ papers per year and growing
- Existing arXiv survey (Gu et al. 2024) is narrower; a definitive top-venue survey
  could become the field's default reference
- Citation network compounds: once the survey is "the" reference, every new LLM-judge
  paper cites it → 500+ citations within 24–36 months is plausible

**The risk**:
- A competing survey at TMLR / JMLR appears mid-execution
- The field shifts (e.g., LLM judging becomes obsolete due to better automated metrics)
- Solo first-author survey faces uphill battle at JMLR

Mitigations are in `KILL_CRITERIA.md`.

---

## 3. Scope boundaries (what is in, what is out)

### In scope
- LLM-as-Judge methods: pointwise, pairwise, listwise, panel, reference-based
- LLM judge applications: RLHF reward modelling, AutoEval, benchmark scoring,
  safety evaluation, content moderation
- Failure modes: position bias, prompt injection, self-preference, length bias,
  style bias, format bias, calibration drift, length-vs-quality confounding
- Defences and mitigations: prompting techniques, ensembling, calibration,
  human-in-the-loop, structured outputs
- Evaluation of judges themselves: meta-evaluation, agreement with humans
- Open problems and research agenda

### Out of scope (explicit boundaries)
- Pre-LLM automatic evaluation (BLEU, ROUGE, BERTScore — covered by Liu et al. 2023 survey)
- Human evaluation methodology (covered by van der Lee et al. 2019 surveys)
- General LLM evaluation beyond judging (covered by Chang et al. 2023)
- Specific clinical / legal / financial domain judges (mention only in §6 applications)
- Multimodal judges (image, audio) — note as future work; do not deep-dive
- Multilingual judging beyond English-Spanish-Chinese — note as research gap

Scope creep is the #1 risk for surveys. Re-read this section monthly.

---

## 4. Timeline (12 months from start to TMLR submission)

| Month | Phase | Deliverable | Gate to next phase |
|---|---|---|---|
| 1 | Literature collection | 200+ papers indexed in `data/survey_corpus.csv` | ≥150 unique on-topic papers found |
| 2 | Taxonomy + outline | Outline v1 with 6 sections; taxonomy in `TAXONOMY.md` | Outline reviewed against 10 random papers — fits all 10 |
| 3 | Draft §1 + §2 | Introduction, Foundations + Methods | ~15 pages written |
| 4 | Draft §3 + §4 | Failure Modes + Defences | ~30 pages cumulative |
| 5 | Draft §5 + §6 | Evaluation Methodology + Open Problems | ~50 pages cumulative |
| 6 | Full draft v1 | All sections; figures placeholders | Complete draft exists end-to-end |
| 7 | Internal critique | Self-review + 1 external reader if possible | Reader returns written feedback |
| 8 | Revision v2 | Address critique; finalize figures and tables | All TODOs in draft resolved |
| 9 | Companion repo | Publish `llm-judge-survey` GitHub repo with metadata for all papers | Repo passes own self-check (every paper cited has metadata) |
| 10 | TMLR submission | Submit to TMLR (survey certification) | Submission confirmed |
| 11 | Reviewer cycle 1 | Reviews returned; major revisions if requested | Author response submitted |
| 12 | Reviewer cycle 2 | Final decision | Accept / reject |

**Hard date**: if no TMLR submission by month 14, trigger `KILL_CRITERIA` review.

---

## 5. Phase 1 — Literature collection (month 1)

### 5.1 Method
Build a structured corpus of every LLM-as-Judge paper from 2021–2026.

**Sources to query**:
- Semantic Scholar API (use existing `02_collect_topic_evidence.py` machinery)
- arXiv (search "LLM judge", "LLM-as-a-Judge", "evaluator LLM", "judge model")
- ACL Anthology (annual proceedings 2022–2026)
- OpenReview (NeurIPS, ICLR, COLM)
- Google Scholar (manual sample to find non-indexed work)
- Existing surveys' bibliographies (Gu et al. 2024, Chang et al. 2023) — mine for papers

**Initial seed queries** (extend over the month):
```
"LLM-as-a-judge"
"LLM as judge"
"language model judge"
"automatic evaluator" AND ("large language model" OR "LLM")
"reward model" AND ("RLHF" OR "preference learning")
"pairwise preference" AND "language model"
"judge prompt" AND ("evaluation" OR "benchmark")
```

### 5.2 Per-paper metadata schema

Each paper in `data/survey_corpus.csv` gets:

| Field | Description |
|---|---|
| paper_id | Citation key (e.g., zheng2023judging) |
| title | Full title |
| authors | All authors, " and "-separated |
| year | Publication year |
| venue | Full venue name |
| arxiv_id | If applicable |
| doi | If applicable |
| url | Primary URL |
| in_scope | yes / partial / no |
| section | Which survey section this paper belongs in (1.1, 3.2, etc.) |
| key_contribution | 1–2 sentence summary |
| failure_mode_addressed | Which failure mode(s) the paper addresses (if any) |
| method_type | pointwise / pairwise / panel / other |
| has_code | yes / no / linked |
| has_dataset | yes / no / linked |
| read_status | unread / skimmed / read / deep |
| relevance_to_us | High / Medium / Low |
| my_notes | Free text |

**Target**: 200+ papers indexed by end of month 1. Target 150 deeply read by end of month 6.

### 5.3 Read-prioritisation rule
- Tier 1 (must read deeply): venue ∈ {NeurIPS, ICML, ICLR, ACL, EMNLP, NAACL, TMLR, JMLR} AND citations > 50
- Tier 2 (read carefully): cited by ≥2 Tier 1 papers
- Tier 3 (skim only): arXiv-only with <10 citations and unrelated to our taxonomy gaps

---

## 6. Phase 2 — Taxonomy + outline (month 2)

### 6.1 The taxonomy is THE contribution

The single most-cited feature of a comprehensive survey is its taxonomy.
Subsequent papers cite the taxonomy to position their own work
("We extend Author 2027's taxonomy of judge failure modes by adding...").

**Initial taxonomy structure** (to be refined in `TAXONOMY.md`):

```
LLM-as-Judge
├── Methods
│   ├── Single-pass: pointwise scoring, pairwise comparison, listwise ranking
│   ├── Multi-pass: chain-of-thought judging, self-consistency, panel voting
│   ├── Reference-based: with gold answer, without gold answer
│   └── Augmented: tool-using judges, retrieval-augmented judges
├── Failure Modes
│   ├── Input-side: position bias, length bias, style bias, format bias
│   ├── Adversarial: prompt injection (CSPI), jailbreak via candidate
│   ├── Self-referential: self-preference, family-preference
│   ├── Calibration: confidence drift, scale compression, scoring distribution shift
│   └── Methodological: human-judge gap, evaluator-evaluator gap
├── Defences
│   ├── Prompt-level: position randomisation, explicit warnings, CoT prompting
│   ├── Ensemble: multi-judge consensus, multi-prompt aggregation
│   ├── Calibration: post-hoc calibration, learned calibration models
│   ├── Hybrid: human-in-the-loop, judge + automatic metric combination
│   └── Structural: structured outputs, parser-validated responses
├── Applications
│   ├── RLHF reward modelling
│   ├── AutoEval pipelines (HELM, MT-Bench, AlpacaEval)
│   ├── Safety and content moderation
│   ├── Benchmark scoring
│   └── Domain-specific (medical, legal, code)
└── Meta-Evaluation
    ├── Agreement with humans
    ├── Cross-judge agreement
    ├── Inter-method agreement
    └── Stability over time / model versions
```

This taxonomy is preliminary; refine in `TAXONOMY.md` as literature is digested.

### 6.2 Section outline

See `SURVEY_STRUCTURE.md` for the full section-by-section plan.

---

## 7. Quality bar (why this survey gets cited, not ignored)

A survey gets cited if it:

1. **Is comprehensive**: covers ≥80% of relevant work in the field
2. **Has a clear taxonomy**: subsequent papers position themselves within it
3. **Is well-written**: prose flows, figures are clear, tables are referenced
4. **Identifies real open problems**: not platitudes; specific testable research questions
5. **Is reproducible**: every claim cites a primary source; metadata-rich repo
6. **Is timely**: published before the field saturates with competing surveys
7. **Is sole-authored or led by a clear voice**: surveys with too many authors read as committee work

Detailed criteria in `QUALITY_RUBRIC.md`.

---

## 8. Companion artifacts (citation multipliers)

### 8.1 GitHub repo `llm-judge-survey`

- One YAML file per surveyed paper with structured metadata
- Search interface (simple web page) for the field
- Quarterly updates with new papers
- Encourages community to file PRs with new entries → community ownership = citations

### 8.2 Living survey website (optional but high-leverage)

- Markdown / Quarto site rendered from the GitHub repo
- Public URL (e.g., `llm-judge-survey.org` or GitHub Pages)
- Citation: "We maintain a living version of this survey at [URL]."
- Becomes a frequently-visited resource → more downloads → more citations

### 8.3 Annotated bibliography

- 500–1000 line BibTeX file released alongside paper
- Reduces friction for any future researcher writing about the field
- Cited directly: "We use the bibliography of [Author 2027] augmented with..."

---

## 9. Marketing plan (citation amplifiers)

Citations are not just about quality — they are about **discoverability**.
Plan (executes after acceptance / preprint posting):

| Channel | What to do | When |
|---|---|---|
| arXiv | Post preprint at time of TMLR submission | Month 10 |
| Twitter / Bluesky | Thread summarising the taxonomy + key findings | Within 48hr of arXiv post |
| GitHub | Public release of `llm-judge-survey` repo with starter PRs | Within 1 week |
| Hacker News / Reddit / r/MachineLearning | Single high-quality post | Within 2 weeks |
| Newsletters | Submit to Sebastian Raschka's, The Batch, ML Notes | Within 1 month |
| Talks | Submit talk proposals to relevant workshops | Months 11–12 |
| Cross-reference | Email authors of the most-cited surveyed papers thanking them and notifying of survey | Within 1 month |
| Conference attendance | Attend NeurIPS / ICLR 2027 and present at workshops | After acceptance |

Marketing without quality is sleazy. Quality without marketing is invisible.
Both are needed.

---

## 10. Reproducibility commitments

- All 200+ papers in the corpus have provenance metadata
- All quantitative claims (e.g., "X% of judges show position bias of magnitude > Y")
  cite a specific paper or our own empirical work (T02)
- All figures generated by code in the companion repo
- No hand-waving: each subsection ends with "Primary references: [..]"

---

## 11. Sign-off + check-in cadence

- **Weekly**: review `data/survey_corpus.csv` growth (target: 50 new papers / week in month 1)
- **Monthly**: review against the timeline (§4) and kill criteria
- **Quarterly**: re-evaluate strategy in light of pipeline scoop watch and field shifts
- **At month 6**: stop adding new sections; everything in is in, everything out is out

| Field | Value |
|---|---|
| Protocol version | 1.0 |
| Protocol date | 2026-05-16 |
| Author | rohithreddybc |
| Target venue (primary) | TMLR (survey certification) |
| Target venue (fallback 1) | ACM Computing Surveys |
| Target venue (fallback 2) | JMLR |
| Target submission date | Month 10 (Feb–Mar 2027) |
| Target acceptance date | Month 14–16 (Jun–Aug 2027) |
| Target publication date | Month 16–18 (Aug–Oct 2027) |
| Target citation count (3yr post-pub) | 500+ |
