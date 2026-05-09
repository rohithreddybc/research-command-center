"""
00_setup_repo.py
Scaffold the research-command-center repo.
Idempotent: safe to re-run.
"""
from __future__ import annotations
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

FOLDERS = [
    "00_admin",
    "01_topic_discovery",
    "02_current_verification",
    "03_literature_review",
    "04_topic_scoring",
    "05_venue_selection",
    "06_paper_pipeline",
    "07_experiments",
    "08_reproducibility",
    "09_public_artifacts",
    "10_peer_review",
    "11_collaborators",
    "12_citation_tracking",
    "13_immigration_evidence",
    "14_visibility",
    "15_career_portfolio",
    "templates",
    "data",
    "data/cache",
    "data/queries",
    "data/evidence",
    "data/papers_dedup",
    "data/scores",
    "data/reviews",
    "data/agreement",
    "data/decisions",
    "data/round_log",
    "reports",
    "logs",
    "scripts/common",
    "scripts/tests",
]


def write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def make_folders() -> None:
    for f in FOLDERS:
        p = REPO_ROOT / f
        p.mkdir(parents=True, exist_ok=True)
        gitkeep = p / ".gitkeep"
        if not any(p.iterdir()):
            gitkeep.write_text("", encoding="utf-8")


# ---------- 20 templates ----------
TEMPLATES: dict[str, str] = {
    "01_topic_eval.md": """---
topic_id: T<NN>
date: YYYY-MM-DD
status: PROV | NME | VER | REJ
---

# Topic: <title>

## One-line idea
## Category and sub-area
## Why now (3 sentences max)
## Stated gap (specific, falsifiable)
## Differentiator vs prior art (1 sentence — must name 3+ prior works)
## Artifact type
survey | taxonomy | benchmark | dataset | metric | tool | method | empirical

## MVP version (30 days)
## Stronger version (60 days)
## Ideal version (90 days)
## Required data sources (public links)
## Coding required?
none | scripts | repo | toolkit | webapp

## Collaboration required?
## Likely venues (with VERIFY tags)
## Free/no-APC route (with VERIFY)
## Risks: saturation / novelty / data / IP / ethics
## NIW value (1–5) and rationale
## EB-1A value (1–5) and rationale
## FAANG/career value (1–5) and rationale
## What MUST be verified before commit
## Decision (KEEP/DROP/NARROW) + date
## Kill criteria (specific, observable)
""",
    "02_source_verification.md": """---
topic_id: T<NN>
query: ""
source: ""
date: YYYY-MM-DD
---

# Verification log entry

- query:
- source: semantic_scholar | openalex | crossref | arxiv | doaj | github | huggingface | paperswithcode | openreview | manual
- n_results:
- top3 papers (id, year, citations, title):
- key takeaway:
- VERIFY tag (true/false):
- VERIFY reason (only if true):
- automated next step:
""",
    "03_literature_extraction.csv": "paper_id,year,venue,model,dataset,judge_config,sample_size,stat_test,repro_level_1to5,disclosure_completeness_1to5,notes\n",
    "04_paper_summary.md": """---
paper_id:
year:
venue:
---

# Paper summary

- Title:
- Authors:
- Problem:
- Contribution:
- Method:
- Datasets:
- Results:
- Limitations stated by authors:
- My use:
- Citation:
""",
    "05_venue_eval.md": """---
venue_name: ""
type: journal | conference | workshop
date: YYYY-MM-DD
---

# Venue evaluation

- Name:
- Type:
- Indexing (DOAJ / Scopus / WoS / PubMed) [VERIFY each]:
- APC fee (USD) [VERIFY]:
- Review timeline [VERIFY]:
- h5-index [VERIFY at Google Scholar Metrics]:
- Scope match (1–5):
- Citation potential fit (1–5):
- Decision: SHORTLIST / FALLBACK / REJECT
- Source URLs checked:
- Automated next step (if VERIFY):
""",
    "06_no_apc_checklist.md": """# No-APC venue checklist

- [ ] DOAJ-listed (link)
- [ ] Peer-review confirmed (link to editorial process)
- [ ] Indexed in at least one of Scopus / WoS / PubMed / DOAJ
- [ ] Scope matches my topic
- [ ] Decision time acceptable for my deadline
- [ ] No APC confirmed on official site (screenshot URL)
- [ ] No predatory red flags (Think.Check.Submit. pass)
- [ ] Recent issues exist and are real
""",
    "07_predatory_checklist.md": """# Predatory venue avoidance checklist

- [ ] Editorial board members are real and verifiable
- [ ] Journal listed in DOAJ (or society-published)
- [ ] Think.Check.Submit. checks pass
- [ ] No unsolicited spam to me
- [ ] Acceptance time is realistic (not <1 week)
- [ ] DOIs resolve and are registered with Crossref
- [ ] Articles in last 12 months are coherent and properly cited
- [ ] Publisher policies clear on retractions, copyright, OA license
""",
    "08_proposal_one_pager.md": """# One-pager: <topic title>

## Research question
## Why now
## Single-sentence contribution
## Method (3 bullets)
## Artifact (what is publicly released)
## Target venue + fallback
## Timeline (3 milestones)
## Kill criteria
""",
    "09_experiment_plan.md": """# Experiment plan

- Hypothesis:
- Factors / IVs:
- Conditions:
- Sample size + power calc:
- Metrics (primary, secondary):
- Baselines:
- Ablations:
- Compute budget:
- Schedule:
- Risk to validity + mitigation:
""",
    "10_repro_checklist.md": """# Reproducibility checklist

- [ ] Code archived (Zenodo DOI + GitHub tag)
- [ ] Environment pinned (requirements.txt or environment.yml + Dockerfile)
- [ ] Random seeds documented
- [ ] Datasets documented (public links + license)
- [ ] Prompts and configs versioned in repo
- [ ] Logs + intermediate artifacts archived
- [ ] Model versions/snapshots specified
- [ ] Hardware specified
- [ ] License declared (MIT for code, CC-BY for data)
- [ ] README has quickstart + reproduce-paper command
- [ ] Citation file (CITATION.cff)
""",
    "11_artifact_release_checklist.md": """# Public artifact release checklist

- [ ] License (MIT/Apache/CC-BY) declared
- [ ] README quality reviewed
- [ ] Examples and quickstart present
- [ ] CONTRIBUTING.md / CODE_OF_CONDUCT.md
- [ ] CI passing
- [ ] Zenodo DOI minted
- [ ] CITATION.cff present
- [ ] Security review (no secrets, no PHI, no employer data)
- [ ] Demo link or HF Space (if applicable)
- [ ] Announcement plan (LinkedIn, X/BlueSky, mailing list)
""",
    "12_outreach_tracker.csv": "person,public_profile_url,reason,draft_message_link,sent_date,replied,follow_up_date,notes\n",
    "13_review_opportunity.md": """# Peer-review opportunity

- Venue:
- Role: program committee / reviewer / area chair
- Date applied:
- Status:
- Action items:
""",
    "14_citation_tracker.csv": "paper,date,citing_paper,venue,type,narrative_use\n",
    "15_immigration_evidence.md": """---
criterion: ""  # NIW prong 1/2/3 OR EB-1A criterion (citations / scholarly articles / original contributions / judging / press / awards / membership / leading role / high salary)
date: YYYY-MM-DD
---

# Evidence item

- Type:
- Description:
- Public link / file path:
- Strength (1–5):
- Gap-to-fill:
- Notes:
""",
    "16_weekly_plan.md": """---
week: NN
start_date: YYYY-MM-DD
---

# Weekly plan

## Goals
## Deliverables
## Claude tasks
## ChatGPT tasks
## Manual / verification tasks
## Decisions to make
## Stop/continue gate
""",
    "17_kill_criteria.md": """# Kill criteria for topic <id>

- If by <date>: <observable condition> then DROP.
- If during verification: <evidence finding> then NARROW.
- If during execution: <result threshold not met> then PIVOT to MVP.
""",
    "18_red_team_review.md": """# Red-team review

For each candidate topic, identify:

- Anchoring bias:
- Recency bias:
- Immigration bias (NIW good but citation poor):
- Career bias (FAANG good but immigration poor):
- Feasibility illusion:
- Publication illusion:
- Free-publication illusion:
- Tool-building bias:
- Citation illusion:
- Venue prestige illusion:
- AI hype bias:
- Survey-paper bias:

For each: which topics are affected, and what score adjustment.
""",
    "19_reviewer_response.md": """# Response to reviewer

- Reviewer comment:
- Our response:
- Change made (file + line OR section):
- Verification:
""",
    "20_publication_decision.md": """# Publication decision

- Venue chosen:
- Alternatives considered:
- Date decided:
- Rationale:
- Fallback path if rejected:
""",
}


