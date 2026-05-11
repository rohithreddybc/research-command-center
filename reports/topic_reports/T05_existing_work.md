# Existing Work Report — T05: Judge confidence calibration vs human gold

> ⚠️ **DIFFERENTIATOR REQUIRED** — paper_direct=0, artifact_direct=3; paper_strength=`strong`, artifact_strength=`strong`.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 0 |
| HuggingFace direct artifacts | 3 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 3 |
| Artifact diff strength | `strong` |
| Partial overlaps (total) | 13 |
| Adjacent | 31 |
| Total findings | 47 |
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
| 1 | huggingface | [potsawee/chatbot-arena-llm-judges](https://huggingface.co/datasets/potsawee/chatbot-arena-llm-judges) |  | HuggingFace | dataset | 170 | strong |
| 2 | huggingface | [eaddario/imatrix-calibration](https://huggingface.co/datasets/eaddario/imatrix-calibration) |  | HuggingFace | dataset | 35734 | strong |
| 3 | huggingface | [calibration-tuning/Mistral-7B-v0.1-20k-oe](https://huggingface.co/datasets/calibration-tuning/Mistral-7B-v0.1-20k-oe) |  | HuggingFace | dataset | 102 | strong |

### 1. potsawee/chatbot-arena-llm-judges
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/potsawee/chatbot-arena-llm-judges
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'potsawee/chatbot-arena-llm-judges' (170 downloads) matched 'LLM judge' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. eaddario/imatrix-calibration
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/eaddario/imatrix-calibration
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'eaddario/imatrix-calibration' (35,734 downloads) matched 'calibration' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. calibration-tuning/Mistral-7B-v0.1-20k-oe
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/calibration-tuning/Mistral-7B-v0.1-20k-oe
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'calibration-tuning/Mistral-7B-v0.1-20k-oe' (102 downloads) matched 'calibration' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box,](https://doi.org/10.48550/arXiv.2504.19254) | 2025 | Trans. Mach. Learn. Res. | paper | 0.6 | moderate |
| 2 | paper | [Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human ](https://doi.org/10.48550/arXiv.2510.09738) | 2025 | arXiv.org | empirical | 0.6 | moderate |
| 3 | paper | [Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations](https://doi.org/10.48550/arXiv.2510.11822) | 2025 | arXiv.org | paper | 0.6 | moderate |
| 4 | paper | [When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silentl](https://doi.org/10.48550/arXiv.2509.20293) | 2025 | arXiv.org | benchmark | 0.6 | moderate |
| 5 | paper | [Auto-Prompt Ensemble for LLM Judge](https://doi.org/10.48550/arXiv.2510.06538) | 2025 | arXiv.org | paper | 0.6 | moderate |
| 6 | paper | [Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Ope](https://doi.org/10.48550/arXiv.2602.05125) | 2026 | arXiv.org | paper | 0.5 | moderate |
| 7 | paper | [Ask a Strong LLM Judge when Your Reward Model is Uncertain](https://doi.org/10.48550/arXiv.2510.20369) | 2025 | arXiv.org | paper | 0.5 | moderate |
| 8 | paper | Tuning LLM Judge Design Decisions for 1/1000 of the Cost | 2025 | International Conference on Machine Lear | paper | 0.5 | moderate |
| 9 | paper | [Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating na](https://doi.org/10.48550/arXiv.2504.02867) | 2025 | arXiv.org | paper | 0.5 | moderate |
| 10 | paper | [DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation](https://doi.org/10.48550/arXiv.2601.22230) | 2026 | arXiv.org | paper | 0.5 | moderate |
| 11 | paper | [ObjexMT: Objective Extraction and Metacognitive Calibration for LLM-as-a-Judge u](https://doi.org/10.48550/arXiv.2508.16889) | 2025 | arXiv.org | paper | 0.438 | moderate |
| 12 | paper | [When the Judge is Wrong: Measuring LLM-as-Judge Reliability Against Graph-Verifi](https://doi.org/10.2139/ssrn.6482162) | 2026 |  | paper | 0.438 | moderate |
| 13 | paper | [Beyond human gold standards: A multimodel framework for automated abstract class](https://doi.org/10.1017/rsm.2025.10054) | 2025 | Research Synthesis Methods | tool | 0.35 | moderate |

### 1. Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ensemble Scorers
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.19254
- **Year/Venue**: 2025 / Trans. Mach. Learn. Res.
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.60: paper titled 'Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ense' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:llm judge|kw:abstract:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.09738
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.60: paper titled 'Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement' contributes a 'empirical' matching target artifact 'empirical'. Matched keywords: primary:title:llm judge|kw:abstract:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.11822
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.60: paper titled 'Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:llm judge|kw:abstract:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2509.20293
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.60: paper titled 'When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity' contributes a 'benchmark' matching target artifact 'empirical'. Matched keywords: primary:title:llm judge|kw:abstract:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. Auto-Prompt Ensemble for LLM Judge
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.06538
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.60: paper titled 'Auto-Prompt Ensemble for LLM Judge' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:llm judge|kw:abstract:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2602.05125
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. Ask a Strong LLM Judge when Your Reward Model is Uncertain
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.20369
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Ask a Strong LLM Judge when Your Reward Model is Uncertain' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. Tuning LLM Judge Design Decisions for 1/1000 of the Cost
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Tuning LLM Judge Design Decisions for 1/1000 of the Cost' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language generation applications
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.02867
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language gener' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2601.22230
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. ObjexMT: Objective Extraction and Metacognitive Calibration for LLM-as-a-Judge under Multi-Turn Jailbreaks
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2508.16889
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.44: paper titled 'ObjexMT: Objective Extraction and Metacognitive Calibration for LLM-as-a-Judge under Multi-Turn Jail' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:abstract:llm judge|kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. When the Judge is Wrong: Measuring LLM-as-Judge Reliability Against Graph-Verified Ground Truth in Financial Documents
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6482162
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.44: paper titled 'When the Judge is Wrong: Measuring LLM-as-Judge Reliability Against Graph-Verified Ground Truth in F' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:abstract:llm judge|kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 13. Beyond human gold standards: A multimodel framework for automated abstract classification and information extraction
- **Source**: paper  **URL**: https://doi.org/10.1017/rsm.2025.10054
- **Year/Venue**: 2025 / Research Synthesis Methods
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.35: paper titled 'Beyond human gold standards: A multimodel framework for automated abstract classification and inform' contributes a 'tool' matching target artifact 'empirical'. Matched keywords: kw:title:human gold|kw:abstract:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [How to Correctly Report LLM-as-a-Judge Evaluations](https://doi.org/10.48550/arXiv.2511.21140) | 2025 | arXiv.org | paper | 0.287 | strong |
| 2 | paper | Causal Judge Evaluation: Calibrated Surrogate Metrics for LLM Systems | 2025 |  | tool | 0.287 | strong |
| 3 | paper | [Universal generating function -based narrow reliability bounds to evaluate relia](https://doi.org/10.1016/j.ress.2021.108121) | 2022 | Reliability Engineering &amp; System Saf | paper | 0.25 | strong |
| 4 | paper | [Calibration Attack: Adversarial Attacks Against Model Calibration](https://doi.org/10.2139/ssrn.4474509) | 2023 |  | paper | 0.25 | strong |
| 5 | paper | [Microelectronics Reliability: Publisher’s note](https://doi.org/10.1016/j.microrel.2023.114902) | 2023 | Microelectronics Reliability | paper | 0.25 | strong |
| 6 | paper | [Design for Reliability (DFR) Aware EDA Solution for Product Reliability (Invited](https://doi.org/10.1109/irps48228.2024.10529434) | 2024 | 2024 IEEE International Reliability Phys | paper | 0.25 | strong |
| 7 | paper | [Reliability improved dual driven feedback 10T SRAM bit cell](https://doi.org/10.1016/j.microrel.2022.114804) | 2022 | Microelectronics Reliability | paper | 0.25 | strong |
| 8 | paper | [Reliability](https://doi.org/10.4324/9780367198459-reprw159-1) | 2022 | Reliability | paper | 0.25 | strong |
| 9 | paper | [Analysis of Experiments for Reliability Improvement and Robust Reliability](https://doi.org/10.1201/9781003418313-9) | 2023 | Recent Advances in Life-Testing and Reli | empirical | 0.25 | strong |
| 10 | paper | [Models of autoantibody mediated diseases: actively nearing the human gold standa](https://doi.org/10.1093/brain/awaf160) | 2025 | Brain : a journal of neurology | paper | 0.25 | strong |
| 11 | paper | [The Impact of Likert Scale Design on Judgment Reliability in Korean and English ](https://doi.org/10.5626/ktcp.2026.32.3.126) | 2026 | KIISE Transactions on Computing Practice | paper | 0.25 | strong |
| 12 | paper | [TUNGSTEN CARBIDE CALIBRATION SPHERES](https://doi.org/10.25144/23629) | 2024 | Underwater Acoustic Calibration and Meas | paper | 0.25 | strong |
| 13 | paper | [ABSOLUTE CALIBRATION OF HYDROPHONES](https://doi.org/10.25144/23632) | 2024 | Underwater Acoustic Calibration and Meas | paper | 0.25 | strong |
| 14 | paper | [A calibration method combining hand-eye calibration and TCP calibration](https://doi.org/10.21203/rs.3.rs-7457937/v1) | 2025 |  | paper | 0.25 | strong |
| 15 | paper | [NuMI Hadron Monitor – Calibration Stand](https://doi.org/10.2172/1998902) | 2023 | NuMI Hadron Monitor – Calibration Stand | paper | 0.25 | strong |
| 16 | paper | [Calibration Principles](https://doi.org/10.1002/9781394442218.ch1) | 2026 | Calibration | paper | 0.25 | strong |
| 17 | paper | [Pressure Instrument Calibration](https://doi.org/10.1002/9781394442218.ch4) | 2026 | Calibration | paper | 0.25 | strong |
| 18 | paper | [Temperature Instrument Calibration](https://doi.org/10.1002/9781394442218.ch3) | 2026 | Calibration | paper | 0.25 | strong |
| 19 | paper | [Level Instrument Calibration](https://doi.org/10.1002/9781394442218.ch5) | 2026 | Calibration | paper | 0.25 | strong |
| 20 | paper | [Flow Instrument Calibration](https://doi.org/10.1002/9781394442218.ch6) | 2026 | Calibration | paper | 0.25 | strong |
| 21 | paper | [UNDERWATER ACOUSTIC CALIBRATION AND MEASUREMENTS IN HSEI](https://doi.org/10.25144/23642) | 2024 | Underwater Acoustic Calibration and Meas | paper | 0.25 | strong |
| 22 | paper | [Final Control Devices Calibration](https://doi.org/10.1002/9781394442218.ch7) | 2026 | Calibration | paper | 0.25 | strong |
| 23 | paper | [Process Analytical Instrument Calibration](https://doi.org/10.1002/9781394442218.ch8) | 2026 | Calibration | paper | 0.25 | strong |
| 24 | paper | [Differential Scanning Calorimetry(DSC) Calibration and Measurement](https://doi.org/10.2172/1989874) | 2023 | Differential Scanning Calorimetry(DSC) C | paper | 0.25 | strong |
| 25 | paper | [International Calibration System (ILAC)](https://doi.org/10.1002/9781394442188.ch2) | 2026 | Calibration Handbook of Measuring Instru | tool | 0.25 | strong |
| 26 | paper | [ReliaLearnR: Learning Modules for Reliability Analysis](https://doi.org/10.32614/cran.package.relialearnr) | 2026 | CRAN: Contributed Packages | empirical | 0.25 | strong |
| 27 | paper | [System Reliability](https://doi.org/10.1017/9781108991889.009) | 2022 | Structural and System Reliability | tool | 0.25 | strong |
| 28 | paper | [Increase Effectiveness of Reliability Tools with the Role of Reliability Czar](https://doi.org/10.1109/rams51473.2023.10088195) | 2023 | 2023 Annual Reliability and Maintainabil | tool | 0.25 | strong |
| 29 | paper | [A fuzzy-arithmetic-based reliability assessment model for digital circuits (FARA](https://doi.org/10.1016/j.microrel.2025.115893) | 2025 | Microelectronics Reliability | paper | 0.25 | strong |
| 30 | paper | [reliacoef: Unidimensional and Multidimensional Reliability Coefficients](https://doi.org/10.32614/cran.package.reliacoef) | 2026 | CRAN: Contributed Packages | paper | 0.25 | strong |
| 31 | paper | [Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution](https://doi.org/10.48550/arXiv.2508.06225) | 2025 | arXiv.org | paper | 0.2 | strong |

### 1. How to Correctly Report LLM-as-a-Judge Evaluations
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2511.21140
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.29: paper titled 'How to Correctly Report LLM-as-a-Judge Evaluations' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:abstract:llm judge|kw:abstract:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. Causal Judge Evaluation: Calibrated Surrogate Metrics for LLM Systems
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2025 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.29: paper titled 'Causal Judge Evaluation: Calibrated Surrogate Metrics for LLM Systems' contributes a 'tool' matching target artifact 'empirical'. Matched keywords: primary:abstract:llm judge|kw:abstract:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. Universal generating function -based narrow reliability bounds to evaluate reliability of project completion time
- **Source**: paper  **URL**: https://doi.org/10.1016/j.ress.2021.108121
- **Year/Venue**: 2022 / Reliability Engineering &amp; System Safety
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Universal generating function -based narrow reliability bounds to evaluate reliability of project co' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. Calibration Attack: Adversarial Attacks Against Model Calibration
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.4474509
- **Year/Venue**: 2023 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Calibration Attack: Adversarial Attacks Against Model Calibration' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. Microelectronics Reliability: Publisher’s note
- **Source**: paper  **URL**: https://doi.org/10.1016/j.microrel.2023.114902
- **Year/Venue**: 2023 / Microelectronics Reliability
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Microelectronics Reliability: Publisher’s note' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. Design for Reliability (DFR) Aware EDA Solution for Product Reliability (Invited)
- **Source**: paper  **URL**: https://doi.org/10.1109/irps48228.2024.10529434
- **Year/Venue**: 2024 / 2024 IEEE International Reliability Physics Symposium (IRPS)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Design for Reliability (DFR) Aware EDA Solution for Product Reliability (Invited)' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. Reliability improved dual driven feedback 10T SRAM bit cell
- **Source**: paper  **URL**: https://doi.org/10.1016/j.microrel.2022.114804
- **Year/Venue**: 2022 / Microelectronics Reliability
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reliability improved dual driven feedback 10T SRAM bit cell' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Reliability
- **Source**: paper  **URL**: https://doi.org/10.4324/9780367198459-reprw159-1
- **Year/Venue**: 2022 / Reliability
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reliability' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. Analysis of Experiments for Reliability Improvement and Robust Reliability
- **Source**: paper  **URL**: https://doi.org/10.1201/9781003418313-9
- **Year/Venue**: 2023 / Recent Advances in Life-Testing and Reliability
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'Analysis of Experiments for Reliability Improvement and Robust Reliability' contributes a 'empirical' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Models of autoantibody mediated diseases: actively nearing the human gold standard.
- **Source**: paper  **URL**: https://doi.org/10.1093/brain/awaf160
- **Year/Venue**: 2025 / Brain : a journal of neurology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Models of autoantibody mediated diseases: actively nearing the human gold standard.' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:human gold.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. The Impact of Likert Scale Design on Judgment Reliability in Korean and English LLM-as-a-Judge
- **Source**: paper  **URL**: https://doi.org/10.5626/ktcp.2026.32.3.126
- **Year/Venue**: 2026 / KIISE Transactions on Computing Practices
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Impact of Likert Scale Design on Judgment Reliability in Korean and English LLM-as-a-Judge' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. TUNGSTEN CARBIDE CALIBRATION SPHERES
- **Source**: paper  **URL**: https://doi.org/10.25144/23629
- **Year/Venue**: 2024 / Underwater Acoustic Calibration and Measurements 1984
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'TUNGSTEN CARBIDE CALIBRATION SPHERES' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. ABSOLUTE CALIBRATION OF HYDROPHONES
- **Source**: paper  **URL**: https://doi.org/10.25144/23632
- **Year/Venue**: 2024 / Underwater Acoustic Calibration and Measurements 1984
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'ABSOLUTE CALIBRATION OF HYDROPHONES' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 14. A calibration method combining hand-eye calibration and TCP calibration
- **Source**: paper  **URL**: https://doi.org/10.21203/rs.3.rs-7457937/v1
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'A calibration method combining hand-eye calibration and TCP calibration' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 15. NuMI Hadron Monitor – Calibration Stand
- **Source**: paper  **URL**: https://doi.org/10.2172/1998902
- **Year/Venue**: 2023 / NuMI Hadron Monitor – Calibration Stand
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'NuMI Hadron Monitor – Calibration Stand' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 16. Calibration Principles
- **Source**: paper  **URL**: https://doi.org/10.1002/9781394442218.ch1
- **Year/Venue**: 2026 / Calibration
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Calibration Principles' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 17. Pressure Instrument Calibration
- **Source**: paper  **URL**: https://doi.org/10.1002/9781394442218.ch4
- **Year/Venue**: 2026 / Calibration
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pressure Instrument Calibration' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 18. Temperature Instrument Calibration
- **Source**: paper  **URL**: https://doi.org/10.1002/9781394442218.ch3
- **Year/Venue**: 2026 / Calibration
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Temperature Instrument Calibration' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 19. Level Instrument Calibration
- **Source**: paper  **URL**: https://doi.org/10.1002/9781394442218.ch5
- **Year/Venue**: 2026 / Calibration
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Level Instrument Calibration' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 20. Flow Instrument Calibration
- **Source**: paper  **URL**: https://doi.org/10.1002/9781394442218.ch6
- **Year/Venue**: 2026 / Calibration
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Flow Instrument Calibration' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 21. UNDERWATER ACOUSTIC CALIBRATION AND MEASUREMENTS IN HSEI
- **Source**: paper  **URL**: https://doi.org/10.25144/23642
- **Year/Venue**: 2024 / Underwater Acoustic Calibration and Measurements 1984
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'UNDERWATER ACOUSTIC CALIBRATION AND MEASUREMENTS IN HSEI' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 22. Final Control Devices Calibration
- **Source**: paper  **URL**: https://doi.org/10.1002/9781394442218.ch7
- **Year/Venue**: 2026 / Calibration
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Final Control Devices Calibration' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 23. Process Analytical Instrument Calibration
- **Source**: paper  **URL**: https://doi.org/10.1002/9781394442218.ch8
- **Year/Venue**: 2026 / Calibration
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Process Analytical Instrument Calibration' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 24. Differential Scanning Calorimetry(DSC) Calibration and Measurement
- **Source**: paper  **URL**: https://doi.org/10.2172/1989874
- **Year/Venue**: 2023 / Differential Scanning Calorimetry(DSC) Calibration and Measurement
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Differential Scanning Calorimetry(DSC) Calibration and Measurement' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 25. International Calibration System (ILAC)
- **Source**: paper  **URL**: https://doi.org/10.1002/9781394442188.ch2
- **Year/Venue**: 2026 / Calibration Handbook of Measuring Instruments
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'International Calibration System (ILAC)' contributes a 'tool' matching target artifact 'empirical'. Matched keywords: kw:title:calibration.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 26. ReliaLearnR: Learning Modules for Reliability Analysis
- **Source**: paper  **URL**: https://doi.org/10.32614/cran.package.relialearnr
- **Year/Venue**: 2026 / CRAN: Contributed Packages
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'ReliaLearnR: Learning Modules for Reliability Analysis' contributes a 'empirical' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 27. System Reliability
- **Source**: paper  **URL**: https://doi.org/10.1017/9781108991889.009
- **Year/Venue**: 2022 / Structural and System Reliability
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'System Reliability' contributes a 'tool' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 28. Increase Effectiveness of Reliability Tools with the Role of Reliability Czar
- **Source**: paper  **URL**: https://doi.org/10.1109/rams51473.2023.10088195
- **Year/Venue**: 2023 / 2023 Annual Reliability and Maintainability Symposium (RAMS)
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'Increase Effectiveness of Reliability Tools with the Role of Reliability Czar' contributes a 'tool' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 29. A fuzzy-arithmetic-based reliability assessment model for digital circuits (FARAM-DC)
- **Source**: paper  **URL**: https://doi.org/10.1016/j.microrel.2025.115893
- **Year/Venue**: 2025 / Microelectronics Reliability
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'A fuzzy-arithmetic-based reliability assessment model for digital circuits (FARAM-DC)' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 30. reliacoef: Unidimensional and Multidimensional Reliability Coefficients
- **Source**: paper  **URL**: https://doi.org/10.32614/cran.package.reliacoef
- **Year/Venue**: 2026 / CRAN: Contributed Packages
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'reliacoef: Unidimensional and Multidimensional Reliability Coefficients' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 31. Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2508.06225
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.20: paper titled 'Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:abstract:calibration|kw:abstract:reliability.
- **How we differ**: Our proposed work focuses specifically on 'Judge confidence calibration vs human gold'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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

1. Complete the Artifact Differentiator Checklist above (3 artifacts found).
2. This topic can proceed to GO if artifact differentiator is articulated explicitly.
3. Write one paragraph for §6 verification log explaining differentiation from top artifacts.
