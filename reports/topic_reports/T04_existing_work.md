# Existing Work Report — T04: Prompt-template sensitivity benchmark for clinical-domain LLM judges

> ⛔ **GO BLOCKED** — 3 direct overlap(s) found; differentiator strength = `none`.

## Summary

| Metric | Value |
|---|---|
| Direct overlaps | 3 |
| Partial overlaps | 12 |
| Adjacent | 21 |
| Total findings | 36 |
| Differentiator strength | `none` |
| GO blocked | **YES** |
| Differentiator required | Yes |

## Direct Overlaps (GO-blocking)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silentl](https://doi.org/10.48550/arXiv.2509.20293) | 2025 | arXiv.org | benchmark | 0.5 | none |
| 2 | github | [reacher-z/ClawBench](https://github.com/reacher-z/ClawBench) |  | GitHub | benchmark | 196 | none |
| 3 | huggingface | [potsawee/chatbot-arena-llm-judges](https://huggingface.co/datasets/potsawee/chatbot-arena-llm-judges) |  | HuggingFace | dataset | 170 | none |

### 1. When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2509.20293
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity' contributes a 'benchmark' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `none`

### 2. reacher-z/ClawBench
- **Source**: github  **URL**: https://github.com/reacher-z/ClawBench
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'reacher-z/ClawBench' (196 stars) provides an implementation of 'llm judge'. Description: open-source benchmark for browser ai agents on 153 everyday online tasks across 144 live websites. 5-layer recording + d.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `none`

### 3. potsawee/chatbot-arena-llm-judges
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/potsawee/chatbot-arena-llm-judges
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'potsawee/chatbot-arena-llm-judges' (170 downloads) matched 'LLM judge' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `none`

## Partial Overlaps (differentiator required)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box,](https://doi.org/10.48550/arXiv.2504.19254) | 2025 | Trans. Mach. Learn. Res. | paper | 0.5 | weak |
| 2 | paper | [Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human ](https://doi.org/10.48550/arXiv.2510.09738) | 2025 | arXiv.org | empirical | 0.5 | weak |
| 3 | paper | [Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Ope](https://doi.org/10.48550/arXiv.2602.05125) | 2026 | arXiv.org | paper | 0.5 | weak |
| 4 | paper | [Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations](https://doi.org/10.48550/arXiv.2510.11822) | 2025 | arXiv.org | paper | 0.5 | weak |
| 5 | paper | [Ask a Strong LLM Judge when Your Reward Model is Uncertain](https://doi.org/10.48550/arXiv.2510.20369) | 2025 | arXiv.org | paper | 0.5 | weak |
| 6 | paper | Tuning LLM Judge Design Decisions for 1/1000 of the Cost | 2025 | International Conference on Machine Lear | paper | 0.5 | weak |
| 7 | paper | [Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating na](https://doi.org/10.48550/arXiv.2504.02867) | 2025 | arXiv.org | paper | 0.5 | weak |
| 8 | paper | [Auto-Prompt Ensemble for LLM Judge](https://doi.org/10.48550/arXiv.2510.06538) | 2025 | arXiv.org | paper | 0.5 | weak |
| 9 | paper | [DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation](https://doi.org/10.48550/arXiv.2601.22230) | 2026 | arXiv.org | paper | 0.5 | weak |
| 10 | paper | When LLM Judge Scores Look Good but Best-of-N Decisions Fail | 2026 |  | paper | 0.5 | weak |
| 11 | github | [baaivision/JudgeLM](https://github.com/baaivision/JudgeLM) |  | GitHub | tool | 429 | weak |
| 12 | github | [UW-Madison-Lee-Lab/LLM-judge-reporting](https://github.com/UW-Madison-Lee-Lab/LLM-judge-reporting) |  | GitHub | tool | 77 | weak |

### 1. Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ensemble Scorers
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.19254
- **Year/Venue**: 2025 / Trans. Mach. Learn. Res.
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ense' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 2. Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.09738
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.50: paper titled 'Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement' contributes a 'empirical' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 3. Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2602.05125
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 4. Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.11822
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 5. Ask a Strong LLM Judge when Your Reward Model is Uncertain
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.20369
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Ask a Strong LLM Judge when Your Reward Model is Uncertain' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 6. Tuning LLM Judge Design Decisions for 1/1000 of the Cost
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Tuning LLM Judge Design Decisions for 1/1000 of the Cost' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 7. Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language generation applications
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.02867
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language gener' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 8. Auto-Prompt Ensemble for LLM Judge
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.06538
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Auto-Prompt Ensemble for LLM Judge' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 9. DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2601.22230
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 10. When LLM Judge Scores Look Good but Best-of-N Decisions Fail
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'When LLM Judge Scores Look Good but Best-of-N Decisions Fail' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 11. baaivision/JudgeLM
- **Source**: github  **URL**: https://github.com/baaivision/JudgeLM
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'baaivision/JudgeLM' (429 stars) provides an implementation of 'llm judge'. Description: [iclr 2025 spotlight] an open-sourced llm judge for evaluating llm-generated answers..
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 12. UW-Madison-Lee-Lab/LLM-judge-reporting
- **Source**: github  **URL**: https://github.com/UW-Madison-Lee-Lab/LLM-judge-reporting
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'UW-Madison-Lee-Lab/LLM-judge-reporting' (77 stars) provides an implementation of 'llm judge'. Description: a simple plug-in framework that corrects bias and computes confidence intervals in reporting llm-as-a-judge evaluation, .
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Two Senses of Experimental Robustness: Result Robustness and Procedure Robustnes](https://doi.org/10.1093/bjps/axy031) | 2022 | The British Journal for the Philosophy o | paper | 0.25 | strong |
| 2 | paper | [What Do You See in this Patient? Behavioral Testing of Clinical NLP Models](https://doi.org/10.18653/v1/2022.clinicalnlp-1.7) | 2022 | Proceedings of the 4th Clinical Natural  | paper | 0.25 | strong |
| 3 | paper | [The Difficulties of Clinical NLP](https://doi.org/10.1201/9781003283980-17) | 2023 | Engineering Mathematics and Artificial I | paper | 0.25 | strong |
| 4 | paper | [Adversarial robustness of beyond neural network models](https://doi.org/10.1016/b978-0-12-824020-5.00027-2) | 2023 | Adversarial Robustness for Machine Learn | paper | 0.25 | strong |
| 5 | paper | [Improving railway timetable robustness : Development and application of robustne](https://doi.org/10.3384/9789180758567) | 2025 | Linköping Studies in Science and Technol | paper | 0.25 | strong |
| 6 | paper | [Adversarial robustness in meta-learning and contrastive learning](https://doi.org/10.1016/b978-0-12-824020-5.00028-4) | 2023 | Adversarial Robustness for Machine Learn | paper | 0.25 | strong |
| 7 | paper | [PSAS: Multi-Template Prompt-Weighted Robustness for Adversarial Perturbations](https://doi.org/10.1109/iscait69154.2026.11477509) | 2026 | 2026 5th International Symposium on Comp | paper | 0.25 | strong |
| 8 | paper | [Examining Deep Learning in Clinical NLP](https://doi.org/10.31219/osf.io/3e6m8) | 2023 |  | paper | 0.25 | strong |
| 9 | paper | [Aggressive Compression Compromises Care: Patient Safety Risks in Clinical NLP](https://doi.org/10.37547/tajmspr/volume08issue04-14) | 2026 | The American Journal of Medical Sciences | paper | 0.25 | strong |
| 10 | paper | [Tunability / robustness of Nb3Sn](https://doi.org/10.2172/2246931) | 2023 | Tunability / robustness of Nb3Sn | paper | 0.25 | strong |
| 11 | paper | [Pareto adversarial robustness: balancing spatial robustness and sensitivity-base](https://doi.org/10.1007/s11432-022-3861-8) | 2025 | Science China Information Sciences | paper | 0.25 | strong |
| 12 | paper | [Certified robustness training](https://doi.org/10.1016/b978-0-12-824020-5.00025-9) | 2023 | Adversarial Robustness for Machine Learn | paper | 0.25 | strong |
| 13 | paper | [Preliminaries of Robustness Optimization](https://doi.org/10.1007/978-981-16-9609-1_2) | 2022 | Robustness Optimization for IoT Topology | paper | 0.25 | strong |
| 14 | paper | [Robustness](https://doi.org/10.1007/978-1-4842-9306-5_9) | 2023 | Building Responsible AI Algorithms | paper | 0.25 | strong |
| 15 | paper | [Robustness Optimization Based on Genetic Evolution](https://doi.org/10.1007/978-981-16-9609-1_4) | 2022 | Robustness Optimization for IoT Topology | paper | 0.25 | strong |
| 16 | paper | [Robustness Optimization Based on Self-Learning](https://doi.org/10.1007/978-981-16-9609-1_7) | 2022 | Robustness Optimization for IoT Topology | paper | 0.25 | strong |
| 17 | paper | [Robustness Optimization Based on Self-Organization](https://doi.org/10.1007/978-981-16-9609-1_3) | 2022 | Robustness Optimization for IoT Topology | paper | 0.25 | strong |
| 18 | paper | [Robustness Optimization Based on Node Self-Learning](https://doi.org/10.1007/978-981-16-9609-1_8) | 2022 | Robustness Optimization for IoT Topology | paper | 0.25 | strong |
| 19 | paper | [Robustness Optimization Based on Swarm Intelligence](https://doi.org/10.1007/978-981-16-9609-1_5) | 2022 | Robustness Optimization for IoT Topology | paper | 0.25 | strong |
| 20 | paper | [The American Fragility–Robustness Nexus](https://doi.org/10.1017/9781009265058.008) | 2022 | Robustness and Fragility of Political Or | paper | 0.25 | strong |
| 21 | paper | [Ontology-grounded knowledge graphs for mitigating hallucinations in large langua](https://doi.org/10.1016/j.jbi.2026.104993) | 2026 | Journal of Biomedical Informatics | paper | 0.225 | strong |

### 1. Two Senses of Experimental Robustness: Result Robustness and Procedure Robustness
- **Source**: paper  **URL**: https://doi.org/10.1093/bjps/axy031
- **Year/Venue**: 2022 / The British Journal for the Philosophy of Science
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Two Senses of Experimental Robustness: Result Robustness and Procedure Robustness' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. What Do You See in this Patient? Behavioral Testing of Clinical NLP Models
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2022.clinicalnlp-1.7
- **Year/Venue**: 2022 / Proceedings of the 4th Clinical Natural Language Processing Workshop
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'What Do You See in this Patient? Behavioral Testing of Clinical NLP Models' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:clinical nlp.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. The Difficulties of Clinical NLP
- **Source**: paper  **URL**: https://doi.org/10.1201/9781003283980-17
- **Year/Venue**: 2023 / Engineering Mathematics and Artificial Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Difficulties of Clinical NLP' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:clinical nlp.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. Adversarial robustness of beyond neural network models
- **Source**: paper  **URL**: https://doi.org/10.1016/b978-0-12-824020-5.00027-2
- **Year/Venue**: 2023 / Adversarial Robustness for Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Adversarial robustness of beyond neural network models' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. Improving railway timetable robustness : Development and application of robustness indicators
- **Source**: paper  **URL**: https://doi.org/10.3384/9789180758567
- **Year/Venue**: 2025 / Linköping Studies in Science and Technology. Dissertations
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Improving railway timetable robustness : Development and application of robustness indicators' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. Adversarial robustness in meta-learning and contrastive learning
- **Source**: paper  **URL**: https://doi.org/10.1016/b978-0-12-824020-5.00028-4
- **Year/Venue**: 2023 / Adversarial Robustness for Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Adversarial robustness in meta-learning and contrastive learning' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. PSAS: Multi-Template Prompt-Weighted Robustness for Adversarial Perturbations
- **Source**: paper  **URL**: https://doi.org/10.1109/iscait69154.2026.11477509
- **Year/Venue**: 2026 / 2026 5th International Symposium on Computer Applications and Information Technology (ISCAIT)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'PSAS: Multi-Template Prompt-Weighted Robustness for Adversarial Perturbations' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Examining Deep Learning in Clinical NLP
- **Source**: paper  **URL**: https://doi.org/10.31219/osf.io/3e6m8
- **Year/Venue**: 2023 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Examining Deep Learning in Clinical NLP' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:clinical nlp.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. Aggressive Compression Compromises Care: Patient Safety Risks in Clinical NLP
- **Source**: paper  **URL**: https://doi.org/10.37547/tajmspr/volume08issue04-14
- **Year/Venue**: 2026 / The American Journal of Medical Sciences and Pharmaceutical Research
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Aggressive Compression Compromises Care: Patient Safety Risks in Clinical NLP' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:clinical nlp.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Tunability / robustness of Nb3Sn
- **Source**: paper  **URL**: https://doi.org/10.2172/2246931
- **Year/Venue**: 2023 / Tunability / robustness of Nb3Sn
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Tunability / robustness of Nb3Sn' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. Pareto adversarial robustness: balancing spatial robustness and sensitivity-based robustness
- **Source**: paper  **URL**: https://doi.org/10.1007/s11432-022-3861-8
- **Year/Venue**: 2025 / Science China Information Sciences
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pareto adversarial robustness: balancing spatial robustness and sensitivity-based robustness' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. Certified robustness training
- **Source**: paper  **URL**: https://doi.org/10.1016/b978-0-12-824020-5.00025-9
- **Year/Venue**: 2023 / Adversarial Robustness for Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Certified robustness training' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. Preliminaries of Robustness Optimization
- **Source**: paper  **URL**: https://doi.org/10.1007/978-981-16-9609-1_2
- **Year/Venue**: 2022 / Robustness Optimization for IoT Topology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Preliminaries of Robustness Optimization' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 14. Robustness
- **Source**: paper  **URL**: https://doi.org/10.1007/978-1-4842-9306-5_9
- **Year/Venue**: 2023 / Building Responsible AI Algorithms
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Robustness' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 15. Robustness Optimization Based on Genetic Evolution
- **Source**: paper  **URL**: https://doi.org/10.1007/978-981-16-9609-1_4
- **Year/Venue**: 2022 / Robustness Optimization for IoT Topology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Robustness Optimization Based on Genetic Evolution' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 16. Robustness Optimization Based on Self-Learning
- **Source**: paper  **URL**: https://doi.org/10.1007/978-981-16-9609-1_7
- **Year/Venue**: 2022 / Robustness Optimization for IoT Topology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Robustness Optimization Based on Self-Learning' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 17. Robustness Optimization Based on Self-Organization
- **Source**: paper  **URL**: https://doi.org/10.1007/978-981-16-9609-1_3
- **Year/Venue**: 2022 / Robustness Optimization for IoT Topology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Robustness Optimization Based on Self-Organization' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 18. Robustness Optimization Based on Node Self-Learning
- **Source**: paper  **URL**: https://doi.org/10.1007/978-981-16-9609-1_8
- **Year/Venue**: 2022 / Robustness Optimization for IoT Topology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Robustness Optimization Based on Node Self-Learning' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 19. Robustness Optimization Based on Swarm Intelligence
- **Source**: paper  **URL**: https://doi.org/10.1007/978-981-16-9609-1_5
- **Year/Venue**: 2022 / Robustness Optimization for IoT Topology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Robustness Optimization Based on Swarm Intelligence' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 20. The American Fragility–Robustness Nexus
- **Source**: paper  **URL**: https://doi.org/10.1017/9781009265058.008
- **Year/Venue**: 2022 / Robustness and Fragility of Political Orders
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The American Fragility–Robustness Nexus' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:title:robustness.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 21. Ontology-grounded knowledge graphs for mitigating hallucinations in large language models for clinical question answerin
- **Source**: paper  **URL**: https://doi.org/10.1016/j.jbi.2026.104993
- **Year/Venue**: 2026 / Journal of Biomedical Informatics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.23: paper titled 'Ontology-grounded knowledge graphs for mitigating hallucinations in large language models for clinic' contributes a 'paper' matching target artifact 'benchmark+tool'. Matched keywords: kw:abstract:robustness|syn:title:clinical question answering.
- **How we differ**: Our proposed work focuses specifically on 'Prompt-template sensitivity benchmark for clinical-domain LLM judges'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

## Recommended Actions

1. **Do not promote T04 to GO** until you have articulated a concrete differentiator vs the 3 direct overlap(s) above.
2. For each DIRECT_OVERLAP, fill in the 'how_we_differ' column in the CSV with a specific contribution claim.
3. If a differentiator cannot be found, consider DROPping or NARROWING further.