# ---------- Top-level docs ----------
README = """# research-command-center

Private/local research workflow scaffold for high-citation paper production with NIW/EB-1A and FAANG/career evidence value.

## Quickstart

```
python scripts/00_setup_repo.py        # idempotent scaffold
python scripts/10_run_pipeline.py      # full automated verification pipeline
```

## Pipeline

```
data/topics_seed.csv
  -> 01_generate_queries.py
  -> 02_collect_topic_evidence.py    (Semantic Scholar, OpenAlex, Crossref, arXiv)
  -> 03_collect_extra_evidence.py    (GitHub, HuggingFace, Papers With Code, DOAJ)
  -> 04_collect_venue_evidence.py    (DOAJ, OpenReview, Crossref journals)
  -> 05_score_topics.py
  -> 06_llm_review_topics.py         (Anthropic + OpenAI panel; skipped if keys missing)
  -> 07_compare_reviewers.py
  -> 08_confidence_gate.py           (GO / NARROW / DROP / NEEDS_MORE_EVIDENCE)
  -> [loop back to 03 if NEEDS_MORE_EVIDENCE and rounds remaining]
  -> 09_generate_final_report.py     (reports/final_decision_report.md)
```

## Privacy / IP

See `00_admin/ip_safety_rules.md`. Public data only. Never commit PHI, employer SQL, internal URLs, screenshots, or proprietary logic.

## Layout

- `00_admin/` — goals, IP rules, weekly review log
- `01_topic_discovery/` — topic universe (75-topic catalog)
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
- `scripts/` — automation pipeline
- `data/` — pipeline inputs and intermediate artifacts
- `reports/` — final reports
- `logs/` — pipeline logs

All claims marked **VERIFY** are time-sensitive and must be re-checked before any commitment of >30 days work.
"""

