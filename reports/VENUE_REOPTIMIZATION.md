# Venue + Topic + Title Re-Optimization
## After user clarification 2026-05-16

The user clarified two distinct optimization targets:

1. **Bridge**: optimize for **shortest submission-to-publication time** at a free venue.
2. **High-citation**: optimize **topic + title + venue** for max citations at a free venue.

This document is the re-analysis. It supersedes earlier venue choices in
`BRIDGE_PUBLICATION_STRATEGY.md` and tightens `HIGH_CITATION_STRATEGY.md` §5.

---

## Part 1 — Bridge venue (fast submission-to-publication)

### The candidates, ranked by submission-to-publication time (free venues only)

| Venue | Sub → Pub | Free? | Notes |
|---|---|---|---|
| **NeurIPS / ICML / ICLR / ACL / EMNLP workshop** | **1.5–3 mo** | Yes | Annual cycle; ACL Anthology / OpenReview indexed |
| JOSS (software paper) | 1–3 mo | Yes | CrossRef + GS; **software contributions only** — not for empirical findings |
| ML Reproducibility Challenge | 2–4 mo | Yes | TMLR proceedings |
| TMLR (main paper) | 3–5 mo | Yes | Rolling; no deadline; predictable |
| TMLR (Survey Certification) | 3–6 mo | Yes | For surveys |
| ACL / EMNLP Findings (via ARR) | 4–6 mo | Yes | Two-stage (ARR + commitment) |
| Conference main track | 5–7 mo | Yes | Most prestigious; slowest |
| NeurIPS Datasets & Benchmarks | 6–8 mo | Yes | Annual full conference |
| ACM Computing Surveys | 8–18 mo | Yes (Green OA) | Surveys only |
| JMLR | 12–24 mo | Yes | Very slow, very high prestige |

### Recommendation: top-conference workshop for T02

**Primary**: **EMNLP 2026 Workshop** (Eval4NLP, BlackboxNLP, GenBench, or TrustNLP).
- Submission: ~2026-08-15 (~3 months from today)
- Decision: ~2026-10-15
- Camera-ready: ~2026-11-15
- Workshop / publication: ~2026-12-10
- **Submission-to-publication: ~3.5 months**
- 8-page format (long paper) or 4-page (short paper) — fits T02
- Free; peer-reviewed; ACL Anthology indexed
- Counts as peer-reviewed publication for NIW and EB-1A criterion (vi)

**Backup 1**: NeurIPS 2026 Safety Workshop (or similar)
- Submission: ~2026-09-15
- Workshop: 2026-12 (mid-month)
- Submission-to-publication: ~3 months

**Backup 2**: TMLR direct
- Submission anytime
- Submission-to-publication: ~3–5 months
- Slightly more prestige than workshop; slightly slower; predictable

**Backup 3**: ICLR 2027 workshop
- Submission ~2027-02
- Publication ~2027-04
- Faster sub→pub (~2 months) but later publication date overall

### Why workshop over TMLR for the bridge specifically

The user's metric is **submission-to-publication time**, not total elapsed.

| Dimension | EMNLP Workshop | TMLR direct |
|---|---|---|
| Submission-to-publication | **3.5 mo** ✅ | 3–5 mo |
| Drafting effort (page count) | 8 pages ✅ | 8–12 pages |
| Deadline pressure | Hard (Aug 15) | None (rolling) |
| Prestige (per-paper) | Workshop | Journal |
| Free? | Yes | Yes |
| Indexing | ACL Anthology + DBLP + GS | DBLP + GS + OpenReview |
| USCIS recognised? | Yes | Yes |
| Citation ceiling | Lower (~30–80) | Higher (~80–150) |

For a **bridge** paper whose role is "lock in a peer-reviewed publication FAST"
(not to be the citation centre), the workshop wins on the user's stated metric.

The citation work is done by the survey, not by T02. T02's role is publication
count, fastest possible.

### What we lose by going workshop instead of TMLR

- ~50 fewer expected citations on T02 (workshop ceiling ~80, TMLR ceiling ~150)
- Slightly less prestige per-paper
- BUT: T02's results still get cited via the survey §6.1 case study
- AND: The arXiv preprint accumulates citations regardless of venue

### What we keep

- Same publication month (December 2026)
- Same author-effort budget
- Same scientific content
- Faster declared "publication" date for petitions

---

