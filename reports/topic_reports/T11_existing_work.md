# Existing Work Report — T11: Format sensitivity benchmark on LLM evaluations

> ✅ **Clear to proceed** — no blocking overlaps (paper_direct=0, artifact_direct=0).

## Summary

| Metric | Value |
|---|---|
| **Paper direct overlaps** | 0 |
| Paper diff strength | `strong` |
| GitHub direct artifacts | 0 |
| HuggingFace direct artifacts | 0 |
| PWC direct artifacts | 0 |
| **Artifact direct count** | 0 |
| Artifact diff strength | `strong` |
| Partial overlaps (total) | 1 |
| Adjacent | 2 |
| Total findings | 3 |
| peer_reviewed_direct | No |
| high_artifact_overlap | No |
| GO blocked | No |
| Differentiator required | No |
| Artifact differentiator required | No |

## Peer-Reviewed Direct Overlaps

_None._

## Artifact Direct Overlaps (GitHub / HF / PWC)

_None._

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evid | 2026 |  | paper | 0.5 | moderate |

### 1. Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlled Prompt Structure
- **Source**: paper  **URL**: n/a
- **Year/Venue**: 2026 / n/a
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Is Evaluation Awareness Just Format Sensitivity? Limitations of Probe-Based Evidence under Controlle' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: primary:title:format sensitivity.
- **How we differ**: Our proposed work focuses specifically on 'Format sensitivity benchmark on LLM evaluations'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [BenchING: A Benchmark for Evaluating Large Language Models in Following Structur](https://doi.org/10.1109/TG.2025.3529117) | 2025 | IEEE Transactions on Games | benchmark | 0.25 | strong |
| 2 | paper | [Quantifying the Impact of Structured Output Format on Large Language Models thro](https://doi.org/10.18653/v1/2026.findings-eacl.91) | 2025 | Conference of the European Chapter of th | paper | 0.25 | strong |

### 1. BenchING: A Benchmark for Evaluating Large Language Models in Following Structured Output Format Instruction in Text-Bas
- **Source**: paper  **URL**: https://doi.org/10.1109/TG.2025.3529117
- **Year/Venue**: 2025 / IEEE Transactions on Games
- **Contribution type**: benchmark
- **Why it overlaps**: Relevance 0.25: paper titled 'BenchING: A Benchmark for Evaluating Large Language Models in Following Structured Output Format Ins' contributes a 'benchmark' matching target artifact 'benchmark'. Matched keywords: syn:title:output format|syn:title:structured output.
- **How we differ**: Our proposed work focuses specifically on 'Format sensitivity benchmark on LLM evaluations'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. Quantifying the Impact of Structured Output Format on Large Language Models through Causal Inference
- **Source**: paper  **URL**: https://doi.org/10.18653/v1/2026.findings-eacl.91
- **Year/Venue**: 2025 / Conference of the European Chapter of the Association for Computational Linguistics
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Quantifying the Impact of Structured Output Format on Large Language Models through Causal Inference' contributes a 'paper' matching target artifact 'benchmark'. Matched keywords: syn:title:output format|syn:title:structured output.
- **How we differ**: Our proposed work focuses specifically on 'Format sensitivity benchmark on LLM evaluations'. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

## Recommended Actions

1. No blocking overlaps. Proceed with normal GO gate checks.
2. Review 2 adjacent item(s) for citation and framing.
