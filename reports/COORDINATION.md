# Bridge × Survey — Parallel Execution Coordination

*Source*: user reconfirmation 2026-05-16 — "I actually need both quick bridge but
good paper at good and free venue (to get count) fast, and then this 500+ citation
paper at free venue."
*Strategy*: Option B (parallel) from `reports/HIGH_CITATION_STRATEGY.md` §4.
*Logged*: `DECISIONS.md` 2026-05-16 entries.

This document is the single page that shows how T02 (bridge) and the LLM-as-Judge
survey (high-citation) run together, what hits in what month, and how the bridge
work feeds the survey.

---

## Two papers, two roles, one career

| | T02 (BRIDGE) | SURVEY (PRIMARY) |
|---|---|---|
| **Role** | Publication-count starter; first-ever peer-reviewed | The big citation play (target 500+) |
| **Type** | Empirical paper, 8 pages (workshop format) | Comprehensive survey, ~70 pages |
| **Title** | *Position Bias in LLM Judges: A Cross-Model Quantification* | *"Trustworthy LLM-as-a-Judge: A Comprehensive Survey of Methods, Failure Modes, and Defences"* |
| **Primary venue** | **EMNLP 2026 Workshop** (Eval4NLP) | **TMLR** (Survey Certification) |
| **Backup venues** | NeurIPS 2026 Safety Workshop → TMLR → ICLR 2027 Workshop | ACM Computing Surveys → JMLR → CL journal |
| **Sub→Pub time** | ~3.5 months | 3–6 months |
| **Cost ($)** | ~$1,500 API budget | <$200 (mostly reading time) |
| **Calendar effort** | 13 weeks active | 10–12 months |
| **Cognitive mode** | Experiments + analysis + writing | Reading + synthesis + writing |
| **USCIS role** | Publication #1 (basic peer-reviewed evidence) | Strongest single EB-1A exhibit (criterion vi) |
| **APC** | $0 | $0 |
| **Citation ceiling** | 30–80 | 500–1500 (target 500+) |

---

## Critical insight: the bridge feeds the survey

T02's empirical results become **Survey §6.1 Case Study: Position bias across
5 frontier judges** automatically. This means:

- T02 is not "wasted effort if the survey gets accepted first" — it is the survey's
  empirical backbone.
