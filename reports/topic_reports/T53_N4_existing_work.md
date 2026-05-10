# Existing Work Report — T53_N4: Test-set contamination audit of healthcare LLM benchmarks — noise-pruned

> ⚠️ **DIFFERENTIATOR REQUIRED** — paper_direct=0, artifact_direct=6; paper_strength=`strong`, artifact_strength=`strong`.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 2 |
| HuggingFace direct artifacts | 4 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 6 |
| Artifact diff strength | `strong` |
| Partial overlaps (total) | 38 |
| Adjacent | 1 |
| Total findings | 45 |
| peer_reviewed_direct | No |
| high_artifact_overlap | No |
| GO blocked | No |
| Differentiator required | Yes |
| Artifact differentiator required | Yes |

## Peer-Reviewed Direct Overlaps

_None._

## Artifact Direct Overlaps (GitHub / HF / PWC)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | github | [SeekingDream/Static-to-Dynamic-LLMEval](https://github.com/SeekingDream/Static-to-Dynamic-LLMEval) |  | GitHub | benchmark | 503 | strong |
| 2 | github | [SeekingDream/DyCodeEval](https://github.com/SeekingDream/DyCodeEval) |  | GitHub | benchmark | 235 | strong |
| 3 | huggingface | [qiaojin/PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA) |  | HuggingFace | dataset | 32315 | strong |
| 4 | huggingface | [fedml/PubMedQA_instruction](https://huggingface.co/datasets/fedml/PubMedQA_instruction) |  | HuggingFace | dataset | 999 | strong |
| 5 | huggingface | [MedSwin/PubMedQA-u-RAG](https://huggingface.co/datasets/MedSwin/PubMedQA-u-RAG) |  | HuggingFace | dataset | 323 | strong |
| 6 | huggingface | [bigbio/pubmed_qa](https://huggingface.co/datasets/bigbio/pubmed_qa) |  | HuggingFace | dataset | 6824 | strong |

### 1. SeekingDream/Static-to-Dynamic-LLMEval
- **Source**: github  **URL**: https://github.com/SeekingDream/Static-to-Dynamic-LLMEval
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'SeekingDream/Static-to-Dynamic-LLMEval' (503 stars) provides an implementation of 'data contamination'. Description: the official github repository of the paper "recent advances in large language model benchmarks against data contaminati.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. SeekingDream/DyCodeEval
- **Source**: github  **URL**: https://github.com/SeekingDream/DyCodeEval
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'SeekingDream/DyCodeEval' (235 stars) provides an implementation of 'data contamination'. Description: official repository of the icml2025 paper “dynamic benchmarking of reasoning capabilities in code large language models .
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. qiaojin/PubMedQA
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/qiaojin/PubMedQA
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'qiaojin/PubMedQA' (32,315 downloads) matched 'PubMedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. fedml/PubMedQA_instruction
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/fedml/PubMedQA_instruction
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'fedml/PubMedQA_instruction' (999 downloads) matched 'PubMedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. MedSwin/PubMedQA-u-RAG
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/MedSwin/PubMedQA-u-RAG
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'MedSwin/PubMedQA-u-RAG' (323 downloads) matched 'PubMedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. bigbio/pubmed_qa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/bigbio/pubmed_qa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'bigbio/pubmed_qa' (6,824 downloads) matched 'PubMedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Generalization or Memorization: Data Contamination and Trustworthy Evaluation fo](https://doi.org/10.48550/arXiv.2402.15938) | 2024 | Annual Meeting of the Association for Co | paper | 0.625 | moderate |
| 2 | paper | [Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to D](https://doi.org/10.48550/arXiv.2507.10532) | 2025 | AAAI Conference on Artificial Intelligen | paper | 0.625 | moderate |
| 3 | paper | [Data Contamination or Genuine Generalization? Disentangling LLM Performance on B](https://doi.org/10.70393/616a6e73.323836) | 2025 | Academic Journal of Natural Science | benchmark | 0.6 | moderate |
| 4 | paper | [Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large La](https://doi.org/10.1162/tacl.a.20) | 2025 | Transactions of the Association for Comp | tool | 0.55 | moderate |
| 5 | paper | [Detecting Data Contamination in LLMs via In-Context Learning](https://doi.org/10.48550/arXiv.2510.27055) | 2025 | arXiv.org | paper | 0.55 | moderate |
| 6 | paper | [NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for eac](https://doi.org/10.48550/arXiv.2310.18018) | 2023 | Conference on Empirical Methods in Natur | benchmark | 0.5 | moderate |
| 7 | paper | [Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-So](https://doi.org/10.48550/arXiv.2402.03927) | 2024 | Conference of the European Chapter of th | paper | 0.5 | moderate |
| 8 | paper | [Benchmark Data Contamination of Large Language Models: A Survey](https://doi.org/10.48550/arXiv.2406.04244) | 2024 | arXiv.org | benchmark | 0.5 | moderate |
| 9 | paper | [Investigating Data Contamination for Pre-training Language Models](https://doi.org/10.48550/arXiv.2401.06059) | 2024 | arXiv.org | paper | 0.5 | moderate |
| 10 | paper | [AntiLeak-Bench: Preventing Data Contamination by Automatically Constructing Benc](https://doi.org/10.48550/arXiv.2412.13670) | 2024 | Annual Meeting of the Association for Co | benchmark | 0.5 | moderate |
| 11 | paper | [Evading Data Contamination Detection for Language Models is (too) Easy](https://doi.org/10.48550/arXiv.2402.02823) | 2024 | arXiv.org | paper | 0.5 | moderate |
| 12 | paper | [Evaluation data contamination in LLMs: how do we measure it and (when) does it m](https://doi.org/10.48550/arXiv.2411.03923) | 2024 | arXiv.org | paper | 0.5 | moderate |
| 13 | paper | [Recent Advances in Large Langauge Model Benchmarks against Data Contamination: F](https://doi.org/10.48550/arXiv.2502.17521) | 2025 | arXiv.org | benchmark | 0.5 | moderate |
| 14 | paper | [Data Contamination Calibration for Black-box LLMs](https://doi.org/10.48550/arXiv.2405.11930) | 2024 | Annual Meeting of the Association for Co | paper | 0.5 | moderate |
| 15 | paper | [A Survey on Data Contamination for Large Language Models](https://doi.org/10.48550/arXiv.2502.14425) | 2025 | arXiv.org | survey | 0.5 | moderate |
| 16 | paper | [Dynamic Benchmarking of Reasoning Capabilities in Code Large Language Models Und](https://doi.org/10.48550/arXiv.2503.04149) | 2025 | International Conference on Machine Lear | benchmark | 0.5 | moderate |
| 17 | paper | [Benchmarking Large Language Models Under Data Contamination: A Survey from Stati](https://doi.org/10.18653/v1/2025.emnlp-main.511) | 2025 | Conference on Empirical Methods in Natur | benchmark | 0.5 | moderate |
| 18 | paper | [VeriContaminated: Assessing LLM-Driven Verilog Coding for Data Contamination](https://doi.org/10.1109/ICLAD65226.2025.00017) | 2025 | 2025 IEEE International Conference on LL | paper | 0.5 | moderate |
| 19 | paper | [Overestimation in LLM Evaluation: A Controlled Large-Scale Study on Data Contami](https://doi.org/10.48550/arXiv.2501.18771) | 2025 | International Conference on Machine Lear | empirical | 0.5 | moderate |
| 20 | paper | [Search-Time Data Contamination](https://doi.org/10.48550/arXiv.2508.13180) | 2025 | arXiv.org | paper | 0.5 | moderate |
| 21 | paper | [The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation ](https://doi.org/10.48550/arXiv.2503.16402) | 2025 | International Conference on Machine Lear | benchmark | 0.5 | moderate |
| 22 | paper | [Beyond Next Token Probabilities: Learnable, Fast Detection of Hallucinations and](https://doi.org/10.1609/aaai.v40i36.40254) | 2025 | AAAI Conference on Artificial Intelligen | paper | 0.5 | moderate |
| 23 | paper | [DCR: Quantifying Data Contamination in LLMs Evaluation](https://doi.org/10.48550/arXiv.2507.11405) | 2025 | Conference on Empirical Methods in Natur | paper | 0.5 | moderate |
| 24 | paper | [Detecting Data Contamination from Reinforcement Learning Post-training for Large](https://doi.org/10.48550/arXiv.2510.09259) | 2025 | arXiv.org | paper | 0.5 | moderate |
| 25 | paper | [A Taxonomy for Data Contamination in Large Language Models](https://doi.org/10.18653/v1/2024.conda-1.3) | 2024 | Proceedings of the 1st Workshop on Data  | survey | 0.5 | moderate |
| 26 | paper | [Confounders in Instance Variation for the Analysis of Data Contamination](https://doi.org/10.18653/v1/2024.conda-1.2) | 2024 | Proceedings of the 1st Workshop on Data  | empirical | 0.5 | moderate |
| 27 | paper | [Analysis of Semantic Benchmark Data Contamination Attack for LLM-Driven Fake New](https://doi.org/10.1109/BigData66926.2025.11402039) | 2025 | BigData Congress [Services Society] | benchmark | 0.5 | moderate |
| 28 | paper | [Proceedings of the 1st Workshop on Data Contamination (CONDA)](https://doi.org/10.18653/v1/2024.conda-1) | 2024 |  | paper | 0.5 | moderate |
| 29 | paper | [Data Contamination in AI Evaluation (Preprint)](https://doi.org/10.2196/preprints.80987) | 2025 |  | paper | 0.5 | moderate |
| 30 | paper | [Density Deconvolution with Limited Data Contamination](https://doi.org/10.2139/ssrn.4916179) | 2024 | SSRN Electronic Journal | paper | 0.5 | moderate |
| 31 | paper | [Data Contamination in AI Evaluation](https://doi.org/10.2196/80987) | 2025 | JMIR Medical Informatics | paper | 0.5 | moderate |
| 32 | paper | [Data Contamination in LLMs: A Scoping Literature Review](https://doi.org/10.37766/inplasy2025.11.0050) | 2025 |  | survey | 0.5 | moderate |
| 33 | paper | [Fully Unsupervised Anomaly Detection in Industrial Images with Unknown Data Cont](https://doi.org/10.1109/sds66131.2025.00013) | 2025 | 2025 IEEE Swiss Conference on Data Scien | paper | 0.5 | moderate |
| 34 | github | [liyucheng09/Contamination_Detector](https://github.com/liyucheng09/Contamination_Detector) |  | GitHub | tool | 52 | moderate |
| 35 | huggingface | [tan9/pubmedQA](https://huggingface.co/datasets/tan9/pubmedQA) |  | HuggingFace | dataset | 69 | moderate |
| 36 | huggingface | [pythonist/PubMedQA](https://huggingface.co/datasets/pythonist/PubMedQA) |  | HuggingFace | dataset | 30 | moderate |
| 37 | huggingface | [reginaboateng/cleaned_pubmedqa](https://huggingface.co/datasets/reginaboateng/cleaned_pubmedqa) |  | HuggingFace | dataset | 22 | moderate |
| 38 | huggingface | [highnote/pubmed_qa](https://huggingface.co/datasets/highnote/pubmed_qa) |  | HuggingFace | dataset | 24 | moderate |

### 1. Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2402.15938
- **Year/Venue**: 2024 / Annual Meeting of the Association for Computational Linguistics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.62: paper titled 'Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Mod' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination|syn:title:memorization.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2507.10532
- **Year/Venue**: 2025 / AAAI Conference on Artificial Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.62: paper titled 'Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination|syn:title:memorization.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. Data Contamination or Genuine Generalization? Disentangling LLM Performance on Benchmarks
- **Source**: paper  **URL**: https://doi.org/10.70393/616a6e73.323836
- **Year/Venue**: 2025 / Academic Journal of Natural Science
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.60: paper titled 'Data Contamination or Genuine Generalization? Disentangling LLM Performance on Benchmarks' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination|syn:abstract:memorization|syn:abstract:n-gram overlap.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.1162/tacl.a.20
- **Year/Venue**: 2025 / Transactions of the Association for Computational Linguistics
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.55: paper titled 'Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models' contributes a 'tool' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination|syn:abstract:memorization.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. Detecting Data Contamination in LLMs via In-Context Learning
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.27055
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.55: paper titled 'Detecting Data Contamination in LLMs via In-Context Learning' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination|syn:abstract:memorization.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2310.18018
- **Year/Venue**: 2023 / Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2402.03927
- **Year/Venue**: 2024 / Conference of the European Chapter of the Association for Computational Linguistics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. Benchmark Data Contamination of Large Language Models: A Survey
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2406.04244
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Benchmark Data Contamination of Large Language Models: A Survey' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. Investigating Data Contamination for Pre-training Language Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2401.06059
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Investigating Data Contamination for Pre-training Language Models' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. AntiLeak-Bench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2412.13670
- **Year/Venue**: 2024 / Annual Meeting of the Association for Computational Linguistics
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'AntiLeak-Bench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated ' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. Evading Data Contamination Detection for Language Models is (too) Easy
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2402.02823
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Evading Data Contamination Detection for Language Models is (too) Easy' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2411.03923
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 13. Recent Advances in Large Langauge Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2502.17521
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Recent Advances in Large Langauge Model Benchmarks against Data Contamination: From Static to Dynami' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 14. Data Contamination Calibration for Black-box LLMs
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2405.11930
- **Year/Venue**: 2024 / Annual Meeting of the Association for Computational Linguistics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Data Contamination Calibration for Black-box LLMs' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 15. A Survey on Data Contamination for Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2502.14425
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'A Survey on Data Contamination for Large Language Models' contributes a 'survey' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 16. Dynamic Benchmarking of Reasoning Capabilities in Code Large Language Models Under Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2503.04149
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Dynamic Benchmarking of Reasoning Capabilities in Code Large Language Models Under Data Contaminatio' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 17. Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2025.emnlp-main.511
- **Year/Venue**: 2025 / Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluat' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 18. VeriContaminated: Assessing LLM-Driven Verilog Coding for Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.1109/ICLAD65226.2025.00017
- **Year/Venue**: 2025 / 2025 IEEE International Conference on LLM-Aided Design (ICLAD)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'VeriContaminated: Assessing LLM-Driven Verilog Coding for Data Contamination' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 19. Overestimation in LLM Evaluation: A Controlled Large-Scale Study on Data Contamination's Impact on Machine Translation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2501.18771
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.50: paper titled 'Overestimation in LLM Evaluation: A Controlled Large-Scale Study on Data Contamination's Impact on M' contributes a 'empirical' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 20. Search-Time Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2508.13180
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Search-Time Data Contamination' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 21. The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contam
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2503.16402
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM B' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 22. Beyond Next Token Probabilities: Learnable, Fast Detection of Hallucinations and Data Contamination on LLM Output Distri
- **Source**: paper  **URL**: https://doi.org/10.1609/aaai.v40i36.40254
- **Year/Venue**: 2025 / AAAI Conference on Artificial Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Beyond Next Token Probabilities: Learnable, Fast Detection of Hallucinations and Data Contamination ' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 23. DCR: Quantifying Data Contamination in LLMs Evaluation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2507.11405
- **Year/Venue**: 2025 / Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'DCR: Quantifying Data Contamination in LLMs Evaluation' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 24. Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.09259
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 25. A Taxonomy for Data Contamination in Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2024.conda-1.3
- **Year/Venue**: 2024 / Proceedings of the 1st Workshop on Data Contamination (CONDA)
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'A Taxonomy for Data Contamination in Large Language Models' contributes a 'survey' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 26. Confounders in Instance Variation for the Analysis of Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2024.conda-1.2
- **Year/Venue**: 2024 / Proceedings of the 1st Workshop on Data Contamination (CONDA)
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.50: paper titled 'Confounders in Instance Variation for the Analysis of Data Contamination' contributes a 'empirical' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 27. Analysis of Semantic Benchmark Data Contamination Attack for LLM-Driven Fake News Detection
- **Source**: paper  **URL**: https://doi.org/10.1109/BigData66926.2025.11402039
- **Year/Venue**: 2025 / BigData Congress [Services Society]
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Analysis of Semantic Benchmark Data Contamination Attack for LLM-Driven Fake News Detection' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 28. Proceedings of the 1st Workshop on Data Contamination (CONDA)
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2024.conda-1
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Proceedings of the 1st Workshop on Data Contamination (CONDA)' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 29. Data Contamination in AI Evaluation (Preprint)
- **Source**: paper  **URL**: https://doi.org/10.2196/preprints.80987
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Data Contamination in AI Evaluation (Preprint)' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 30. Density Deconvolution with Limited Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.4916179
- **Year/Venue**: 2024 / SSRN Electronic Journal
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Density Deconvolution with Limited Data Contamination' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 31. Data Contamination in AI Evaluation
- **Source**: paper  **URL**: https://doi.org/10.2196/80987
- **Year/Venue**: 2025 / JMIR Medical Informatics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Data Contamination in AI Evaluation' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 32. Data Contamination in LLMs: A Scoping Literature Review
- **Source**: paper  **URL**: https://doi.org/10.37766/inplasy2025.11.0050
- **Year/Venue**: 2025 / n/a
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'Data Contamination in LLMs: A Scoping Literature Review' contributes a 'survey' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 33. Fully Unsupervised Anomaly Detection in Industrial Images with Unknown Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.1109/sds66131.2025.00013
- **Year/Venue**: 2025 / 2025 IEEE Swiss Conference on Data Science (SDS)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Fully Unsupervised Anomaly Detection in Industrial Images with Unknown Data Contamination' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 34. liyucheng09/Contamination_Detector
- **Source**: github  **URL**: https://github.com/liyucheng09/Contamination_Detector
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'liyucheng09/Contamination_Detector' (52 stars) provides an implementation of 'data contamination'. Description: lightweight tool to identify data contamination in llms evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 35. tan9/pubmedQA
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/tan9/pubmedQA
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'tan9/pubmedQA' (69 downloads) matched 'PubMedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 36. pythonist/PubMedQA
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/pythonist/PubMedQA
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'pythonist/PubMedQA' (30 downloads) matched 'PubMedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 37. reginaboateng/cleaned_pubmedqa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/reginaboateng/cleaned_pubmedqa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'reginaboateng/cleaned_pubmedqa' (22 downloads) matched 'PubMedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 38. highnote/pubmed_qa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/highnote/pubmed_qa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'highnote/pubmed_qa' (24 downloads) matched 'PubMedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Benchmark Leakage, Plasticity Loss, and Regime Transitions in Large Language Mod](https://doi.org/10.2139/ssrn.6084208) | 2026 |  | benchmark | 0.25 | strong |

### 1. Benchmark Leakage, Plasticity Loss, and Regime Transitions in Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6084208
- **Year/Venue**: 2026 / n/a
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'Benchmark Leakage, Plasticity Loss, and Regime Transitions in Large Language Models' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: kw:title:benchmark leakage.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks — noise-pruned'. Narrowing note: removed noisy secondaries=['MedQA']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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

1. Complete the Artifact Differentiator Checklist above (6 artifacts found).
2. This topic can proceed to GO if artifact differentiator is articulated explicitly.
3. Write one paragraph for §6 verification log explaining differentiation from top artifacts.
