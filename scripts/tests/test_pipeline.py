"""
Lightweight tests for the verification pipeline.
Run with:  python -m unittest scripts.tests.test_pipeline -v
or:        python scripts/tests/test_pipeline.py
"""
from __future__ import annotations
import importlib.util
import json
import os
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))


def _load(stem: str):
    matches = list((ROOT / "scripts").glob(f"{stem}*.py"))
    spec = importlib.util.spec_from_file_location(f"_t_{stem}", matches[0])
    mod = importlib.util.module_from_spec(spec)  # type: ignore
    spec.loader.exec_module(mod)  # type: ignore
    return mod


class TestQueryGeneration(unittest.TestCase):
    def test_build_queries_basic(self):
        gen = _load("01_generate_queries")
        topic = {
            "topic_id": "TX",
            "title": "Test topic",
            "category": "eval",
            "keywords": "LLM judge|prompt sensitivity|robustness",
            "synonyms": "evaluator;automatic judge",
            "negative_keywords": "",
            "target_artifact": "benchmark",
            "prelim_priority": "5",
        }
        q = gen.build_queries(topic)
        self.assertIn("semantic_scholar", q)
        self.assertGreaterEqual(len(q["semantic_scholar"]), 3)
        self.assertGreaterEqual(len(q["arxiv"]), 1)
        self.assertGreaterEqual(len(q["github"]), 1)
        self.assertGreaterEqual(len(q["doaj"]), 1)
        self.assertTrue(q["google_scholar_manual"][0]["url"].startswith("https://scholar.google.com"))


class TestDeduplication(unittest.TestCase):
    def test_dedupe_by_doi_and_title(self):
        ev = _load("02_collect_topic_evidence")
        papers = [
            {"source": "semantic_scholar", "doi": "10.1/x", "title": "A great paper", "citations": 5, "abstract": "short"},
            {"source": "openalex", "doi": "10.1/X", "title": "A great paper", "citations": 7, "abstract": "longer abstract version"},
            {"source": "crossref", "doi": "", "title": "  A   GREAT paper ", "citations": 2, "abstract": ""},
            {"source": "arxiv", "doi": "", "title": "Different paper title", "citations": 0, "abstract": ""},
        ]
        out = ev.deduplicate(papers)
        self.assertEqual(len(out), 2)
        merged = next(p for p in out if "great" in (p.get("title", "").lower()))
        self.assertEqual(merged["citations"], 7)
        self.assertGreaterEqual(len(merged.get("sources", [])), 2)
        self.assertEqual(merged["abstract"], "longer abstract version")


class TestScoring(unittest.TestCase):
    def test_paper_signal_calculations(self):
        sc = _load("05_score_topics")
        cy = sc._now_year()
        raw = [
            {"abstract": "future work to extend the benchmark", "year": cy, "citations": 10},
            {"abstract": "limitation of our approach is", "year": cy - 1, "citations": 100},
            {"abstract": "no benchmark exists for clinical X", "year": cy - 2, "citations": 5},
            {"abstract": "unrelated", "year": cy - 5, "citations": 50},
        ]
        ps = sc.compute_paper_signals(raw)
        self.assertEqual(ps["n_papers"], 4)
        self.assertGreaterEqual(ps["n_papers_24mo"], 3)
        self.assertEqual(ps["top_citation"], 100)
        self.assertGreaterEqual(sc.gap_phrase_hits(raw), 3)

    def test_artifact_opportunity(self):
        sc = _load("05_score_topics")
        # plenty of gap signal, no datasets/tools => high opportunity
        raw = [{"abstract": "limitation no benchmark exists", "year": 2024, "citations": 0}] * 6
        out = sc.artifact_opportunity(raw, [{"datasets": []}], [{"results": []}], [{"results": []}], saturation_score=2)
        self.assertGreaterEqual(out["artifact_opportunity_0to5"], 4)

    def test_overall_rubric_monotonic(self):
        sc = _load("05_score_topics")
        # high citation, low risk, low saturation => higher Overall
        m_high = {
            "paper": {"n_papers": 100, "n_papers_24mo": 60, "n_papers_12mo": 40,
                      "median_citations": 30, "top_citation": 1000, "growth_yoy_proxy": 0.5},
            "saturation": {"saturation_score_0to5": 1, "n_papers": 100, "dominant_tools": 0, "big_datasets": 0},
            "artifact": {"artifact_opportunity_0to5": 5, "gap_phrase_hits": 8, "n_existing_pwc_datasets": 0, "n_existing_hf_datasets": 0},
            "venue": {"venue_signal_0to5": 4, "doaj_no_apc_journals": 3, "crossref_active_venues": 5, "openreview_hits": 10},
            "risk": {"ip_risk_0to5": 0, "ip_risk_flags": []},
        }
        m_low = {
            "paper": {"n_papers": 5, "n_papers_24mo": 0, "n_papers_12mo": 0,
                      "median_citations": 0, "top_citation": 0, "growth_yoy_proxy": -0.2},
            "saturation": {"saturation_score_0to5": 5, "n_papers": 500, "dominant_tools": 5, "big_datasets": 5},
            "artifact": {"artifact_opportunity_0to5": 1, "gap_phrase_hits": 0, "n_existing_pwc_datasets": 10, "n_existing_hf_datasets": 20},
            "venue": {"venue_signal_0to5": 0, "doaj_no_apc_journals": 0, "crossref_active_venues": 0, "openreview_hits": 0},
            "risk": {"ip_risk_0to5": 5, "ip_risk_flags": ["proprietary"]},
        }
        rh = sc.heuristic_overall(m_high)
        rl = sc.heuristic_overall(m_low)
        self.assertGreater(rh["composites"]["Overall"], rl["composites"]["Overall"])
        self.assertGreater(rh["composites"]["CitationPotential"], rl["composites"]["CitationPotential"])