DECISIONS = """# DECISIONS log

Append-only. Every commitment of >1 week of work goes here with date and rationale.

| Date | Decision | Rationale | Topic ID | Reversible? |
|------|----------|-----------|----------|-------------|
"""

IP_RULES = """# IP / privacy safety rules (non-negotiable)

This repo lives on personal devices and personal accounts only. It is private.

## Never commit

- PHI of any kind
- Member IDs, claim IDs, encounter IDs
- Employer SQL, stored procedures, business logic
- Power BI screenshots or DAX expressions from work
- Internal URLs, internal architecture diagrams
- Slack / Teams / email content from work
- Vendor contracts, internal documents
- Employer credentials of any kind
- Any data you cannot independently re-derive from public sources

## Healthcare topics: public data only

- MIMIC-IV / eICU (with DUA, do not redistribute raw data)
- CMS SynPUF, SyntheticMass, Synthea
- MedMCQA, MedQA, PubMedQA, MMLU-clinical
- USPSTF / CDC / NICE / WHO public guidelines (verify license per source)

## Process rules

- Personal device, personal accounts, personal time only
- VERIFY employment IP / moonlighting clause in writing with HR/legal before any artifact release
- Re-check public dataset DUAs before each release
- Run a secrets scan before any artifact release
- Do not train or finetune on employer data, even if "anonymized"

## VERIFY items requiring legal/HR judgment (not automatable)

- Employer IP assignment clause interpretation
- Moonlighting policy interpretation
- Whether a specific public dataset's DUA permits a specific use
- Patent / publication clearance with employer if any overlap
"""

GITIGNORE = """# secrets
.env
*.key
*.pem

# data caches and large files
data/cache/
*.sqlite
*.db
__pycache__/
*.pyc

# OS
.DS_Store
Thumbs.db

# editor
.vscode/
.idea/
"""

GOALS = """# Goals (high level only)

- Publish 2 peer-reviewed papers + 1 public artifact within 90 days
- Build EB-1A / NIW evidence: scholarly articles, original contributions, judging (peer review), and citations
- Position for higher-paying ML / data-science roles
- Maintain low IP / employer risk through public-data-only scope
"""

WEEKLY_REVIEW = """# Weekly review log

Append one entry per week. Use template `templates/16_weekly_plan.md` as the per-week structure.
"""


