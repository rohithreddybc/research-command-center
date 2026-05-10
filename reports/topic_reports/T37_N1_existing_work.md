# Existing Work Report — T37_N1: Clinical-guideline consistency across LLM versions over time — noise-pruned

> ⚠️ **DIFFERENTIATOR REQUIRED** — paper_direct=0, artifact_direct=0; paper_strength=`strong`, artifact_strength=`strong`.

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
| Partial overlaps (total) | 17 |
| Adjacent | 16 |
| Total findings | 33 |
| peer_reviewed_direct | No |
| high_artifact_overlap | No |
| GO blocked | No |
| Differentiator required | Yes |
| Artifact differentiator required | No |

## Peer-Reviewed Direct Overlaps

_None._

## Artifact Direct Overlaps (GitHub / HF / PWC)

_None._

## Partial Overlaps

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [First ‘NICE-curated’ clinical guideline announced](https://doi.org/10.1211/pj.2025.1.372584) | 2025 | Pharmaceutical Journal | paper | 0.625 | moderate |
| 2 | paper | [CDC Clinical Guidelines on the Use of Doxycycline Postexposure Prophylaxis for B](https://doi.org/10.15585/mmwr.rr7302a1) | 2024 | MMWR Recommendations and Reports | paper | 0.5 | moderate |
| 3 | paper | [ACG Clinical Guideline: Diagnosis and Management of Eosinophilic Esophagitis.](https://doi.org/10.14309/ajg.0000000000003194) | 2025 | American Journal of Gastroenterology | paper | 0.5 | moderate |
| 4 | paper | [ACG Clinical Guideline Update: Ulcerative Colitis in Adults](https://doi.org/10.14309/ajg.0000000000003463) | 2025 | American Journal of Gastroenterology | paper | 0.5 | moderate |
| 5 | paper | [ACG Clinical Guideline: Management of Crohn's Disease in Adults](https://doi.org/10.14309/ajg.0000000000003465) | 2025 | American Journal of Gastroenterology | paper | 0.5 | moderate |
| 6 | paper | [ACG Clinical Guideline: Malnutrition and Nutritional Recommendations in Liver Di](https://doi.org/10.14309/ajg.0000000000003379) | 2025 | American Journal of Gastroenterology | paper | 0.5 | moderate |
| 7 | paper | [ACG Clinical Guideline: Diagnosis and Management of Gastric Premalignant Conditi](https://doi.org/10.14309/ajg.0000000000003350) | 2025 | American Journal of Gastroenterology | paper | 0.5 | moderate |
| 8 | paper | [The 2024 UK clinical guideline for the prevention and treatment of osteoporosis](https://doi.org/10.1007/s11657-025-01588-3) | 2025 | Archives of Osteoporosis | paper | 0.5 | moderate |
| 9 | paper | [ACG Clinical Guideline Update: Preventive Care in Inflammatory Bowel Disease.](https://doi.org/10.14309/ajg.0000000000003541) | 2025 | American Journal of Gastroenterology | paper | 0.5 | moderate |
| 10 | paper | [Appraisal of Clinical Practice Guideline: Australian Clinical Guideline for Phys](https://doi.org/10.1016/j.jphys.2024.05.009) | 2024 | Journal of Physiotherapy | paper | 0.5 | moderate |
| 11 | huggingface | [rubanza/uganda-clinical-guidelines](https://huggingface.co/datasets/rubanza/uganda-clinical-guidelines) |  | HuggingFace | dataset | 60 | moderate |
| 12 | huggingface | [ClarusC64/clinical-guideline-strength-correspondence-v0.1](https://huggingface.co/datasets/ClarusC64/clinical-guideline-strength-correspondence-v0.1) |  | HuggingFace | dataset | 24 | moderate |
| 13 | huggingface | [chisomrutherford/nigeria-clinical-guidelines-dataset](https://huggingface.co/datasets/chisomrutherford/nigeria-clinical-guidelines-dataset) |  | HuggingFace | dataset | 81 | moderate |
| 14 | huggingface | [Khyatimirani/pcos-clinical-guideline-101](https://huggingface.co/datasets/Khyatimirani/pcos-clinical-guideline-101) |  | HuggingFace | dataset | 52 | moderate |
| 15 | huggingface | [Khyatimirani/peri-menopause-clinical-guideline](https://huggingface.co/datasets/Khyatimirani/peri-menopause-clinical-guideline) |  | HuggingFace | dataset | 32 | moderate |
| 16 | huggingface | [Khyatimirani/pcos-lean-clinical-guideline](https://huggingface.co/datasets/Khyatimirani/pcos-lean-clinical-guideline) |  | HuggingFace | dataset | 22 | moderate |
| 17 | huggingface | [ClarusC64/clinical-team-mental-model-drift-detection-v0.1](https://huggingface.co/datasets/ClarusC64/clinical-team-mental-model-drift-detection-v0.1) |  | HuggingFace | dataset | 20 | moderate |

### 1. First ‘NICE-curated’ clinical guideline announced
- **Source**: paper  **URL**: https://doi.org/10.1211/pj.2025.1.372584
- **Year/Venue**: 2025 / Pharmaceutical Journal
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.62: paper titled 'First ‘NICE-curated’ clinical guideline announced' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:clinical guideline|syn:title:nice.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 2. CDC Clinical Guidelines on the Use of Doxycycline Postexposure Prophylaxis for Bacterial Sexually Transmitted Infection 
- **Source**: paper  **URL**: https://doi.org/10.15585/mmwr.rr7302a1
- **Year/Venue**: 2024 / MMWR Recommendations and Reports
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'CDC Clinical Guidelines on the Use of Doxycycline Postexposure Prophylaxis for Bacterial Sexually Tr' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:clinical guideline.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 3. ACG Clinical Guideline: Diagnosis and Management of Eosinophilic Esophagitis.
- **Source**: paper  **URL**: https://doi.org/10.14309/ajg.0000000000003194
- **Year/Venue**: 2025 / American Journal of Gastroenterology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'ACG Clinical Guideline: Diagnosis and Management of Eosinophilic Esophagitis.' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:clinical guideline.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 4. ACG Clinical Guideline Update: Ulcerative Colitis in Adults
- **Source**: paper  **URL**: https://doi.org/10.14309/ajg.0000000000003463
- **Year/Venue**: 2025 / American Journal of Gastroenterology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'ACG Clinical Guideline Update: Ulcerative Colitis in Adults' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:clinical guideline.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 5. ACG Clinical Guideline: Management of Crohn's Disease in Adults
- **Source**: paper  **URL**: https://doi.org/10.14309/ajg.0000000000003465
- **Year/Venue**: 2025 / American Journal of Gastroenterology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'ACG Clinical Guideline: Management of Crohn's Disease in Adults' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:clinical guideline.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 6. ACG Clinical Guideline: Malnutrition and Nutritional Recommendations in Liver Disease
- **Source**: paper  **URL**: https://doi.org/10.14309/ajg.0000000000003379
- **Year/Venue**: 2025 / American Journal of Gastroenterology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'ACG Clinical Guideline: Malnutrition and Nutritional Recommendations in Liver Disease' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:clinical guideline.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 7. ACG Clinical Guideline: Diagnosis and Management of Gastric Premalignant Conditions
- **Source**: paper  **URL**: https://doi.org/10.14309/ajg.0000000000003350
- **Year/Venue**: 2025 / American Journal of Gastroenterology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'ACG Clinical Guideline: Diagnosis and Management of Gastric Premalignant Conditions' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:clinical guideline.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 8. The 2024 UK clinical guideline for the prevention and treatment of osteoporosis
- **Source**: paper  **URL**: https://doi.org/10.1007/s11657-025-01588-3
- **Year/Venue**: 2025 / Archives of Osteoporosis
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'The 2024 UK clinical guideline for the prevention and treatment of osteoporosis' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:clinical guideline.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 9. ACG Clinical Guideline Update: Preventive Care in Inflammatory Bowel Disease.
- **Source**: paper  **URL**: https://doi.org/10.14309/ajg.0000000000003541
- **Year/Venue**: 2025 / American Journal of Gastroenterology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'ACG Clinical Guideline Update: Preventive Care in Inflammatory Bowel Disease.' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:clinical guideline.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 10. Appraisal of Clinical Practice Guideline: Australian Clinical Guideline for Physical Rehabilitation and Mobilisation in 
- **Source**: paper  **URL**: https://doi.org/10.1016/j.jphys.2024.05.009
- **Year/Venue**: 2024 / Journal of Physiotherapy
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.50: paper titled 'Appraisal of Clinical Practice Guideline: Australian Clinical Guideline for Physical Rehabilitation ' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:title:clinical guideline.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 11. rubanza/uganda-clinical-guidelines
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/rubanza/uganda-clinical-guidelines
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'rubanza/uganda-clinical-guidelines' (60 downloads) matched 'clinical guideline' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 12. ClarusC64/clinical-guideline-strength-correspondence-v0.1
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/ClarusC64/clinical-guideline-strength-correspondence-v0.1
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'ClarusC64/clinical-guideline-strength-correspondence-v0.1' (24 downloads) matched 'clinical guideline' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 13. chisomrutherford/nigeria-clinical-guidelines-dataset
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/chisomrutherford/nigeria-clinical-guidelines-dataset
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'chisomrutherford/nigeria-clinical-guidelines-dataset' (81 downloads) matched 'clinical guideline' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 14. Khyatimirani/pcos-clinical-guideline-101
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Khyatimirani/pcos-clinical-guideline-101
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Khyatimirani/pcos-clinical-guideline-101' (52 downloads) matched 'clinical guideline' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 15. Khyatimirani/peri-menopause-clinical-guideline
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Khyatimirani/peri-menopause-clinical-guideline
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Khyatimirani/peri-menopause-clinical-guideline' (32 downloads) matched 'clinical guideline' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 16. Khyatimirani/pcos-lean-clinical-guideline
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/Khyatimirani/pcos-lean-clinical-guideline
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'Khyatimirani/pcos-lean-clinical-guideline' (22 downloads) matched 'clinical guideline' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

### 17. ClarusC64/clinical-team-mental-model-drift-detection-v0.1
- **Source**: huggingface  **URL**: https://huggingface.co/datasets/ClarusC64/clinical-team-mental-model-drift-detection-v0.1
- **Year/Venue**:  / HuggingFace
- **Contribution type**: dataset
- **Why it overlaps**: HuggingFace dataset/space 'ClarusC64/clinical-team-mental-model-drift-detection-v0.1' (20 downloads) matched 'model drift' — provides similar data/evaluation assets.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `moderate`

## Adjacent Work (context only)

| # | Source | Name | Year | Venue | Contrib | Rel/Stars | Diff-Strength |
|---|---|---|---|---|---|---|---|
| 1 | paper | [CDC Guidelines for the Prevention and Treatment of Anthrax, 2023](https://doi.org/10.15585/mmwr.rr7206a1) | 2023 | MMWR Recommendations and Reports | paper | 0.312 | strong |
| 2 | paper | [Model Drift in Dynamic Networks](https://doi.org/10.1109/MCOM.003.2200306) | 2023 | IEEE Communications Magazine | paper | 0.25 | strong |
| 3 | paper | [Performance of GPT-4 on the American College of Radiology In-training Examinatio](https://doi.org/10.1016/j.acra.2024.04.006) | 2024 | Academic Radiology | paper | 0.25 | strong |
| 4 | paper | [Machine Learning Model Drift: Predicting Diagnostic Imaging Follow-Up as a Case ](https://doi.org/10.1016/j.jacr.2022.05.030) | 2022 | Journal of the American College of Radio | paper | 0.25 | strong |
| 5 | paper | [Tackling data and model drift in AI: Strategies for maintaining accuracy during ](https://doi.org/10.30574/ijsra.2023.10.2.0855) | 2023 | International Journal of Science and Res | paper | 0.25 | strong |
| 6 | paper | [Understanding Model Drift and Its Impact on Health Care Policy.](https://doi.org/10.1001/jamahealthforum.2025.2724) | 2025 | JAMA Health Forum | paper | 0.25 | strong |
| 7 | paper | [Susceptibility of AutoML mortality prediction algorithms to model drift caused b](https://doi.org/10.1186/s12911-024-02428-z) | 2024 | BMC Medical Informatics and Decision Mak | paper | 0.25 | strong |
| 8 | paper | [Explainable Artificial Intelligence-Based Model Drift Detection Applicable to Un](https://doi.org/10.32604/cmc.2023.040235) | 2023 | Computers, Materials &amp; Continua | paper | 0.25 | strong |
| 9 | paper | [Joint Prediction of SOH and RUL for Lithium Batteries Considering Capacity Self ](https://doi.org/10.1109/JIOT.2025.3550270) | 2025 | IEEE Internet of Things Journal | paper | 0.25 | strong |
| 10 | paper | [Data Quality Aware Approaches for Addressing Model Drift of Semantic Segmentatio](https://doi.org/10.48550/arXiv.2402.07258) | 2024 | VISIGRAPP : VISAPP | paper | 0.25 | strong |
| 11 | paper | [Dual Self-Attention is What You Need for Model Drift Detection in 6G Networks](https://doi.org/10.1109/TMLCN.2025.3576727) | 2025 | IEEE Transactions on Machine Learning in | paper | 0.25 | strong |
| 12 | paper | [Model Drift in Deployed Machine Learning Models for Predicting Learning Success](https://doi.org/10.3390/computers14090351) | 2025 | De Computis | paper | 0.25 | strong |
| 13 | paper | [Model Drift-Adaptive Resource Reservation in ISAC Networks: A Digital Twin-Based](https://doi.org/10.1109/ICCC62479.2024.10681925) | 2024 | 2024 IEEE/CIC International Conference o | paper | 0.25 | strong |
| 14 | paper | [Interpretable Model Drift Detection](https://doi.org/10.1145/3632410.3632434) | 2024 | COMAD/CODS | paper | 0.25 | strong |
| 15 | paper | [Effects of Model Drift on Ship Detection Models](https://doi.org/10.5220/0012443600003660) | 2024 | VISIGRAPP : VISAPP | paper | 0.25 | strong |
| 16 | paper | [Quantifying Model Drift in Machine Learning for Estimating Wireless Link Quality](https://doi.org/10.1109/MeditCom64437.2025.11104484) | 2025 | International Mediterranean Conference o | paper | 0.25 | strong |

### 1. CDC Guidelines for the Prevention and Treatment of Anthrax, 2023
- **Source**: paper  **URL**: https://doi.org/10.15585/mmwr.rr7206a1
- **Year/Venue**: 2023 / MMWR Recommendations and Reports
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.31: paper titled 'CDC Guidelines for the Prevention and Treatment of Anthrax, 2023' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: primary:abstract:clinical guideline|syn:title:cdc guidelines.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 2. Model Drift in Dynamic Networks
- **Source**: paper  **URL**: https://doi.org/10.1109/MCOM.003.2200306
- **Year/Venue**: 2023 / IEEE Communications Magazine
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Model Drift in Dynamic Networks' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 3. Performance of GPT-4 on the American College of Radiology In-training Examination: Evaluating Accuracy, Model Drift, and
- **Source**: paper  **URL**: https://doi.org/10.1016/j.acra.2024.04.006
- **Year/Venue**: 2024 / Academic Radiology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Performance of GPT-4 on the American College of Radiology In-training Examination: Evaluating Accura' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 4. Machine Learning Model Drift: Predicting Diagnostic Imaging Follow-Up as a Case Example.
- **Source**: paper  **URL**: https://doi.org/10.1016/j.jacr.2022.05.030
- **Year/Venue**: 2022 / Journal of the American College of Radiology
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Machine Learning Model Drift: Predicting Diagnostic Imaging Follow-Up as a Case Example.' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 5. Tackling data and model drift in AI: Strategies for maintaining accuracy during ML model inference
- **Source**: paper  **URL**: https://doi.org/10.30574/ijsra.2023.10.2.0855
- **Year/Venue**: 2023 / International Journal of Science and Research Archive
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Tackling data and model drift in AI: Strategies for maintaining accuracy during ML model inference' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 6. Understanding Model Drift and Its Impact on Health Care Policy.
- **Source**: paper  **URL**: https://doi.org/10.1001/jamahealthforum.2025.2724
- **Year/Venue**: 2025 / JAMA Health Forum
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Understanding Model Drift and Its Impact on Health Care Policy.' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 7. Susceptibility of AutoML mortality prediction algorithms to model drift caused by the COVID pandemic
- **Source**: paper  **URL**: https://doi.org/10.1186/s12911-024-02428-z
- **Year/Venue**: 2024 / BMC Medical Informatics and Decision Making
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Susceptibility of AutoML mortality prediction algorithms to model drift caused by the COVID pandemic' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 8. Explainable Artificial Intelligence-Based Model Drift Detection Applicable to Unsupervised Environments
- **Source**: paper  **URL**: https://doi.org/10.32604/cmc.2023.040235
- **Year/Venue**: 2023 / Computers, Materials &amp; Continua
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Explainable Artificial Intelligence-Based Model Drift Detection Applicable to Unsupervised Environme' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 9. Joint Prediction of SOH and RUL for Lithium Batteries Considering Capacity Self Recovery and Model Drift
- **Source**: paper  **URL**: https://doi.org/10.1109/JIOT.2025.3550270
- **Year/Venue**: 2025 / IEEE Internet of Things Journal
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Joint Prediction of SOH and RUL for Lithium Batteries Considering Capacity Self Recovery and Model D' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 10. Data Quality Aware Approaches for Addressing Model Drift of Semantic Segmentation Models
- **Source**: paper  **URL**: https://doi.org/10.48550/arXiv.2402.07258
- **Year/Venue**: 2024 / VISIGRAPP : VISAPP
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Data Quality Aware Approaches for Addressing Model Drift of Semantic Segmentation Models' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 11. Dual Self-Attention is What You Need for Model Drift Detection in 6G Networks
- **Source**: paper  **URL**: https://doi.org/10.1109/TMLCN.2025.3576727
- **Year/Venue**: 2025 / IEEE Transactions on Machine Learning in Communications and Networking
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Dual Self-Attention is What You Need for Model Drift Detection in 6G Networks' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 12. Model Drift in Deployed Machine Learning Models for Predicting Learning Success
- **Source**: paper  **URL**: https://doi.org/10.3390/computers14090351
- **Year/Venue**: 2025 / De Computis
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Model Drift in Deployed Machine Learning Models for Predicting Learning Success' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 13. Model Drift-Adaptive Resource Reservation in ISAC Networks: A Digital Twin-Based Approach
- **Source**: paper  **URL**: https://doi.org/10.1109/ICCC62479.2024.10681925
- **Year/Venue**: 2024 / 2024 IEEE/CIC International Conference on Communications in China (ICCC)
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Model Drift-Adaptive Resource Reservation in ISAC Networks: A Digital Twin-Based Approach' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 14. Interpretable Model Drift Detection
- **Source**: paper  **URL**: https://doi.org/10.1145/3632410.3632434
- **Year/Venue**: 2024 / COMAD/CODS
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Interpretable Model Drift Detection' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 15. Effects of Model Drift on Ship Detection Models
- **Source**: paper  **URL**: https://doi.org/10.5220/0012443600003660
- **Year/Venue**: 2024 / VISIGRAPP : VISAPP
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Effects of Model Drift on Ship Detection Models' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

### 16. Quantifying Model Drift in Machine Learning for Estimating Wireless Link Quality
- **Source**: paper  **URL**: https://doi.org/10.1109/MeditCom64437.2025.11104484
- **Year/Venue**: 2025 / International Mediterranean Conference on Communications and Networking
- **Contribution type**: paper
- **Why it overlaps**: Relevance 0.25: paper titled 'Quantifying Model Drift in Machine Learning for Estimating Wireless Link Quality' contributes a 'paper' matching target artifact 'empirical'. Matched keywords: kw:title:model drift.
- **How we differ**: Our proposed work focuses specifically on 'Clinical-guideline consistency across LLM versions over time — noise-pruned'. Narrowing note: removed noisy secondaries=['longitudinal evaluation']; added to negatives. Articulate a concrete contribution gap versus this existing work before promoting to GO (see §6 verification log).
- **Differentiator strength**: `strong`

## Recommended Actions

1. Document a clear differentiator before GO (partial overlaps: 17).