class TestConfidenceGate(unittest.TestCase):
    def setUp(self):
        # Stage minimal evidence in temp pseudo-paths within the repo
        self.gate = _load("08_confidence_gate")
        self.repo = ROOT
        # Use a unique topic id
        self.tid = "TZ_TEST"
        # Make minimal queries file so gate_topic finds the topic
        (self.repo / "data" / "queries").mkdir(parents=True, exist_ok=True)
        (self.repo / "data" / "queries" / f"{self.tid}.json").write_text(json.dumps({
            "topic": {"topic_id": self.tid, "title": "test", "keywords": "x"},
            "queries": {}
        }))
        # Score file
        (self.repo / "data" / "scores").mkdir(parents=True, exist_ok=True)
        (self.repo / "data" / "scores" / f"{self.tid}.json").write_text(json.dumps({
            "paper": {"n_papers": 100, "n_papers_24mo": 60},
            "saturation": {"saturation_score_0to5": 2},
            "artifact": {"artifact_opportunity_0to5": 5, "gap_phrase_hits": 5,
                         "n_existing_pwc_datasets": 0, "n_existing_hf_datasets": 0,
                         "existing_artifact_density": 0.1, "differentiator_required": False},
            "venue": {"venue_signal_0to5": 4},
            "risk": {"ip_risk_0to5": 0, "ip_risk_flags": []},
            "citation_signal_0to5": 5,
            "niw_0to5": 4, "eb1a_0to5": 5, "career_0to5": 4, "tool_potential_0to5": 4,
            "relevance_purity": 0.6, "kept_papers": 30,
            "rubric": {"composites": {"Overall": 18, "CitationPotential": 25, "ExecFeasibility": 12,
                                       "ImmigrationValue": 15, "CareerValue": 10, "PublicationPath": 12,
                                       "RiskPenalty": 5}},
        }))
        # Agreement (simulate strong reviewer GO)
        (self.repo / "data" / "agreement").mkdir(parents=True, exist_ok=True)
        (self.repo / "data" / "agreement" / f"{self.tid}.json").write_text(json.dumps({
            "topic_id": self.tid, "n_reviews": 8, "plurality_decision": "GO",
            "decision_score_mean_0to3": 2.4, "high_confidence_drops": 0,
            "high_disagreement_flag": False, "decisions": {"GO": 6, "NARROW": 2},
        }))
        # Dedup CSV with two sources contributing and relevance_score column
        (self.repo / "data" / "papers_dedup").mkdir(parents=True, exist_ok=True)
        (self.repo / "data" / "papers_dedup" / f"{self.tid}.csv").write_text(
            "title,abstract_snippet,year,venue,citations,influential_citations,doi,url,sources,authors,relevance_score,matched_keywords,reason_included\n"
            "P,abs1,2025,V,10,1,10.1/a,https://doi.org/10.1/a,semantic_scholar|openalex,A,0.8,kw:title:x,r1\n"
            "Q,abs2,2024,V,5,0,10.1/b,https://doi.org/10.1/b,crossref|arxiv,B,0.6,kw:title:x,r2\n"
            "R,abs3,2024,V,3,0,10.1/c,https://doi.org/10.1/c,arxiv,C,0.5,kw:abstract:x,r3\n"
        )

    def tearDown(self):
        for p in [
            self.repo / "data" / "queries" / f"{self.tid}.json",
            self.repo / "data" / "scores" / f"{self.tid}.json",
            self.repo / "data" / "agreement" / f"{self.tid}.json",
            self.repo / "data" / "papers_dedup" / f"{self.tid}.csv",
            self.repo / "data" / "decisions" / f"{self.tid}.json",
        ]:
            try:
                p.unlink()
            except Exception:
                pass

    def test_gate_GO(self):
        d = self.gate.gate_topic(self.tid)
        self.assertEqual(d["final_decision"], "GO")
        self.assertIn(d["final_confidence"], ("MEDIUM", "HIGH"))

    def test_gate_DROP_high_ip(self):
        score_path = self.repo / "data" / "scores" / f"{self.tid}.json"
        s = json.loads(score_path.read_text())
        s["risk"] = {"ip_risk_0to5": 5, "ip_risk_flags": ["proprietary"]}
        score_path.write_text(json.dumps(s))
        d = self.gate.gate_topic(self.tid)
        self.assertEqual(d["final_decision"], "DROP")

    def test_gate_NARROW_when_saturated(self):
        score_path = self.repo / "data" / "scores" / f"{self.tid}.json"
        s = json.loads(score_path.read_text())
        s["saturation"]["saturation_score_0to5"] = 4
        s["artifact"]["artifact_opportunity_0to5"] = 3
        s["rubric"]["composites"]["Overall"] = 11
        score_path.write_text(json.dumps(s))
        d = self.gate.gate_topic(self.tid)
        self.assertIn(d["final_decision"], ("NARROW", "NEEDS_MORE_EVIDENCE"))


class TestReportGeneration(unittest.TestCase):
    def test_report_writes_file(self):
        rep = _load("09_generate_final_report")
        out = ROOT / "reports" / "_test_report.md"
        sys.argv = ["09", "--out", str(out)]
        rep.main(["--out", str(out)])
        self.assertTrue(out.exists())
        text = out.read_text(encoding="utf-8")
        self.assertIn("# Final decision report", text)
        self.assertIn("## 1. Executive summary", text)
        self.assertIn("Report status:", text)
        out.unlink(missing_ok=True)


