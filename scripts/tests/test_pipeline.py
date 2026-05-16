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

    # ---- paper threshold tests ----

    def test_classify_papers_partial_at_0_50(self):
        """Paper with relevance=0.50 → PARTIAL_OVERLAP at default threshold (0.65)."""
        import tempfile, csv as _csv
        orig = self.mod.DEDUP_DIR
        with tempfile.TemporaryDirectory() as td:
            self.mod.DEDUP_DIR = Path(td)
            csv_path = Path(td) / "TP1.csv"
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                w = _csv.DictWriter(f, fieldnames=[
                    "title", "abstract", "year", "venue", "doi",
                    "relevance_score", "matched_keywords", "citations", "sources",
                ])
                w.writeheader()
                w.writerow({
                    "title": "A benchmark for LLM judge evaluation",
                    "abstract": "We propose a benchmark to evaluate judges.",
                    "year": "2024", "venue": "ACL", "doi": "10.1234/tp1",
                    "relevance_score": "0.50",   # below default 0.65 threshold
                    "matched_keywords": "primary:title:LLM judge",
                    "citations": "10", "sources": "semantic_scholar",
                })
            topic = {
                "topic_id": "TP1", "keywords": "LLM judge|benchmark", "synonyms": "",
                "negative_keywords": "", "target_artifact": "benchmark",
                "title": "LLM judge benchmark", "narrowing_note": "",
            }
            results = self.mod.classify_papers(topic)   # uses default DIRECT_REL_THRESHOLD=0.65
        self.mod.DEDUP_DIR = orig
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["overlap_class"], "PARTIAL_OVERLAP",
                         "Score 0.50 must be PARTIAL, not DIRECT, at default threshold 0.65")

    def test_classify_papers_direct_at_0_70(self):
        """Paper with relevance=0.70 AND artifact match AND year≥2022 → DIRECT_OVERLAP."""
        import tempfile, csv as _csv
        orig = self.mod.DEDUP_DIR
        with tempfile.TemporaryDirectory() as td:
            self.mod.DEDUP_DIR = Path(td)
            csv_path = Path(td) / "TP2.csv"
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                w = _csv.DictWriter(f, fieldnames=[
                    "title", "abstract", "year", "venue", "doi",
                    "relevance_score", "matched_keywords", "citations", "sources",
                ])
                w.writeheader()
                w.writerow({
                    "title": "LLM judge benchmark for prompt injection robustness",
                    "abstract": "A benchmark evaluating LLM judge robustness to injection attacks.",
                    "year": "2024", "venue": "NeurIPS", "doi": "10.1234/tp2",
                    "relevance_score": "0.70",
                    "matched_keywords": "primary:title:llm judge",
                    "citations": "55", "sources": "semantic_scholar",
                })
            topic = {
                "topic_id": "TP2", "keywords": "LLM judge|benchmark", "synonyms": "",
                "negative_keywords": "", "target_artifact": "benchmark",
                "title": "LLM judge benchmark", "narrowing_note": "",
            }
            results = self.mod.classify_papers(topic)
        self.mod.DEDUP_DIR = orig
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["overlap_class"], "DIRECT_OVERLAP",
                         "Score 0.70 with artifact match must be DIRECT_OVERLAP")

    # ── source-count tests ──────────────────────────────────────────────────────

    def test_analyze_topic_source_counts_github(self):
        """GitHub DIRECT_OVERLAP increments direct_github_count, not direct_paper_count."""
        import tempfile, json as _json
        orig_ded = self.mod.DEDUP_DIR
        orig_ev  = self.mod.EVIDENCE_DIR
        with tempfile.TemporaryDirectory() as td:
            ded_dir = Path(td) / "dedup"
            ev_dir  = Path(td) / "evidence"
            ded_dir.mkdir(); ev_dir.mkdir()
            self.mod.DEDUP_DIR    = ded_dir
            self.mod.EVIDENCE_DIR = ev_dir
            # No papers CSV → zero paper findings
            gh_dir = ev_dir / "TSC"
            gh_dir.mkdir()
            (gh_dir / "github.json").write_text(_json.dumps([{
                "query": "prompt injection benchmark",
                "results": [{
                    "name": "acme/prompt-injection-benchmark",
                    "stars": 200,
                    "description": "A benchmark for evaluation of prompt injection in LLM judges",
                    "url": "https://github.com/acme/prompt-injection-benchmark",
                    "topics": ["benchmark", "prompt-injection"],
                    "pushed_at": "2025-01-01T00:00:00Z",
                    "updated_at": "2025-01-01T00:00:00Z",
                }],
            }]), encoding="utf-8")
            topic = {
                "topic_id": "TSC", "keywords": "prompt injection|LLM judge", "synonyms": "",
                "negative_keywords": "", "target_artifact": "benchmark",
                "title": "Prompt injection benchmark", "narrowing_note": "",
            }
            result = self.mod.analyze_topic(topic)
        self.mod.DEDUP_DIR    = orig_ded
        self.mod.EVIDENCE_DIR = orig_ev
        s = result["summary"]
        self.assertEqual(s["direct_paper_count"], 0, "No papers → direct_paper_count must be 0")
        self.assertGreater(s["direct_github_count"], 0, "GitHub DIRECT must increment direct_github_count")
        self.assertFalse(s["peer_reviewed_direct_overlap"], "No paper overlap → peer_reviewed_direct must be False")
        self.assertTrue(s["artifact_direct_overlap"], "GitHub DIRECT → artifact_direct_overlap must be True")

    def test_analyze_topic_source_counts_hf(self):
        """HuggingFace DIRECT_OVERLAP increments direct_hf_count, not direct_paper_count."""
        import tempfile, json as _json
        orig_ded = self.mod.DEDUP_DIR
        orig_ev  = self.mod.EVIDENCE_DIR
        with tempfile.TemporaryDirectory() as td:
            ded_dir = Path(td) / "dedup"
            ev_dir  = Path(td) / "evidence"
            ded_dir.mkdir(); ev_dir.mkdir()
            self.mod.DEDUP_DIR    = ded_dir
            self.mod.EVIDENCE_DIR = ev_dir
            hf_dir = ev_dir / "THF"
            hf_dir.mkdir()
            (hf_dir / "huggingface.json").write_text(_json.dumps([{
                "query": "prompt injection",
                "results": [{
                    "id": "acme/prompt-injection-benchmark-dataset",
                    "downloads": 5000,   # well above HF_DIRECT_DOWNLOADS=100
                    "likes": 80,
                    "tags": ["text-classification", "prompt-injection"],
                    "description": "Dataset for prompt injection detection benchmarks",
                }],
            }]), encoding="utf-8")
            topic = {
                "topic_id": "THF", "keywords": "prompt injection|LLM judge", "synonyms": "",
                "negative_keywords": "", "target_artifact": "dataset",
                "title": "Prompt injection dataset", "narrowing_note": "",
            }
            result = self.mod.analyze_topic(topic)
        self.mod.DEDUP_DIR    = orig_ded
        self.mod.EVIDENCE_DIR = orig_ev
        s = result["summary"]
        self.assertEqual(s["direct_paper_count"], 0, "No papers → direct_paper_count must be 0")
        self.assertGreater(s["direct_hf_count"], 0, "HF DIRECT must increment direct_hf_count")
        self.assertFalse(s["peer_reviewed_direct_overlap"])
        self.assertTrue(s["artifact_direct_overlap"])

    # ── _artifact_differentiator_strength tests ────────────────────────────────

    def test_artifact_differentiator_strength_domain_topic(self):
        """Clinical topic with no peer-reviewed paper overlap → 'strong' artifact diff."""
        topic = {
            "topic_id": "TADS",
            "keywords": "clinical LLM|benchmark|reproducibility",
            "synonyms": "",
            "negative_keywords": "",
            "target_artifact": "benchmark",
            "title": "Clinical LLM benchmark",
            "category": "eval",
        }
        strength = self.mod._artifact_differentiator_strength(topic, peer_reviewed_direct=0, artifact_direct_count=5)
        self.assertEqual(strength, "strong",
                         "Domain-specific (clinical) + systematic (benchmark/reproducib) → strong")

    def test_artifact_differentiator_strength_generic_high(self):
        """Generic topic with many artifacts and no paper overlap → 'weak' or 'moderate'."""
        topic = {
            "topic_id": "TADG",
            "keywords": "language model|NLP",
            "synonyms": "",
            "negative_keywords": "",
            "target_artifact": "paper",
            "title": "Language model study",
            "category": "general",
        }
        strength = self.mod._artifact_differentiator_strength(
            topic, peer_reviewed_direct=0,
            artifact_direct_count=self.mod.HIGH_ARTIFACT_OVERLAP_THRESHOLD + 2
        )
        self.assertIn(strength, ("weak", "moderate"),
                      "Generic topic + many artifacts → weak or moderate, not strong")

    # ── go_blocked logic tests ─────────────────────────────────────────────────

    def test_go_blocked_high_paper_overlap(self):
        """3+ peer-reviewed DIRECT papers → go_blocked must be True."""
        import tempfile, csv as _csv
        orig = self.mod.DEDUP_DIR
        with tempfile.TemporaryDirectory() as td:
            self.mod.DEDUP_DIR = Path(td)
            csv_path = Path(td) / "TGB.csv"
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                w = _csv.DictWriter(f, fieldnames=[
                    "title", "abstract", "year", "venue", "doi",
                    "relevance_score", "matched_keywords", "citations", "sources",
                ])
                w.writeheader()
                for i in range(4):   # 4 direct-quality papers
                    w.writerow({
                        "title": f"LLM judge benchmark paper {i} for prompt injection",
                        "abstract": "A benchmark for LLM judge robustness.",
                        "year": "2024", "venue": "ACL", "doi": f"10.1234/tgb{i}",
                        "relevance_score": "0.75",
                        "matched_keywords": "primary:title:llm judge",
                        "citations": "30", "sources": "semantic_scholar",
                    })
            topic = {
                "topic_id": "TGB", "keywords": "LLM judge|benchmark", "synonyms": "",
                "negative_keywords": "", "target_artifact": "benchmark",
                "title": "LLM judge benchmark", "narrowing_note": "",
            }
            result = self.mod.analyze_topic(topic)
        self.mod.DEDUP_DIR = orig
        s = result["summary"]
        self.assertGreaterEqual(s["direct_paper_count"], 3)
        self.assertTrue(s["high_peer_reviewed_overlap"])
        self.assertTrue(s["go_blocked"], "high_peer_reviewed_overlap + weak/none paper_diff → go_blocked")

    def test_no_go_blocked_artifact_only_strong_diff(self):
        """0 direct papers + high artifact overlap + strong artifact diff → go_blocked False."""
        import tempfile, json as _json
        orig_ded = self.mod.DEDUP_DIR
        orig_ev  = self.mod.EVIDENCE_DIR
        with tempfile.TemporaryDirectory() as td:
            ded_dir = Path(td) / "dedup"
            ev_dir  = Path(td) / "evidence"
            ded_dir.mkdir(); ev_dir.mkdir()
            self.mod.DEDUP_DIR    = ded_dir
            self.mod.EVIDENCE_DIR = ev_dir
            gh_dir = ev_dir / "TNGB"
            gh_dir.mkdir()
            # Create 10 direct GitHub artifact overlaps (above HIGH_ARTIFACT_OVERLAP_THRESHOLD=8)
            repos = [
                {
                    "name": f"org/prompt-injection-bench-{i}",
                    "stars": 150,
                    "description": f"Benchmark for evaluating prompt injection in LLM judge {i}",
                    "url": f"https://github.com/org/prompt-injection-bench-{i}",
                    "topics": ["benchmark", "prompt-injection"],
                    "pushed_at": "2025-01-01T00:00:00Z",
                    "updated_at": "2025-01-01T00:00:00Z",
                }
                for i in range(10)
            ]
            (gh_dir / "github.json").write_text(
                _json.dumps([{"query": "prompt injection benchmark", "results": repos}]),
                encoding="utf-8"
            )
            # Topic has clear domain + evaluation differentiators → artifact_diff = strong
            topic = {
                "topic_id": "TNGB",
                "keywords": "prompt injection|LLM judge|benchmark",
                "synonyms": "evaluator robustness",
                "negative_keywords": "",
                "target_artifact": "benchmark",
                "title": "Clinical LLM judge robustness benchmark",
                "category": "eval+safety",
                "narrowing_note": "",
            }
            result = self.mod.analyze_topic(topic)
        self.mod.DEDUP_DIR    = orig_ded
        self.mod.EVIDENCE_DIR = orig_ev
        s = result["summary"]
        self.assertEqual(s["direct_paper_count"], 0)
        self.assertTrue(s["high_artifact_overlap"], "10 GitHub repos must trigger high_artifact_overlap")
        self.assertFalse(s["peer_reviewed_direct_overlap"])
        # artifact_diff should be strong (topic has benchmark/robustness keywords → systematic + eval_focused)
        self.assertIn(s["artifact_differentiator_strength"], ("strong", "moderate"))
        self.assertFalse(s["go_blocked"],
                         "Strong/moderate artifact diff with no paper overlap must NOT block GO")

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


