# Existing Work Report — T74_N1: Open structured-metadata dataset of LLM-eval papers — noise-pruned

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
| Partial overlaps (total) | 2 |
| Adjacent | 0 |
| Total findings | 2 |
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
| 1 | paper | [Magic Sequence: LLM evaluation methodology of logical problem solving for sequen](https://doi.org/10.1109/GACLM67198.2025.11232232) | 2025 | 2025 2nd International Generative AI and | paper | 0.5 | moderate |
| 2 | github | [aws-samples/llm-evaluation-methodology](https://github.com/aws-samples/llm-evaluation-methodology) |  | GitHub | tool | 47 | moderate |

### 1. Magic Sequence: LLM evaluation methodology of logical problem solving for sequence manipulation. Application to mathemat
- **Source**: paper  **URL**: https://doi.org/10.1109/GACLM67198.2025.11232232
- **Year/Venue**: 2025 / 2025 2nd International Generative AI and Computational Language Modelling Conference (GACLM)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Magic Sequence: LLM evaluation methodology of logical problem solving for sequence manipulation. App' contributes a 'paper' matching target artifact 'dataset'. Matched keywords: primary:title:llm evaluation methodology.
- **How we differ**: Our proposed work focuses specifically on 'Open structured-metadata dataset of LLM-eval papers — noise-pruned'. Narrowing note: removed noisy secondaries=['metadata', 'systematic mapping']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. aws-samples/llm-evaluation-methodology
- **Source**: github  **URL**: https://github.com/aws-samples/llm-evaluation-methodology
- **Year/Venue**:  / GitHub
- **Contribution type**: tool
- **Why it overlaps**: GitHub repo 'aws-samples/llm-evaluation-methodology' (47 stars) provides an implementation of 'llm evaluation methodology'. Description: n/a.
- **How we differ**: Our proposed work focuses specifically on 'Open structured-metadata dataset of LLM-eval papers — noise-pruned'. Narrowing note: removed noisy secondaries=['metadata', 'systematic mapping']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

_None._

## Recommended Actions

1. No blocking overlaps. Proceed with normal GO gate checks.
