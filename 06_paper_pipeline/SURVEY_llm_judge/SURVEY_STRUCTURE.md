# Survey Structure — Section-by-Section Plan

*Working title*: **"Trustworthy LLM-as-a-Judge: A Comprehensive Survey of Methods, Failure Modes, and Defences"**
*(v3; updated 2026-05-16 after empirical title check found WEAK-ECHO on prior "Judging the Judges" version)*
*Target length*: 60–80 pages (TMLR survey certification)

The structure below is the citation-magnet template from `HIGH_CITATION_STRATEGY.md` §3.3:
Comprehensive survey + novel taxonomy + empirical case study + identified open problems.

---

## §1 — Introduction (4–6 pages)

### §1.1 Motivation
- The rise of LLM-as-Judge: from MT-Bench (2023) to industry deployment (2024–2026)
- Scope: an LLM evaluating another LLM's output
- Why this matters: RLHF training data, leaderboards, safety evaluation, content moderation

### §1.2 Why a survey now
- Volume of work (cite citation growth chart from `HIGH_CITATION_STRATEGY.md`)
- Lack of coherent taxonomy
- Reproducibility crisis: every paper defines its judge differently
- Need a reference point

### §1.3 Contributions of this survey
1. A unified taxonomy of LLM-as-Judge methods, failure modes, and defences
2. Comprehensive review of ~200 papers (2021–2026)
3. Empirical case studies validating identified failure modes
4. A research agenda with 12 specific open problems
5. Companion GitHub repo with metadata for every surveyed paper

### §1.4 Scope and organisation
- What this survey covers (judging methodology + failures + defences + evaluation)
- What it does not cover (pre-LLM automatic metrics, human evaluation methodology, etc.)
- Reader guide: which sections matter for whom (practitioners, researchers, policymakers)

### §1.5 Methodology of this survey
- Paper inclusion criteria (cite ≥2 of {appears in ACL Anthology, arXiv with >5 citations, mentioned in another survey})
- Total papers reviewed: N (final number)
- Sources: Semantic Scholar, arXiv, ACL Anthology, OpenReview
- Annotation protocol (single reviewer; conservative inclusion)

---

## §2 — Foundations (6–8 pages)

### §2.1 What is LLM-as-Judge?
- Definition: an LLM scoring or comparing other LLM outputs
- Distinction from "LLM-as-Annotator" (general labelling)
- Distinction from "LLM-as-Critic" (text feedback, not scores)

### §2.2 Historical context
- Pre-LLM automatic metrics (brief — 2 paragraphs)
- BLEURT, COMET — neural metrics requiring training data
- Emergence of GPT-3.5/4 as zero-shot judge (2023)
- Industrial adoption: HELM, Chatbot Arena, MT-Bench (2023–2024)
- Current state (2026): default infrastructure in RLHF and AutoEval

### §2.3 Why LLMs make plausible judges
- Pretraining on text inherently captures quality signals
- Few-shot generalisation across tasks
- Cost-time tradeoff vs human evaluation

### §2.4 Why LLMs make unreliable judges
- Systematic biases (preview of §3 / §4)
- Distribution shift from training data to evaluation
- Hallucination in judge rationale
- Adversarial vulnerability

### §2.5 The judging pipeline (canonical form)
- Inputs: task instruction, candidate(s), optional reference
- Outputs: score (scalar), preference (categorical), or rationale (text)
- Aggregation: how judge calls combine into evaluations
- Diagram: full pipeline with components labelled

---

## §3 — Methods Taxonomy (8–12 pages)

### §3.1 Pointwise vs Pairwise vs Listwise
- Definitions, when each is used, comparative strengths

### §3.2 Single-judge vs Panel
- Single LLM, single call
- Single LLM, multiple calls (self-consistency)
- Multiple LLMs (panel / ensemble)
- Heterogeneous panels (judges from different families)

### §3.3 With-reference vs Without-reference
- Gold-answer-as-reference (e.g., HumanEval grading)
- No gold answer (subjective tasks)

### §3.4 Chain-of-Thought judging
- Direct scoring vs CoT scoring
- Empirical evidence: when CoT helps, when it hurts
- The "scoring rubric" prompt pattern (e.g., G-Eval)

