# Existing Work Report — NC07_NC: RAG for question answering [NEGATIVE_CONTROL]

> ⛔ **GO BLOCKED (artifact overlap)** — 15 direct artifact(s) (GitHub=4, HF=11, PWC=0); artifact_diff_strength=`weak`. No peer-reviewed paper directly covers this — but artifact overlap is high and differentiator is weak. Narrow before GO.

> 📌 **Note (artifact-only overlap):** Academic/paper overlap appears low, but artifact overlap is high (15 direct artifacts). This topic may still be publishable — a peer-reviewed benchmark/protocol with a clear domain or methodological focus is inherently differentiated from GitHub repos and HuggingFace datasets. Explicitly state: (1) peer-reviewed systematic protocol vs existing repos; (2) specific domain/use-case vs general artifacts; (3) evaluation harness + reproducibility package vs raw data.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 4 |
| HuggingFace direct artifacts | 11 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 15 |
| Artifact diff strength | `weak` |
| Partial overlaps (total) | 64 |
| Adjacent | 12 |
| Total findings | 91 |
| peer_reviewed_direct | No |
| high_artifact_overlap | ⚠️ Yes |
| GO blocked | **YES** |
| Differentiator required | Yes |
| Artifact differentiator required | Yes |

## Peer-Reviewed Direct Overlaps

_None._

