# Existing Work Report — T07_N1: Judge robustness to candidate-side prompt injection — noise-pruned

> ⚠️ **ARTIFACT DIFFERENTIATOR REQUIRED** — 25 direct artifact(s) (GitHub=5, HF=20, PWC=0), no peer-reviewed paper overlap. artifact_diff_strength=`moderate`. Our peer-reviewed contribution is inherently different, but must be explicit.

> 📌 **Note (artifact-only overlap):** Academic/paper overlap appears low, but artifact overlap is high (25 direct artifacts). This topic may still be publishable — a peer-reviewed benchmark/protocol with a clear domain or methodological focus is inherently differentiated from GitHub repos and HuggingFace datasets. Explicitly state: (1) peer-reviewed systematic protocol vs existing repos; (2) specific domain/use-case vs general artifacts; (3) evaluation harness + reproducibility package vs raw data.

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 5 |
| HuggingFace direct artifacts | 20 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 25 |
| Artifact diff strength | `moderate` |
| Partial overlaps (total) | 24 |
| Adjacent | 11 |
| Total findings | 60 |
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
| 1 | github | [liu00222/Open-Prompt-Injection](https://github.com/liu00222/Open-Prompt-Injection) |  | GitHub | benchmark | 438 | moderate |
| 2 | github | [lakeraai/pint-benchmark](https://github.com/lakeraai/pint-benchmark) |  | GitHub | benchmark | 184 | moderate |
| 3 | github | [microsoft/BIPIA](https://github.com/microsoft/BIPIA) |  | GitHub | benchmark | 124 | moderate |
| 4 | github | [lucija8320nhung4/HacxGPT](https://github.com/lucija8320nhung4/HacxGPT) |  | GitHub | tool | 921 | moderate |
| 5 | github | [ReversecLabs/spikee](https://github.com/ReversecLabs/spikee) |  | GitHub | tool | 182 | moderate |
| 6 | huggingface | [deepset/prompt-injections](https://huggingface.co/datasets/deepset/prompt-injections) |  | HuggingFace | dataset | 5438 | moderate |
| 7 | huggingface | [rogue-security/prompt-injections-benchmark](https://huggingface.co/datasets/rogue-security/prompt-injections-benchmark) |  | HuggingFace | dataset | 933 | moderate |
| 8 | huggingface | [JasperLS/prompt-injections](https://huggingface.co/datasets/JasperLS/prompt-injections) |  | HuggingFace | dataset | 765 | moderate |
| 9 | huggingface | [Lakera/mosscap_prompt_injection](https://huggingface.co/datasets/Lakera/mosscap_prompt_injection) |  | HuggingFace | dataset | 496 | moderate |
| 10 | huggingface | [yanismiraoui/prompt_injections](https://huggingface.co/datasets/yanismiraoui/prompt_injections) |  | HuggingFace | dataset | 403 | moderate |
| 11 | huggingface | [reshabhs/SPML_Chatbot_Prompt_Injection](https://huggingface.co/datasets/reshabhs/SPML_Chatbot_Prompt_Injection) |  | HuggingFace | dataset | 1172 | moderate |
| 12 | huggingface | [Albertmade/prompt-injection](https://huggingface.co/datasets/Albertmade/prompt-injection) |  | HuggingFace | dataset | 108 | moderate |
| 13 | huggingface | [xTRam1/safe-guard-prompt-injection](https://huggingface.co/datasets/xTRam1/safe-guard-prompt-injection) |  | HuggingFace | dataset | 2171 | moderate |
| 14 | huggingface | [jayavibhav/prompt-injection](https://huggingface.co/datasets/jayavibhav/prompt-injection) |  | HuggingFace | dataset | 396 | moderate |
| 15 | huggingface | [jayavibhav/prompt-injection-safety](https://huggingface.co/datasets/jayavibhav/prompt-injection-safety) |  | HuggingFace | dataset | 358 | moderate |
| 16 | huggingface | [potsawee/chatbot-arena-llm-judges](https://huggingface.co/datasets/potsawee/chatbot-arena-llm-judges) |  | HuggingFace | dataset | 170 | moderate |
| 17 | huggingface | [rubend18/ChatGPT-Jailbreak-Prompts](https://huggingface.co/datasets/rubend18/ChatGPT-Jailbreak-Prompts) |  | HuggingFace | dataset | 2494 | moderate |
| 18 | huggingface | [llm-semantic-router/jailbreak-detection-dataset](https://huggingface.co/datasets/llm-semantic-router/jailbreak-detection-dataset) |  | HuggingFace | dataset | 322 | moderate |
| 19 | huggingface | [deadbits/vigil-jailbreak-ada-002](https://huggingface.co/datasets/deadbits/vigil-jailbreak-ada-002) |  | HuggingFace | dataset | 114 | moderate |
| 20 | huggingface | [deadbits/vigil-jailbreak-all-MiniLM-L6-v2](https://huggingface.co/datasets/deadbits/vigil-jailbreak-all-MiniLM-L6-v2) |  | HuggingFace | dataset | 113 | moderate |
| 21 | huggingface | [jackhhao/jailbreak-classification](https://huggingface.co/datasets/jackhhao/jailbreak-classification) |  | HuggingFace | dataset | 3236 | moderate |
| 22 | huggingface | [JailbreakV-28K/JailBreakV-28k](https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k) |  | HuggingFace | dataset | 3005 | moderate |
| 23 | huggingface | [JailbreakBench/JBB-Behaviors](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors) |  | HuggingFace | dataset | 30227 | moderate |
| 24 | huggingface | [walledai/JailbreakBench](https://huggingface.co/datasets/walledai/JailbreakBench) |  | HuggingFace | dataset | 963 | moderate |
| 25 | huggingface | [walledai/JailbreakHub](https://huggingface.co/datasets/walledai/JailbreakHub) |  | HuggingFace | dataset | 873 | moderate |

### 1. liu00222/Open-Prompt-Injection
- **Source**: github  **URL**: https://github.com/liu00222/Open-Prompt-Injection
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'liu00222/Open-Prompt-Injection' (438 stars) provides an implementation of 'prompt injection'. Description: this repository provides a benchmark for prompt injection attacks and defenses in llms.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. lakeraai/pint-benchmark
- **Source**: github  **URL**: https://github.com/lakeraai/pint-benchmark
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'lakeraai/pint-benchmark' (184 stars) provides an implementation of 'prompt injection'. Description: a benchmark for prompt injection detection systems..
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. microsoft/BIPIA
- **Source**: github  **URL**: https://github.com/microsoft/BIPIA
- **Year/Venue**:  / GitHub
- **Contribution type**: benchmark
- **Why it overlaps**: GitHub repo 'microsoft/BIPIA' (124 stars) provides an implementation of 'prompt injection'. Description: a benchmark for evaluating the robustness of llms and defenses to indirect prompt injection attacks..
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. lucija8320nhung4/HacxGPT
- **Source**: github  **URL**: https://github.com/lucija8320nhung4/HacxGPT
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'lucija8320nhung4/HacxGPT' (921 stars) provides an implementation of 'prompt injection'. Description: hacxgpt cli — open-source command-line interface for unrestricted ai model access with multi-provider support, prompt in.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. ReversecLabs/spikee
- **Source**: github  **URL**: https://github.com/ReversecLabs/spikee
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'ReversecLabs/spikee' (182 stars) provides an implementation of 'prompt injection'. Description: simple prompt injection kit for evaluation and exploitation.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. deepset/prompt-injections
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/deepset/prompt-injections
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'deepset/prompt-injections' (5,438 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. rogue-security/prompt-injections-benchmark
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/rogue-security/prompt-injections-benchmark
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'rogue-security/prompt-injections-benchmark' (933 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. JasperLS/prompt-injections
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/JasperLS/prompt-injections
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'JasperLS/prompt-injections' (765 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. Lakera/mosscap_prompt_injection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Lakera/mosscap_prompt_injection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Lakera/mosscap_prompt_injection' (496 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. yanismiraoui/prompt_injections
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/yanismiraoui/prompt_injections
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'yanismiraoui/prompt_injections' (403 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. reshabhs/SPML_Chatbot_Prompt_Injection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/reshabhs/SPML_Chatbot_Prompt_Injection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'reshabhs/SPML_Chatbot_Prompt_Injection' (1,172 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. Albertmade/prompt-injection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Albertmade/prompt-injection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Albertmade/prompt-injection' (108 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 13. xTRam1/safe-guard-prompt-injection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/xTRam1/safe-guard-prompt-injection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'xTRam1/safe-guard-prompt-injection' (2,171 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 14. jayavibhav/prompt-injection
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/jayavibhav/prompt-injection
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'jayavibhav/prompt-injection' (396 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 15. jayavibhav/prompt-injection-safety
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/jayavibhav/prompt-injection-safety
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'jayavibhav/prompt-injection-safety' (358 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 16. potsawee/chatbot-arena-llm-judges
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/potsawee/chatbot-arena-llm-judges
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'potsawee/chatbot-arena-llm-judges' (170 downloads) matched 'LLM judge' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 17. rubend18/ChatGPT-Jailbreak-Prompts
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/rubend18/ChatGPT-Jailbreak-Prompts
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'rubend18/ChatGPT-Jailbreak-Prompts' (2,494 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 18. llm-semantic-router/jailbreak-detection-dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/llm-semantic-router/jailbreak-detection-dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'llm-semantic-router/jailbreak-detection-dataset' (322 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 19. deadbits/vigil-jailbreak-ada-002
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/deadbits/vigil-jailbreak-ada-002
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'deadbits/vigil-jailbreak-ada-002' (114 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 20. deadbits/vigil-jailbreak-all-MiniLM-L6-v2
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/deadbits/vigil-jailbreak-all-MiniLM-L6-v2
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'deadbits/vigil-jailbreak-all-MiniLM-L6-v2' (113 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 21. jackhhao/jailbreak-classification
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/jackhhao/jailbreak-classification
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'jackhhao/jailbreak-classification' (3,236 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 22. JailbreakV-28K/JailBreakV-28k
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'JailbreakV-28K/JailBreakV-28k' (3,005 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 23. JailbreakBench/JBB-Behaviors
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'JailbreakBench/JBB-Behaviors' (30,227 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 24. walledai/JailbreakBench
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/walledai/JailbreakBench
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'walledai/JailbreakBench' (963 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 25. walledai/JailbreakHub
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/walledai/JailbreakHub
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'walledai/JailbreakHub' (873 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [Red Teaming the Mind of the Machine: A Systematic Evaluation of Prompt Injection](https://doi.org/10.48550/arXiv.2505.04806) | 2025 | arXiv.org | tool | 0.625 | moderate |
| 2 | paper | [Signed-prompt: A new approach to prevent prompt injection attacks against LLM-In](https://doi.org/10.1063/5.0222987) | 2024 | AIP Conference Proceedings | paper | 0.5 | moderate |
| 3 | paper | [Mind Mapping Prompt Injection: Visual Prompt Injection Attacks in Modern Large L](https://doi.org/10.3390/electronics14101907) | 2025 | Electronics | paper | 0.5 | moderate |
| 4 | paper | [Enhancing Security in Large Language Models: A Comprehensive Review of Prompt In](https://doi.org/10.36227/techrxiv.172954263.32914470/v1) | 2024 |  | survey | 0.5 | moderate |
| 5 | paper | [Prompt Injection](https://doi.org/10.61608/9783775757027-002) | 2024 | Worldbuilding | paper | 0.5 | moderate |
| 6 | paper | [An Evaluation of the Safety of ChatGPT with Malicious Prompt Injection](https://doi.org/10.21203/rs.3.rs-4487194/v1) | 2024 |  | paper | 0.5 | moderate |
| 7 | paper | [REAL TIME AI DEFENSE AGAINST PROMPT INJECTION ATTACKS](https://doi.org/10.37962/icydd/2025/23-24) | 2025 | 2nd International Conference on Cybersec | paper | 0.5 | moderate |
| 8 | paper | [Reconstruction-Based Prompt Generation Algorithm for Prompt Injection Attacks](https://doi.org/10.1109/aann66429.2025.11257661) | 2025 | 2025 5th International Conference on Adv | paper | 0.5 | moderate |
| 9 | paper | [Intent Vectoring: Black-Box Prompt Injection Detection via Semantic Trajectory M](https://doi.org/10.2139/ssrn.6280858) | 2026 |  | paper | 0.5 | moderate |
| 10 | paper | [Dynamic Moving Target Defense for Mitigating Targeted LLM Prompt Injection](https://doi.org/10.36227/techrxiv.171822345.56781952/v1) | 2024 |  | paper | 0.5 | moderate |
| 11 | paper | [Evaluating Hybrid Guardrail Architectures for Prompt Injection Defense in Large ](https://doi.org/10.2139/ssrn.6246379) | 2026 |  | paper | 0.5 | moderate |
| 12 | paper | [Feedback-Guided Prompt Injection Defense in Retrieval-Augmented Text-to-Cypher G](https://doi.org/10.2139/ssrn.5669662) | 2025 |  | paper | 0.5 | moderate |
| 13 | paper | [Prompt Injection Attacks on LLM-Based Spam Filters](https://doi.org/10.15611/2025.07.4.02) | 2025 | Informatyka w biznesie | paper | 0.5 | moderate |
| 14 | paper | [Secure Artificial Intelligence (SAI): A Dual-layer defence model against prompt ](https://doi.org/10.36948/ijfmr.2025.v07i01.35371) | 2025 | International Journal For Multidisciplin | paper | 0.5 | moderate |
| 15 | github | [SaFo-Lab/AgentDyn](https://github.com/SaFo-Lab/AgentDyn) |  | GitHub | tool | 50 | moderate |
| 16 | github | [sleeepeer/PIArena](https://github.com/sleeepeer/PIArena) |  | GitHub | tool | 32 | moderate |
| 17 | huggingface | [prodnull/prompt-injection-repo-dataset](https://huggingface.co/datasets/prodnull/prompt-injection-repo-dataset) |  | HuggingFace | dataset | 58 | moderate |
| 18 | huggingface | [beratcmn/turkish-prompt-injections](https://huggingface.co/datasets/beratcmn/turkish-prompt-injections) |  | HuggingFace | dataset | 51 | moderate |
| 19 | huggingface | [innodatalabs/rt-inod-jailbreaking](https://huggingface.co/datasets/innodatalabs/rt-inod-jailbreaking) |  | HuggingFace | dataset | 46 | moderate |
| 20 | huggingface | [markush1/LLM-Jailbreak-Classifier](https://huggingface.co/datasets/markush1/LLM-Jailbreak-Classifier) |  | HuggingFace | dataset | 64 | moderate |
| 21 | huggingface | [IDA-SERICS/Disaster-tweet-jailbreaking](https://huggingface.co/datasets/IDA-SERICS/Disaster-tweet-jailbreaking) |  | HuggingFace | dataset | 24 | moderate |
| 22 | huggingface | [GeorgeDaDude/Jailbreak_Complete_DS_labeled](https://huggingface.co/datasets/GeorgeDaDude/Jailbreak_Complete_DS_labeled) |  | HuggingFace | dataset | 29 | moderate |
| 23 | huggingface | [yuntian-deng/WildChat-1M-Jailbreaking-Internal](https://huggingface.co/datasets/yuntian-deng/WildChat-1M-Jailbreaking-Internal) |  | HuggingFace | dataset | 20 | moderate |
| 24 | huggingface | [innodatalabs/rt2-jailbreakv-alpaca](https://huggingface.co/datasets/innodatalabs/rt2-jailbreakv-alpaca) |  | HuggingFace | dataset | 41 | moderate |

### 1. Red Teaming the Mind of the Machine: A Systematic Evaluation of Prompt Injection and Jailbreak Vulnerabilities in LLMs
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2505.04806
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: tool
- **Why it overlaps**: Relevance 0.62: paper titled 'Red Teaming the Mind of the Machine: A Systematic Evaluation of Prompt Injection and Jailbreak Vulne' contributes a 'tool' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection|syn:title:jailbreak.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. Signed-prompt: A new approach to prevent prompt injection attacks against LLM-Integrated applications
- **Source**: paper  **URL**: https://doi.org/10.1063/5.0222987
- **Year/Venue**: 2024 / AIP Conference Proceedings
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Signed-prompt: A new approach to prevent prompt injection attacks against LLM-Integrated application' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. Mind Mapping Prompt Injection: Visual Prompt Injection Attacks in Modern Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.3390/electronics14101907
- **Year/Venue**: 2025 / Electronics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Mind Mapping Prompt Injection: Visual Prompt Injection Attacks in Modern Large Language Models' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. Enhancing Security in Large Language Models: A Comprehensive Review of Prompt Injection Attacks and Defenses
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.172954263.32914470/v1
- **Year/Venue**: 2024 / n/a
- **Contribution type**: survey
- **Why it overlaps**: Relevance 0.50: paper titled 'Enhancing Security in Large Language Models: A Comprehensive Review of Prompt Injection Attacks and ' contributes a 'survey' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. Prompt Injection
- **Source**: paper  **URL**: https://doi.org/10.61608/9783775757027-002
- **Year/Venue**: 2024 / Worldbuilding
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Prompt Injection' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. An Evaluation of the Safety of ChatGPT with Malicious Prompt Injection
- **Source**: paper  **URL**: https://doi.org/10.21203/rs.3.rs-4487194/v1
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'An Evaluation of the Safety of ChatGPT with Malicious Prompt Injection' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. REAL TIME AI DEFENSE AGAINST PROMPT INJECTION ATTACKS
- **Source**: paper  **URL**: https://doi.org/10.37962/icydd/2025/23-24
- **Year/Venue**: 2025 / 2nd International Conference on Cybersecurity and Digital Defense (ICyDD)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'REAL TIME AI DEFENSE AGAINST PROMPT INJECTION ATTACKS' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. Reconstruction-Based Prompt Generation Algorithm for Prompt Injection Attacks
- **Source**: paper  **URL**: https://doi.org/10.1109/aann66429.2025.11257661
- **Year/Venue**: 2025 / 2025 5th International Conference on Advanced Algorithms and Neural Networks (AANN)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Reconstruction-Based Prompt Generation Algorithm for Prompt Injection Attacks' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. Intent Vectoring: Black-Box Prompt Injection Detection via Semantic Trajectory Monitoring
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6280858
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Intent Vectoring: Black-Box Prompt Injection Detection via Semantic Trajectory Monitoring' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. Dynamic Moving Target Defense for Mitigating Targeted LLM Prompt Injection
- **Source**: paper  **URL**: https://doi.org/10.36227/techrxiv.171822345.56781952/v1
- **Year/Venue**: 2024 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Dynamic Moving Target Defense for Mitigating Targeted LLM Prompt Injection' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. Evaluating Hybrid Guardrail Architectures for Prompt Injection Defense in Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.6246379
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Evaluating Hybrid Guardrail Architectures for Prompt Injection Defense in Large Language Models' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. Feedback-Guided Prompt Injection Defense in Retrieval-Augmented Text-to-Cypher Generation
- **Source**: paper  **URL**: https://doi.org/10.2139/ssrn.5669662
- **Year/Venue**: 2025 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Feedback-Guided Prompt Injection Defense in Retrieval-Augmented Text-to-Cypher Generation' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 13. Prompt Injection Attacks on LLM-Based Spam Filters
- **Source**: paper  **URL**: https://doi.org/10.15611/2025.07.4.02
- **Year/Venue**: 2025 / Informatyka w biznesie
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Prompt Injection Attacks on LLM-Based Spam Filters' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 14. Secure Artificial Intelligence (SAI): A Dual-layer defence model against prompt injection and prompt poisoning attacks
- **Source**: paper  **URL**: https://doi.org/10.36948/ijfmr.2025.v07i01.35371
- **Year/Venue**: 2025 / International Journal For Multidisciplinary Research
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Secure Artificial Intelligence (SAI): A Dual-layer defence model against prompt injection and prompt' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:prompt injection.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 15. SaFo-Lab/AgentDyn
- **Source**: github  **URL**: https://github.com/SaFo-Lab/AgentDyn
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'SaFo-Lab/AgentDyn' (50 stars) provides an implementation of 'prompt injection'. Description: the official implementation of the paper "agentdyn: a dynamic open-ended benchmark for evaluating prompt injection attac.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 16. sleeepeer/PIArena
- **Source**: github  **URL**: https://github.com/sleeepeer/PIArena
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'sleeepeer/PIArena' (32 stars) provides an implementation of 'prompt injection'. Description: [acl 2026] piarena: a platform for prompt injection evaluation.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 17. prodnull/prompt-injection-repo-dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/prodnull/prompt-injection-repo-dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'prodnull/prompt-injection-repo-dataset' (58 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 18. beratcmn/turkish-prompt-injections
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/beratcmn/turkish-prompt-injections
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'beratcmn/turkish-prompt-injections' (51 downloads) matched 'prompt injection' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 19. innodatalabs/rt-inod-jailbreaking
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/innodatalabs/rt-inod-jailbreaking
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'innodatalabs/rt-inod-jailbreaking' (46 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 20. markush1/LLM-Jailbreak-Classifier
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/markush1/LLM-Jailbreak-Classifier
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'markush1/LLM-Jailbreak-Classifier' (64 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 21. IDA-SERICS/Disaster-tweet-jailbreaking
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/IDA-SERICS/Disaster-tweet-jailbreaking
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'IDA-SERICS/Disaster-tweet-jailbreaking' (24 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 22. GeorgeDaDude/Jailbreak_Complete_DS_labeled
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/GeorgeDaDude/Jailbreak_Complete_DS_labeled
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'GeorgeDaDude/Jailbreak_Complete_DS_labeled' (29 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 23. yuntian-deng/WildChat-1M-Jailbreaking-Internal
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/yuntian-deng/WildChat-1M-Jailbreaking-Internal
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'yuntian-deng/WildChat-1M-Jailbreaking-Internal' (20 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 24. innodatalabs/rt2-jailbreakv-alpaca
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/innodatalabs/rt2-jailbreakv-alpaca
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'innodatalabs/rt2-jailbreakv-alpaca' (41 downloads) matched 'jailbreak' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | ["Do Anything Now": Characterizing and Evaluating In-The-Wild Jailbreak Prompts o](https://doi.org/10.1145/3658644.3670388) | 2023 | Conference on Computer and Communication | paper | 0.312 | strong |
| 2 | paper | [Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box,](https://doi.org/10.48550/arXiv.2504.19254) | 2025 | Trans. Mach. Learn. Res. | paper | 0.25 | strong |
| 3 | paper | [Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human ](https://doi.org/10.48550/arXiv.2510.09738) | 2025 | arXiv.org | empirical | 0.25 | strong |
| 4 | paper | [Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Ope](https://doi.org/10.48550/arXiv.2602.05125) | 2026 | arXiv.org | paper | 0.25 | strong |
| 5 | paper | [Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations](https://doi.org/10.48550/arXiv.2510.11822) | 2025 | arXiv.org | paper | 0.25 | strong |
| 6 | paper | [Ask a Strong LLM Judge when Your Reward Model is Uncertain](https://doi.org/10.48550/arXiv.2510.20369) | 2025 | arXiv.org | paper | 0.25 | strong |
| 7 | paper | Tuning LLM Judge Design Decisions for 1/1000 of the Cost | 2025 | International Conference on Machine Lear | paper | 0.25 | strong |
| 8 | paper | [Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating na](https://doi.org/10.48550/arXiv.2504.02867) | 2025 | arXiv.org | paper | 0.25 | strong |
| 9 | paper | [When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silentl](https://doi.org/10.48550/arXiv.2509.20293) | 2025 | arXiv.org | benchmark | 0.25 | strong |
| 10 | paper | [Auto-Prompt Ensemble for LLM Judge](https://doi.org/10.48550/arXiv.2510.06538) | 2025 | arXiv.org | paper | 0.25 | strong |
| 11 | paper | [DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation](https://doi.org/10.48550/arXiv.2601.22230) | 2026 | arXiv.org | paper | 0.25 | strong |

### 1. "Do Anything Now": Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models
- **Source**: paper  **URL**: https://doi.org/10.1145/3658644.3670388
- **Year/Venue**: 2023 / Conference on Computer and Communications Security
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled '"Do Anything Now": Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Mod' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:abstract:prompt injection|syn:title:jailbreak.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ensemble Scorers
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.19254
- **Year/Venue**: 2025 / Trans. Mach. Learn. Res.
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Uncertainty Quantification for Language Models: A Suite of Black-Box, White-Box, LLM Judge, and Ense' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.09738
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: empirical
- **Why it overlaps**: Relevance 0.25: paper titled 'Judge's Verdict: A Comprehensive Analysis of LLM Judge Capability Through Human Agreement' contributes a 'empirical' matching target artifact 'benchmark'. Matched keywords: kw:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2602.05125
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.11822
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Beyond Consensus: Mitigating the Agreeableness Bias in LLM Judge Evaluations' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. Ask a Strong LLM Judge when Your Reward Model is Uncertain
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.20369
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Ask a Strong LLM Judge when Your Reward Model is Uncertain' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. Tuning LLM Judge Design Decisions for 1/1000 of the Cost
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2025 / International Conference on Machine Learning
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Tuning LLM Judge Design Decisions for 1/1000 of the Cost' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language generation applications
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2504.02867
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Multi-Agent LLM Judge: automatic personalized LLM judge design for evaluating natural language gener' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2509.20293
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'When Judgment Becomes Noise: How Design Failures in LLM Judge Benchmarks Silently Undermine Validity' contributes a 'benchmark' matching target artifact 'benchmark'. Matched keywords: kw:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Auto-Prompt Ensemble for LLM Judge
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2510.06538
- **Year/Venue**: 2025 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Auto-Prompt Ensemble for LLM Judge' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2601.22230
- **Year/Venue**: 2026 / arXiv.org
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'DAJ: Data-Reweighted LLM Judge for Test-Time Scaling in Code Generation' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: kw:title:llm judge.
- **How we differ**: Our proposed work focuses specifically on 'Judge robustness to candidate-side prompt injection — noise-pruned'. Narrowing note: removed noisy secondaries=['adversarial robustness']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
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

1. Complete the Artifact Differentiator Checklist above (25 artifacts found).
2. This topic can proceed to GO if artifact differentiator is articulated explicitly.
3. Write one paragraph for §6 verification log explaining differentiation from top artifacts.
