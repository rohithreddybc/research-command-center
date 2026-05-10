# Existing Work Report — T25: Hallucination taxonomy: RAG vs no-RAG

> ⚠️ **DIFFERENTIATOR REQUIRED** — paper_direct=1, artifact_direct=2; paper_strength=`moderate`, artifact_strength=`weak`.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 1 |
| Paper diff strength | `moderate` |
| GitHub direct artifacts | 2 |
| HuggingFace direct artifacts | 0 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 2 |
| Artifact diff strength | `weak` |
| Partial overlaps (total) | 16 |
| Adjacent | 16 |
| Total findings | 35 |
| peer_reviewed_direct | ✅ Yes |
| high_artifact_overlap | No |
| GO blocked | No |
| Differentiator required | Yes |
| Artifact differentiator required | Yes |

## Peer-Reviewed Direct Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Correctness is not Faithfulness in Retrieval Augmented Generation Attributions](https://doi.org/10.1145/3731120.3744592) | 2025 | International Conference on the Theory o | paper | 0.75 | moderate |

### 1. Correctness is not Faithfulness in Retrieval Augmented Generation Attributions
- **Source**: paper  **URL**: https://doi.org/10.1145/3731120.3744592
- **Year/Venue**: 2025 / International Conference on the Theory of Information Retrieval
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.75: paper titled 'Correctness is not Faithfulness in Retrieval Augmented Generation Attributions' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: primary:title:retrieval augmented generation|kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Artifact Direct Overlaps (GitHub / HF / PWC)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | github | [Alibaba-NLP/OmniSearch](https://github.com/Alibaba-NLP/OmniSearch) |  | GitHub | benchmark | 423 | weak |
| 2 | github | [Denis2054/RAG-Driven-Generative-AI](https://github.com/Denis2054/RAG-Driven-Generative-AI) |  | GitHub | tool | 601 | weak |

### 1. Alibaba-NLP/OmniSearch
- **Source**: github  **URL**: https://github.com/Alibaba-NLP/OmniSearch
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'Alibaba-NLP/OmniSearch' (423 stars) provides an implementation of 'retrieval augmented generation'. Description: repo for benchmarking multimodal retrieval augmented generation with dynamic vqa dataset and self-adaptive planning agen.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 2. Denis2054/RAG-Driven-Generative-AI
- **Source**: github  **URL**: https://github.com/Denis2054/RAG-Driven-Generative-AI
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'Denis2054/RAG-Driven-Generative-AI' (601 stars) provides an implementation of 'retrieval augmented generation'. Description: this repository provides programs to build retrieval augmented generation (rag) code for generative ai with llamaindex, .
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document ](https://doi.org/10.18653/v1/2025.emnlp-main.710) | 2025 | Conference on Empirical Methods in Natur | tool | 0.5 | weak |
| 2 | paper | [Visual-RAG: Benchmarking Text-to-Image Retrieval Augmented Generation for Visual](https://doi.org/10.48550/arXiv.2502.16636) | 2025 | arXiv.org | benchmark | 0.5 | weak |
| 3 | paper | [Prospects of Retrieval Augmented Generation (RAG) for Academic Library Search an](https://doi.org/10.2139/ssrn.5295044) | 2025 |  | tool | 0.5 | weak |
| 4 | paper | [Retrieval Augmented Generation (RAG) Model](https://doi.org/10.55248/gengpi.6.0125.0635) | 2025 | International Journal of Research Public | paper | 0.5 | weak |
| 5 | paper | [Retrieval Augmented Generation for HPC Code Optimization](https://doi.org/10.31274/cc-20260223-58) | 2025 |  | paper | 0.5 | weak |
| 6 | paper | [Understanding Retrieval Pitfalls: Challenges Faced by Retrieval Augmented Genera](https://doi.org/10.59350/xcq3s-jvk04) | 2024 |  | benchmark | 0.5 | weak |
| 7 | paper | [Protótipo de Pesquisa Documental para a Polícia Militar do Paraná com Retrieval ](https://doi.org/10.51473/rcmos.v1i2.2024.736) | 2024 | RCMOS - Revista Científica Multidiscipli | paper | 0.5 | weak |
| 8 | paper | [Comparative Performance of Retrieval Augmented Generation Tourism Chatbots](https://doi.org/10.21070/ijins.v27i1.1836) | 2026 | Indonesian Journal of Innovation Studies | paper | 0.5 | weak |
| 9 | github | [qinchuanhui/UDA-Benchmark](https://github.com/qinchuanhui/UDA-Benchmark) |  | GitHub | tool | 43 | weak |
| 10 | github | [TonicAI/tonic_validate](https://github.com/TonicAI/tonic_validate) |  | GitHub | tool | 325 | weak |
| 11 | github | [neulab/ragged](https://github.com/neulab/ragged) |  | GitHub | tool | 61 | weak |
| 12 | huggingface | [mtc/cleaned_xsum-faith-test-set-with-faithfulness-annotation](https://huggingface.co/datasets/mtc/cleaned_xsum-faith-test-set-with-faithfulness-annotation) |  | HuggingFace | dataset | 23 | weak |
| 13 | huggingface | [mtc/faithfulness_benchmark_sanity_check_factcc](https://huggingface.co/datasets/mtc/faithfulness_benchmark_sanity_check_factcc) |  | HuggingFace | dataset | 40 | weak |
| 14 | huggingface | [mtc/faithfulness_benchmark_sanity_check_xsum_faith](https://huggingface.co/datasets/mtc/faithfulness_benchmark_sanity_check_xsum_faith) |  | HuggingFace | dataset | 34 | weak |
| 15 | huggingface | [mtc/absinth_german_faithfulness_detection_dataset](https://huggingface.co/datasets/mtc/absinth_german_faithfulness_detection_dataset) |  | HuggingFace | dataset | 43 | weak |
| 16 | huggingface | [mtc/span_absinth_german_faithfulness_detection_dataset](https://huggingface.co/datasets/mtc/span_absinth_german_faithfulness_detection_dataset) |  | HuggingFace | dataset | 26 | weak |

### 1. TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document Reasoning
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2025.emnlp-main.710
- **Year/Venue**: 2025 / Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'TableRAG: A Retrieval Augmented Generation Framework for Heterogeneous Document Reasoning' contributes a 'tool' matching target artifact 'taxonomy+paper'. Matched keywords: primary:title:retrieval augmented generation.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 2. Visual-RAG: Benchmarking Text-to-Image Retrieval Augmented Generation for Visual Knowledge Intensive Queries
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2502.16636
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Visual-RAG: Benchmarking Text-to-Image Retrieval Augmented Generation for Visual Knowledge Intensive' contributes a 'benchmark' matching target artifact 'taxonomy+paper'. Matched keywords: primary:title:retrieval augmented generation.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 3. Prospects of Retrieval Augmented Generation (RAG) for Academic Library Search and Retrieval
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.5295044
- **Year/Venue**: 2025 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'Prospects of Retrieval Augmented Generation (RAG) for Academic Library Search and Retrieval' contributes a 'tool' matching target artifact 'taxonomy+paper'. Matched keywords: primary:title:retrieval augmented generation.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 4. Retrieval Augmented Generation (RAG) Model
- **Source**: paper  **URL**: https://doi.org/10.55248/gengpi.6.0125.0635
- **Year/Venue**: 2025 / International Journal of Research Publication and Reviews
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Retrieval Augmented Generation (RAG) Model' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: primary:title:retrieval augmented generation.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 5. Retrieval Augmented Generation for HPC Code Optimization
- **Source**: paper  **URL**: https://doi.org/10.31274/cc-20260223-58
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Retrieval Augmented Generation for HPC Code Optimization' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: primary:title:retrieval augmented generation.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 6. Understanding Retrieval Pitfalls: Challenges Faced by Retrieval Augmented Generation (RAG) models
- **Source**: paper  **URL**: https://doi.org/10.59350/xcq3s-jvk04
- **Year/Venue**: 2024 / n/a
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'Understanding Retrieval Pitfalls: Challenges Faced by Retrieval Augmented Generation (RAG) models' contributes a 'benchmark' matching target artifact 'taxonomy+paper'. Matched keywords: primary:title:retrieval augmented generation.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 7. Protótipo de Pesquisa Documental para a Polícia Militar do Paraná com Retrieval Augmented Generation e Gemini AI em Ambi
- **Source**: paper  **URL**: https://doi.org/10.51473/rcmos.v1i2.2024.736
- **Year/Venue**: 2024 / RCMOS - Revista Científica Multidisciplinar O Saber
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Protótipo de Pesquisa Documental para a Polícia Militar do Paraná com Retrieval Augmented Generation' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: primary:title:retrieval augmented generation.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 8. Comparative Performance of Retrieval Augmented Generation Tourism Chatbots
- **Source**: paper  **URL**: https://doi.org/10.21070/ijins.v27i1.1836
- **Year/Venue**: 2026 / Indonesian Journal of Innovation Studies
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Comparative Performance of Retrieval Augmented Generation Tourism Chatbots' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: primary:title:retrieval augmented generation.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 9. qinchuanhui/UDA-Benchmark
- **Source**: github  **URL**: https://github.com/qinchuanhui/UDA-Benchmark
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'qinchuanhui/UDA-Benchmark' (43 stars) provides an implementation of 'retrieval augmented generation'. Description: [neurips'24] uda: a benchmark suite for retrieval augmented generation in real-world document analysis.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 10. TonicAI/tonic_validate
- **Source**: github  **URL**: https://github.com/TonicAI/tonic_validate
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'TonicAI/tonic_validate' (325 stars) provides an implementation of 'retrieval augmented generation'. Description: metrics to evaluate the quality of responses of your retrieval augmented generation (rag) applications..
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 11. neulab/ragged
- **Source**: github  **URL**: https://github.com/neulab/ragged
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'neulab/ragged' (61 stars) provides an implementation of 'retrieval augmented generation'. Description: retrieval augmented generation generalized evaluation dataset.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 12. mtc/cleaned_xsum-faith-test-set-with-faithfulness-annotation
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/mtc/cleaned_xsum-faith-test-set-with-faithfulness-annotation
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'mtc/cleaned_xsum-faith-test-set-with-faithfulness-annotation' (23 downloads) matched 'faithfulness' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 13. mtc/faithfulness_benchmark_sanity_check_factcc
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/mtc/faithfulness_benchmark_sanity_check_factcc
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'mtc/faithfulness_benchmark_sanity_check_factcc' (40 downloads) matched 'faithfulness' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 14. mtc/faithfulness_benchmark_sanity_check_xsum_faith
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/mtc/faithfulness_benchmark_sanity_check_xsum_faith
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'mtc/faithfulness_benchmark_sanity_check_xsum_faith' (34 downloads) matched 'faithfulness' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 15. mtc/absinth_german_faithfulness_detection_dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/mtc/absinth_german_faithfulness_detection_dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'mtc/absinth_german_faithfulness_detection_dataset' (43 downloads) matched 'faithfulness' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 16. mtc/span_absinth_german_faithfulness_detection_dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/mtc/span_absinth_german_faithfulness_detection_dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'mtc/span_absinth_german_faithfulness_detection_dataset' (26 downloads) matched 'faithfulness' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Correctness is not Faithfulness in RAG Attributions](https://doi.org/10.48550/arXiv.2412.18004) | 2024 | arXiv.org | paper | 0.3 | strong |
| 2 | paper | [HAD: HAllucination Detection Language Models Based on a Comprehensive Hallucinat](https://doi.org/10.48550/arXiv.2510.19318) | 2025 | arXiv.org | survey | 0.25 | strong |
| 3 | paper | [From Prerequisites to Predictions: Validating a Geometric Hallucination Taxonomy](https://doi.org/10.48550/arXiv.2603.00307) | 2026 | arXiv.org | survey | 0.25 | strong |
| 4 | paper | [faithfulness, n.](https://doi.org/10.1093/oed/1055996628) | 2023 | Oxford English Dictionary | paper | 0.25 | strong |
| 5 | paper | [God's Faithfulness and Dementia: Christian Theology in Context](https://doi.org/10.4324/9781003434030-7) | 2023 | Still Waters Run Deep | paper | 0.25 | strong |
| 6 | paper | [FAITHFULNESS](https://doi.org/10.2307/jj.26622536.7) | 2025 | Love's Virtues | paper | 0.25 | strong |
| 7 | paper | [Faithfulness to Faithfulness: The Compass of Spiritual Reading in the Letters of](https://doi.org/10.57106/scientia.v13i1.176) | 2024 | Scientia - The International Journal on  | paper | 0.25 | strong |
| 8 | paper | [The Faithfulness of Pluralism](https://doi.org/10.2307/j.ctv2xkjp3k) | 2023 |  | paper | 0.25 | strong |
| 9 | paper | [FACET: Measuring Attribution Faithfulness in Multi-Factor LLM Reasoning](https://doi.org/10.2139/ssrn.6564479) | 2026 |  | paper | 0.25 | strong |
| 10 | paper | [God’s faithfulness has never failed](https://doi.org/10.5040/9781350401259.0021) | 2025 | Christians in the City of Lagos | paper | 0.25 | strong |
| 11 | paper | [”Faithfulness Itself“](https://doi.org/10.14325/mississippi/9781496837981.003.0004) | 2022 | Little Women at 150 | paper | 0.25 | strong |
| 12 | paper | [Post Truth? Facts and Faithfulness](https://doi.org/10.51644/iesk5852) | 2024 | Consensus | paper | 0.25 | strong |
| 13 | paper | [The Faithfulness of Jesus (12:1–13)](https://doi.org/10.5040/9780567696052.ch-019) | 2025 | Hebrews A Social Identity Commentary | paper | 0.25 | strong |
| 14 | paper | [Input Prevocalic Faithfulness and Opacity](https://doi.org/10.1162/ling.a.56) | 2025 | Linguistic Inquiry | paper | 0.25 | strong |
| 15 | paper | [The Faithfulness of Self-Realisation](https://doi.org/10.4324/9781003670049) | 2026 |  | paper | 0.25 | strong |
| 16 | paper | [God’s Faithfulness (6:9–20)](https://doi.org/10.5040/9780567696052.ch-012) | 2025 | Hebrews A Social Identity Commentary | paper | 0.25 | strong |

### 1. Correctness is not Faithfulness in RAG Attributions
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2412.18004
- **Year/Venue**: 2024 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.30: paper titled 'Correctness is not Faithfulness in RAG Attributions' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness|syn:abstract:citation correctness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. HAD: HAllucination Detection Language Models Based on a Comprehensive Hallucination Taxonomy
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.19318
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.25: paper titled 'HAD: HAllucination Detection Language Models Based on a Comprehensive Hallucination Taxonomy' contributes a 'survey' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:hallucination taxonomy.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. From Prerequisites to Predictions: Validating a Geometric Hallucination Taxonomy Through Controlled Induction
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2603.00307
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.25: paper titled 'From Prerequisites to Predictions: Validating a Geometric Hallucination Taxonomy Through Controlled ' contributes a 'survey' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:hallucination taxonomy.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. faithfulness, n.
- **Source**: paper  **URL**: https://doi.org/10.1093/oed/1055996628
- **Year/Venue**: 2023 / Oxford English Dictionary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'faithfulness, n.' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. God's Faithfulness and Dementia: Christian Theology in Context
- **Source**: paper  **URL**: https://doi.org/10.4324/9781003434030-7
- **Year/Venue**: 2023 / Still Waters Run Deep
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'God's Faithfulness and Dementia: Christian Theology in Context' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. FAITHFULNESS
- **Source**: paper  **URL**: https://doi.org/10.2307/jj.26622536.7
- **Year/Venue**: 2025 / Love's Virtues
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'FAITHFULNESS' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. Faithfulness to Faithfulness: The Compass of Spiritual Reading in the Letters of Saint Paul
- **Source**: paper  **URL**: https://doi.org/10.57106/scientia.v13i1.176
- **Year/Venue**: 2024 / Scientia - The International Journal on the Liberal Arts
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Faithfulness to Faithfulness: The Compass of Spiritual Reading in the Letters of Saint Paul' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. The Faithfulness of Pluralism
- **Source**: paper  **URL**: https://doi.org/10.2307/j.ctv2xkjp3k
- **Year/Venue**: 2023 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Faithfulness of Pluralism' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. FACET: Measuring Attribution Faithfulness in Multi-Factor LLM Reasoning
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6564479
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'FACET: Measuring Attribution Faithfulness in Multi-Factor LLM Reasoning' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. God’s faithfulness has never failed
- **Source**: paper  **URL**: https://doi.org/10.5040/9781350401259.0021
- **Year/Venue**: 2025 / Christians in the City of Lagos
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'God’s faithfulness has never failed' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. ”Faithfulness Itself“
- **Source**: paper  **URL**: https://doi.org/10.14325/mississippi/9781496837981.003.0004
- **Year/Venue**: 2022 / Little Women at 150
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled '”Faithfulness Itself“' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. Post Truth? Facts and Faithfulness
- **Source**: paper  **URL**: https://doi.org/10.51644/iesk5852
- **Year/Venue**: 2024 / Consensus
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Post Truth? Facts and Faithfulness' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. The Faithfulness of Jesus (12:1–13)
- **Source**: paper  **URL**: https://doi.org/10.5040/9780567696052.ch-019
- **Year/Venue**: 2025 / Hebrews A Social Identity Commentary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Faithfulness of Jesus (12:1–13)' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 14. Input Prevocalic Faithfulness and Opacity
- **Source**: paper  **URL**: https://doi.org/10.1162/ling.a.56
- **Year/Venue**: 2025 / Linguistic Inquiry
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Input Prevocalic Faithfulness and Opacity' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 15. The Faithfulness of Self-Realisation
- **Source**: paper  **URL**: https://doi.org/10.4324/9781003670049
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'The Faithfulness of Self-Realisation' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 16. God’s Faithfulness (6:9–20)
- **Source**: paper  **URL**: https://doi.org/10.5040/9780567696052.ch-012
- **Year/Venue**: 2025 / Hebrews A Social Identity Commentary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'God’s Faithfulness (6:9–20)' contributes a 'paper' matching target artifact 'taxonomy+paper'. Matched keywords: kw:title:faithfulness.
- **How we differ**: Our proposed work focuses specifically on 'Hallucination taxonomy: RAG vs no-RAG'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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

1. Document a clear differentiator before GO (partial overlaps: 16).
