# Existing Work Report — T01: Cross-judge agreement on long-context QA

> ⚠️ **DIFFERENTIATOR REQUIRED** — paper_direct=0, artifact_direct=3; paper_strength=`strong`, artifact_strength=`moderate`.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 1 |
| HuggingFace direct artifacts | 2 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 3 |
| Artifact diff strength | `moderate` |
| Partial overlaps (total) | 13 |
| Adjacent | 1 |
| Total findings | 17 |
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
| 1 | github | [reacher-z/ClawBench](https://github.com/reacher-z/ClawBench) |  | GitHub | benchmark | 196 | moderate |
| 2 | huggingface | [potsawee/chatbot-arena-llm-judges](https://huggingface.co/datasets/potsawee/chatbot-arena-llm-judges) |  | HuggingFace | dataset | 170 | moderate |
| 3 | huggingface | [Abzu/long-context-qa-df](https://huggingface.co/datasets/Abzu/long-context-qa-df) |  | HuggingFace | dataset | 111 | moderate |

### 1. reacher-z/ClawBench
- **Source**: github  **URL**: https://github.com/reacher-z/ClawBench
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'reacher-z/ClawBench' (196 stars) provides an implementation of 'llm judge'. Description: open-source benchmark for browser ai agents on 153 everyday online tasks across 144 live websites. 5-layer recording + d.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. potsawee/chatbot-arena-llm-judges
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/potsawee/chatbot-arena-llm-judges
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'potsawee/chatbot-arena-llm-judges' (170 downloads) matched 'LLM judge' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. Abzu/long-context-qa-df
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Abzu/long-context-qa-df
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Abzu/long-context-qa-df' (111 downloads) matched 'long context QA' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box,](https://doi.org/10.48550/arXiv.2504.19254) | 2025 | Trans. Mach. Learn. Res. | paper | 0.5 | moderate |
| 2 | paper | [Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human ](https://doi.org/10.48550/arXiv.2510.09738) | 2025 | arXiv.org | empirical | 0.5 | moderate |
| 3 | paper | [Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Ope](https://doi.org/10.48550/arXiv.2602.05125) | 2026 | arXiv.org | paper | 0.5 | moderate |
| 4 | paper | [Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations](https://doi.org/10.48550/arXiv.2510.11822) | 2025 | arXiv.org | paper | 0.5 | moderate |
| 5 | paper | [Ask a Strong LLM Judge when Your Reward Model is Uncertain](https://doi.org/10.48550/arXiv.2510.20369) | 2025 | arXiv.org | paper | 0.5 | moderate |
| 6 | paper | Tuning LLM Judge Design Decisions for 1/1000 of the Cost | 2025 | International Conference on Machine Lear | paper | 0.5 | moderate |
| 7 | paper | [Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating na](https://doi.org/10.48550/arXiv.2504.02867) | 2025 | arXiv.org | paper | 0.5 | moderate |
| 8 | paper | [When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silentl](https://doi.org/10.48550/arXiv.2509.20293) | 2025 | arXiv.org | benchmark | 0.5 | moderate |
| 9 | paper | [Auto-Prompt Ensemble for LLM Judge](https://doi.org/10.48550/arXiv.2510.06538) | 2025 | arXiv.org | paper | 0.5 | moderate |
| 10 | paper | [DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation](https://doi.org/10.48550/arXiv.2601.22230) | 2026 | arXiv.org | paper | 0.5 | moderate |
| 11 | paper | When LLM Judge Scores Look Good but Best-of-N Decisions Fail | 2026 |  | paper | 0.5 | moderate |
| 12 | github | [baaivision/JudgeLM](https://github.com/baaivision/JudgeLM) |  | GitHub | tool | 429 | moderate |
| 13 | github | [UW-Madison-Lee-Lab/LLM-judge-reporting](https://github.com/UW-Madison-Lee-Lab/LLM-judge-reporting) |  | GitHub | tool | 77 | moderate |

### 1. Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ensemble Scorers
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.19254
- **Year/Venue**: 2025 / Trans. Mach. Learn. Res.
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ense' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.09738
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.50: paper titled 'Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement' contributes a 'empirical' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2602.05125
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.11822
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. Ask a Strong LLM Judge when Your Reward Model is Uncertain
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.20369
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Ask a Strong LLM Judge when Your Reward Model is Uncertain' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. Tuning LLM Judge Design Decisions for 1/1000 of the Cost
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Tuning LLM Judge Design Decisions for 1/1000 of the Cost' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language generation applications
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.02867
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language gener' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2509.20293
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity' contributes a 'benchmark' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. Auto-Prompt Ensemble for LLM Judge
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.06538
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Auto-Prompt Ensemble for LLM Judge' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2601.22230
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. When LLM Judge Scores Look Good but Best-of-N Decisions Fail
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'When LLM Judge Scores Look Good but Best-of-N Decisions Fail' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. baaivision/JudgeLM
- **Source**: github  **URL**: https://github.com/baaivision/JudgeLM
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'baaivision/JudgeLM' (429 stars) provides an implementation of 'llm judge'. Description: [iclr 2025 spotlight] an open-sourced llm judge for evaluating llm-generated answers..
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 13. UW-Madison-Lee-Lab/LLM-judge-reporting
- **Source**: github  **URL**: https://github.com/UW-Madison-Lee-Lab/LLM-judge-reporting
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'UW-Madison-Lee-Lab/LLM-judge-reporting' (77 stars) provides an implementation of 'llm judge'. Description: a simple plug-in framework that corrects bias and computes confidence intervals in reporting llm-as-a-judge evaluation, .
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Expect the Unexpected: FailSafe Long Context QA for Finance](https://doi.org/10.48550/arXiv.2502.06329) | 2025 | arXiv.org | paper | 0.25 | strong |

### 1. Expect the Unexpected: FailSafe Long Context QA for Finance
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2502.06329
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Expect the Unexpected: FailSafe Long Context QA for Finance' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:long context qa.
- **How we differ**: Our proposed work focuses specifically on 'Cross-judge agreement on long-context QA'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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
