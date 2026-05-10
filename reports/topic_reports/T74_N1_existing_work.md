# Existing Work Report — T74_N1: Open structured-metadata dataset of LLM-eval papers — noise-pruned

> ⚠️ **DIFFERENTIATOR REQUIRED** — 0 direct + 2 partial overlap(s); strength = `strong`.

## Summary

| Metric | Value |
|---|---|
| Direct overlaps | 0 |
| Partial overlaps | 2 |
| Adjacent | 0 |
| Total findings | 2 |
| Differentiator strength | `strong` |
| GO blocked | No |
| Differentiator required | Yes |

## Direct Overlaps (GO-blocking)

_None._

## Partial Overlaps (differentiator required)

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

1. Document a clear differentiator before promoting to GO (partial overlaps: 2).
2. Update `data/existing_work/T74_N1.json` → `requires_differentiator: true` acknowledged.