# ============================================================================
# Tier-1 bias-fix tests (16 tests)
# ============================================================================

class TestNeutralReviewerPanel(unittest.TestCase):
    """Default reviewer panel must be academically neutral."""

    def setUp(self):
        from common import llm_panel
        self.lp = llm_panel

    def test_default_panel_excludes_personal_goal_reviewers(self):
        """[#1] Default REVIEWER_ROLES (and get_reviewer_roles()) must exclude
        niw_eb1a and career_faang."""
        roles = self.lp.get_reviewer_roles(include_personal_goals=False)
        names = {r["role"] for r in roles}
        self.assertNotIn("niw_eb1a", names)
        self.assertNotIn("career_faang", names)
        # Same check for legacy alias
        legacy = {r["role"] for r in self.lp.REVIEWER_ROLES}
        self.assertNotIn("niw_eb1a", legacy)
        self.assertNotIn("career_faang", legacy)

    def test_include_personal_goals_adds_them(self):
        """[#2] --include-personal-goals (i.e., include_personal_goals=True)
        must add the niw_eb1a and career_faang reviewers."""
        roles = self.lp.get_reviewer_roles(include_personal_goals=True)
        names = {r["role"] for r in roles}
        self.assertIn("niw_eb1a", names)
        self.assertIn("career_faang", names)
        # And the count should be exactly len(neutral) + 2
        n_neutral = len(self.lp.NEUTRAL_REVIEWER_ROLES)
        self.assertEqual(len(roles), n_neutral + 2)


