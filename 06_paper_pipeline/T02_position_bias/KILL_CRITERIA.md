# T02 — Kill Criteria

*Based on `templates/17_kill_criteria.md`*
*Defined BEFORE execution starts. Re-read at every weekly checkpoint.*

The point of explicit kill criteria is to prevent sunk-cost continuation.
If any of the conditions below trigger, stop execution and reassess.
Document the reassessment in `06_paper_pipeline/T02_position_bias/CHANGES.md`.

---

## Hard kills (stop and pivot)

### K1: Scoop appears with reusable harness
**Trigger**: A paper appears on arXiv or in any peer-reviewed venue that:
- (a) Provides a cross-model PBI quantification across 3+ judges, AND
- (b) Releases a reusable open-source evaluation harness, AND
- (c) Was posted before our arXiv preprint.

**Detection**: `scripts/15_arxiv_watch.py` runs weekly; manual check at every
weekly milestone in PROTOCOL.md §8.

**Action**:
1. Read the scoop paper in full within 48 hours.
2. Identify the unique angle our paper still has (different mitigations,
   different task families, different judge models).
3. If no unique angle remains: **kill T02**, redirect effort to T07 or T01.
4. If a defensible angle remains: pivot scope, document in CHANGES.md.

### K2: Pilot shows no measurable bias
**Trigger**: After week-3 pilot (50 items × 2 judges × 1 task), all PBI values
are below 0.02 with 95% CIs that include 0.

**Action**:
1. Try harder tasks (longer responses, more ambiguous quality).
2. Try smaller judges (Llama-8B, Mistral-7B) where bias is expected to be larger.
3. If still PBI < 0.02 across all conditions: the finding is "judges have minimal
   position bias on standard tasks" — still publishable as a negative result at
   TMLR or Negative Results workshop, but reframe paper.
4. If even the reframed version is too weak: **kill T02**, switch to T07.

### K3: Cost overrun
**Trigger**: API spend exceeds $1,500 with less than 80% of grid completed.

**Action**:
1. Cap remaining cohorts at smaller N (e.g., 100 items per task).
2. Drop one model (lowest-priority: Mistral-Large-2).
3. Drop one task (lowest-priority: T-Code if pairwise tasks already show effect).
4. Hard cap at $2,000. If we hit $2,000: **kill T02**, write up partial results.

### K4: Calendar overrun
**Trigger**: 6 months elapsed since week 1 with no submission to any venue.

**Action**:
1. Submit whatever exists to TMLR (continuous, no deadline).
2. If draft is incomplete: **kill T02**, switch to T07 if Red Teaming paper
   has been cleared.

---

## Soft signals (raise concerns, do not auto-kill)

### S1: Single judge shows bias, others do not
**Detection**: After week 7 analysis, only 1 of 5 judges shows PBI > 0.05.

**Response**: Reframe as a single-judge case study, broaden discussion
of why judge family matters. Still publishable.

### S2: Reviewer feedback is harsh in internal review (week 12)
**Response**: Address the feedback, do not kill. The whole point of internal
review is to catch problems before peer review.

### S3: ARR rejects
**Response**: Do not kill. Submit to TMLR or next ARR cycle. ARR rejections
are common and not project-ending.

### S4: One model's API becomes unavailable mid-run
**Response**: Document, drop that model from the cohort, note in limitations.
Do not kill.

---

## Continuation criteria (must hold at every weekly checkpoint)

- Estimated time-to-submission ≤ 6 months
- Estimated total cost ≤ $1,500
- No K1–K4 trigger
- Author bandwidth available (≥10 hours/week)
- No urgent JudgeSense / survey / clinical-paper revision request blocking work

---

## Red-team self-check (do once, week 1)

Before writing any code, answer in `CHANGES.md`:

1. **Is the differentiator paragraph (PROTOCOL.md §7) genuinely unique, or am I
   convincing myself?** Cross-check: search arXiv for "position bias judge" and
   "LLM judge bias quantification" — read top 5 results in full.

2. **Is the citation thesis real?** Check at least 3 recent NLP eval / RLHF papers.
   Do they currently cite a position-bias paper? If they all cite Wang 2023 already
   and don't see a gap, the citation upside is lower than estimated.

3. **Will reviewers say "trivial extension of Wang 2023"?** Pre-empt by:
   - Including 1+ task that is not in Wang 2023 (T-Sum and T-Code qualify).
   - Demonstrating the rank-order corruption that pure MCQ position-bias work
     cannot show.

4. **Is 200 items × 5 judges × 4 conditions × 3 tasks enough power?** Check via
   simulation in `notebooks/01_pilot.ipynb`. If not, increase N.

5. **Am I fooling myself about the cost?** Re-estimate with actual API pricing
   from each provider's pricing page (not memory). Confirm total < $1,500.

---

## Sign-off

If all kill criteria are reviewed and none trigger, proceed to next milestone.
If any trigger, follow the action plan and document in CHANGES.md before continuing.

| Checkpoint | Date | K1 | K2 | K3 | K4 | Action taken |
|---|---|---|---|---|---|---|
| Week 1 | TBD | ✅ | n/a | ✅ | ✅ | — |
| Week 3 (pilot) | TBD | | | | | |
| Week 6 (mid-run) | TBD | | | | | |
| Week 10 (draft) | TBD | | | | | |
| Week 14 (preprint) | TBD | | | | | |
| Week 16 (submit) | TBD | | | | | |
