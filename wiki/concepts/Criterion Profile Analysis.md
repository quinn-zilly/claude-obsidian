---
address: c-000992
type: concept
title: "Criterion Profile Analysis"
status: developing
tags:
  - concept
  - methods
  - configural
  - meta-analysis
created: 2026-07-07
updated: 2026-07-07
related:
  - "[[Configural Relationships]]"
  - "[[Composite vs Multiple Criteria]]"
  - "[[Cross-Validation]]"
  - "[[Overfitting]]"
  - "[[Meta-Analysis]]"
  - "[[MASEM]]"
sources:
  - "[[davison-davenport-2002-criterion-related-patterns]]"
  - "[[wiernik-et-al-2021-meta-analytic-cpa]]"
---

# Criterion Profile Analysis

**Criterion profile analysis (CPA)** is a regression-based pattern-matching procedure (Davison & Davenport 2002) that identifies the **pattern of predictor scores that optimally relates to a criterion** and quantifies how strongly that pattern predicts.

## Two stages

1. **Identify the criterion pattern.** OLS regression gives predictor weights; the criterion pattern is the vector of **contrast coefficients** $\boldsymbol{\beta}^* = \boldsymbol{\beta} - \bar{\beta}\mathbf{1}$ (each weight minus the mean weight). It encodes which predictors should be relatively *high* vs *low*.
2. **Decompose prediction.** Each person's predictor profile is re-expressed as (a) **profile level** — the within-person mean across predictors (overall elevation) — and (b) **criterion pattern similarity** — the covariance of their profile with the criterion pattern. Regressing the criterion on these two yields the same $R^2$ as the original OLS, split into a **level effect** and a **pattern effect**.

## Why decompose?

It answers whether a predictor set works through **configuration** (the *shape* of scores matters, holding elevation constant) vs **simple accumulation** (only overall level matters). This is the **contrastive** type of [[Configural Relationships|configural relationship]], distinct from **interactive** (multiplicative) effects tested by moderated regression.

## MACPA — the meta-analytic extension

Historically CPA needed individual-level data. [[wiernik-et-al-2021-meta-analytic-cpa|Wiernik et al. (2021)]] showed all key statistics can be computed from a **correlation matrix alone**, via the theory of composites. This enables **meta-analytic CPA (MACPA)**: reanalyze published meta-analyses from a pattern perspective and apply psychometric artifact corrections. Key formulas rest on three quantities: $r_{lev,y}$, $r_{pat,y}$, and $r_{lev,pat}$.

## Cautions

- **Measurement error** flattens the pattern and over-attributes variance to the level effect — correct it.
- **Overfitting** inflates the pattern effect $r_{pat,y}$ — use a shrunken-$R^2$ estimator (see [[Overfitting]], [[Cross-Validation]]).
- Run **[[Configural Relationships#Fungible profile analysis|fungible profile analysis]]** to check the pattern shape is robust to matrix perturbations.

## Primary source detail

The method-origin paper [[davison-davenport-2002-criterion-related-patterns|Davison & Davenport (2002)]] supplies: the re-expression $\hat{Y}_p = (V/k)\text{Cov}_{pc} + V\bar{b}\bar{X}_{p\cdot} + a$; the df split (level = 1, pattern = $V-1$); nested $F$-tests ($R^2_F$ vs $R^2_L$ = pattern-over-level; $R^2_F$ vs $R^2_P$ = level-over-pattern); **double cross-validation**; and two worked examples (vocational interest → Social Closeness, pattern = 12.9%; math course-work → achievement, pattern adds 36.8% over level). Where level and pattern are themselves correlated (course-work example, $r=.61$), the decomposition still isolates the incremental pattern contribution.

R implementation: `configural` package.