## Artifact Direct Overlaps (GitHub / HF / PWC)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | github | [raga-ai-hub/RagaAI-Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) |  | GitHub | tool | 16154 | weak |
| 2 | github | [Marker-Inc-Korea/AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) |  | GitHub | tool | 4753 | weak |
| 3 | github | [1517005260/graph-rag-agent](https://github.com/1517005260/graph-rag-agent) |  | GitHub | tool | 2148 | weak |
| 4 | github | [AnkitNayak-eth/EpsteinFiles-RAG](https://github.com/AnkitNayak-eth/EpsteinFiles-RAG) |  | GitHub | tool | 372 | weak |
| 5 | huggingface | [galileo-ai/ragbench](https://huggingface.co/datasets/galileo-ai/ragbench) |  | HuggingFace | dataset | 4077 | weak |
| 6 | huggingface | [bharat-raghunathan/indian-foods-dataset](https://huggingface.co/datasets/bharat-raghunathan/indian-foods-dataset) |  | HuggingFace | dataset | 217 | weak |
| 7 | huggingface | [neural-bridge/rag-dataset-1200](https://huggingface.co/datasets/neural-bridge/rag-dataset-1200) |  | HuggingFace | dataset | 1032 | weak |
| 8 | huggingface | [wandb/RAGTruth-processed](https://huggingface.co/datasets/wandb/RAGTruth-processed) |  | HuggingFace | dataset | 1554 | weak |
| 9 | huggingface | [MedSwin/PubMedQA-u-RAG](https://huggingface.co/datasets/MedSwin/PubMedQA-u-RAG) |  | HuggingFace | dataset | 324 | weak |
| 10 | huggingface | [vibrantlabsai/ragas-wikiqa](https://huggingface.co/datasets/vibrantlabsai/ragas-wikiqa) |  | HuggingFace | dataset | 334 | weak |
| 11 | huggingface | [Malikeh1375/medical-question-answering-datasets](https://huggingface.co/datasets/Malikeh1375/medical-question-answering-datasets) |  | HuggingFace | dataset | 1600 | weak |
| 12 | huggingface | [AswiN037/tamil-question-answering-dataset](https://huggingface.co/datasets/AswiN037/tamil-question-answering-dataset) |  | HuggingFace | dataset | 238 | weak |
| 13 | huggingface | [nogyxo/question-answering-ukrainian](https://huggingface.co/datasets/nogyxo/question-answering-ukrainian) |  | HuggingFace | dataset | 275 | weak |
| 14 | huggingface | [lnwang/retrieval_qa](https://huggingface.co/datasets/lnwang/retrieval_qa) |  | HuggingFace | dataset | 154 | weak |
| 15 | huggingface | [MCINext/synthetic-persian-qa-retrieval](https://huggingface.co/datasets/MCINext/synthetic-persian-qa-retrieval) |  | HuggingFace | dataset | 123 | weak |

### 1. raga-ai-hub/RagaAI-Catalyst
- **Source**: github  **URL**: https://github.com/raga-ai-hub/RagaAI-Catalyst
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'raga-ai-hub/RagaAI-Catalyst' (16,154 stars) provides an implementation of 'rag'. Description: python sdk for agent ai observability, monitoring and evaluation framework. includes features like agent, llm and tools .
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 2. Marker-Inc-Korea/AutoRAG
- **Source**: github  **URL**: https://github.com/Marker-Inc-Korea/AutoRAG
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'Marker-Inc-Korea/AutoRAG' (4,753 stars) provides an implementation of 'rag'. Description: autorag: an open-source framework for retrieval-augmented generation (rag) evaluation & optimization with automl-style a.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 3. 1517005260/graph-rag-agent
- **Source**: github  **URL**: https://github.com/1517005260/graph-rag-agent
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo '1517005260/graph-rag-agent' (2,148 stars) provides an implementation of 'rag'. Description: 拼好rag：手搓并融合了graphrag、lightrag、neo4j-llm-graph-builder进行知识图谱构建以及搜索；整合deepsearch技术实现私域rag的推理；自制针对graphrag的评估框架| integrate .
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 4. AnkitNayak-eth/EpsteinFiles-RAG
- **Source**: github  **URL**: https://github.com/AnkitNayak-eth/EpsteinFiles-RAG
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'AnkitNayak-eth/EpsteinFiles-RAG' (372 stars) provides an implementation of 'rag'. Description: a rag pipeline implementation built on the 'epstein files 20k' dataset from hugging face (teyler)..
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 5. galileo-ai/ragbench
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/galileo-ai/ragbench
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'galileo-ai/ragbench' (4,077 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 6. bharat-raghunathan/indian-foods-dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/bharat-raghunathan/indian-foods-dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'bharat-raghunathan/indian-foods-dataset' (217 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 7. neural-bridge/rag-dataset-1200
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/neural-bridge/rag-dataset-1200
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'neural-bridge/rag-dataset-1200' (1,032 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 8. wandb/RAGTruth-processed
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/wandb/RAGTruth-processed
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'wandb/RAGTruth-processed' (1,554 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 9. MedSwin/PubMedQA-u-RAG
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/MedSwin/PubMedQA-u-RAG
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'MedSwin/PubMedQA-u-RAG' (324 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 10. vibrantlabsai/ragas-wikiqa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/vibrantlabsai/ragas-wikiqa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'vibrantlabsai/ragas-wikiqa' (334 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 11. Malikeh1375/medical-question-answering-datasets
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Malikeh1375/medical-question-answering-datasets
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Malikeh1375/medical-question-answering-datasets' (1,600 downloads) matched 'question answering' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 12. AswiN037/tamil-question-answering-dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/AswiN037/tamil-question-answering-dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'AswiN037/tamil-question-answering-dataset' (238 downloads) matched 'question answering' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 13. nogyxo/question-answering-ukrainian
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/nogyxo/question-answering-ukrainian
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'nogyxo/question-answering-ukrainian' (275 downloads) matched 'question answering' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 14. lnwang/retrieval_qa
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/lnwang/retrieval_qa
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'lnwang/retrieval_qa' (154 downloads) matched 'retrieval QA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

### 15. MCINext/synthetic-persian-qa-retrieval
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/MCINext/synthetic-persian-qa-retrieval
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'MCINext/synthetic-persian-qa-retrieval' (123 downloads) matched 'retrieval QA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `weak`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Tatarstan Toponyms: A Bilingual Dataset and Hybrid RAG System for Geospatial Que](http://arxiv.org/abs/2605.05962v1) | 2026 | arXiv | dataset | 0.75 | moderate |
| 2 | paper | [MedRAG: Retrieval-Augmented Generation for Medical QA-Comparing Base and RAG-Aug](https://doi.org/10.2139/ssrn.6608518) | 2026 |  | survey | 0.6 | moderate |
| 3 | paper | [LatentRAG: Latent Reasoning and Retrieval for Efficient Agentic RAG](http://arxiv.org/abs/2605.06285v1) | 2026 | arXiv | paper | 0.6 | moderate |
| 4 | paper | [DO-RAG: A Domain-Specific QA Framework Using Knowledge Graph-Enhanced Retrieval-](https://doi.org/10.36227/techrxiv.174837976.69904638/v1) | 2025 |  | tool | 0.5 | moderate |
| 5 | paper | [Traditional RAG vs. Agentic RAG: A Comparative Study of Retrieval-Augmented Syst](https://doi.org/10.36227/techrxiv.175624551.12254549/v1) | 2025 |  | tool | 0.5 | moderate |
| 6 | paper | [PandaChat-RAG: Towards the Benchmark for Slovenian RAG Applications](https://doi.org/10.70314/is.2024.scai.538) | 2024 | Proceedings of Slovenian Conference on A | benchmark | 0.5 | moderate |
| 7 | paper | [Rag Pickers](https://doi.org/10.2307/jj.21426705.7) | 2025 | Rag Pickers | paper | 0.5 | moderate |
| 8 | paper | [Safe RAG by RAG: Untying the Bell That RAG Rang with the RAG Hand](https://doi.org/10.1609/aaai.v40i38.40462) | 2026 | Proceedings of the AAAI Conference on Ar | paper | 0.5 | moderate |
| 9 | paper | [rag business/rag trade](https://doi.org/10.5040/9781501365287.2195) | 2022 | The Fairchild Books Dictionary of Fashio | paper | 0.5 | moderate |
| 10 | paper | [A Unified Evaluation Framework for Grounded LLM Architectures: Comparative Analy](https://doi.org/10.1109/aisp68263.2025.11396270) | 2025 | 2025 5th International Conference on Art | tool | 0.5 | moderate |
| 11 | paper | [Agentic RAG Optimization via MDP Modeling and Pruning: The DecEx-RAG Framework](https://doi.org/10.22541/au.176478094.40436687/v1) | 2025 |  | tool | 0.5 | moderate |
| 12 | paper | [Domain-Partitioned Retrieval as a Hallucination Mitigation Strategy in Conversat](https://doi.org/10.21203/rs.3.rs-9334334/v1) | 2026 |  | paper | 0.5 | moderate |
| 13 | paper | [Lightweight DS-RAG: A Training-Free RAG Framework for Multi-Document QA on Edge ](https://doi.org/10.9708/jksci.2025.30.11.019) | 2025 | Journal of the Korea Society of Computer | tool | 0.5 | moderate |
| 14 | paper | [SAKA-RAG: Structure-Aware Knowledge Abstraction RAG Framework for Legal Reasonin](https://doi.org/10.2139/ssrn.5413499) | 2025 |  | tool | 0.5 | moderate |
| 15 | paper | [BHT-RAG: Birch-based Hierarchical Tree RAG in Mass Spectrometry](https://doi.org/10.3724/2096-7004.di.2025.0047) | 2025 | Data Intelligence | paper | 0.5 | moderate |
| 16 | paper | [rag-burn, v.](https://doi.org/10.1093/oed/2013843301) | 2023 | Oxford English Dictionary | paper | 0.5 | moderate |
| 17 | paper | [rag, n.¹](https://doi.org/10.1093/oed/4686794569) | 2023 | Oxford English Dictionary | paper | 0.5 | moderate |
| 18 | paper | [rag, v.³](https://doi.org/10.1093/oed/9884299696) | 2023 | Oxford English Dictionary | paper | 0.5 | moderate |
| 19 | paper | [CoralX.AI: Multi-Hop, Redundancy-Aware Scientific QA via Hybrid Semantic-Graph R](https://doi.org/10.31274/cc-20251215-154) | 2025 |  | paper | 0.5 | moderate |
| 20 | paper | [Event-Causal RAG: A Retrieval-Augmented Generation Framework for Long Video Reas](http://arxiv.org/abs/2605.06185v1) | 2026 | arXiv | tool | 0.5 | moderate |
| 21 | paper | [Retina-RAG: Retrieval-Augmented Vision-Language Modeling for Joint Retinal Diagn](http://arxiv.org/abs/2605.06173v1) | 2026 | arXiv | paper | 0.5 | moderate |
| 22 | paper | [LeakDojo: Decoding the Leakage Threats of RAG Systems](http://arxiv.org/abs/2605.05818v1) | 2026 | arXiv | tool | 0.5 | moderate |
| 23 | paper | [Text-Graph Synergy: A Bidirectional Verification and Completion Framework for RA](http://arxiv.org/abs/2605.05643v1) | 2026 | arXiv | tool | 0.5 | moderate |
| 24 | paper | [Architecture Matters: Comparing RAG Systems under Knowledge Base Poisoning](http://arxiv.org/abs/2605.05632v1) | 2026 | arXiv | tool | 0.5 | moderate |
| 25 | github | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) |  | GitHub | tool | 80179 | moderate |
| 26 | github | [pathwaycom/pathway](https://github.com/pathwaycom/pathway) |  | GitHub | tool | 63263 | moderate |
| 27 | github | [deepset-ai/haystack](https://github.com/deepset-ai/haystack) |  | GitHub | tool | 25142 | moderate |
| 28 | github | [HKUDS/RAG-Anything](https://github.com/HKUDS/RAG-Anything) |  | GitHub | tool | 20013 | moderate |
| 29 | github | [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) |  | GitHub | tool | 16289 | moderate |
| 30 | github | [llmware-ai/llmware](https://github.com/llmware-ai/llmware) |  | GitHub | tool | 14862 | moderate |
| 31 | github | [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) |  | GitHub | tool | 11930 | moderate |
| 32 | github | [OpenSPG/KAG](https://github.com/OpenSPG/KAG) |  | GitHub | tool | 8725 | moderate |
| 33 | github | [OpenBMB/UltraRAG](https://github.com/OpenBMB/UltraRAG) |  | GitHub | tool | 5540 | moderate |
| 34 | github | [truefoundry/cognita](https://github.com/truefoundry/cognita) |  | GitHub | tool | 4410 | moderate |
| 35 | github | [OSU-NLP-Group/HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) |  | GitHub | tool | 3496 | moderate |
| 36 | github | [IntelLabs/fastRAG](https://github.com/IntelLabs/fastRAG) |  | GitHub | tool | 1778 | moderate |
| 37 | github | [AkariAsai/self-rag](https://github.com/AkariAsai/self-rag) |  | GitHub | tool | 2377 | moderate |
| 38 | github | [IlyaRice/RAG-Challenge-2](https://github.com/IlyaRice/RAG-Challenge-2) |  | GitHub | tool | 2291 | moderate |
| 39 | github | [PromtEngineer/localGPT-Vision](https://github.com/PromtEngineer/localGPT-Vision) |  | GitHub | tool | 630 | moderate |
| 40 | github | [Azure-Samples/aisearch-openai-rag-audio](https://github.com/Azure-Samples/aisearch-openai-rag-audio) |  | GitHub | tool | 554 | moderate |
| 41 | github | [liu673/rag-all-techniques](https://github.com/liu673/rag-all-techniques) |  | GitHub | tool | 468 | moderate |
| 42 | github | [FareedKhan-dev/complex-RAG-guide](https://github.com/FareedKhan-dev/complex-RAG-guide) |  | GitHub | tool | 451 | moderate |
| 43 | github | [Leon1207/Video-RAG-master](https://github.com/Leon1207/Video-RAG-master) |  | GitHub | tool | 427 | moderate |
| 44 | github | [FudanDNN-NLP/RAG](https://github.com/FudanDNN-NLP/RAG) |  | GitHub | tool | 346 | moderate |
| 45 | github | [sci-m-wang/OpenCE](https://github.com/sci-m-wang/OpenCE) |  | GitHub | tool | 333 | moderate |
| 46 | github | [emarco177/documentation-helper](https://github.com/emarco177/documentation-helper) |  | GitHub | tool | 301 | moderate |
| 47 | github | [daveebbelaar/pgvectorscale-rag-solution](https://github.com/daveebbelaar/pgvectorscale-rag-solution) |  | GitHub | tool | 264 | moderate |
| 48 | github | [ashleve/ActiveRagdoll](https://github.com/ashleve/ActiveRagdoll) |  | GitHub | tool | 250 | moderate |
| 49 | huggingface | [dwb2023/ragas-golden-dataset](https://huggingface.co/datasets/dwb2023/ragas-golden-dataset) |  | HuggingFace | dataset | 77 | moderate |
| 50 | huggingface | [reglab/legal_rag_hallucinations](https://huggingface.co/datasets/reglab/legal_rag_hallucinations) |  | HuggingFace | dataset | 39 | moderate |
| 51 | huggingface | [Azzindani/ID_REG_MD_RAG](https://huggingface.co/datasets/Azzindani/ID_REG_MD_RAG) |  | HuggingFace | dataset | 75 | moderate |
| 52 | huggingface | [s1arsky/Warhammer-Fantasy-Lexicanum-RAG_v1.12](https://huggingface.co/datasets/s1arsky/Warhammer-Fantasy-Lexicanum-RAG_v1.12) |  | HuggingFace | dataset | 84 | moderate |
| 53 | huggingface | [huggingartists/rage-against-the-machine](https://huggingface.co/datasets/huggingartists/rage-against-the-machine) |  | HuggingFace | dataset | 69 | moderate |
| 54 | huggingface | [hr16/Miwano-Rag](https://huggingface.co/datasets/hr16/Miwano-Rag) |  | HuggingFace | dataset | 24 | moderate |
| 55 | huggingface | [raghuram13/autotrain-data-sentiment_analysis](https://huggingface.co/datasets/raghuram13/autotrain-data-sentiment_analysis) |  | HuggingFace | dataset | 72 | moderate |
| 56 | huggingface | [luozhouyang/question-answering-datasets](https://huggingface.co/datasets/luozhouyang/question-answering-datasets) |  | HuggingFace | dataset | 56 | moderate |
| 57 | huggingface | [RUCAIBox/Question-Answering](https://huggingface.co/datasets/RUCAIBox/Question-Answering) |  | HuggingFace | dataset | 41 | moderate |
| 58 | huggingface | [open-source-metrics/visual-question-answering-checkpoint-downloads](https://huggingface.co/datasets/open-source-metrics/visual-question-answering-checkpoint-downloads) |  | HuggingFace | dataset | 43 | moderate |
| 59 | huggingface | [LangChainDatasets/question-answering-state-of-the-union](https://huggingface.co/datasets/LangChainDatasets/question-answering-state-of-the-union) |  | HuggingFace | dataset | 61 | moderate |
| 60 | huggingface | [nogyxo/question-answering-ukrainian-json-answers](https://huggingface.co/datasets/nogyxo/question-answering-ukrainian-json-answers) |  | HuggingFace | dataset | 24 | moderate |
| 61 | huggingface | [chenle015/OpenMP_Question_Answering](https://huggingface.co/datasets/chenle015/OpenMP_Question_Answering) |  | HuggingFace | dataset | 36 | moderate |
| 62 | huggingface | [zihanz/RetrievalQA](https://huggingface.co/datasets/zihanz/RetrievalQA) |  | HuggingFace | dataset | 32 | moderate |
| 63 | huggingface | [aialt/RetrievalQA](https://huggingface.co/datasets/aialt/RetrievalQA) |  | HuggingFace | dataset | 54 | moderate |
| 64 | huggingface | [xiao-centml/rag-qa-retrieval](https://huggingface.co/datasets/xiao-centml/rag-qa-retrieval) |  | HuggingFace | dataset | 27 | moderate |

### 1. Tatarstan Toponyms: A Bilingual Dataset and Hybrid RAG System for Geospatial Question Answering
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.05962v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: dataset
- **Why it overlaps**: Relevance 0.75: paper titled 'Tatarstan Toponyms: A Bilingual Dataset and Hybrid RAG System for Geospatial Question Answering' contributes a 'dataset' matching target artifact 'framework'. Matched keywords: primary:title:rag|kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. MedRAG: Retrieval-Augmented Generation for Medical QA-Comparing Base and RAG-Augmented LLM Performance on Evidence from 
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6608518
- **Year/Venue**: 2026 / n/a
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.60: paper titled 'MedRAG: Retrieval-Augmented Generation for Medical QA-Comparing Base and RAG-Augmented LLM Performan' contributes a 'survey' matching target artifact 'framework'. Matched keywords: primary:title:rag|kw:abstract:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. LatentRAG: Latent Reasoning and Retrieval for Efficient Agentic RAG
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06285v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.60: paper titled 'LatentRAG: Latent Reasoning and Retrieval for Efficient Agentic RAG' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag|kw:abstract:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. DO-RAG: A Domain-Specific QA Framework Using Knowledge Graph-Enhanced Retrieval-Augmented Generation
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.174837976.69904638/v1
- **Year/Venue**: 2025 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'DO-RAG: A Domain-Specific QA Framework Using Knowledge Graph-Enhanced Retrieval-Augmented Generation' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. Traditional RAG vs. Agentic RAG: A Comparative Study of Retrieval-Augmented Systems
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.175624551.12254549/v1
- **Year/Venue**: 2025 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'Traditional RAG vs. Agentic RAG: A Comparative Study of Retrieval-Augmented Systems' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. PandaChat-RAG: Towards the Benchmark for Slovenian RAG Applications
- **Source**: paper  **URL**: https://doi.org/10.70314/is.2024.scai.538
- **Year/Venue**: 2024 / Proceedings of Slovenian Conference on Artificial Intelligence 2024
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'PandaChat-RAG: Towards the Benchmark for Slovenian RAG Applications' contributes a 'benchmark' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. Rag Pickers
- **Source**: paper  **URL**: https://doi.org/10.2307/jj.21426705.7
- **Year/Venue**: 2025 / Rag Pickers
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Rag Pickers' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. Safe RAG by RAG: Untying the Bell That RAG Rang with the RAG Hand
- **Source**: paper  **URL**: https://doi.org/10.1609/aaai.v40i38.40462
- **Year/Venue**: 2026 / Proceedings of the AAAI Conference on Artificial Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Safe RAG by RAG: Untying the Bell That RAG Rang with the RAG Hand' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. rag business/rag trade
- **Source**: paper  **URL**: https://doi.org/10.5040/9781501365287.2195
- **Year/Venue**: 2022 / The Fairchild Books Dictionary of Fashion
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'rag business/rag trade' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. A Unified Evaluation Framework for Grounded LLM Architectures: Comparative Analysis of RAG, Self-RAG, and Agentic RAG
- **Source**: paper  **URL**: https://doi.org/10.1109/aisp68263.2025.11396270
- **Year/Venue**: 2025 / 2025 5th International Conference on Artificial Intelligence and Signal Processing (AISP)
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'A Unified Evaluation Framework for Grounded LLM Architectures: Comparative Analysis of RAG, Self-RAG' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. Agentic RAG Optimization via MDP Modeling and Pruning: The DecEx-RAG Framework
- **Source**: paper  **URL**: https://doi.org/10.22541/au.176478094.40436687/v1
- **Year/Venue**: 2025 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'Agentic RAG Optimization via MDP Modeling and Pruning: The DecEx-RAG Framework' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. Domain-Partitioned Retrieval as a Hallucination Mitigation Strategy in Conversational RAG: The PC-RAG Architecture
- **Source**: paper  **URL**: https://doi.org/10.21203/rs.3.rs-9334334/v1
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Domain-Partitioned Retrieval as a Hallucination Mitigation Strategy in Conversational RAG: The PC-RA' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 13. Lightweight DS-RAG: A Training-Free RAG Framework for Multi-Document QA on Edge Devices
- **Source**: paper  **URL**: https://doi.org/10.9708/jksci.2025.30.11.019
- **Year/Venue**: 2025 / Journal of the Korea Society of Computer and Information
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'Lightweight DS-RAG: A Training-Free RAG Framework for Multi-Document QA on Edge Devices' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 14. SAKA-RAG: Structure-Aware Knowledge Abstraction RAG Framework for Legal Reasoning
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.5413499
- **Year/Venue**: 2025 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'SAKA-RAG: Structure-Aware Knowledge Abstraction RAG Framework for Legal Reasoning' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 15. BHT-RAG: Birch-based Hierarchical Tree RAG in Mass Spectrometry
- **Source**: paper  **URL**: https://doi.org/10.3724/2096-7004.di.2025.0047
- **Year/Venue**: 2025 / Data Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'BHT-RAG: Birch-based Hierarchical Tree RAG in Mass Spectrometry' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 16. rag-burn, v.
- **Source**: paper  **URL**: https://doi.org/10.1093/oed/2013843301
- **Year/Venue**: 2023 / Oxford English Dictionary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'rag-burn, v.' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 17. rag, n.¹
- **Source**: paper  **URL**: https://doi.org/10.1093/oed/4686794569
- **Year/Venue**: 2023 / Oxford English Dictionary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'rag, n.¹' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 18. rag, v.³
- **Source**: paper  **URL**: https://doi.org/10.1093/oed/9884299696
- **Year/Venue**: 2023 / Oxford English Dictionary
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'rag, v.³' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 19. CoralX.AI: Multi-Hop, Redundancy-Aware Scientific QA via Hybrid Semantic-Graph Retrieval and RAG
- **Source**: paper  **URL**: https://doi.org/10.31274/cc-20251215-154
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'CoralX.AI: Multi-Hop, Redundancy-Aware Scientific QA via Hybrid Semantic-Graph Retrieval and RAG' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 20. Event-Causal RAG: A Retrieval-Augmented Generation Framework for Long Video Reasoning in Complex Scenarios
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06185v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'Event-Causal RAG: A Retrieval-Augmented Generation Framework for Long Video Reasoning in Complex Sce' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 21. Retina-RAG: Retrieval-Augmented Vision-Language Modeling for Joint Retinal Diagnosis and Clinical Report Generation
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.06173v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Retina-RAG: Retrieval-Augmented Vision-Language Modeling for Joint Retinal Diagnosis and Clinical Re' contributes a 'paper' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 22. LeakDojo: Decoding the Leakage Threats of RAG Systems
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.05818v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'LeakDojo: Decoding the Leakage Threats of RAG Systems' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 23. Text-Graph Synergy: A Bidirectional Verification and Completion Framework for RAG
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.05643v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'Text-Graph Synergy: A Bidirectional Verification and Completion Framework for RAG' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 24. Architecture Matters: Comparing RAG Systems under Knowledge Base Poisoning
- **Source**: paper  **URL**: http://arxiv.org/abs/2605.05632v1
- **Year/Venue**: 2026 / arXiv
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.50: paper titled 'Architecture Matters: Comparing RAG Systems under Knowledge Base Poisoning' contributes a 'tool' matching target artifact 'framework'. Matched keywords: primary:title:rag.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 25. infiniflow/ragflow
- **Source**: github  **URL**: https://github.com/infiniflow/ragflow
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'infiniflow/ragflow' (80,179 stars) provides an implementation of 'rag'. Description: ragflow is a leading open-source retrieval-augmented generation (rag) engine that fuses cutting-edge rag with agent capa.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 26. pathwaycom/pathway
- **Source**: github  **URL**: https://github.com/pathwaycom/pathway
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'pathwaycom/pathway' (63,263 stars) provides an implementation of 'rag'. Description: python etl framework for stream processing, real-time analytics, llm pipelines, and rag..
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 27. deepset-ai/haystack
- **Source**: github  **URL**: https://github.com/deepset-ai/haystack
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'deepset-ai/haystack' (25,142 stars) provides an implementation of 'rag'. Description: open-source ai orchestration framework for building context-engineered, production-ready llm applications. design modula.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 28. HKUDS/RAG-Anything
- **Source**: github  **URL**: https://github.com/HKUDS/RAG-Anything
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'HKUDS/RAG-Anything' (20,013 stars) provides an implementation of 'rag'. Description: "rag-anything: all-in-one rag framework".
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 29. QwenLM/Qwen-Agent
- **Source**: github  **URL**: https://github.com/QwenLM/Qwen-Agent
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'QwenLM/Qwen-Agent' (16,289 stars) provides an implementation of 'rag'. Description: agent framework and applications built upon qwen>=3.0, featuring function calling, mcp, code interpreter, rag, chrome ex.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 30. llmware-ai/llmware
- **Source**: github  **URL**: https://github.com/llmware-ai/llmware
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'llmware-ai/llmware' (14,862 stars) provides an implementation of 'rag'. Description: unified framework for building enterprise rag pipelines with small, specialized models.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 31. langchain4j/langchain4j
- **Source**: github  **URL**: https://github.com/langchain4j/langchain4j
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'langchain4j/langchain4j' (11,930 stars) provides an implementation of 'rag'. Description: langchain4j is an idiomatic, open-source java library for building llm-powered applications on the jvm. it offers a unif.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 32. OpenSPG/KAG
- **Source**: github  **URL**: https://github.com/OpenSPG/KAG
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'OpenSPG/KAG' (8,725 stars) provides an implementation of 'rag'. Description: kag is a logical form-guided reasoning and retrieval framework based on openspg engine and llms. it is used to build log.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 33. OpenBMB/UltraRAG
- **Source**: github  **URL**: https://github.com/OpenBMB/UltraRAG
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'OpenBMB/UltraRAG' (5,540 stars) provides an implementation of 'rag'. Description: [github trending #2] a low-code mcp framework for building complex and innovative rag pipelines.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 34. truefoundry/cognita
- **Source**: github  **URL**: https://github.com/truefoundry/cognita
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'truefoundry/cognita' (4,410 stars) provides an implementation of 'rag'. Description: rag (retrieval augmented generation) framework for building modular, open source applications for production by truefoun.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 35. OSU-NLP-Group/HippoRAG
- **Source**: github  **URL**: https://github.com/OSU-NLP-Group/HippoRAG
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'OSU-NLP-Group/HippoRAG' (3,496 stars) provides an implementation of 'rag'. Description: [neurips'24] hipporag is a novel rag framework inspired by human long-term memory that enables llms to continuously inte.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 36. IntelLabs/fastRAG
- **Source**: github  **URL**: https://github.com/IntelLabs/fastRAG
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'IntelLabs/fastRAG' (1,778 stars) provides an implementation of 'rag'. Description: efficient retrieval augmentation and generation framework.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 37. AkariAsai/self-rag
- **Source**: github  **URL**: https://github.com/AkariAsai/self-rag
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'AkariAsai/self-rag' (2,377 stars) provides an implementation of 'rag'. Description: this includes the original implementation of self-rag: learning to retrieve, generate and critique through self-reflecti.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 38. IlyaRice/RAG-Challenge-2
- **Source**: github  **URL**: https://github.com/IlyaRice/RAG-Challenge-2
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'IlyaRice/RAG-Challenge-2' (2,291 stars) provides an implementation of 'rag'. Description: implementation of my rag system that won all categories in enterprise rag challenge 2.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 39. PromtEngineer/localGPT-Vision
- **Source**: github  **URL**: https://github.com/PromtEngineer/localGPT-Vision
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'PromtEngineer/localGPT-Vision' (630 stars) provides an implementation of 'rag'. Description: chat with your documents using vision language models. this repo implements an end to end rag pipeline with both local a.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 40. Azure-Samples/aisearch-openai-rag-audio
- **Source**: github  **URL**: https://github.com/Azure-Samples/aisearch-openai-rag-audio
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'Azure-Samples/aisearch-openai-rag-audio' (554 stars) provides an implementation of 'rag'. Description: a simple example implementation of the voicerag pattern to power interactive voice generative ai experiences using rag w.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 41. liu673/rag-all-techniques
- **Source**: github  **URL**: https://github.com/liu673/rag-all-techniques
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'liu673/rag-all-techniques' (468 stars) provides an implementation of 'rag'. Description: implementation of all rag techniques in a simpler way（以简单的方式实现所有 rag 技术）.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 42. FareedKhan-dev/complex-RAG-guide
- **Source**: github  **URL**: https://github.com/FareedKhan-dev/complex-RAG-guide
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'FareedKhan-dev/complex-RAG-guide' (451 stars) provides an implementation of 'rag'. Description: a step by step implementation of a complex rag pipeline to solve real world situations.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 43. Leon1207/Video-RAG-master
- **Source**: github  **URL**: https://github.com/Leon1207/Video-RAG-master
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'Leon1207/Video-RAG-master' (427 stars) provides an implementation of 'rag'. Description: ✨✨[neurips 2025] this is the official implementation of our paper "video-rag: visually-aligned retrieval-augmented long .
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 44. FudanDNN-NLP/RAG
- **Source**: github  **URL**: https://github.com/FudanDNN-NLP/RAG
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'FudanDNN-NLP/RAG' (346 stars) provides an implementation of 'rag'. Description: this is an implementation of the paper: searching for best practices in retrieval-augmented generation (emnlp2024).
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 45. sci-m-wang/OpenCE
- **Source**: github  **URL**: https://github.com/sci-m-wang/OpenCE
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'sci-m-wang/OpenCE' (333 stars) provides an implementation of 'rag'. Description: opence (open context engineering): a community toolkit to implement, evaluate, and combine llm context strategies (rag, .
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 46. emarco177/documentation-helper
- **Source**: github  **URL**: https://github.com/emarco177/documentation-helper
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'emarco177/documentation-helper' (301 stars) provides an implementation of 'rag'. Description: reference implementation of a rag-based documentation helper using langchain, pinecone, and tavily...
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 47. daveebbelaar/pgvectorscale-rag-solution
- **Source**: github  **URL**: https://github.com/daveebbelaar/pgvectorscale-rag-solution
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'daveebbelaar/pgvectorscale-rag-solution' (264 stars) provides an implementation of 'rag'. Description: an implementation of pgvectorscale to a build powerful rag solutions..
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 48. ashleve/ActiveRagdoll
- **Source**: github  **URL**: https://github.com/ashleve/ActiveRagdoll
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'ashleve/ActiveRagdoll' (250 stars) provides an implementation of 'rag'. Description: from-scratch implementation of physically simulated character animation with proportional-integral-derivative controller.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 49. dwb2023/ragas-golden-dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/dwb2023/ragas-golden-dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'dwb2023/ragas-golden-dataset' (77 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 50. reglab/legal_rag_hallucinations
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/reglab/legal_rag_hallucinations
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'reglab/legal_rag_hallucinations' (39 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 51. Azzindani/ID_REG_MD_RAG
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Azzindani/ID_REG_MD_RAG
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Azzindani/ID_REG_MD_RAG' (75 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 52. s1arsky/Warhammer-Fantasy-Lexicanum-RAG_v1.12
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/s1arsky/Warhammer-Fantasy-Lexicanum-RAG_v1.12
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 's1arsky/Warhammer-Fantasy-Lexicanum-RAG_v1.12' (84 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 53. huggingartists/rage-against-the-machine
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/huggingartists/rage-against-the-machine
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'huggingartists/rage-against-the-machine' (69 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 54. hr16/Miwano-Rag
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/hr16/Miwano-Rag
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'hr16/Miwano-Rag' (24 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 55. raghuram13/autotrain-data-sentiment_analysis
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/raghuram13/autotrain-data-sentiment_analysis
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'raghuram13/autotrain-data-sentiment_analysis' (72 downloads) matched 'RAG' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 56. luozhouyang/question-answering-datasets
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/luozhouyang/question-answering-datasets
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'luozhouyang/question-answering-datasets' (56 downloads) matched 'question answering' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 57. RUCAIBox/Question-Answering
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/RUCAIBox/Question-Answering
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'RUCAIBox/Question-Answering' (41 downloads) matched 'question answering' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 58. open-source-metrics/visual-question-answering-checkpoint-downloads
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/open-source-metrics/visual-question-answering-checkpoint-downloads
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'open-source-metrics/visual-question-answering-checkpoint-downloads' (43 downloads) matched 'question answering' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 59. LangChainDatasets/question-answering-state-of-the-union
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/LangChainDatasets/question-answering-state-of-the-union
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'LangChainDatasets/question-answering-state-of-the-union' (61 downloads) matched 'question answering' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 60. nogyxo/question-answering-ukrainian-json-answers
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/nogyxo/question-answering-ukrainian-json-answers
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'nogyxo/question-answering-ukrainian-json-answers' (24 downloads) matched 'question answering' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 61. chenle015/OpenMP_Question_Answering
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/chenle015/OpenMP_Question_Answering
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'chenle015/OpenMP_Question_Answering' (36 downloads) matched 'question answering' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 62. zihanz/RetrievalQA
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/zihanz/RetrievalQA
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'zihanz/RetrievalQA' (32 downloads) matched 'retrieval QA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 63. aialt/RetrievalQA
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/aialt/RetrievalQA
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'aialt/RetrievalQA' (54 downloads) matched 'retrieval QA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 64. xiao-centml/rag-qa-retrieval
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/xiao-centml/rag-qa-retrieval
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'xiao-centml/rag-qa-retrieval' (27 downloads) matched 'retrieval QA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Parameter-Efficient Abstractive Question Answering over Tables or Text](https://doi.org/10.18653/v1/2022.dialdoc-1.5) | 2022 | Proceedings of the Second DialDoc Worksh | paper | 0.25 | strong |
| 2 | paper | [Enhancing yes/no question answering with weak supervision via extractive questio](https://doi.org/10.1007/s10489-023-04751-w) | 2023 | Applied Intelligence | paper | 0.25 | strong |
| 3 | paper | [MoQA: Benchmarking Multi-Type Open-Domain Question Answering](https://doi.org/10.18653/v1/2023.dialdoc-1.2) | 2023 | Proceedings of the Third DialDoc Worksho | benchmark | 0.25 | strong |
| 4 | paper | [Visual question answering system](https://doi.org/10.55248/gengpi.6.0825.3178) | 2025 | International Journal of Research Public | tool | 0.25 | strong |
| 5 | paper | [Question Answering Evaluation](https://doi.org/10.1007/978-3-031-16552-8_3) | 2022 | Question Answering over Text and Knowled | paper | 0.25 | strong |
| 6 | paper | [Question Answering over Text](https://doi.org/10.1007/978-3-031-16552-8_5) | 2022 | Question Answering over Text and Knowled | paper | 0.25 | strong |
| 7 | paper | [Question Answering in Real Applications](https://doi.org/10.1007/978-3-031-16552-8_8) | 2022 | Question Answering over Text and Knowled | paper | 0.25 | strong |
| 8 | paper | [Question Answering over Knowledge Base](https://doi.org/10.1007/978-3-031-16552-8_6) | 2022 | Question Answering over Text and Knowled | paper | 0.25 | strong |
| 9 | paper | [Future Directions of Question Answering](https://doi.org/10.1007/978-3-031-16552-8_9) | 2022 | Question Answering over Text and Knowled | paper | 0.25 | strong |
| 10 | paper | [Feature-Based Question Routing in Community Question Answering Platforms](https://doi.org/10.32920/24191931.v1) | 2023 |  | tool | 0.25 | strong |
| 11 | paper | [FAQ-Based Question Answering Systems with Query-Question and Query-Answer Simila](https://doi.org/10.5220/0012454800003636) | 2024 | Proceedings of the 16th International Co | tool | 0.25 | strong |
| 12 | paper | [QUESTION ANSWERING SYSTEM UPON UNIFIED LANGUAGE MODEL AND EVALUATING PERFORMANCE](https://doi.org/10.47344/sdubnts.v62i1.738) | 2024 | Suleyman Demirel University Bulletin Nat | dataset | 0.25 | strong |

### 1. Parameter-Efficient Abstractive Question Answering over Tables or Text
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2022.dialdoc-1.5
- **Year/Venue**: 2022 / Proceedings of the Second DialDoc Workshop on Document-grounded Dialogue and Conversational Question Answering
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Parameter-Efficient Abstractive Question Answering over Tables or Text' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. Enhancing yes/no question answering with weak supervision via extractive question answering
- **Source**: paper  **URL**: https://doi.org/10.1007/s10489-023-04751-w
- **Year/Venue**: 2023 / Applied Intelligence
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Enhancing yes/no question answering with weak supervision via extractive question answering' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. MoQA: Benchmarking Multi-Type Open-Domain Question Answering
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2023.dialdoc-1.2
- **Year/Venue**: 2023 / Proceedings of the Third DialDoc Workshop on Document-grounded Dialogue and Conversational Question Answering
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'MoQA: Benchmarking Multi-Type Open-Domain Question Answering' contributes a 'benchmark' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. Visual question answering system
- **Source**: paper  **URL**: https://doi.org/10.55248/gengpi.6.0825.3178
- **Year/Venue**: 2025 / International Journal of Research Publication and Reviews
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'Visual question answering system' contributes a 'tool' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. Question Answering Evaluation
- **Source**: paper  **URL**: https://doi.org/10.1007/978-3-031-16552-8_3
- **Year/Venue**: 2022 / Question Answering over Text and Knowledge Base
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Question Answering Evaluation' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. Question Answering over Text
- **Source**: paper  **URL**: https://doi.org/10.1007/978-3-031-16552-8_5
- **Year/Venue**: 2022 / Question Answering over Text and Knowledge Base
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Question Answering over Text' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. Question Answering in Real Applications
- **Source**: paper  **URL**: https://doi.org/10.1007/978-3-031-16552-8_8
- **Year/Venue**: 2022 / Question Answering over Text and Knowledge Base
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Question Answering in Real Applications' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Question Answering over Knowledge Base
- **Source**: paper  **URL**: https://doi.org/10.1007/978-3-031-16552-8_6
- **Year/Venue**: 2022 / Question Answering over Text and Knowledge Base
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Question Answering over Knowledge Base' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. Future Directions of Question Answering
- **Source**: paper  **URL**: https://doi.org/10.1007/978-3-031-16552-8_9
- **Year/Venue**: 2022 / Question Answering over Text and Knowledge Base
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Future Directions of Question Answering' contributes a 'paper' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Feature-Based Question Routing in Community Question Answering Platforms
- **Source**: paper  **URL**: https://doi.org/10.32920/24191931.v1
- **Year/Venue**: 2023 / n/a
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'Feature-Based Question Routing in Community Question Answering Platforms' contributes a 'tool' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. FAQ-Based Question Answering Systems with Query-Question and Query-Answer Similarity
- **Source**: paper  **URL**: https://doi.org/10.5220/0012454800003636
- **Year/Venue**: 2024 / Proceedings of the 16th International Conference on Agents and Artificial Intelligence
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.25: paper titled 'FAQ-Based Question Answering Systems with Query-Question and Query-Answer Similarity' contributes a 'tool' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. QUESTION ANSWERING SYSTEM UPON UNIFIED LANGUAGE MODEL AND EVALUATING PERFORMANCE OF DATASETS
- **Source**: paper  **URL**: https://doi.org/10.47344/sdubnts.v62i1.738
- **Year/Venue**: 2024 / Suleyman Demirel University Bulletin Natural and Technical Sciences
- **Contribution type**: dataset
- **Why it overlaps**: Relevance 0.25: paper titled 'QUESTION ANSWERING SYSTEM UPON UNIFIED LANGUAGE MODEL AND EVALUATING PERFORMANCE OF DATASETS' contributes a 'dataset' matching target artifact 'framework'. Matched keywords: kw:title:question answering.
- **How we differ**: Our proposed work focuses specifically on 'RAG for question answering [NEGATIVE_CONTROL]'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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

1. **GO blocked by artifact overlap** — 15 direct artifacts, artifact_diff=`weak`.
2. Complete the Artifact Differentiator Checklist above.
3. If differentiator becomes clear (≥ 3 checklist items): update this JSON manually and re-run gate.