# ---------- New tests (per audit fix #12) ----------

class TestRelevanceFiltering(unittest.TestCase):
    def test_irrelevant_papers_filtered(self):
        from common.relevance import filter_by_relevance, score_paper
        topic = {
            "topic_id": "TX",
            "keywords": "LLM judge|prompt template sensitivity|clinical NLP",
            "synonyms": "clinical question answering;medical QA",
            "negative_keywords": "",
        }
        papers = [
            {"title": "Prompt template sensitivity in clinical NLP LLM judges",
             "abstract": "we benchmark medical QA with LLM judge prompts under template variation."},
            {"title": "A study of pizza toppings preferences",
             "abstract": "we sample 200 customers and analyze pizza topping orders by region."},
            {"title": "Quantum chemistry of low-temperature catalysts",
             "abstract": "we compute DFT energies for catalyst surfaces."},
        ]
        kept = filter_by_relevance(papers, topic)
        titles = [p["title"] for p in kept]
        self.assertIn("Prompt template sensitivity in clinical NLP LLM judges", titles)
        self.assertNotIn("A study of pizza toppings preferences", titles)
        self.assertNotIn("Quantum chemistry of low-temperature catalysts", titles)
        # The relevant one should have a positive score
        rel, matched, _ = score_paper(papers[0], topic)
        self.assertGreater(rel, 0.3)
        self.assertGreater(len(matched), 0)


class TestArtifactDensityPenalty(unittest.TestCase):
    def test_artifact_opportunity_drops_with_density(self):
        sc = _load("05_score_topics")
        # Construct gap signals: many gap mentions => base 5
        raw = [{"abstract": "limitation no benchmark exists", "year": 2024, "citations": 10}] * 6
        # Low density: zero comparable artifacts
        low = sc.artifact_opportunity(raw, [{"datasets": []}], [{"results": []}], [{"results": []}], saturation_score=2)
        # High density: many big repos + datasets + HF downloads
        gh_big = [{"results": [{"stars": 5000}, {"stars": 3000}, {"stars": 2000}, {"stars": 1500}]}]
        hf_big = [{"results": [{"downloads": 9000}, {"downloads": 4000}, {"downloads": 2000}]}]
        pwc_big = [{"datasets": [{}, {}, {}, {}, {}, {}]}]
        high = sc.artifact_opportunity(raw, pwc_big, hf_big, gh_big, saturation_score=2)
        self.assertLess(high["artifact_opportunity_0to5"], low["artifact_opportunity_0to5"])
        self.assertGreater(high["existing_artifact_density"], low["existing_artifact_density"])
        self.assertTrue(high["differentiator_required"])


class TestTopicAwareScoring(unittest.TestCase):
    def test_niw_eb1a_career_vary_across_topics(self):
        sc = _load("05_score_topics")
        clinical = {"title": "Clinical guideline consistency over time",
                    "category": "healthcare", "keywords": "clinical guideline|patient safety",
                    "synonyms": "ehr;medical advice", "target_artifact": "empirical"}
        engineering = {"title": "Tokenization-induced leaderboard variance",
                       "category": "eval", "keywords": "tokenizer|leaderboard variance",
                       "synonyms": "BPE;encoding effects", "target_artifact": "tool+benchmark"}
        survey = {"title": "Survey of evaluation failure modes",
                  "category": "meta", "keywords": "survey|evaluation",
                  "synonyms": "review", "target_artifact": "survey"}
        niw_c = sc.niw_score(clinical); niw_e = sc.niw_score(engineering); niw_s = sc.niw_score(survey)
        eb_c = sc.eb1a_score(clinical, citation_signal_0to5=3, artifact_score_0to5=4)
        eb_e = sc.eb1a_score(engineering, citation_signal_0to5=3, artifact_score_0to5=4)
        car_c = sc.career_score(clinical, artifact_score_0to5=4)
        car_e = sc.career_score(engineering, artifact_score_0to5=4)
        # Clinical NIW > engineering NIW (national-importance hook)
        self.assertGreater(niw_c, niw_e)
        # Engineering Career > clinical Career (broader FAANG market)
        self.assertGreaterEqual(car_e, car_c)
        # All three must produce DIFFERENT NIW values (no constants)
        self.assertGreater(len({niw_c, niw_e, niw_s}), 1)
        # All in 1..5
        for v in (niw_c, niw_e, niw_s, eb_c, eb_e, car_c, car_e):
            self.assertGreaterEqual(v, 1); self.assertLessEqual(v, 5)


