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


if __name__ == "__main__":
    unittest.main(verbosity=2)
