---
address: c-000156
type: concept
title: "Training vs Test Error"
aliases: ["Test Error", "Training Error", "Out-of-Sample Error", "Generalization Error"]
tags: [concept, machine-learning, methodology, statistics]
status: developing
created: 2026-05-22
updated: 2026-05-22
related: ["[[Overfitting]]", "[[Cross-Validation]]", "[[Bias-Variance Tradeoff]]", "[[Prediction vs Explanation (Psychology)]]", "[[yarkoni-westfall-2017-prediction-vs-explanation]]"]
---

# Training vs Test Error

The fundamental distinction between a model's performance on the data used to fit it (training error) and its performance on new, unseen data (test error). The gap between these two quantities is what overfitting produces.

**Primary source:** [[yarkoni-westfall-2017-prediction-vs-explanation]] (Yarkoni & Westfall, 2017)

## Definitions

- **Training error** — prediction error computed on the same dataset used to estimate the model parameters. In psychology, model fit statistics (R², χ², RMSEA) are almost always training error.
- **Test error** (generalization error) — prediction error computed on new data not used in model fitting. The quantity researchers actually care about.

## Why the Gap Matters

The values of fitted parameters (b₀, b₁, b₂) are selected to minimize error *in the training sample*. They will always fit noise specific to that sample along with signal. When those same coefficients are applied to a new sample, the noise component of the fit is no longer useful — test error will be higher.

> Test error will almost always be larger than training error.

## R² Misunderstands This Distinction

R² answers the question: "In repeated random samples, if I fit this *model form* fresh each time, how much variance will I reduce on average?" It does *not* answer: "How well does this specific fitted equation predict new data?"

This is why R²=0.45 in a training sample might correspond to R²=0.02 out of sample — adjusted R² corrects for the form/fitted-equation confusion but still overstates out-of-sample accuracy.

## Estimating Test Error

Rather than assuming training error approximates test error, machine learning requires explicit estimation of test error — typically via [[Cross-Validation]].

## Connections

- [[Overfitting]] — the process by which training error becomes an unreliable proxy for test error
- [[Cross-Validation]] — the standard method for estimating test error without collecting new data
- [[Replication Crisis]] — at scale, failed replications are failed out-of-sample predictions; the field confused training error (initial study fit) with test error
