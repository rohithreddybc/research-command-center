# Existing Work Report — T07: Judge robustness to candidate-side prompt injection

> ⚠️ **ARTIFACT DIFFERENTIATOR REQUIRED** — 12 direct artifact(s) (GitHub=1, HF=11, PWC=0), no peer-reviewed paper overlap. artifact_diff_strength=`moderate`. Our peer-reviewed contribution is inherently different, but must be explicit.

> 📌 **Note (artifact-only overlap):** Academic/paper overlap appears low, but artifact overlap is high (12 direct artifacts). This topic may still be publishable — a peer-reviewed benchmark/protocol with a clear domain or methodological focus is inherently differentiated from GitHub repos and HuggingFace datasets. Explicitly state: (1) peer-reviewed systematic protocol vs existing repos; (2) specific domain/use-case vs general artifacts; (3) evaluation harness + reproducibility package vs raw data.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 1 |
| HuggingFace direct artifacts | 11 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 12 |
| Artifact diff strength | `moderate` |
| Partial overlaps (total) | 29 |
| Adjacent | 13 |
| Total findings | 54 |
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
| 1 | github | [reacher-z/ClawBench](https://github.com/reacher-z/ClawBench) |  | GitHub | benchmark | 196 | moderate |
| 2 | huggingface | [potsawee/chatbot-arena-llm-judges](https://huggingface.co/datasets/potsawee/chatbot-arena-llm-judges) |  | HuggingFace | dataset | 170 | moderate |
| 3 | huggingface | [deepset/prompt-injections](https://huggingface.co/datasets/deepset/prompt-injections) |  | HuggingFace | dataset | 5438 | moderate |
| 4 | huggingface | [rogue-security/prompt-injections-benchmark](https://huggingface.co/datasets/rogue-security/prompt-injections-benchmark) |  | HuggingFace | dataset | 933 | moderate |
| 5 | huggingface | [JasperLS/prompt-injections](https://huggingface.co/datasets/JasperLS/prompt-injections) |  | HuggingFace | dataset | 765 | moderate |
| 6 | huggingface | [Lakera/mosscap_prompt_injection](https://huggingface.co/datasets/Lakera/mosscap_prompt_injection) |  | HuggingFace | dataset | 496 | moderate |
| 7 | huggingface | [yanismiraoui/prompt_injections](https://huggingface.co/datasets/yanismiraoui/prompt_injections) |  | HuggingFace | dataset | 403 | moderate |
| 8 | huggingface | [reshabhs/SPML_Chatbot_Prompt_Injection](https://huggingface.co/datasets/reshabhs/SPML_Chatbot_Prompt_Injection) |  | HuggingFace | dataset | 1172 | moderate |
| 9 | huggingface | [Albertmade/prompt-injection](https://huggingface.co/datasets/Albertmade/prompt-injection) |  | HuggingFace | dataset | 108 | moderate |
| 10 | huggingface | [xTRam1/safe-guard-prompt-injection](https://huggingface.co/datasets/xTRam1/safe-guard-prompt-injection) |  | HuggingFace | dataset | 2171 | moderate |
| 11 | huggingface | [jayavibhav/prompt-injection](https://huggingface.co/datasets/jayavibhav/prompt-injection) |  | HuggingFace | dataset | 396 | moderate |
| 12 | huggingface | [jayavibhav/prompt-injection-safety](https://huggingface.co/datasets/jayavibhav/prompt-injection-safety) |  | HuggingFace | dataset | 358 | moderate |

### 1. reacher-z/ClawBench
- **Source**: github  **URL**: https://github.com/reacher-z/ClawBench
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'reacher-z/ClawBench' (196 stars) provides an implementation of 'llm judge'. Description: open-source benchmark for browser ai agents on 153 everyday online tasks across 144 live websites. 5-layer recording + d.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. potsawee/chatbot-arena-llm-judges
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/potsawee/chatbot-arena-llm-judges
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'potsawee/chatbot-arena-llm-judges' (170 downloads) matched 'LLM judge' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. deepset/prompt-injections
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/deepset/prompt-injections
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'deepset/prompt-injections' (5,438 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. rogue-security/prompt-injections-benchmark
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/rogue-security/prompt-injections-benchmark
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'rogue-security/prompt-injections-benchmark' (933 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. JasperLS/prompt-injections
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/JasperLS/prompt-injections
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'JasperLS/prompt-injections' (765 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. Lakera/mosscap_prompt_injection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Lakera/mosscap_prompt_injection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Lakera/mosscap_prompt_injection' (496 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. yanismiraoui/prompt_injections
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/yanismiraoui/prompt_injections
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'yanismiraoui/prompt_injections' (403 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. reshabhs/SPML_Chatbot_Prompt_Injection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/reshabhs/SPML_Chatbot_Prompt_Injection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'reshabhs/SPML_Chatbot_Prompt_Injection' (1,172 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. Albertmade/prompt-injection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Albertmade/prompt-injection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Albertmade/prompt-injection' (108 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. xTRam1/safe-guard-prompt-injection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/xTRam1/safe-guard-prompt-injection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'xTRam1/safe-guard-prompt-injection' (2,171 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. jayavibhav/prompt-injection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/jayavibhav/prompt-injection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'jayavibhav/prompt-injection' (396 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. jayavibhav/prompt-injection-safety
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/jayavibhav/prompt-injection-safety
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'jayavibhav/prompt-injection-safety' (358 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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
| 12 | paper | [Prompt Injection attack against LLM-integrated Applications](https://doi.org/10.48550/arXiv.2306.05499) | 2023 | arXiv.org | paper | 0.375 | moderate |
| 13 | paper | [Optimization-based Prompt Injection Attack to LLM-as-a-Judge](https://doi.org/10.1145/3658644.3690291) | 2024 | Conference on Computer and Communication | paper | 0.375 | moderate |
| 14 | paper | [Prompt Injection Attack to Tool Selection in LLM Agents](https://doi.org/10.48550/arXiv.2504.19793) | 2025 | arXiv.org | tool | 0.375 | moderate |
| 15 | paper | [Defense Against Prompt Injection Attack by Leveraging Attack Techniques](https://doi.org/10.48550/arXiv.2411.00459) | 2024 | Annual Meeting of the Association for Co | paper | 0.375 | moderate |
| 16 | paper | [WebInject: Prompt Injection Attack to Web Agents](https://doi.org/10.18653/v1/2025.emnlp-main.104) | 2025 | Conference on Empirical Methods in Natur | paper | 0.375 | moderate |
| 17 | paper | [Signed-prompt: A new approach to prevent prompt injection attacks against LLM-In](https://doi.org/10.1063/5.0222987) | 2024 | AIP Conference Proceedings | paper | 0.375 | moderate |
| 18 | paper | [To Protect the LLM Agent Against the Prompt Injection Attack with Polymorphic Pr](https://doi.org/10.1109/DSN-S65789.2025.00037) | 2025 | 2025 55th Annual IEEE/IFIP International | paper | 0.375 | moderate |
| 19 | paper | [TopicAttack: An Indirect Prompt Injection Attack via Topic Transition](https://doi.org/10.48550/arXiv.2507.13686) | 2025 | Conference on Empirical Methods in Natur | paper | 0.375 | moderate |
| 20 | paper | [Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Acces](https://doi.org/10.48550/arXiv.2507.14799) | 2025 | arXiv.org | paper | 0.375 | moderate |
| 21 | paper | [Mind Mapping Prompt Injection: Visual Prompt Injection Attacks in Modern Large L](https://doi.org/10.3390/electronics14101907) | 2025 | Electronics | paper | 0.375 | moderate |
| 22 | paper | [Enhancing Security in Large Language Models: A Comprehensive Review of Prompt In](https://doi.org/10.36227/techrxiv.172954263.32914470/v1) | 2024 |  | survey | 0.375 | moderate |
| 23 | paper | [REAL TIME AI DEFENSE AGAINST PROMPT INJECTION ATTACKS](https://doi.org/10.37962/icydd/2025/23-24) | 2025 | 2nd International Conference on Cybersec | paper | 0.375 | moderate |
| 24 | paper | [Reconstruction-Based Prompt Generation Algorithm for Prompt Injection Attacks](https://doi.org/10.1109/aann66429.2025.11257661) | 2025 | 2025 5th International Conference on Adv | paper | 0.375 | moderate |
| 25 | paper | [Prompt Injection Attacks on LLM-Based Spam Filters](https://doi.org/10.15611/2025.07.4.02) | 2025 | Informatyka w biznesie | paper | 0.375 | moderate |
| 26 | github | [baaivision/JudgeLM](https://github.com/baaivision/JudgeLM) |  | GitHub | tool | 429 | moderate |
| 27 | github | [UW-Madison-Lee-Lab/LLM-judge-reporting](https://github.com/UW-Madison-Lee-Lab/LLM-judge-reporting) |  | GitHub | tool | 77 | moderate |
| 28 | huggingface | [prodnull/prompt-injection-repo-dataset](https://huggingface.co/datasets/prodnull/prompt-injection-repo-dataset) |  | HuggingFace | dataset | 58 | moderate |
| 29 | huggingface | [beratcmn/turkish-prompt-injections](https://huggingface.co/datasets/beratcmn/turkish-prompt-injections) |  | HuggingFace | dataset | 51 | moderate |

### 1. Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ensemble Scorers
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.19254
- **Year/Venue**: 2025 / Trans. Mach. Learn. Res.
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ense' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.09738
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.50: paper titled 'Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement' contributes a 'empirical' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2602.05125
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.11822
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. Ask a Strong LLM Judge when Your Reward Model is Uncertain
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.20369
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Ask a Strong LLM Judge when Your Reward Model is Uncertain' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. Tuning LLM Judge Design Decisions for 1/1000 of the Cost
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Tuning LLM Judge Design Decisions for 1/1000 of the Cost' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language generation applications
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.02867
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language gener' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2509.20293
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.50: paper titled 'When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity' contributes a 'benchmark' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. Auto-Prompt Ensemble for LLM Judge
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.06538
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Auto-Prompt Ensemble for LLM Judge' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2601.22230
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. When LLM Judge Scores Look Good but Best-of-N Decisions Fail
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'When LLM Judge Scores Look Good but Best-of-N Decisions Fail' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. Prompt Injection attack against LLM-integrated Applications
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2306.05499
- **Year/Venue**: 2023 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Prompt Injection attack against LLM-integrated Applications' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 13. Optimization-based Prompt Injection Attack to LLM-as-a-Judge
- **Source**: paper  **URL**: https://doi.org/10.1145/3658644.3690291
- **Year/Venue**: 2024 / Conference on Computer and Communications Security
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Optimization-based Prompt Injection Attack to LLM-as-a-Judge' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 14. Prompt Injection Attack to Tool Selection in LLM Agents
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.19793
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.38: paper titled 'Prompt Injection Attack to Tool Selection in LLM Agents' contributes a 'tool' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 15. Defense Against Prompt Injection Attack by Leveraging Attack Techniques
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2411.00459
- **Year/Venue**: 2024 / Annual Meeting of the Association for Computational Linguistics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Defense Against Prompt Injection Attack by Leveraging Attack Techniques' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 16. WebInject: Prompt Injection Attack to Web Agents
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2025.emnlp-main.104
- **Year/Venue**: 2025 / Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'WebInject: Prompt Injection Attack to Web Agents' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 17. Signed-prompt: A new approach to prevent prompt injection attacks against LLM-Integrated applications
- **Source**: paper  **URL**: https://doi.org/10.1063/5.0222987
- **Year/Venue**: 2024 / AIP Conference Proceedings
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Signed-prompt: A new approach to prevent prompt injection attacks against LLM-Integrated application' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 18. To Protect the LLM Agent Against the Prompt Injection Attack with Polymorphic Prompt
- **Source**: paper  **URL**: https://doi.org/10.1109/DSN-S65789.2025.00037
- **Year/Venue**: 2025 / 2025 55th Annual IEEE/IFIP International Conference on Dependable Systems and Networks - Supplemental Volume (DSN-S)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'To Protect the LLM Agent Against the Prompt Injection Attack with Polymorphic Prompt' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 19. TopicAttack: An Indirect Prompt Injection Attack via Topic Transition
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2507.13686
- **Year/Venue**: 2025 / Conference on Empirical Methods in Natural Language Processing
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'TopicAttack: An Indirect Prompt Injection Attack via Topic Transition' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 20. Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Accessibility Tree
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2507.14799
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Accessibility Tree' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 21. Mind Mapping Prompt Injection: Visual Prompt Injection Attacks in Modern Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.3390/electronics14101907
- **Year/Venue**: 2025 / Electronics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Mind Mapping Prompt Injection: Visual Prompt Injection Attacks in Modern Large Language Models' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 22. Enhancing Security in Large Language Models: A Comprehensive Review of Prompt Injection Attacks and Defenses
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.172954263.32914470/v1
- **Year/Venue**: 2024 / n/a
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.38: paper titled 'Enhancing Security in Large Language Models: A Comprehensive Review of Prompt Injection Attacks and ' contributes a 'survey' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 23. REAL TIME AI DEFENSE AGAINST PROMPT INJECTION ATTACKS
- **Source**: paper  **URL**: https://doi.org/10.37962/icydd/2025/23-24
- **Year/Venue**: 2025 / 2nd International Conference on Cybersecurity and Digital Defense (ICyDD)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'REAL TIME AI DEFENSE AGAINST PROMPT INJECTION ATTACKS' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 24. Reconstruction-Based Prompt Generation Algorithm for Prompt Injection Attacks
- **Source**: paper  **URL**: https://doi.org/10.1109/aann66429.2025.11257661
- **Year/Venue**: 2025 / 2025 5th International Conference on Advanced Algorithms and Neural Networks (AANN)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Reconstruction-Based Prompt Generation Algorithm for Prompt Injection Attacks' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 25. Prompt Injection Attacks on LLM-Based Spam Filters
- **Source**: paper  **URL**: https://doi.org/10.15611/2025.07.4.02
- **Year/Venue**: 2025 / Informatyka w biznesie
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.38: paper titled 'Prompt Injection Attacks on LLM-Based Spam Filters' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:title:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 26. baaivision/JudgeLM
- **Source**: github  **URL**: https://github.com/baaivision/JudgeLM
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'baaivision/JudgeLM' (429 stars) provides an implementation of 'llm judge'. Description: [iclr 2025 spotlight] an open-sourced llm judge for evaluating llm-generated answers..
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 27. UW-Madison-Lee-Lab/LLM-judge-reporting
- **Source**: github  **URL**: https://github.com/UW-Madison-Lee-Lab/LLM-judge-reporting
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'UW-Madison-Lee-Lab/LLM-judge-reporting' (77 stars) provides an implementation of 'llm judge'. Description: a simple plug-in framework that corrects bias and computes confidence intervals in reporting llm-as-a-judge evaluation, .
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 28. prodnull/prompt-injection-repo-dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/prodnull/prompt-injection-repo-dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'prodnull/prompt-injection-repo-dataset' (58 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 29. beratcmn/turkish-prompt-injections
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/beratcmn/turkish-prompt-injections
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'beratcmn/turkish-prompt-injections' (51 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Evaluating Hybrid Guardrail Architectures for Prompt Injection Defense in Large ](https://doi.org/10.2139/ssrn.6246379) | 2026 |  | paper | 0.3 | strong |
| 2 | paper | [Adversarial Robustness for Machine Learning](https://doi.org/10.1016/c2020-0-01078-9) | 2023 |  | paper | 0.25 | strong |
| 3 | paper | [Prompt Injection](https://doi.org/10.61608/9783775757027-002) | 2024 | Worldbuilding | paper | 0.25 | strong |
| 4 | paper | [An Evaluation of the Safety of ChatGPT with Malicious Prompt Injection](https://doi.org/10.21203/rs.3.rs-4487194/v1) | 2024 |  | paper | 0.25 | strong |
| 5 | paper | [Adversarial robustness of beyond neural network models](https://doi.org/10.1016/b978-0-12-824020-5.00027-2) | 2023 | Adversarial Robustness for Machine Learn | paper | 0.25 | strong |
| 6 | paper | [Adversarial robustness in meta-learning and contrastive learning](https://doi.org/10.1016/b978-0-12-824020-5.00028-4) | 2023 | Adversarial Robustness for Machine Learn | paper | 0.25 | strong |
| 7 | paper | [Intent Vectoring: Black-Box Prompt Injection Detection via Semantic Trajectory M](https://doi.org/10.2139/ssrn.6280858) | 2026 |  | paper | 0.25 | strong |
| 8 | paper | [Dynamic Moving Target Defense for Mitigating Targeted LLM Prompt Injection](https://doi.org/10.36227/techrxiv.171822345.56781952/v1) | 2024 |  | paper | 0.25 | strong |
| 9 | paper | [Feedback-Guided Prompt Injection Defense in Retrieval-Augmented Text-to-Cypher G](https://doi.org/10.2139/ssrn.5669662) | 2025 |  | paper | 0.25 | strong |
| 10 | paper | [Secure Artificial Intelligence (SAI): A Dual-layer defence model against prompt ](https://doi.org/10.36948/ijfmr.2025.v07i01.35371) | 2025 | International Journal For Multidisciplin | paper | 0.25 | strong |
| 11 | paper | [Feature Augmentation for Adversarial Robustness](https://doi.org/10.36227/techrxiv.19609623.v1) | 2022 |  | paper | 0.25 | strong |
| 12 | paper | [CAFI: Copula-based Adversarial Feature Index for Adversarial Robustness Analysis](https://doi.org/10.36227/techrxiv.174140757.76329713/v1) | 2025 |  | empirical | 0.25 | strong |
| 13 | paper | [On the Adversarial Robustness of Subspace Learning](https://doi.org/10.1007/978-3-031-16375-3_4) | 2022 | Wireless Networks | paper | 0.25 | strong |

### 1. Evaluating Hybrid Guardrail Architectures for Prompt Injection Defense in Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6246379
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.30: paper titled 'Evaluating Hybrid Guardrail Architectures for Prompt Injection Defense in Large Language Models' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection|syn:abstract:injection attack.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. Adversarial Robustness for Machine Learning
- **Source**: paper  **URL**: https://doi.org/10.1016/c2020-0-01078-9
- **Year/Venue**: 2023 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Adversarial Robustness for Machine Learning' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:adversarial robustness.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. Prompt Injection
- **Source**: paper  **URL**: https://doi.org/10.61608/9783775757027-002
- **Year/Venue**: 2024 / Worldbuilding
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Prompt Injection' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. An Evaluation of the Safety of ChatGPT with Malicious Prompt Injection
- **Source**: paper  **URL**: https://doi.org/10.21203/rs.3.rs-4487194/v1
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'An Evaluation of the Safety of ChatGPT with Malicious Prompt Injection' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. Adversarial robustness of beyond neural network models
- **Source**: paper  **URL**: https://doi.org/10.1016/b978-0-12-824020-5.00027-2
- **Year/Venue**: 2023 / Adversarial Robustness for Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Adversarial robustness of beyond neural network models' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:adversarial robustness.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. Adversarial robustness in meta-learning and contrastive learning
- **Source**: paper  **URL**: https://doi.org/10.1016/b978-0-12-824020-5.00028-4
- **Year/Venue**: 2023 / Adversarial Robustness for Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Adversarial robustness in meta-learning and contrastive learning' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:adversarial robustness.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. Intent Vectoring: Black-Box Prompt Injection Detection via Semantic Trajectory Monitoring
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6280858
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Intent Vectoring: Black-Box Prompt Injection Detection via Semantic Trajectory Monitoring' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Dynamic Moving Target Defense for Mitigating Targeted LLM Prompt Injection
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.171822345.56781952/v1
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Dynamic Moving Target Defense for Mitigating Targeted LLM Prompt Injection' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. Feedback-Guided Prompt Injection Defense in Retrieval-Augmented Text-to-Cypher Generation
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.5669662
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Feedback-Guided Prompt Injection Defense in Retrieval-Augmented Text-to-Cypher Generation' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Secure Artificial Intelligence (SAI): A Dual-layer defence model against prompt injection and prompt poisoning attacks
- **Source**: paper  **URL**: https://doi.org/10.36948/ijfmr.2025.v07i01.35371
- **Year/Venue**: 2025 / International Journal For Multidisciplinary Research
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Secure Artificial Intelligence (SAI): A Dual-layer defence model against prompt injection and prompt' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. Feature Augmentation for Adversarial Robustness
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.19609623.v1
- **Year/Venue**: 2022 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Feature Augmentation for Adversarial Robustness' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:adversarial robustness.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. CAFI: Copula-based Adversarial Feature Index for Adversarial Robustness Analysis
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.174140757.76329713/v1
- **Year/Venue**: 2025 / n/a
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'CAFI: Copula-based Adversarial Feature Index for Adversarial Robustness Analysis' contributes a 'empirical' matching target artifact 'benchmark'. Matched keywords: kw:title:adversarial robustness.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. On the Adversarial Robustness of Subspace Learning
- **Source**: paper  **URL**: https://doi.org/10.1007/978-3-031-16375-3_4
- **Year/Venue**: 2022 / Wireless Networks
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'On the Adversarial Robustness of Subspace Learning' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:adversarial robustness.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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

1. Complete the Artifact Differentiator Checklist above (12 artifacts found).
2. This topic can proceed to GO if artifact differentiator is articulated explicitly.
3. Write one paragraph for §6 verification log explaining differentiation from top artifacts.