# ---------- Starter CSVs ----------
TOPIC_UNIVERSE = """topic_id,title,category,artifact_type,public_data,coding,feasibility_days,saturation_risk,citation_audience,ip_risk,prelim_priority
T01,Cross-judge agreement on long-context QA,Eval,benchmark,Y,Y,60,High,Lg,L,3
T02,Position-bias quantification across judge models,Eval,empirical+harness,Y,Y,30,High,Lg,L,3
T03,Self-preference bias in same-family judges,Eval,empirical,Y,Y,30,High,Lg,L,3
T04,Prompt-template sensitivity benchmark for clinical-domain LLM judges,Eval,bench+tool,Y,Y,60,Med,Lg,L,5
T05,Judge confidence calibration vs human gold,Eval,empirical,Y,Y,60,Med,Md,L,4
T06,Pairwise vs pointwise judge agreement under perturbation,Eval,empirical,Y,Y,30,High,Md,L,3
T07,Judge robustness to candidate-side prompt injection,Eval/Safety,empirical+bench,Y,Y,60,Low-Med,Lg,L,5
T08,Cost-quality Pareto small open judges vs frontier,Eval,empirical,Y,Y,30,Med,Lg,L,4
T09,Judge consistency under temperature/seed variation,Eval,empirical,Y,Y,30,High,Md,L,3
T10,Reproducibility audit / meta-analysis of LLM-judge papers,Meta,database+paper,Y,Light,45,Low,Lg,L,5
T11,Format sensitivity (JSON/YAML/prose) on benchmark scores,Prompt,bench,Y,Y,30,Med,Lg,L,4
T17,Tokenization-induced leaderboard variance,Eval,empirical,Y,Y,45,Low,Lg,L,4
T25,Hallucination taxonomy: RAG vs no-RAG,RAG,taxonomy+paper,Y,Light,60,Med,Lg,L,4
T37,Clinical-guideline consistency across LLM versions over time,HC AI,empirical,Y,Y,60,Low,Md,L,5
T43,Reproducibility audit of clinical LLM papers,Meta/HC,database+paper,Y,Light,60,Low,Md,L,5
T53,Test-set contamination audit of healthcare LLM benchmarks,Methodology,database+paper,Y,Y,60,Low,Md,L,5
T74,Open structured-metadata dataset of LLM-eval papers,Meta,dataset,Y,Light,60,Low,Lg,L,5
"""

# Top-10 seed used by the MVP run. (Subset of universe; one row per topic with rich keywords.)
TOPICS_SEED = """topic_id,title,category,keywords,synonyms,negative_keywords,target_artifact,prelim_priority
T10,Reproducibility audit of LLM-judge papers,meta,"LLM-as-a-judge|reproducibility|methodology disclosure|evaluation","LLM judge;automatic evaluator;LLM evaluator;model-based evaluation","tutorial;workshop summary",database+paper,5
T04,Prompt-template sensitivity benchmark for clinical-domain LLM judges,eval,"LLM judge|prompt template sensitivity|clinical NLP|robustness","clinical question answering;medical QA;judge prompt;evaluator prompt","general chatbot",benchmark+tool,5
T53,Test-set contamination audit of healthcare LLM benchmarks,methodology,"data contamination|benchmark leakage|MedQA|PubMedQA|MMLU clinical","training data leakage;memorization;n-gram overlap","unrelated NLP",empirical+database,5
T74,Open structured-metadata dataset of LLM-eval papers,meta,"LLM evaluation methodology|metadata|systematic mapping","evaluation survey;benchmarking practices","tutorial",dataset,5
T37,Clinical-guideline consistency across LLM versions over time,healthcare,"clinical guideline|model drift|LLM versioning|longitudinal evaluation","USPSTF;CDC guidelines;NICE;medical advice consistency","drug discovery",empirical,5
T07,Judge robustness to candidate-side prompt injection,eval+safety,"prompt injection|LLM judge|adversarial robustness","jailbreak;evaluator manipulation","general red teaming",benchmark,5
T11,Format sensitivity benchmark on LLM evaluations,prompt,"format sensitivity|JSON YAML prose|benchmark variance","output format;structured output","unrelated UI",benchmark,4
T17,Tokenization-induced leaderboard variance,eval,"tokenizer|BPE|leaderboard variance|evaluation noise","subword;encoding effects","compiler tokenizers",empirical,4
T25,Hallucination taxonomy: RAG vs no-RAG,rag,"retrieval augmented generation|hallucination taxonomy|faithfulness","grounded generation;citation correctness","unrelated retrieval",taxonomy+paper,4
T43,Reproducibility audit of clinical LLM papers,meta+healthcare,"clinical LLM|reproducibility|methodology disclosure","medical NLP;clinical NLP","drug docking",database+paper,5
"""

