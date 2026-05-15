# Next 30 Days

*Generated 2026-05-12 from the bridge publication strategy.*
*Update or replace at any time — this is a one-page action sheet, not a contract.*

---

## This week (May 12–18, 2026)

### Day 1 — read the strategy
- [ ] Read `reports/BRIDGE_PUBLICATION_STRATEGY.md` (37 KB; one sitting)
- [ ] Read `06_paper_pipeline/T02_position_bias/PROTOCOL.md`
- [ ] Read `06_paper_pipeline/T02_position_bias/KILL_CRITERIA.md`
- [ ] If anything looks wrong, document the disagreement in `DECISIONS.md`

### Day 2 — sign-off + setup
- [ ] Sign off on T02 PROTOCOL §13 (or revise)
- [ ] Run `python scripts/15_arxiv_watch.py --bootstrap` once arXiv is not throttled
- [ ] Confirm `references/T02.bib` looks reasonable as a starting bibliography

### Days 3–5 — T07 blocking-paper read
- [ ] Open `06_paper_pipeline/T07_judge_injection/PRE_EXECUTION_CHECKLIST.md`
- [ ] Find and read "Red Teaming the Mind of the Machine" (arXiv 2025)
- [ ] Write `BLOCKING_PAPER_NOTES.md` — proceed / pivot / kill?
- [ ] If proceed: write `DIFFERENTIATOR.md` and post `ARXIV_PREPRINT_STUB.md` to arXiv within 14 days

### Day 6–7 — T02 lit review
- [ ] Read Wang et al. 2023 "Large Language Models are not Robust Multiple Choice Selectors"
- [ ] Read Zheng et al. 2023 "Judging LLM-as-a-Judge with MT-Bench"
- [ ] Read top 3 entries from `references/T02.bib`
- [ ] Update T02 PROTOCOL §7 differentiator if reading reveals new context

---

## Next 2 weeks (May 19–June 1, 2026)

### Code scaffold
- [ ] Create `judge-bias-eval` repo on GitHub (private until first release)
- [ ] Copy structure from `06_paper_pipeline/T02_position_bias/CODE_SCAFFOLD.md`
- [ ] Implement 4 of 5 `clients/*` modules (skip Mistral if no API key yet)
- [ ] Implement `judge.py`, `conditions.py`, `pbi.py` (testable in isolation)

### Pilot data
- [ ] Acquire OpenAI + Anthropic API keys (or confirm existing keys have budget)
- [ ] Load 50 items from one task (e.g., CNN/DailyMail validation set)
- [ ] Run pilot: 50 items × 2 judges × 1 task = 100 calls
- [ ] Manually inspect 10 outputs

### Scoop watch
- [ ] Bootstrap arXiv watch successfully (retry off-peak hours)
- [ ] Schedule weekly run (Windows Task Scheduler):
  ```
  schtasks /create /tn "ScoopWatch" /tr "python C:\path\to\scripts\15_arxiv_watch.py" /sc weekly /d MON /st 09:00
  ```

---

## Days 30 (June 12, 2026)

By end of month, you should have:

- [ ] T02 pilot complete; PBI is or is not measurable
- [ ] T07 blocking paper read; decision logged
- [ ] If proceeding T07: arXiv preprint posted (priority claim)
- [ ] Decision in `DECISIONS.md` whether to proceed full-grid on T02
- [ ] Updated weekly milestone status in T02 KILL_CRITERIA §sign-off

---

## What you should NOT do this month

- **Do not start writing the T02 paper** until pilot data is in. Writing
  before data invites confirmation bias.
- **Do not start T01 or B05 work** — they are queued, not scheduled. Focus.
- **Do not respond to NeurIPS / ACM / clinical-paper revisions** by deferring
  T02. JudgeSense and the survey are slow by design; T02 needs continuous progress.
- **Do not change the scoring profile** mid-stream. The bridge decision
  was made under `blind_citation`; changing it invalidates the rationale.

---

## When you're stuck

1. Re-read `06_paper_pipeline/T02_position_bias/KILL_CRITERIA.md`. Are you
   actually blocked or just procrastinating?
2. Re-run the pipeline if the underlying data is older than 60 days.
3. Update `DECISIONS.md` with what changed and why.
4. Run `python scripts/15_arxiv_watch.py` — sometimes the answer is "scoop happened, pivot."

---

## Definition of done for this 30-day window

| Goal | Measure |
|---|---|
| T02 pilot complete | 50+ judge calls executed, PBI estimated |
| T07 unblocked | Read decision documented in BLOCKING_PAPER_NOTES.md |
| Code scaffold | At least `clients/`, `judge.py`, `pbi.py` working with tests |
| arXiv watch active | Bootstrap succeeded; weekly schedule set |
| Bibliography ready | `references/T02.bib` exists and is complete |

If 4 of 5 are done by day 30: on track.
If fewer than 3: re-read KILL_CRITERIA and decide whether to slow other commitments
or pivot.
