# T07 — Pre-Execution Checklist

*Project status: Long-term paper candidate (per `reports/BRIDGE_PUBLICATION_STRATEGY.md`)*
*Pipeline source: blind_citation profile, run c805933 (2026-05-11)*
*EW profile: 0 paper direct / 12 artifact direct / artifact_diff = moderate*

T07 cannot start execution until **every box below is checked**.
Estimated time to complete the checklist: 4–8 hours (one focused day).

---

## ✅ Block 1: Read the blocking arXiv paper

**Paper**: "Red Teaming the Mind of the Machine: A Systematic Evaluation of Prompt Injection"
*(arXiv 2025; relevance 0.625 in pipeline data; highest-relevance partial paper for T07)*

- [ ] Found the paper on arXiv (search: "Red Teaming the Mind of the Machine")
- [ ] Downloaded PDF
- [ ] Read abstract + introduction + section on threat model
- [ ] Read related-work section (do they cite any judge-as-target paper?)
- [ ] Read methodology section (are judge LLMs included as targets?)
- [ ] Read results section (what models do they attack?)
- [ ] Read released-artifact section (do they release a benchmark?)

**Decision tree**:
- ✅ If they explicitly include LLM-as-judge as a target with quantified
  injection success rates: **PIVOT T07** to a narrower angle (see Block 5).
- ✅ If they target only assistants/agents in tool-use contexts (not judges):
  **PROCEED with T07** as scoped in PROTOCOL.
- ⚠️ If unclear: assume they cover it (worst case) and pivot.

**Write a 3-sentence summary in `BLOCKING_PAPER_NOTES.md`** before continuing.

---

## ✅ Block 2: Inspect the 12 direct artifacts

The pipeline detected 12 direct GitHub/HuggingFace/PWC artifacts. Each must be
inspected to confirm none target judge LLMs.

Run:
```powershell
python -c "
import json
ew = json.loads(open('data/existing_work/T07.json', encoding='utf-8').read())
for d in ew.get('documents', []):
    if d.get('overlap_type') == 'DIRECT_OVERLAP' and d.get('source_type') in ('github','huggingface','paperswithcode'):
        print(f'[{d[\"source_type\"]}] {d.get(\"title\",\"\")[:80]} -- {d.get(\"url\",\"\")}')
"
```

For each artifact:

- [ ] Visit the URL
- [ ] Check README / dataset card
- [ ] Determine: does it target *assistants* (the threat model is "user gives
  malicious input; assistant misbehaves") or *judges* (the threat model is
  "candidate response embeds injection; judge gets fooled")?
- [ ] Record the verdict in `ARTIFACT_AUDIT.md`

Expected pattern: nearly all 12 will be assistant-focused (Open-Prompt-Injection,
PINT, BIPIA, etc.) — this is the gap.

If any 1+ artifacts ARE judge-focused: those become the most important related
work to differentiate from in the paper. They are not necessarily kills.

---

## ✅ Block 3: Cross-check arXiv 2024–2026

The pipeline ran a corpus snapshot at a fixed time. New papers may have appeared.
Run a fresh check:

- [ ] arXiv search: "LLM judge prompt injection" — read top 10 results
- [ ] arXiv search: "evaluator robustness adversarial LLM" — read top 5
- [ ] arXiv search: "judge model attack" — read top 5
- [ ] Google Scholar: "candidate-side prompt injection LLM-as-a-judge" — read top 5

For any paper not already in the pipeline corpus that targets judges directly:
add to `BLOCKING_PAPER_NOTES.md` and re-evaluate.

---

## ✅ Block 4: Set up the scoop watch

- [ ] Add T07 to `data/scoop_watch_queries.json` (already done by default)
- [ ] Run `python scripts/15_arxiv_watch.py --days 30` to bootstrap
- [ ] Schedule weekly run (Windows Task Scheduler or manual)

---

## ✅ Block 5: Write the differentiator paragraph

After Blocks 1–3 are complete, write a single paragraph (≤150 words) that:

1. Names the closest 2–3 existing works (paper or artifact).
2. States the precise dimension on which T07 is different.
3. States why that difference matters (citation thesis).

**Template**:

> Existing prompt-injection benchmarks ([X], [Y], [Z]) target [assistant LLMs in
> tool-use settings / agent contexts / RLHF training data]. T07 targets a distinct
> threat model: the **judge LLM as victim**, where the attacker controls the
> candidate response being evaluated, and the judge is the security boundary.
> This matters because [LLM-as-judge is now standard infrastructure in RLHF /
> AutoEval / leaderboards]; a corrupted judge invalidates downstream conclusions
> at scale. To our knowledge, no peer-reviewed work systematically characterises
> this threat model with a released, reusable benchmark.

Write the paragraph in `DIFFERENTIATOR.md`. The paper introduction will cite this
verbatim.

---

## ✅ Block 6: Decide pivot vs proceed

Based on Blocks 1–5, choose ONE:

- [ ] **PROCEED**: T07 scope is intact. Move to PROTOCOL.md (TBD — write next).
- [ ] **PIVOT-NARROW**: T07 scope must shrink. Update PROTOCOL.md with the
      narrower scope (e.g., "RLHF reward models as judges only" or "defence-only,
      no new attacks").
- [ ] **KILL T07**: Insurmountable scoop. Reallocate effort to T02 (already
      bridge), T01, or B05.

**Document the choice in `BLOCKING_PAPER_NOTES.md` with date and rationale.**

---

## ✅ Block 7: Post the priority-claim arXiv preprint

If proceeding (or pivoting): post a short technical report to arXiv within
**2 weeks** of clearing Blocks 1–5.

- [ ] Write the preprint using `ARXIV_PREPRINT_STUB.md`
- [ ] Submit to arXiv (cs.CL primary, cs.CR secondary)
- [ ] Receive arXiv ID
- [ ] Update `DIFFERENTIATOR.md` with the arXiv ID

The preprint establishes the priority claim against the artifact ecosystem
even if the full paper is months away.

---

## ✅ Block 8: Begin execution

Only after Blocks 1–7 are complete. Then:
- Write `PROTOCOL.md` mirroring the structure of T02's PROTOCOL
- Write `PAPER_OUTLINE.md`
- Write `CODE_SCAFFOLD.md`
- Begin work

---

## Status

| Block | Owner | Date completed | Notes |
|---|---|---|---|
| 1. Read blocking paper | | | |
| 2. Inspect 12 artifacts | | | |
| 3. Cross-check arXiv | | | |
| 4. Set up scoop watch | | | |
| 5. Write differentiator | | | |
| 6. Decide pivot/proceed | | | |
| 7. arXiv preprint posted | | | |
| 8. Begin execution | | | |

---

## Files in this directory

- **PRE_EXECUTION_CHECKLIST.md** (this file)
- **ARXIV_PREPRINT_STUB.md** — preprint template for Block 7
- **BLOCKING_PAPER_NOTES.md** — TBD, written during Block 1
- **ARTIFACT_AUDIT.md** — TBD, written during Block 2
- **DIFFERENTIATOR.md** — TBD, written during Block 5
- **PROTOCOL.md** — TBD, written after Block 6 if PROCEED/PIVOT
- **PAPER_OUTLINE.md** — TBD, written after PROTOCOL is finalised
- **CODE_SCAFFOLD.md** — TBD, written after PAPER_OUTLINE