VENUE_MASTER = """venue,type,credibility_prelim,apc_status_VERIFY,timeline_VERIFY,fit,notes,source_url
TMLR,journal,high,no_APC_VERIFY,rolling_VERIFY,excellent,primary,https://jmlr.org/tmlr/
ACL Findings,conf,high,free,cycle_bound,excellent,,https://www.aclweb.org/
EMNLP Findings,conf,high,free,cycle_bound,excellent,,https://2024.emnlp.org/
NeurIPS Datasets and Benchmarks,conf_track,high,free,annual_VERIFY,excellent,,https://neurips.cc/
ML4H,workshop,high,free,annual_VERIFY,excellent,healthcare workshop,https://ml4health.github.io/
MLHC,conf,high,reg_fee_VERIFY,annual_VERIFY,excellent,,https://www.mlforhc.org/
JAMIA Open,journal,high,APC_VERIFY,months_VERIFY,good,,https://academic.oup.com/jamiaopen
JMIR,journal,high,APC_VERIFY,weeks_VERIFY,good,not free,https://www.jmir.org/
PLOS Digital Health,journal,med-high,APC_VERIFY,months_VERIFY,good,,https://journals.plos.org/digitalhealth/
npj Digital Medicine,journal,high,APC_VERIFY,months_VERIFY,good,,https://www.nature.com/npjdigitalmed/
ACM Computing Surveys,journal,very_high,APC_VERIFY,slow_VERIFY,survey only,,https://csur.acm.org/
"""

SCORING_RUBRIC = """# Scoring rubric

For each topic, score 1–5 on each factor below.

Factors:
- A Trend strength
- B Audience size
- C Gap clarity
- D Reusability
- E Bench/dataset potential
- F Tool potential
- G Survey/taxonomy potential
- H Venue availability
- I Speed to submission
- J No-APC likelihood
- K Profile fit
- L NIW value
- M EB-1A value
- N Career/FAANG
- O Crowded risk
- P Weak-novelty risk
- Q Private-data dependency
- R IP/employer risk
- S Verifiability ease
- T Collab dependency
- U Reproducibility
- V Public-artifact potential
- W Ethics/legal
- X Reviewer interest

Composites:

```
CitationPotential = 1.5*A + 1.5*B + 2*C + 1.5*D + X
ExecFeasibility   = 2*I + 1.5*K + 1.5*S + U - 1.5*Q - 1.5*T
ImmigrationValue  = 1.5*L + 1.5*M + 1.2*V + 0.5*D
CareerValue       = 1.5*N + V + 0.5*F + 0.5*D
PublicationPath   = 1.5*H + 1.5*J + I - P
RiskPenalty       = O + P + 1.5*Q + 2*R + 0.5*W + 0.5*T

Overall = 0.30*CitationPotential
        + 0.20*ExecFeasibility
        + 0.20*ImmigrationValue
        + 0.10*CareerValue
        + 0.20*PublicationPath
        - 0.40*RiskPenalty
```

All scores PRELIMINARY until evidence-based scoring runs in `scripts/05_score_topics.py`.
"""


def main() -> int:
    make_folders()

    # Templates
    template_dir = REPO_ROOT / "templates"
    for name, body in TEMPLATES.items():
        write_if_missing(template_dir / name, body)

    # Top-level docs
    write_if_missing(REPO_ROOT / "README.md", README)
    write_if_missing(REPO_ROOT / "DECISIONS.md", DECISIONS)
    write_if_missing(REPO_ROOT / ".gitignore", GITIGNORE)
    write_if_missing(REPO_ROOT / "00_admin" / "ip_safety_rules.md", IP_RULES)
    write_if_missing(REPO_ROOT / "00_admin" / "goals.md", GOALS)
    write_if_missing(REPO_ROOT / "00_admin" / "weekly_review_log.md", WEEKLY_REVIEW)

    # Starter CSVs
    write_if_missing(REPO_ROOT / "01_topic_discovery" / "topic_universe.csv", TOPIC_UNIVERSE)
    write_if_missing(REPO_ROOT / "data" / "topics_seed.csv", TOPICS_SEED)
    write_if_missing(REPO_ROOT / "05_venue_selection" / "venue_master.csv", VENUE_MASTER)
    write_if_missing(REPO_ROOT / "04_topic_scoring" / "scoring_rubric.md", SCORING_RUBRIC)

    print(f"Repo scaffolded at: {REPO_ROOT}")
    print(f"Folders created: {len(FOLDERS)}")
    print(f"Templates created: {len(TEMPLATES)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
