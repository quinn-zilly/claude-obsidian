---
address: c-001001
type: concept
title: "Coefficient Alpha"
aliases: ["Cronbach's alpha", "coefficient alpha", "Guttman lambda-3", "KR-20"]
tags:
  - concept
  - psychometrics
  - reliability
  - measurement
status: developing
created: 2026-07-07
updated: 2026-07-07
related:
  - "[[Coefficient Omega]]"
  - "[[Reliability]]"
sources:
  - "[[revelle-condon-2019-reliability-alpha-to-omega]]"
---

# Coefficient Alpha

Nav: [[index]] | [[log]]

**Coefficient alpha** (Cronbach 1951) — identical to Guttman's (1945) $\lambda_3$ and a generalization of KR-20 — is the most routinely reported reliability estimate. [[revelle-condon-2019-reliability-alpha-to-omega|Revelle & Condon (2019)]] argue this ubiquity is "unfortunate."

$$\alpha = \frac{n}{n-1}\left(1 - \frac{\sum v_i}{V_t}\right)$$

where $V_t$ is total test variance, $v_i$ item variances, $n$ items.

## Two problems

1. **Not an estimate of reliability** except under **tau-equivalence** (all items load equally on one factor) — a condition "rare for psychological scales." When violated, α *underestimates* total reliability but can *overestimate* general-factor saturation.
2. **Not a measure of internal consistency or unidimensionality.** α is only a function of the number of items and the average inter-item correlation. Two unrelated homogeneous subtests can produce a high α. A high α tells you nothing about whether the test measures one thing.

## Historical rationale (now obsolete)

α, $\lambda_3$, and KR-20 were 1930s–50s **computational shortcuts**: on desk calculators it was far easier to compute $n$ item variances + one total variance than the $n(n-1)/2$ covariances or a factor structure. Modern software makes model-based [[Coefficient Omega|omega]] "just as easy," removing the reason to prefer α.

## What to report instead

$\omega_h$ (general-factor saturation) and $\omega_t$ (total reliable variance). See [[Coefficient Omega]]. α remains defensible only when a strong prior establishes tau-equivalence, or as one of several reported estimates.

Confidence intervals: `alpha.ci` (Feldt) / Duhachek & Iacobucci (2004), in the R `psych` package.