class TestProfileSystem(unittest.TestCase):
    """Default profile is blind_citation; weights & overrides work."""

    def setUp(self):
        from common import profiles
        self.p = profiles
        self.profiles = profiles.load_profiles()

    def test_default_profile_is_blind_citation(self):
        """[#3] DEFAULT_PROFILE constant must be blind_citation."""
        self.assertEqual(self.p.DEFAULT_PROFILE, "blind_citation")
        self.assertIn("blind_citation", self.profiles)

    def test_blind_citation_zeros_personal_goals(self):
        """[#4] In blind_citation, all personal-goal weights must be exactly 0."""
        weights = self.profiles["blind_citation"]["weights"]
        for c in self.p.PERSONAL_GOAL_COMPONENTS:
            self.assertEqual(
                float(weights.get(c, 0)), 0.0,
                f"blind_citation has non-zero weight for personal-goal '{c}': "
                f"{weights.get(c)}",
            )

    def test_niw_optimized_increases_niw_weight(self):
        """[#5] niw_optimized must boost niw_value vs blind_citation."""
        bc = float(self.profiles["blind_citation"]["weights"]["niw_value"])
        nw = float(self.profiles["niw_optimized"]["weights"]["niw_value"])
        self.assertGreater(nw, bc + 1.0,
                           f"niw_optimized niw_value ({nw}) should >> blind_citation ({bc})")

    def test_eb1a_optimized_increases_eb1a_weight(self):
        """[#6] eb1a_optimized must boost eb1a_value vs blind_citation."""
        bc = float(self.profiles["blind_citation"]["weights"]["eb1a_value"])
        eb = float(self.profiles["eb1a_optimized"]["weights"]["eb1a_value"])
        self.assertGreater(eb, bc + 1.0)

    def test_faang_career_increases_career_weight(self):
        """[#7] faang_career must boost faang_career_value vs blind_citation."""
        bc = float(self.profiles["blind_citation"]["weights"]["faang_career_value"])
        fc = float(self.profiles["faang_career"]["weights"]["faang_career_value"])
        self.assertGreater(fc, bc + 1.0)

    def test_custom_weights_override_defaults(self):
        """[#8] --profile custom with --weight-* flags must populate the profile."""
        import argparse
        parser = argparse.ArgumentParser()
        self.p.add_profile_args(parser)
        args = parser.parse_args(["--profile", "custom", "--weight-citation", "9.0"])
        name, profile = self.p.resolve_profile(args, self.profiles)
        self.assertEqual(name, "custom")
        self.assertEqual(float(profile["weights"]["citation_potential"]), 9.0)
        # Unspecified weights default to 0
        self.assertEqual(float(profile["weights"]["niw_value"]), 0.0)


class TestQueryGenerationConditional(unittest.TestCase):
    """Forced artifact-axis terms must NOT be added unless artifact type requires them."""

    def setUp(self):
        self.gen = _load("01_generate_queries")

    def test_paper_target_gets_no_axis_injection(self):
        """[#9a] target_artifact='paper' must NOT inject benchmark/eval/repro."""
        topic = {
            "topic_id": "TX",
            "title": "Theoretical analysis of Transformer attention",
            "category": "theory",
            "keywords": "transformer|attention",
            "synonyms": "self-attention",
            "negative_keywords": "",
            "target_artifact": "paper",
            "prelim_priority": "3",
        }
        q = self.gen.build_queries(topic)
        all_text = " ".join(q["semantic_scholar"] + q["github"] + q["huggingface"]).lower()
        for forced in ("benchmark", "evaluation", "robustness", "reproducibility"):
            self.assertNotIn(forced, all_text,
                             f"target_artifact=paper but query contains '{forced}': {all_text[:200]}")

    def test_benchmark_target_gets_benchmark_axis(self):
        """[#9b] target_artifact='benchmark' SHOULD inject benchmark/evaluation."""
        topic = {
            "topic_id": "TX",
            "title": "Format sensitivity",
            "category": "eval",
            "keywords": "format sensitivity",
            "synonyms": "structured output",
            "negative_keywords": "",
            "target_artifact": "benchmark",
            "prelim_priority": "4",
        }
        q = self.gen.build_queries(topic)
        all_text = " ".join(q["semantic_scholar"]).lower()
        self.assertTrue("benchmark" in all_text or "evaluation" in all_text,
                        f"benchmark target should inject benchmark/eval terms: {all_text[:200]}")


class TestSeedKeywordCap(unittest.TestCase):
    """[#10] Seed keyword cap warning fires when a keyword exceeds 3 occurrences."""

    def test_keyword_cap_warning_fires(self):
        from common import seed_audit
        import tempfile, csv as _csv
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "test_seed.csv"
            with tmp.open("w", newline="", encoding="utf-8") as f:
                w = _csv.DictWriter(f, fieldnames=[
                    "topic_id", "title", "category", "keywords", "synonyms",
                    "negative_keywords", "target_artifact", "prelim_priority",
                ])
                w.writeheader()
                # 4× "llm judge" → exceeds cap (3)
                for i in range(4):
                    w.writerow({"topic_id": f"X{i}", "title": f"Topic {i}",
                                "category": "eval", "keywords": "llm judge",
                                "synonyms": "", "negative_keywords": "",
                                "target_artifact": "benchmark", "prelim_priority": "3"})
            audit = seed_audit.audit_seed_file(tmp)
            self.assertGreater(len(audit["repeated_keywords"]), 0)
            kws = [r["keyword"] for r in audit["repeated_keywords"]]
            self.assertIn("llm judge", kws)


