---
address: c-000155
type: concept
title: "Bias-Variance Tradeoff"
aliases: ["Bias-Variance Decomposition", "Bias Variance"]
tags: [concept, machine-learning, methodology, statistics]
status: developing
created: 2026-05-22
related: ["[[Overfitting]]", "[[Regularization]]", "[[Cross-Validation]]", "[[Training vs Test Error]]", "[[Prediction vs Explanation (Psychology)]]", "[[Procedural Overfitting]]", "[[yarkoni-westfall-2017-prediction-vs-explanation]]"]
---

# Bias-Variance Tradeoff

The fundamental decomposition of a model's total prediction error into two components — bias and variance — and the unavoidable tradeoff between them. Increasing a model's bias to reduce its variance (or vice versa) is the core design choice in statistical modeling.

**Primary source:** [[yarkoni-westfall-2017-prediction-vs-explanation]] (Yarkoni & Westfall, 2017)

## Decomposition

**Total prediction error = Bias² + Variance + Irreducible noise**

- **Bias** — systematic tendency to produce answers wrong in a particular direction (e.g., consistently overestimating). Not synonymous with "error" in the pejorative sense; a *deliberate* bias can reduce total prediction error.
- **Variance** — extent to which a model's fitted parameters deviate from their central tendency across different datasets; high variance = unstable, dataset-dependent estimates.

**Dart-throwing analogy (Yarkoni & Westfall):**
- Low bias, low variance = darts clustered at the bullseye ✓
- High bias, low variance = darts clustered away from the bullseye (systematic miss)
- Low bias, high variance = darts scattered around the bullseye
- High bias, high variance = darts scattered away from the bullseye ✗

## The Tradeoff

Increasing bias *decreases* variance: constraining an estimator to prefer certain regions of parameter space prevents it from chasing noise in other regions. Whether this trade improves total error depends on context.

**Flexible models** (low bias) capture real signal but also overfit noise → high variance, large test error.  
**Constrained models** (high bias) miss some real signal but ignore noise → low variance, potentially lower test error.

## Examples in Psychology

| Method | Bias | Variance | Notes |
|--------|------|----------|-------|
| OLS regression | Low | Can be very high when p/N is large | Standard in psychology; ignores variance problem |
| Multilevel models | Deliberate (shrinkage toward mean) | Lower than OLS for cluster effects | Pooling = beneficial bias |
| Lasso regression | Deliberate (shrinks small coefficients to 0) | Lower than OLS | [[Regularization]] operationalizes this |
| Unit-weighting schemes | High | Very low | Often outperform OLS when N is small |
| Preregistration | ↑ bias (constrains analytic choices) | ↓ variance (fewer researcher df) | [[Procedural Overfitting]] control |

## Research Practice Implications

Psychology's explanatory focus = minimizing bias at all costs. But:
- High-variance models are unstable: small changes in data → large changes in conclusions
- This is exactly the situation in which findings fail to replicate across samples
- Machine learning approach: minimize *total prediction error*, accepting bias when it reduces variance

## Connections

- [[Overfitting]] — the high-variance failure mode
- [[Regularization]] — primary tool for deliberately introducing bias to control variance
- [[Cross-Validation]] — used to estimate total prediction error and identify where on the tradeoff curve a model sits
- [[Procedural Overfitting]] — p-hacking = maximally low-bias, maximally high-variance analytic strategy
- [[Preregistration]] — shifts researchers toward higher-bias, lower-variance analytic strategies
