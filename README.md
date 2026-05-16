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

# 3) Full pipeline with iterative verification (default profile = blind_citation)
python scripts\10_run_pipeline.py --topics data\topics_seed_balanced.csv --max-rounds 3 --llm-review

# 4) Bias audit (negative-control sentinel + 13-profile rank stability)
python scripts\13_bias_audit.py

# 5) Personal-goal overlay on the neutral baseline (selection aid only)
python scripts\14_personal_overlay.py

# 6) Weekly arXiv scoop watch (alerts on new papers in active topic spaces)
python scripts\15_arxiv_watch.py

# 7) Generate BibTeX for a topic when starting to write a paper
python scripts\16_extract_bibtex.py --topic T02

# 8) SURVEY support — seed corpus from existing topics, then track progress
python scripts\17_survey_corpus.py --seed-from-dedup
python scripts\18_survey_progress.py
```

Key outputs:

- `reports/final_decision_report.md` — master per-topic report
- `reports/BIAS_AUDIT_REPORT.md` — anti-bias audit + negative-control sentinel
- `reports/PERSONAL_OVERLAY_REPORT.md` — safe vs risky personal-goal choices
- `reports/BRIDGE_PUBLICATION_STRATEGY.md` — bridge-paper analysis
- `reports/SCOOP_WATCH.md` — arXiv scoop monitor (kill-signal alerts)
- `data/scores/scores.csv` — evidence-derived scores per topic
- `data/decisions/decisions.csv` — final per-topic decisions
- `reports/llm_review_errors.md` — written only if LLM calls failed
- `reports/audit_notes.md` — append-only run log
- `DECISIONS.md` — append-only commitment log
- `references/<topic>.bib` — BibTeX for paper writing

## Current state (2026-05-12)

The most recent balanced pipeline run (commit `c805933`, 36 topics) produced:
- 6 topics passing `blind_citation_acceptable=True`: B05, B12, T07, T01, B11, T02
- 0 topics meeting the strict GO threshold
- Bridge paper selected: **T02 (position-bias quantification)** — see
  `06_paper_pipeline/T02_position_bias/PROTOCOL.md` for the execution plan.
- Long-term paper queued: **T07 (judge prompt injection)** — see
  `06_paper_pipeline/T07_judge_injection/PRE_EXECUTION_CHECKLIST.md` first.

See `DECISIONS.md` for the running rationale.

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
data/topics_seed_balanced.csv  (or topics_seed.csv)
   ↓
01_generate_queries.py             per-source synonym-expanded queries;
                                   conditional axis injection by target_artifact
   ↓
02_collect_topic_evidence.py       Semantic Scholar, OpenAlex, Crossref, arXiv
                                   (relevance-scored + threshold-filtered dedup)
   ↓
03_collect_extra_evidence.py       GitHub, HuggingFace, Papers With Code, DOAJ
   ↓
04_collect_venue_evidence.py       DOAJ, OpenReview, Crossref journals
   ↓
05_score_topics.py                 18-component scoring under all 13 profiles;
                                   sorts by active profile (default blind_citation)
   ↓
12_detect_existing_work.py         Paper vs artifact overlap distinction;
                                   per-source EW report + summary
   ↓
06_llm_review_topics.py            8 neutral reviewers (default);
                                   --include-personal-goals for niw_eb1a + faang
   ↓
07_compare_reviewers.py            agreement + per-role disagreement
   ↓
08_confidence_gate.py              GO / NARROW / DROP / NEEDS_MORE_EVIDENCE
                                   + blind_citation gate + NC sentinel + EW gate
   ↓ (loop back to 03 if NEEDS_MORE_EVIDENCE and rounds remain)
   ↓
09_generate_final_report.py        reports/final_decision_report.md (with
                                   active profile + 13-profile rank stability
                                   + personal-goal overlay)

Auxiliary (on-demand, not in pipeline loop):
  13_bias_audit.py        anti-bias audit, negative-control sentinel, 13 profiles
  14_personal_overlay.py  selection aid: safe vs risky personal-goal choices
  15_arxiv_watch.py       weekly arXiv scoop monitor with kill-signal alerts
  16_extract_bibtex.py    convert dedup CSV -> references/<topic>.bib
  17_survey_corpus.py     build/maintain LLM-as-Judge survey corpus
                          (data/survey_corpus.csv) — auto-classifies in-scope
                          and section; preserves manual edits on re-run
  18_survey_progress.py   reports/SURVEY_PROGRESS.md — corpus size vs target,
                          section coverage, read-status, draft pages,
                          quality-rubric completion, kill-criteria sign-off
```