class TestNegativeControlSentinel(unittest.TestCase):
    """[#11] If NC topics in top half under active profile, GO is blocked."""

    def test_nc_top_half_blocks_go(self):
        # Synthetic NC sentinel result with one leaky profile
        nc_sentinel = {
            "available": True,
            "leak_detected": True,
            "leaky_profiles": ["niw_optimized"],
        }
        # Build a fake topic that would otherwise be GO
        gate_mod = _load("08_confidence_gate")
        # Patch in-memory readers to simulate signals that would cause GO
        scores_data = {
            "rubric": {"composites": {"Overall": 20}},
            "citation_signal_0to5": 5,
            "artifact": {"artifact_opportunity_0to5": 4, "existing_artifact_density": 0.1,
                         "differentiator_required": False},
            "saturation": {"saturation_score_0to5": 1},
            "venue": {"venue_signal_0to5": 3},
            "risk": {"ip_risk_0to5": 0},
            "relevance_purity": 0.6,
            "kept_papers": 30,
            "niw_0to5": 4,
            "eb1a_0to5": 4,
            "career_0to5": 3,
            "profile_scores": {
                "blind_citation":  {"score": 18.0, "is_personal_goal": False},
                "niw_optimized":   {"score": 22.0, "is_personal_goal": True},
            },
        }
        agree_data = {
            "plurality_decision": "GO", "decision_score_mean_0to3": 2.5,
            "high_confidence_drops": 0, "high_disagreement_flag": False,
            "n_reviews": 8,
        }
        # Stub readers
        orig_read = gate_mod.read_json
        def fake_read(path, default=None):
            sp = str(path)
            if sp.endswith("scores"+os.sep+"NCTOPIC.json") or "NCTOPIC.json" in sp and "scores" in sp:
                return scores_data
            if sp.endswith("agreement"+os.sep+"NCTOPIC.json") or ("NCTOPIC.json" in sp and "agreement" in sp):
                return agree_data
            return default if default is not None else {}
        gate_mod.read_json = fake_read
        try:
            d = gate_mod.gate_topic("NCTOPIC",
                                    active_profile_name="niw_optimized",
                                    active_profile_is_personal_goal=True,
                                    blind_citation_median=10.0,
                                    nc_sentinel=nc_sentinel)
            # Per spec: NC-leaky profile must set negative_control_blocked_go
            # (the flag persists regardless of whether the GO branch was reached
            # — the flag prevents GO from ever happening downstream).
            self.assertTrue(d["negative_control_blocked_go"],
                            "NC-leaky profile must set negative_control_blocked_go=True")
            self.assertNotEqual(d["final_decision"], "GO")
        finally:
            gate_mod.read_json = orig_read


class TestReportShowsProfileAndSentinel(unittest.TestCase):
    """[#12] Final report must include scoring profile + negative-control status."""

    def test_report_contains_profile_and_sentinel(self):
        rep_path = ROOT / "reports" / "final_decision_report.md"
        if not rep_path.exists():
            self.skipTest("Final report not generated yet")
        text = rep_path.read_text(encoding="utf-8")
        self.assertIn("## 2.5 Scoring Configuration", text)
        self.assertIn("Active scoring profile", text)
        self.assertIn("Negative-control sentinel", text)


class TestPersonalGoalOnlyWeak(unittest.TestCase):
    """[#13] Topic high only under personal-goal profile must be flagged."""

    def test_personal_goal_only_warning(self):
        gate_mod = _load("08_confidence_gate")
        scores_data = {
            "rubric": {"composites": {"Overall": 20}},
            "citation_signal_0to5": 5,
            "artifact": {"artifact_opportunity_0to5": 4, "existing_artifact_density": 0.1,
                         "differentiator_required": False},
            "saturation": {"saturation_score_0to5": 1},
            "venue": {"venue_signal_0to5": 3},
            "risk": {"ip_risk_0to5": 0},
            "relevance_purity": 0.15,         # below 0.30 → blind_citation gate fails
            "kept_papers": 30,
            "niw_0to5": 5, "eb1a_0to5": 5, "career_0to5": 2,
            "profile_scores": {
                "blind_citation":  {"score": 5.0, "is_personal_goal": False},
                "niw_optimized":   {"score": 25.0, "is_personal_goal": True},
            },
        }
        agree_data = {
            "plurality_decision": "GO", "decision_score_mean_0to3": 2.5,
            "high_confidence_drops": 0, "high_disagreement_flag": False, "n_reviews": 8,
        }
        orig_read = gate_mod.read_json
        def fake_read(path, default=None):
            sp = str(path)
            if "PGT.json" in sp and "scores" in sp:
                return scores_data
            if "PGT.json" in sp and "agreement" in sp:
                return agree_data
            return default if default is not None else {}
        gate_mod.read_json = fake_read
        try:
            d = gate_mod.gate_topic("PGT",
                                    active_profile_name="niw_optimized",
                                    active_profile_is_personal_goal=True,
                                    blind_citation_median=10.0,
                                    nc_sentinel={"available": True, "leak_detected": False,
                                                 "leaky_profiles": []})
            self.assertTrue(d["personal_goal_only_weak_topic"])
            self.assertNotEqual(d["final_decision"], "GO")
        finally:
            gate_mod.read_json = orig_read


class TestGoBlockedIfBlindCitationFails(unittest.TestCase):
    """[#14] GO blocked if topic fails blind_citation but wins under niw_optimized."""

    def test_blind_citation_failure_blocks_go(self):
        # This is structurally the same path as test_personal_goal_only_warning
        # but checks the explicit reasoning string.
        gate_mod = _load("08_confidence_gate")
        scores_data = {
            "rubric": {"composites": {"Overall": 20}},
            "citation_signal_0to5": 5,
            "artifact": {"artifact_opportunity_0to5": 4, "existing_artifact_density": 0.1,
                         "differentiator_required": False},
            "saturation": {"saturation_score_0to5": 1},
            "venue": {"venue_signal_0to5": 3},
            "risk": {"ip_risk_0to5": 0},
            "relevance_purity": 0.15,
            "kept_papers": 30, "niw_0to5": 5, "eb1a_0to5": 5, "career_0to5": 2,
            "profile_scores": {
                "blind_citation": {"score": -2.0, "is_personal_goal": False},
                "niw_optimized":  {"score": 28.0, "is_personal_goal": True},
            },
        }
        agree_data = {
            "plurality_decision": "GO", "decision_score_mean_0to3": 2.5,
            "high_confidence_drops": 0, "high_disagreement_flag": False, "n_reviews": 8,
        }
        orig_read = gate_mod.read_json
        def fake_read(path, default=None):
            sp = str(path)
            if "BCFAIL.json" in sp and "scores" in sp:
                return scores_data
            if "BCFAIL.json" in sp and "agreement" in sp:
                return agree_data
            return default if default is not None else {}
        gate_mod.read_json = fake_read
        try:
            d = gate_mod.gate_topic("BCFAIL",
                                    active_profile_name="niw_optimized",
                                    active_profile_is_personal_goal=True,
                                    blind_citation_median=10.0,
                                    nc_sentinel={"available": True, "leak_detected": False,
                                                 "leaky_profiles": []})
            self.assertNotEqual(d["final_decision"], "GO")
            self.assertIn("PERSONAL_GOAL_ONLY_WEAK_TOPIC", d["reasoning_summary"])
        finally:
            gate_mod.read_json = orig_read