## Part 2 — High-citation paper (topic + title + venue)

### Topic re-evaluation

Three candidate topics, scored on citation potential:

| Topic | Citation ceiling (3yr, solo, free venue) | Probability of acceptance | Match with user identity |
|---|---|---|---|
| **A. LLM-as-Judge survey** (current plan) | 500–1500 | High (60–75%) | Perfect (JudgeSense + T02 directly feed it) |
| B. Broader LLM Reliability survey | 800–2500 | Medium (40–55%) | Good (broader, but more competition) |
| C. New benchmark "JudgeBench" | 1000–3000 IF adopted | Low (20–30%) | Good but engineering-heavy |
| D. Position paper "Towards Trustworthy Judges" | 200–5000 (very variable) | Medium (30–50%) | Good but high variance |

**Recommendation**: **A — Keep LLM-as-Judge survey**.

Reasons:
1. **Highest probability of becoming THE canonical reference.** Surveys that become "the default cite" hit 500+ reliably. A broader survey competes with Chang et al. 2023 (~1,500 cit) and is unlikely to displace it. A narrower survey on LLM-as-Judge has no top-venue competitor.
2. **JudgeSense + T02 + T07 directly feed it** as case studies — empirical authority compounds.
3. **Solo executability**: 70 pages on LLM-as-Judge is one focused author-year; 150 pages on broader "LLM reliability" is two author-years.
4. **The ceiling (1500) is plenty** for the 500-citation target. Optimizing past 500 → 1500 is diminishing returns vs the survey path's probability.

### Title re-optimization

Current title: *"LLM-as-Judge: A Comprehensive Survey of Methods, Failure Modes, and Evaluation Frameworks"*

This title is fine but not optimal for citations. Highly-cited surveys share traits:
- Memorable hook (alliteration, wordplay, question form, or evocative phrase)
- Topic keyword present (search discoverability)
- "Survey" or "Comprehensive" signals completeness
- Under 12 words (citation managers truncate long titles)

#### Title candidates (ranked)

1. **"Judging the Judges: A Comprehensive Survey of LLM-as-a-Judge"** ⭐
   - Memorable hook (alliteration + concept inversion)
   - Topic keyword: LLM-as-a-Judge
   - "Comprehensive Survey" signal
   - 11 words
   - Sounds quotable
2. **"On the Reliability of LLM-as-a-Judge: A Comprehensive Survey"**
   - Academic tone
   - "On the" opening signals foundational paper
   - 10 words
3. **"A Survey of LLM-as-a-Judge: Methods, Failures, and the Road Ahead"**
   - Promises three things (good for content positioning)
   - 12 words
   - Slightly less hook
4. **"LLM-as-a-Judge: A Survey of Methods, Failure Modes, and Defences"**
   - Workmanlike
   - Explicit promise of coverage

**Recommendation**: Title #1 ("Judging the Judges") for primary submission.
If reviewers object to the catchy phrasing as unscientific, fall back to #2.

### Venue re-evaluation for max citations

| Venue | APC | Sub → Pub | Citation ceiling (3yr) | Reach | Author-status gate |
|---|---|---|---|---|---|
| **TMLR (Survey Certification)** | $0 | 3–6 mo | 500–1500 | ML + NLP communities | None |
| ACM Computing Surveys | $0 (Green OA) | 8–18 mo | 800–2500 | Broad CS | High (favours established PIs) |
| JMLR | $0 | 12–24 mo | 500–2000 | ML community | High |
| Foundations and Trends in ML | $0 (invited) | 6–12 mo | 800–3000 | ML community | Very high (invitation usually) |

#### The earlier-publication advantage

Citation accumulation is roughly linear in time. A paper published August 2027
at TMLR has **6 more months** to accumulate citations by August 2030 than the
same paper published February 2028 at ACM CS.

At ~50–150 citations/year for a successful comprehensive survey, 6 months earlier
publication is worth **25–75 additional citations** in any time-window comparison.

#### Recommendation: TMLR Survey Certification as primary

- **Free** ✓
- **Fast for a journal** (3–6 months vs ACM CS 8–18 months) → more time for citations
- **No author-status gate** ✓ (critical for solo first-time author)
- **Indexed** ✓ (DBLP, Google Scholar, OpenReview)
- **USCIS-recognised** ✓
- **HELM precedent** at TMLR: 1,500+ citations achieved