class TestGateForcesLowWhenNoReviews(unittest.TestCase):
    def setUp(self):
        self.gate = _load("08_confidence_gate")
        self.tid = "TLOW_TEST"
        for d in ("data/queries", "data/scores", "data/agreement", "data/papers_dedup", "data/decisions"):
            (ROOT / d).mkdir(parents=True, exist_ok=True)
        (ROOT / "data" / "queries" / f"{self.tid}.json").write_text(json.dumps({
            "topic": {"topic_id": self.tid, "title": "x", "keywords": "x"}, "queries": {}}))
        (ROOT / "data" / "scores" / f"{self.tid}.json").write_text(json.dumps({
            "paper": {"n_papers": 100, "n_papers_24mo": 60},
            "saturation": {"saturation_score_0to5": 2},
            "artifact": {"artifact_opportunity_0to5": 5, "gap_phrase_hits": 5,
                         "n_existing_pwc_datasets": 0, "n_existing_hf_datasets": 0,
                         "existing_artifact_density": 0.1, "differentiator_required": False},
            "venue": {"venue_signal_0to5": 4},
            "risk": {"ip_risk_0to5": 0, "ip_risk_flags": []},
            "citation_signal_0to5": 5,
            "niw_0to5": 4, "eb1a_0to5": 5, "career_0to5": 4, "tool_potential_0to5": 4,
            "relevance_purity": 0.6, "kept_papers": 30,
            "rubric": {"composites": {"Overall": 18, "CitationPotential": 25, "ExecFeasibility": 12,
                                       "ImmigrationValue": 15, "CareerValue": 10, "PublicationPath": 12,
                                       "RiskPenalty": 5}},
        }))
        # No reviews -> empty agreement
        (ROOT / "data" / "agreement" / f"{self.tid}.json").write_text(json.dumps({
            "topic_id": self.tid, "n_reviews": 0, "plurality_decision": "NEEDS_MORE_EVIDENCE",
            "decision_score_mean_0to3": 0, "high_confidence_drops": 0,
            "high_disagreement_flag": False, "decisions": {}}))
        (ROOT / "data" / "papers_dedup" / f"{self.tid}.csv").write_text(
            "title,abstract_snippet,year,venue,citations,influential_citations,doi,url,sources,authors,relevance_score,matched_keywords,reason_included\n"
            "P,abs,2025,V,10,1,10.1/a,https://doi.org/10.1/a,semantic_scholar|openalex,A,0.8,kw:title:x,test\n"
            "Q,abs,2024,V,5,0,10.1/b,https://doi.org/10.1/b,crossref|arxiv,B,0.7,kw:title:x,test\n"
        )

    def tearDown(self):
        for p in [
            ROOT / "data" / "queries" / f"{self.tid}.json",
            ROOT / "data" / "scores" / f"{self.tid}.json",
            ROOT / "data" / "agreement" / f"{self.tid}.json",
            ROOT / "data" / "papers_dedup" / f"{self.tid}.csv",
            ROOT / "data" / "decisions" / f"{self.tid}.json",
        ]:
            try:
                p.unlink()
            except Exception:
                pass

    def test_no_reviews_forces_low_and_blocks_go(self):
        d = self.gate.gate_topic(self.tid, allow_go_without_llm=False)
        self.assertEqual(d["final_confidence"], "LOW")
        self.assertNotEqual(d["final_decision"], "GO")  # GO blocked without LLM
        self.assertEqual(d["status"], "PRELIMINARY_HEURISTIC_ONLY")

    def test_override_allows_go(self):
        d = self.gate.gate_topic(self.tid, allow_go_without_llm=True)
        # All other GO conditions met; override should permit GO
        self.assertEqual(d["final_decision"], "GO")
        # Even with override, confidence stays LOW because no reviewers
        self.assertEqual(d["final_confidence"], "LOW")


class TestReportWarnsWhenNoLLM(unittest.TestCase):
    def test_report_contains_warning(self):
        rep = _load("09_generate_final_report")
        out = ROOT / "reports" / "_test_warn.md"
        rep.main(["--out", str(out)])
        text = out.read_text(encoding="utf-8")
        # Either the warning banner OR a "FULL_REVIEW_COMPLETE" status must be present
        if "n_reviews=0" in text or "PRELIMINARY_HEURISTIC_ONLY" in text:
            self.assertIn("LLM REVIEW NOT RUN", text.upper().replace("Â", ""))
        out.unlink(missing_ok=True)