class TestBiasAuditOutputs(unittest.TestCase):
    """[#15][#16] Bias audit report and profile comparison table must be generated."""

    def test_bias_audit_report_exists(self):
        rep = ROOT / "reports" / "BIAS_AUDIT_REPORT.md"
        if not rep.exists():
            self.skipTest("BIAS_AUDIT_REPORT.md not yet generated; "
                          "run python scripts/13_bias_audit.py first")
        text = rep.read_text(encoding="utf-8")
        self.assertIn("Bias Audit Report", text)

    def test_profile_comparison_table_in_audit_outputs(self):
        pr = ROOT / "data" / "bias_audit" / "profile_rankings.csv"
        if not pr.exists():
            self.skipTest("profile_rankings.csv not generated")
        import csv as _csv
        rows = list(_csv.DictReader(pr.open(encoding="utf-8")))
        self.assertGreater(len(rows), 0)
        # Must contain rank columns for the canonical default profile
        first = rows[0]
        self.assertTrue(any(k.startswith("rank_blind_citation") for k in first.keys())
                        or any(k.startswith("rank_current_strategy") for k in first.keys()),
                        f"profile_rankings.csv missing expected rank_* columns; got {list(first.keys())[:6]}")


class TestArxivWatch(unittest.TestCase):
    """Tests for scripts/15_arxiv_watch.py.

    These tests cover the pure (non-network) helpers — relevance scoring,
    Atom-feed parsing, diff state-tracking, and report rendering — because
    network-based tests would be flaky.
    """

    def setUp(self):
        self.mod = _load("15_arxiv_watch")

    def test_relevance_score_full_match(self):
        score = self.mod.relevance_score(
            title="Position bias in LLM judges",
            summary="We measure ordering effects in evaluator models",
            keywords=["position bias", "judge", "LLM"],
        )
        self.assertAlmostEqual(score, 1.0, places=2)

    def test_relevance_score_partial_match(self):
        score = self.mod.relevance_score(
            title="Image classification benchmark",
            summary="A new dataset for vision",
            keywords=["position bias", "judge", "LLM"],
        )
        self.assertEqual(score, 0.0)

    def test_relevance_score_case_insensitive(self):
        score = self.mod.relevance_score(
            title="POSITION BIAS in JUDGES",
            summary="",
            keywords=["position bias", "judge"],
        )
        self.assertAlmostEqual(score, 1.0, places=2)

    def test_kill_signal_detection(self):
        flag, kws = self.mod.kill_signal(
            title="LLM judge benchmark released",
            summary="We release an open-source harness for evaluating",
            kill_keywords=["benchmark", "released code", "harness"],
        )
        self.assertTrue(flag)
        self.assertIn("benchmark", kws)
        self.assertIn("harness", kws)

    def test_kill_signal_negative(self):
        flag, kws = self.mod.kill_signal(
            title="Theory of pre-training optima",
            summary="We prove convergence properties",
            kill_keywords=["benchmark", "harness"],
        )
        self.assertFalse(flag)
        self.assertEqual(kws, [])

    def test_diff_new_ids_first_run(self):
        new = self.mod.diff_new_ids(["a", "b", "c"], [])
        self.assertEqual(set(new), {"a", "b", "c"})

    def test_diff_new_ids_no_change(self):
        new = self.mod.diff_new_ids(["a", "b"], ["a", "b"])
        self.assertEqual(new, [])

    def test_diff_new_ids_partial(self):
        new = self.mod.diff_new_ids(["a", "b", "c", "d"], ["a", "c"])
        self.assertEqual(set(new), {"b", "d"})

    def test_parse_atom_feed_minimal(self):
        # Minimal Atom feed with one entry
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2501.01234v2</id>
            <title>Position bias in LLM judges</title>
            <summary>We quantify position bias across five judges.</summary>
            <published>2025-01-15T00:00:00Z</published>
            <updated>2025-01-20T00:00:00Z</updated>
            <author><name>Jane Doe</name></author>
            <author><name>John Smith</name></author>
            <category term="cs.CL"/>
            <category term="cs.AI"/>
            <link rel="alternate" href="https://arxiv.org/abs/2501.01234"/>
          </entry>
        </feed>
        """
        papers = self.mod.parse_atom_feed(xml)
        self.assertEqual(len(papers), 1)
        p = papers[0]
        self.assertEqual(p["arxiv_id"], "2501.01234")
        self.assertIn("Position bias", p["title"])
        self.assertEqual(p["authors"], ["Jane Doe", "John Smith"])
        self.assertEqual(set(p["categories"]), {"cs.CL", "cs.AI"})

    def test_parse_atom_feed_empty(self):
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom"></feed>"""
        papers = self.mod.parse_atom_feed(xml)
        self.assertEqual(papers, [])

    def test_render_report_no_results_no_kill(self):
        # Empty results list still produces valid markdown
        md = self.mod.render_report([])
        self.assertIn("# arXiv Scoop Watch", md)
        self.assertIn("Queries run: **0**", md)

    def test_render_report_kill_signal_surfaces_first(self):
        results = [{
            "query_id": "T02_position_bias",
            "topic_id": "T02",
            "title": "Position-bias",
            "watch_priority": "HIGH",
            "n_fetched": 5,
            "n_new": 1,
            "n_relevant": 1,
            "n_kill_signal": 1,
            "new_papers": [{
                "arxiv_id": "2501.99999",
                "title": "Cross-model position bias benchmark with released harness",
                "summary": "We release a new harness.",
                "published": "2025-01-15T00:00:00Z",
                "link": "https://arxiv.org/abs/2501.99999",
                "authors": ["A Researcher"],
                "categories": ["cs.CL"],
                "relevance_score": 0.95,
                "kill_signal": True,
                "kill_keywords": ["benchmark", "harness"],
            }],
            "kill_papers": [{
                "arxiv_id": "2501.99999",
                "title": "Cross-model position bias benchmark with released harness",
                "summary": "We release a new harness.",
                "published": "2025-01-15T00:00:00Z",
                "link": "https://arxiv.org/abs/2501.99999",
                "authors": ["A Researcher"],
                "categories": ["cs.CL"],
                "relevance_score": 0.95,
                "kill_signal": True,
                "kill_keywords": ["benchmark", "harness"],
            }],
            "error": None,
        }]
        md = self.mod.render_report(results)
        self.assertIn("KILL SIGNAL", md)
        # Kill section must appear before per-query results
        kill_idx = md.find("KILL SIGNAL")
        per_q_idx = md.find("Per-query results")
        self.assertGreater(per_q_idx, kill_idx)