Fallback chain unchanged: TMLR → ACM CS → JMLR → CL journal → arXiv-only.

---

## Part 3 — Combined recommendation (lock in)

### Bridge paper

| Field | Value |
|---|---|
| Project | T02 (Position-bias quantification across judge models) |
| Title | *Position Bias in LLM Judges: A Cross-Model Quantification* (current; suitable) |
| Venue (primary) | **EMNLP 2026 Workshop** (Eval4NLP target) |
| Venue (backup 1) | NeurIPS 2026 Safety Workshop |
| Venue (backup 2) | TMLR direct |
| Submission target | 2026-08-15 (EMNLP workshop deadline) |
| Publication target | 2026-12 (~3.5 mo sub→pub) |
| Citation target | 30–80 (3yr) |
| Role | Publication count #1; Survey §6.1 case study |

### High-citation paper

| Field | Value |
|---|---|
| Project | SURVEY_llm_judge |
| Title | **"Judging the Judges: A Comprehensive Survey of LLM-as-a-Judge"** |
| Venue (primary) | **TMLR Survey Certification** |
| Venue (backup 1) | ACM Computing Surveys |
| Venue (backup 2) | JMLR |
| Venue (backup 3) | Computational Linguistics journal |
| Backup-of-backup | arXiv-only with annual updates |
| Submission target | 2027-02-15 |
| Publication target | 2027-08 (~6 mo sub→pub) |
| Citation target | 500+ (3yr post-publication) |

### What this combined plan delivers

| Date | Event |
|---|---|
| 2026-08-15 | T02 submitted to EMNLP 2026 Workshop + arXiv preprint posted |
| 2026-10-15 | T02 workshop notification |
| 2026-12 | **T02 published** (publication #1) |
| 2027-02-15 | Survey submitted to TMLR Survey Certification + arXiv preprint |
| 2027-08 | **Survey published** (publication #2; the citation engine) |
| 2030-08 (3yr post-pub) | Survey: target 500+ citations |

---

## Part 4 — What was rejected and why

### Rejected: TMLR for the bridge
- Slower sub→pub (3–5 mo) than workshop (3–4 mo)
- More drafting effort (longer page allowance gets used)
- Same publication month either way (Dec 2026)
- Prestige delta does not justify the speed cost for "publication count" purpose

### Rejected: Broader LLM Reliability survey
- Citation ceiling slightly higher but probability of becoming canonical reference much lower
- Competes with Chang et al. 2023 (~1,500 cit, ACM TIST) directly
- More work, worse expected value

### Rejected: Building a new benchmark instead of a survey
- Higher ceiling IF adopted (~3,000 cit) but very low probability of adoption for solo author
- Engineering-heavy (12-18 months) vs reading-heavy (10-12 months)
- Adoption requires marketing capacity a solo author rarely has

### Rejected: ACM Computing Surveys or JMLR as PRIMARY for survey
- 6 months later publication = 25–75 fewer citations in any time-window
- Higher author-status gate (favours established PIs)
- Kept as fallback if TMLR rejects

### Rejected: paid open-access journals
- Violates the free-venue constraint
- Universally lower reviewer trust in ML

---

## Part 5 — Documents to update (action list)

This document spawns updates to:

- `06_paper_pipeline/T02_position_bias/PROTOCOL.md` — change venue from TMLR-direct to EMNLP workshop; adjust week 9 milestone
- `06_paper_pipeline/T02_position_bias/BRIDGE_SPRINT.md` — week 9 submission target changes
- `06_paper_pipeline/SURVEY_llm_judge/PROTOCOL.md` — update title; reaffirm TMLR
- `06_paper_pipeline/SURVEY_llm_judge/SURVEY_STRUCTURE.md` — update title in header
- `06_paper_pipeline/SURVEY_llm_judge/VENUE_ANALYSIS.md` — already TMLR-primary, just confirm
- `reports/COORDINATION.md` — update calendar with new milestones
- `reports/HIGH_CITATION_STRATEGY.md` — append a §5 update noting the title change
- `DECISIONS.md` — log the venue + title changes
- `NEXT_90_DAYS.md` — week 9 deliverable changes (workshop submission, not TMLR)
- `05_venue_selection/SUBMISSION_CALENDAR_2026-2027.md` — verify EMNLP workshop dates
- `data/scoop_watch_queries.json` — no changes; competitors monitored unchanged
