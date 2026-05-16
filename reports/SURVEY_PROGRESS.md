# Survey Progress Report — LLM-as-Judge

*Generated: 2026-05-16T04:51:23Z*
*Source: `scripts/18_survey_progress.py`*
*Project: `06_paper_pipeline/SURVEY_llm_judge/`*

## 1. Headline

- Corpus size: **273** papers
- In scope (yes): **43**
- Deeply read: **0**
- Draft pages (total across sections): **0.0** / target 67.5
- Quality rubric: **0/82** items checked

## 2. Corpus targets

| Target | Required | Current | Progress |
|---|---|---|---|
| month_1_indexed | 150 | 43 | `[======              ]` 28% |
| month_1_stretch | 200 | 43 | `[====                ]` 21% |
| month_6_deeply_read | 150 | 0 | `[                    ]` 0% |
| submission_cited | 150 | 43 | `[======              ]` 28% |

## 3. Corpus composition

### 3.1 By in-scope label

| Label | Count |
|---|---|
| yes | 43 |
| partial | 12 |
| no | 218 |

### 3.2 By survey section (auto-classified)

| Section | Count |
|---|---|
| 3_methods | 36 |
| 4_failure_modes | 56 |
| 5_defences | 19 |
| 6_empirical | 42 |
| 7_evaluation | 1 |
| 8_open_problems | 4 |
| UNCLASSIFIED | 115 |

### 3.3 By read status

| Status | Count |
|---|---|
| unread | 273 |
| skimmed | 0 |
| read | 0 |
| deep | 0 |

### 3.4 Failure-mode coverage

| Failure mode | Papers tagged |
|---|---|
| calibration | 19 |
| position_bias | 10 |
| prompt_injection | 21 |
| self_preference | 6 |

### 3.5 Artifact availability

- Papers with code: **0** / 273
- Papers with dataset: **0** / 273

## 4. Draft sections

| Section | Target pages | Drafted pages | Words | Progress | File |
|---|---|---|---|---|---|
| 1_introduction | 5 | 0.0 | 0 | `[                    ]` 0% | `(missing)` |
| 2_foundations | 7 | 0.0 | 0 | `[                    ]` 0% | `(missing)` |
| 3_methods | 10 | 0.0 | 0 | `[                    ]` 0% | `(missing)` |
| 4_failure_modes | 12 | 0.0 | 0 | `[                    ]` 0% | `(missing)` |
| 5_defences | 9 | 0.0 | 0 | `[                    ]` 0% | `(missing)` |
| 6_empirical | 9 | 0.0 | 0 | `[                    ]` 0% | `(missing)` |
| 7_evaluation | 5 | 0.0 | 0 | `[                    ]` 0% | `(missing)` |
| 8_open_problems | 5 | 0.0 | 0 | `[                    ]` 0% | `(missing)` |
| 9_discussion | 4 | 0.0 | 0 | `[                    ]` 0% | `(missing)` |
| 10_conclusion | 1.5 | 0.0 | 0 | `[                    ]` 0% | `(missing)` |

## 5. Quality rubric (60-item)

**0 / 82 (0%)** items checked in QUALITY_RUBRIC.md

`[                                        ]`

## 6. KILL_CRITERIA sign-off

| Checkpoint | Date | K1 | K2 | K3 | K4 | Action |
|---|---|---|---|---|---|---|
| Month 1 | TBD |  |  |  |  |  |
| Month 3 | TBD |  |  |  |  |  |
| Month 6 | TBD |  |  |  |  |  |
| Month 9 | TBD |  |  |  |  |  |
| Month 12 | TBD |  |  |  |  |  |
| Month 15 (post TMLR decision) | TBD |  |  |  |  |  |

---

## Suggested next actions

- Corpus is below month-1 target — add 107 more in-scope papers via `python scripts/17_survey_corpus.py --fetch-arxiv`
- 115 papers are UNCLASSIFIED — hand-edit section assignment in `data/survey_corpus.csv`
- Reading is behind the corpus — read 10 priority (Tier 1) papers this week
- All sections empty — begin writing §1 Introduction (5 pages target)
- Quality rubric < 30% — review `06_paper_pipeline/SURVEY_llm_judge/QUALITY_RUBRIC.md`