class TestExtractBibtex(unittest.TestCase):
    """Tests for scripts/16_extract_bibtex.py."""

    def setUp(self):
        self.mod = _load("16_extract_bibtex")

    def test_cite_key_basic(self):
        k = self.mod.cite_key(
            authors="Wang Yifan; Doe Jane",
            year="2023",
            title="Large Language Models are not Robust Multiple Choice Selectors",
        )
        # First author last name + year + first significant word
        self.assertEqual(k, "yifan2023large")

    def test_split_authors_pipe(self):
        out = self.mod._split_authors("A B|C D|E F")
        self.assertEqual(out, ["A B", "C D", "E F"])

    def test_split_authors_semicolon(self):
        out = self.mod._split_authors("A B; C D")
        self.assertEqual(out, ["A B", "C D"])

    def test_split_authors_and(self):
        out = self.mod._split_authors("A B and C D and E F")
        self.assertEqual(out, ["A B", "C D", "E F"])

    def test_split_authors_single(self):
        out = self.mod._split_authors("A B")
        self.assertEqual(out, ["A B"])

    def test_split_authors_empty(self):
        self.assertEqual(self.mod._split_authors(""), [])
        self.assertEqual(self.mod._split_authors("   "), [])

    def test_cite_key_no_year(self):
        k = self.mod.cite_key(authors="Smith Jane", year="", title="A paper")
        self.assertIn("nd", k)

    def test_cite_key_no_authors(self):
        k = self.mod.cite_key(authors="", year="2024", title="A title")
        self.assertTrue(k.startswith("anonymous2024"))

    def test_to_bibtex_article(self):
        row = {
            "title":   "Position Bias",
            "authors": "Wang Y; Doe J",
            "year":    "2023",
            "venue":   "Journal of ML Research",
            "doi":     "10.1/xyz",
            "url":     "https://example.com/paper",
            "relevance_score": "0.85",
            "citations": "42",
        }
        bib = self.mod.to_bibtex(row)
        self.assertIn("@article{", bib)
        self.assertIn("title = {Position Bias}", bib)
        self.assertIn("journal = {Journal of ML Research}", bib)
        self.assertIn("doi = {10.1/xyz}", bib)
        self.assertIn("note = {relevance=0.85; citations=42}", bib)

    def test_to_bibtex_arxiv_misc(self):
        row = {
            "title": "Some preprint",
            "authors": "Smith J",
            "year": "2024",
            "venue": "arXiv",
            "doi": "",
            "url": "https://arxiv.org/abs/2401.12345",
        }
        bib = self.mod.to_bibtex(row)
        self.assertIn("@misc{", bib)
        self.assertIn("eprint = {2401.12345}", bib)
        self.assertIn("archivePrefix = {arXiv}", bib)

    def test_to_bibtex_inproceedings(self):
        row = {
            "title": "X",
            "authors": "A B",
            "year": "2025",
            "venue": "Proceedings of NeurIPS",
            "doi": "",
            "url": "",
        }
        bib = self.mod.to_bibtex(row)
        self.assertIn("@inproceedings{", bib)
        self.assertIn("booktitle = {Proceedings of NeurIPS}", bib)

    def test_bibtex_special_chars_escaped(self):
        row = {
            "title": "Models & Methods: 100% accuracy_test",
            "authors": "X",
            "year": "2024",
            "venue": "v",
            "doi": "", "url": "",
        }
        bib = self.mod.to_bibtex(row)
        self.assertIn(r"\&", bib)
        self.assertIn(r"\%", bib)
        self.assertIn(r"\_", bib)

    def test_deduplicate_keys(self):
        e1 = "@article{wang2023position,\n  title = {A}\n}\n"
        e2 = "@article{wang2023position,\n  title = {B}\n}\n"
        e3 = "@article{wang2023position,\n  title = {C}\n}\n"
        out = self.mod.deduplicate_keys([e1, e2, e3])
        keys = []
        import re as _re
        for x in out:
            m = _re.match(r"^@\w+\{([^,]+),", x)
            if m:
                keys.append(m.group(1))
        self.assertEqual(keys, ["wang2023position", "wang2023positiona", "wang2023positionb"])

    def test_arxiv_id_from_url(self):
        f = self.mod._arxiv_id_from_url
        self.assertEqual(f("https://arxiv.org/abs/2401.12345"), "2401.12345")
        self.assertEqual(f("https://arxiv.org/abs/2401.12345v2"), "2401.12345")
        self.assertEqual(f("https://arxiv.org/pdf/2401.12345.pdf"), "2401.12345")
        self.assertIsNone(f("https://example.com/paper"))
        self.assertIsNone(f(""))

    def test_process_topic_end_to_end(self):
        import csv as _csv
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td)
            dedup_dir = tdp / "dedup"
            dedup_dir.mkdir()
            out_dir = tdp / "out"
            csv_path = dedup_dir / "TEST.csv"
            with csv_path.open("w", encoding="utf-8", newline="") as f:
                w = _csv.DictWriter(f, fieldnames=[
                    "title", "authors", "year", "venue", "doi", "url",
                    "relevance_score", "citations",
                ])
                w.writeheader()
                w.writerow({
                    "title": "First paper",
                    "authors": "Wang Y; Doe J",
                    "year": "2023",
                    "venue": "JMLR",
                    "doi": "10.1/a",
                    "url": "",
                    "relevance_score": "0.9",
                    "citations": "10",
                })
                w.writerow({
                    "title": "Second paper",
                    "authors": "Smith J",
                    "year": "2024",
                    "venue": "arXiv",
                    "doi": "",
                    "url": "https://arxiv.org/abs/2401.99999",
                    "relevance_score": "0.3",
                    "citations": "0",
                })
            # Patch DEDUP_DIR
            orig_dedup = self.mod.DEDUP_DIR
            self.mod.DEDUP_DIR = dedup_dir
            try:
                n, out_path = self.mod.process_topic(
                    "TEST", min_relevance=0.0, out_dir=out_dir,
                )
            finally:
                self.mod.DEDUP_DIR = orig_dedup
            self.assertEqual(n, 2)
            text = out_path.read_text(encoding="utf-8")
            self.assertIn("First paper", text)
            self.assertIn("Second paper", text)
            self.assertIn("eprint = {2401.99999}", text)


