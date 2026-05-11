# Existing Work Report — B05: Synthetic data quality evaluation metrics

> ⚠️ **DIFFERENTIATOR REQUIRED** — paper_direct=0, artifact_direct=5; paper_strength=`strong`, artifact_strength=`moderate`.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 3 |
| HuggingFace direct artifacts | 2 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 5 |
| Artifact diff strength | `moderate` |
| Partial overlaps (total) | 70 |
| Adjacent | 33 |
| Total findings | 108 |
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
| 1 | github | [Project-AgML/AgML](https://github.com/Project-AgML/AgML) |  | GitHub | benchmark | 279 | moderate |
| 2 | github | [stephenleo/llm-structured-output-benchmarks](https://github.com/stephenleo/llm-structured-output-benchmarks) |  | GitHub | benchmark | 186 | moderate |
| 3 | github | [opendatalab/LOKI](https://github.com/opendatalab/LOKI) |  | GitHub | benchmark | 180 | moderate |
| 4 | huggingface | [ProGamerGov/synthetic-dataset-1m-dalle3-high-quality-captions](https://huggingface.co/datasets/ProGamerGov/synthetic-dataset-1m-dalle3-high-quality-captions) |  | HuggingFace | dataset | 3316 | moderate |
| 5 | huggingface | [Irfanuruchi/building-engineering-synthetic-dataset-v5](https://huggingface.co/datasets/Irfanuruchi/building-engineering-synthetic-dataset-v5) |  | HuggingFace | dataset | 141 | moderate |

### 1. Project-AgML/AgML
- **Source**: github  **URL**: https://github.com/Project-AgML/AgML
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'Project-AgML/AgML' (279 stars) provides an implementation of 'synthetic data'. Description: agml is a centralized framework for agricultural machine learning. agml provides access to public agricultural datasets .
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. stephenleo/llm-structured-output-benchmarks
- **Source**: github  **URL**: https://github.com/stephenleo/llm-structured-output-benchmarks
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'stephenleo/llm-structured-output-benchmarks' (186 stars) provides an implementation of 'synthetic data'. Description: benchmark various llm structured output frameworks: instructor, mirascope, langchain, llamaindex, fructose, marvin, outl.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. opendatalab/LOKI
- **Source**: github  **URL**: https://github.com/opendatalab/LOKI
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'opendatalab/LOKI' (180 stars) provides an implementation of 'synthetic data'. Description: [iclr 2025 spotlight] the official implementation of the paper “loki：a comprehensive synthetic data detection benchmark .
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. ProGamerGov/synthetic-dataset-1m-dalle3-high-quality-captions
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/ProGamerGov/synthetic-dataset-1m-dalle3-high-quality-captions
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'ProGamerGov/synthetic-dataset-1m-dalle3-high-quality-captions' (3,316 downloads) matched 'synthetic data' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. Irfanuruchi/building-engineering-synthetic-dataset-v5
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Irfanuruchi/building-engineering-synthetic-dataset-v5
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Irfanuruchi/building-engineering-synthetic-dataset-v5' (141 downloads) matched 'synthetic data' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [mmE5: Improving Multimodal Multilingual Embeddings via High-quality Synthetic Da](https://doi.org/10.48550/arXiv.2502.08468) | 2025 | Annual Meeting of the Association for Co | paper | 0.65 | moderate |
| 2 | paper | [A synthetic data strategy for Scotland: Using synthetic data to improve access t](https://doi.org/10.23889/ijpds.v8i2.2215) | 2023 | International Journal of Population Data | paper | 0.6 | moderate |
| 3 | paper | [Mending Synthetic Healthcare Data with MAPS: Model Agnostic Post-hoc Synthetic D](https://doi.org/10.21203/rs.3.rs-9379765/v1) | 2026 |  | tool | 0.6 | moderate |
| 4 | paper | [Scaling Synthetic Data Creation with 1,000,000,000 Personas](https://doi.org/10.48550/arXiv.2406.20094) | 2024 | arXiv.org | paper | 0.55 | moderate |
| 5 | paper | [Synthetic Data Generation Using Large Language Models: Advances in Text and Code](https://doi.org/10.1109/ACCESS.2025.3589503) | 2025 | IEEE Access | paper | 0.55 | moderate |
| 6 | paper | LLaVA-Video: Video Instruction Tuning With Synthetic Data | 2024 | Trans. Mach. Learn. Res. | paper | 0.5 | moderate |
| 7 | paper | [Video Instruction Tuning With Synthetic Data](https://doi.org/10.48550/arXiv.2410.02713) | 2024 | arXiv.org | paper | 0.5 | moderate |
| 8 | paper | [On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey](https://doi.org/10.48550/arXiv.2406.15126) | 2024 | Annual Meeting of the Association for Co | survey | 0.5 | moderate |
| 9 | paper | [DreamSim: Learning New Dimensions of Human Visual Similarity using Synthetic Dat](https://doi.org/10.48550/arXiv.2306.09344) | 2023 | Neural Information Processing Systems | paper | 0.5 | moderate |
| 10 | paper | [DeepSeek-Prover: Advancing Theorem Proving in LLMs through Large-Scale Synthetic](https://doi.org/10.48550/arXiv.2405.14333) | 2024 | arXiv.org | paper | 0.5 | moderate |
| 11 | paper | [A Systematic Review of Synthetic Data Generation Techniques Using Generative AI](https://doi.org/10.3390/electronics13173509) | 2024 | Electronics | survey | 0.5 | moderate |
| 12 | paper | [Synthetic data](https://doi.org/10.1177/02663821241231101) | 2024 | Business Information Review | paper | 0.5 | moderate |
| 13 | paper | [Synthetic data generation methods in healthcare: A review on open-source tools a](https://doi.org/10.1016/j.csbj.2024.07.005) | 2024 | Computational and Structural Biotechnolo | survey | 0.5 | moderate |
| 14 | paper | [A scoping review of privacy and utility metrics in medical synthetic data](https://doi.org/10.1038/s41746-024-01359-3) | 2025 | npj Digital Medicine | survey | 0.5 | moderate |
| 15 | paper | [Enhancing pine wilt disease detection with synthetic data and external attention](https://doi.org/10.1016/j.engappai.2025.111655) | 2025 | Engineering applications of artificial i | paper | 0.5 | moderate |
| 16 | paper | [Scaling Laws of Synthetic Data for Language Models](https://doi.org/10.48550/arXiv.2503.19551) | 2025 | arXiv.org | paper | 0.5 | moderate |
| 17 | paper | [Synthetic data generation: a privacy-preserving approach to accelerate rare dise](https://doi.org/10.3389/fdgth.2025.1563991) | 2025 | Frontiers Digit. Health | paper | 0.5 | moderate |
| 18 | paper | [Synthetic Data Generation & Multi-Step RL for Reasoning & Tool Use](https://doi.org/10.48550/arXiv.2504.04736) | 2025 | arXiv.org | tool | 0.5 | moderate |
| 19 | paper | [TimePFN: Effective Multivariate Time Series Forecasting with Synthetic Data](https://doi.org/10.48550/arXiv.2502.16294) | 2025 | AAAI Conference on Artificial Intelligen | paper | 0.5 | moderate |
| 20 | paper | [Can Synthetic Data be Fair and Private? A Comparative Study of Synthetic Data Ge](https://doi.org/10.1145/3706468.3706546) | 2025 | International Conference on Learning Ana | empirical | 0.5 | moderate |
| 21 | paper | [Synthetic Data is an Elegant GIFT for Continual Vision-Language Models](https://doi.org/10.1109/CVPR52734.2025.00268) | 2025 | Computer Vision and Pattern Recognition | paper | 0.5 | moderate |
| 22 | paper | [Is synthetic data generation effective in maintaining clinical biomarkers? Inves](https://doi.org/10.3389/frai.2024.1454441) | 2025 | Frontiers Artif. Intell. | paper | 0.5 | moderate |
| 23 | paper | [Synthetic Data Generation for Healthcare: Exploring Generative Adversarial Netwo](https://doi.org/10.1007/s41060-025-00816-w) | 2025 | International Journal of Data Science an | paper | 0.5 | moderate |
| 24 | paper | [Creating Artificial Students that Never Existed: Leveraging Large Language Model](https://doi.org/10.1145/3706468.3706523) | 2025 | International Conference on Learning Ana | paper | 0.5 | moderate |
| 25 | paper | [A consensus privacy metrics framework for synthetic data](https://doi.org/10.1016/j.patter.2025.101320) | 2025 | Patterns | tool | 0.5 | moderate |
| 26 | paper | [Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling L](https://doi.org/10.48550/arXiv.2510.01631) | 2025 | Conference on Empirical Methods in Natur | tool | 0.5 | moderate |
| 27 | paper | [Optimized Synthetic Data Integration With Transformer’s DGA Data for Improved ML](https://doi.org/10.1109/TDEI.2024.3421915) | 2025 | IEEE transactions on dielectrics and ele | paper | 0.5 | moderate |
| 28 | paper | [An Introduction to Synthetic Data](https://doi.org/10.1007/978-1-4842-8587-9_1) | 2022 | Synthetic Data for Deep Learning | paper | 0.5 | moderate |
| 29 | paper | [Synthetic Data and Generative AI](https://doi.org/10.1016/c2023-0-00094-2) | 2024 |  | paper | 0.5 | moderate |
| 30 | paper | [Synthetic Data for Deep Learning](https://doi.org/10.1007/978-1-4842-8587-9) | 2022 |  | paper | 0.5 | moderate |
| 31 | paper | [Foundations of Synthetic data](https://doi.org/10.1007/978-1-4842-8587-9_2) | 2022 | Synthetic Data for Deep Learning | paper | 0.5 | moderate |
| 32 | paper | [Synthetic data, measured data integrated learning experiments](https://doi.org/10.1117/12.2665521) | 2023 | Algorithms for Synthetic Aperture Radar  | paper | 0.5 | moderate |
| 33 | paper | [Synthetic Data in Investment Management](https://doi.org/10.56227/25.1.24) | 2025 |  | paper | 0.5 | moderate |
| 34 | paper | [Synthetic Data: Servicing Privacy](https://doi.org/10.1332/policypress/9781529239683.003.0010) | 2025 | Beyond Privacy | paper | 0.5 | moderate |
| 35 | paper | [Synthetic data, interpretable regression, and submodels](https://doi.org/10.1016/b978-0-44-321857-6.00011-4) | 2024 | Synthetic Data and Generative AI | paper | 0.5 | moderate |
| 36 | paper | [Synthetic Data Generation with Python](https://doi.org/10.1007/978-1-4842-8587-9_5) | 2022 | Synthetic Data for Deep Learning | paper | 0.5 | moderate |
| 37 | paper | [Synthetic Data Generation with R](https://doi.org/10.1007/978-1-4842-8587-9_4) | 2022 | Synthetic Data for Deep Learning | paper | 0.5 | moderate |
| 38 | paper | [Artificial Intelligence Agents Powered by Synthetic Data](https://doi.org/10.4018/979-8-3373-2277-3.ch004) | 2025 | Digital Synthetic Data and Outputs | paper | 0.5 | moderate |
| 39 | paper | [Productivity Enhancements from Digital Synthetic Data](https://doi.org/10.4018/979-8-3373-2277-3.ch007) | 2025 | Digital Synthetic Data and Outputs | paper | 0.5 | moderate |
| 40 | paper | [Synthetic Data1](https://doi.org/10.1201/9781003185284-13) | 2024 | Handbook of Sharing Confidential Data | paper | 0.5 | moderate |
| 41 | paper | [Methods for Synthetic Data Generation](https://doi.org/10.1201/9781003185284-14) | 2024 | Handbook of Sharing Confidential Data | paper | 0.5 | moderate |
| 42 | paper | [The Synthetic Mirror - Synthetic Data at the Age of Agentic AI](https://doi.org/10.36227/techrxiv.175022167.74487124/v1) | 2025 |  | paper | 0.5 | moderate |
| 43 | paper | [synthesizer: Fast, Robust, and High-Quality Synthetic Data Generation with a Tun](https://doi.org/10.32614/cran.package.synthesizer) | 2024 | CRAN: Contributed Packages | paper | 0.5 | moderate |
| 44 | paper | [Tools to Create Synthetic Data for Brain Images](https://doi.org/10.4018/979-8-3693-1886-7.ch011) | 2024 | Advances in Data Mining and Database Man | tool | 0.5 | moderate |
| 45 | paper | [StructSynth: Leveraging LLMs for Structure-Aware Tabular Data Synthesis in Low-D](https://doi.org/10.48550/arXiv.2508.02601) | 2025 | arXiv.org | paper | 0.412 | moderate |
| 46 | paper | [Tabular generative modeling framework for multi-property data synthesis of pyrol](https://doi.org/10.1016/j.biortech.2025.133207) | 2025 | Bioresource Technology | tool | 0.412 | moderate |
| 47 | paper | [Synth-MIA: A Testbed for Auditing Privacy Leakage in Tabular Data Synthesis](https://doi.org/10.48550/arXiv.2509.18014) | 2025 | arXiv.org | empirical | 0.362 | moderate |
| 48 | github | [argilla-io/distilabel](https://github.com/argilla-io/distilabel) |  | GitHub | tool | 3211 | moderate |
| 49 | github | [hitsz-ids/synthetic-data-generator](https://github.com/hitsz-ids/synthetic-data-generator) |  | GitHub | tool | 2417 | moderate |
| 50 | github | [CHATS-lab/verbalized-sampling](https://github.com/CHATS-lab/verbalized-sampling) |  | GitHub | tool | 758 | moderate |
| 51 | github | [USTCPCS/CVPR2018_attention](https://github.com/USTCPCS/CVPR2018_attention) |  | GitHub | tool | 179 | moderate |
| 52 | github | [statice/anonymeter](https://github.com/statice/anonymeter) |  | GitHub | tool | 101 | moderate |
| 53 | github | [junchengli1/Sim-Suction-API](https://github.com/junchengli1/Sim-Suction-API) |  | GitHub | tool | 47 | moderate |
| 54 | github | [NVIDIA/synthda](https://github.com/NVIDIA/synthda) |  | GitHub | tool | 46 | moderate |
| 55 | github | [junchengli1/Sim-Grasp](https://github.com/junchengli1/Sim-Grasp) |  | GitHub | tool | 45 | moderate |
| 56 | github | [haoran1062/so101-autogen](https://github.com/haoran1062/so101-autogen) |  | GitHub | tool | 32 | moderate |
| 57 | github | [menyifang/En3D](https://github.com/menyifang/En3D) |  | GitHub | tool | 541 | moderate |
| 58 | github | [StoryMY/take-off-eyeglasses](https://github.com/StoryMY/take-off-eyeglasses) |  | GitHub | tool | 154 | moderate |
| 59 | github | [declare-lab/RelationPrompt](https://github.com/declare-lab/RelationPrompt) |  | GitHub | tool | 134 | moderate |
| 60 | github | [SunzeY/Bootstrap3D](https://github.com/SunzeY/Bootstrap3D) |  | GitHub | tool | 94 | moderate |
| 61 | github | [ahstat/episodic-memory-benchmark](https://github.com/ahstat/episodic-memory-benchmark) |  | GitHub | tool | 67 | moderate |
| 62 | github | [mirkovicdev/CLUSTERING-MARKET-REGIMES](https://github.com/mirkovicdev/CLUSTERING-MARKET-REGIMES) |  | GitHub | tool | 58 | moderate |
| 63 | github | [Kiteretsu77/VCISR-official](https://github.com/Kiteretsu77/VCISR-official) |  | GitHub | tool | 52 | moderate |
| 64 | github | [hnavidan/LocalizationGAN](https://github.com/hnavidan/LocalizationGAN) |  | GitHub | tool | 49 | moderate |
| 65 | github | [Lornatang/Real_ESRGAN-PyTorch](https://github.com/Lornatang/Real_ESRGAN-PyTorch) |  | GitHub | tool | 42 | moderate |
| 66 | github | [Flame-Chasers/SynTBPR](https://github.com/Flame-Chasers/SynTBPR) |  | GitHub | tool | 39 | moderate |
| 67 | huggingface | [cRick/NL-to-LTL-Synthetic-Dataset](https://huggingface.co/datasets/cRick/NL-to-LTL-Synthetic-Dataset) |  | HuggingFace | dataset | 54 | moderate |
| 68 | huggingface | [Anonymous0624/llm-psychometric-fidelity-audit](https://huggingface.co/datasets/Anonymous0624/llm-psychometric-fidelity-audit) |  | HuggingFace | dataset | 21 | moderate |
| 69 | huggingface | [AxonData/ibeta-high-fidelity-rubber-mask-dataset](https://huggingface.co/datasets/AxonData/ibeta-high-fidelity-rubber-mask-dataset) |  | HuggingFace | dataset | 27 | moderate |
| 70 | huggingface | [realitydriftproject/semantic-fidelity-examples](https://huggingface.co/datasets/realitydriftproject/semantic-fidelity-examples) |  | HuggingFace | dataset | 23 | moderate |

### 1. mmE5: Improving Multimodal Multilingual Embeddings via High-quality Synthetic Data
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2502.08468
- **Year/Venue**: 2025 / Annual Meeting of the Association for Computational Linguistics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.65: paper titled 'mmE5: Improving Multimodal Multilingual Embeddings via High-quality Synthetic Data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data|kw:abstract:fidelity|syn:abstract:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. A synthetic data strategy for Scotland: Using synthetic data to improve access to public sector data for research
- **Source**: paper  **URL**: https://doi.org/10.23889/ijpds.v8i2.2215
- **Year/Venue**: 2023 / International Journal of Population Data Science
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.60: paper titled 'A synthetic data strategy for Scotland: Using synthetic data to improve access to public sector data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data|kw:abstract:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. Mending Synthetic Healthcare Data with MAPS: Model Agnostic Post-hoc Synthetic Data Refinement Framework
- **Source**: paper  **URL**: https://doi.org/10.21203/rs.3.rs-9379765/v1
- **Year/Venue**: 2026 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.60: paper titled 'Mending Synthetic Healthcare Data with MAPS: Model Agnostic Post-hoc Synthetic Data Refinement Frame' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data|kw:abstract:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. Scaling Synthetic Data Creation with 1,000,000,000 Personas
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2406.20094
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.55: paper titled 'Scaling Synthetic Data Creation with 1,000,000,000 Personas' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data|syn:abstract:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. Synthetic Data Generation Using Large Language Models: Advances in Text and Code
- **Source**: paper  **URL**: https://doi.org/10.1109/ACCESS.2025.3589503
- **Year/Venue**: 2025 / IEEE Access
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.55: paper titled 'Synthetic Data Generation Using Large Language Models: Advances in Text and Code' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data|syn:abstract:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. LLaVA-Video: Video Instruction Tuning With Synthetic Data
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2024 / Trans. Mach. Learn. Res.
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'LLaVA-Video: Video Instruction Tuning With Synthetic Data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. Video Instruction Tuning With Synthetic Data
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2410.02713
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Video Instruction Tuning With Synthetic Data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2406.15126
- **Year/Venue**: 2024 / Annual Meeting of the Association for Computational Linguistics
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey' contributes a 'survey' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. DreamSim: Learning New Dimensions of Human Visual Similarity using Synthetic Data
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2306.09344
- **Year/Venue**: 2023 / Neural Information Processing Systems
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'DreamSim: Learning New Dimensions of Human Visual Similarity using Synthetic Data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. DeepSeek-Prover: Advancing Theorem Proving in LLMs through Large-Scale Synthetic Data
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2405.14333
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'DeepSeek-Prover: Advancing Theorem Proving in LLMs through Large-Scale Synthetic Data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. A Systematic Review of Synthetic Data Generation Techniques Using Generative AI
- **Source**: paper  **URL**: https://doi.org/10.3390/electronics13173509
- **Year/Venue**: 2024 / Electronics
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'A Systematic Review of Synthetic Data Generation Techniques Using Generative AI' contributes a 'survey' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. Synthetic data
- **Source**: paper  **URL**: https://doi.org/10.1177/02663821241231101
- **Year/Venue**: 2024 / Business Information Review
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 13. Synthetic data generation methods in healthcare: A review on open-source tools and methods
- **Source**: paper  **URL**: https://doi.org/10.1016/j.csbj.2024.07.005
- **Year/Venue**: 2024 / Computational and Structural Biotechnology Journal
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic data generation methods in healthcare: A review on open-source tools and methods' contributes a 'survey' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 14. A scoping review of privacy and utility metrics in medical synthetic data
- **Source**: paper  **URL**: https://doi.org/10.1038/s41746-024-01359-3
- **Year/Venue**: 2025 / npj Digital Medicine
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'A scoping review of privacy and utility metrics in medical synthetic data' contributes a 'survey' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 15. Enhancing pine wilt disease detection with synthetic data and external attention-based transformers
- **Source**: paper  **URL**: https://doi.org/10.1016/j.engappai.2025.111655
- **Year/Venue**: 2025 / Engineering applications of artificial intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Enhancing pine wilt disease detection with synthetic data and external attention-based transformers' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 16. Scaling Laws of Synthetic Data for Language Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2503.19551
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Scaling Laws of Synthetic Data for Language Models' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 17. Synthetic data generation: a privacy-preserving approach to accelerate rare disease research
- **Source**: paper  **URL**: https://doi.org/10.3389/fdgth.2025.1563991
- **Year/Venue**: 2025 / Frontiers Digit. Health
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic data generation: a privacy-preserving approach to accelerate rare disease research' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 18. Synthetic Data Generation & Multi-Step RL for Reasoning & Tool Use
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.04736
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic Data Generation & Multi-Step RL for Reasoning & Tool Use' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 19. TimePFN: Effective Multivariate Time Series Forecasting with Synthetic Data
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2502.16294
- **Year/Venue**: 2025 / AAAI Conference on Artificial Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'TimePFN: Effective Multivariate Time Series Forecasting with Synthetic Data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 20. Can Synthetic Data be Fair and Private? A Comparative Study of Synthetic Data Generation and Fairness Algorithms
- **Source**: paper  **URL**: https://doi.org/10.1145/3706468.3706546
- **Year/Venue**: 2025 / International Conference on Learning Analytics and Knowledge
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.50: paper titled 'Can Synthetic Data be Fair and Private? A Comparative Study of Synthetic Data Generation and Fairnes' contributes a 'empirical' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 21. Synthetic Data is an Elegant GIFT for Continual Vision-Language Models
- **Source**: paper  **URL**: https://doi.org/10.1109/CVPR52734.2025.00268
- **Year/Venue**: 2025 / Computer Vision and Pattern Recognition
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic Data is an Elegant GIFT for Continual Vision-Language Models' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 22. Is synthetic data generation effective in maintaining clinical biomarkers? Investigating diffusion models across diverse
- **Source**: paper  **URL**: https://doi.org/10.3389/frai.2024.1454441
- **Year/Venue**: 2025 / Frontiers Artif. Intell.
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Is synthetic data generation effective in maintaining clinical biomarkers? Investigating diffusion m' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 23. Synthetic Data Generation for Healthcare: Exploring Generative Adversarial Networks Variants for Medical Tabular Data
- **Source**: paper  **URL**: https://doi.org/10.1007/s41060-025-00816-w
- **Year/Venue**: 2025 / International Journal of Data Science and Analysis
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic Data Generation for Healthcare: Exploring Generative Adversarial Networks Variants for Med' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 24. Creating Artificial Students that Never Existed: Leveraging Large Language Models and CTGANs for Synthetic Data Generati
- **Source**: paper  **URL**: https://doi.org/10.1145/3706468.3706523
- **Year/Venue**: 2025 / International Conference on Learning Analytics and Knowledge
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Creating Artificial Students that Never Existed: Leveraging Large Language Models and CTGANs for Syn' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 25. A consensus privacy metrics framework for synthetic data
- **Source**: paper  **URL**: https://doi.org/10.1016/j.patter.2025.101320
- **Year/Venue**: 2025 / Patterns
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'A consensus privacy metrics framework for synthetic data' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 26. Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.01631
- **Year/Venue**: 2025 / Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and P' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 27. Optimized Synthetic Data Integration With Transformer’s DGA Data for Improved ML-Based Fault Identification
- **Source**: paper  **URL**: https://doi.org/10.1109/TDEI.2024.3421915
- **Year/Venue**: 2025 / IEEE transactions on dielectrics and electrical insulation
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Optimized Synthetic Data Integration With Transformer’s DGA Data for Improved ML-Based Fault Identif' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 28. An Introduction to Synthetic Data
- **Source**: paper  **URL**: https://doi.org/10.1007/978-1-4842-8587-9_1
- **Year/Venue**: 2022 / Synthetic Data for Deep Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'An Introduction to Synthetic Data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 29. Synthetic Data and Generative AI
- **Source**: paper  **URL**: https://doi.org/10.1016/c2023-0-00094-2
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic Data and Generative AI' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 30. Synthetic Data for Deep Learning
- **Source**: paper  **URL**: https://doi.org/10.1007/978-1-4842-8587-9
- **Year/Venue**: 2022 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic Data for Deep Learning' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 31. Foundations of Synthetic data
- **Source**: paper  **URL**: https://doi.org/10.1007/978-1-4842-8587-9_2
- **Year/Venue**: 2022 / Synthetic Data for Deep Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Foundations of Synthetic data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 32. Synthetic data, measured data integrated learning experiments
- **Source**: paper  **URL**: https://doi.org/10.1117/12.2665521
- **Year/Venue**: 2023 / Algorithms for Synthetic Aperture Radar Imagery XXX
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic data, measured data integrated learning experiments' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 33. Synthetic Data in Investment Management
- **Source**: paper  **URL**: https://doi.org/10.56227/25.1.24
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic Data in Investment Management' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 34. Synthetic Data: Servicing Privacy
- **Source**: paper  **URL**: https://doi.org/10.1332/policypress/9781529239683.003.0010
- **Year/Venue**: 2025 / Beyond Privacy
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic Data: Servicing Privacy' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 35. Synthetic data, interpretable regression, and submodels
- **Source**: paper  **URL**: https://doi.org/10.1016/b978-0-44-321857-6.00011-4
- **Year/Venue**: 2024 / Synthetic Data and Generative AI
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic data, interpretable regression, and submodels' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 36. Synthetic Data Generation with Python
- **Source**: paper  **URL**: https://doi.org/10.1007/978-1-4842-8587-9_5
- **Year/Venue**: 2022 / Synthetic Data for Deep Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic Data Generation with Python' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 37. Synthetic Data Generation with R
- **Source**: paper  **URL**: https://doi.org/10.1007/978-1-4842-8587-9_4
- **Year/Venue**: 2022 / Synthetic Data for Deep Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic Data Generation with R' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 38. Artificial Intelligence Agents Powered by Synthetic Data
- **Source**: paper  **URL**: https://doi.org/10.4018/979-8-3373-2277-3.ch004
- **Year/Venue**: 2025 / Digital Synthetic Data and Outputs
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Artificial Intelligence Agents Powered by Synthetic Data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 39. Productivity Enhancements from Digital Synthetic Data
- **Source**: paper  **URL**: https://doi.org/10.4018/979-8-3373-2277-3.ch007
- **Year/Venue**: 2025 / Digital Synthetic Data and Outputs
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Productivity Enhancements from Digital Synthetic Data' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 40. Synthetic Data1
- **Source**: paper  **URL**: https://doi.org/10.1201/9781003185284-13
- **Year/Venue**: 2024 / Handbook of Sharing Confidential Data
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Synthetic Data1' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 41. Methods for Synthetic Data Generation
- **Source**: paper  **URL**: https://doi.org/10.1201/9781003185284-14
- **Year/Venue**: 2024 / Handbook of Sharing Confidential Data
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Methods for Synthetic Data Generation' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 42. The Synthetic Mirror - Synthetic Data at the Age of Agentic AI
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.175022167.74487124/v1
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'The Synthetic Mirror - Synthetic Data at the Age of Agentic AI' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 43. synthesizer: Fast, Robust, and High-Quality Synthetic Data Generation with a Tuneable Privacy-Utility Trade-Off
- **Source**: paper  **URL**: https://doi.org/10.32614/cran.package.synthesizer
- **Year/Venue**: 2024 / CRAN: Contributed Packages
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'synthesizer: Fast, Robust, and High-Quality Synthetic Data Generation with a Tuneable Privacy-Utilit' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 44. Tools to Create Synthetic Data for Brain Images
- **Source**: paper  **URL**: https://doi.org/10.4018/979-8-3693-1886-7.ch011
- **Year/Venue**: 2024 / Advances in Data Mining and Database Management
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'Tools to Create Synthetic Data for Brain Images' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 45. StructSynth: Leveraging LLMs for Structure-Aware Tabular Data Synthesis in Low-Data Regimes
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2508.02601
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.41: paper titled 'StructSynth: Leveraging LLMs for Structure-Aware Tabular Data Synthesis in Low-Data Regimes' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|kw:abstract:fidelity|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 46. Tabular generative modeling framework for multi-property data synthesis of pyrolyzed biochar.
- **Source**: paper  **URL**: https://doi.org/10.1016/j.biortech.2025.133207
- **Year/Venue**: 2025 / Bioresource Technology
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.41: paper titled 'Tabular generative modeling framework for multi-property data synthesis of pyrolyzed biochar.' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|kw:abstract:fidelity|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 47. Synth-MIA: A Testbed for Auditing Privacy Leakage in Tabular Data Synthesis
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2509.18014
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.36: paper titled 'Synth-MIA: A Testbed for Auditing Privacy Leakage in Tabular Data Synthesis' contributes a 'empirical' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|syn:title:data synthesis|syn:abstract:tabular synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 48. argilla-io/distilabel
- **Source**: github  **URL**: https://github.com/argilla-io/distilabel
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'argilla-io/distilabel' (3,211 stars) provides an implementation of 'synthetic data'. Description: distilabel is a framework for synthetic data and ai feedback for engineers who need fast, reliable and scalable pipeline.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 49. hitsz-ids/synthetic-data-generator
- **Source**: github  **URL**: https://github.com/hitsz-ids/synthetic-data-generator
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'hitsz-ids/synthetic-data-generator' (2,417 stars) provides an implementation of 'synthetic data'. Description: sdg is a specialized framework designed to generate high-quality structured tabular data..
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 50. CHATS-lab/verbalized-sampling
- **Source**: github  **URL**: https://github.com/CHATS-lab/verbalized-sampling
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'CHATS-lab/verbalized-sampling' (758 stars) provides an implementation of 'synthetic data'. Description: verbalized sampling, a training-free prompting strategy to mitigate mode collapse in llms by requesting responses with p.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 51. USTCPCS/CVPR2018_attention
- **Source**: github  **URL**: https://github.com/USTCPCS/CVPR2018_attention
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'USTCPCS/CVPR2018_attention' (179 stars) provides an implementation of 'synthetic data'. Description: context encoding for semantic segmentation megadepth: learning single-view depth prediction from internet photos liteflo.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 52. statice/anonymeter
- **Source**: github  **URL**: https://github.com/statice/anonymeter
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'statice/anonymeter' (101 stars) provides an implementation of 'synthetic data'. Description: a unified framework for quantifying privacy risk in synthetic data according to the gdpr.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 53. junchengli1/Sim-Suction-API
- **Source**: github  **URL**: https://github.com/junchengli1/Sim-Suction-API
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'junchengli1/Sim-Suction-API' (47 stars) provides an implementation of 'synthetic data'. Description: sim-suction-api offers a simulation framework to generate synthetic data and train models for robotic suction grasping i.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 54. NVIDIA/synthda
- **Source**: github  **URL**: https://github.com/NVIDIA/synthda
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'NVIDIA/synthda' (46 stars) provides an implementation of 'synthetic data'. Description: synthda is a framework designed to make synthetic data generation for human actions more usable and accessible. this is .
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 55. junchengli1/Sim-Grasp
- **Source**: github  **URL**: https://github.com/junchengli1/Sim-Grasp
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'junchengli1/Sim-Grasp' (45 stars) provides an implementation of 'synthetic data'. Description: sim-grasp offers a simulation framework to generate synthetic data and train models for robotic two finger grasping in c.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 56. haoran1062/so101-autogen
- **Source**: github  **URL**: https://github.com/haoran1062/so101-autogen
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'haoran1062/so101-autogen' (32 stars) provides an implementation of 'synthetic data'. Description: zero teleop, infinite data: the automated synthetic data framework for robotics. / 零遥操，一键生成：您的自动化机器人数据集引擎。.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 57. menyifang/En3D
- **Source**: github  **URL**: https://github.com/menyifang/En3D
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'menyifang/En3D' (541 stars) provides an implementation of 'synthetic data'. Description: official implementation of "en3d: an enhanced generative model for sculpting 3d humans from 2d synthetic data", cvpr 202.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 58. StoryMY/take-off-eyeglasses
- **Source**: github  **URL**: https://github.com/StoryMY/take-off-eyeglasses
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'StoryMY/take-off-eyeglasses' (154 stars) provides an implementation of 'synthetic data'. Description: official pytorch implementation of paper "portrait eyeglasses and shadow removal by leveraging 3d synthetic data" (cvpr .
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 59. declare-lab/RelationPrompt
- **Source**: github  **URL**: https://github.com/declare-lab/RelationPrompt
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'declare-lab/RelationPrompt' (134 stars) provides an implementation of 'synthetic data'. Description: this repository implements our acl findings 2022 research paper relationprompt: leveraging prompts to generate synthetic.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 60. SunzeY/Bootstrap3D
- **Source**: github  **URL**: https://github.com/SunzeY/Bootstrap3D
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'SunzeY/Bootstrap3D' (94 stars) provides an implementation of 'synthetic data'. Description: [iccv-2025] official implementation of bootstrap3d: improving multi-view diffusion model with synthetic data.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 61. ahstat/episodic-memory-benchmark
- **Source**: github  **URL**: https://github.com/ahstat/episodic-memory-benchmark
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'ahstat/episodic-memory-benchmark' (67 stars) provides an implementation of 'synthetic data'. Description: synthetic data generation and benchmark implementation for "episodic memories generation and evaluation benchmark for la.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 62. mirkovicdev/CLUSTERING-MARKET-REGIMES
- **Source**: github  **URL**: https://github.com/mirkovicdev/CLUSTERING-MARKET-REGIMES
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'mirkovicdev/CLUSTERING-MARKET-REGIMES' (58 stars) provides an implementation of 'synthetic data'. Description: python implementation of "clustering market regimes using the wasserstein distance" (horvath et al., 2021). detects bull.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 63. Kiteretsu77/VCISR-official
- **Source**: github  **URL**: https://github.com/Kiteretsu77/VCISR-official
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'Kiteretsu77/VCISR-official' (52 stars) provides an implementation of 'synthetic data'. Description: official implementation of vcisr: blind single image super-resolution with video compression synthetic data (wacv 2024).
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 64. hnavidan/LocalizationGAN
- **Source**: github  **URL**: https://github.com/hnavidan/LocalizationGAN
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'hnavidan/LocalizationGAN' (49 stars) provides an implementation of 'synthetic data'. Description: implementation of the paper using synthetic data to enhance the accuracy of fingerprint-based localization: a deep learn.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 65. Lornatang/Real_ESRGAN-PyTorch
- **Source**: github  **URL**: https://github.com/Lornatang/Real_ESRGAN-PyTorch
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'Lornatang/Real_ESRGAN-PyTorch' (42 stars) provides an implementation of 'synthetic data'. Description: pytorch implements `real-esrgan: training real-world blind super-resolution with pure synthetic data` paper..
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 66. Flame-Chasers/SynTBPR
- **Source**: github  **URL**: https://github.com/Flame-Chasers/SynTBPR
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'Flame-Chasers/SynTBPR' (39 stars) provides an implementation of 'synthetic data'. Description: implement of an empirical study of validating synthetic data for text-based person retrieval.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 67. cRick/NL-to-LTL-Synthetic-Dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/cRick/NL-to-LTL-Synthetic-Dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'cRick/NL-to-LTL-Synthetic-Dataset' (54 downloads) matched 'synthetic data' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 68. Anonymous0624/llm-psychometric-fidelity-audit
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Anonymous0624/llm-psychometric-fidelity-audit
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Anonymous0624/llm-psychometric-fidelity-audit' (21 downloads) matched 'fidelity' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 69. AxonData/ibeta-high-fidelity-rubber-mask-dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/AxonData/ibeta-high-fidelity-rubber-mask-dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'AxonData/ibeta-high-fidelity-rubber-mask-dataset' (27 downloads) matched 'fidelity' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 70. realitydriftproject/semantic-fidelity-examples
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/realitydriftproject/semantic-fidelity-examples
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'realitydriftproject/semantic-fidelity-examples' (23 downloads) matched 'fidelity' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Mixed-Type Tabular Data Synthesis with Score-based Diffusion in Latent Space](https://doi.org/10.48550/arXiv.2310.09656) | 2023 | International Conference on Learning Rep | paper | 0.312 | strong |
| 2 | paper | [HARMONIC: Harnessing LLMs for Tabular Data Synthesis and Privacy Protection](https://doi.org/10.48550/arXiv.2408.02927) | 2024 | Neural Information Processing Systems | paper | 0.312 | strong |
| 3 | paper | [Controllable Tabular Data Synthesis Using Diffusion Models](https://doi.org/10.1145/3639283) | 2024 | Proc. ACM Manag. Data | paper | 0.312 | strong |
| 4 | paper | [EPIC: Effective Prompting for Imbalanced-Class Data Synthesis in Tabular Data Cl](https://doi.org/10.52202/079017-0990) | 2024 | Neural Information Processing Systems | paper | 0.312 | strong |
| 5 | paper | [SampleLLM: Optimizing Tabular Data Synthesis in Recommendations](https://doi.org/10.1145/3701716.3715253) | 2025 | The Web Conference | paper | 0.312 | strong |
| 6 | paper | [Flow Matching for Tabular Data Synthesis](https://doi.org/10.48550/arXiv.2512.00698) | 2025 | Trans. Mach. Learn. Res. | paper | 0.312 | strong |
| 7 | paper | [LogiCoTab: Controllable Tabular Data Synthesis with Logical Relationships Awaren](https://doi.org/10.1109/ICME59968.2025.11209558) | 2025 | IEEE International Conference on Multime | paper | 0.312 | strong |
| 8 | paper | [Oral Cancer Detection by Using Tabular Data Synthesis and Classification](https://doi.org/10.1109/ICDMW69685.2025.00094) | 2025 | 2025 IEEE International Conference on Da | paper | 0.312 | strong |
| 9 | paper | [Measuring LLM Sensitivity in Transformer-based Tabular Data Synthesis](https://doi.org/10.48550/arXiv.2509.20768) | 2025 | arXiv.org | paper | 0.312 | strong |
| 10 | paper | [Hi3dgen: High-Fidelity 3D Geometry Generation From Images Via Normal Bridging](https://doi.org/10.1109/ICCV51701.2025.02323) | 2025 | IEEE International Conference on Compute | paper | 0.3 | strong |
| 11 | paper | [MitoHiFi: a python pipeline for mitochondrial genome assembly from PacBio high f](https://doi.org/10.1186/s12859-023-05385-y) | 2023 | bioRxiv | paper | 0.25 | strong |
| 12 | paper | [ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variationa](https://doi.org/10.48550/arXiv.2305.16213) | 2023 | Neural Information Processing Systems | paper | 0.25 | strong |
| 13 | paper | [High Fidelity Neural Audio Compression](https://doi.org/10.48550/arXiv.2210.13438) | 2022 | Trans. Mach. Learn. Res. | paper | 0.25 | strong |
| 14 | paper | [Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction](https://doi.org/10.1109/CVPR52733.2024.01922) | 2023 | Computer Vision and Pattern Recognition | paper | 0.25 | strong |
| 15 | paper | [High-Fidelity Audio Compression with Improved RVQGAN](https://doi.org/10.48550/arXiv.2306.06546) | 2023 | Neural Information Processing Systems | paper | 0.25 | strong |
| 16 | paper | [ScanNet++: A High-Fidelity Dataset of 3D Indoor Scenes](https://doi.org/10.1109/ICCV51070.2023.00008) | 2023 | IEEE International Conference on Compute | dataset | 0.25 | strong |
| 17 | paper | [Neuralangelo: High-Fidelity Neural Surface Reconstruction](https://doi.org/10.1109/CVPR52729.2023.00817) | 2023 | Computer Vision and Pattern Recognition | paper | 0.25 | strong |
| 18 | paper | [High-fidelity parallel entangling gates on a neutral-atom quantum computer](https://doi.org/10.1038/s41586-023-06481-y) | 2023 | Nature | paper | 0.25 | strong |
| 19 | paper | [ViewCrafter: Taming Video Diffusion Models for High-fidelity Novel View Synthesi](https://doi.org/10.48550/arXiv.2409.02048) | 2024 | IEEE Transactions on Pattern Analysis an | paper | 0.25 | strong |
| 20 | paper | [PGSR: Planar-Based Gaussian Splatting for Efficient and High-Fidelity Surface Re](https://doi.org/10.1109/TVCG.2024.3494046) | 2024 | IEEE Transactions on Visualization and C | paper | 0.25 | strong |
| 21 | paper | [Vista: A Generalizable Driving World Model with High Fidelity and Versatile Cont](https://doi.org/10.48550/arXiv.2405.17398) | 2024 | Neural Information Processing Systems | paper | 0.25 | strong |
| 22 | paper | [Animatable Gaussians: Learning Pose-Dependent Gaussian Maps for High-Fidelity Hu](https://doi.org/10.1109/CVPR52733.2024.01864) | 2024 | Computer Vision and Pattern Recognition | paper | 0.25 | strong |
| 23 | paper | [Jumping Ahead: Improving Reconstruction Fidelity with JumpReLU Sparse Autoencode](https://doi.org/10.48550/arXiv.2407.14435) | 2024 | arXiv.org | paper | 0.25 | strong |
| 24 | paper | [Gaussian Head Avatar: Ultra High-Fidelity Head Avatar via Dynamic Gaussians](https://doi.org/10.1109/CVPR52733.2024.00189) | 2024 | Computer Vision and Pattern Recognition | paper | 0.25 | strong |
| 25 | paper | [TripoSG: High-Fidelity 3D Shape Synthesis using Large-Scale Rectified Flow Model](https://doi.org/10.48550/arXiv.2502.06608) | 2025 | IEEE Transactions on Pattern Analysis an | paper | 0.25 | strong |
| 26 | paper | [Hunyuan3D 2.1: From Images to High-Fidelity 3D Assets with Production-Ready PBR ](https://doi.org/10.48550/arXiv.2506.15442) | 2025 | arXiv.org | paper | 0.25 | strong |
| 27 | paper | [Blind Image Quality Assessment: Exploring Content Fidelity Perceptibility via Qu](https://doi.org/10.1007/s11263-024-02338-7) | 2025 | International Journal of Computer Vision | paper | 0.25 | strong |
| 28 | paper | [Hunyuan3D 2.5: Towards High-Fidelity 3D Assets Generation with Ultimate Details](https://doi.org/10.48550/arXiv.2506.16504) | 2025 | arXiv.org | paper | 0.25 | strong |
| 29 | paper | [Step1X-3D: Towards High-Fidelity and Controllable Generation of Textured 3D Asse](https://doi.org/10.48550/arXiv.2505.07747) | 2025 | arXiv.org | paper | 0.25 | strong |
| 30 | paper | [Animate Anyone 2: High-Fidelity Character Image Animation with Environment Affor](https://doi.org/10.1109/ICCV51701.2025.00951) | 2025 | IEEE International Conference on Compute | paper | 0.25 | strong |
| 31 | paper | [HunyuanVideo-Avatar: High-Fidelity Audio-Driven Human Animation for Multiple Cha](https://doi.org/10.48550/arXiv.2505.20156) | 2025 | arXiv.org | paper | 0.25 | strong |
| 32 | paper | [VideoAnydoor: High-fidelity Video Object Insertion with Precise Motion Control](https://doi.org/10.1145/3721238.3730647) | 2025 | International Conference on Computer Gra | paper | 0.25 | strong |
| 33 | paper | [EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeli](https://doi.org/10.48550/arXiv.2509.23909) | 2025 | arXiv.org | paper | 0.25 | strong |

### 1. Mixed-Type Tabular Data Synthesis with Score-based Diffusion in Latent Space
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2310.09656
- **Year/Venue**: 2023 / International Conference on Learning Representations
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'Mixed-Type Tabular Data Synthesis with Score-based Diffusion in Latent Space' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. HARMONIC: Harnessing LLMs for Tabular Data Synthesis and Privacy Protection
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2408.02927
- **Year/Venue**: 2024 / Neural Information Processing Systems
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'HARMONIC: Harnessing LLMs for Tabular Data Synthesis and Privacy Protection' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. Controllable Tabular Data Synthesis Using Diffusion Models
- **Source**: paper  **URL**: https://doi.org/10.1145/3639283
- **Year/Venue**: 2024 / Proc. ACM Manag. Data
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'Controllable Tabular Data Synthesis Using Diffusion Models' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. EPIC: Effective Prompting for Imbalanced-Class Data Synthesis in Tabular Data Classification via Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.52202/079017-0990
- **Year/Venue**: 2024 / Neural Information Processing Systems
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'EPIC: Effective Prompting for Imbalanced-Class Data Synthesis in Tabular Data Classification via Lar' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. SampleLLM: Optimizing Tabular Data Synthesis in Recommendations
- **Source**: paper  **URL**: https://doi.org/10.1145/3701716.3715253
- **Year/Venue**: 2025 / The Web Conference
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'SampleLLM: Optimizing Tabular Data Synthesis in Recommendations' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. Flow Matching for Tabular Data Synthesis
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2512.00698
- **Year/Venue**: 2025 / Trans. Mach. Learn. Res.
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'Flow Matching for Tabular Data Synthesis' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. LogiCoTab: Controllable Tabular Data Synthesis with Logical Relationships Awareness
- **Source**: paper  **URL**: https://doi.org/10.1109/ICME59968.2025.11209558
- **Year/Venue**: 2025 / IEEE International Conference on Multimedia and Expo
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'LogiCoTab: Controllable Tabular Data Synthesis with Logical Relationships Awareness' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Oral Cancer Detection by Using Tabular Data Synthesis and Classification
- **Source**: paper  **URL**: https://doi.org/10.1109/ICDMW69685.2025.00094
- **Year/Venue**: 2025 / 2025 IEEE International Conference on Data Mining Workshops (ICDMW)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'Oral Cancer Detection by Using Tabular Data Synthesis and Classification' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. Measuring LLM Sensitivity in Transformer-based Tabular Data Synthesis
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2509.20768
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'Measuring LLM Sensitivity in Transformer-based Tabular Data Synthesis' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:abstract:synthetic data|syn:title:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Hi3dgen: High-Fidelity 3D Geometry Generation From Images Via Normal Bridging
- **Source**: paper  **URL**: https://doi.org/10.1109/ICCV51701.2025.02323
- **Year/Venue**: 2025 / IEEE International Conference on Computer Vision
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.30: paper titled 'Hi3dgen: High-Fidelity 3D Geometry Generation From Images Via Normal Bridging' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity|syn:abstract:data synthesis.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. MitoHiFi: a python pipeline for mitochondrial genome assembly from PacBio high fidelity reads
- **Source**: paper  **URL**: https://doi.org/10.1186/s12859-023-05385-y
- **Year/Venue**: 2023 / bioRxiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'MitoHiFi: a python pipeline for mitochondrial genome assembly from PacBio high fidelity reads' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variational Score Distillation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2305.16213
- **Year/Venue**: 2023 / Neural Information Processing Systems
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'ProlificDreamer: High-Fidelity and Diverse Text-to-3D Generation with Variational Score Distillation' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. High Fidelity Neural Audio Compression
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2210.13438
- **Year/Venue**: 2022 / Trans. Mach. Learn. Res.
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'High Fidelity Neural Audio Compression' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 14. Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction
- **Source**: paper  **URL**: https://doi.org/10.1109/CVPR52733.2024.01922
- **Year/Venue**: 2023 / Computer Vision and Pattern Recognition
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Deformable 3D Gaussians for High-Fidelity Monocular Dynamic Scene Reconstruction' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 15. High-Fidelity Audio Compression with Improved RVQGAN
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2306.06546
- **Year/Venue**: 2023 / Neural Information Processing Systems
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'High-Fidelity Audio Compression with Improved RVQGAN' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 16. ScanNet++: A High-Fidelity Dataset of 3D Indoor Scenes
- **Source**: paper  **URL**: https://doi.org/10.1109/ICCV51070.2023.00008
- **Year/Venue**: 2023 / IEEE International Conference on Computer Vision
- **Contribution type**: dataset
- **Why it overlaps**: Relevance 0.25: paper titled 'ScanNet++: A High-Fidelity Dataset of 3D Indoor Scenes' contributes a 'dataset' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 17. Neuralangelo: High-Fidelity Neural Surface Reconstruction
- **Source**: paper  **URL**: https://doi.org/10.1109/CVPR52729.2023.00817
- **Year/Venue**: 2023 / Computer Vision and Pattern Recognition
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Neuralangelo: High-Fidelity Neural Surface Reconstruction' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 18. High-fidelity parallel entangling gates on a neutral-atom quantum computer
- **Source**: paper  **URL**: https://doi.org/10.1038/s41586-023-06481-y
- **Year/Venue**: 2023 / Nature
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'High-fidelity parallel entangling gates on a neutral-atom quantum computer' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 19. ViewCrafter: Taming Video Diffusion Models for High-fidelity Novel View Synthesis
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2409.02048
- **Year/Venue**: 2024 / IEEE Transactions on Pattern Analysis and Machine Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'ViewCrafter: Taming Video Diffusion Models for High-fidelity Novel View Synthesis' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 20. PGSR: Planar-Based Gaussian Splatting for Efficient and High-Fidelity Surface Reconstruction
- **Source**: paper  **URL**: https://doi.org/10.1109/TVCG.2024.3494046
- **Year/Venue**: 2024 / IEEE Transactions on Visualization and Computer Graphics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'PGSR: Planar-Based Gaussian Splatting for Efficient and High-Fidelity Surface Reconstruction' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 21. Vista: A Generalizable Driving World Model with High Fidelity and Versatile Controllability
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2405.17398
- **Year/Venue**: 2024 / Neural Information Processing Systems
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Vista: A Generalizable Driving World Model with High Fidelity and Versatile Controllability' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 22. Animatable Gaussians: Learning Pose-Dependent Gaussian Maps for High-Fidelity Human Avatar Modeling
- **Source**: paper  **URL**: https://doi.org/10.1109/CVPR52733.2024.01864
- **Year/Venue**: 2024 / Computer Vision and Pattern Recognition
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Animatable Gaussians: Learning Pose-Dependent Gaussian Maps for High-Fidelity Human Avatar Modeling' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 23. Jumping Ahead: Improving Reconstruction Fidelity with JumpReLU Sparse Autoencoders
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2407.14435
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Jumping Ahead: Improving Reconstruction Fidelity with JumpReLU Sparse Autoencoders' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 24. Gaussian Head Avatar: Ultra High-Fidelity Head Avatar via Dynamic Gaussians
- **Source**: paper  **URL**: https://doi.org/10.1109/CVPR52733.2024.00189
- **Year/Venue**: 2024 / Computer Vision and Pattern Recognition
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Gaussian Head Avatar: Ultra High-Fidelity Head Avatar via Dynamic Gaussians' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 25. TripoSG: High-Fidelity 3D Shape Synthesis using Large-Scale Rectified Flow Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2502.06608
- **Year/Venue**: 2025 / IEEE Transactions on Pattern Analysis and Machine Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'TripoSG: High-Fidelity 3D Shape Synthesis using Large-Scale Rectified Flow Models' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 26. Hunyuan3D 2.1: From Images to High-Fidelity 3D Assets with Production-Ready PBR Material
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2506.15442
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Hunyuan3D 2.1: From Images to High-Fidelity 3D Assets with Production-Ready PBR Material' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 27. Blind Image Quality Assessment: Exploring Content Fidelity Perceptibility via Quality Adversarial Learning
- **Source**: paper  **URL**: https://doi.org/10.1007/s11263-024-02338-7
- **Year/Venue**: 2025 / International Journal of Computer Vision
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Blind Image Quality Assessment: Exploring Content Fidelity Perceptibility via Quality Adversarial Le' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 28. Hunyuan3D 2.5: Towards High-Fidelity 3D Assets Generation with Ultimate Details
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2506.16504
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Hunyuan3D 2.5: Towards High-Fidelity 3D Assets Generation with Ultimate Details' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 29. Step1X-3D: Towards High-Fidelity and Controllable Generation of Textured 3D Assets
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2505.07747
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Step1X-3D: Towards High-Fidelity and Controllable Generation of Textured 3D Assets' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 30. Animate Anyone 2: High-Fidelity Character Image Animation with Environment Affordance
- **Source**: paper  **URL**: https://doi.org/10.1109/ICCV51701.2025.00951
- **Year/Venue**: 2025 / IEEE International Conference on Computer Vision
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Animate Anyone 2: High-Fidelity Character Image Animation with Environment Affordance' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 31. HunyuanVideo-Avatar: High-Fidelity Audio-Driven Human Animation for Multiple Characters
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2505.20156
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'HunyuanVideo-Avatar: High-Fidelity Audio-Driven Human Animation for Multiple Characters' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 32. VideoAnydoor: High-fidelity Video Object Insertion with Precise Motion Control
- **Source**: paper  **URL**: https://doi.org/10.1145/3721238.3730647
- **Year/Venue**: 2025 / International Conference on Computer Graphics and Interactive Techniques
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'VideoAnydoor: High-fidelity Video Object Insertion with Precise Motion Control' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 33. EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2509.23909
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'EditScore: Unlocking Online RL for Image Editing via High-Fidelity Reward Modeling' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:fidelity.
- **How we differ**: Our proposed work focuses specifically on 'Synthetic data quality evaluation metrics'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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

1. Complete the Artifact Differentiator Checklist above (5 artifacts found).
2. This topic can proceed to GO if artifact differentiator is articulated explicitly.
3. Write one paragraph for §6 verification log explaining differentiation from top artifacts.
