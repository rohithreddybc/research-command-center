# Project State Validation Report

*Generated: 2026-05-16T06:12:49Z*
*Source: `scripts/20_validate_state.py`*

**Summary**: 11 PASS · 0 FAIL · 1 WARN · 0 SKIP

ℹ️ Warnings present — recommended to fix but not blocking.

## Per-check results

| Status | Check | Message |
|---|---|---|
| ✅ PASS | `required_scripts_exist` | All 21 pipeline scripts present |
| ✅ PASS | `paper_projects_complete` | All paper projects under 06_paper_pipeline/ have appropriate files for their phase |
| ✅ PASS | `titles_match_proposed` | All 3 PROTOCOL titles are listed in data/proposed_titles.txt |
| ✅ PASS | `no_past_deadline_claims` | No past-deadline submission claims found |
| ✅ PASS | `survey_corpus_freshness` | Survey corpus most recently refreshed 0 days ago (within 30-day window) |
| ✅ PASS | `title_check_freshness` | Title check is 0 days old (within 30-day window) |
| ✅ PASS | `scoop_watch_freshness` | Scoop watch is 1 days old (within 7-day window) |
| ✅ PASS | `scoop_watch_covers_topics` | All 3 active projects have scoop-watch queries |
| ✅ PASS | `config_files_parse` | All 4 config files parse cleanly |
| ✅ PASS | `decisions_log_format` | DECISIONS.md has canonical header and 34 entries |
| ⚠️ WARN | `no_deprecated_venue_claims` | 3 document(s) make unverified venue claims |
| ✅ PASS | `test_suite_files` | Test suite file present |

## Details for non-passing checks

### ⚠️ no_deprecated_venue_claims (WARN)

**Message**: 3 document(s) make unverified venue claims

**Fix**: Update the affected documents

**Details**:
- reports\CODE_GUARDRAILS.md: claim that IEEE Access is free (IEEE Access charges $1,995 APC — never free)
- reports\STATE_VALIDATION.md: claim that IEEE Access is free (IEEE Access charges $1,995 APC — never free)
- 06_paper_pipeline\SURVEY_llm_judge\VENUE_ANALYSIS.md: claim that IEEE Access is free (IEEE Access charges $1,995 APC — never free)