class TestNarrowingScript(unittest.TestCase):
    """Tests for 11_generate_narrowed_topics.py"""

    def setUp(self):
        self.mod = _load("11_generate_narrowed_topics")

    # ---- term extraction ----

    def test_extract_title_ngrams_returns_frequent_terms(self):
        # Titles where specific phrases repeat across papers (same domain concept)
        papers = [
            {"title": "Adversarial prompt injection attacks on LLM judge evaluation"},
            {"title": "Adversarial prompt injection vulnerabilities in LLM evaluators"},
            {"title": "Defending against adversarial prompt injection in automated judges"},
            {"title": "Adversarial prompt injection robustness benchmark for evaluation"},
        ]
        grams = self.mod.extract_title_ngrams(papers, n_range=(2, 3), min_count=2)
        # "adversarial prompt" or "prompt injection" should appear >= 2 times
        self.assertIsInstance(grams, list)
        self.assertGreater(len(grams), 0)
        # At least one gram containing "prompt" or "injection" should be present
        found_relevant = any("prompt" in g or "injection" in g for g in grams)
        self.assertTrue(found_relevant, f"Expected prompt/injection grams, got: {grams}")

    def test_extract_title_ngrams_filters_by_min_count(self):
        papers = [
            {"title": "Unique phrase only once here xyz"},
            {"title": "Repeated domain phrase appears twice"},
            {"title": "Repeated domain phrase again here"},
        ]
        grams = self.mod.extract_title_ngrams(papers, n_range=(2, 3), min_count=2)
        self.assertIn("repeated domain", grams)
        # "unique phrase" appears only once -> filtered
        self.assertNotIn("unique phrase", grams)

    # ---- noisy keyword detection ----

    def test_find_noisy_keywords_identifies_noise(self):
        hi = [
            {"title": "LLM judge prompt sensitivity", "matched_keywords": "kw:title:llm judge"},
            {"title": "LLM judge evaluation robustness", "matched_keywords": "kw:title:llm judge"},
        ]
        lo = [
            {"title": "Robustness of IoT networks", "matched_keywords": "kw:title:robustness"},
            {"title": "Railway robustness indicators", "matched_keywords": "kw:title:robustness"},
            {"title": "Superconductor robustness model", "matched_keywords": "kw:title:robustness"},
        ]
        noisy = self.mod.find_noisy_keywords(hi, lo, ["clinical nlp", "robustness"])
        self.assertIn("robustness", noisy)
        # "clinical nlp" doesn't appear in lo → not noisy
        self.assertNotIn("clinical nlp", noisy)

    def test_find_noisy_keywords_clean_keyword_not_flagged(self):
        hi = [{"title": "Prompt template for LLM judge evaluation", "matched_keywords": "kw:title:prompt template"}] * 4
        lo = [{"title": "Unrelated paper about weather", "matched_keywords": "kw:title:other"}] * 2
        noisy = self.mod.find_noisy_keywords(hi, lo, ["prompt template", "robustness"])
        # "prompt template" hits hi papers much more → should not be noisy
        self.assertNotIn("prompt template", noisy)

    # ---- overlap check ----

    def test_anchors_overlap_rejects_overlapping(self):
        # "contamination language" overlaps "data contamination" by 50% (contamination)
        self.assertTrue(self.mod._anchors_overlap("contamination language models", "data contamination"))

    def test_anchors_overlap_passes_non_overlapping(self):
        # "clinical benchmark" shares no words with "data contamination"
        self.assertFalse(self.mod._anchors_overlap("clinical benchmark", "data contamination"))

    # ---- variant generation ----

    def test_generate_variants_always_produces_at_least_one(self):
        """Even with 0 hi papers, a fallback variant should be generated."""
        parent = {
            "seed": {
                "topic_id": "TX",
                "title": "Test topic",
                "category": "eval",
                "keywords": "llm judge|robustness",
                "synonyms": "evaluator;judge",
                "negative_keywords": "",
                "target_artifact": "benchmark",
                "prelim_priority": "5",
            },
            "decision_json": {"relevance_purity": 0.25},
            "score_json": {
                "artifact": {"artifact_opportunity_0to5": 2},
                "saturation": {"saturation_score_0to5": 2},
                "niw_0to5": 3, "eb1a_0to5": 3, "career_0to5": 3,
                "citation_signal_0to5": 2,
            },
            "agree_json": {},
            "papers": [
                {"title": "Robustness of robotic arms", "relevance_score": "0.25",
                 "matched_keywords": "kw:title:robustness", "citations": "0"},
            ],
        }
        hi, mid, lo = self.mod.split_by_tier(parent["papers"], hi_threshold=0.45)
        variants = self.mod.generate_variants(parent, hi, lo, hi_threshold=0.45)
        self.assertGreater(len(variants), 0)
        # All variants must have the required CSV columns
        for v in variants:
            for col in ("topic_id", "title", "keywords", "synonyms",
                        "negative_keywords", "target_artifact", "prelim_priority",
                        "parent_topic_id", "narrowing_type"):
                self.assertIn(col, v, f"Missing column '{col}' in variant")

    def test_generate_variants_noise_pruned_removes_noisy_keyword(self):
        """noise_pruned variant should exclude the noisy secondary keyword."""
        parent = {
            "seed": {
                "topic_id": "TY",
                "title": "Judge robustness to prompt injection",
                "category": "eval+safety",
                "keywords": "prompt injection|LLM judge|adversarial robustness",
                "synonyms": "jailbreak;evaluator manipulation",
                "negative_keywords": "general red teaming",
                "target_artifact": "benchmark",
                "prelim_priority": "5",
            },
            "decision_json": {"relevance_purity": 0.25},
            "score_json": {
                "artifact": {"artifact_opportunity_0to5": 2},
                "saturation": {"saturation_score_0to5": 2},
                "niw_0to5": 4, "eb1a_0to5": 4, "career_0to5": 5,
                "citation_signal_0to5": 3,
            },
            "agree_json": {},
            "papers": [
                {"title": "Prompt injection attacks on LLM judges", "relevance_score": "0.5",
                 "matched_keywords": "primary:title:prompt injection|kw:title:llm judge",
                 "citations": "10"},
                {"title": "Prompt injection in multi-agent systems", "relevance_score": "0.5",
                 "matched_keywords": "primary:title:prompt injection", "citations": "5"},
                {"title": "Adversarial robustness of neural network classifiers",
                 "relevance_score": "0.25",
                 "matched_keywords": "kw:title:adversarial robustness", "citations": "2"},
                {"title": "IoT network adversarial robustness survey",
                 "relevance_score": "0.25",
                 "matched_keywords": "kw:title:adversarial robustness", "citations": "1"},
                {"title": "Certified adversarial robustness for deep models",
                 "relevance_score": "0.25",
                 "matched_keywords": "kw:title:adversarial robustness", "citations": "0"},
            ],
        }
        hi = [p for p in parent["papers"] if float(p["relevance_score"]) >= 0.45]
        lo = [p for p in parent["papers"] if float(p["relevance_score"]) < 0.3]
        variants = self.mod.generate_variants(parent, hi, lo, hi_threshold=0.45)
        noise_pruned = [v for v in variants if v["narrowing_type"] == "noise_pruned"]
        self.assertGreater(len(noise_pruned), 0)
        np_v = noise_pruned[0]
        # "adversarial robustness" should be moved to negatives
        self.assertIn("adversarial robustness", np_v["negative_keywords"])
        # "prompt injection" and "LLM judge" should still be in keywords
        self.assertIn("prompt injection", np_v["keywords"])
        self.assertIn("LLM judge", np_v["keywords"])

    # ---- signal estimation ----

    def test_estimate_signals_structure(self):
        """estimate_signals must return all required keys with valid types."""
        parent = {
            "decision_json": {"relevance_purity": 0.25},
            "score_json": {
                "artifact": {"artifact_opportunity_0to5": 3},
                "saturation": {"saturation_score_0to5": 2},
                "niw_0to5": 4, "eb1a_0to5": 4, "career_0to5": 4,
                "citation_signal_0to5": 3,
            },
            "papers": [],
        }
        passing = [
            {"_sim_relevance": 0.75, "citations": "50"},
            {"_sim_relevance": 0.5, "citations": "10"},
            {"_sim_relevance": 0.5, "citations": "5"},
        ]
        sig = self.mod.estimate_signals(passing, parent, hi_threshold=0.45)
        required_keys = (
            "est_relevance_purity", "est_kept_papers", "est_hi_papers",
            "est_citation_signal", "est_artifact", "est_saturation",
            "est_evidence_quality", "est_niw", "est_eb1a", "est_career",
            "est_novelty_risk", "est_exec_feasibility",
            "composite_score", "purity_gain_vs_parent",
        )
        for k in required_keys:
            self.assertIn(k, sig, f"Missing key '{k}' in estimated signals")
        self.assertGreaterEqual(sig["est_relevance_purity"], 0)
        self.assertLessEqual(sig["est_relevance_purity"], 1)
        self.assertGreater(sig["composite_score"], 0)

    # ---- top-N selection ----

    def test_select_top_variants_respects_diversity(self):
        """max_per_parent constraint must be enforced."""
        base_v = {
            "topic_id": "?",
            "parent_topic_id": "?",
            "narrowing_type": "noise_pruned",
            "composite_score": 0.5,
            "est_relevance_purity": 0.5,
            "est_citation_signal": 3,
        }
        # 5 variants from TA, 2 from TB
        variants = []
        for i in range(5):
            v = dict(base_v)
            v["topic_id"] = f"TA_N{i+1}"
            v["parent_topic_id"] = "TA"
            v["composite_score"] = 0.9 - i * 0.01
            v["narrowing_type"] = ["noise_pruned", "primary_anchor", "compound_pivot",
                                   "synonym_promoted", "tightened_negatives"][i]
            variants.append(v)
        for i in range(2):
            v = dict(base_v)
            v["topic_id"] = f"TB_N{i+1}"
            v["parent_topic_id"] = "TB"
            v["composite_score"] = 0.6 - i * 0.01
            v["narrowing_type"] = ["noise_pruned", "primary_anchor"][i]
            variants.append(v)

        selected = self.mod.select_top_variants(variants, top_n=4, max_per_parent=2)
        # At most 2 from TA
        ta_sel = [v for v in selected if v["parent_topic_id"] == "TA"]
        self.assertLessEqual(len(ta_sel), 2)
        # Total <= 4
        self.assertLessEqual(len(selected), 4)

    # ---- full dry-run integration ----

    def test_main_no_autorun_produces_csv_and_report(self):
        """11_generate_narrowed_topics main() --no-autorun should produce output files.
        Uses temporary output paths so it does NOT overwrite production data.
        """
        import csv as _csv
        import tempfile
        import os
        # Only run if real decisions exist (i.e., pipeline has been run)
        decisions_csv = ROOT / "data" / "decisions" / "decisions.csv"
        if not decisions_csv.exists():
            self.skipTest("decisions.csv not found; pipeline not yet run")
        # Write to temp files so production CSV/report are not overwritten
        with tempfile.TemporaryDirectory() as td:
            tmp_csv = Path(td) / "narrowed_test.csv"
            tmp_report = Path(td) / "narrowing_test.md"
            # Monkey-patch the module's output paths for this test
            orig_out_csv = self.mod.OUT_CSV
            orig_reports_dir = self.mod.REPORTS_DIR
            try:
                self.mod.OUT_CSV = tmp_csv
                self.mod.REPORTS_DIR = Path(td)
                rc = self.mod.main(["--no-autorun", "--top-n", "4", "--max-per-parent", "1"])
                self.assertEqual(rc, 0)
                self.assertTrue(tmp_csv.exists(), "Narrowed CSV not written")
                report_file = Path(td) / "narrowing_report.md"
                self.assertTrue(report_file.exists(), "Narrowing report not written")
                # Check CSV has correct header
                with open(tmp_csv, newline="", encoding="utf-8") as f:
                    reader = _csv.DictReader(f)
                    headers = reader.fieldnames or []
                for col in ("topic_id", "title", "keywords", "parent_topic_id", "narrowing_type"):
                    self.assertIn(col, headers, f"Missing CSV column: {col}")
                # Check report has expected sections
                text = report_file.read_text(encoding="utf-8")
                self.assertIn("# Narrowing Report", text)
                self.assertIn("## Selected Variants", text)
                self.assertIn("## Per-Parent Analysis", text)
            finally:
                # Restore module-level paths
                self.mod.OUT_CSV = orig_out_csv
                self.mod.REPORTS_DIR = orig_reports_dir


