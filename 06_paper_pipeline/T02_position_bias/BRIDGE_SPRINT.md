# T02 — 9-Week Bridge Sprint Checklist

*Source*: `06_paper_pipeline/T02_position_bias/PROTOCOL.md` v1.1 (timeline §8)
*Target*: TMLR submission + arXiv preprint by **2026-07-15**
*Publication target*: December 2026

Print this. Tape it to the monitor. Tick weekly.

---

## Week 1 — May 16–22, 2026 (sprint kickoff)

- [ ] Re-read `PROTOCOL.md` §1–§13 end-to-end and sign off in §13
- [ ] Re-read `KILL_CRITERIA.md` and red-team self-check
- [ ] Create private GitHub repo: `github.com/rohithreddybc/judge-bias-eval`
- [ ] Copy `CODE_SCAFFOLD.md` repo layout into the new repo
- [ ] Implement `clients/base.py` and `clients/openai_client.py`
- [ ] Implement `clients/anthropic_client.py`
- [ ] Implement `judge.py`, `conditions.py` (no actual judging yet — pure dataclasses)
- [ ] Implement `budget.py` with hard $1,500 cap
- [ ] Write `tests/test_pbi.py` skeleton (TDD)
- [ ] **Gate**: code passes own self-test (mocked clients), no real API calls yet

**Estimated hours**: 14 (T02) + 6 (survey reading) = 20

---

## Week 2 — May 23–29, 2026 (dataset + API access)

- [ ] Acquire OpenAI API key with $500 budget
- [ ] Acquire Anthropic API key with $500 budget
- [ ] Acquire Together AI key (for Llama-3.3-70B + Mistral-Large-2) — $200 budget
- [ ] Acquire Google AI Studio key — $100 budget
- [ ] Implement `clients/together_client.py` and `clients/google_client.py`
- [ ] Load 200 items from CNN/DailyMail validation (T-Sum task)
- [ ] Construct paraphrase pairs OR use existing labelled ties — document the choice in `PILOT_NOTES.md`
- [ ] Write prompt templates in `data/prompts/T-Sum.yaml`
- [ ] **Gate**: one end-to-end call works (1 item × 1 judge × 1 condition → JSON-line in `data/runs/`)

**Estimated hours**: 14 (T02) + 6 (survey) = 20

---

## Week 3 — May 30 – June 5, 2026 (pilot)

- [ ] Run pilot: 50 items × 2 judges (GPT-4o + Claude) × 1 task (T-Sum) × 4 conditions
  = 400 calls
- [ ] Cost check: should be ~$30
- [ ] Inspect 10 outputs manually; document patterns in `PILOT_NOTES.md`
- [ ] Compute pilot PBI for both judges
- [ ] **Decision gate (K2 check)**: Is PBI > 0.02 with non-zero-overlapping CI? If yes, proceed.
  If no, follow K2 action plan in `KILL_CRITERIA.md`
- [ ] Refine prompts if pilot reveals format / parsing issues
- [ ] Update `CHANGES.md` with any protocol adjustments

**Estimated hours**: 14 (T02) + 6 (survey) = 20

---

## Week 4 — June 6–12, 2026 (data collection part 1)

- [ ] Run T-Sum cohort: 200 items × 5 judges × 4 conditions = 4,000 calls
- [ ] Cost check: ~$240 cumulative
- [ ] Daily JSONL logs to `data/runs/T-Sum_<date>.jsonl`
- [ ] Sanity check at end of week: response parse rate ≥ 95%
- [ ] **Gate**: T-Sum cohort complete; data quality acceptable

**Estimated hours**: 14 (T02) + 6 (survey) = 20

---

## Week 5 — June 13–19, 2026 (data collection part 2)

- [ ] Run T-QA cohort: 200 × 5 × 4 = 4,000 calls
- [ ] Run T-Code cohort: 200 × 5 × 4 = 4,000 calls
- [ ] Cost check: ~$720 cumulative (well under $1,500 cap)
- [ ] **Decision gate (K3 check)**: cost projections still under $1,500? If at $1,200,
  drop T-Code or drop one judge per `PROTOCOL.md` §8 scope reductions
