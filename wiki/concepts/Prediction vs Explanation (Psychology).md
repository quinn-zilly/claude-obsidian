---
address: c-000151
type: concept
title: "Prediction vs Explanation (Psychology)"
aliases: ["Prediction-Explanation Tension", "Explanatory vs Predictive Science"]
tags: [concept, methodology, machine-learning, psychology, open-science]
status: developing
created: 2026-05-22
updated: 2026-05-22
related: ["[[Overfitting]]", "[[Cross-Validation]]", "[[Regularization]]", "[[Bias-Variance Tradeoff]]", "[[Replication Crisis]]", "[[P-hacking]]", "[[Questionable Research Practices]]", "[[yarkoni-westfall-2017-prediction-vs-explanation]]"]
---

# Prediction vs Explanation (Psychology)

The tension between two scientific goals in psychology — *explanation* (identifying causal mechanisms that give rise to behavior) and *prediction* (accurately forecasting unobserved behavior) — and the argument that psychology's near-exclusive focus on explanation has produced a field populated by intricate mechanistic theories with little verifiable predictive power.

**Primary source:** [[yarkoni-westfall-2017-prediction-vs-explanation]] (Yarkoni & Westfall, 2017)

## The Tension

Although explanation and prediction are *philosophically compatible* (a good causal model should also predict well), they are often in **statistical and pragmatic tension**:

1. The model that most closely approximates the data-generating process is not necessarily the best predictor of future observations (due to [[Overfitting]])
2. A biased, psychologically implausible model can systematically outperform a mechanistically accurate but complex model
3. There is no guarantee that psychological phenomena are simple enough to be well approximated by human-comprehensible models

## Two Scientific Cultures (Breiman 2001)

| Culture | Assumption | Goal |
|---------|-----------|------|
| **Data modeling** (explanatory) | Data arise from a specific process | Estimate true parameters of that process |
| **Algorithmic modeling** (predictive) | Process is unknown/unknowable | Find algorithm that produces same outputs from same inputs |

Psychology belongs almost entirely to the data modeling culture. Machine learning belongs to the algorithmic culture. Yarkoni & Westfall argue for greater balance.

## How Explanatory Focus Produces Poor Prediction

1. **In-sample fit ≠ out-of-sample prediction.** R² and other fit indices assess how well the model form generalizes, not how well the fitted equation predicts new data. See [[Training vs Test Error]].
2. **[[Procedural Overfitting]].** Flexible analytical practices (p-hacking, optional stopping, covariate selection) capitalize on sample-specific noise, producing findings that don't replicate.
3. **Small samples.** Small samples produce high-variance estimates; the "decline effect" reflects regression to the mean as larger samples emerge.

## Machine Learning's Answer

The ML community treats *out-of-sample prediction error* as the gold standard. Key tools:
- **[[Cross-Validation]]** — estimate generalization performance without collecting new data
- **[[Regularization]]** — deliberately introduce bias to reduce variance
- **[[Bias-Variance Tradeoff]]** — principled framework for managing the exploration-accuracy tradeoff
- **Large samples** — the single most reliable protection against overfitting

## Implications for Research Practice

- Applied psychology domains (I/O, clinical, educational) should routinely report cross-validated predictive accuracy alongside significance tests
- Even in explanatory research, ML techniques provide instrumental value: better model selection, reduced p-hacking, interpretability tools
- Predictive models can reveal structure of the parameter space (sparse vs. dense, linear vs. nonlinear)
- Well-designed randomized experiments remain the gold standard for causal inference

## Connections

- [[Replication Crisis]] — replication failures are, in part, a predictive failure: models that "explain" an initial sample fail to predict the same behavior in subsequent samples
- [[P-hacking]] — reframed as [[Procedural Overfitting]]: the human analyst is a flexible model capitalizing on noise
- [[Questionable Research Practices]] — systematic bias toward in-sample fit over out-of-sample prediction
- [[HARKing]] — presents post-hoc pattern recognition as a priori hypothesis, obscuring the true (overfit) test error
- [[Open Science]] — preregistration is a bias-increasing, variance-decreasing intervention; it constrains the analyst's flexibility
