# Existing Work Report — T10: Reproducibility audit of LLM-judge papers

> ⛔ **GO BLOCKED (peer-reviewed overlap)** — 3 peer-reviewed DIRECT overlap(s); paper_diff_strength=`none`. Must articulate a clear differentiator before proceeding.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 3 |
| Paper diff strength | `none` |
| GitHub direct artifacts | 1 |
| HuggingFace direct artifacts | 2 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 3 |
| Artifact diff strength | `none` |
| Partial overlaps (total) | 24 |
| Adjacent | 59 |
| Total findings | 89 |
| peer_reviewed_direct | ✅ Yes |
| high_artifact_overlap | No |
| GO blocked | **YES** |
| Differentiator required | Yes |
| Artifact differentiator required | Yes |

## Peer-Reviewed Direct Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [An Empirical Study of LLM-as-a-Judge for LLM Evaluation: Fine-tuned Judge Model ](https://doi.org/10.18653/v1/2025.findings-acl.306) | 2025 | Findings of the Association for Computat | empirical | 0.75 | none |
| 2 | paper | [Automated LLM Deployment and Evaluation: A Cloud-Native Approach Using LLM-as-a-](https://doi.org/10.1109/cloud67622.2025.00053) | 2025 | 2025 IEEE 18th International Conference  | paper | 0.75 | none |
| 3 | paper | [Uncovering the Risk of Evaluation Formalism: A Debiased LLM-as-a-Judge Study in ](https://doi.org/10.2139/ssrn.5249953) | 2025 |  | survey | 0.75 | none |

### 1. An Empirical Study of LLM-as-a-Judge for LLM Evaluation: Fine-tuned Judge Model is not a General Substitute for GPT-4
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2025.findings-acl.306
- **Year/Venue**: 2025 / Findings of the Association for Computational Linguistics: ACL 2025
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.75: paper titled 'An Empirical Study of LLM-as-a-Judge for LLM Evaluation: Fine-tuned Judge Model is not a General Sub' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge|kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `none`

### 2. Automated LLM Deployment and Evaluation: A Cloud-Native Approach Using LLM-as-a-Judge
- **Source**: paper  **URL**: https://doi.org/10.1109/cloud67622.2025.00053
- **Year/Venue**: 2025 / 2025 IEEE 18th International Conference on Cloud Computing (CLOUD)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.75: paper titled 'Automated LLM Deployment and Evaluation: A Cloud-Native Approach Using LLM-as-a-Judge' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge|kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `none`

### 3. Uncovering the Risk of Evaluation Formalism: A Debiased LLM-as-a-Judge Study in Japan's Government Project Reviews
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.5249953
- **Year/Venue**: 2025 / n/a
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.75: paper titled 'Uncovering the Risk of Evaluation Formalism: A Debiased LLM-as-a-Judge Study in Japan's Government P' contributes a 'survey' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge|kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `none`

## Artifact Direct Overlaps (GitHub / HF / PWC)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | github | [IBM/eval-assist](https://github.com/IBM/eval-assist) |  | GitHub | tool | 100 | none |
| 2 | huggingface | [AI-EcoNet/HUGO-Bench-Paper-Reproducibility](https://huggingface.co/datasets/AI-EcoNet/HUGO-Bench-Paper-Reproducibility) |  | HuggingFace | dataset | 261 | none |
| 3 | huggingface | [zyzhou110/Squidiff_reproducibility](https://huggingface.co/datasets/zyzhou110/Squidiff_reproducibility) |  | HuggingFace | dataset | 106 | none |

### 1. IBM/eval-assist
- **Source**: github  **URL**: https://github.com/IBM/eval-assist
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'IBM/eval-assist' (100 stars) provides an implementation of 'llm-as-a-judge'. Description: evalassist is an open-source project that simplifies using large language models as evaluators (llm-as-a-judge) of the o.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `none`

### 2. AI-EcoNet/HUGO-Bench-Paper-Reproducibility
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/AI-EcoNet/HUGO-Bench-Paper-Reproducibility
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'AI-EcoNet/HUGO-Bench-Paper-Reproducibility' (261 downloads) matched 'reproducibility' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `none`

### 3. zyzhou110/Squidiff_reproducibility
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/zyzhou110/Squidiff_reproducibility
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'zyzhou110/Squidiff_reproducibility' (106 downloads) matched 'reproducibility' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `none`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [LLM Evaluations for Emotional Expressiveness and Factual Consistency in Medical ](https://doi.org/10.1109/resgenxai64788.2025.11344029) | 2025 | 2025 International Conference on Respons | tool | 0.75 | weak |
| 2 | paper | [A Survey on LLM-as-a-Judge](https://doi.org/10.48550/arXiv.2411.15594) | 2024 | arXiv.org | survey | 0.6 | weak |
| 3 | paper | MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchm | 2024 | International Conference on Machine Lear | benchmark | 0.6 | weak |
| 4 | paper | [Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Softw](https://doi.org/10.1145/3728963) | 2025 | Proc. ACM Softw. Eng. | empirical | 0.6 | weak |
| 5 | paper | [Preference Leakage: A Contamination Problem in LLM-as-a-judge](https://doi.org/10.48550/arXiv.2502.01534) | 2025 | arXiv.org | paper | 0.6 | weak |
| 6 | paper | [Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations](https://doi.org/10.48550/arXiv.2510.11822) | 2025 | arXiv.org | paper | 0.562 | weak |
| 7 | paper | [Judging LLM-as-a-judge with MT-Bench and Chatbot Arena](https://doi.org/10.52202/075280-2020) | 2023 | Neural Information Processing Systems | paper | 0.55 | weak |
| 8 | paper | [Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-sh](https://doi.org/10.18653/v1/2024.emnlp-main.427) | 2024 | Proceedings of the 2024 Conference on Em | paper | 0.5 | weak |
| 9 | paper | [The Impact of Likert Scale Design on Judgment Reliability in Korean and English ](https://doi.org/10.5626/ktcp.2026.32.3.126) | 2026 | KIISE Transactions on Computing Practice | paper | 0.5 | weak |
| 10 | paper | [How Reliable is Multilingual LLM-as-a-Judge?](https://doi.org/10.18653/v1/2025.findings-emnlp.587) | 2025 | Findings of the Association for Computat | paper | 0.5 | weak |
| 11 | paper | [LLM Evaluations: A Survey of Programmatic, Human, and LLM-as-Judge Approaches](https://doi.org/10.15680/ijirset.2025.1406011) | 2025 | International Journal of Innovative Rese | survey | 0.438 | weak |
| 12 | paper | Adaptive Rigor in AI System Evaluation using Temperature-Controlled Verdict Aggr | 2026 |  | tool | 0.438 | weak |
| 13 | paper | [Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating na](https://doi.org/10.48550/arXiv.2504.02867) | 2025 | arXiv.org | paper | 0.412 | weak |
| 14 | paper | [DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation](https://doi.org/10.48550/arXiv.2601.22230) | 2026 | arXiv.org | paper | 0.412 | weak |
| 15 | paper | [Multi-Dimensional Behavioral Evaluation of Agentic Stock Prediction Systems Usin](http://arxiv.org/abs/2605.05739v1) | 2026 | arXiv | tool | 0.375 | weak |
| 16 | paper | [A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Repr](https://doi.org/10.48550/arXiv.2504.07086) | 2025 | arXiv.org | paper | 0.35 | weak |
| 17 | paper | [Radiomics and Deep Features: Robust Classification of Brain Hemorrhages and Repr](https://doi.org/10.3390/bioengineering11070643) | 2024 | Bioengineering | empirical | 0.35 | weak |
| 18 | paper | [CORE-Bench: Fostering the Credibility of Published Research Through a Computatio](https://doi.org/10.48550/arXiv.2409.11363) | 2024 | Trans. Mach. Learn. Res. | benchmark | 0.35 | weak |
| 19 | github | [UW-Madison-Lee-Lab/LLM-judge-reporting](https://github.com/UW-Madison-Lee-Lab/LLM-judge-reporting) |  | GitHub | tool | 77 | weak |
| 20 | github | [ibm-self-serve-assets/JudgeIt-LLM-as-a-Judge](https://github.com/ibm-self-serve-assets/JudgeIt-LLM-as-a-Judge) |  | GitHub | tool | 35 | weak |
| 21 | huggingface | [team-dentaku/dentaku-llm-as-a-judge](https://huggingface.co/datasets/team-dentaku/dentaku-llm-as-a-judge) |  | HuggingFace | dataset | 30 | weak |
| 22 | huggingface | [bird-of-paradise/muon-distributed-reproducibility](https://huggingface.co/datasets/bird-of-paradise/muon-distributed-reproducibility) |  | HuggingFace | dataset | 40 | weak |
| 23 | huggingface | [throwaway-reproducibility-354364563/FinTrain](https://huggingface.co/datasets/throwaway-reproducibility-354364563/FinTrain) |  | HuggingFace | dataset | 21 | weak |
| 24 | huggingface | [anon7f3k2026/neurips_reproducibility_bundle](https://huggingface.co/datasets/anon7f3k2026/neurips_reproducibility_bundle) |  | HuggingFace | dataset | 22 | weak |

### 1. LLM Evaluations for Emotional Expressiveness and Factual Consistency in Medical Dialogue Systems Using LLM-as-a-Judge
- **Source**: paper  **URL**: https://doi.org/10.1109/resgenxai64788.2025.11344029
- **Year/Venue**: 2025 / 2025 International Conference on Responsible, Generative and Explainable AI (ResGenXAI)
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.75: paper titled 'LLM Evaluations for Emotional Expressiveness and Factual Consistency in Medical Dialogue Systems Usi' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge|kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 2. A Survey on LLM-as-a-Judge
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2411.15594
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.60: paper titled 'A Survey on LLM-as-a-Judge' contributes a 'survey' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 3. MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2024 / International Conference on Machine Learning
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.60: paper titled 'MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark' contributes a 'benchmark' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 4. Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering
- **Source**: paper  **URL**: https://doi.org/10.1145/3728963
- **Year/Venue**: 2025 / Proc. ACM Softw. Eng.
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.60: paper titled 'Can LLMs Replace Human Evaluators? An Empirical Study of LLM-as-a-Judge in Software Engineering' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 5. Preference Leakage: A Contamination Problem in LLM-as-a-judge
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2502.01534
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.60: paper titled 'Preference Leakage: A Contamination Problem in LLM-as-a-judge' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 6. Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.11822
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.56: paper titled 'Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:title:evaluation|syn:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 7. Judging LLM-as-a-judge with MT-Bench and Chatbot Arena
- **Source**: paper  **URL**: https://doi.org/10.52202/075280-2020
- **Year/Venue**: 2023 / Neural Information Processing Systems
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.55: paper titled 'Judging LLM-as-a-judge with MT-Bench and Chatbot Arena' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge|syn:abstract:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 8. Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2024.emnlp-main.427
- **Year/Venue**: 2024 / Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 9. The Impact of Likert Scale Design on Judgment Reliability in Korean and English LLM-as-a-Judge
- **Source**: paper  **URL**: https://doi.org/10.5626/ktcp.2026.32.3.126
- **Year/Venue**: 2026 / KIISE Transactions on Computing Practices
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'The Impact of Likert Scale Design on Judgment Reliability in Korean and English LLM-as-a-Judge' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 10. How Reliable is Multilingual LLM-as-a-Judge?
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2025.findings-emnlp.587
- **Year/Venue**: 2025 / Findings of the Association for Computational Linguistics: EMNLP 2025
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'How Reliable is Multilingual LLM-as-a-Judge?' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:title:llm-as-a-judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 11. LLM Evaluations: A Survey of Programmatic, Human, and LLM-as-Judge Approaches
- **Source**: paper  **URL**: https://doi.org/10.15680/ijirset.2025.1406011
- **Year/Venue**: 2025 / International Journal of Innovative Research in Science, Engineering and Technology
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.44: paper titled 'LLM Evaluations: A Survey of Programmatic, Human, and LLM-as-Judge Approaches' contributes a 'survey' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 12. Adaptive Rigor in AI System Evaluation using Temperature-Controlled Verdict Aggregation via Generalized Power Mean
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2026 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.44: paper titled 'Adaptive Rigor in AI System Evaluation using Temperature-Controlled Verdict Aggregation via Generali' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 13. Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language generation applications
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.02867
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.41: paper titled 'Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language gener' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation|syn:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 14. DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2601.22230
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.41: paper titled 'DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation|syn:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 15. Multi-Dimensional Behavioral Evaluation of Agentic Stock Prediction Systems Using LLM Judges with Closed-Loop Reinforcem
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.05739v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.38: paper titled 'Multi-Dimensional Behavioral Evaluation of Agentic Stock Prediction Systems Using LLM Judges with Cl' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation|syn:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 16. A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.07086
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.35: paper titled 'A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 17. Radiomics and Deep Features: Robust Classification of Brain Hemorrhages and Reproducibility Analysis Using a 3D Autoenco
- **Source**: paper  **URL**: https://doi.org/10.3390/bioengineering11070643
- **Year/Venue**: 2024 / Bioengineering
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.35: paper titled 'Radiomics and Deep Features: Robust Classification of Brain Hemorrhages and Reproducibility Analysis' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 18. CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2409.11363
- **Year/Venue**: 2024 / Trans. Mach. Learn. Res.
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.35: paper titled 'CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility ' contributes a 'benchmark' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 19. UW-Madison-Lee-Lab/LLM-judge-reporting
- **Source**: github  **URL**: https://github.com/UW-Madison-Lee-Lab/LLM-judge-reporting
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'UW-Madison-Lee-Lab/LLM-judge-reporting' (77 stars) provides an implementation of 'llm-as-a-judge'. Description: a simple plug-in framework that corrects bias and computes confidence intervals in reporting llm-as-a-judge evaluation, .
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 20. ibm-self-serve-assets/JudgeIt-LLM-as-a-Judge
- **Source**: github  **URL**: https://github.com/ibm-self-serve-assets/JudgeIt-LLM-as-a-Judge
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'ibm-self-serve-assets/JudgeIt-LLM-as-a-Judge' (35 stars) provides an implementation of 'llm-as-a-judge'. Description: automation framework using llm-as-a-judge to evaluate of agentic ai, rag, text2sql at scale; that is a good proxy for hu.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 21. team-dentaku/dentaku-llm-as-a-judge
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/team-dentaku/dentaku-llm-as-a-judge
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'team-dentaku/dentaku-llm-as-a-judge' (30 downloads) matched 'LLM-as-a-judge' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 22. bird-of-paradise/muon-distributed-reproducibility
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/bird-of-paradise/muon-distributed-reproducibility
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'bird-of-paradise/muon-distributed-reproducibility' (40 downloads) matched 'reproducibility' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 23. throwaway-reproducibility-354364563/FinTrain
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/throwaway-reproducibility-354364563/FinTrain
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'throwaway-reproducibility-354364563/FinTrain' (21 downloads) matched 'reproducibility' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 24. anon7f3k2026/neurips_reproducibility_bundle
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/anon7f3k2026/neurips_reproducibility_bundle
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'anon7f3k2026/neurips_reproducibility_bundle' (22 downloads) matched 'reproducibility' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box,](https://doi.org/10.48550/arXiv.2504.19254) | 2025 | Trans. Mach. Learn. Res. | paper | 0.312 | strong |
| 2 | paper | [A Benchmark for Long-Form Medical Question Answering](https://doi.org/10.48550/arXiv.2411.09834) | 2024 | arXiv.org | benchmark | 0.287 | strong |
| 3 | paper | [Agentic Program Repair from Test Failures at Scale: A Neuro-symbolic approach wi](https://doi.org/10.48550/arXiv.2507.18755) | 2025 | arXiv.org | empirical | 0.287 | strong |
| 4 | paper | [Rethinking Retrieval: From Traditional Retrieval Augmented Generation to Agentic](https://doi.org/10.48550/arXiv.2511.18177) | 2025 | Proceedings of the 18th International Co | tool | 0.287 | strong |
| 5 | paper | DeEscalWild: A Real-World Benchmark for Automated De-Escalation Training with SL | 2026 |  | benchmark | 0.287 | strong |
| 6 | paper | [Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Re](http://arxiv.org/abs/2605.06635v1) | 2026 | arXiv | paper | 0.287 | strong |
| 7 | paper | [Autonomous Adversary: Red-Teaming in the age of LLM](http://arxiv.org/abs/2605.06486v1) | 2026 | arXiv | paper | 0.287 | strong |
| 8 | paper | [Joint Consistency: A Unified Test-Time Aggregation Framework via Energy Minimiza](http://arxiv.org/abs/2605.06219v1) | 2026 | arXiv | tool | 0.287 | strong |
| 9 | paper | [Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges](http://arxiv.org/abs/2605.06161v1) | 2026 | arXiv | paper | 0.287 | strong |
| 10 | paper | [Evaluating Non-English Developer Support in Machine Learning for Software Engine](http://arxiv.org/abs/2605.05902v1) | 2026 | arXiv | paper | 0.287 | strong |
| 11 | paper | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | Patterns | paper | 0.25 | strong |
| 12 | paper | [Benchmarking the reproducibility of all-solid-state battery cell performance](https://doi.org/10.1038/s41560-024-01634-3) | 2024 | Nature Energy | benchmark | 0.25 | strong |
| 13 | paper | [Reproducibility in Machine Learning-based Research: Overview, Barriers and Drive](https://doi.org/10.48550/arXiv.2406.14325) | 2024 | The AI Magazine | survey | 0.25 | strong |
| 14 | paper | [Flexible Temperature Sensor with High Reproducibility and Wireless Closed‐Loop S](https://doi.org/10.1002/adma.202407859) | 2024 | Advances in Materials | tool | 0.25 | strong |
| 15 | paper | [Reproducibility of in vivo electrophysiological measurements in mice](https://doi.org/10.1101/2022.05.09.491042) | 2024 | bioRxiv | paper | 0.25 | strong |
| 16 | paper | The Model Openness Framework: Promoting Completeness and Openness for Reproducib | 2024 |  | tool | 0.25 | strong |
| 17 | paper | [Fluorinated isopropanol for improved defect passivation and reproducibility in p](https://doi.org/10.1038/s41560-025-01791-z) | 2025 | Nature Energy | paper | 0.25 | strong |
| 18 | paper | [Assessing Consistency and Reproducibility in the Outputs of Large Language Model](https://doi.org/10.48550/arXiv.2503.16974) | 2025 | arXiv.org | paper | 0.25 | strong |
| 19 | paper | [Discordance, accuracy and reproducibility study of pathologists’ diagnosis of me](https://doi.org/10.1038/s41467-025-56160-x) | 2025 | Nature Communications | empirical | 0.25 | strong |
| 20 | paper | [fNIRS reproducibility varies with data quality, analysis pipelines, and research](https://doi.org/10.1038/s42003-025-08412-1) | 2025 | Communications Biology | empirical | 0.25 | strong |
| 21 | paper | [Open science interventions to improve reproducibility and replicability of resea](https://doi.org/10.1098/rsos.242057) | 2025 | Royal Society Open Science | survey | 0.25 | strong |
| 22 | paper | ['Publish or perish' culture blamed for reproducibility crisis.](https://doi.org/10.1038/d41586-024-04253-w) | 2025 | Nature | paper | 0.25 | strong |
| 23 | paper | [Evaluation policy and organizational evaluation capacity building: A study of in](https://doi.org/10.1002/ev.20494) | 2022 | New Directions for Evaluation | empirical | 0.25 | strong |
| 24 | paper | [An Evaluation Roadmap for a more effective government](https://doi.org/10.1002/ev.20491) | 2022 | New Directions for Evaluation | paper | 0.25 | strong |
| 25 | paper | [Program Plan Evaluation: A Participatory Approach to Bridge Plan Evaluation and ](https://doi.org/10.1177/10982140241231906) | 2024 | American Journal of Evaluation | paper | 0.25 | strong |
| 26 | paper | [Reproducibility in Management Science](https://doi.org/10.31219/osf.io/mydzv) | 2023 |  | paper | 0.25 | strong |
| 27 | paper | [Embedding evaluation theory on African philosophies: An asset to evaluation tran](https://doi.org/10.4102/aej.v12i2.735) | 2024 | African Evaluation Journal | paper | 0.25 | strong |
| 28 | paper | [After Computational Reproducibility: Scientific Reproducibility and Trustworthy ](https://doi.org/10.1162/99608f92.ea5e6f9a) | 2024 | Harvard Data Science Review | paper | 0.25 | strong |
| 29 | paper | [The Swahili evaluation approach: Content and guidance for doing development eval](https://doi.org/10.4102/aej.v12i2.739) | 2024 | African Evaluation Journal | paper | 0.25 | strong |
| 30 | paper | [Technological revolution in evaluation: Artificial intelligence and the adherenc](https://doi.org/10.1177/13563890251331066) | 2025 | Evaluation | paper | 0.25 | strong |
| 31 | paper | [Meta-evaluation: Validating program evaluation standards through the United Nati](https://doi.org/10.1177/1035719x231220979) | 2023 | Evaluation Journal of Australasia | paper | 0.25 | strong |
| 32 | paper | [Summer of Reproducibility: Building Global Capacity for Practical Reproducibilit](https://doi.org/10.1145/3736731.3746149) | 2025 | Proceedings of the 3rd ACM Conference on | paper | 0.25 | strong |
| 33 | paper | [Incorporating process evaluation into impact evaluation: what, why and how](https://doi.org/10.23846/wp0050) | 2022 |  | paper | 0.25 | strong |
| 34 | paper | [Modern LLM Evaluation Techniques: A Mathematical Framework From Classical Metric](https://doi.org/10.2139/ssrn.6531679) | 2026 |  | tool | 0.25 | strong |
| 35 | paper | [DR-100: Rubric-Based LLM-as-Judge in Machine Translation Via a Simple Meta-Evalu](https://doi.org/10.36227/techrxiv.174584742.28568002/v1) | 2025 |  | tool | 0.25 | strong |
| 36 | paper | [BioModels Reproducibility Scorecard](https://doi.org/10.52843/cassyni.x36fmy) | 2022 |  | paper | 0.25 | strong |
| 37 | paper | [Reproducibility](https://doi.org/10.5194/egusphere-2025-5497-rc1) | 2026 |  | paper | 0.25 | strong |
| 38 | paper | [Rigor and Reproducibility in Research](https://doi.org/10.4135/9781036219994) | 2024 |  | paper | 0.25 | strong |
| 39 | paper | [Validity of biomedical science, reproducibility, and irreproducibility](https://doi.org/10.1016/b978-0-443-13829-4.00013-1) | 2024 | Reproducibility in Biomedical Research | paper | 0.25 | strong |
| 40 | paper | [Committing to Reproducibility and Explainability]{Committing to Reproducibility ](https://doi.org/10.21203/rs.3.rs-2640542/v1) | 2023 |  | paper | 0.25 | strong |
| 41 | paper | [Form to Assess Result Reproducibility of Manuscripts](https://doi.org/10.1061/reprod.000001) | 2024 |  | paper | 0.25 | strong |
| 42 | paper | [Reproducibility, Transparency, Positionality? Perspectives From Different Resear](https://doi.org/10.52843/cassyni.dq8svs) | 2024 |  | paper | 0.25 | strong |
| 43 | paper | [More information needed for reproducibility](https://doi.org/10.5194/egusphere-2025-5497-cc5) | 2025 |  | paper | 0.25 | strong |
| 44 | paper | [Resolution and Reproducibility](https://doi.org/10.5194/egusphere-2024-3560-ac2) | 2025 |  | paper | 0.25 | strong |
| 45 | paper | [reproducibility, n.](https://doi.org/10.1093/oed/4082406807) | 2023 | Oxford English Dictionary | paper | 0.25 | strong |
| 46 | paper | [Reproducibility in Biomedical Research](https://doi.org/10.1016/c2022-0-02971-8) | 2024 |  | paper | 0.25 | strong |
| 47 | paper | [Transforming rural livelihoods in India: Findings from NRETP and NRLM evaluation](https://doi.org/10.23846/nrlmie149) | 2025 |  | paper | 0.25 | strong |
| 48 | paper | [Program Evaluation Tip Sheet: Economic Evaluation; and, Program Evaluation Tip S](https://doi.org/10.15620/cdc/251872) | 2026 |  | paper | 0.25 | strong |
| 49 | paper | [The garden of evaluation approaches: Supporting explicit, theory-informed evalua](https://doi.org/10.1177/13563890261421931) | 2026 | Evaluation | paper | 0.25 | strong |
| 50 | paper | [Book Review: Evaluation Time: A Practical Guide for Evaluation BarringtonGail Va](https://doi.org/10.1177/1035719x241307342) | 2024 | Evaluation Journal of Australasia | survey | 0.25 | strong |
| 51 | paper | [The African Evaluation Journal and the field of monitoring and evaluation in Afr](https://doi.org/10.4102/aej.v11i1.714) | 2023 | African Evaluation Journal | paper | 0.25 | strong |
| 52 | paper | [Social Ontology and Evaluation—
                    <i>A Comment on “Framing Eva](https://doi.org/10.1177/10982140221134779) | 2023 | American Journal of Evaluation | paper | 0.25 | strong |
| 53 | paper | Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Captu | 2026 |  | benchmark | 0.25 | strong |
| 54 | paper | [SCRuB: Social Concept Reasoning under Rubric-Based Evaluation](http://arxiv.org/abs/2605.06444v1) | 2026 | arXiv | paper | 0.25 | strong |
| 55 | paper | [Measuring Evaluation-Context Divergence in Open-Weight LLMs: A Paired-Prompt Pro](http://arxiv.org/abs/2605.06327v1) | 2026 | arXiv | paper | 0.25 | strong |
| 56 | paper | [Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human ](https://doi.org/10.48550/arXiv.2510.09738) | 2025 | arXiv.org | empirical | 0.225 | strong |
| 57 | paper | [Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Ope](https://doi.org/10.48550/arXiv.2602.05125) | 2026 | arXiv.org | paper | 0.225 | strong |
| 58 | paper | Tuning LLM Judge Design Decisions for 1/1000 of the Cost | 2025 | International Conference on Machine Lear | paper | 0.225 | strong |
| 59 | paper | [When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silentl](https://doi.org/10.48550/arXiv.2509.20293) | 2025 | arXiv.org | benchmark | 0.225 | strong |

### 1. Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ensemble Scorers
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.19254
- **Year/Venue**: 2025 / Trans. Mach. Learn. Res.
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ense' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|syn:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. A Benchmark for Long-Form Medical Question Answering
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2411.09834
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.29: paper titled 'A Benchmark for Long-Form Medical Question Answering' contributes a 'benchmark' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. Agentic Program Repair from Test Failures at Scale: A Neuro-symbolic approach with static analysis and test execution fe
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2507.18755
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.29: paper titled 'Agentic Program Repair from Test Failures at Scale: A Neuro-symbolic approach with static analysis a' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. Rethinking Retrieval: From Traditional Retrieval Augmented Generation to Agentic and Non-Vector Reasoning Systems in the
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2511.18177
- **Year/Venue**: 2025 / Proceedings of the 18th International Conference on Agents and Artificial Intelligence
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.29: paper titled 'Rethinking Retrieval: From Traditional Retrieval Augmented Generation to Agentic and Non-Vector Reas' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. DeEscalWild: A Real-World Benchmark for Automated De-Escalation Training with SLMs
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2026 / n/a
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.29: paper titled 'DeEscalWild: A Real-World Benchmark for Automated De-Escalation Training with SLMs' contributes a 'benchmark' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06635v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.29: paper titled 'Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. Autonomous Adversary: Red-Teaming in the age of LLM
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06486v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.29: paper titled 'Autonomous Adversary: Red-Teaming in the age of LLM' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Joint Consistency: A Unified Test-Time Aggregation Framework via Energy Minimization
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06219v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.29: paper titled 'Joint Consistency: A Unified Test-Time Aggregation Framework via Energy Minimization' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06161v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.29: paper titled 'Beyond Accuracy: Policy Invariance as a Reliability Test for LLM Safety Judges' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Evaluating Non-English Developer Support in Machine Learning for Software Engineering
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.05902v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.29: paper titled 'Evaluating Non-English Developer Support in Machine Learning for Software Engineering' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: primary:abstract:llm-as-a-judge|kw:abstract:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. Leakage and the reproducibility crisis in machine-learning-based science
- **Source**: paper  **URL**: https://doi.org/10.1016/j.patter.2023.100804
- **Year/Venue**: 2023 / Patterns
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Leakage and the reproducibility crisis in machine-learning-based science' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. Benchmarking the reproducibility of all-solid-state battery cell performance
- **Source**: paper  **URL**: https://doi.org/10.1038/s41560-024-01634-3
- **Year/Venue**: 2024 / Nature Energy
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'Benchmarking the reproducibility of all-solid-state battery cell performance' contributes a 'benchmark' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. Reproducibility in Machine Learning-based Research: Overview, Barriers and Drivers
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2406.14325
- **Year/Venue**: 2024 / The AI Magazine
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility in Machine Learning-based Research: Overview, Barriers and Drivers' contributes a 'survey' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 14. Flexible Temperature Sensor with High Reproducibility and Wireless Closed‐Loop System for Decoupled Multimodal Health Mo
- **Source**: paper  **URL**: https://doi.org/10.1002/adma.202407859
- **Year/Venue**: 2024 / Advances in Materials
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'Flexible Temperature Sensor with High Reproducibility and Wireless Closed‐Loop System for Decoupled ' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 15. Reproducibility of in vivo electrophysiological measurements in mice
- **Source**: paper  **URL**: https://doi.org/10.1101/2022.05.09.491042
- **Year/Venue**: 2024 / bioRxiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility of in vivo electrophysiological measurements in mice' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 16. The Model Openness Framework: Promoting Completeness and Openness for Reproducibility, Transparency, and Usability in Ar
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2024 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'The Model Openness Framework: Promoting Completeness and Openness for Reproducibility, Transparency,' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 17. Fluorinated isopropanol for improved defect passivation and reproducibility in perovskite solar cells
- **Source**: paper  **URL**: https://doi.org/10.1038/s41560-025-01791-z
- **Year/Venue**: 2025 / Nature Energy
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Fluorinated isopropanol for improved defect passivation and reproducibility in perovskite solar cell' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 18. Assessing Consistency and Reproducibility in the Outputs of Large Language Models: Evidence Across Diverse Finance and A
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2503.16974
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Assessing Consistency and Reproducibility in the Outputs of Large Language Models: Evidence Across D' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 19. Discordance, accuracy and reproducibility study of pathologists’ diagnosis of melanoma and melanocytic tumors
- **Source**: paper  **URL**: https://doi.org/10.1038/s41467-025-56160-x
- **Year/Venue**: 2025 / Nature Communications
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'Discordance, accuracy and reproducibility study of pathologists’ diagnosis of melanoma and melanocyt' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 20. fNIRS reproducibility varies with data quality, analysis pipelines, and researcher experience
- **Source**: paper  **URL**: https://doi.org/10.1038/s42003-025-08412-1
- **Year/Venue**: 2025 / Communications Biology
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'fNIRS reproducibility varies with data quality, analysis pipelines, and researcher experience' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 21. Open science interventions to improve reproducibility and replicability of research: a scoping review
- **Source**: paper  **URL**: https://doi.org/10.1098/rsos.242057
- **Year/Venue**: 2025 / Royal Society Open Science
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.25: paper titled 'Open science interventions to improve reproducibility and replicability of research: a scoping revie' contributes a 'survey' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 22. 'Publish or perish' culture blamed for reproducibility crisis.
- **Source**: paper  **URL**: https://doi.org/10.1038/d41586-024-04253-w
- **Year/Venue**: 2025 / Nature
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled ''Publish or perish' culture blamed for reproducibility crisis.' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 23. Evaluation policy and organizational evaluation capacity building: A study of international aid agency evaluation polici
- **Source**: paper  **URL**: https://doi.org/10.1002/ev.20494
- **Year/Venue**: 2022 / New Directions for Evaluation
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'Evaluation policy and organizational evaluation capacity building: A study of international aid agen' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 24. An Evaluation Roadmap for a more effective government
- **Source**: paper  **URL**: https://doi.org/10.1002/ev.20491
- **Year/Venue**: 2022 / New Directions for Evaluation
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'An Evaluation Roadmap for a more effective government' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 25. Program Plan Evaluation: A Participatory Approach to Bridge Plan Evaluation and Program Evaluation
- **Source**: paper  **URL**: https://doi.org/10.1177/10982140241231906
- **Year/Venue**: 2024 / American Journal of Evaluation
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Program Plan Evaluation: A Participatory Approach to Bridge Plan Evaluation and Program Evaluation' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 26. Reproducibility in Management Science
- **Source**: paper  **URL**: https://doi.org/10.31219/osf.io/mydzv
- **Year/Venue**: 2023 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility in Management Science' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 27. Embedding evaluation theory on African philosophies: An asset to evaluation transformation
- **Source**: paper  **URL**: https://doi.org/10.4102/aej.v12i2.735
- **Year/Venue**: 2024 / African Evaluation Journal
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Embedding evaluation theory on African philosophies: An asset to evaluation transformation' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 28. After Computational Reproducibility: Scientific Reproducibility and Trustworthy AI
- **Source**: paper  **URL**: https://doi.org/10.1162/99608f92.ea5e6f9a
- **Year/Venue**: 2024 / Harvard Data Science Review
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'After Computational Reproducibility: Scientific Reproducibility and Trustworthy AI' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 29. The Swahili evaluation approach: Content and guidance for doing development evaluation
- **Source**: paper  **URL**: https://doi.org/10.4102/aej.v12i2.739
- **Year/Venue**: 2024 / African Evaluation Journal
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Swahili evaluation approach: Content and guidance for doing development evaluation' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 30. Technological revolution in evaluation: Artificial intelligence and the adherence to evaluation standards
- **Source**: paper  **URL**: https://doi.org/10.1177/13563890251331066
- **Year/Venue**: 2025 / Evaluation
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Technological revolution in evaluation: Artificial intelligence and the adherence to evaluation stan' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 31. Meta-evaluation: Validating program evaluation standards through the United Nations Evaluation Quality Assessment (EQAs)
- **Source**: paper  **URL**: https://doi.org/10.1177/1035719x231220979
- **Year/Venue**: 2023 / Evaluation Journal of Australasia
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Meta-evaluation: Validating program evaluation standards through the United Nations Evaluation Quali' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 32. Summer of Reproducibility: Building Global Capacity for Practical Reproducibility through Hands-On Mentorship
- **Source**: paper  **URL**: https://doi.org/10.1145/3736731.3746149
- **Year/Venue**: 2025 / Proceedings of the 3rd ACM Conference on Reproducibility and Replicability
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Summer of Reproducibility: Building Global Capacity for Practical Reproducibility through Hands-On M' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 33. Incorporating process evaluation into impact evaluation: what, why and how
- **Source**: paper  **URL**: https://doi.org/10.23846/wp0050
- **Year/Venue**: 2022 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Incorporating process evaluation into impact evaluation: what, why and how' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 34. Modern LLM Evaluation Techniques: A Mathematical Framework From Classical Metrics to LLM-as-Judge and Psychometric Found
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6531679
- **Year/Venue**: 2026 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'Modern LLM Evaluation Techniques: A Mathematical Framework From Classical Metrics to LLM-as-Judge an' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 35. DR-100: Rubric-Based LLM-as-Judge in Machine Translation Via a Simple Meta-Evaluation Framework
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.174584742.28568002/v1
- **Year/Venue**: 2025 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'DR-100: Rubric-Based LLM-as-Judge in Machine Translation Via a Simple Meta-Evaluation Framework' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 36. BioModels Reproducibility Scorecard
- **Source**: paper  **URL**: https://doi.org/10.52843/cassyni.x36fmy
- **Year/Venue**: 2022 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'BioModels Reproducibility Scorecard' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 37. Reproducibility
- **Source**: paper  **URL**: https://doi.org/10.5194/egusphere-2025-5497-rc1
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 38. Rigor and Reproducibility in Research
- **Source**: paper  **URL**: https://doi.org/10.4135/9781036219994
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Rigor and Reproducibility in Research' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 39. Validity of biomedical science, reproducibility, and irreproducibility
- **Source**: paper  **URL**: https://doi.org/10.1016/b978-0-443-13829-4.00013-1
- **Year/Venue**: 2024 / Reproducibility in Biomedical Research
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Validity of biomedical science, reproducibility, and irreproducibility' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 40. Committing to Reproducibility and Explainability]{Committing to Reproducibility and Explainability: Version Control as R
- **Source**: paper  **URL**: https://doi.org/10.21203/rs.3.rs-2640542/v1
- **Year/Venue**: 2023 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Committing to Reproducibility and Explainability]{Committing to Reproducibility and Explainability: ' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 41. Form to Assess Result Reproducibility of Manuscripts
- **Source**: paper  **URL**: https://doi.org/10.1061/reprod.000001
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Form to Assess Result Reproducibility of Manuscripts' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 42. Reproducibility, Transparency, Positionality? Perspectives From Different Research Fields
- **Source**: paper  **URL**: https://doi.org/10.52843/cassyni.dq8svs
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility, Transparency, Positionality? Perspectives From Different Research Fields' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 43. More information needed for reproducibility
- **Source**: paper  **URL**: https://doi.org/10.5194/egusphere-2025-5497-cc5
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'More information needed for reproducibility' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 44. Resolution and Reproducibility
- **Source**: paper  **URL**: https://doi.org/10.5194/egusphere-2024-3560-ac2
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Resolution and Reproducibility' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 45. reproducibility, n.
- **Source**: paper  **URL**: https://doi.org/10.1093/oed/4082406807
- **Year/Venue**: 2023 / Oxford English Dictionary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'reproducibility, n.' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 46. Reproducibility in Biomedical Research
- **Source**: paper  **URL**: https://doi.org/10.1016/c2022-0-02971-8
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility in Biomedical Research' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 47. Transforming rural livelihoods in India: Findings from NRETP and NRLM evaluation
- **Source**: paper  **URL**: https://doi.org/10.23846/nrlmie149
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Transforming rural livelihoods in India: Findings from NRETP and NRLM evaluation' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 48. Program Evaluation Tip Sheet: Economic Evaluation; and, Program Evaluation Tip Sheet: Reach and Impact [August 2011]
- **Source**: paper  **URL**: https://doi.org/10.15620/cdc/251872
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Program Evaluation Tip Sheet: Economic Evaluation; and, Program Evaluation Tip Sheet: Reach and Impa' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 49. The garden of evaluation approaches: Supporting explicit, theory-informed evaluation practice
- **Source**: paper  **URL**: https://doi.org/10.1177/13563890261421931
- **Year/Venue**: 2026 / Evaluation
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The garden of evaluation approaches: Supporting explicit, theory-informed evaluation practice' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 50. Book Review: Evaluation Time: A Practical Guide for Evaluation BarringtonGail VallanceTriana-TremainBeverly. (2022). Eva
- **Source**: paper  **URL**: https://doi.org/10.1177/1035719x241307342
- **Year/Venue**: 2024 / Evaluation Journal of Australasia
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.25: paper titled 'Book Review: Evaluation Time: A Practical Guide for Evaluation BarringtonGail VallanceTriana-Tremain' contributes a 'survey' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 51. The African Evaluation Journal and the field of monitoring and evaluation in Africa
- **Source**: paper  **URL**: https://doi.org/10.4102/aej.v11i1.714
- **Year/Venue**: 2023 / African Evaluation Journal
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The African Evaluation Journal and the field of monitoring and evaluation in Africa' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 52. Social Ontology and Evaluation—
                    <i>A Comment on “Framing Evaluation in Reality: An Introduction to O
- **Source**: paper  **URL**: https://doi.org/10.1177/10982140221134779
- **Year/Venue**: 2023 / American Journal of Evaluation
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Social Ontology and Evaluation—
                    <i>A Comment on “Framing Evaluation in Reality: ' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 53. Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Capture the Flag Challenges
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2026 / n/a
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'Do Agents Dream of Root Shells? Partial-Credit Evaluation of LLM Agents in Capture the Flag Challeng' contributes a 'benchmark' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 54. SCRuB: Social Concept Reasoning under Rubric-Based Evaluation
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06444v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'SCRuB: Social Concept Reasoning under Rubric-Based Evaluation' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 55. Measuring Evaluation-Context Divergence in Open-Weight LLMs: A Paired-Prompt Protocol with Pilot Evidence of Alignment-P
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06327v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Measuring Evaluation-Context Divergence in Open-Weight LLMs: A Paired-Prompt Protocol with Pilot Evi' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 56. Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.09738
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.23: paper titled 'Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: kw:abstract:evaluation|syn:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 57. Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2602.05125
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.23: paper titled 'Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:abstract:evaluation|syn:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 58. Tuning LLM Judge Design Decisions for 1/1000 of the Cost
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.23: paper titled 'Tuning LLM Judge Design Decisions for 1/1000 of the Cost' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:abstract:reproducibility|syn:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 59. When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2509.20293
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.23: paper titled 'When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity' contributes a 'benchmark' matching target artifact 'database+paper'. Matched keywords: kw:abstract:evaluation|syn:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of LLM-judge papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

## Artifact Differentiator Checklist

Answer each question to establish whether our proposed contribution is distinct:

- [ ] **Peer-reviewed vs repo**: Is our contribution a peer-reviewed paper (not just a code dump)?
- [ ] **Systematic protocol**: Does our benchmark/dataset follow a documented, reproducible protocol unlike existing repos?
- [ ] **Domain-specific**: Does our work target a specific domain (clinical, legal, finance) while existing artifacts are general?
- [ ] **Evaluation focus**: Are we *evaluating behavior* (robustness, bias, sensitivity) rather than merely collecting prompts?
- [ ] **LLM-judge-specific**: Do we target LLM-as-a-judge specifically, not general prompt injection?
- [ ] **Reproducibility harness**: Do we release evaluation code + results, not just raw data?

## Recommended Actions

1. **Do not promote T10 to GO** — 3 peer-reviewed paper(s) directly cover this.
2. For each DIRECT paper, fill 'how_we_differ' in the CSV with a specific contribution claim.
3. If no differentiator: consider DROP or further narrowing.
