# research-command-center

Private/local research workflow scaffold for high-citation paper production
with NIW / EB-1A and FAANG / career evidence value.

The scaffold is two things at once:

1. A folder layout (16 workflow folders + 20 reusable templates) for managing
   topic discovery, literature review, venue selection, paper drafts,
   reproducibility, peer-review work, citation tracking, and immigration
   evidence.
2. An automated **verification-first** pipeline that scores candidate research
   topics against current public evidence and a multi-reviewer LLM panel,
   then emits a `GO / NARROW / DROP / NEEDS_MORE_EVIDENCE` recommendation per
   topic with traceable evidence.

---

## Quickstart

```powershell
# 1) Scaffold (idempotent)
python scripts\00_setup_repo.py

# 2) One-time auth so the LLM panel can run on your Max plan (no API charges)
claude auth login

# 3) Full pipeline with iterative verification
python scripts\10_run_pipeline.py --max-rounds 3
```

Key outputs:

- `reports/final_decision_report.md` — the master report
- `data/scores/scores.csv` — evidence-derived scores per topic
- `data/decisions/decisions.csv` — final per-topic decisions
- `reports/llm_review_errors.md` — written only if LLM calls failed
- `reports/audit_notes.md` — append-only run log

---

## LLM provider design

This system **does not use the Anthropic API**.

- **Claude reviewers** invoke the local Claude Code CLI (`claude -p ...`) as a
  subprocess. Auth uses your Max-plan OAuth — no API key, no charges.
  Override the binary path with `CLAUDE_CLI_PATH` if needed.
- **OpenAI** is **strict tiebreaker only**:
  - Off by default. Enable with `--use-openai-tiebreaker`.
  - Used only on the top-N topics by Overall score
    (`--tiebreaker-top-n`, default 4).
  - Used only on the two most divisive roles (`brutal_skeptic`,
    `novelty_saturation`).
  - Only invoked when Claude reviewers show no >50% plurality.
  - Hard-bounded by `data/cache/openai_budget.json`
    (default 8 calls per pipeline run; reset with `--reset-openai-budget`).
- All reviewer responses are **cached on disk**
  (`data/cache/llm_cache/`) keyed by (role, packet hash) so reruns and partial
  pipeline replays are free.
- If the Claude CLI is not yet authed, the panel writes prompt files to
  `data/reviews/_inbox/`, an error log to `reports/llm_review_errors.md`,
  and the final report is clearly labelled
  **PRELIMINARY_HEURISTIC_ONLY**.

---

## Pipeline

```
data/topics_seed.csv
   ↓
01_generate_queries.py             per-source synonym-expanded queries
   ↓
02_collect_topic_evidence.py       Semantic Scholar, OpenAlex, Crossref, arXiv
                                   (relevance-scored + threshold-filtered dedup)
   ↓
03_collect_extra_evidence.py       GitHub, HuggingFace, Papers With Code, DOAJ
   ↓
04_collect_venue_evidence.py       DOAJ, OpenReview, Crossref journals
   ↓
05_score_topics.py                 7 evidence-derived signals + topic-aware
                                   NIW / EB-1A / Career + artifact density
   ↓
06_llm_review_topics.py            Claude CLI panel; bounded OpenAI tiebreaker
   ↓
07_compare_reviewers.py            agreement + per-role disagreement
   ↓
08_confidence_gate.py              GO / NARROW / DROP / NEEDS_MORE_EVIDENCE
                                   + completeness + status banner
   ↓ (loop back to 03 if NEEDS_MORE_EVIDENCE and rounds remain)
   ↓
09_generate_final_report.py        reports/final_decision_report.md
```

`scripts/10_run_pipeline.py` orchestrates the loop with `--max-rounds`.

---

## Configuration

Edit `config.yaml`. All thresholds (relevance cutoff, gate rules, density
limits, LLM budgets) are read from there with sane defaults baked in.

---

## Privacy / IP

See `00_admin/ip_safety_rules.md`. Public data only.

Never commit:

- PHI of any kind
- Employer SQL, business logic, internal URLs
- Power BI screenshots, internal architecture diagrams
- Any data you cannot re-derive from public sources

`.gitignore` excludes `.env`, all cache directories, all per-run evidence
artifacts, and logs. The committed repo carries source, templates, seed CSVs,
config, README, and (optionally) the latest `reports/final_decision_report.md`.

---

## Testing

```powershell
python scripts\tests\test_pipeline.py
```

Unit-tested: query generation, deduplication, relevance filtering,
scoring rubric monotonicity, topic-aware NIW/EB-1A/Career variation,
artifact-density penalty, confidence-gate decision rules, final-report
warning when LLM did not run.

---

## Layout

| Folder | Purpose |
|---|---|
| `00_admin/` | goals, IP rules, weekly review log |
| `01_topic_discovery/` | topic universe (75-topic catalog seed) |
| `02_current_verification/` | per-topic verification logs |
| `03_literature_review/` | Zotero exports, extraction sheets |
| `04_topic_scoring/` | scoring rubric + scores.csv |
| `05_venue_selection/` | venue master list and per-venue evals |
| `06_paper_pipeline/` | drafts and outlines |
| `07_experiments/` | configs, runs, results |
| `08_reproducibility/` | env pins, Dockerfile, data provenance |
| `09_public_artifacts/` | release checklists |
| `10_peer_review/` | review opportunities and outputs |
| `11_collaborators/` | outreach tracker |
| `12_citation_tracking/` | citations log |
| `13_immigration_evidence/` | NIW / EB-1A evidence index |
| `14_visibility/` | LinkedIn, blog drafts |
| `15_career_portfolio/` | portfolio plan |
| `templates/` | 20 reusable templates |
| `scripts/` | automation pipeline |
| `data/` | pipeline inputs and intermediate artifacts (mostly gitignored) |
| `reports/` | final reports |
| `logs/` | pipeline logs |

All claims marked **VERIFY** are time-sensitive and must be re-checked
before any commitment of more than 30 days of work.