### §3.5 Augmented judges
- Retrieval-augmented: judges with access to external knowledge
- Tool-using: judges that execute code or search
- Multi-step: judges that decompose evaluation into subskills

### §3.6 Specialised judges
- Domain-tuned (medical, legal, code)
- Fine-tuned reward models (RLHF reward models as judges)
- Distilled small judges (cheap, fast, lower quality)

### §3.7 Comparative table
- Method × {cost, latency, accuracy proxy, common failure modes}

---

## §4 — Failure Modes (10–14 pages, the citation core)

This section is the single most-cited part of typical surveys. **Goal**: every
LLM judge user must know these failure modes; every paper on judge robustness
must cite this section.

### §4.1 Position bias
- Definition (cite Wang 2023; Zheng 2023; T02 empirical study)
- Magnitude across judges
- Why it happens (causal hypotheses)
- Detection methods

### §4.2 Self-preference bias
- Judges prefer their own outputs / their family's outputs (cite Panickssery 2024)
- Quantification across model families
- Implication for cross-family RLHF

### §4.3 Length bias
- Judges prefer longer responses
- Magnitude (cite Singhal 2023; Saito 2023)
- Decoupling length from quality

### §4.4 Style bias
- Judges prefer confident, well-formatted, "AI-sounding" responses
- Even when factuality is lower
- Empirical evidence (cite Park 2024; Hosking 2024)

### §4.5 Format bias
- Judges prefer specific output formats (JSON, Markdown, plain prose)
- The structured-output interaction (cite EACL 2026 paper)

### §4.6 Adversarial vulnerability — Candidate-Side Prompt Injection (CSPI)
- New threat model (cite T07 — once arXiv preprint posted)
- Attack taxonomy: score override, role confusion, distractor injection, format hijacking, confidence manipulation
- Empirical attack success rates

### §4.7 Calibration drift
- Judge scores drift across model versions
- Reproducibility implication: results not comparable across API updates
- Mitigation: version pinning

### §4.8 Length-quality confounding
- The hardest-to-detect failure mode
- When the judge is right (quality really is correlated with length) vs when it's a bias

### §4.9 Cross-judge agreement gaps
- Inter-judge agreement is often lower than reported
- Long-context tasks especially (cite T01)
- Implication: a single judge's score is a sample, not ground truth

### §4.10 Summary table of failure modes
- One row per failure mode: severity (typical), detection method, defence references

---

## §5 — Defences and Mitigations (8–10 pages)

### §5.1 Prompt-level defences
- Position randomisation
- Explicit position-bias warnings in the prompt
- Chain-of-Thought
- Output structure (JSON-only)

### §5.2 Ensemble methods
- Multi-judge consensus
- Multi-prompt averaging
- Panel-of-judges with disagreement detection

### §5.3 Calibration methods
- Post-hoc calibration (Platt scaling, isotonic regression)
- Learned calibration heads
- Human-anchored calibration

### §5.4 Structural / pipeline defences
- Parser-validated outputs
- Sandboxed evaluation
- Human-in-the-loop review

### §5.5 Adversarial defences
- System-prompt hardening against CSPI
- Dual-judge consensus
- Adversarial-trained judges (emerging)

### §5.6 Defence effectiveness comparison
- Empirical effectiveness numbers (where available)
- Cost-of-defence vs benefit table

---

## §6 — Empirical Case Studies (8–10 pages)

This section is the survey's "skin in the game" — it cites our own empirical
work to validate claims made in §4.

### §6.1 Case Study 1: Position bias across 5 frontier judges
*(This is the T02 paper, re-presented as a survey section.)*
- Methods, results, take-aways
- Cite T02 paper as primary reference
- Tables and figures from T02

### §6.2 Case Study 2: Cross-judge agreement on long-context QA
*(This is the T01 paper, if executed.)*
- If T01 is not published yet: a brief replication-style study showing the gap

### §6.3 Case Study 3: CSPI attack effectiveness
*(This is the T07 paper, if executed.)*
- Brief presentation of T07 results
- If T07 is not published yet: rely on the arXiv preprint as a citation

### §6.4 Cross-cutting analysis
- Which failure modes are correlated?
- Which defences are co-effective?
- A unified empirical view across the case studies

---

## §7 — Evaluation Methodology for Judges (4–6 pages)