- T02 published → cite from the survey ("see [Author 2026] for empirical evidence
  of position bias magnitude").
- Survey published → cite T02 from the survey's abstract and introduction.
- Reciprocal citations help both papers' citation counts.

The same applies to T07 (→ Survey §6.3) and T01 (→ Survey §6.2) if executed.

---

## Calendar (May 2026 → December 2027)

```
                MAY  JUN  JUL  AUG  SEP  OCT  NOV  DEC  JAN  FEB  MAR  APR  MAY  JUN  JUL  AUG  SEP  OCT  NOV  DEC
                2026                                    2027                                    2027

T02 BRIDGE
  scaffold       ##
  pilot              #
  data run             ###
  analysis                ##
  draft                      ##
  TMLR submit                  *                                                  (* = arXiv preprint same day)
  reviews                        ###
  decision                            *
  publish                                 *

SURVEY
  lit collect    #################
  taxonomy                ###
  draft 1+2                       ####
  draft 3+4                              ####
  draft 5+6                                       ####
  draft v1                                                #
  internal rev                                                ##
  draft v2                                                        ##
  TMLR submit                                                           *
  arXiv preprint                                                        *
  reviews                                                                  ####
  publish                                                                              *

OTHER
  T07 clear            #
  T07 arXiv pre         *
  JudgeSense (NeurIPS) external timeline — track but don't depend on
```

**Key milestones**:
- 2026-06-05: T02 pilot complete
- 2026-08-15: T02 paper submitted to EMNLP 2026 Workshop + arXiv preprint
- 2026-10-15: T02 workshop notification
- 2026-12-10: T02 published at EMNLP 2026 (publication #1)
- 2027-02-15: Survey submitted to TMLR Survey Certification + arXiv preprint
- 2027-08-15: Survey published at TMLR (publication #2; the citation engine)

---

## Weekly time budget (suggested)

Total: ~20 hours/week of research time.

| Week phase | T02 hours | Survey hours | Notes |
|---|---|---|---|
| Weeks 1–2 (now) | 12 | 8 | Bridge scaffold has priority; survey starts with reading |
| Weeks 3–6 (T02 data) | 14 | 6 | T02 in execution; survey progresses on reading only |
| Weeks 7–9 (T02 draft) | 10 | 10 | Switching modes daily prevents fatigue |
| Weeks 10–11 (T02 submit) | 12 | 8 | Final push for T02 |
| Weeks 12+ (T02 in review) | 4 | 16 | T02 done; full focus shifts to survey |

If bandwidth drops below 15 hr/week: pause survey reading, keep T02 on track. Survey
can absorb a 1-month pause without disaster; T02 cannot miss its TMLR submission window
without slipping publication to mid-2027.

---

## Three-month sprint plan (May 16 – Aug 16, 2026)

Aligned with `NEXT_90_DAYS.md`. By Aug 16 you should have:

| Goal | Source of truth |
|---|---|
| T02 submitted to TMLR + arXiv preprint posted | `06_paper_pipeline/T02_position_bias/PROTOCOL.md` (updated timeline) |
| Survey corpus ≥ 150 in-scope papers | `data/survey_corpus.csv` |
| Survey draft §1 + §2 + §3 (~25 pages) | `06_paper_pipeline/SURVEY_llm_judge/drafts/` |
| T07 blocking-paper decision logged | `06_paper_pipeline/T07_judge_injection/BLOCKING_PAPER_NOTES.md` |
| arXiv scoop watch running (no kill signals) | `reports/SCOOP_WATCH.md` |

---

## Decision rules during execution

### If T02 falls behind (e.g., data collection delayed past July 5)
- Drop T-Code task → reduce cohort to 2 tasks × 5 judges × 4 conditions × 200 items = 8,000 calls
- Submit reduced-scope T02 to TMLR by July 31
- Document scope reduction in T02 CHANGES.md

### If survey corpus grows below target (e.g., < 100 in-scope by month 1)
- Drop survey scope to "LLM-as-Judge: Failure Modes and Defences" (smaller paper, ~40 pages)
- Re-evaluate TMLR vs ACM CS — smaller paper better fits TMLR

### If both fall behind in same month
- Stop survey reading immediately
- Focus 100% on T02 until submitted
- Resume survey reading after T02 submission

### If a scoop appears on T02 (position bias quantification)
- See `06_paper_pipeline/T02_position_bias/KILL_CRITERIA.md` K1
- If scoop has reusable harness → pivot T02 to mitigation comparison (defences only)
- Survey is unaffected; T02 results become §6.1 case study regardless

### If a scoop appears on the survey (competing comprehensive survey at TMLR/JMLR/ACM CS)
- See `06_paper_pipeline/SURVEY_llm_judge/KILL_CRITERIA.md` K1
- Pivot survey to differentiated angle (e.g., security focus, reproducibility focus)
- T02 is unaffected; continues to TMLR as standalone

---

## Status at a glance

After each week, refresh status:

```powershell
python scripts\18_survey_progress.py     # survey
python scripts\15_arxiv_watch.py         # scoop watch
```

Then update T02 progress manually in `06_paper_pipeline/T02_position_bias/STATUS.md`
(create this file if it doesn't exist; mirror the format of the survey progress report).

---

## Why this coordination matters

The temptation when running two projects in parallel is to drift between them
without finishing either. The discipline is:

1. **T02 has a hard deadline** (TMLR July 15 self-target). Survey does not.
   When in doubt, T02 wins time slots.
2. **Survey reading compounds**. Skipping reading in week 3 means working harder
   in week 12.
3. **Cognitive modes alternate**. Don't try to switch every hour — alternate by
   day or by half-day to maintain depth.
4. **One submission at a time** in the same week.

---

## Files this coordination references

- `reports/HIGH_CITATION_STRATEGY.md` — the strategic analysis
- `reports/BRIDGE_PUBLICATION_STRATEGY.md` — the bridge analysis
- `06_paper_pipeline/T02_position_bias/PROTOCOL.md` — bridge execution
- `06_paper_pipeline/SURVEY_llm_judge/PROTOCOL.md` — survey execution
- `NEXT_90_DAYS.md` — quarter sprint plan
- `DECISIONS.md` — append-only commitment log
