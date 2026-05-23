---
address: c-000153
type: concept
title: "Cross-Validation"
aliases: ["K-Fold Cross-Validation", "Leave-One-Out Cross-Validation", "LOOCV", "K-Fold CV"]
tags: [concept, machine-learning, methodology, statistics]
status: developing
created: 2026-05-22
related: ["[[Overfitting]]", "[[Training vs Test Error]]", "[[Regularization]]", "[[Bias-Variance Tradeoff]]", "[[Procedural Overfitting]]", "[[Prediction vs Explanation (Psychology)]]", "[[Analytic Reproducibility]]", "[[Preregistration]]", "[[yarkoni-westfall-2017-prediction-vs-explanation]]"]
---

# Cross-Validation

A family of techniques that estimate a model's out-of-sample prediction error (test error) by training and testing on different subsets of the available data. The most fundamental tool for quantifying whether a model generalizes beyond the sample used to fit it.

**Primary source:** [[yarkoni-westfall-2017-prediction-vs-explanation]] (Yarkoni & Westfall, 2017)

## Core Problem Solved

In psychology, model performance is almost always assessed on the same data used to fit the model — producing an optimistic, overfit estimate of predictive accuracy (see [[Training vs Test Error]]). Cross-validation provides a minimally biased estimate of true out-of-sample performance without requiring new data collection.

## Variants

### Hold-Out Split
Randomly partition data into *training* (fit model) and *test* (evaluate model) sets. Unbiased estimate of test error, but wastes half the data. Risk of underfitting due to smaller training set.

### K-Fold Cross-Validation
1. Randomly divide data into K equal-sized folds
2. Train on K-1 folds, test on the held-out fold
3. Repeat K times, each fold serving as the test set once
4. Average the K test-error estimates

Most common: K=5 or K=10. Provides efficient use of all data while maintaining separation between training and testing.

### Leave-One-Out Cross-Validation (LOOCV)
K = N (sample size). Fit model N times, each time leaving out one observation and predicting its score. Used in small-sample settings or specific applications (e.g., Rissman et al., 2010, fMRI memory study).

## Key Properties

- **Applicable to virtually any estimator** — unlike AIC/BIC, does not require a tractable likelihood function; works for regression, SEM, random forests, neural networks
- **Guards against both estimation-stage and procedural overfitting** — but only if all researcher degrees of freedom are embedded *within* the CV loop (not just the final model)
- **Non-deterministic results** — different random folds produce slightly different estimates; this reflects real estimation uncertainty, not a weakness

## Cross-Validation vs. Replication

Traditional independent replication is cross-validation's canonical form (train in sample 1, test in sample 2). But independent replication is expensive and slow. K-fold CV provides most of the benefit at no extra data-collection cost — though it estimates generalization within the same population/context rather than across populations.

## Limitations

1. **Computational cost** — each model must be fit K times
2. **Slight underestimation** — CV can underestimate out-of-sample performance (related to [[Bias-Variance Tradeoff]])
3. **Still subject to procedural overfitting** — if analyst selects the model with the best CV score from many tried, overfitting remains (though attenuated); nested CV or hold-out sets needed for full protection
4. **Information leakage** — even innocuous preprocessing steps (e.g., standardizing full dataset before CV) can leak test-set information into training

## Usage in Psychology (at time of writing)

Largely absent from mainstream psychology despite having roots in the field since the 1940s (Mosier, 1951: "the effectiveness of the predictor-composite *must* be determined on a separate, independent sample"). Essentially mandatory in applied machine learning.

## Connections

- [[Overfitting]] — the problem CV is designed to detect and quantify
- [[Regularization]] — CV often used to select the regularization penalty parameter
- [[Procedural Overfitting]] — CV controls this only when analyst df are inside the CV loop
- [[Analytic Reproducibility]] — CV is a within-study reproducibility check
- [[Preregistration]] — complementary tools; preregistration constrains procedural choices, CV quantifies predictive accuracy
- [[Replication Crisis]] — widespread failure to use CV is one mechanism behind the replication crisis