`scripts/10_run_pipeline.py` orchestrates the main loop with `--max-rounds`,
`--profile`, and `--include-personal-goals`.

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
python -m pytest scripts\tests\test_pipeline.py -q
```

90 tests covering: query generation (incl. conditional axis injection by target
artifact), deduplication, relevance filtering, scoring rubric monotonicity,
topic-aware NIW/EB-1A/Career variation, artifact-density penalty, confidence-gate
decision rules, final-report warning when LLM did not run, neutral-reviewer panel
defaults, profile system (13 profiles + custom weight overrides), seed keyword
cap, negative-control sentinel, personal-goal-only-weak gating, blind-citation
gate enforcement, bias audit outputs, paper-vs-artifact existing-work detection
(8 tests), arXiv scoop watch helpers (11 tests), and BibTeX extraction (10 tests).

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

---

## Bias-resistance design

The pipeline was redesigned in May 2026 to be academically neutral by default.
See `reports/BIAS_AUDIT_REPORT.md` for the full audit. Highlights:

- **Default scoring profile**: `blind_citation` (citation/novelty/gap-clarity
  driven; all NIW/EB1A/career weights = 0).
- **13 weight profiles** in `config/weight_profiles.yaml`; each topic carries
  scores under all 13. Run `13_bias_audit.py` to see rank stability per topic.
- **8 neutral LLM reviewers** by default; personal-goal reviewers (niw_eb1a,
  career_faang) only included when `--include-personal-goals` is passed.
- **Negative-control sentinel**: 7 deliberately-vague topics seeded into the
  CSV (`is_negative_control=true`); if any rank in the top half under the
  active profile, GO is blocked and the pipeline reports SCORING_LEAK_DETECTED.
- **Paper vs artifact existing-work distinction**: `12_detect_existing_work.py`
  separates peer-reviewed paper overlap from GitHub/HF/PWC artifact overlap;
  GO is only blocked by paper overlap.
- **Personal-goal overlay**: `14_personal_overlay.py` is a selection aid that
  runs AFTER the neutral ranking; it cannot promote a topic that fails
  `blind_citation_acceptable`.
- **Conditional axis-term injection**: `01_generate_queries.py` only injects
  benchmark/evaluation axis terms for benchmark-target topics.
- **Seed keyword cap**: `common/seed_audit.py` flags overrepresented exact
  keywords (>3 across topics) in `reports/seed_bias_warnings.md`.

---

## Active paper projects

| Project | Role | Venue | Submit / Publish | Folder |
|---|---|---|---|---|
| **T02** — Position-bias quantification | **Bridge** (fastest sub→pub, ~3.5 mo) | EMNLP 2026 Workshop (Eval4NLP) | 2026-08-15 / 2026-12 | `06_paper_pipeline/T02_position_bias/` |
| **SURVEY** — *"Judging the Judges"* | **High-citation primary** (target 500+) | TMLR Survey Certification | 2027-02-15 / 2027-08 | `06_paper_pipeline/SURVEY_llm_judge/` |
| **T07** — Judge prompt injection | Companion + Survey §6.3 case study (if executed) | TBD (post blocking-paper read) | TBD | `06_paper_pipeline/T07_judge_injection/` |

Each project folder contains: PROTOCOL, PAPER_OUTLINE / SURVEY_STRUCTURE,
KILL_CRITERIA, and project-specific supporting documents.

**Strategy pivot 2026-05-16**: from a "fast bridge paper" strategy to a
"high-citation survey" strategy. See `reports/HIGH_CITATION_STRATEGY.md` for
the honest probability analysis and venue waterfall. Both strategies coexist
under Option B (parallel execution) — see `DECISIONS.md` 2026-05-16 entries.
