---
address: c-001004
type: source
title: "Davison & Davenport (2002) — Identifying Criterion-Related Patterns of Predictor Scores Using Multiple Regression"
authors: ["Mark L. Davison", "Ernest C. Davenport Jr."]
year: 2002
venue: "Psychological Methods, 7(4), 468–484"
doi: "10.1037/1082-989X.7.4.468"
status: developing
tags:
  - source
  - methods
  - configural
  - regression
  - psychometrics
created: 2026-07-07
updated: 2026-07-07
related:
  - "[[Criterion Profile Analysis]]"
  - "[[Configural Relationships]]"
  - "[[Cross-Validation]]"
  - "[[Mark L. Davison]]"
  - "[[Ernest C. Davenport Jr.]]"
---

# Davison & Davenport (2002) — Identifying Criterion-Related Patterns of Predictor Scores

Nav: [[index]] | [[log]] | [[Criterion Profile Analysis]]

> [!abstract] One-line
> The **primary source** for **criterion profile analysis (CPA)**: a multiple-regression procedure that identifies the *pattern* of predictor scores associated with high criterion scores, and partitions predictive variance into a **level effect** and a **pattern effect**.

## The question (via Meehl 1950)

Meehl called *pattern* "one of the most important words in the clinician's vocabulary." The paper doesn't settle whether patterns *improve prediction*, but supplies the regression machinery to **ask** it rigorously — an **external** (criterion-referenced) alternative to internal profile methods (cluster analysis, modal profile analysis, MDS, configural frequency analysis) that ignore any criterion and, for continuous predictors, force lossy categorization.

## Decomposing a profile

Each person's predictor vector splits into:

- **Level** — the within-person mean $\bar{X}_{p\cdot}$ (overall profile elevation).
- **Pattern** — deviations of each score from that mean, $x_p = [X_{pv} - \bar{X}_{p\cdot}]$ (sums to zero).

## The criterion pattern

Run OLS of the criterion on the predictors → weights $b$. The **criterion-pattern vector** is the deviation of weights about their mean, $b^* = [b_v - \bar{b}]$. The whole proportional family $x_c = kb^*$ ($k>0$) shares the same *pattern* (arrangement of highs and lows). The regression equation can be **re-expressed** in terms of any $x_c$:

$$\hat{Y}_p = (V/k)\,\text{Cov}_{pc} + V\bar{b}\,\bar{X}_{p\cdot} + a$$

where $\text{Cov}_{pc}$ = covariance of person $p$'s profile with the criterion-pattern vector (the **pattern effect**, conditional on level) and $\bar{X}_{p\cdot}$ carries the **level effect**.

## Partitioning variance

- **Pattern effect** = squared correlation of $\text{Cov}_{pc}$ with $Y$.
- **Level effect** = squared correlation of $\bar{X}_{p\cdot}$ with $Y$.
- Degrees of freedom: level = 1; pattern = $V-1$ (the $V$ deviation weights sum to zero).
- Nested $F$-tests: $R^2_F$ (full: level + pattern) vs $R^2_L$ (level only) tests whether **pattern adds over level**; vs $R^2_P$ (pattern only) tests whether **level adds over pattern**.

## Cross-validation

Regression weights are "notoriously unstable" (Dawes 1979), so a pattern derived in one sample may shrink in another. The paper uses **double cross-validation**: derive $b^*$ in Sample 1, compute $\text{Cov}_{pc}$ and predict $Y$ in Sample 2, then reverse — yielding two estimates of the pattern effect's cross-sample validity. In the cross-validated model, the pattern effect carries only **1 df**.

## Worked examples

1. **Vocational interest → personality.** Six Holland interest scales predicting Tellegen's *Social Closeness* ($N=328$). Pattern effect alone accounted for **12.9%** of variance; level effect ≈ 0. Marker variables: high *Social*, low *Realistic* (the "people vs things" dimension). Cross-validation confirmed pattern, not level, carries the signal.
2. **Math course-work → achievement.** Seven course-category frequencies ($N\approx10{,}245$, NELS) predicting senior math achievement. Pattern added **36.8%** over level; together **57.4%**. Here level and pattern were *correlated* (.61) — students who take more courses also take more advanced ones. Shows CPA applies to any set of predictors describing a per-person distribution.

## Invariance & interpretation

Choice of $k$ is arbitrary for variance accounted for but matters for interpretation/graphing and especially when $\text{Cov}_{pc}$ is used to **classify** people against several competing criterion patterns (standardize so $\frac{1}{V}\sum x_{cv}^2 = 1$ per pattern). A significance test (Appendix B) flags which weights sit significantly above/below the mean, identifying **marker variables** to label the pattern.

## Why it's in the vault

The **method-origin primary source** for [[Criterion Profile Analysis]], previously footed only on the meta-analytic extension [[wiernik-et-al-2021-meta-analytic-cpa|Wiernik et al. (2021)]] (MACPA). This is the **contrastive** flavor of [[Configural Relationships]]. Its cross-validation caution links to [[Cross-Validation]] and [[Overfitting]]; its predictor-pattern framing is a methodological cousin to lens-model/linear-judgment work already in the vault.
