# Code Guardrails

*What this repo does to prevent the class of mistakes that have hit us before.*
*Read this when onboarding, when something feels off, or before any submission.*

---

## The pattern this defends against

I (the AI assistant) generated plausible claims without verification:
- Proposed a title ("Judging the Judges") without checking it exists
- Claimed only 1 LLM-as-Judge survey existed when there are 3
- Claimed ARR June 2026 was a target when the deadline was 30 days past
- Claimed IEEE Access was free when it has a $1,995 APC

The user caught these manually. Code now catches them automatically.

---

## The guardrail stack

There are **five layers** of defence:

### Layer 1 — Authoritative data sources

Every claim that can be verified is verified against a public source:

| Claim type | Verified against |
|---|---|
| Whether a title is novel | Semantic Scholar + arXiv + OpenAlex (`scripts/19_title_check.py`) |
| Whether a venue is free | Hand-maintained registry with 180-day re-verify rule (`scripts/23_venue_verify.py`) |
| Whether a competing paper exists | Weekly arXiv scoop watch (`scripts/15_arxiv_watch.py`) |
| Whether the survey corpus is current | Per-row `last_seen` timestamps (`scripts/17_survey_corpus.py`) |
| Whether T02 spend is within budget | JSONL-log aggregation (`scripts/21_cost_tracker.py`) |

### Layer 2 — Per-script self-defence

Each tool that fetches external data has:
- **Retry with backoff** for API rate limits
- **Multi-source fallback** (e.g., arXiv → OpenAlex when 429s)
- **State preservation** so manual edits aren't lost on re-run
- **Verdict thresholds** so subtle issues don't go undetected

### Layer 3 — Project-state validator (`scripts/20_validate_state.py`)

Meta-check that runs over the whole project:

