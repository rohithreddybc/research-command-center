# Kill Criteria — Survey on LLM-as-Judge

*Defined BEFORE execution starts. Re-read at every monthly checkpoint.*
*Companion: T02 KILL_CRITERIA.md (same format).*

---

## Hard kills (stop and pivot)

### K1: Scoop appears with comparable survey at TMLR / JMLR / ACM CS

**Trigger**: A comprehensive LLM-as-Judge survey appears at TMLR, ACM Computing
Surveys, JMLR, or Foundations and Trends in ML, with:
- (a) Comparable scope (covers ≥80% of our taxonomy), AND
- (b) Comparable comprehensiveness (≥150 papers cited), AND
- (c) Was accepted before our submission.

**Detection**: `scripts/15_arxiv_watch.py` weekly check; manual quarterly scan of TMLR / ACM CS recent acceptances.

**Action**:
1. Read the competing survey in full within 1 week.
2. Identify the dimension(s) on which our survey is differentiated:
   - Deeper failure-mode taxonomy?
   - Empirical case studies they lack?
   - More recent papers (we are submitting later)?
   - Different framing (e.g., security-focused, reproducibility-focused)?
3. If a defensible differentiator exists: **pivot** the survey to emphasise it. Stay in execution.
4. If no defensible differentiator: **kill the survey project**, redirect effort to T07 or B05.

### K2: Field collapses or pivots

**Trigger**: A fundamental paradigm shift makes LLM-as-Judge obsolete (e.g., a new automatic metric that is provably calibrated to human judgment without LLM intermediation).

**Probability**: Low. Even if a better metric appears, the survey of LLM-as-Judge (2021–2026) remains a historical reference.

**Action**: Continue but reframe survey title as "A Survey of LLM-as-Judge (2021–2026): Methods, Failures, and Lessons for Future Evaluation."

### K3: Author bandwidth collapse

**Trigger**: At any monthly checkpoint, < 10 hours/week available to the survey for ≥ 2 consecutive months.

**Action**:
1. Pause the survey (do not kill).
2. Continue T02 only.
3. Resume survey when bandwidth returns.
4. Hard pause for > 6 months → re-evaluate whether the survey is still timely.

### K4: TMLR rejects with no resubmission allowed

**Trigger**: TMLR rejection at month 13–14 with no path to revision.

**Action**:
1. Read the rejection carefully — what were the specific reviewer concerns?
2. Revise per reviews (1–2 months).
3. Submit to ACM Computing Surveys.
4. If ACM CS also rejects: submit to JMLR or Computational Linguistics.
5. arXiv preprint remains regardless — citations accumulate independently of journal acceptance.
6. **Survey is NOT killed by a single rejection.** The survey is killed only if ALL viable venues reject.

---

## Soft signals (raise concerns, do not auto-kill)

### S1: Corpus size plateau in month 1
**Detection**: < 100 papers indexed by end of month 1.
**Response**: Reassess query strategy; expand search terms. Do not kill.

### S2: Taxonomy v1 unstable
**Detection**: Major taxonomy revisions needed after reading first 50 papers.
**Response**: Expected; revise taxonomy in `TAXONOMY.md`. Surveys evolve.

### S3: Reading exceeds time budget
**Detection**: Falling behind on monthly reading targets.
**Response**: Tighten scope (drop low-priority sub-areas); do not abandon. Re-read scope boundaries in PROTOCOL.md §3.

### S4: T02 paper rejected at EMNLP / TMLR
**Response**: Does not affect the survey. The survey cites T02 from arXiv regardless of journal status.

### S5: A competing arXiv survey appears (not yet at top venue)
**Response**: Read it carefully; cite it appropriately; do not kill. Our advantage is the top-tier-venue submission.

---

## Continuation criteria (must hold at every monthly checkpoint)

- Estimated time-to-submission ≤ 18 months from start (was 12; 50% buffer)
- No K1–K4 trigger
- Author bandwidth available (≥ 10 hours/week on average)
- TMLR / ACM CS / JMLR still accepting survey submissions
- No fundamental field collapse

---

## Red-team self-check (do once, month 1)

Before deep literature collection, answer in `CHANGES.md`:

1. **Am I genuinely capable of writing a 60–80 page comprehensive survey?**
   Self-test: write a 5-page "mini-survey" on one sub-area in week 1. If it
   takes more than 20 hours or feels miserable, the full survey may not be feasible.

2. **Is the field actually under-served by existing surveys?**
   Cross-check: read Gu et al. 2024 in full. Identify ≥ 5 specific gaps.
   Document the gaps in `GAPS.md`. If you cannot find 5 gaps, the survey may be redundant.

3. **Am I positioned to be cited?**
   Honest assessment: do you have any prior arXiv activity? Twitter following?
   Network of researchers who know your name? If none of these, the survey
   has to be exceptional to overcome the discovery deficit.

4. **Can I sustain interest for 12 months?**
   Surveys are slogs. Identify what will keep you going: (a) the citation goal,
   (b) the NIW/EB-1A path, (c) intellectual interest in the field, (d) all three.
   If less than 2 of 3, plan to pair with T02 work to break monotony.

5. **What is my fallback if the survey fails?**
   - If at month 6 the draft is incomplete → trigger K3 review
   - If at month 12 TMLR rejects without resubmit → escalate to ACM CS
   - If at month 24 all top venues reject → arXiv-only release with annual updates
   In NO scenario do I claim the survey was "wasted effort" — the literature collection alone is valuable for future work.

---

## Sign-off table

| Checkpoint | Date | K1 | K2 | K3 | K4 | Action taken |
|---|---|---|---|---|---|---|
| Month 1 | TBD | | | | | |
| Month 3 | TBD | | | | | |
| Month 6 | TBD | | | | | |
| Month 9 | TBD | | | | | |
| Month 12 | TBD | | | | | |
| Month 15 (post TMLR decision) | TBD | | | | | |