How do we evaluate the judges themselves? This is the meta-question.

### §7.1 Agreement with humans (the standard test)
- Cohen's κ, Krippendorff's α, Pearson / Spearman correlation
- Pitfalls: small N, biased crowd, instruction sensitivity
- Where this metric is and is not appropriate

### §7.2 Agreement across judges (inter-judge)
- When two judges disagree, which is right?
- Triangulation methods

### §7.3 Stability over time
- Judge scores under repeated calls
- Judge scores across model versions
- Reproducibility implications

### §7.4 Sensitivity to prompt
- Prompt-rephrasing studies
- How fragile is judging?

### §7.5 Recommended best practices for reporting judges in papers
- A checklist for any future paper using LLM judging
- Becomes a citation target itself

---

## §8 — Open Problems and Research Agenda (4–6 pages)

This is the "future work" section — but with teeth. Each open problem is a
specific, testable research question that subsequent papers will address (and cite us).

### §8.1 Adversarial-robust judges
- Can we build judges that resist CSPI by design?

### §8.2 Cross-cultural and multilingual judging
- All current judges are anglocentric; massive gap for non-English

### §8.3 Long-context judging at scale
- Judges struggle with >32K context; what changes at 1M context?

### §8.4 Judge alignment with diverse human values
- Whose preferences does the judge encode?

### §8.5 Judge interpretability
- Can we explain judge decisions to non-ML stakeholders (clinicians, lawyers, regulators)?

### §8.6 Standards and certification
- Should there be a "certified judge" standard for safety-critical applications?

### §8.7 Reward modelling vs general judging
- Are RLHF reward models a special case of judges, or qualitatively different?

### §8.8 Cost-quality Pareto
- When is a cheap small judge sufficient?

### §8.9 Domain transfer
- A judge trained on general text — does it generalise to medical, legal, code?

### §8.10 Judge data contamination
- Has the judge seen the evaluation set in pretraining?

### §8.11 Cascading judges
- Hierarchical judging: cheap first-pass + expensive second-pass for ambiguous cases

### §8.12 Regulatory implications
- EU AI Act, NIST AI RMF, FDA SaMD — what does "validated automatic evaluation" mean legally?

---

## §9 — Discussion and Recommendations (3–4 pages)

### §9.1 For practitioners
- Choosing a judge for your application
- Reporting standards

### §9.2 For researchers
- The most under-explored areas
- Reproducibility expectations

### §9.3 For policymakers
- When automatic judging is acceptable as the primary evaluation
- Auditability requirements

### §9.4 Limitations of this survey
- English-only literature
- Cut-off date (2026-XX)
- Single-author bias (note explicitly)

---

## §10 — Conclusion (1–2 pages)

- Summarise the taxonomy
- The 12 open problems
- A vision for trustworthy LLM-as-Judge

---

## Appendix A — Full reference table (5–10 pages)

Every surveyed paper, with: citation, year, venue, method type, failure modes addressed,
defences proposed, has-code, key contribution.

This appendix is itself a citation target.

---

## Appendix B — Reproducibility appendix (2–3 pages)

- How papers were collected
- Inclusion / exclusion criteria
- All taxonomy decisions with rationale
- Companion repo structure

---

## Appendix C — Best-practices checklist (1–2 pages)

A printable, citable checklist for any future paper using LLM-as-Judge.
Modelled after Pineau et al. 2021 (the ML reproducibility checklist).

This appendix is the secondary citation target — when papers in the future
say "we follow the LLM-Judge Reporting Checklist (Author 2027)", that's us.

---

## Length budget summary

| Section | Pages |
|---|---|
| §1 Introduction | 5 |
| §2 Foundations | 7 |
| §3 Methods Taxonomy | 10 |
| §4 Failure Modes | 12 |
| §5 Defences | 9 |
| §6 Empirical Case Studies | 9 |
| §7 Evaluation Methodology | 5 |
| §8 Open Problems | 5 |
| §9 Discussion | 4 |
| §10 Conclusion | 1.5 |
| Appendix A — Reference table | 7 |
| Appendix B — Reproducibility | 2 |
| Appendix C — Checklist | 1.5 |
| References | 6–10 |
| **Total** | **~84 pages** |

(Within TMLR survey certification, ACM CS, and JMLR survey envelopes.)
