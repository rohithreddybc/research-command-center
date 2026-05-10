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

## 2026-05-10 full-review-complete-1
- topics_in: 10 (data/topics_seed.csv)
- relevance_threshold: 0.20
- claude_cli_authed: yes (Max plan, claude.ai OAuth)
- openai_used: no (tiebreaker disabled; Claude plurality unanimous on NARROW)
- llm_calls: 80 (8 reviewers × 10 topics) — all completed, 0 errors
- aggregate plurality: 10/10 NARROW
- decisions_overridden: none
- known_issues:
  - Papers With Code API returned 0 across queries (endpoint format)
  - 07_compare_reviewers picked up `_inbox` directory as a topic id (cosmetic)
  - relevance_purity sits at 0.25 for most topics: too many partial-keyword matches (e.g., "robustness" in railway/IoT papers leaking into T04)
  - GO conditions (`relevance_purity >= 0.4`, `artifact >= 3`) not met by any topic; no topic promoted to GO even with full LLM agreement on plurality
- reviewer notes (T04 brutal_skeptic, score 2 / DROP HIGH):
  "75% of retrieved papers are about unrelated robustness topics (philosophy, railways, IoT, superconductors). This suggests the research area either does not exist as a unified concept OR the topic is so poorly defined that literature search cannot identify real work."
- next_calibrations_needed:
  - Tighten per-topic synonyms in `topics_seed_full_75.csv` to lift relevance purity above 0.4
  - Bump `relevance_min: 0.30` in config.yaml and re-run 02; expect kept-paper count to drop and purity to rise
  - Per-topic narrowing pass before promoting any to GO (e.g., T04 → "clinical-judge candidate-side prompt-template benchmark", T07 → "clinical-judge prompt-injection robustness")
  - TMLR no-APC + indexing (jmlr.org/tmlr; manual, HTML)
  - Employer IP / moonlighting clause (legal)
  - Per-dataset DUA (legal)

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
