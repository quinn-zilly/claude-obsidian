---
address: c-000148
type: source
title: "Choosing Prediction Over Explanation in Psychology: Lessons From Machine Learning"
authors: ["Tal Yarkoni", "Jacob Westfall"]
year: 2017
journal: "Perspectives on Psychological Science"
volume: 12
issue: 6
pages: "1100–1122"
doi: "10.1177/1745691617693393"
tags: [source, open-science, machine-learning, methodology, prediction, psychology]
status: evergreen
created: 2026-05-22
updated: 2026-05-22
related: ["[[Prediction vs Explanation (Psychology)]]", "[[Overfitting]]", "[[Cross-Validation]]", "[[Regularization]]", "[[Bias-Variance Tradeoff]]", "[[Procedural Overfitting]]", "[[Training vs Test Error]]", "[[Replication Crisis]]", "[[P-hacking]]", "[[Questionable Research Practices]]", "[[Tal Yarkoni]]", "[[Jacob Westfall]]"]
---

# Yarkoni & Westfall (2017) — Choosing Prediction Over Explanation in Psychology

**Citation:** Yarkoni, T., & Westfall, J. (2017). Choosing prediction over explanation in psychology: Lessons from machine learning. *Perspectives on Psychological Science*, *12*(6), 1100–1122. https://doi.org/10.1177/1745691617693393

## Core Argument

Psychology has near-exclusively prioritized *explanation* (identifying causal mechanisms) over *prediction* (accurately forecasting unobserved behavior). This focus, combined with small samples and flexible analytic practices, produces intricate mechanistic theories with little (or unknown) out-of-sample predictive accuracy. The paper argues that importing core concepts from machine learning — overfitting, cross-validation, regularization — would make psychology a more rigorous and ultimately more explanatory science.

> [!key-insight] Central claim
> Explanation and prediction are *statistically and pragmatically in tension*, not just philosophically compatible. The model that best approximates the data-generating process is not necessarily the best predictor of future behavior (due to overfitting). Psychology has reflexively chosen explanation without giving serious consideration to predictive approaches.

## Key Concepts Introduced

### 1. Overfitting and the Goodness-of-Fit Illusion

R² estimated in-sample systematically overstates out-of-sample predictive accuracy. The R² statistic estimates the performance of the *model form* (equation 1), not the performance of the *fitted model* (equation 2) applied to new data. The gap between training error and **test error** grows as:
- number of predictors increases
- sample size decreases  
- effect sizes are small

**Dramatic example:** With N=50 and 20 predictors each r=0.10 with DV, observed R²=0.45, true R²=0.07, out-of-sample R²=0.02 — a 22× overestimate.

### 2. p-hacking as Procedural Overfitting

The authors reframe p-hacking as a *special case of overfitting* — procedural overfitting — that occurs before model estimation: during data cleaning, model selection, covariate inclusion decisions. The human analyst capitalizing on idiosyncratic data patterns is structurally identical to a flexible statistical model doing the same. The "garden of forking paths" (Gelman & Loken, 2013) is the mechanism.

### 3. Bias-Variance Tradeoff

Total prediction error = bias² + variance. The explanatory approach minimizes bias but ignores variance — producing high-variance models that are unstable across samples. Machine learning minimizes *total prediction error*, which often means accepting some bias to drastically reduce variance. Connections: multilevel models "shrink" cluster estimates toward the population mean (deliberate bias); unit-weighting outperforms OLS in low-N/high-p situations.

### 4. Big Data as Overfitting Protection

Larger samples guard against overfitting because they are more representative of the population. The "decline effect" (effect sizes shrinking as fields mature) is explained not by sloppier research but by the fact that small-sample studies are massively overfitted. The authors endorse large-sample collaborative projects over small-sample single-lab studies.

### 5. Cross-Validation

K-fold cross-validation — partitioning data into training/test folds — provides an unbiased estimate of out-of-sample prediction error without requiring new data collection. It can guard against both model-estimation overfitting and procedural overfitting (if analyst degrees of freedom are embedded *within* the CV loop). Practically absent from psychology at time of writing.

### 6. Regularization

Penalized regression methods (lasso, ridge) deliberately introduce bias to reduce variance. Lasso shrinks small coefficients to zero, producing sparse solutions that generalize better when p is large relative to n. The penalty parameter controls the bias-variance tradeoff. Lasso outperforms OLS in dense, low-n/high-p settings; advantage diminishes in large, sparse datasets.

### 7. Psychology as a Predictive Science

Applied examples:
- **Personality from Facebook Likes** (Kosinski et al., 2013): 58,000 users; cross-validated r=0.29–0.43 for Big Five traits
- **Implicit memory recognition via fMRI** (Rissman et al., 2010): LOOCV; brain data predicts subjective ratings (90% accuracy) but not objective old/new status
- Decision trees and feature-set comparison as interpretability tools
- Predictive accuracy as consensus metric for comparing non-nested models (replaces AIC/BIC)

### 8. Two Cultures in Statistics (Breiman 2001)

"Data modeling culture" (explanatory; estimate true parameters) vs. "algorithmic modeling culture" (predictive; minimize output error regardless of mechanism). Psychology belongs entirely to the first; the paper advocates balanced adoption of the second.

## Position in the Replication Crisis Literature

The paper provides a *statistical mechanism* for why the replication crisis happened: psychology systematically confuses in-sample fit (training error) with out-of-sample prediction (test error). This complements:
- [[P-hacking]] (Simmons et al. 2011) — procedural overfitting
- [[Questionable Research Practices]] (Nosek et al. 2022)
- [[Replication Crisis]] (OSC 2015)
- [[HARKing]] (Kerr 1998)
- [[Publication Bias]]

## Limitations and Caveats

- Not arguing prediction should *replace* explanation; randomized experiments remain gold standard for causal inference
- Prediction-focused approaches not appropriate for all research questions
- Cross-validation is not a panacea: doesn't eliminate overfitting when analyst degrees of freedom fall *outside* the CV loop; can underestimate out-of-sample performance; computationally expensive for complex models
- No free lunch: lasso can hurt when sample is large relative to predictors and penalty is poorly tuned

## Methods / Code Resources

Python and R tutorials available at http://github.com/tyarkoni/PPS2016

## Pages Created / Updated

**Created:** [[Prediction vs Explanation (Psychology)]], [[Overfitting]], [[Cross-Validation]], [[Regularization]], [[Bias-Variance Tradeoff]], [[Training vs Test Error]], [[Procedural Overfitting]], [[Tal Yarkoni]], [[Jacob Westfall]]

**Updated:** [[Replication Crisis]], [[P-hacking]], [[Questionable Research Practices]], [[HARKing]]
