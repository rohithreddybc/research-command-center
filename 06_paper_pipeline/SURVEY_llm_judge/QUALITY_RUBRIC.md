# Quality Rubric — Referee-Proofing Checklist

*Use during writing (monthly checkpoint) and before submission (final pass).*
*Source*: synthesised from successful TMLR / ACM CS / JMLR surveys.

The objective is to make rejection difficult to justify, not to make the
paper "look impressive." Each item below corresponds to a common reviewer
critique.

---

## A. Coverage (defends against "you missed paper X")

- [ ] **A1**: ≥ 200 papers indexed in `data/survey_corpus.csv`
- [ ] **A2**: ≥ 150 papers cited in the survey body (not just appendix)
- [ ] **A3**: Every major venue (NeurIPS, ICML, ICLR, ACL, EMNLP, NAACL, TMLR, JMLR) represented
- [ ] **A4**: Papers from 2021 through year-of-submission included
- [ ] **A5**: Both academic and industry-published work included
- [ ] **A6**: Both English-language and where possible non-English-language work included (or non-English exclusion explicitly noted as limitation)
- [ ] **A7**: At least 3 prior surveys explicitly compared and differentiated
- [ ] **A8**: A "How to extend this survey" section so reviewers can suggest additions without rejecting

---

## B. Taxonomy (defends against "the taxonomy is arbitrary")