class TestSurveyCorpus(unittest.TestCase):
    """Tests for scripts/17_survey_corpus.py (LLM-as-Judge survey corpus builder)."""

    def setUp(self):
        self.mod = _load("17_survey_corpus")

    def test_classify_in_scope_yes(self):
        v = self.mod.classify_in_scope(
            "LLM-as-a-judge for code generation",
            "We use GPT-4 as a judge to evaluate code outputs.",
        )
        self.assertEqual(v, "yes")

    def test_classify_in_scope_partial(self):
        v = self.mod.classify_in_scope(
            "Evaluating large language models on summarization",
            "We measure GPT-4 performance using metrics like BLEU.",
        )
        # Has LLM + eval but not judge → partial
        self.assertEqual(v, "partial")

    def test_classify_in_scope_no(self):
        v = self.mod.classify_in_scope(
            "Image classification with convolutional networks",
            "We train a ResNet on ImageNet.",
        )
        self.assertEqual(v, "no")

    def test_classify_section_failure_modes(self):
        sec = self.mod.classify_section(
            "Position bias in LLM-as-a-judge",
            "We show systematic position bias and prompt injection vulnerability.",
        )
        self.assertEqual(sec, "4_failure_modes")

    def test_classify_section_methods(self):
        sec = self.mod.classify_section(
            "Pairwise comparison with chain-of-thought for LLM judges",
            "We compare pointwise and pairwise judging methods using ensemble.",
        )
        self.assertEqual(sec, "3_methods")

    def test_classify_section_defences(self):
        sec = self.mod.classify_section(
            "Calibration of LLM judges via consensus",
            "We propose a mitigation using dual-judge consensus and structured output.",
        )
        self.assertEqual(sec, "5_defences")

    def test_classify_section_unclassified(self):
        sec = self.mod.classify_section(
            "An unrelated topic about quantum computing",
            "We discuss qubits and entanglement.",
        )
        self.assertEqual(sec, "UNCLASSIFIED")

    def test_detect_failure_modes_multi(self):
        tags = self.mod.detect_failure_modes(
            "Adversarial study",
            "We analyse position bias and length bias and prompt injection.",
        )
        self.assertIn("position_bias", tags)
        self.assertIn("length_bias", tags)
        self.assertIn("prompt_injection", tags)

    def test_detect_method_type_pairwise(self):
        v = self.mod.detect_method_type(
            "Pairwise preference learning",
            "We use pairwise comparisons.",
        )
        self.assertEqual(v, "pairwise")

    def test_detect_method_type_panel(self):
        v = self.mod.detect_method_type(
            "Judge panels for safety",
            "We aggregate via a panel of judges.",
        )
        self.assertEqual(v, "panel")

    def test_derive_paper_id_stable(self):
        pid1 = self.mod.derive_paper_id(
            "Position Bias in LLM Judges",
            "Wang Yifan|Doe Jane",
            "2023",
        )
        pid2 = self.mod.derive_paper_id(
            "Position Bias in LLM Judges",
            "Wang Yifan|Doe Jane",
            "2023",
        )
        self.assertEqual(pid1, pid2)
        self.assertIn("2023", pid1)
        self.assertIn("yifan", pid1.lower())

    def test_arxiv_id_extraction(self):
        f = self.mod.arxiv_id_from_url
        self.assertEqual(f("https://arxiv.org/abs/2501.01234"), "2501.01234")
        self.assertEqual(f("https://arxiv.org/abs/2501.01234v3"), "2501.01234")
        self.assertEqual(f("https://example.com/paper"), "")

    def test_detect_code_dataset_github(self):
        code, data = self.mod.detect_code_dataset(
            "https://github.com/example/repo",
            "Some abstract",
        )
        self.assertEqual(code, "yes")

    def test_detect_code_dataset_huggingface(self):
        code, data = self.mod.detect_code_dataset(
            "https://huggingface.co/datasets/example",
            "Some abstract",
        )
        self.assertEqual(data, "yes")

    def test_row_from_dedup_full(self):
        rec = {
            "title":    "LLM-as-a-judge survey",
            "authors":  "Wang Y|Doe J",
            "year":     "2024",
            "venue":    "ACL",
            "doi":      "10.1/x",
            "url":      "https://arxiv.org/abs/2401.12345",
            "abstract": "We survey LLM-as-a-judge methods and position bias.",
        }
        row = self.mod.row_from_dedup(rec, "T02")
        self.assertEqual(row["source_topic"], "T02")
        self.assertEqual(row["in_scope"], "yes")
        self.assertEqual(row["arxiv_id"], "2401.12345")
        self.assertIn("position_bias", row["failure_mode_addressed"])

    def test_merge_rows_preserves_manual_edits(self):
        existing = [{
            "paper_id": "wang2023position",
            "title":    "Position bias",
            "authors":  "Wang Y",
            "year":     "2023",
            "venue":    "ACL",
            "in_scope": "yes",
            "section":  "4_failure_modes",
            "read_status": "deep",          # manual: user has read it
            "my_notes":     "Foundational. Cite in §4.1.",  # manual
            "relevance_to_us": "High",      # manual
            "key_contribution": "First study of position bias",  # manual
            "failure_mode_addressed": "position_bias",
            "method_type": "pairwise",
            "has_code":    "yes",
            "has_dataset": "no",
            "source_topic": "T02",
            "last_seen":   "2026-01-01T00:00:00Z",
        }]
        new = [{
            "paper_id": "wang2023position",
            "title":    "Position bias",  # same
            "authors":  "Wang Y",
            "year":     "2023",
            "venue":    "ACL",
            "in_scope": "yes",  # auto re-classifies the same
            "section":  "4_failure_modes",
            "read_status": "unread",  # auto default — should NOT overwrite
            "my_notes":     "",       # auto default — should NOT overwrite
            "relevance_to_us": "",
            "key_contribution": "",
            "failure_mode_addressed": "position_bias",
            "method_type": "pairwise",
            "has_code":    "yes",
            "has_dataset": "no",
            "source_topic": "T07",   # appearing under a new source
        }]
        merged = self.mod.merge_rows(existing, new)
        self.assertEqual(len(merged), 1)
        r = merged[0]
        # Manual fields preserved
        self.assertEqual(r["read_status"], "deep")
        self.assertEqual(r["my_notes"], "Foundational. Cite in §4.1.")
        self.assertEqual(r["relevance_to_us"], "High")
        self.assertEqual(r["key_contribution"], "First study of position bias")
        # source_topic merged
        self.assertIn("T02", r["source_topic"])
        self.assertIn("T07", r["source_topic"])

    def test_merge_rows_adds_new(self):
        existing = []
        new = [{"paper_id": "abc2024new", "title": "x", "year": "2024", "authors": "A B"}]
        merged = self.mod.merge_rows(existing, new)
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]["paper_id"], "abc2024new")

    def test_parse_arxiv_atom_to_rows(self):
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
          <entry>
            <id>http://arxiv.org/abs/2501.99999v1</id>
            <title>LLM-as-a-judge survey</title>
            <summary>We survey position bias and prompt injection.</summary>
            <published>2025-01-15T00:00:00Z</published>
            <author><name>A Researcher</name></author>
            <link rel="alternate" href="https://arxiv.org/abs/2501.99999"/>
          </entry>
        </feed>
        """
        rows = self.mod.parse_arxiv_atom_to_rows(xml)
        self.assertEqual(len(rows), 1)
        r = rows[0]
        self.assertEqual(r["arxiv_id"], "2501.99999")
        self.assertEqual(r["in_scope"], "yes")
        # Section classification: paper mentions position bias + prompt injection
        # → should land in failure_modes
        self.assertEqual(r["section"], "4_failure_modes")


class TestSurveyProgress(unittest.TestCase):
    """Tests for scripts/18_survey_progress.py."""

    def setUp(self):
        self.mod = _load("18_survey_progress")

    def test_count_checkboxes(self):
        md = """
        - [ ] item one
        - [x] item two
        - [X] item three
        - [ ] item four
        """
        checked, total = self.mod.count_checkboxes(md)
        self.assertEqual(checked, 2)
        self.assertEqual(total, 4)

    def test_count_checkboxes_empty(self):
        self.assertEqual(self.mod.count_checkboxes(""), (0, 0))
        self.assertEqual(self.mod.count_checkboxes("no checkboxes here"), (0, 0))

    def test_word_count_strips_code(self):
        text = """
        Some words here.
        ```
        code block ignored
        ```
        More words.
        """
        wc = self.mod.word_count(text)
        # "Some words here" + "More words" = 5 words
        self.assertEqual(wc, 5)

    def test_word_count_strips_urls(self):
        text = "See https://example.com/page for details."
        wc = self.mod.word_count(text)
        # "See for details" = 3 words
        self.assertEqual(wc, 3)

    def test_word_count_keeps_link_text(self):
        text = "Per [Wang et al](https://example.com) 2023."
        wc = self.mod.word_count(text)
        # "Per Wang et al 2023" = 5 words
        self.assertEqual(wc, 5)

    def test_summarise_corpus_empty(self):
        s = self.mod.summarise_corpus([])
        self.assertEqual(s["n_total"], 0)
        self.assertEqual(s["by_in_scope"], {})

    def test_summarise_corpus_populated(self):
        rows = [
            {"in_scope": "yes", "section": "4_failure_modes", "read_status": "deep",
             "year": "2024", "has_code": "yes", "has_dataset": "no",
             "failure_mode_addressed": "position_bias;length_bias"},
            {"in_scope": "partial", "section": "3_methods", "read_status": "unread",
             "year": "2023", "has_code": "no", "has_dataset": "no",
             "failure_mode_addressed": ""},
            {"in_scope": "yes", "section": "4_failure_modes", "read_status": "read",
             "year": "2024", "has_code": "yes", "has_dataset": "yes",
             "failure_mode_addressed": "position_bias"},
        ]
        s = self.mod.summarise_corpus(rows)
        self.assertEqual(s["n_total"], 3)
        self.assertEqual(s["by_in_scope"]["yes"], 2)
        self.assertEqual(s["by_section"]["4_failure_modes"], 2)
        self.assertEqual(s["by_read"]["deep"], 1)
        self.assertEqual(s["n_with_code"], 2)
        self.assertEqual(s["n_with_data"], 1)
        self.assertEqual(s["failure_modes"]["position_bias"], 2)
        self.assertEqual(s["failure_modes"]["length_bias"], 1)

    def test_progress_against_targets(self):
        summary = {
            "n_total": 100,
            "by_in_scope": {"yes": 80, "partial": 15, "no": 5},
            "by_read":     {"unread": 60, "skimmed": 20, "read": 15, "deep": 5},
        }
        targets = {"month_1_indexed": 150, "month_1_stretch": 200, "month_6_deeply_read": 100}
        out = self.mod.progress_against_targets(summary, targets)
        # 80/150 = 53%, 80/200 = 40%, (5+15)/100 = 20%
        by_name = {p["name"]: p for p in out}
        self.assertEqual(by_name["month_1_indexed"]["actual"], 80)
        self.assertEqual(by_name["month_1_indexed"]["pct"], 53)
        self.assertEqual(by_name["month_1_stretch"]["pct"], 40)
        self.assertEqual(by_name["month_6_deeply_read"]["actual"], 20)

    def test_scan_draft_sections_missing(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td) / "drafts"
            tdp.mkdir()
            out = self.mod.scan_draft_sections(tdp)
            # All sections should be reported as missing (0 pages, "(missing)" path)
            self.assertTrue(all(s["actual_pages"] == 0 for s in out))
            self.assertTrue(any(s["path"] == "(missing)" for s in out))

    def test_scan_draft_sections_with_content(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tdp = Path(td) / "drafts"
            tdp.mkdir()
            # Create a 1_introduction.md with ~500 words
            words = " ".join(["word"] * 500)
            (tdp / "1_introduction.md").write_text(f"# Intro\n\n{words}\n", encoding="utf-8")
            out = self.mod.scan_draft_sections(tdp)
            by_section = {s["section"]: s for s in out}
            self.assertEqual(by_section["1_introduction"]["words"], 501)  # 500 + "Intro"
            self.assertGreater(by_section["1_introduction"]["actual_pages"], 1.5)

    def test_parse_kill_signoff(self):
        md = """