| Check | What it catches |
|---|---|
| `required_scripts_exist` | Files referenced in README/pipeline missing from disk |
| `paper_projects_complete` | Active paper missing PROTOCOL / KILL_CRITERIA |
| `titles_match_proposed` | Title in PROTOCOL not listed in `data/proposed_titles.txt` (means it wasn't title-checked) |
| `no_past_deadline_claims` | Documents reference deadlines already past (e.g., "submit by 2026-06-15" when today is 2026-09-01) |
| `survey_corpus_freshness` | Survey corpus hasn't been refreshed in 30+ days |
| `title_check_freshness` | Title check hasn't been re-run in 30+ days |
| `scoop_watch_freshness` | Scoop watch hasn't been run in 7+ days |
| `scoop_watch_covers_active_topics` | A project exists but has no scoop-watch query |
| `config_files_parse` | YAML/JSON config files have syntax errors |
| `decisions_log_format` | DECISIONS.md missing canonical header or entries |
| `no_deprecated_venue_claims` | Documents claim "free" for known-paid venues (IEEE Access, PLOS ONE, Frontiers, MDPI) |

Run: `python scripts/20_validate_state.py`
Exit codes: 0 = all pass, 1 = any FAIL, 2 = only WARN.

### Layer 4 — Pre-submission preflight (`scripts/22_preflight.py`)

Runs the full check stack before any paper submission:

| Gate | Source |
|---|---|
| `state_validator` | Layer 3 must pass (or only WARN) |
| `tests_pass` | `pytest scripts/tests/test_pipeline.py` must be green |
| `title_clear` | The exact paper title must have CLEAR verdict in `TITLE_CHECK.md` |
| `scoop_no_kill` | No kill-signal papers in `SCOOP_WATCH.md` |
| `protocol_files` | PROTOCOL + KILL_CRITERIA present for the project |
| `reproducibility_snapshot` | `data/_snapshots/` has at least one snapshot file |
| `references_bib` | `references/<topic>.bib` exists (if applicable) |
| `cost_within_budget` | API spend within budget (if applicable) |

Run: `python scripts/22_preflight.py --project <P> --title "<T>"`
Exit codes: 0 = cleared, 1 = blocked, 2 = warn only.

### Layer 5 — DECISIONS.md (the audit trail)

Every commitment of >1 week is logged with: date, decision, rationale, reversibility.
This is append-only. If a decision is reversed, append a new entry — never edit history.

The audit trail catches a different class of error: not "wrong now" but "we forgot why we chose this." It's the user-facing version of the validator.

---

## Failure modes the guardrails defend against

| # | Failure mode | Defence | Status |
|---|---|---|---|
| 1 | AI proposes title without verification | Layer 1: `19_title_check.py` runs on `proposed_titles.txt` | ✅ |
| 2 | Claimed gap in literature without evidence | Layer 1: multi-source corpus seeding | ✅ |
| 3 | Documents reference past deadlines | Layer 3: `check_no_past_deadline_claims` | ✅ |
| 4 | Claimed paid venue is free | Layer 3: `check_no_deprecated_venue_claims` + Layer 1: `venue_registry.json` | ✅ |
| 5 | arXiv rate limiting kills the watch | Layer 2: retry+backoff + OpenAlex fallback | ✅ |
| 6 | Field-name mismatch in pipeline data | Layer 2: per-script schema falls back through alternate field names | ✅ |
| 7 | Strategy drift across documents | Layer 3: `titles_match_proposed`, `scoop_watch_covers_active_topics` | ✅ |
| 8 | Submit without re-running title check | Layer 4: preflight gate `title_clear` | ✅ |
| 9 | Submit without re-running scoop watch | Layer 4: preflight gate `scoop_no_kill` | ✅ |
| 10 | API costs exceed budget silently | Layer 1: `21_cost_tracker.py`; Layer 4: preflight gate | ✅ |
| 11 | Survey corpus goes stale | Layer 2 + 3: staleness warning in script + validator | ✅ |
| 12 | Test suite broken at submission | Layer 4: preflight gate `tests_pass` | ✅ |
| 13 | Documents reference deprecated venues | Layer 3: `check_no_deprecated_venue_claims` | ✅ |
| 14 | Companion repo not public at submission | Layer 4: preflight gate (manual check item) | ⚠️ partial |
| 15 | Single arXiv query misses competitors | Layer 2: multi-source fallback | ✅ |
| 16 | Venue claims (APC, review time) become outdated | Layer 1: `23_venue_verify.py` enforces 180-day re-verify | ✅ |

---

## How to use the guardrails

### Day-to-day (weekly)

```powershell
python scripts\15_arxiv_watch.py            # weekly scoop watch
python scripts\20_validate_state.py          # weekly state check
python scripts\18_survey_progress.py         # survey progress
```

### When working on a paper

```powershell
# After changing the title:
python scripts\19_title_check.py --titles-file data\proposed_titles.txt

# After adding a venue to consider:
# 1. Add it to data/venue_registry.json with last_verified_iso = today
python scripts\23_venue_verify.py

# During experiments (T02):
python scripts\21_cost_tracker.py
```

### Before submission

```powershell
# MUST pass these:
python scripts\22_preflight.py --project T02_position_bias --title "Position Bias in LLM Judges: A Cross-Model Quantification"
python scripts\22_preflight.py --project SURVEY_llm_judge --title "Trustworthy LLM-as-a-Judge: A Comprehensive Survey of Methods, Failure Modes, and Defences"
```

If preflight exits 1, **do not submit**. If it exits 2, read the warnings and decide.

---

## Onboarding for a future operator

If you (the user, or someone else) returns to this repo after months away:

1. Read `README.md` for orientation
2. Read `DECISIONS.md` for the why
3. Run `python scripts/20_validate_state.py` to see what's stale
4. Read `reports/STATE_VALIDATION.md` and fix anything FAIL
5. Read `reports/SCOOP_WATCH.md` for any new kill signals
6. Read `NEXT_90_DAYS.md` for current action items

If something seems out of sync between documents — that's a strategy-drift bug.
Add a check to `scripts/20_validate_state.py` that would have caught it.

---

## Limits — what the guardrails do NOT catch

Be honest about the boundary:

- **Quality of the actual research** (the experiments, the analysis, the writing) — no code can validate this. Human judgment + external review.
- **Whether the strategy is right** — code can verify consistency, not correctness. The strategy choice (Option B parallel etc.) is a human decision.
- **Whether claims about citation potential are accurate** — these are probabilistic; we can verify they're labelled as estimates.
- **Whether reviewers will accept the paper** — out of scope.
- **Whether external events invalidate the plan** (e.g., NeurIPS rejects JudgeSense) — code can flag, but human decides what to do.
- **Whether the AI itself (me) is correct on novel claims** — that's why this entire system exists.

---

## How to add a new guardrail

Saw a class of mistake the system didn't catch? Add a guardrail:

1. **For a per-script issue**: Add a unit test in `scripts/tests/test_pipeline.py` and a runtime check in the relevant script.
2. **For a project-state issue**: Add a check function to `scripts/20_validate_state.py` and add it to the `CHECKS` list.
3. **For a pre-submission gotcha**: Add a gate function to `scripts/22_preflight.py`.
4. **For a venue claim**: Update `data/venue_registry.json` and `scripts/23_venue_verify.py`.

Document the new guardrail in this file's table.
