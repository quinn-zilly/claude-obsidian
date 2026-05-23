---
address: c-000152
type: concept
title: "Overfitting"
aliases: ["Model Overfitting", "Overfitted Model"]
tags: [concept, machine-learning, methodology, statistics]
status: developing
created: 2026-05-22
related: ["[[Training vs Test Error]]", "[[Cross-Validation]]", "[[Bias-Variance Tradeoff]]", "[[Regularization]]", "[[Procedural Overfitting]]", "[[Prediction vs Explanation (Psychology)]]", "[[P-hacking]]", "[[yarkoni-westfall-2017-prediction-vs-explanation]]"]
---

# Overfitting

The tendency for a statistical model to fit sample-specific noise as if it were signal, producing parameter estimates that perform well on the training data but generalize poorly to new observations. Minimizing overfitting is one of the primary objectives of machine learning.

**Primary source:** [[yarkoni-westfall-2017-prediction-vs-explanation]] (Yarkoni & Westfall, 2017)

## Mechanism

In any sample, the relationship between variables is shaped by both true signal and sampling/measurement error. Because OLS regression minimizes the sum of squared errors *in the training sample*, the estimated coefficients will partially capture error patterns that are idiosyncratic to that sample and absent from the population. The result: the fitted model systematically overstates its own predictive accuracy.

**Key distinction:**
- R² estimates performance of the *model form* (averaged over hypothetical replications with fresh parameter estimates)
- **Test error** measures performance of the *specific fitted equation* on new data — and is virtually always larger

## Severity by Conditions

| Condition | Overfitting severity |
|-----------|---------------------|
| Many predictors, small N, small effects | Extreme |
| Few predictors, large N, large effects | Negligible |

**Concrete example (Yarkoni & Westfall):** N=50, p=20, r=0.10 per predictor
- Observed R² = 0.45 (massive overfit)
- True population R² = 0.07
- Out-of-sample R² = 0.02
- Even adjusted R² ≈ 0.07 — still 3.5× larger than out-of-sample estimate

## Visualizing Overfitting

A 10th-order polynomial fit to data with a linear true function captures illusory curves — "hallucinating" patterns that exist only in the training sample. Training MSE decreases, but test MSE explodes.

## Overfitting in Psychology

Psychology's typical study design (small N, multiple predictors, flexible analysis) creates ideal conditions for overfitting. The ongoing [[Replication Crisis]] is, in part, a consequence: models that appear to explain behavior in one sample systematically fail to predict the same behavior in new samples.

## Solutions

- **[[Cross-Validation]]** — estimate test error directly by training and testing on different data folds
- **[[Regularization]]** — constrain model complexity; trade some bias for variance reduction
- **Larger samples** — most reliable protection; more data = less room for noise to masquerade as signal
- **[[Preregistration]]** — constrains procedural overfitting by fixing analysis decisions in advance

## Related Concepts

- **[[Procedural Overfitting]]** — overfitting via flexible analysis choices rather than model estimation
- **[[Bias-Variance Tradeoff]]** — formal decomposition of prediction error into bias and variance components
- **[[Training vs Test Error]]** — the fundamental gap that overfitting produces
- **[[P-hacking]]** — a form of procedural overfitting