Some preamble.

| Checkpoint | Date | K1 | K2 | K3 | K4 | Action taken |
|---|---|---|---|---|---|---|
| Month 1 | 2026-06-15 | ✅ | ✅ | ✅ | ✅ | None |
| Month 3 | TBD | | | | | |

Other content.
        """
        rows = self.mod.parse_kill_signoff(md)
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["checkpoint"], "Month 1")
        self.assertEqual(rows[0]["date"], "2026-06-15")
        self.assertEqual(rows[1]["checkpoint"], "Month 3")

    def test_render_report_empty(self):
        md = self.mod.render_report(
            corpus_summary={"n_total": 0, "by_in_scope": {}, "by_section": {},
                            "by_read": {}, "by_year": {}, "n_with_code": 0,
                            "n_with_data": 0, "failure_modes": {}},
            target_progress=[],
            section_drafts=[],
            rubric_checked=0,
            rubric_total=0,
            kill_rows=[],
        )
        self.assertIn("Survey Progress Report", md)
        self.assertIn("Corpus size: **0**", md)

    def test_derive_actions_low_corpus(self):
        summary = {
            "n_total": 50,
            "by_in_scope": {"yes": 30, "partial": 20},
            "by_section":  {"UNCLASSIFIED": 30},
            "by_read":     {"unread": 50},
        }
        targets = []
        drafts = [{"section": s, "actual_pages": 0, "target_pages": 5, "pct": 0, "words": 0, "path": "(missing)"}
                  for s in self.mod.SECTION_PAGE_TARGETS]
        actions = self.mod.derive_actions(summary, targets, drafts, 0, 60)
        # Should suggest more corpus, hand-edit unclassified, begin §1
        action_text = "\n".join(actions)
        self.assertIn("17_survey_corpus.py", action_text)
        self.assertIn("UNCLASSIFIED", action_text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
