---
address: c-000154
type: concept
title: "Regularization"
aliases: ["Penalized Regression", "Lasso", "Ridge Regression", "Shrinkage"]
tags: [concept, machine-learning, methodology, statistics]
status: developing
created: 2026-05-22
related: ["[[Overfitting]]", "[[Bias-Variance Tradeoff]]", "[[Cross-Validation]]", "[[Training vs Test Error]]", "[[Prediction vs Explanation (Psychology)]]", "[[yarkoni-westfall-2017-prediction-vs-explanation]]"]
---

# Regularization

A class of techniques that constrain or penalize a statistical model's complexity, deliberately introducing bias to reduce variance — and thereby reduce total prediction error, especially when the number of predictors is large relative to the sample size.

**Primary source:** [[yarkoni-westfall-2017-prediction-vs-explanation]] (Yarkoni & Westfall, 2017)

## Core Idea

In OLS regression, the only objective is minimizing sum of squared residuals. In regularized regression, an additional *penalty term* is added to the cost function, forcing the model to balance fit against complexity. As the penalty increases, the model becomes sparser/simpler; some variance is sacrificed for bias, but total prediction error often decreases.

This is a direct operationalization of the [[Bias-Variance Tradeoff]]: regularization is the knob that moves a model from low-bias/high-variance to high-bias/low-variance.

## Major Regularization Methods

### Lasso Regression (L1 Penalty)
Cost function: minimize Σ(yᵢ - ŷᵢ)² + λ·Σ|βⱼ|

- Penalty proportional to *sum of absolute values* of coefficients
- Effect: "shrinks" small coefficients exactly to zero → sparse solutions (subset of predictors retained)
- Interpretable: results in a small set of predictors with non-trivial effects
- Best when true signal is sparse (few variables matter)

### Ridge Regression (L2 Penalty)
Cost function: minimize Σ(yᵢ - ŷᵢ)² + λ·Σβⱼ²

- Penalty proportional to *sum of squared* coefficients
- Effect: shrinks all coefficients toward zero, but rarely to exactly zero
- Best when many predictors each contribute small amounts (dense signal)

### Elastic Net
Combines L1 and L2 penalties; useful when predictors are correlated.

## When Regularization Helps

Regularization is most beneficial when:
- Number of predictors (p) is large relative to sample size (N)
- True signal is sparse (lasso) or diffuse (ridge)
- OLS overfits severely (large gap between training and test error)

Regularization provides little advantage when:
- N is very large relative to p
- True effects are large and well-identified
- Model is already sparse

## The Penalty Parameter λ

Controls the bias-variance tradeoff:
- λ = 0 → OLS (no regularization)
- λ → ∞ → all coefficients = 0 (maximum regularization, maximum bias)
- Optimal λ typically selected via [[Cross-Validation]]

## Regularization as Shrinkage (Psychology Examples)

Psychologists already use regularized estimation without always recognizing it:

1. **Multilevel models** — "shrink" cluster-level estimates toward the grand mean; deliberate bias that improves out-of-sample performance for individual clusters
2. **Unit-weighting** — assigning equal coefficients to all predictors; highly biased but often outperforms OLS when N is small (Dawes, 1979; Wainer, 1976)
3. **Bayesian priors** — placing informative priors on parameters is regularization in Bayesian terms

## Interpretability Trade-off

Regularized methods are sometimes dismissed as "black boxes," but:
- Lasso produces *sparse*, interpretable solutions
- The penalty parameter provides explicit control over model complexity
- Comparing models with different features retained (feature importance analysis) is an interpretability tool analogous to hierarchical regression
- If lasso outperforms ridge → signal is sparse; if GAMs/SVM/forests outperform regression → nonlinearities exist

## Connections

- [[Overfitting]] — the problem regularization solves
- [[Bias-Variance Tradeoff]] — regularization is the primary mechanism for navigating this tradeoff
- [[Cross-Validation]] — used to select optimal penalty parameter; also estimates regularized model performance
- [[Prediction vs Explanation (Psychology)]] — regularization embodies the predictive approach: biased but better generalizing
