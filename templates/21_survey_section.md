# §{section_number} — {section_title}

*Length target*: {target_pages} pages (~{target_words} words at 250 words/page)
*Draft status*: not started / in progress / first draft / revised / final

---

## Topic statement (one sentence)

> [A single sentence that any reviewer can read to understand what this section covers.]

---

## Subsections

### §{section_number}.1 [Subsection name]

(Topic sentence.)

(Body: 1–3 paragraphs. Each paragraph ≤ 200 words. Each substantive claim cites a primary reference.)

**Primary references**: [author1{year1}], [author2{year2}], [author3{year3}]

---

### §{section_number}.2 [Subsection name]

(As above.)

---

## Figures / tables planned

- **Figure {section_number}.1**: [Caption.] *Source*: [code path or derivation]
- **Table {section_number}.1**: [Caption.] *Source*: [csv path]

---

## Cited corpus entries

Papers from `data/survey_corpus.csv` whose `section = {section_id}` should be considered for inclusion.
Run `python scripts/18_survey_progress.py` to refresh the count.

Currently auto-classified to this section: [auto-count]

---

## Quality-rubric self-check (this section only)

- [ ] Topic statement present in one sentence
- [ ] Each subsection starts with a topic sentence
- [ ] No undefined acronyms
- [ ] Every claim has a primary citation OR is explicitly labelled as inference
- [ ] Section ends with "Primary references" pointer
- [ ] No paragraph longer than 200 words
- [ ] Figures and tables are self-contained (caption explains all)
- [ ] Page count within ±20% of target
- [ ] Reviewed against `06_paper_pipeline/SURVEY_llm_judge/QUALITY_RUBRIC.md` (relevant items)

---

## Open TODOs for this section

- [ ] [Specific todo 1]
- [ ] [Specific todo 2]