- [ ] **B1**: Taxonomy presented as a single labelled diagram in §1 or §3
- [ ] **B2**: Each branch of the taxonomy has ≥ 3 cited papers
- [ ] **B3**: For each leaf, distinguishing criteria from sibling leaves explicitly stated
- [ ] **B4**: Edge cases discussed (what doesn't fit the taxonomy)
- [ ] **B5**: Taxonomy compared to prior taxonomies (e.g., Gu et al. 2024)
- [ ] **B6**: Taxonomy justified empirically (citing examples from §6 case studies)

---

## C. Prose quality (defends against "writing is unclear")

- [ ] **C1**: Each section has a single-sentence topic statement at the start
- [ ] **C2**: Each subsection ends with a "Primary references" pointer
- [ ] **C3**: No undefined acronyms (define on first use; glossary in appendix)
- [ ] **C4**: No undefined notation (notation table at start)
- [ ] **C5**: Reading-flow check: any reviewer should be able to read the abstract + §1 + §10 in 30 minutes and understand the contribution
- [ ] **C6**: Tables and figures are self-contained (captions explain everything)
- [ ] **C7**: No paragraphs longer than 200 words
- [ ] **C8**: No section longer than 1500 words without subsection breaks

---

## D. Figures and tables (defends against "could be better visualised")

- [ ] **D1**: Taxonomy diagram (§3) — high-quality vector graphic, not screenshot
- [ ] **D2**: Failure-modes summary table (§4) — one row per mode, severity + detection + defence columns
- [ ] **D3**: Defence-effectiveness comparison table (§5)
- [ ] **D4**: Empirical case-study figures (§6) — reproducible from code in companion repo
- [ ] **D5**: Open-problems summary table (§8) — one row per problem with difficulty + research direction
- [ ] **D6**: At least one timeline / growth-of-field figure showing why the survey is timely
- [ ] **D7**: All figures have alt-text descriptions for accessibility (also helps indexing)

---

## E. Empirical grounding (defends against "you're summarising others' work")

- [ ] **E1**: §6 contains ≥ 2 of {T02, T01, T07} case studies as our original empirical work
- [ ] **E2**: Each empirical claim in §4 is tied to a cited paper or our own case study
- [ ] **E3**: No unsupported "common knowledge" claims — every claim has a citation
- [ ] **E4**: Where claims are inferred / synthesised, this is stated explicitly ("We infer that...")
- [ ] **E5**: Reproducibility of our own empirical work documented in companion repo

---

## F. Open problems quality (defends against "future work is vague")

- [ ] **F1**: Each open problem (§8) is phrased as a specific research question, not a topic area
- [ ] **F2**: Each open problem cites at least one paper showing it is open (not solved)
- [ ] **F3**: Each open problem includes a "first step" — concrete way a researcher could attack it
- [ ] **F4**: Open problems span multiple difficulty levels (some 1-paper problems, some grand challenges)
- [ ] **F5**: At least 12 open problems (the magic number — easy for future papers to find one to cite)

---

## G. Comparability and positioning (defends against "how is this different from Gu et al.?")

- [ ] **G1**: §1.2 explicitly contrasts this survey to ≥ 3 existing surveys
- [ ] **G2**: A comparison table (in appendix) shows what each survey covers
- [ ] **G3**: Specific gaps in prior surveys identified and addressed in our coverage
- [ ] **G4**: Honest about overlap — we do not claim originality where there is none

---

## H. Reviewer-anticipation (proactive defence)

Before submission, write a 2-page "reviewer questions" doc anticipating critiques:

- [ ] **H1**: "Why a survey instead of a research paper?" — answered in §1
- [ ] **H2**: "Why now?" — answered in §1.2 with field-growth data
- [ ] **H3**: "Why is your taxonomy better?" — answered in §3 with comparison
- [ ] **H4**: "What's the citation thesis?" — implicit but obvious from §4 and §8
- [ ] **H5**: "Is this really comprehensive?" — answered via methodology section §1.5 and corpus size
- [ ] **H6**: "What about [scoop / contemporary work]?" — addressed in revisions if it appears

---

## I. Companion artifacts (defends against "show me the data")

- [ ] **I1**: Companion GitHub repo public at submission time
- [ ] **I2**: Repo contains structured YAML / JSON for every cited paper
- [ ] **I3**: Repo has search interface or at minimum a filterable table
- [ ] **I4**: Repo has CONTRIBUTING.md inviting community additions
- [ ] **I5**: Repo has CITATION.cff for proper attribution
- [ ] **I6**: All figures in the paper are generated by code in the repo
- [ ] **I7**: Reproducibility appendix in paper points to the repo

---

## J. Marketing readiness (helps post-acceptance citations)

- [ ] **J1**: A 5-tweet thread drafted in `MARKETING.md`
- [ ] **J2**: A blog post draft summarising key findings
- [ ] **J3**: List of newsletters / podcasts to submit to
- [ ] **J4**: Press-friendly summary (200 words)
- [ ] **J5**: Talk slides drafted (for workshop invitations)

---

## K. Submission package quality

- [ ] **K1**: PDF compiles cleanly in TMLR's LaTeX template
- [ ] **K2**: All references resolved (no `[?]` or `(missing)` placeholders)
- [ ] **K3**: All figures embed correctly (no broken paths)
- [ ] **K4**: Page limit checked against venue
- [ ] **K5**: Appendix is in the same PDF (not separate)
- [ ] **K6**: arXiv preprint posted concurrent with submission (same version)
- [ ] **K7**: Companion repo linked from paper
- [ ] **K8**: Conflict-of-interest disclosure (none expected; document anyway)

---

## L. Self-critique pass (1 week before submission)

Spend 1 full day reading the paper as if you are a hostile reviewer.
Write down every weak point you find. Do not submit until each is either
fixed or explicitly addressed in a "Limitations" subsection.

Common self-critique findings:
- "Section 5.3 is shorter than 5.1 and 5.2 — feels incomplete"
- "Figure 7 is hard to read on greyscale printout"
- "The taxonomy in 3.4 is hand-wavy — needs ≥3 examples per leaf"
- "Open problem 8.7 is just restating a known issue"

---

## M. External review (highly recommended)

Even one external reviewer reading the draft is worth 100 hours of self-critique.

Candidate readers:
- A PI or postdoc in the LLM evaluation space (cold-email a survey author)
- A senior PhD student you have any connection to
- A colleague from JudgeSense or the survey-paper collaboration

Provide them with:
- The draft
- A specific question: "What would cause you to reject this at TMLR?"
- 2 weeks for response
- Acknowledge in paper (even if they decline co-authorship)

---

## Final gate

Before clicking "Submit" on TMLR:

- [ ] All items A1–A8 checked
- [ ] All items B1–B6 checked
- [ ] All items C1–C8 checked
- [ ] All items D1–D7 checked
- [ ] All items E1–E5 checked
- [ ] All items F1–F5 checked
- [ ] All items G1–G4 checked
- [ ] All items H1–H6 anticipated
- [ ] All items I1–I7 deployed
- [ ] All items J1–J5 prepared
- [ ] All items K1–K8 verified
- [ ] Self-critique pass complete (L)
- [ ] External review complete or explicit decision to skip (M)

If fewer than 60 of these 60 items are checked: do not submit. Each unchecked
item is a reviewer critique waiting to land.
