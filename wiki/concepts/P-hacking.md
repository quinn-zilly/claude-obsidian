---

type: concept
address: c-000047
title: "P-hacking"
tags:
  - open-science
  - statistics
  - research-methods
  - replication-crisis
status: developing
related:
  - "[[HARKing]]"
  - "[[Publication Bias]]"
  - "[[Preregistration]]"
  - "[[Analytic Reproducibility]]"
  - "[[Replication Crisis]]"
  - "[[munafo-2017-manifesto]]"
  - "[[nosek-2018-preregistration]]"
created: unknown
updated: unknown
---

# P-hacking

P-hacking (also called **data dredging** or **analytic flexibility**) is the practice of making analytical decisions — consciously or unconsciously — that increase the probability of obtaining a statistically significant result (p < .05).

## Mechanisms

P-hacking does not require deliberate fraud. It arises naturally from the combination of:
- Many legitimate analytical choices (exclusion criteria, covariate sets, measurement operationalizations, analysis window endpoints)
- Confirmation and hindsight bias (analysts accept results matching expectations, reject others as "artifacts")
- Incentives that reward significant results

### The Garden of Forking Paths (Gelman & Loken)

In a multi-decision analysis pipeline, each choice point forks the path. With 10 binary decisions, there are 2^10 = 1,024 possible analyses. If the researcher implicitly selects the path that yields p < .05, they are effectively running 1,024 tests while reporting one — severely inflating the false-positive rate.

### Common Forms

- **Outcome switching**: select from multiple measured outcomes the one showing significance
- **Selective exclusion**: drop outliers until results are significant
- **Covariate mining**: add/remove covariates until p < .05
- **Subgroup searching**: find the subgroup within which the effect is significant
- **Optional stopping**: continue data collection until p < .05, then stop

## Detection

- **p-curve analysis**: a p-curve skewed right (many p values just below .05) suggests p-hacking
- **Multiverse analysis** (analytic robustness): run all defensible analytic paths; p-hacked results fragment across paths
- Pre-registration comparison: compare registered and published analyses

## Relationship to Replication Failure

P-hacking is one of the primary causes of failed replications ([[Replication Crisis]]). When an original result was p-hacked, it does not reflect a true effect — and a straightforward replication finds nothing. The [[open-science-collaboration-2015]] effect size decline is consistent with p-hacking inflating original estimates.

## Distinction from HARKing

- **P-hacking**: analytical flexibility at the data analysis stage
- **[[HARKing]]**: hypothesis reformulation after seeing results; occurs at the write-up stage

Both can occur in the same study and are often difficult to separate.

## Remedies

- [[Preregistration]]: commit to analysis plan before data collection
- [[Registered Reports]]: analysis plan reviewed before results known
- Multiverse analysis (analytic robustness): report all defensible analyses
- Larger samples: reduces the payoff from p-hacking because genuine effects emerge more reliably

## Reframing as Procedural Overfitting

Yarkoni & Westfall (2017) reframe p-hacking as a special case of [[Overfitting]] — specifically **[[Procedural Overfitting]]** — that operates at the human-analyst level rather than the model-estimation level. The analyst capitalizing on idiosyncratic sample patterns is structurally identical to a flexible statistical model doing the same. This framing connects p-hacking to the machine learning literature on [[Bias-Variance Tradeoff]] and suggests analogous solutions: constraining flexibility (preregistration) and testing out-of-sample (cross-validation).

## See Also

- [[HARKing]]
- [[Publication Bias]]
- [[Preregistration]]
- [[Analytic Reproducibility]]
- [[Procedural Overfitting]] — Yarkoni & Westfall's reframing
- [[Overfitting]] — the statistical framework underlying procedural overfitting
- [[Bias-Variance Tradeoff]] — p-hacking = low-bias/high-variance analytic strategy
