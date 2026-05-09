# research-command-center

Private/local research workflow scaffold for high-citation paper production with NIW/EB-1A and FAANG/career evidence value.

## Quickstart

```powershell
python scripts/00_setup_repo.py        # idempotent scaffold
claude auth login                       # one-time, so the LLM panel can run on Max plan (no API charges)
python scripts/10_run_pipeline.py      # end-to-end automated verification
```

## LLM provider design

This system **does not use the Anthropic API**.

- **Claude reviewers** are run by invoking the local Claude Code CLI (`claude -p ...`) as a subprocess. Auth uses your Max-plan OAuth — no API key, no charges. Override the binary path with `CLAUDE_CLI_PATH` if needed.
- **OpenAI** is **strict tiebreaker only**:
  - Off by default. Enable with `--use-openai-tiebreaker`.
  - Used only on the top-N topics by Overall score (`--tiebreaker-top-n`, default 4).
  - Used only on the two most divisive roles (`brutal_skeptic`, `novelty_saturation`).
  - Only invoked when Claude reviewers show no >50% plurality.
  - Hard-bounded by `data/cache/openai_budget.json` (default 8 calls per pipeline run; reset with `--reset-openai-budget`).
- All reviewer responses are **cached on disk** (`data/cache/llm_cache/`) keyed by (role, packet hash) so reruns and partial pipeline replays are free.
- If the Claude CLI is not yet authed, the panel writes prompt files to `data/reviews/_inbox/` so you can run `claude auth login` and rerun, or paste them into another Claude / ChatGPT session and save the JSON reply alongside.

## Pipeline

```
data/topics_seed.csv
  -> 01_generate_queries.py
  -> 02_collect_topic_evidence.py    (Semantic Scholar, OpenAlex, Crossref, arXiv)
  -> 03_collect_extra_evidence.py    (GitHub, HuggingFace, Papers With Code, DOAJ)
  -> 04_collect_venue_evidence.py    (DOAJ, OpenReview, Crossref journals)
  -> 05_score_topics.py              (7 evidence-derived signals -> rubric A..X -> Overall)
  -> 06_llm_review_topics.py         (Claude CLI panel; OpenAI tiebreaker if enabled)
  -> 07_compare_reviewers.py
  -> 08_confidence_gate.py           (GO / NARROW / DROP / NEEDS_MORE_EVIDENCE)
  -> [loop back to 03 if NEEDS_MORE_EVIDENCE and rounds remain]
  -> 09_generate_final_report.py     (reports/final_decision_report.md)
```

`scripts/10_run_pipeline.py` orchestrates the loop with `--max-rounds`.

## Privacy / IP

See `00_admin/ip_safety_rules.md`. Public data only. Never commit PHI, employer SQL, internal URLs, screenshots, or proprietary logic.

## Testing

```powershell
python scripts/tests/test_pipeline.py
```

Covers: query generation, deduplication, scoring rubric monotonicity, confidence-gate decision rules, report generation.

## Layout

- `00_admin/` — goals, IP rules, weekly review log
- `01_topic_discovery/` — topic universe (75-topic catalog seed)
- `02_current_verification/` — per-topic verification logs (auto-populated)
- `03_literature_review/` — Zotero exports, extraction sheets, coding schemes
- `04_topic_scoring/` — scoring rubric + scores.csv
- `05_venue_selection/` — venue master list and per-venue evaluations
- `06_paper_pipeline/` — drafts and outlines
- `07_experiments/` — configs, runs, results, notebooks
- `08_reproducibility/` — env pins, Dockerfile, data provenance
- `09_public_artifacts/` — release checklists
- `10_peer_review/` — review opportunities and outputs
- `11_collaborators/` — outreach tracker
- `12_citation_tracking/` — citations log
- `13_immigration_evidence/` — NIW/EB-1A evidence index
- `14_visibility/` — LinkedIn, blog drafts
- `15_career_portfolio/` — portfolio plan
- `templates/` — 20 reusable templates
- `scripts/` — automation pipeline (10 stages + common utilities)
- `scripts/tests/` — unit tests
- `data/` — pipeline inputs and intermediate artifacts (gitignored: cache, secrets)
- `reports/` — final reports
- `logs/` — pipeline logs

All claims marked **VERIFY** are time-sensitive and must be re-checked before any commitment of >30 days work.
