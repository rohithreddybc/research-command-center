# Existing Work Report — B14: Refusal behavior consistency across LLM updates

> ⛔ **GO BLOCKED (peer-reviewed overlap)** — 1 peer-reviewed DIRECT overlap(s); paper_diff_strength=`moderate`. Must articulate a clear differentiator before proceeding.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 1 |
| Paper diff strength | `moderate` |
| GitHub direct artifacts | 0 |
| HuggingFace direct artifacts | 14 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 14 |
| Artifact diff strength | `weak` |
| Partial overlaps (total) | 27 |
| Adjacent | 23 |
| Total findings | 65 |
| peer_reviewed_direct | ✅ Yes |
| high_artifact_overlap | ⚠️ Yes |
| GO blocked | **YES** |
| Differentiator required | Yes |
| Artifact differentiator required | Yes |

## Peer-Reviewed Direct Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs](http://arxiv.org/abs/2605.01913v1) | 2026 | arXiv | paper | 0.75 | moderate |

### 1. RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.01913v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.75: paper titled 'RefusalGuard: Geometry-Preserving Fine-Tuning for Safety in LLMs' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal|kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Artifact Direct Overlaps (GitHub / HF / PWC)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | huggingface | [mrfakename/refusal](https://huggingface.co/datasets/mrfakename/refusal) |  | HuggingFace | dataset | 107 | weak |
| 2 | huggingface | [mrfakename/refusal-xl](https://huggingface.co/datasets/mrfakename/refusal-xl) |  | HuggingFace | dataset | 159 | weak |
| 3 | huggingface | [sruly/asimov_refusals](https://huggingface.co/datasets/sruly/asimov_refusals) |  | HuggingFace | dataset | 705 | weak |
| 4 | huggingface | [PJMixers/mrfakename_refusal-xl-SlopOnly-KTOSloPreferenceShareGPT](https://huggingface.co/datasets/PJMixers/mrfakename_refusal-xl-SlopOnly-KTOSloPreferenceShareGPT) |  | HuggingFace | dataset | 196 | weak |
| 5 | huggingface | [anthracite-org/kalo-opus-instruct-22k-no-refusal](https://huggingface.co/datasets/anthracite-org/kalo-opus-instruct-22k-no-refusal) |  | HuggingFace | dataset | 503 | weak |
| 6 | huggingface | [AIM-Intelligence/XL-SafetyBench](https://huggingface.co/datasets/AIM-Intelligence/XL-SafetyBench) |  | HuggingFace | dataset | 479 | weak |
| 7 | huggingface | [nvidia/Aegis-AI-Content-Safety-Dataset-2.0](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) |  | HuggingFace | dataset | 6646 | weak |
| 8 | huggingface | [keremberke/construction-safety-object-detection](https://huggingface.co/datasets/keremberke/construction-safety-object-detection) |  | HuggingFace | dataset | 506 | weak |
| 9 | huggingface | [ai-safety-institute/AgentHarm](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) |  | HuggingFace | dataset | 4703 | weak |
| 10 | huggingface | [Francesco/construction-safety-gsnvb](https://huggingface.co/datasets/Francesco/construction-safety-gsnvb) |  | HuggingFace | dataset | 126 | weak |
| 11 | huggingface | [thu-coai/Safety-Prompts](https://huggingface.co/datasets/thu-coai/Safety-Prompts) |  | HuggingFace | dataset | 312 | weak |
| 12 | huggingface | [thu-coai/SafetyBench](https://huggingface.co/datasets/thu-coai/SafetyBench) |  | HuggingFace | dataset | 837 | weak |
| 13 | huggingface | [LLM-Tuning-Safety/HEx-PHI](https://huggingface.co/datasets/LLM-Tuning-Safety/HEx-PHI) |  | HuggingFace | dataset | 661 | weak |
| 14 | huggingface | [MelioAI/safety-qa-sample](https://huggingface.co/datasets/MelioAI/safety-qa-sample) |  | HuggingFace | dataset | 17958 | weak |

### 1. mrfakename/refusal
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/mrfakename/refusal
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'mrfakename/refusal' (107 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 2. mrfakename/refusal-xl
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/mrfakename/refusal-xl
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'mrfakename/refusal-xl' (159 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 3. sruly/asimov_refusals
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/sruly/asimov_refusals
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'sruly/asimov_refusals' (705 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 4. PJMixers/mrfakename_refusal-xl-SlopOnly-KTOSloPreferenceShareGPT
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/PJMixers/mrfakename_refusal-xl-SlopOnly-KTOSloPreferenceShareGPT
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'PJMixers/mrfakename_refusal-xl-SlopOnly-KTOSloPreferenceShareGPT' (196 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 5. anthracite-org/kalo-opus-instruct-22k-no-refusal
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/anthracite-org/kalo-opus-instruct-22k-no-refusal
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'anthracite-org/kalo-opus-instruct-22k-no-refusal' (503 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 6. AIM-Intelligence/XL-SafetyBench
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/AIM-Intelligence/XL-SafetyBench
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'AIM-Intelligence/XL-SafetyBench' (479 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 7. nvidia/Aegis-AI-Content-Safety-Dataset-2.0
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'nvidia/Aegis-AI-Content-Safety-Dataset-2.0' (6,646 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 8. keremberke/construction-safety-object-detection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/keremberke/construction-safety-object-detection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'keremberke/construction-safety-object-detection' (506 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 9. ai-safety-institute/AgentHarm
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/ai-safety-institute/AgentHarm
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'ai-safety-institute/AgentHarm' (4,703 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 10. Francesco/construction-safety-gsnvb
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Francesco/construction-safety-gsnvb
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Francesco/construction-safety-gsnvb' (126 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 11. thu-coai/Safety-Prompts
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/thu-coai/Safety-Prompts
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'thu-coai/Safety-Prompts' (312 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 12. thu-coai/SafetyBench
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/thu-coai/SafetyBench
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'thu-coai/SafetyBench' (837 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 13. LLM-Tuning-Safety/HEx-PHI
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/LLM-Tuning-Safety/HEx-PHI
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'LLM-Tuning-Safety/HEx-PHI' (661 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 14. MelioAI/safety-qa-sample
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/MelioAI/safety-qa-sample
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'MelioAI/safety-qa-sample' (17,958 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [On Becoming a Refusal Politician](https://doi.org/10.5040/9798216183525.ch-006) | 2023 | Black Women at Work | paper | 0.5 | weak |
| 2 | paper | [Indonesian EFL Learners' Refusal: Refusal-Speech Act Specific Motivation on Refu](https://doi.org/10.21462/ijefl.v9i1.763) | 2024 | Indonesian Journal of EFL and Linguistic | paper | 0.5 | weak |
| 3 | paper | [Slow Reading as Refusal](https://doi.org/10.4324/9781003367314-15) | 2023 | Working with Theories of Refusal and Dec | paper | 0.5 | weak |
| 4 | paper | [Indigenous Refusal and Rejecting Genocide](https://doi.org/10.14321/jj.31361464.4) | 2025 | Indigenous Activism in the Midwest | paper | 0.5 | weak |
| 5 | paper | [4 Ethnographic Recognition and Refusal](https://doi.org/10.3138/9781487560034-008) | 2025 | Raising Spirit in Blackfoot Territory | paper | 0.5 | weak |
| 6 | paper | [The Affective Dimensions of Refusal in Higher Education Decolonization](https://doi.org/10.4324/9781003367314-4) | 2023 | Working with Theories of Refusal and Dec | paper | 0.5 | weak |
| 7 | paper | [Nihilism and the Refusal of Refusal in Wright and Fanon](https://doi.org/10.2307/jj.36587892.7) | 2026 | At the Margins of Nihilism | paper | 0.5 | weak |
| 8 | paper | [refusal, n.](https://doi.org/10.1093/oed/1170104172) | 2023 | Oxford English Dictionary | paper | 0.5 | weak |
| 9 | paper | [3. Breaking Billboards: Protest and the Politics of Refusal](https://doi.org/10.1515/9781531514105-005) | 2026 | Inappropriable Force | paper | 0.5 | weak |
| 10 | paper | [3 Nihilism and the Refusal of Refusal in Wright and Fanon](https://doi.org/10.1515/9781531512392-005) | 2026 | At the Margins of Nihilism | paper | 0.5 | weak |
| 11 | paper | [SafeHarbor: Hierarchical Memory-Augmented Guardrail for LLM Agent Safety](http://arxiv.org/abs/2605.05704v1) | 2026 | arXiv | paper | 0.438 | weak |
| 12 | paper | [XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and C](http://arxiv.org/abs/2605.05662v1) | 2026 | arXiv | benchmark | 0.438 | weak |
| 13 | paper | [The Geopolitics of AI Safety: A Causal Analysis of Regional LLM Bias](http://arxiv.org/abs/2605.05427v1) | 2026 | arXiv | empirical | 0.438 | weak |
| 14 | paper | [Self-Mined Hardness for Safety Fine-Tuning](http://arxiv.org/abs/2605.03226v1) | 2026 | arXiv | paper | 0.438 | weak |
| 15 | paper | [Alignment Drift in Multimodal LLMs: A Two-Phase, Longitudinal Evaluation of Harm](https://doi.org/10.48550/arXiv.2602.04739) | 2026 | arXiv.org | paper | 0.412 | weak |
| 16 | huggingface | [yaopaul/contextual_refusal_dataset](https://huggingface.co/datasets/yaopaul/contextual_refusal_dataset) |  | HuggingFace | dataset | 58 | weak |
| 17 | huggingface | [justinphan3110/wildchat_over_refusal](https://huggingface.co/datasets/justinphan3110/wildchat_over_refusal) |  | HuggingFace | dataset | 71 | weak |
| 18 | huggingface | [NewEden-Forge/Kalo-Opus-Instruct-22k-Refusal-Murdered](https://huggingface.co/datasets/NewEden-Forge/Kalo-Opus-Instruct-22k-Refusal-Murdered) |  | HuggingFace | dataset | 40 | weak |
| 19 | huggingface | [scarysnake/code-refusal-for-abliteration](https://huggingface.co/datasets/scarysnake/code-refusal-for-abliteration) |  | HuggingFace | dataset | 56 | weak |
| 20 | huggingface | [TeeZee/chat-alpaca-pl-no-refusals](https://huggingface.co/datasets/TeeZee/chat-alpaca-pl-no-refusals) |  | HuggingFace | dataset | 24 | weak |
| 21 | huggingface | [byroneverson/abliterate-refusal](https://huggingface.co/datasets/byroneverson/abliterate-refusal) |  | HuggingFace | dataset | 77 | weak |
| 22 | huggingface | [anthracite-org/kalo-opus-instruct-22k-no-refusal-no-system](https://huggingface.co/datasets/anthracite-org/kalo-opus-instruct-22k-no-refusal-no-system) |  | HuggingFace | dataset | 49 | weak |
| 23 | huggingface | [qualifire/safety-benchmark](https://huggingface.co/datasets/qualifire/safety-benchmark) |  | HuggingFace | dataset | 97 | weak |
| 24 | huggingface | [Diginyx/SafetyALFRED](https://huggingface.co/datasets/Diginyx/SafetyALFRED) |  | HuggingFace | dataset | 59 | weak |
| 25 | huggingface | [mark-matviiv/ukrainian-safety-dataset](https://huggingface.co/datasets/mark-matviiv/ukrainian-safety-dataset) |  | HuggingFace | dataset | 21 | weak |
| 26 | huggingface | [Nexdata/Non-safety_and_inductive_Prompt_data](https://huggingface.co/datasets/Nexdata/Non-safety_and_inductive_Prompt_data) |  | HuggingFace | dataset | 30 | weak |
| 27 | huggingface | [PahaII/vllm_safety_evaluation](https://huggingface.co/datasets/PahaII/vllm_safety_evaluation) |  | HuggingFace | dataset | 75 | weak |

### 1. On Becoming a Refusal Politician
- **Source**: paper  **URL**: https://doi.org/10.5040/9798216183525.ch-006
- **Year/Venue**: 2023 / Black Women at Work
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'On Becoming a Refusal Politician' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 2. Indonesian EFL Learners' Refusal: Refusal-Speech Act Specific Motivation on Refusal Realization
- **Source**: paper  **URL**: https://doi.org/10.21462/ijefl.v9i1.763
- **Year/Venue**: 2024 / Indonesian Journal of EFL and Linguistics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Indonesian EFL Learners' Refusal: Refusal-Speech Act Specific Motivation on Refusal Realization' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 3. Slow Reading as Refusal
- **Source**: paper  **URL**: https://doi.org/10.4324/9781003367314-15
- **Year/Venue**: 2023 / Working with Theories of Refusal and Decolonization in Higher Education
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Slow Reading as Refusal' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 4. Indigenous Refusal and Rejecting Genocide
- **Source**: paper  **URL**: https://doi.org/10.14321/jj.31361464.4
- **Year/Venue**: 2025 / Indigenous Activism in the Midwest
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Indigenous Refusal and Rejecting Genocide' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 5. 4 Ethnographic Recognition and Refusal
- **Source**: paper  **URL**: https://doi.org/10.3138/9781487560034-008
- **Year/Venue**: 2025 / Raising Spirit in Blackfoot Territory
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled '4 Ethnographic Recognition and Refusal' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 6. The Affective Dimensions of Refusal in Higher Education Decolonization
- **Source**: paper  **URL**: https://doi.org/10.4324/9781003367314-4
- **Year/Venue**: 2023 / Working with Theories of Refusal and Decolonization in Higher Education
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'The Affective Dimensions of Refusal in Higher Education Decolonization' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 7. Nihilism and the Refusal of Refusal in Wright and Fanon
- **Source**: paper  **URL**: https://doi.org/10.2307/jj.36587892.7
- **Year/Venue**: 2026 / At the Margins of Nihilism
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Nihilism and the Refusal of Refusal in Wright and Fanon' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 8. refusal, n.
- **Source**: paper  **URL**: https://doi.org/10.1093/oed/1170104172
- **Year/Venue**: 2023 / Oxford English Dictionary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'refusal, n.' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 9. 3. Breaking Billboards: Protest and the Politics of Refusal
- **Source**: paper  **URL**: https://doi.org/10.1515/9781531514105-005
- **Year/Venue**: 2026 / Inappropriable Force
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled '3. Breaking Billboards: Protest and the Politics of Refusal' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 10. 3 Nihilism and the Refusal of Refusal in Wright and Fanon
- **Source**: paper  **URL**: https://doi.org/10.1515/9781531512392-005
- **Year/Venue**: 2026 / At the Margins of Nihilism
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled '3 Nihilism and the Refusal of Refusal in Wright and Fanon' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:title:refusal.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 11. SafeHarbor: Hierarchical Memory-Augmented Guardrail for LLM Agent Safety
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.05704v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.44: paper titled 'SafeHarbor: Hierarchical Memory-Augmented Guardrail for LLM Agent Safety' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 12. XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and Cultural Sensitivity
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.05662v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.44: paper titled 'XL-SafetyBench: A Country-Grounded Cross-Cultural Benchmark for LLM Safety and Cultural Sensitivity' contributes a 'benchmark' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 13. The Geopolitics of AI Safety: A Causal Analysis of Regional LLM Bias
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.05427v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.44: paper titled 'The Geopolitics of AI Safety: A Causal Analysis of Regional LLM Bias' contributes a 'empirical' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 14. Self-Mined Hardness for Safety Fine-Tuning
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.03226v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.44: paper titled 'Self-Mined Hardness for Safety Fine-Tuning' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 15. Alignment Drift in Multimodal LLMs: A Two-Phase, Longitudinal Evaluation of Harm Across Eight Model Releases
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2602.04739
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.41: paper titled 'Alignment Drift in Multimodal LLMs: A Two-Phase, Longitudinal Evaluation of Harm Across Eight Model ' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:abstract:safety|syn:title:alignment drift.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 16. yaopaul/contextual_refusal_dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/yaopaul/contextual_refusal_dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'yaopaul/contextual_refusal_dataset' (58 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 17. justinphan3110/wildchat_over_refusal
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/justinphan3110/wildchat_over_refusal
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'justinphan3110/wildchat_over_refusal' (71 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 18. NewEden-Forge/Kalo-Opus-Instruct-22k-Refusal-Murdered
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/NewEden-Forge/Kalo-Opus-Instruct-22k-Refusal-Murdered
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'NewEden-Forge/Kalo-Opus-Instruct-22k-Refusal-Murdered' (40 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 19. scarysnake/code-refusal-for-abliteration
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/scarysnake/code-refusal-for-abliteration
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'scarysnake/code-refusal-for-abliteration' (56 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 20. TeeZee/chat-alpaca-pl-no-refusals
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/TeeZee/chat-alpaca-pl-no-refusals
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'TeeZee/chat-alpaca-pl-no-refusals' (24 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 21. byroneverson/abliterate-refusal
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/byroneverson/abliterate-refusal
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'byroneverson/abliterate-refusal' (77 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 22. anthracite-org/kalo-opus-instruct-22k-no-refusal-no-system
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/anthracite-org/kalo-opus-instruct-22k-no-refusal-no-system
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'anthracite-org/kalo-opus-instruct-22k-no-refusal-no-system' (49 downloads) matched 'refusal' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 23. qualifire/safety-benchmark
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/qualifire/safety-benchmark
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'qualifire/safety-benchmark' (97 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 24. Diginyx/SafetyALFRED
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Diginyx/SafetyALFRED
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Diginyx/SafetyALFRED' (59 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 25. mark-matviiv/ukrainian-safety-dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/mark-matviiv/ukrainian-safety-dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'mark-matviiv/ukrainian-safety-dataset' (21 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 26. Nexdata/Non-safety_and_inductive_Prompt_data
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Nexdata/Non-safety_and_inductive_Prompt_data
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Nexdata/Non-safety_and_inductive_Prompt_data' (30 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 27. PahaII/vllm_safety_evaluation
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/PahaII/vllm_safety_evaluation
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'PahaII/vllm_safety_evaluation' (75 downloads) matched 'safety' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [TRACEALIGN - Tracing the Drift: Attributing Alignment Failures to Training-Time ](https://doi.org/10.48550/arXiv.2508.02063) | 2025 | arXiv.org | paper | 0.337 | strong |
| 2 | paper | [Measuring Evaluation-Context Divergence in Open-Weight LLMs: A Paired-Prompt Pro](http://arxiv.org/abs/2605.06327v1) | 2026 | arXiv | paper | 0.287 | strong |
| 3 | paper | [Beyond Fixed Benchmarks and Worst-Case Attacks: Dynamic Boundary Evaluation for ](http://arxiv.org/abs/2605.06213v1) | 2026 | arXiv | benchmark | 0.287 | strong |
| 4 | paper | [One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Mul](http://arxiv.org/abs/2605.05630v1) | 2026 | arXiv | paper | 0.287 | strong |
| 5 | paper | [MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents](http://arxiv.org/abs/2605.03952v1) | 2026 | arXiv | paper | 0.287 | strong |
| 6 | paper | [A Validated Prompt Bank for Malicious Code Generation: Separating Executable Wea](http://arxiv.org/abs/2605.03179v1) | 2026 | arXiv | paper | 0.287 | strong |
| 7 | paper | [An Integrated Framework for Implementing Safety-I and Safety-II Principles in Av](https://doi.org/10.3390/safety11020056) | 2025 | Safety | tool | 0.25 | strong |
| 8 | paper | [Intergrating Safety Leadership, Safety Culture and Safety Behavior :Insight from](https://doi.org/10.21070/ups.8870) | 2025 |  | paper | 0.25 | strong |
| 9 | paper | [Acknowledgment to Reviewers of Safety in 2021](https://doi.org/10.3390/safety8010010) | 2022 | Safety | survey | 0.25 | strong |
| 10 | paper | [Safety Future Initiative](https://doi.org/10.65391/r3287) | 2022 | Safety-Critical Systems Newsletter | paper | 0.25 | strong |
| 11 | paper | [AI Safety](https://doi.org/10.65391/r3192) | 2024 | Safety-Critical Systems Newsletter | paper | 0.25 | strong |
| 12 | paper | [Safety Futures Initiative Update](https://doi.org/10.65391/r3183) | 2022 | Safety-Critical Systems Newsletter | paper | 0.25 | strong |
| 13 | paper | [Acknowledgment to the Reviewers of Safety in 2022](https://doi.org/10.3390/safety9010004) | 2023 | Safety | survey | 0.25 | strong |
| 14 | paper | [Brexit and Software Safety](https://doi.org/10.65391/r3244) | 2022 | Safety-Critical Systems Newsletter | paper | 0.25 | strong |
| 15 | paper | [Building Safety Post Grenfell](https://doi.org/10.65391/r3191) | 2024 | Safety-Critical Systems Newsletter | paper | 0.25 | strong |
| 16 | paper | [Avoiding Safety and Cybersecurity Risks](https://doi.org/10.65391/r3279) | 2023 | Safety-Critical Systems Newsletter | paper | 0.25 | strong |
| 17 | paper | [On-Board Safety Monitoring for Drones](https://doi.org/10.65391/r3122) | 2025 | Safety-Critical Systems Newsletter | paper | 0.25 | strong |
| 18 | paper | [Analysis of differences among safety climate, safety knowledge, safety attitude,](https://doi.org/10.52902/kjsc.2024.35.137) | 2024 | Forum of Public Safety and Culture | empirical | 0.25 | strong |
| 19 | paper | [Safety Futures Initiative Introducing … Laure Buysse](https://doi.org/10.65391/r3282) | 2023 | Safety-Critical Systems Newsletter | paper | 0.25 | strong |
| 20 | paper | [Data Safety Analysis using RADISH](https://doi.org/10.65391/r3278) | 2023 | Safety-Critical Systems Newsletter | empirical | 0.25 | strong |
| 21 | paper | [Safety and Highly Automated Machinery](https://doi.org/10.65391/r3124) | 2025 | Safety-Critical Systems Newsletter | paper | 0.25 | strong |
| 22 | paper | [SORT-AI: A Projection-Based Structural Framework for AI Safety Alignment Stabili](https://doi.org/10.2139/ssrn.6095046) | 2026 |  | tool | 0.25 | strong |
| 23 | paper | [Alignment Drift as a Security Threat: Detecting and Mitigating Misaligned AI Beh](https://doi.org/10.38124/ijisrt/25dec1365) | 2025 | International Journal of Innovative Scie | tool | 0.225 | strong |

### 1. TRACEALIGN - Tracing the Drift: Attributing Alignment Failures to Training-Time Belief Sources in LLMs
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2508.02063
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.34: paper titled 'TRACEALIGN - Tracing the Drift: Attributing Alignment Failures to Training-Time Belief Sources in LL' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:abstract:safety|syn:abstract:alignment drift.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. Measuring Evaluation-Context Divergence in Open-Weight LLMs: A Paired-Prompt Protocol with Pilot Evidence of Alignment-P
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06327v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.29: paper titled 'Measuring Evaluation-Context Divergence in Open-Weight LLMs: A Paired-Prompt Protocol with Pilot Evi' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:abstract:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. Beyond Fixed Benchmarks and Worst-Case Attacks: Dynamic Boundary Evaluation for Language Models
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06213v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.29: paper titled 'Beyond Fixed Benchmarks and Worst-Case Attacks: Dynamic Boundary Evaluation for Language Models' contributes a 'benchmark' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:abstract:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.05630v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.29: paper titled 'One Turn Too Late: Response-Aware Defense Against Hidden Malicious Intent in Multi-Turn Dialogue' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:abstract:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.03952v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.29: paper titled 'MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:abstract:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. A Validated Prompt Bank for Malicious Code Generation: Separating Executable Weapons from Security Knowledge in 1,554 Co
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.03179v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.29: paper titled 'A Validated Prompt Bank for Malicious Code Generation: Separating Executable Weapons from Security K' contributes a 'paper' matching target artifact 'paper'. Matched keywords: primary:abstract:refusal|kw:abstract:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. An Integrated Framework for Implementing Safety-I and Safety-II Principles in Aviation Safety Management
- **Source**: paper  **URL**: https://doi.org/10.3390/safety11020056
- **Year/Venue**: 2025 / Safety
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'An Integrated Framework for Implementing Safety-I and Safety-II Principles in Aviation Safety Manage' contributes a 'tool' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Intergrating Safety Leadership, Safety Culture and Safety Behavior :Insight from the Manufacturing Industry
- **Source**: paper  **URL**: https://doi.org/10.21070/ups.8870
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Intergrating Safety Leadership, Safety Culture and Safety Behavior :Insight from the Manufacturing I' contributes a 'paper' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. Acknowledgment to Reviewers of Safety in 2021
- **Source**: paper  **URL**: https://doi.org/10.3390/safety8010010
- **Year/Venue**: 2022 / Safety
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.25: paper titled 'Acknowledgment to Reviewers of Safety in 2021' contributes a 'survey' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Safety Future Initiative
- **Source**: paper  **URL**: https://doi.org/10.65391/r3287
- **Year/Venue**: 2022 / Safety-Critical Systems Newsletter
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Safety Future Initiative' contributes a 'paper' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. AI Safety
- **Source**: paper  **URL**: https://doi.org/10.65391/r3192
- **Year/Venue**: 2024 / Safety-Critical Systems Newsletter
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'AI Safety' contributes a 'paper' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. Safety Futures Initiative Update
- **Source**: paper  **URL**: https://doi.org/10.65391/r3183
- **Year/Venue**: 2022 / Safety-Critical Systems Newsletter
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Safety Futures Initiative Update' contributes a 'paper' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. Acknowledgment to the Reviewers of Safety in 2022
- **Source**: paper  **URL**: https://doi.org/10.3390/safety9010004
- **Year/Venue**: 2023 / Safety
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.25: paper titled 'Acknowledgment to the Reviewers of Safety in 2022' contributes a 'survey' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 14. Brexit and Software Safety
- **Source**: paper  **URL**: https://doi.org/10.65391/r3244
- **Year/Venue**: 2022 / Safety-Critical Systems Newsletter
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Brexit and Software Safety' contributes a 'paper' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 15. Building Safety Post Grenfell
- **Source**: paper  **URL**: https://doi.org/10.65391/r3191
- **Year/Venue**: 2024 / Safety-Critical Systems Newsletter
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Building Safety Post Grenfell' contributes a 'paper' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 16. Avoiding Safety and Cybersecurity Risks
- **Source**: paper  **URL**: https://doi.org/10.65391/r3279
- **Year/Venue**: 2023 / Safety-Critical Systems Newsletter
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Avoiding Safety and Cybersecurity Risks' contributes a 'paper' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 17. On-Board Safety Monitoring for Drones
- **Source**: paper  **URL**: https://doi.org/10.65391/r3122
- **Year/Venue**: 2025 / Safety-Critical Systems Newsletter
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'On-Board Safety Monitoring for Drones' contributes a 'paper' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 18. Analysis of differences among safety climate, safety knowledge, safety attitude, safety motivation, and safety behavior 
- **Source**: paper  **URL**: https://doi.org/10.52902/kjsc.2024.35.137
- **Year/Venue**: 2024 / Forum of Public Safety and Culture
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'Analysis of differences among safety climate, safety knowledge, safety attitude, safety motivation, ' contributes a 'empirical' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 19. Safety Futures Initiative Introducing … Laure Buysse
- **Source**: paper  **URL**: https://doi.org/10.65391/r3282
- **Year/Venue**: 2023 / Safety-Critical Systems Newsletter
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Safety Futures Initiative Introducing … Laure Buysse' contributes a 'paper' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 20. Data Safety Analysis using RADISH
- **Source**: paper  **URL**: https://doi.org/10.65391/r3278
- **Year/Venue**: 2023 / Safety-Critical Systems Newsletter
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'Data Safety Analysis using RADISH' contributes a 'empirical' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 21. Safety and Highly Automated Machinery
- **Source**: paper  **URL**: https://doi.org/10.65391/r3124
- **Year/Venue**: 2025 / Safety-Critical Systems Newsletter
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Safety and Highly Automated Machinery' contributes a 'paper' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 22. SORT-AI: A Projection-Based Structural Framework for AI Safety Alignment Stability, Drift Detection, and Scalable Oversi
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6095046
- **Year/Venue**: 2026 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'SORT-AI: A Projection-Based Structural Framework for AI Safety Alignment Stability, Drift Detection,' contributes a 'tool' matching target artifact 'paper'. Matched keywords: kw:title:safety.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 23. Alignment Drift as a Security Threat: Detecting and Mitigating Misaligned AI Behavior in Regulated Systems
- **Source**: paper  **URL**: https://doi.org/10.38124/ijisrt/25dec1365
- **Year/Venue**: 2025 / International Journal of Innovative Science and Research Technology
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.23: paper titled 'Alignment Drift as a Security Threat: Detecting and Mitigating Misaligned AI Behavior in Regulated S' contributes a 'tool' matching target artifact 'paper'. Matched keywords: kw:abstract:safety|syn:title:alignment drift.
- **How we differ**: Our proposed work focuses specifically on 'Refusal behavior consistency across LLM updates'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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

1. **Do not promote B14 to GO** — 1 peer-reviewed paper(s) directly cover this.
2. For each DIRECT paper, fill 'how_we_differ' in the CSV with a specific contribution claim.
3. If no differentiator: consider DROP or further narrowing.
