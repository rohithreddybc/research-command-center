# Existing Work Report — T06: Pairwise vs pointwise judge agreement under perturbation

> ⚠️ **DIFFERENTIATOR REQUIRED** — paper_direct=0, artifact_direct=2; paper_strength=`strong`, artifact_strength=`moderate`.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 0 |
| HuggingFace direct artifacts | 2 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 2 |
| Artifact diff strength | `moderate` |
| Partial overlaps (total) | 10 |
| Adjacent | 40 |
| Total findings | 52 |
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
| 1 | huggingface | [Dahoas/synthetic-instruct-gptj-pairwise](https://huggingface.co/datasets/Dahoas/synthetic-instruct-gptj-pairwise) |  | HuggingFace | dataset | 585 | moderate |
| 2 | huggingface | [tasksource/oasst1_pairwise_rlhf_reward](https://huggingface.co/datasets/tasksource/oasst1_pairwise_rlhf_reward) |  | HuggingFace | dataset | 225 | moderate |

### 1. Dahoas/synthetic-instruct-gptj-pairwise
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Dahoas/synthetic-instruct-gptj-pairwise
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Dahoas/synthetic-instruct-gptj-pairwise' (585 downloads) matched 'pairwise' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. tasksource/oasst1_pairwise_rlhf_reward
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/tasksource/oasst1_pairwise_rlhf_reward
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'tasksource/oasst1_pairwise_rlhf_reward' (225 downloads) matched 'pairwise' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Alternative Approaches to the Evaluation of Inconsistency in Pairwise Comparison](https://doi.org/10.1007/978-3-031-23884-0_5) | 2022 | Multiple Criteria Decision Making | paper | 0.375 | moderate |
| 2 | paper | [Multiplicative Pairwise Comparisons](https://doi.org/10.1007/978-3-031-23884-0_2) | 2022 | Multiple Criteria Decision Making | paper | 0.375 | moderate |
| 3 | paper | [Experience-Based Pairwise Comparison Dynamics](https://doi.org/10.2139/ssrn.5565060) | 2025 |  | paper | 0.375 | moderate |
| 4 | paper | [Inconsistency of Incomplete Pairwise Comparisons Matrices](https://doi.org/10.1007/978-3-031-23884-0_6) | 2022 | Multiple Criteria Decision Making | paper | 0.375 | moderate |
| 5 | paper | [On Strict Ranking by Pairwise Comparisons](https://doi.org/10.2139/ssrn.5081659) | 2025 |  | paper | 0.375 | moderate |
| 6 | paper | [Desirable Gambles Based on Pairwise Comparisons](https://doi.org/10.2139/ssrn.4620450) | 2023 |  | paper | 0.375 | moderate |
| 7 | huggingface | [reshinthadith/pairwise-code-review-instruct-critique-revision-python](https://huggingface.co/datasets/reshinthadith/pairwise-code-review-instruct-critique-revision-python) |  | HuggingFace | dataset | 48 | moderate |
| 8 | huggingface | [andersonbcdefg/red_teaming_reward_modeling_pairwise](https://huggingface.co/datasets/andersonbcdefg/red_teaming_reward_modeling_pairwise) |  | HuggingFace | dataset | 24 | moderate |
| 9 | huggingface | [rahulseetharaman/msmarco-llm-reranking-pointwise-tokenized](https://huggingface.co/datasets/rahulseetharaman/msmarco-llm-reranking-pointwise-tokenized) |  | HuggingFace | dataset | 29 | moderate |
| 10 | huggingface | [HCY123902/qwen25_7b_base_hc_ssss_n32_r1_pointwise_no_rubric_dpo](https://huggingface.co/datasets/HCY123902/qwen25_7b_base_hc_ssss_n32_r1_pointwise_no_rubric_dpo) |  | HuggingFace | dataset | 31 | moderate |

### 1. Alternative Approaches to the Evaluation of Inconsistency in Pairwise Comparisons
- **Source**: paper  **URL**: https://doi.org/10.1007/978-3-031-23884-0_5
- **Year/Venue**: 2022 / Multiple Criteria Decision Making
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Alternative Approaches to the Evaluation of Inconsistency in Pairwise Comparisons' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise|syn:title:pairwise comparison.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. Multiplicative Pairwise Comparisons
- **Source**: paper  **URL**: https://doi.org/10.1007/978-3-031-23884-0_2
- **Year/Venue**: 2022 / Multiple Criteria Decision Making
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Multiplicative Pairwise Comparisons' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise|syn:title:pairwise comparison.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. Experience-Based Pairwise Comparison Dynamics
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.5565060
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Experience-Based Pairwise Comparison Dynamics' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise|syn:title:pairwise comparison.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. Inconsistency of Incomplete Pairwise Comparisons Matrices
- **Source**: paper  **URL**: https://doi.org/10.1007/978-3-031-23884-0_6
- **Year/Venue**: 2022 / Multiple Criteria Decision Making
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Inconsistency of Incomplete Pairwise Comparisons Matrices' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise|syn:title:pairwise comparison.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. On Strict Ranking by Pairwise Comparisons
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.5081659
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'On Strict Ranking by Pairwise Comparisons' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise|syn:title:pairwise comparison.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. Desirable Gambles Based on Pairwise Comparisons
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.4620450
- **Year/Venue**: 2023 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Desirable Gambles Based on Pairwise Comparisons' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise|syn:title:pairwise comparison.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. reshinthadith/pairwise-code-review-instruct-critique-revision-python
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/reshinthadith/pairwise-code-review-instruct-critique-revision-python
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'reshinthadith/pairwise-code-review-instruct-critique-revision-python' (48 downloads) matched 'pairwise' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. andersonbcdefg/red_teaming_reward_modeling_pairwise
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/andersonbcdefg/red_teaming_reward_modeling_pairwise
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'andersonbcdefg/red_teaming_reward_modeling_pairwise' (24 downloads) matched 'pairwise' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. rahulseetharaman/msmarco-llm-reranking-pointwise-tokenized
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/rahulseetharaman/msmarco-llm-reranking-pointwise-tokenized
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'rahulseetharaman/msmarco-llm-reranking-pointwise-tokenized' (29 downloads) matched 'pointwise' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. HCY123902/qwen25_7b_base_hc_ssss_n32_r1_pointwise_no_rubric_dpo
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/HCY123902/qwen25_7b_base_hc_ssss_n32_r1_pointwise_no_rubric_dpo
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'HCY123902/qwen25_7b_base_hc_ssss_n32_r1_pointwise_no_rubric_dpo' (31 downloads) matched 'pointwise' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Perturbation-adapted perturbation theory](https://doi.org/10.1063/5.0079853) | 2022 | The Journal of Chemical Physics | paper | 0.25 | strong |
| 2 | paper | [Pointwise semi-slant Riemannian maps into almost Hermitian manifolds and Casorat](https://doi.org/10.3842/umzh.v76i9.7652) | 2025 | Ukrains’kyi Matematychnyi Zhurnal | paper | 0.25 | strong |
| 3 | paper | [Pairwise Sequence Alignment](https://doi.org/10.1093/hesc/9780191991318.003.0009) | 2025 | Concepts in Bioinformatics and Genomics | paper | 0.25 | strong |
| 4 | paper | [Pairwise Semiregular Properties on Generalized Pairwise Lindelöf Spaces](https://doi.org/10.28924/2291-8639-21-2023-16) | 2023 | International Journal of Analysis and Ap | paper | 0.25 | strong |
| 5 | paper | [Plausible Pairwise Stability](https://doi.org/10.2139/ssrn.6445978) | 2026 |  | paper | 0.25 | strong |
| 6 | paper | [pairwise, adv. &amp; adj.](https://doi.org/10.1093/oed/5550390966) | 2023 | Oxford English Dictionary | paper | 0.25 | strong |
| 7 | paper | [A General Pairwise-Markov GLMB Filter](https://doi.org/10.31224/6873) | 2026 |  | paper | 0.25 | strong |
| 8 | paper | [Aggregating Pairwise Information Over Optimal Routes](https://doi.org/10.5220/0011981900003479) | 2023 | Proceedings of the 9th International Con | paper | 0.25 | strong |
| 9 | paper | [Locally pairwise paracompact spaces and locally nearly pairwise paracompact spac](https://doi.org/10.1063/5.0231773) | 2024 | AIP Conference Proceedings | paper | 0.25 | strong |
| 10 | paper | [Pairwise Markov Chains for Volatility Forecasting](https://doi.org/10.2139/ssrn.5248108) | 2025 |  | paper | 0.25 | strong |
| 11 | paper | [Pairwise Dissimilarity and Risk-Seeking Portfolio Construction](https://doi.org/10.2139/ssrn.6239578) | 2026 |  | paper | 0.25 | strong |
| 12 | paper | [pointwise, adv. &amp; adj.](https://doi.org/10.1093/oed/4614298818) | 2023 | Oxford English Dictionary | paper | 0.25 | strong |
| 13 | paper | [Pointwise convergence](https://doi.org/10.1017/9781009230063.018) | 2022 | Fourier Analysis | paper | 0.25 | strong |
| 14 | paper | [Pointwise hemislant submersions from cosymplectic manifolds](https://doi.org/10.3842/umzh.v77i8.8710) | 2026 | Ukrains’kyi Matematychnyi Zhurnal | paper | 0.25 | strong |
| 15 | paper | [Dataset Pointwise](https://doi.org/10.12795/11441/169465) | 2025 | Datasets de idUS | dataset | 0.25 | strong |
| 16 | paper | [Pointwise convergence, the answer](https://doi.org/10.1017/9781009230063.022) | 2022 | Fourier Analysis | paper | 0.25 | strong |
| 17 | paper | [From Pointwise to Two-Point Continuum](https://doi.org/10.2139/ssrn.6249079) | 2026 |  | paper | 0.25 | strong |
| 18 | paper | [Casorati curvatures of pointwise slant submanifolds in para-complex space forms](https://doi.org/10.3842/umzh.v77i9.8956) | 2026 | Ukrains’kyi Matematychnyi Zhurnal | paper | 0.25 | strong |
| 19 | paper | [Pointwise Completeness and Pointwise Degeneracy of Descriptor Linear Discrete-Ti](https://doi.org/10.2478/ama-2025-0035) | 2025 | Acta Mechanica et Automatica | tool | 0.25 | strong |
| 20 | paper | [Existence of Common Fixed Points for Pointwise Lipschitzian Semigroups](https://doi.org/10.1007/978-3-032-08869-7_2) | 2026 | SpringerBriefs in Mathematics | paper | 0.25 | strong |
| 21 | paper | [Revolutionary  Analysis of the  Pointwise Stationary Fluid Flow Approximation mo](https://doi.org/10.20944/preprints202402.1086.v1) | 2024 |  | empirical | 0.25 | strong |
| 22 | paper | [Analysis of the pointwise completeness and the pointwise degeneracy of the stand](https://doi.org/10.24136/jaeee.2023.001) | 2023 | Journal of Automation, Electronics and E | tool | 0.25 | strong |
| 23 | paper | [Crossroads between Stability and Randomness of the Non-stationaryQueue’s Pointwi](https://doi.org/10.20944/preprints202405.0544.v1) | 2024 |  | paper | 0.25 | strong |
| 24 | paper | [Convergence theorems and stability results of a two-step iteration scheme for po](https://doi.org/10.28919/afpt/7320) | 2022 | Advances in Fixed Point Theory | paper | 0.25 | strong |
| 25 | paper | [Pointwise quasi hemi-slant submanifolds](https://doi.org/10.22541/au.164873540.04096364/v1) | 2022 |  | paper | 0.25 | strong |
| 26 | paper | [Perturbation Catalogue: Democratising genetic perturbation data for research and](https://doi.org/10.6019/tol.perturbation-catalogue-w.2026.00001.1) | 2026 |  | database | 0.25 | strong |
| 27 | paper | [The Perturbation of O](https://doi.org/10.2307/jj.26844241.2) | 2025 | The Perturbation of O | paper | 0.25 | strong |
| 28 | paper | [Part II: Regular perturbation](https://doi.org/10.1137/1.9781611978865.pt2) | 2026 | Perturbation Methods Using Backward Erro | paper | 0.25 | strong |
| 29 | paper | [Asymptotic Perturbation Methods](https://doi.org/10.1002/9783527841745.fmatter) | 2022 | Asymptotic Perturbation Methods | paper | 0.25 | strong |
| 30 | paper | [The Asymptotic Perturbation Method for Rogue Waves](https://doi.org/10.1002/9783527841745.ch9) | 2022 | Asymptotic Perturbation Methods | paper | 0.25 | strong |
| 31 | paper | [The Asymptotic Perturbation Method for Physics Problems](https://doi.org/10.1002/9783527841745.ch7) | 2022 | Asymptotic Perturbation Methods | paper | 0.25 | strong |
| 32 | paper | [Perturbation](https://doi.org/10.5194/egusphere-2024-3560-ac3) | 2025 |  | paper | 0.25 | strong |
| 33 | paper | [The Asymptotic Perturbation Method for Nonlinear Oscillators](https://doi.org/10.1002/9783527841745.ch1) | 2022 | Asymptotic Perturbation Methods | paper | 0.25 | strong |
| 34 | paper | [The Asymptotic Perturbation Model for Elementary Particle Physics](https://doi.org/10.1002/9783527841745.ch8) | 2022 | Asymptotic Perturbation Methods | paper | 0.25 | strong |
| 35 | paper | [The Asymptotic Perturbation Method for Nonlinear Continuous Systems](https://doi.org/10.1002/9783527841745.ch5) | 2022 | Asymptotic Perturbation Methods | tool | 0.25 | strong |
| 36 | paper | [The Asymptotic Perturbation Method for Remarkable Nonlinear Systems](https://doi.org/10.1002/9783527841745.ch2) | 2022 | Asymptotic Perturbation Methods | tool | 0.25 | strong |
| 37 | paper | [The Asymptotic Perturbation Method for Fractal and Chaotic Solutions](https://doi.org/10.1002/9783527841745.ch10) | 2022 | Asymptotic Perturbation Methods | paper | 0.25 | strong |
| 38 | paper | [The Asymptotic Perturbation Method for Dispersive Nonlinear Partial Differential](https://doi.org/10.1002/9783527841745.ch6) | 2022 | Asymptotic Perturbation Methods | paper | 0.25 | strong |
| 39 | paper | [One Perturbation Fools All: an Adversarial Perturbation Can Attack Different Vis](https://doi.org/10.2139/ssrn.5573446) | 2025 |  | paper | 0.25 | strong |
| 40 | paper | [Ask a Strong LLM Judge when Your Reward Model is Uncertain](https://doi.org/10.48550/arXiv.2510.20369) | 2025 | arXiv.org | paper | 0.225 | strong |

### 1. Perturbation-adapted perturbation theory
- **Source**: paper  **URL**: https://doi.org/10.1063/5.0079853
- **Year/Venue**: 2022 / The Journal of Chemical Physics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Perturbation-adapted perturbation theory' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. Pointwise semi-slant Riemannian maps into almost Hermitian manifolds and Casorati inequalities
- **Source**: paper  **URL**: https://doi.org/10.3842/umzh.v76i9.7652
- **Year/Venue**: 2025 / Ukrains’kyi Matematychnyi Zhurnal
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pointwise semi-slant Riemannian maps into almost Hermitian manifolds and Casorati inequalities' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. Pairwise Sequence Alignment
- **Source**: paper  **URL**: https://doi.org/10.1093/hesc/9780191991318.003.0009
- **Year/Venue**: 2025 / Concepts in Bioinformatics and Genomics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pairwise Sequence Alignment' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. Pairwise Semiregular Properties on Generalized Pairwise Lindelöf Spaces
- **Source**: paper  **URL**: https://doi.org/10.28924/2291-8639-21-2023-16
- **Year/Venue**: 2023 / International Journal of Analysis and Applications
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pairwise Semiregular Properties on Generalized Pairwise Lindelöf Spaces' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. Plausible Pairwise Stability
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6445978
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Plausible Pairwise Stability' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. pairwise, adv. &amp; adj.
- **Source**: paper  **URL**: https://doi.org/10.1093/oed/5550390966
- **Year/Venue**: 2023 / Oxford English Dictionary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'pairwise, adv. &amp; adj.' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. A General Pairwise-Markov GLMB Filter
- **Source**: paper  **URL**: https://doi.org/10.31224/6873
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'A General Pairwise-Markov GLMB Filter' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Aggregating Pairwise Information Over Optimal Routes
- **Source**: paper  **URL**: https://doi.org/10.5220/0011981900003479
- **Year/Venue**: 2023 / Proceedings of the 9th International Conference on Vehicle Technology and Intelligent Transport Systems
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Aggregating Pairwise Information Over Optimal Routes' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. Locally pairwise paracompact spaces and locally nearly pairwise paracompact spaces
- **Source**: paper  **URL**: https://doi.org/10.1063/5.0231773
- **Year/Venue**: 2024 / AIP Conference Proceedings
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Locally pairwise paracompact spaces and locally nearly pairwise paracompact spaces' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Pairwise Markov Chains for Volatility Forecasting
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.5248108
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pairwise Markov Chains for Volatility Forecasting' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. Pairwise Dissimilarity and Risk-Seeking Portfolio Construction
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6239578
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pairwise Dissimilarity and Risk-Seeking Portfolio Construction' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pairwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. pointwise, adv. &amp; adj.
- **Source**: paper  **URL**: https://doi.org/10.1093/oed/4614298818
- **Year/Venue**: 2023 / Oxford English Dictionary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'pointwise, adv. &amp; adj.' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. Pointwise convergence
- **Source**: paper  **URL**: https://doi.org/10.1017/9781009230063.018
- **Year/Venue**: 2022 / Fourier Analysis
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pointwise convergence' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 14. Pointwise hemislant submersions from cosymplectic manifolds
- **Source**: paper  **URL**: https://doi.org/10.3842/umzh.v77i8.8710
- **Year/Venue**: 2026 / Ukrains’kyi Matematychnyi Zhurnal
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pointwise hemislant submersions from cosymplectic manifolds' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 15. Dataset Pointwise
- **Source**: paper  **URL**: https://doi.org/10.12795/11441/169465
- **Year/Venue**: 2025 / Datasets de idUS
- **Contribution type**: dataset
- **Why it overlaps**: Relevance 0.25: paper titled 'Dataset Pointwise' contributes a 'dataset' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 16. Pointwise convergence, the answer
- **Source**: paper  **URL**: https://doi.org/10.1017/9781009230063.022
- **Year/Venue**: 2022 / Fourier Analysis
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pointwise convergence, the answer' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 17. From Pointwise to Two-Point Continuum
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6249079
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'From Pointwise to Two-Point Continuum' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 18. Casorati curvatures of pointwise slant submanifolds in para-complex space forms
- **Source**: paper  **URL**: https://doi.org/10.3842/umzh.v77i9.8956
- **Year/Venue**: 2026 / Ukrains’kyi Matematychnyi Zhurnal
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Casorati curvatures of pointwise slant submanifolds in para-complex space forms' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 19. Pointwise Completeness and Pointwise Degeneracy of Descriptor Linear Discrete-Time Systems with Different Fractional Ord
- **Source**: paper  **URL**: https://doi.org/10.2478/ama-2025-0035
- **Year/Venue**: 2025 / Acta Mechanica et Automatica
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'Pointwise Completeness and Pointwise Degeneracy of Descriptor Linear Discrete-Time Systems with Diff' contributes a 'tool' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 20. Existence of Common Fixed Points for Pointwise Lipschitzian Semigroups
- **Source**: paper  **URL**: https://doi.org/10.1007/978-3-032-08869-7_2
- **Year/Venue**: 2026 / SpringerBriefs in Mathematics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Existence of Common Fixed Points for Pointwise Lipschitzian Semigroups' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 21. Revolutionary  Analysis of the  Pointwise Stationary Fluid Flow Approximation model of the  non-stationary  queue with P
- **Source**: paper  **URL**: https://doi.org/10.20944/preprints202402.1086.v1
- **Year/Venue**: 2024 / n/a
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'Revolutionary  Analysis of the  Pointwise Stationary Fluid Flow Approximation model of the  non-stat' contributes a 'empirical' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 22. Analysis of the pointwise completeness and the pointwise degeneracy of the standard and fractional descriptor linear sys
- **Source**: paper  **URL**: https://doi.org/10.24136/jaeee.2023.001
- **Year/Venue**: 2023 / Journal of Automation, Electronics and Electrical Engineering
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'Analysis of the pointwise completeness and the pointwise degeneracy of the standard and fractional d' contributes a 'tool' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 23. Crossroads between Stability and Randomness of the Non-stationaryQueue’s Pointwise Stationary Fluid Flow Approximation m
- **Source**: paper  **URL**: https://doi.org/10.20944/preprints202405.0544.v1
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Crossroads between Stability and Randomness of the Non-stationaryQueue’s Pointwise Stationary Fluid ' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 24. Convergence theorems and stability results of a two-step iteration scheme for pointwise asymptotically nonexpansive self
- **Source**: paper  **URL**: https://doi.org/10.28919/afpt/7320
- **Year/Venue**: 2022 / Advances in Fixed Point Theory
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Convergence theorems and stability results of a two-step iteration scheme for pointwise asymptotical' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 25. Pointwise quasi hemi-slant submanifolds
- **Source**: paper  **URL**: https://doi.org/10.22541/au.164873540.04096364/v1
- **Year/Venue**: 2022 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Pointwise quasi hemi-slant submanifolds' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:pointwise.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 26. Perturbation Catalogue: Democratising genetic perturbation data for research and drug discovery
- **Source**: paper  **URL**: https://doi.org/10.6019/tol.perturbation-catalogue-w.2026.00001.1
- **Year/Venue**: 2026 / n/a
- **Contribution type**: database
- **Why it overlaps**: Relevance 0.25: paper titled 'Perturbation Catalogue: Democratising genetic perturbation data for research and drug discovery' contributes a 'database' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 27. The Perturbation of O
- **Source**: paper  **URL**: https://doi.org/10.2307/jj.26844241.2
- **Year/Venue**: 2025 / The Perturbation of O
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Perturbation of O' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 28. Part II: Regular perturbation
- **Source**: paper  **URL**: https://doi.org/10.1137/1.9781611978865.pt2
- **Year/Venue**: 2026 / Perturbation Methods Using Backward Error
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Part II: Regular perturbation' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 29. Asymptotic Perturbation Methods
- **Source**: paper  **URL**: https://doi.org/10.1002/9783527841745.fmatter
- **Year/Venue**: 2022 / Asymptotic Perturbation Methods
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Asymptotic Perturbation Methods' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 30. The Asymptotic Perturbation Method for Rogue Waves
- **Source**: paper  **URL**: https://doi.org/10.1002/9783527841745.ch9
- **Year/Venue**: 2022 / Asymptotic Perturbation Methods
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Asymptotic Perturbation Method for Rogue Waves' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 31. The Asymptotic Perturbation Method for Physics Problems
- **Source**: paper  **URL**: https://doi.org/10.1002/9783527841745.ch7
- **Year/Venue**: 2022 / Asymptotic Perturbation Methods
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Asymptotic Perturbation Method for Physics Problems' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 32. Perturbation
- **Source**: paper  **URL**: https://doi.org/10.5194/egusphere-2024-3560-ac3
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Perturbation' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 33. The Asymptotic Perturbation Method for Nonlinear Oscillators
- **Source**: paper  **URL**: https://doi.org/10.1002/9783527841745.ch1
- **Year/Venue**: 2022 / Asymptotic Perturbation Methods
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Asymptotic Perturbation Method for Nonlinear Oscillators' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 34. The Asymptotic Perturbation Model for Elementary Particle Physics
- **Source**: paper  **URL**: https://doi.org/10.1002/9783527841745.ch8
- **Year/Venue**: 2022 / Asymptotic Perturbation Methods
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Asymptotic Perturbation Model for Elementary Particle Physics' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 35. The Asymptotic Perturbation Method for Nonlinear Continuous Systems
- **Source**: paper  **URL**: https://doi.org/10.1002/9783527841745.ch5
- **Year/Venue**: 2022 / Asymptotic Perturbation Methods
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'The Asymptotic Perturbation Method for Nonlinear Continuous Systems' contributes a 'tool' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 36. The Asymptotic Perturbation Method for Remarkable Nonlinear Systems
- **Source**: paper  **URL**: https://doi.org/10.1002/9783527841745.ch2
- **Year/Venue**: 2022 / Asymptotic Perturbation Methods
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'The Asymptotic Perturbation Method for Remarkable Nonlinear Systems' contributes a 'tool' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 37. The Asymptotic Perturbation Method for Fractal and Chaotic Solutions
- **Source**: paper  **URL**: https://doi.org/10.1002/9783527841745.ch10
- **Year/Venue**: 2022 / Asymptotic Perturbation Methods
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Asymptotic Perturbation Method for Fractal and Chaotic Solutions' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 38. The Asymptotic Perturbation Method for Dispersive Nonlinear Partial Differential Equations
- **Source**: paper  **URL**: https://doi.org/10.1002/9783527841745.ch6
- **Year/Venue**: 2022 / Asymptotic Perturbation Methods
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Asymptotic Perturbation Method for Dispersive Nonlinear Partial Differential Equations' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 39. One Perturbation Fools All: an Adversarial Perturbation Can Attack Different Vision Models
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.5573446
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'One Perturbation Fools All: an Adversarial Perturbation Can Attack Different Vision Models' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:perturbation.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 40. Ask a Strong LLM Judge when Your Reward Model is Uncertain
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.20369
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.23: paper titled 'Ask a Strong LLM Judge when Your Reward Model is Uncertain' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:abstract:pairwise|syn:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Pairwise vs pointwise judge agreement under perturbation'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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
