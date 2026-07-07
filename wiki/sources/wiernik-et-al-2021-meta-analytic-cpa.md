---
address: c-000990
type: source
title: "Wiernik, Wilmot, Davison & Ones (2021) — Meta-Analytic Criterion Profile Analysis"
authors: ["[[Brenton M. Wiernik]]", "[[Michael P. Wilmot]]", "[[Mark L. Davison]]", "[[Deniz S. Ones]]"]
year: 2021
venue: "Psychological Methods, 26(2), 186–209. https://doi.org/10.1037/met0000305"
tags:
  - source
  - io-psychology
  - meta-analysis
  - methods
  - configural
  - criterion-profile-analysis
status: developing
created: 2026-07-07
updated: 2026-07-07
related:
  - "[[Criterion Profile Analysis]]"
  - "[[Configural Relationships]]"
  - "[[Meta-Analysis]]"
  - "[[psychometric meta-analysis]]"
  - "[[Composite vs Multiple Criteria]]"
  - "[[Cross-Validation]]"
  - "[[Overfitting]]"
  - "[[Situation Strength]]"
  - "[[Ability-Motivation-Opportunity Model]]"
sources:
  - "[[wiernik-et-al-2021-meta-analytic-cpa]]"
---

# Wiernik, Wilmot, Davison & Ones (2021) — Meta-Analytic Criterion Profile Analysis

> [!abstract] TL;DR
> Extends **[[Criterion Profile Analysis]]** (CPA; Davison & Davenport 2002) — a regression-based pattern-matching procedure — so it can run on **summary/meta-analytic data** instead of requiring individual-level data. The new method, **MACPA**, decomposes a set of predictors' relationship to a criterion into a **level effect** (overall profile elevation) and a **pattern effect** (similarity of a person's profile to the optimal *criterion pattern*). All key CPA statistics ($r_{lev,y}$, $r_{pat,y}$, $r_{lev,pat}$, full-model $R^2$, coefficients) are computed from just the correlation matrix. The paper adds artifact corrections (measurement error, range restriction), shrinkage/overfitting correction for the pattern effect, and **[[Configural Relationships#Fungible profile analysis|fungible profile analysis]]** sensitivity checks. R package `configural`.

## The core idea

A relationship among predictors and a criterion can be **configural** — the meaning of one predictor is contingent on another (Hoffman 1960). CPA targets the **contrastive** flavor of configuration: decomposing predictor variance into **between-person** (profile level/elevation) and **within-person** (profile pattern, irrespective of elevation) components, then asking how each relates to the criterion. This is distinct from the **interactive** (multiplicative, $X_1 \cdot X_2$) flavor tested by moderated regression.

> [!key-insight] Contrastive ≠ interactive
> Van Iddekinge et al. (2018) found ability × motivation had negligible *interactive* incremental validity — but reanalyzing their meta-analytic matrix with MACPA reveals a *contrastive* configural effect: employees relatively more capable than motivated tend to perform better. A null interaction does **not** mean "no configuration."

## Two-stage CPA (Davison & Davenport 2002)

1. **OLS regression** identifies the **criterion pattern** — a vector of contrast coefficients $\boldsymbol{\beta}^* = \boldsymbol{\beta} - \bar{\beta}\mathbf{1}$ (deviations of each regression weight from the mean weight).
2. Each person gets two scores: **profile level** (within-person mean of predictors) and **criterion pattern similarity** (covariance of their predictor vector with the criterion pattern). These are re-entered in a regression whose $R^2$ equals the original OLS $R^2$, decomposing prediction into **level** vs **pattern** effects.

## The MACPA extension

The theory of composites shows level and pattern effects are just alternative weighting schemes for composite correlations. So the three sufficient statistics can be computed from a correlation matrix alone:

- $r_{lev,y}$ = unit-weighted composite correlation (predictor profile level ↔ criterion)
- $r_{pat,y}$ = $\boldsymbol{\beta}^*$-weighted composite correlation (pattern similarity ↔ criterion)
- $r_{lev,pat}$ = correlation between the two composites

This opens CPA to **reanalysis of published meta-analyses** and to psychometric meta-analysis's artifact corrections.

## Statistical artifacts in CPA

| Artifact | Effect on CPA | Correction |
|---|---|---|
| Sampling error | Distorts pattern shape & effect sizes in small samples | Pool via [[Meta-Analysis]]; second-order sampling error addressed |
| Measurement error | Flattens pattern amplitude; weakens both effects; over-attributes to level | Correct matrix cell-by-cell (Viswesvaran & Ones 1995) or correct $r$'s directly (Bulut et al. 2017) |
| Selection effects (range restriction, collider bias) | Can distort shape & flip signs; changes amplitude & relative level/pattern contribution | Correct before MACPA (Dahlke & Wiernik 2019) |
| Overfitting | Positive bias in $r_{pat,y}$ | Shrunken-$R^2$ estimator (needed since two-fold cross-validation requires individual data) |

## Fungible profile analysis (sensitivity)

Following Waller (2008): perturb the input correlation matrix slightly and see whether the criterion pattern's *shape* is robust. Recommended **routinely** before interpreting a pattern's shape or criterion-related validity.

## Why it matters / implications

- **Theory:** distinguishes whether a predictor set works through *configuration* vs *simple accumulation*; can compare criterion patterns across related constructs (construct similarity/distinctiveness) and illuminate within-person mechanisms.
- **Assessment practice:** reduces many predictors to two interpretable pieces — overall quality (level) and prototype similarity (pattern) — which can improve holistic/subjective judgment (cf. [[Mechanical vs Clinical Prediction]]) and make quantitative data more acceptable to decision-makers than easier-but-invalid typologies (e.g., MBTI).
- Applied to organizational, educational, personality, and clinical literatures.

## Cross-references

Method sits alongside [[MASEM]] as a way to squeeze more from meta-analytic correlation matrices. Level/pattern decomposition connects to the [[Composite vs Multiple Criteria]] debate and to [[Configural Relationships]]. Overfitting correction relates to [[Cross-Validation]], [[Overfitting]], and [[Regularization]].
