# Existing Work Report — T43: Reproducibility audit of clinical LLM papers

> ⚠️ **DIFFERENTIATOR REQUIRED** — paper_direct=0, artifact_direct=2; paper_strength=`strong`, artifact_strength=`strong`.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 0 |
| HuggingFace direct artifacts | 2 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 2 |
| Artifact diff strength | `strong` |
| Partial overlaps (total) | 3 |
| Adjacent | 29 |
| Total findings | 34 |
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
| 1 | huggingface | [AI-EcoNet/HUGO-Bench-Paper-Reproducibility](https://huggingface.co/datasets/AI-EcoNet/HUGO-Bench-Paper-Reproducibility) |  | HuggingFace | dataset | 261 | strong |
| 2 | huggingface | [zyzhou110/Squidiff_reproducibility](https://huggingface.co/datasets/zyzhou110/Squidiff_reproducibility) |  | HuggingFace | dataset | 106 | strong |

### 1. AI-EcoNet/HUGO-Bench-Paper-Reproducibility
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/AI-EcoNet/HUGO-Bench-Paper-Reproducibility
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'AI-EcoNet/HUGO-Bench-Paper-Reproducibility' (261 downloads) matched 'reproducibility' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. zyzhou110/Squidiff_reproducibility
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/zyzhou110/Squidiff_reproducibility
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'zyzhou110/Squidiff_reproducibility' (106 downloads) matched 'reproducibility' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | huggingface | [bird-of-paradise/muon-distributed-reproducibility](https://huggingface.co/datasets/bird-of-paradise/muon-distributed-reproducibility) |  | HuggingFace | dataset | 40 | moderate |
| 2 | huggingface | [throwaway-reproducibility-354364563/FinTrain](https://huggingface.co/datasets/throwaway-reproducibility-354364563/FinTrain) |  | HuggingFace | dataset | 21 | moderate |
| 3 | huggingface | [anon7f3k2026/neurips_reproducibility_bundle](https://huggingface.co/datasets/anon7f3k2026/neurips_reproducibility_bundle) |  | HuggingFace | dataset | 22 | moderate |

### 1. bird-of-paradise/muon-distributed-reproducibility
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/bird-of-paradise/muon-distributed-reproducibility
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'bird-of-paradise/muon-distributed-reproducibility' (40 downloads) matched 'reproducibility' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. throwaway-reproducibility-354364563/FinTrain
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/throwaway-reproducibility-354364563/FinTrain
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'throwaway-reproducibility-354364563/FinTrain' (21 downloads) matched 'reproducibility' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. anon7f3k2026/neurips_reproducibility_bundle
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/anon7f3k2026/neurips_reproducibility_bundle
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'anon7f3k2026/neurips_reproducibility_bundle' (22 downloads) matched 'reproducibility' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Leakage and the reproducibility crisis in machine-learning-based science](https://doi.org/10.1016/j.patter.2023.100804) | 2023 | Patterns | paper | 0.25 | strong |
| 2 | paper | [Benchmarking the reproducibility of all-solid-state battery cell performance](https://doi.org/10.1038/s41560-024-01634-3) | 2024 | Nature Energy | benchmark | 0.25 | strong |
| 3 | paper | [A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Repr](https://doi.org/10.48550/arXiv.2504.07086) | 2025 | arXiv.org | paper | 0.25 | strong |
| 4 | paper | [Reproducibility in Machine Learning-based Research: Overview, Barriers and Drive](https://doi.org/10.48550/arXiv.2406.14325) | 2024 | The AI Magazine | survey | 0.25 | strong |
| 5 | paper | [Radiomics and Deep Features: Robust Classification of Brain Hemorrhages and Repr](https://doi.org/10.3390/bioengineering11070643) | 2024 | Bioengineering | empirical | 0.25 | strong |
| 6 | paper | [CORE-Bench: Fostering the Credibility of Published Research Through a Computatio](https://doi.org/10.48550/arXiv.2409.11363) | 2024 | Trans. Mach. Learn. Res. | benchmark | 0.25 | strong |
| 7 | paper | [Flexible Temperature Sensor with High Reproducibility and Wireless Closed‐Loop S](https://doi.org/10.1002/adma.202407859) | 2024 | Advances in Materials | tool | 0.25 | strong |
| 8 | paper | [Reproducibility of in vivo electrophysiological measurements in mice](https://doi.org/10.1101/2022.05.09.491042) | 2024 | bioRxiv | paper | 0.25 | strong |
| 9 | paper | The Model Openness Framework: Promoting Completeness and Openness for Reproducib | 2024 |  | tool | 0.25 | strong |
| 10 | paper | [Fluorinated isopropanol for improved defect passivation and reproducibility in p](https://doi.org/10.1038/s41560-025-01791-z) | 2025 | Nature Energy | paper | 0.25 | strong |
| 11 | paper | [Assessing Consistency and Reproducibility in the Outputs of Large Language Model](https://doi.org/10.48550/arXiv.2503.16974) | 2025 | arXiv.org | paper | 0.25 | strong |
| 12 | paper | [Discordance, accuracy and reproducibility study of pathologists’ diagnosis of me](https://doi.org/10.1038/s41467-025-56160-x) | 2025 | Nature Communications | empirical | 0.25 | strong |
| 13 | paper | [fNIRS reproducibility varies with data quality, analysis pipelines, and research](https://doi.org/10.1038/s42003-025-08412-1) | 2025 | Communications Biology | empirical | 0.25 | strong |
| 14 | paper | [Open science interventions to improve reproducibility and replicability of resea](https://doi.org/10.1098/rsos.242057) | 2025 | Royal Society Open Science | survey | 0.25 | strong |
| 15 | paper | ['Publish or perish' culture blamed for reproducibility crisis.](https://doi.org/10.1038/d41586-024-04253-w) | 2025 | Nature | paper | 0.25 | strong |
| 16 | paper | [Reproducibility in Management Science](https://doi.org/10.31219/osf.io/mydzv) | 2023 |  | paper | 0.25 | strong |
| 17 | paper | [After Computational Reproducibility: Scientific Reproducibility and Trustworthy ](https://doi.org/10.1162/99608f92.ea5e6f9a) | 2024 | Harvard Data Science Review | paper | 0.25 | strong |
| 18 | paper | [Summer of Reproducibility: Building Global Capacity for Practical Reproducibilit](https://doi.org/10.1145/3736731.3746149) | 2025 | Proceedings of the 3rd ACM Conference on | paper | 0.25 | strong |
| 19 | paper | [BioModels Reproducibility Scorecard](https://doi.org/10.52843/cassyni.x36fmy) | 2022 |  | paper | 0.25 | strong |
| 20 | paper | [Reproducibility](https://doi.org/10.5194/egusphere-2025-5497-rc1) | 2026 |  | paper | 0.25 | strong |
| 21 | paper | [Rigor and Reproducibility in Research](https://doi.org/10.4135/9781036219994) | 2024 |  | paper | 0.25 | strong |
| 22 | paper | [Validity of biomedical science, reproducibility, and irreproducibility](https://doi.org/10.1016/b978-0-443-13829-4.00013-1) | 2024 | Reproducibility in Biomedical Research | paper | 0.25 | strong |
| 23 | paper | [Committing to Reproducibility and Explainability]{Committing to Reproducibility ](https://doi.org/10.21203/rs.3.rs-2640542/v1) | 2023 |  | paper | 0.25 | strong |
| 24 | paper | [Form to Assess Result Reproducibility of Manuscripts](https://doi.org/10.1061/reprod.000001) | 2024 |  | paper | 0.25 | strong |
| 25 | paper | [Reproducibility, Transparency, Positionality? Perspectives From Different Resear](https://doi.org/10.52843/cassyni.dq8svs) | 2024 |  | paper | 0.25 | strong |
| 26 | paper | [More information needed for reproducibility](https://doi.org/10.5194/egusphere-2025-5497-cc5) | 2025 |  | paper | 0.25 | strong |
| 27 | paper | [Resolution and Reproducibility](https://doi.org/10.5194/egusphere-2024-3560-ac2) | 2025 |  | paper | 0.25 | strong |
| 28 | paper | [reproducibility, n.](https://doi.org/10.1093/oed/4082406807) | 2023 | Oxford English Dictionary | paper | 0.25 | strong |
| 29 | paper | [Reproducibility in Biomedical Research](https://doi.org/10.1016/c2022-0-02971-8) | 2024 |  | paper | 0.25 | strong |

### 1. Leakage and the reproducibility crisis in machine-learning-based science
- **Source**: paper  **URL**: https://doi.org/10.1016/j.patter.2023.100804
- **Year/Venue**: 2023 / Patterns
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Leakage and the reproducibility crisis in machine-learning-based science' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. Benchmarking the reproducibility of all-solid-state battery cell performance
- **Source**: paper  **URL**: https://doi.org/10.1038/s41560-024-01634-3
- **Year/Venue**: 2024 / Nature Energy
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'Benchmarking the reproducibility of all-solid-state battery cell performance' contributes a 'benchmark' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.07086
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'A Sober Look at Progress in Language Model Reasoning: Pitfalls and Paths to Reproducibility' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. Reproducibility in Machine Learning-based Research: Overview, Barriers and Drivers
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2406.14325
- **Year/Venue**: 2024 / The AI Magazine
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility in Machine Learning-based Research: Overview, Barriers and Drivers' contributes a 'survey' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. Radiomics and Deep Features: Robust Classification of Brain Hemorrhages and Reproducibility Analysis Using a 3D Autoenco
- **Source**: paper  **URL**: https://doi.org/10.3390/bioengineering11070643
- **Year/Venue**: 2024 / Bioengineering
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'Radiomics and Deep Features: Robust Classification of Brain Hemorrhages and Reproducibility Analysis' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility Agent Benchmark
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2409.11363
- **Year/Venue**: 2024 / Trans. Mach. Learn. Res.
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'CORE-Bench: Fostering the Credibility of Published Research Through a Computational Reproducibility ' contributes a 'benchmark' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. Flexible Temperature Sensor with High Reproducibility and Wireless Closed‐Loop System for Decoupled Multimodal Health Mo
- **Source**: paper  **URL**: https://doi.org/10.1002/adma.202407859
- **Year/Venue**: 2024 / Advances in Materials
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'Flexible Temperature Sensor with High Reproducibility and Wireless Closed‐Loop System for Decoupled ' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Reproducibility of in vivo electrophysiological measurements in mice
- **Source**: paper  **URL**: https://doi.org/10.1101/2022.05.09.491042
- **Year/Venue**: 2024 / bioRxiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility of in vivo electrophysiological measurements in mice' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. The Model Openness Framework: Promoting Completeness and Openness for Reproducibility, Transparency, and Usability in Ar
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2024 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'The Model Openness Framework: Promoting Completeness and Openness for Reproducibility, Transparency,' contributes a 'tool' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Fluorinated isopropanol for improved defect passivation and reproducibility in perovskite solar cells
- **Source**: paper  **URL**: https://doi.org/10.1038/s41560-025-01791-z
- **Year/Venue**: 2025 / Nature Energy
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Fluorinated isopropanol for improved defect passivation and reproducibility in perovskite solar cell' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. Assessing Consistency and Reproducibility in the Outputs of Large Language Models: Evidence Across Diverse Finance and A
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2503.16974
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Assessing Consistency and Reproducibility in the Outputs of Large Language Models: Evidence Across D' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. Discordance, accuracy and reproducibility study of pathologists’ diagnosis of melanoma and melanocytic tumors
- **Source**: paper  **URL**: https://doi.org/10.1038/s41467-025-56160-x
- **Year/Venue**: 2025 / Nature Communications
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'Discordance, accuracy and reproducibility study of pathologists’ diagnosis of melanoma and melanocyt' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. fNIRS reproducibility varies with data quality, analysis pipelines, and researcher experience
- **Source**: paper  **URL**: https://doi.org/10.1038/s42003-025-08412-1
- **Year/Venue**: 2025 / Communications Biology
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'fNIRS reproducibility varies with data quality, analysis pipelines, and researcher experience' contributes a 'empirical' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 14. Open science interventions to improve reproducibility and replicability of research: a scoping review
- **Source**: paper  **URL**: https://doi.org/10.1098/rsos.242057
- **Year/Venue**: 2025 / Royal Society Open Science
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.25: paper titled 'Open science interventions to improve reproducibility and replicability of research: a scoping revie' contributes a 'survey' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 15. 'Publish or perish' culture blamed for reproducibility crisis.
- **Source**: paper  **URL**: https://doi.org/10.1038/d41586-024-04253-w
- **Year/Venue**: 2025 / Nature
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled ''Publish or perish' culture blamed for reproducibility crisis.' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 16. Reproducibility in Management Science
- **Source**: paper  **URL**: https://doi.org/10.31219/osf.io/mydzv
- **Year/Venue**: 2023 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility in Management Science' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 17. After Computational Reproducibility: Scientific Reproducibility and Trustworthy AI
- **Source**: paper  **URL**: https://doi.org/10.1162/99608f92.ea5e6f9a
- **Year/Venue**: 2024 / Harvard Data Science Review
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'After Computational Reproducibility: Scientific Reproducibility and Trustworthy AI' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 18. Summer of Reproducibility: Building Global Capacity for Practical Reproducibility through Hands-On Mentorship
- **Source**: paper  **URL**: https://doi.org/10.1145/3736731.3746149
- **Year/Venue**: 2025 / Proceedings of the 3rd ACM Conference on Reproducibility and Replicability
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Summer of Reproducibility: Building Global Capacity for Practical Reproducibility through Hands-On M' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 19. BioModels Reproducibility Scorecard
- **Source**: paper  **URL**: https://doi.org/10.52843/cassyni.x36fmy
- **Year/Venue**: 2022 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'BioModels Reproducibility Scorecard' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 20. Reproducibility
- **Source**: paper  **URL**: https://doi.org/10.5194/egusphere-2025-5497-rc1
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 21. Rigor and Reproducibility in Research
- **Source**: paper  **URL**: https://doi.org/10.4135/9781036219994
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Rigor and Reproducibility in Research' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 22. Validity of biomedical science, reproducibility, and irreproducibility
- **Source**: paper  **URL**: https://doi.org/10.1016/b978-0-443-13829-4.00013-1
- **Year/Venue**: 2024 / Reproducibility in Biomedical Research
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Validity of biomedical science, reproducibility, and irreproducibility' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 23. Committing to Reproducibility and Explainability]{Committing to Reproducibility and Explainability: Version Control as R
- **Source**: paper  **URL**: https://doi.org/10.21203/rs.3.rs-2640542/v1
- **Year/Venue**: 2023 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Committing to Reproducibility and Explainability]{Committing to Reproducibility and Explainability: ' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 24. Form to Assess Result Reproducibility of Manuscripts
- **Source**: paper  **URL**: https://doi.org/10.1061/reprod.000001
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Form to Assess Result Reproducibility of Manuscripts' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 25. Reproducibility, Transparency, Positionality? Perspectives From Different Research Fields
- **Source**: paper  **URL**: https://doi.org/10.52843/cassyni.dq8svs
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility, Transparency, Positionality? Perspectives From Different Research Fields' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 26. More information needed for reproducibility
- **Source**: paper  **URL**: https://doi.org/10.5194/egusphere-2025-5497-cc5
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'More information needed for reproducibility' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 27. Resolution and Reproducibility
- **Source**: paper  **URL**: https://doi.org/10.5194/egusphere-2024-3560-ac2
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Resolution and Reproducibility' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 28. reproducibility, n.
- **Source**: paper  **URL**: https://doi.org/10.1093/oed/4082406807
- **Year/Venue**: 2023 / Oxford English Dictionary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'reproducibility, n.' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 29. Reproducibility in Biomedical Research
- **Source**: paper  **URL**: https://doi.org/10.1016/c2022-0-02971-8
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Reproducibility in Biomedical Research' contributes a 'paper' matching target artifact 'database+paper'. Matched keywords: kw:title:reproducibility.
- **How we differ**: Our proposed work focuses specifically on 'Reproducibility audit of clinical LLM papers'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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

1. Complete the Artifact Differentiator Checklist above (2 artifacts found).
2. This topic can proceed to GO if artifact differentiator is articulated explicitly.
3. Write one paragraph for §6 verification log explaining differentiation from top artifacts.
