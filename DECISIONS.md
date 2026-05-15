# DECISIONS log

Append-only. Every commitment of >1 week of work goes here with date and rationale.

| Date | Decision | Rationale | Topic ID | Reversible? |
|------|----------|-----------|----------|-------------|
| 2026-05-10 | Adopt blind_citation as default scoring profile | Tier-1 bias audit (`reports/BIAS_AUDIT_REPORT.md`) showed personal-goal weights distorted ranking. Neutral profile is the canonical academic-merit baseline; personal-goal overlays are advisory only. | n/a | Yes — change `--profile` arg |
| 2026-05-11 | Run balanced 36-topic neutral pipeline | Replace prior 14-topic biased seed with `data/topics_seed_balanced.csv` (7 NCs, balanced LLM-judge keyword). Gives unbiased candidate pool. | n/a (all) | Yes — re-run with old seed |
| 2026-05-11 | Accept the 6 bc_acceptable topics as the candidate pool | B05, B12, T07, T01, B11, T02 passed `blind_citation_acceptable=True`. No topic gets GO automatically; pool is the basis for further evaluation. | B05, B12, T07, T01, B11, T02 | Yes — re-pool after next pipeline run |
| 2026-05-12 | Select **T02 (position-bias quantification)** as bridge paper | Cleanest EW (0/0 direct); fastest solo execution (3–4 months); directly synergistic with JudgeSense; safest "first peer-reviewed publication." See `reports/BRIDGE_PUBLICATION_STRATEGY.md` and `06_paper_pipeline/T02_position_bias/PROTOCOL.md`. | T02 | Yes — kill criteria in `06_paper_pipeline/T02_position_bias/KILL_CRITERIA.md` |
| 2026-05-12 | Defer T07 execution pending blocking-paper read | T07 has highest NIW/EB1A/career value but the arXiv 2025 "Red Teaming the Mind of the Machine" paper must be cleared first. See `06_paper_pipeline/T07_judge_injection/PRE_EXECUTION_CHECKLIST.md`. | T07 | Yes — proceed once cleared |
| 2026-05-12 | Eliminate B12 from active candidate pool | 29 direct artifacts + multilingual resource barrier make solo execution infeasible in bridge timeframe. Catalogue as long-term collaboration opportunity only. | B12 | Yes — revisit if collaborator surfaces |
| 2026-05-12 | De-prioritise B11 | Wrong research identity (ML systems vs LLM evaluation cluster). Keep available but do not allocate execution effort. | B11 | Yes |
| 2026-05-12 | Add `scripts/15_arxiv_watch.py` for weekly scoop monitoring | T02 + T07 timelines depend on no scoop appearing. Manual checking is unreliable. State-tracked alerts in `reports/SCOOP_WATCH.md`. | T02, T07, T01, B05 | Yes — disable by removing cron entry |
| 2026-05-12 | Submission target for T02: ARR June 2026 → EMNLP 2026 Findings (Dec 2026); fallback TMLR | ARR is free, no-APC, ACL Anthology indexed. EMNLP Findings is a credible NIW/EB1A exhibit. TMLR rolling fallback if cycle slips. | T02 | Yes — switch to TMLR at any time |
