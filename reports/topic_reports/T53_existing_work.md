# Existing Work Report — T53: Test-set contamination audit of healthcare LLM benchmarks

> ⚠️ **ARTIFACT DIFFERENTIATOR REQUIRED** — 11 direct artifact(s) (GitHub=2, HF=9, PWC=0), no peer-reviewed paper overlap. artifact_diff_strength=`strong`. Our peer-reviewed contribution is inherently different, but must be explicit.

> 📌 **Note (artifact-only overlap):** Academic/paper overlap appears low, but artifact overlap is high (11 direct artifacts). This topic may still be publishable — a peer-reviewed benchmark/protocol with a clear domain or methodological focus is inherently differentiated from GitHub repos and HuggingFace datasets. Explicitly state: (1) peer-reviewed systematic protocol vs existing repos; (2) specific domain/use-case vs general artifacts; (3) evaluation harness + reproducibility package vs raw data.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 2 |
| HuggingFace direct artifacts | 9 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 11 |
| Artifact diff strength | `strong` |
| Partial overlaps (total) | 45 |
| Adjacent | 14 |
| Total findings | 70 |
| peer_reviewed_direct | No |
| high_artifact_overlap | ⚠️ Yes |
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
| 3 | huggingface | [GBaker/MedQA-USMLE-4-options](https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options) |  | HuggingFace | dataset | 17631 | strong |
| 4 | huggingface | [GBaker/MedQA-USMLE-4-options-hf](https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options-hf) |  | HuggingFace | dataset | 8554 | strong |
| 5 | huggingface | [katielink/nejm-medqa-diagnostic-reasoning-dataset](https://huggingface.co/datasets/katielink/nejm-medqa-diagnostic-reasoning-dataset) |  | HuggingFace | dataset | 224 | strong |
| 6 | huggingface | [Williamsanderson/MedQA-Darija-MultiLingual](https://huggingface.co/datasets/Williamsanderson/MedQA-Darija-MultiLingual) |  | HuggingFace | dataset | 53285 | strong |
| 7 | huggingface | [bigbio/med_qa](https://huggingface.co/datasets/bigbio/med_qa) |  | HuggingFace | dataset | 3857 | strong |
| 8 | huggingface | [medalpaca/medical_meadow_medqa](https://huggingface.co/datasets/medalpaca/medical_meadow_medqa) |  | HuggingFace | dataset | 3205 | strong |
| 9 | huggingface | [truehealth/medqa](https://huggingface.co/datasets/truehealth/medqa) |  | HuggingFace | dataset | 348 | strong |
| 10 | huggingface | [augtoma/medqa_usmle](https://huggingface.co/datasets/augtoma/medqa_usmle) |  | HuggingFace | dataset | 178 | strong |
| 11 | huggingface | [VodLM/medqa](https://huggingface.co/datasets/VodLM/medqa) |  | HuggingFace | dataset | 214 | strong |

### 1. SeekingDream/Static-to-Dynamic-LLMEval
- **Source**: github  **URL**: https://github.com/SeekingDream/Static-to-Dynamic-LLMEval
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'SeekingDream/Static-to-Dynamic-LLMEval' (503 stars) provides an implementation of 'data contamination'. Description: the official github repository of the paper "recent advances in large language model benchmarks against data contaminati.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. SeekingDream/DyCodeEval
- **Source**: github  **URL**: https://github.com/SeekingDream/DyCodeEval
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'SeekingDream/DyCodeEval' (235 stars) provides an implementation of 'data contamination'. Description: official repository of the icml2025 paper “dynamic benchmarking of reasoning capabilities in code large language models .
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. GBaker/MedQA-USMLE-4-options
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'GBaker/MedQA-USMLE-4-options' (17,631 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. GBaker/MedQA-USMLE-4-options-hf
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options-hf
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'GBaker/MedQA-USMLE-4-options-hf' (8,554 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. katielink/nejm-medqa-diagnostic-reasoning-dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/katielink/nejm-medqa-diagnostic-reasoning-dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'katielink/nejm-medqa-diagnostic-reasoning-dataset' (224 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. Williamsanderson/MedQA-Darija-MultiLingual
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Williamsanderson/MedQA-Darija-MultiLingual
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Williamsanderson/MedQA-Darija-MultiLingual' (53,285 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. bigbio/med_qa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/bigbio/med_qa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'bigbio/med_qa' (3,857 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. medalpaca/medical_meadow_medqa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/medalpaca/medical_meadow_medqa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'medalpaca/medical_meadow_medqa' (3,205 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. truehealth/medqa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/truehealth/medqa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'truehealth/medqa' (348 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. augtoma/medqa_usmle
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/augtoma/medqa_usmle
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'augtoma/medqa_usmle' (178 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. VodLM/medqa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/VodLM/medqa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'VodLM/medqa' (214 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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
| 34 | paper | [Interpretable Biomedical QA: Customizing Models for PubMedQA with Knowledge Dist](https://doi.org/10.1109/icec2nt65402.2025.11380163) | 2025 | 2025 International Conference on Electro | paper | 0.5 | moderate |
| 35 | paper | [Balancing Binary Biomedical QA: Parameter-Efficient Instruction Tuning on BioASQ](https://doi.org/10.1109/icecte69292.2026.11429214) | 2026 | 2026 5th International Conference on Ele | paper | 0.5 | moderate |
| 36 | paper | [Information Reasoning and Question Answering in Healthcare: A PubMedQA Benchmark](https://doi.org/10.1109/aiccsa66935.2025.11315481) | 2025 | 2025 IEEE/ACS 22nd International Confere | benchmark | 0.5 | moderate |
| 37 | github | [liyucheng09/Contamination_Detector](https://github.com/liyucheng09/Contamination_Detector) |  | GitHub | tool | 52 | moderate |
| 38 | huggingface | [GBaker/MedQA-USMLE-4-options-hf-MPNet-IR](https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options-hf-MPNet-IR) |  | HuggingFace | dataset | 85 | moderate |
| 39 | huggingface | [GBaker/MedQA-USMLE-4-options-hf-DBPedia-context](https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options-hf-DBPedia-context) |  | HuggingFace | dataset | 33 | moderate |
| 40 | huggingface | [Shubham09/medqa](https://huggingface.co/datasets/Shubham09/medqa) |  | HuggingFace | dataset | 24 | moderate |
| 41 | huggingface | [katielink/med_qa](https://huggingface.co/datasets/katielink/med_qa) |  | HuggingFace | dataset | 38 | moderate |
| 42 | huggingface | [DreamyP/MedQA](https://huggingface.co/datasets/DreamyP/MedQA) |  | HuggingFace | dataset | 83 | moderate |
| 43 | huggingface | [prognosis/guidelines_medqa_qa_v1](https://huggingface.co/datasets/prognosis/guidelines_medqa_qa_v1) |  | HuggingFace | dataset | 40 | moderate |
| 44 | huggingface | [maximegmd/medqa_alpaca_format](https://huggingface.co/datasets/maximegmd/medqa_alpaca_format) |  | HuggingFace | dataset | 40 | moderate |
| 45 | huggingface | [HuggingSara/medqa](https://huggingface.co/datasets/HuggingSara/medqa) |  | HuggingFace | dataset | 83 | moderate |

### 1. Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2402.15938
- **Year/Venue**: 2024 / Annual Meeting of the Association for Computational Linguistics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.62: paper titled 'Generalization or Memorization: Data Contamination and Trustworthy Evaluation for Large Language Mod' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination|syn:title:memorization.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2507.10532
- **Year/Venue**: 2025 / AAAI Conference on Artificial Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.62: paper titled 'Reasoning or Memorization? Unreliable Results of Reinforcement Learning Due to Data Contamination' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination|syn:title:memorization.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. Data Contamination or Genuine Generalization? Disentangling LLM Performance on Benchmarks
- **Source**: paper  **URL**: https://doi.org/10.70393/616a6e73.323836
- **Year/Venue**: 2025 / Academic Journal of Natural Science
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.60: paper titled 'Data Contamination or Genuine Generalization? Disentangling LLM Performance on Benchmarks' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination|syn:abstract:memorization|syn:abstract:n-gram overlap.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.1162/tacl.a.20
- **Year/Venue**: 2025 / Transactions of the Association for Computational Linguistics
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.55: paper titled 'Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models' contributes a 'tool' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination|syn:abstract:memorization.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. Detecting Data Contamination in LLMs via In-Context Learning
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.27055
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.55: paper titled 'Detecting Data Contamination in LLMs via In-Context Learning' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination|syn:abstract:memorization.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2310.18018
- **Year/Venue**: 2023 / Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2402.03927
- **Year/Venue**: 2024 / Conference of the European Chapter of the Association for Computational Linguistics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in Closed-Source LLMs' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. Benchmark Data Contamination of Large Language Models: A Survey
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2406.04244
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Benchmark Data Contamination of Large Language Models: A Survey' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. Investigating Data Contamination for Pre-training Language Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2401.06059
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Investigating Data Contamination for Pre-training Language Models' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. AntiLeak-Bench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated Real-World Knowledge
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2412.13670
- **Year/Venue**: 2024 / Annual Meeting of the Association for Computational Linguistics
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'AntiLeak-Bench: Preventing Data Contamination by Automatically Constructing Benchmarks with Updated ' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. Evading Data Contamination Detection for Language Models is (too) Easy
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2402.02823
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Evading Data Contamination Detection for Language Models is (too) Easy' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2411.03923
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 13. Recent Advances in Large Langauge Model Benchmarks against Data Contamination: From Static to Dynamic Evaluation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2502.17521
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Recent Advances in Large Langauge Model Benchmarks against Data Contamination: From Static to Dynami' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 14. Data Contamination Calibration for Black-box LLMs
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2405.11930
- **Year/Venue**: 2024 / Annual Meeting of the Association for Computational Linguistics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Data Contamination Calibration for Black-box LLMs' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 15. A Survey on Data Contamination for Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2502.14425
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'A Survey on Data Contamination for Large Language Models' contributes a 'survey' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 16. Dynamic Benchmarking of Reasoning Capabilities in Code Large Language Models Under Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2503.04149
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Dynamic Benchmarking of Reasoning Capabilities in Code Large Language Models Under Data Contaminatio' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 17. Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2025.emnlp-main.511
- **Year/Venue**: 2025 / Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluat' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 18. VeriContaminated: Assessing LLM-Driven Verilog Coding for Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.1109/ICLAD65226.2025.00017
- **Year/Venue**: 2025 / 2025 IEEE International Conference on LLM-Aided Design (ICLAD)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'VeriContaminated: Assessing LLM-Driven Verilog Coding for Data Contamination' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 19. Overestimation in LLM Evaluation: A Controlled Large-Scale Study on Data Contamination's Impact on Machine Translation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2501.18771
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.50: paper titled 'Overestimation in LLM Evaluation: A Controlled Large-Scale Study on Data Contamination's Impact on M' contributes a 'empirical' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 20. Search-Time Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2508.13180
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Search-Time Data Contamination' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 21. The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM Benchmark Data Contam
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2503.16402
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'The Emperor's New Clothes in Benchmarking? A Rigorous Examination of Mitigation Strategies for LLM B' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 22. Beyond Next Token Probabilities: Learnable, Fast Detection of Hallucinations and Data Contamination on LLM Output Distri
- **Source**: paper  **URL**: https://doi.org/10.1609/aaai.v40i36.40254
- **Year/Venue**: 2025 / AAAI Conference on Artificial Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Beyond Next Token Probabilities: Learnable, Fast Detection of Hallucinations and Data Contamination ' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 23. DCR: Quantifying Data Contamination in LLMs Evaluation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2507.11405
- **Year/Venue**: 2025 / Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'DCR: Quantifying Data Contamination in LLMs Evaluation' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 24. Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.09259
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 25. A Taxonomy for Data Contamination in Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2024.conda-1.3
- **Year/Venue**: 2024 / Proceedings of the 1st Workshop on Data Contamination (CONDA)
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'A Taxonomy for Data Contamination in Large Language Models' contributes a 'survey' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 26. Confounders in Instance Variation for the Analysis of Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2024.conda-1.2
- **Year/Venue**: 2024 / Proceedings of the 1st Workshop on Data Contamination (CONDA)
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.50: paper titled 'Confounders in Instance Variation for the Analysis of Data Contamination' contributes a 'empirical' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 27. Analysis of Semantic Benchmark Data Contamination Attack for LLM-Driven Fake News Detection
- **Source**: paper  **URL**: https://doi.org/10.1109/BigData66926.2025.11402039
- **Year/Venue**: 2025 / BigData Congress [Services Society]
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Analysis of Semantic Benchmark Data Contamination Attack for LLM-Driven Fake News Detection' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 28. Proceedings of the 1st Workshop on Data Contamination (CONDA)
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2024.conda-1
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Proceedings of the 1st Workshop on Data Contamination (CONDA)' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 29. Data Contamination in AI Evaluation (Preprint)
- **Source**: paper  **URL**: https://doi.org/10.2196/preprints.80987
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Data Contamination in AI Evaluation (Preprint)' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 30. Density Deconvolution with Limited Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.4916179
- **Year/Venue**: 2024 / SSRN Electronic Journal
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Density Deconvolution with Limited Data Contamination' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 31. Data Contamination in AI Evaluation
- **Source**: paper  **URL**: https://doi.org/10.2196/80987
- **Year/Venue**: 2025 / JMIR Medical Informatics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Data Contamination in AI Evaluation' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 32. Data Contamination in LLMs: A Scoping Literature Review
- **Source**: paper  **URL**: https://doi.org/10.37766/inplasy2025.11.0050
- **Year/Venue**: 2025 / n/a
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'Data Contamination in LLMs: A Scoping Literature Review' contributes a 'survey' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 33. Fully Unsupervised Anomaly Detection in Industrial Images with Unknown Data Contamination
- **Source**: paper  **URL**: https://doi.org/10.1109/sds66131.2025.00013
- **Year/Venue**: 2025 / 2025 IEEE Swiss Conference on Data Science (SDS)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Fully Unsupervised Anomaly Detection in Industrial Images with Unknown Data Contamination' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: primary:title:data contamination.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 34. Interpretable Biomedical QA: Customizing Models for PubMedQA with Knowledge Distillation and XAI
- **Source**: paper  **URL**: https://doi.org/10.1109/icec2nt65402.2025.11380163
- **Year/Venue**: 2025 / 2025 International Conference on Electronics and Computing, Communication Networking Automation Technologies (ICEC2NT)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Interpretable Biomedical QA: Customizing Models for PubMedQA with Knowledge Distillation and XAI' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa|kw:title:pubmedqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 35. Balancing Binary Biomedical QA: Parameter-Efficient Instruction Tuning on BioASQ and PubMedQA
- **Source**: paper  **URL**: https://doi.org/10.1109/icecte69292.2026.11429214
- **Year/Venue**: 2026 / 2026 5th International Conference on Electrical, Computer &amp;amp; Telecommunication Engineering (ICECTE)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Balancing Binary Biomedical QA: Parameter-Efficient Instruction Tuning on BioASQ and PubMedQA' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa|kw:title:pubmedqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 36. Information Reasoning and Question Answering in Healthcare: A PubMedQA Benchmark Study
- **Source**: paper  **URL**: https://doi.org/10.1109/aiccsa66935.2025.11315481
- **Year/Venue**: 2025 / 2025 IEEE/ACS 22nd International Conference on Computer Systems and Applications (AICCSA)
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Information Reasoning and Question Answering in Healthcare: A PubMedQA Benchmark Study' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa|kw:title:pubmedqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 37. liyucheng09/Contamination_Detector
- **Source**: github  **URL**: https://github.com/liyucheng09/Contamination_Detector
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'liyucheng09/Contamination_Detector' (52 stars) provides an implementation of 'data contamination'. Description: lightweight tool to identify data contamination in llms evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 38. GBaker/MedQA-USMLE-4-options-hf-MPNet-IR
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options-hf-MPNet-IR
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'GBaker/MedQA-USMLE-4-options-hf-MPNet-IR' (85 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 39. GBaker/MedQA-USMLE-4-options-hf-DBPedia-context
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options-hf-DBPedia-context
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'GBaker/MedQA-USMLE-4-options-hf-DBPedia-context' (33 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 40. Shubham09/medqa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Shubham09/medqa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Shubham09/medqa' (24 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 41. katielink/med_qa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/katielink/med_qa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'katielink/med_qa' (38 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 42. DreamyP/MedQA
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/DreamyP/MedQA
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'DreamyP/MedQA' (83 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 43. prognosis/guidelines_medqa_qa_v1
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/prognosis/guidelines_medqa_qa_v1
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'prognosis/guidelines_medqa_qa_v1' (40 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 44. maximegmd/medqa_alpaca_format
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/maximegmd/medqa_alpaca_format
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'maximegmd/medqa_alpaca_format' (40 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 45. HuggingSara/medqa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/HuggingSara/medqa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'HuggingSara/medqa' (83 downloads) matched 'MedQA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Toward expert-level medical question answering with large language models](https://doi.org/10.1038/s41591-024-03423-7) | 2025 | Nature Medicine | paper | 0.3 | strong |
| 2 | paper | [Towards Expert-Level Medical Question Answering with Large Language Models](https://doi.org/10.48550/arXiv.2305.09617) | 2023 | arXiv.org | paper | 0.3 | strong |
| 3 | paper | [LLM-MedQA: Enhancing Medical Question Answering through Case Studies in Large La](https://doi.org/10.1109/IJCNN64981.2025.11228647) | 2024 | IEEE International Joint Conference on N | paper | 0.25 | strong |
| 4 | paper | [MedQA-CS: Objective Structured Clinical Examination (OSCE)-Style Benchmark for E](https://doi.org/10.18653/v1/2026.eacl-long.292) | 2024 |  | benchmark | 0.25 | strong |
| 5 | paper | [MedQA-SWE - a Clinical Question & Answer Dataset for Swedish](https://doi.org/10.63317/4ckcc2pepdd3) | 2024 | International Conference on Language Res | dataset | 0.25 | strong |
| 6 | paper | [MedQA-CS: Benchmarking Large Language Models Clinical Skills Using an AI-SCE Fra](https://doi.org/10.48550/arXiv.2410.01553) | 2024 | arXiv.org | benchmark | 0.25 | strong |
| 7 | paper | [Beyond MedQA: Towards Real-world Clinical Decision Making in the Era of LLMs](https://doi.org/10.48550/arXiv.2510.20001) | 2025 | arXiv.org | paper | 0.25 | strong |
| 8 | paper | [Small Models Exhibit Limited Answer Consistency in Repetition Trials of the Mult](https://doi.org/10.1609/aaai.v40i39.40550) | 2026 | AAAI Conference on Artificial Intelligen | benchmark | 0.25 | strong |
| 9 | paper | [Auditing Demographic Bias in Mistral: An Open-Source LLM’s Diagnostic Performanc](https://doi.org/10.1109/ACCESS.2026.3656396) | 2026 | IEEE Access | benchmark | 0.25 | strong |
| 10 | paper | [MedQA-FoRA-MultiHospital: A Non-IID Multihospital Benchmark and Adaptive Federat](https://doi.org/10.71448/bcds2671-5) | 2026 | Bulletin of Computer and Data Sciences | benchmark | 0.25 | strong |
| 11 | paper | [MedQA-MA: A Moroccan Arabic medical question-answering dataset for virtual healt](https://doi.org/10.1016/j.dib.2026.112537) | 2026 | Data in Brief | dataset | 0.25 | strong |
| 12 | paper | [Benchmark Leakage, Plasticity Loss, and Regime Transitions in Large Language Mod](https://doi.org/10.2139/ssrn.6084208) | 2026 |  | benchmark | 0.25 | strong |
| 13 | paper | [A Compact 3B Language Model Achieving Competitive MedQA Performance with Minimal](https://doi.org/10.36227/techrxiv.176531815.53078915/v1) | 2025 |  | paper | 0.25 | strong |
| 14 | paper | [Integrating Knowledge Graph with Retrieval-Augmented Generation in Medical Quest](https://doi.org/10.2196/preprints.92241) | 2026 |  | empirical | 0.25 | strong |

### 1. Toward expert-level medical question answering with large language models
- **Source**: paper  **URL**: https://doi.org/10.1038/s41591-024-03423-7
- **Year/Venue**: 2025 / Nature Medicine
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.30: paper titled 'Toward expert-level medical question answering with large language models' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: kw:abstract:medqa|kw:abstract:pubmedqa|kw:abstract:mmlu clinical.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. Towards Expert-Level Medical Question Answering with Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2305.09617
- **Year/Venue**: 2023 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.30: paper titled 'Towards Expert-Level Medical Question Answering with Large Language Models' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: kw:abstract:medqa|kw:abstract:pubmedqa|kw:abstract:mmlu clinical.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. LLM-MedQA: Enhancing Medical Question Answering through Case Studies in Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.1109/IJCNN64981.2025.11228647
- **Year/Venue**: 2024 / IEEE International Joint Conference on Neural Network
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'LLM-MedQA: Enhancing Medical Question Answering through Case Studies in Large Language Models' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. MedQA-CS: Objective Structured Clinical Examination (OSCE)-Style Benchmark for Evaluating LLM Clinical Skills
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2026.eacl-long.292
- **Year/Venue**: 2024 / n/a
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'MedQA-CS: Objective Structured Clinical Examination (OSCE)-Style Benchmark for Evaluating LLM Clinic' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. MedQA-SWE - a Clinical Question & Answer Dataset for Swedish
- **Source**: paper  **URL**: https://doi.org/10.63317/4ckcc2pepdd3
- **Year/Venue**: 2024 / International Conference on Language Resources and Evaluation
- **Contribution type**: dataset
- **Why it overlaps**: Relevance 0.25: paper titled 'MedQA-SWE - a Clinical Question & Answer Dataset for Swedish' contributes a 'dataset' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. MedQA-CS: Benchmarking Large Language Models Clinical Skills Using an AI-SCE Framework
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2410.01553
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'MedQA-CS: Benchmarking Large Language Models Clinical Skills Using an AI-SCE Framework' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. Beyond MedQA: Towards Real-world Clinical Decision Making in the Era of LLMs
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.20001
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Beyond MedQA: Towards Real-world Clinical Decision Making in the Era of LLMs' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Small Models Exhibit Limited Answer Consistency in Repetition Trials of the Multiple-Choice MMLU-Redux and MedQA Benchma
- **Source**: paper  **URL**: https://doi.org/10.1609/aaai.v40i39.40550
- **Year/Venue**: 2026 / AAAI Conference on Artificial Intelligence
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'Small Models Exhibit Limited Answer Consistency in Repetition Trials of the Multiple-Choice MMLU-Red' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. Auditing Demographic Bias in Mistral: An Open-Source LLM’s Diagnostic Performance on the MedQA Benchmark
- **Source**: paper  **URL**: https://doi.org/10.1109/ACCESS.2026.3656396
- **Year/Venue**: 2026 / IEEE Access
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'Auditing Demographic Bias in Mistral: An Open-Source LLM’s Diagnostic Performance on the MedQA Bench' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. MedQA-FoRA-MultiHospital: A Non-IID Multihospital Benchmark and Adaptive Federated Low-Rank Framework for Privacy-Preser
- **Source**: paper  **URL**: https://doi.org/10.71448/bcds2671-5
- **Year/Venue**: 2026 / Bulletin of Computer and Data Sciences
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'MedQA-FoRA-MultiHospital: A Non-IID Multihospital Benchmark and Adaptive Federated Low-Rank Framewor' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. MedQA-MA: A Moroccan Arabic medical question-answering dataset for virtual healthcare assistants and large language mode
- **Source**: paper  **URL**: https://doi.org/10.1016/j.dib.2026.112537
- **Year/Venue**: 2026 / Data in Brief
- **Contribution type**: dataset
- **Why it overlaps**: Relevance 0.25: paper titled 'MedQA-MA: A Moroccan Arabic medical question-answering dataset for virtual healthcare assistants and' contributes a 'dataset' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. Benchmark Leakage, Plasticity Loss, and Regime Transitions in Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6084208
- **Year/Venue**: 2026 / n/a
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'Benchmark Leakage, Plasticity Loss, and Regime Transitions in Large Language Models' contributes a 'benchmark' matching target artifact 'empirical+database'. Matched keywords: kw:title:benchmark leakage.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. A Compact 3B Language Model Achieving Competitive MedQA Performance with Minimal Supervision
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.176531815.53078915/v1
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'A Compact 3B Language Model Achieving Competitive MedQA Performance with Minimal Supervision' contributes a 'paper' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 14. Integrating Knowledge Graph with Retrieval-Augmented Generation in Medical Question Answering: Development and Usability
- **Source**: paper  **URL**: https://doi.org/10.2196/preprints.92241
- **Year/Venue**: 2026 / n/a
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'Integrating Knowledge Graph with Retrieval-Augmented Generation in Medical Question Answering: Devel' contributes a 'empirical' matching target artifact 'empirical+database'. Matched keywords: kw:title:medqa.
- **How we differ**: Our proposed work focuses specifically on 'Test-set contamination audit of healthcare LLM benchmarks'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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

1. Complete the Artifact Differentiator Checklist above (11 artifacts found).
2. This topic can proceed to GO if artifact differentiator is articulated explicitly.
3. Write one paragraph for §6 verification log explaining differentiation from top artifacts.
