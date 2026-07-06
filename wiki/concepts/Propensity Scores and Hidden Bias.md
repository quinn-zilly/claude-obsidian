---
address: c-000891
type: concept
title: "Propensity Scores and Hidden Bias"
tags:
  - concept
  - research-methods
  - causal-inference
  - quasi-experiments
  - statistics
status: seed
created: 2026-07-06
updated: 2026-07-06
related:
  - "[[Quasi-Experimental Design]]"
  - "[[Nonequivalent Control Group Design]]"
  - "[[Selection Bias]]"
  - "[[Matching (Quasi-Experiments)]]"
sources:
  - "[[shadish-cook-campbell-2002-quasi-designs-control-and-pretests]]"
---

# Propensity Scores and Hidden Bias

Nav: [[index]] | [[log]]

A statistical adjustment for nonequivalent groups (SCC Ch. 5 appendix). A **propensity score** is the predicted probability of being in the treatment (vs. control) group, from a logistic regression on measured covariates. It collapses many covariates into one number, so you can **match, stratify, or covary** on it to balance groups.

Governing motto: **"statistical adjustment only after the best possible design controls have been used."**

## Using the score

- **Matching** — pair treated and control units on the score (optimal matching minimizes aggregate distance).
- **Stratifying** — ~5 strata (quintiles) remove ~90% of the bias due to the covariate (Cochran 1968).
- **Covariance** — enter the score in ANCOVA; efficient *if* the model is correctly specified, but can worsen bias if not. Matching/stratifying + covariance combined is the most robust.

Include **all** predictors of selection that are related to outcome (even weak or nonsignificant ones); getting the *set* right matters more than getting the functional form right.

## The hidden-bias limit

The crucial caveat: propensity scores balance groups **only on observed covariates**. Random assignment balances observed **and** unobserved covariates in expectation; propensity adjustment leaves **hidden bias** from any unmeasured confounder of both selection and outcome. This is a strong assumption and is rarely fully satisfiable.

## Sensitivity analysis

Because hidden bias can't be removed or even detected directly, **sensitivity analysis** (Rosenbaum) asks: *how large* would a hidden bias have to be to overturn the result? It reports how far significance could depart from the randomized case as the assignment probability departs from .50. It indicates a study's *vulnerability* to bias, not whether bias is present.

## Related adjustment families

- **Selection-bias models** (Heckman) — selection + outcome equations, can model correlated errors; highly assumption-sensitive and often fail to match randomized benchmarks (LaLonde 1986). See [[Selection Bias]].
- **Latent-variable SEM** — corrects measurement unreliability; still only as good as the design.

All three developed in separate disciplines (statistics, econometrics, psychometrics) but are closely related (Winship & Morgan 1999).
