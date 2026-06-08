---
type: concept
title: "MASEM (Meta-Analytic Structural Equation Modelling)"
created: 2026-06-07
updated: 2026-06-07
address: c-000617
tags:
  - methodology
  - meta-analysis
  - concept
status: developing
related:
  - "[[UTAUT]]"
  - "[[Revised UTAUT Model]]"
sources:
  - "[[dwivedi-2019-utaut-revision|Dwivedi et al. (2019)]]"
---

# MASEM

**Meta-Analytic Structural Equation Modelling** — synthesize correlation matrices from many primary studies into a single pooled correlation matrix, then fit a structural equation model to it (Viswesvaran & Ones 1998; Cheung & Chan 2005).

## Why use it

A theory-driven quantitative review. Its key advantage: **not every relationship needs to appear in every primary study** — the required population correlations can be assembled meta-analytically across the literature, then tested as one model.

## Procedure (as applied in [[dwivedi-2019-utaut-revision|Dwivedi et al. (2019)]])

1. **Code** effect sizes (Pearson r), sample sizes, and reliabilities from each study.
2. **Correct** each effect size for measurement error using construct reliabilities, then for sampling error via sample-size-weighted pooling.
3. **Pool** into a corrected correlation matrix.
4. **Choose a single N** for SEM (minimum, harmonic mean, or average sample size — they used the minimum, N = 4319, validating with the others).
5. **Fit** the SEM (AMOS), pruning paths with critical ratio < 1.96 and adding emergent paths with modification index ≥ 10 that are theoretically defensible.

## Caveats

Assumes it is meaningful to combine similar-but-not-identical measures across studies. Sensitive to which studies report convertible statistics, and to imputation of missing reliabilities/SDs. Moderator effects are hard to recover if primary studies don't report them.
