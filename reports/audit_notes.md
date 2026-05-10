# Audit notes

Append-only. One section per pipeline run. Captures heuristic decisions, calibration notes, and any user/auditor concerns.

## Schema

```
## YYYY-MM-DD <run_id>
- topics_in: ...
- relevance_threshold: ...
- claude_cli_authed: yes/no
- openai_used: yes/no, calls=N
- known_issues:
  - ...
- decisions_overridden:
  - ...
- next_calibrations_needed:
  - ...
```

## 2026-05-09 baseline-mvp
- topics_in: 10 (data/topics_seed.csv)
- relevance_threshold: 0.20
- claude_cli_authed: no (subprocess returned "Not logged in"; user must run `claude auth login` once)
- openai_used: no (tiebreaker disabled by default)
- known_issues:
  - Papers With Code API returned 0 across all queries; needs endpoint check
  - Crossref-only papers initially had year=0; fixed by extracting from `issued.date-parts`
  - Without LLM panel, every topic capped at LOW confidence; reports labeled PRELIMINARY_HEURISTIC_ONLY
- decisions_overridden: none
- next_calibrations_needed:
  - Confirm relevance threshold against held-out judged papers (manual)
  - TMLR no-APC + indexing (jmlr.org/tmlr; not via API)
  - Employer IP/moonlighting clause (legal interpretation)
  - Public dataset DUAs for any clinical work (legal/contractual)
