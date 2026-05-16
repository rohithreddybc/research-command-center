# Next 90 Days (May 16 – Aug 16, 2026)

*Replaces `NEXT_30_DAYS.md`. The pivot to the survey-primary strategy
extends the planning horizon. Two projects run in parallel: T02 (bridge)
and the LLM-as-Judge survey (primary high-citation paper).*

*Source strategies:*
- *`reports/HIGH_CITATION_STRATEGY.md` — the why and the venue analysis*
- *`06_paper_pipeline/SURVEY_llm_judge/PROTOCOL.md` — the survey execution plan*
- *`06_paper_pipeline/T02_position_bias/PROTOCOL.md` — the T02 execution plan*

---

## Headline: this quarter

By the end of August 2026 (90 days from today), you should have:

- **Survey corpus** of ≥ 150 papers indexed in `data/survey_corpus.csv`
- **Survey draft sections 1 + 2 + 3** (~25 pages) complete
- **T02 pilot** complete (50 items × 2 judges × 1 task)
- **T02 main data collection** begun
- **T07** blocking-paper read and decision logged (`BLOCKING_PAPER_NOTES.md`)
- **Companion repo skeleton** for both papers
- **arXiv watch** running weekly, no kill signals (or pivot if any)

These are the **definition of "on track"**. If 5 of 7 are done by day 90,
on track. If fewer than 3, escalate per kill criteria.

---

## Month 1 (May 16 – June 15, 2026)

### Survey — literature collection phase

- [ ] **Week 1**: Read the strategy docs end-to-end
  - `reports/HIGH_CITATION_STRATEGY.md`
  - `06_paper_pipeline/SURVEY_llm_judge/PROTOCOL.md`
  - `06_paper_pipeline/SURVEY_llm_judge/SURVEY_STRUCTURE.md`
  - `06_paper_pipeline/SURVEY_llm_judge/VENUE_ANALYSIS.md`
  - `06_paper_pipeline/SURVEY_llm_judge/USCIS_EVIDENCE_MAP.md`
  - `06_paper_pipeline/SURVEY_llm_judge/QUALITY_RUBRIC.md`
  - `06_paper_pipeline/SURVEY_llm_judge/KILL_CRITERIA.md`
- [ ] **Week 1**: Disagree with anything? Document in `DECISIONS.md` before continuing.
- [ ] **Week 1**: Red-team self-check from `KILL_CRITERIA.md` "Red-team self-check" section
- [ ] **Week 1**: Read Gu et al. 2024 *"A Survey on LLM-as-a-Judge"* in full; identify ≥ 5 specific gaps in `06_paper_pipeline/SURVEY_llm_judge/GAPS.md`
- [ ] **Week 2**: Build initial corpus — run targeted queries via `scripts/02_collect_topic_evidence.py` adapted for the survey topic. Target: 100 papers indexed.
- [ ] **Week 3**: Hand-augment corpus from ACL Anthology, OpenReview, top survey bibliographies. Target: 150 papers.
- [ ] **Week 4**: Initial taxonomy draft in `06_paper_pipeline/SURVEY_llm_judge/TAXONOMY.md`. Compare to Gu et al. 2024.

### T02 — pilot phase

- [ ] **Week 1**: Read `06_paper_pipeline/T02_position_bias/PROTOCOL.md` sign-off again
- [ ] **Week 2**: Code scaffold — `clients/` for at least OpenAI + Anthropic, `judge.py`, `conditions.py`
- [ ] **Week 3**: Load 50 items from one task (CNN/DailyMail validation)
- [ ] **Week 4**: Run pilot: 50 items × 2 judges × 1 task = 100 calls
- [ ] **Week 4**: Inspect 10 outputs manually; document in `06_paper_pipeline/T02_position_bias/PILOT_NOTES.md`

### T07 — clearing phase (parallel to above)

- [ ] **Week 1–2**: Find and read "Red Teaming the Mind of the Machine" (arXiv 2025)
- [ ] **Week 2**: Write `06_paper_pipeline/T07_judge_injection/BLOCKING_PAPER_NOTES.md`
- [ ] **Week 3**: If proceed: write `DIFFERENTIATOR.md` + draft `ARXIV_PREPRINT_STUB.md`
- [ ] **Week 4**: If proceed: post T07 arXiv preprint (priority claim)

### Infrastructure

- [ ] **Week 1**: Run `python scripts/15_arxiv_watch.py --bootstrap` once arXiv un-throttles
- [ ] **Week 1**: Schedule weekly arXiv watch (Windows Task Scheduler)
- [ ] **Week 2**: Add survey-specific watch query (covered by `data/scoop_watch_queries.json` extension)
- [ ] **Week 4**: First-month checkpoint — fill in K1–K4 rows in both KILL_CRITERIA sign-off tables