- [ ] **Gate**: all 12,000 calls complete

**Estimated hours**: 14 (T02) + 6 (survey) = 20

---

## Week 6 — June 20–26, 2026 (analysis)

- [ ] Run `pbi.py` analysis: compute PBI per (model, task) with bootstrap CIs
- [ ] Run `stability.py`: Kendall τ between C1 vs C2 rankings
- [ ] Apply BH correction across 15 (model, task) tests at q=0.05
- [ ] Generate all paper tables (Table 1: PBI; Table 2: mitigations effectiveness)
- [ ] Generate all paper figures (Figure 1: Kendall τ vs N; Figure 2: Wasserstein for T-Code)
- [ ] **Gate**: every figure in the paper traceable to a specific JSONL record

**Estimated hours**: 10 (T02) + 10 (survey) = 20

---

## Week 7 — June 27 – July 3, 2026 (draft v1)

- [ ] Draft §1 Introduction (~1 page) — use `PAPER_OUTLINE.md` as scaffold
- [ ] Draft §2 Background and Related Work (~1 page)
- [ ] Draft §3 Method (~1.5 pages)
- [ ] Draft §4 Experiments (~1 page)
- [ ] Draft §5 Results (~1.5 pages)
- [ ] Insert all tables and figures from week 6
- [ ] **Gate**: 6-page draft complete with all data; missing only §6+§7

**Estimated hours**: 10 (T02) + 10 (survey) = 20

---

## Week 8 — July 4–10, 2026 (draft v2)

- [ ] Draft §6 Discussion (~1 page)
- [ ] Draft §7 Conclusion (~0.5 page)
- [ ] Refine abstract (≤ 200 words)
- [ ] Polish every figure (high-resolution, accessible)
- [ ] Write Reproducibility Appendix
- [ ] Generate BibTeX: `python scripts\16_extract_bibtex.py --topic T02 --min-relevance 0.4`
- [ ] Cross-reference all citations
- [ ] Self-review pass: read paper from start to finish; mark every TODO / unclear claim
- [ ] **Gate**: full 8-page paper exists end-to-end with all TODOs resolved

**Estimated hours**: 12 (T02) + 8 (survey) = 20

---

## Week 9 — July 11–15, 2026 (submission week)

- [ ] Mon-Tue: final revisions per self-review notes
- [ ] Wed: format check — TMLR LaTeX template compiles cleanly
- [ ] Wed: companion GitHub repo public release — `judge-bias-eval` v0.1
- [ ] Thu: arXiv submission (cs.CL primary, cs.AI secondary)
- [ ] Fri (2026-07-15): **TMLR submission via OpenReview**
- [ ] Fri: log submission in `DECISIONS.md`
- [ ] Fri: tweet thread announcing arXiv preprint + repo
- [ ] **Gate**: submission confirmed; arXiv ID received

**Estimated hours**: 12 (T02) + 8 (survey) = 20

---

## After submission (weeks 10+)

- T02 enters TMLR review cycle (3–5 months)
- Full bandwidth shifts to survey (16 hr/week survey, 4 hr/week T02 response)
- Monitor for reviewer assignment within 2–3 weeks of submission
- Maintain arXiv preprint visibility (cite from survey, share at workshops)

---

## Status check format

At end of each week, append to this file:

```
### Week X status (date)
- Completed: [list]
- Not done: [list]
- Cost so far: $X
- Blockers: [list]
- Next-week priority: [one sentence]
```

---

## Hard kill triggers (re-check weekly)

From `KILL_CRITERIA.md`:
- K1 (scoop): another paper publishes cross-model PBI + harness
- K2 (no effect): pilot shows PBI < 0.02 with overlapping CIs across all judges
- K3 (cost): spend > $1,500 with < 80% complete
- K4 (calendar): no submission by 2026-08-15 (13 weeks)

If any trigger fires, follow the action plan in `KILL_CRITERIA.md` and document
the decision in `DECISIONS.md`.