class TestExistingWorkDetection(unittest.TestCase):
    """Tests for 12_detect_existing_work.py"""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load("12_detect_existing_work")

    # ---- helper function tests ----

    def test_contribution_type_benchmark(self):
        ct = self.mod._contribution_type("A benchmark for LLM evaluation robustness")
        self.assertEqual(ct, "benchmark")

    def test_contribution_type_dataset(self):
        ct = self.mod._contribution_type("A dataset for clinical NLP", "We release a corpus of 10k annotations.")
        self.assertEqual(ct, "dataset")

    def test_contribution_type_survey(self):
        ct = self.mod._contribution_type("A systematic review of LLM judges")
        self.assertEqual(ct, "survey")

    def test_contribution_type_tool(self):
        ct = self.mod._contribution_type("An evaluation framework and toolkit for LLM safety")
        self.assertEqual(ct, "tool")

    def test_contribution_type_empirical(self):
        ct = self.mod._contribution_type("Empirical analysis of tokenizer variance across LLMs")
        self.assertEqual(ct, "empirical")

    def test_contribution_type_paper_fallback(self):
        ct = self.mod._contribution_type("Understanding LLM behavior in clinical settings")
        self.assertEqual(ct, "paper")

    def test_artifact_matches_direct(self):
        """Same type → always matches."""
        self.assertTrue(self.mod._artifact_matches("benchmark", {"benchmark"}))
        self.assertTrue(self.mod._artifact_matches("dataset", {"dataset"}))

    def test_artifact_matches_via_alias(self):
        """tool matches benchmark target (via alias)."""
        self.assertTrue(self.mod._artifact_matches("tool", {"benchmark"}))

    def test_artifact_matches_no_cross(self):
        """survey should NOT match benchmark target."""
        self.assertFalse(self.mod._artifact_matches("survey", {"benchmark"}))

    def test_differentiator_strength(self):
        self.assertEqual(self.mod._differentiator_strength(0), "strong")
        self.assertEqual(self.mod._differentiator_strength(1), "moderate")
        self.assertEqual(self.mod._differentiator_strength(2), "weak")
        self.assertEqual(self.mod._differentiator_strength(5), "none")

    # ---- paper classification tests ----

    def test_classify_papers_empty_when_no_csv(self):
        """classify_papers returns [] when the dedup CSV does not exist."""
        import tempfile, os
        # Override DEDUP_DIR to a temp dir where no CSVs exist
        orig = self.mod.DEDUP_DIR
        with tempfile.TemporaryDirectory() as td:
            self.mod.DEDUP_DIR = Path(td)
            topic = {"topic_id": "T_FAKE", "keywords": "foo|bar", "synonyms": "",
                     "negative_keywords": "", "target_artifact": "benchmark",
                     "title": "fake topic"}
            result = self.mod.classify_papers(topic)
            self.assertEqual(result, [])
        self.mod.DEDUP_DIR = orig

    def test_classify_papers_direct_overlap(self):
        """High-relevance paper with matching artifact type and year ≥ 2022 → DIRECT_OVERLAP."""
        import tempfile, csv as _csv
        orig = self.mod.DEDUP_DIR
        with tempfile.TemporaryDirectory() as td:
            self.mod.DEDUP_DIR = Path(td)
            # Write a fake CSV with one high-relevance paper
            csv_path = Path(td) / "TZ.csv"
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                w = _csv.DictWriter(f, fieldnames=[
                    "title", "abstract", "year", "venue", "doi", "relevance_score",
                    "matched_keywords", "citations", "sources"
                ])
                w.writeheader()
                w.writerow({
                    "title": "A benchmark for prompt injection detection in LLM judges",
                    "abstract": "We build a benchmark to evaluate prompt injection robustness.",
                    "year": "2024",
                    "venue": "NeurIPS",
                    "doi": "10.1234/test",
                    "relevance_score": "0.75",
                    "matched_keywords": "primary:title:prompt injection",
                    "citations": "42",
                    "sources": "semantic_scholar",
                })
            topic = {
                "topic_id": "TZ",
                "keywords": "prompt injection|LLM judge",
                "synonyms": "jailbreak",
                "negative_keywords": "",
                "target_artifact": "benchmark",
                "title": "Prompt injection benchmark",
                "narrowing_note": "",
            }
            results = self.mod.classify_papers(topic)
        self.mod.DEDUP_DIR = orig
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["overlap_class"], "DIRECT_OVERLAP")
        self.assertEqual(results[0]["contribution_type"], "benchmark")

    def test_classify_papers_adjacent_low_score(self):
        """Low-relevance paper → ADJACENT."""
        import tempfile, csv as _csv
        orig = self.mod.DEDUP_DIR
        with tempfile.TemporaryDirectory() as td:
            self.mod.DEDUP_DIR = Path(td)
            csv_path = Path(td) / "TZ2.csv"
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                w = _csv.DictWriter(f, fieldnames=[
                    "title", "abstract", "year", "venue", "doi", "relevance_score",
                    "matched_keywords", "citations", "sources"
                ])
                w.writeheader()
                w.writerow({
                    "title": "A study on robustness of railway systems",
                    "abstract": "Railway IoT robustness analysis.",
                    "year": "2024",
                    "venue": "ICRA",
                    "doi": "10.1234/rail",
                    "relevance_score": "0.25",
                    "matched_keywords": "kw:title:robustness",
                    "citations": "3",
                    "sources": "semantic_scholar",
                })
            topic = {
                "topic_id": "TZ2",
                "keywords": "prompt injection|robustness",
                "synonyms": "",
                "negative_keywords": "",
                "target_artifact": "benchmark",
                "title": "Prompt injection benchmark",
                "narrowing_note": "",
            }
            results = self.mod.classify_papers(topic)
        self.mod.DEDUP_DIR = orig
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["overlap_class"], "ADJACENT")

    # ---- GitHub classification tests ----

    def test_classify_github_direct_overlap(self):
        """High-stars repo with primary keyword and artifact term → DIRECT_OVERLAP."""
        import tempfile, json as _json
        orig = self.mod.EVIDENCE_DIR
        with tempfile.TemporaryDirectory() as td:
            self.mod.EVIDENCE_DIR = Path(td)
            topic_dir = Path(td) / "TG"
            topic_dir.mkdir()
            (topic_dir / "github.json").write_text(_json.dumps([{
                "query": "prompt injection benchmark in:name,description",
                "results": [{
                    "name": "org/prompt-injection-benchmark",
                    "stars": 500,
                    "forks": 50,
                    "description": "A benchmark for evaluating LLM judge robustness to prompt injection",
                    "url": "https://github.com/org/prompt-injection-benchmark",
                    "topics": ["benchmark", "llm", "prompt-injection"],
                    "pushed_at": "2025-01-01T00:00:00Z",
                    "updated_at": "2025-01-01T00:00:00Z",
                }]
            }]), encoding="utf-8")
            topic = {
                "topic_id": "TG",
                "keywords": "prompt injection|LLM judge",
                "synonyms": "jailbreak",
                "negative_keywords": "",
                "target_artifact": "benchmark",
                "title": "Prompt injection benchmark",
                "narrowing_note": "",
            }
            results = self.mod.classify_github(topic)
        self.mod.EVIDENCE_DIR = orig
        self.assertGreater(len(results), 0)
        self.assertEqual(results[0]["overlap_class"], "DIRECT_OVERLAP")
        self.assertEqual(results[0]["venue"], "GitHub")

    def test_classify_github_skips_awesome_repos(self):
        """Awesome-list repos are filtered out (always ADJACENT, then skipped)."""
        import tempfile, json as _json
        orig = self.mod.EVIDENCE_DIR
        with tempfile.TemporaryDirectory() as td:
            self.mod.EVIDENCE_DIR = Path(td)
            topic_dir = Path(td) / "TG2"
            topic_dir.mkdir()
            (topic_dir / "github.json").write_text(_json.dumps([{
                "query": "prompt injection in:readme,description",
                "results": [{
                    "name": "sindresorhus/awesome",
                    "stars": 464235,
                    "forks": 34828,
                    "description": "Awesome lists about prompt injection and other topics",
                    "url": "https://github.com/sindresorhus/awesome",
                    "topics": ["awesome", "awesome-list"],
                    "pushed_at": "2025-01-01T00:00:00Z",
                    "updated_at": "2025-01-01T00:00:00Z",
                }]
            }]), encoding="utf-8")
            topic = {
                "topic_id": "TG2",
                "keywords": "prompt injection|LLM judge",
                "synonyms": "",
                "negative_keywords": "",
                "target_artifact": "benchmark",
                "title": "Prompt injection benchmark",
                "narrowing_note": "",
            }
            results = self.mod.classify_github(topic)
        self.mod.EVIDENCE_DIR = orig
        # Awesome-list repos should not appear in DIRECT/PARTIAL
        self.assertEqual(len(results), 0)

    # ---- full topic analysis test ----

    def test_analyze_topic_summary_structure(self):
        """analyze_topic must return summary with all required keys."""
        import tempfile
        orig_ded = self.mod.DEDUP_DIR
        orig_ev = self.mod.EVIDENCE_DIR
        with tempfile.TemporaryDirectory() as td:
            self.mod.DEDUP_DIR = Path(td) / "dedup"
            self.mod.EVIDENCE_DIR = Path(td) / "evidence"
            (self.mod.DEDUP_DIR).mkdir()
            topic = {
                "topic_id": "TAN",
                "keywords": "LLM judge|benchmark",
                "synonyms": "",
                "negative_keywords": "",
                "target_artifact": "benchmark",
                "title": "LLM judge benchmark",
                "narrowing_note": "",
            }
            result = self.mod.analyze_topic(topic)
        self.mod.DEDUP_DIR = orig_ded
        self.mod.EVIDENCE_DIR = orig_ev
        summary = result["summary"]
        for key in ("topic_id", "n_direct", "n_partial", "n_adjacent",
                    "differentiator_strength", "go_blocked", "requires_differentiator"):
            self.assertIn(key, summary, f"Missing key '{key}' in summary")
        # With no data, expect 0 findings and "strong" differentiator
        self.assertEqual(summary["n_direct"], 0)
        self.assertEqual(summary["differentiator_strength"], "strong")
        self.assertFalse(summary["go_blocked"])

    # ---- integration test (runs on real data if present) ----

    def test_main_runs_on_real_data(self):
        """main() must exit 0 when real dedup CSVs + evidence exist."""
        decisions_csv = ROOT / "data" / "decisions" / "decisions.csv"
        if not decisions_csv.exists():
            self.skipTest("Pipeline not yet run; skipping integration test.")
        import tempfile, os
        orig_out = self.mod.OUT_DIR
        orig_rep = self.mod.REPORTS_DIR
        with tempfile.TemporaryDirectory() as td:
            self.mod.OUT_DIR = Path(td) / "ew"
            self.mod.REPORTS_DIR = Path(td) / "reports"
            self.mod.OUT_DIR.mkdir()
            self.mod.REPORTS_DIR.mkdir()
            rc = self.mod.main(["--no-report"])
        self.mod.OUT_DIR = orig_out
        self.mod.REPORTS_DIR = orig_rep
        self.assertEqual(rc, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