---

## Month 2 (June 16 – July 15, 2026)

### Survey — taxonomy lock + first writing

- [ ] Lock the taxonomy (no major changes after this month)
- [ ] Draft §1 Introduction (~5 pages)
- [ ] Draft §2 Foundations (~7 pages)
- [ ] Begin §3 Methods Taxonomy
- [ ] Continue reading: target 50 additional papers (cumulative 200 in corpus)

### T02 — main data collection

- [ ] Acquire API budget for all 5 judge models
- [ ] Run full grid: 200 items × 5 judges × 4 conditions × 3 tasks (12,000 calls)
- [ ] Continuous logging to `data/runs/` JSONL files
- [ ] Cost monitoring vs $1,500 cap

### Infrastructure / quality

- [ ] Monthly checkpoint — both KILL_CRITERIA tables
- [ ] Update arxiv watch report; review for kill signals
- [ ] Mid-quarter retrospective in `DECISIONS.md`: what's working, what's not

---

## Month 3 (July 16 – August 16, 2026)

### Survey — middle sections

- [ ] Complete §3 Methods Taxonomy
- [ ] Draft §4 Failure Modes (start; the biggest section)
- [ ] Target cumulative: §1 + §2 + §3 done; §4 in progress (~30 pages total)

### T02 — analysis + first draft

- [ ] Complete data collection
- [ ] Compute PBI per (model, task) with bootstrap CIs
- [ ] Kendall's τ rank-order analysis
- [ ] BH multiple-comparisons correction
- [ ] Start T02 paper draft (introduction + method)

### Companion artifacts

- [ ] Create `llm-judge-survey` private repo on GitHub
- [ ] Migrate `data/survey_corpus.csv` to structured YAML per paper
- [ ] Build minimum-viable search interface (static site)

### End-of-quarter review

- [ ] Headline check (top of this file): how many of the 7 are done?
- [ ] Update `DECISIONS.md` with quarter retrospective
- [ ] Write `NEXT_90_DAYS_Q2.md` (Aug–Nov 2026) based on actual progress

---

## What NOT to do this quarter

- **Do not start writing the survey before reading 150 papers.** Premature writing
  results in shallow analysis and forces rewrites.
- **Do not start T01 or B05 work.** They are queued — bandwidth is finite.
- **Do not chase a faster survey venue** (e.g., a workshop). The whole point of
  the strategy pivot is to publish at a top venue, not a fast venue.
- **Do not skip the quality rubric.** Every monthly checkpoint, re-read
  `06_paper_pipeline/SURVEY_llm_judge/QUALITY_RUBRIC.md` and tick what's done.
- **Do not announce the survey publicly before the corpus is 80% complete.**
  Public commitment without delivery damages credibility.
- **Do not respond to a single negative reviewer comment by abandoning the project.**
  Surveys at TMLR / JMLR / CSUR all have multi-round revision cycles by design.

---

## What to do when stuck

1. **Stuck on reading**: drop to 1 paper per day for a week. Momentum > volume.
2. **Stuck on writing**: write 200 words/day on whichever section feels easiest.
   The hard sections benefit from cumulative confidence.
3. **Stuck on T02 experiments**: check the API status page; if throttled, switch
   to writing the T02 paper sections that don't need data.
4. **Stuck on the taxonomy**: pick 5 papers and force-fit them into the current
   taxonomy. Where they don't fit, that's a new leaf.
5. **Stuck on motivation**: re-read `06_paper_pipeline/SURVEY_llm_judge/USCIS_EVIDENCE_MAP.md`.
   The mechanical path from survey → NIW/EB-1A → green card is concrete.

---

## Monthly checkpoint format

At the end of each month, write a 200-word retrospective and append to `DECISIONS.md`:

```
| 2026-XX-XX | Month X checkpoint | Survey: X papers indexed, X pages drafted. T02: X% complete. Issues: ... . Adjustments: ... | n/a | n/a |
```

---

## Quarter-end gate

If at month 3 end:
- **5 of 7 headline items done**: continue per plan.
- **3–4 of 7 done**: tighten — drop T07, focus on survey + T02 only.
- **< 3 of 7 done**: trigger KILL_CRITERIA review for both projects. Consider
  collapsing to survey-only (Option A) or pausing both for 30 days.

---

## When to file NIW (preliminary thinking)

This 90-day window is too early for an NIW filing. Earliest realistic filing:
month 14–18, after the survey is published. See `06_paper_pipeline/SURVEY_llm_judge/USCIS_EVIDENCE_MAP.md`
for the timeline mapping.
