---
address: c-000349
type: concept
title: "Coefficient Omega"
tags: [concept, psychometrics, reliability, measurement]
status: evergreen
created: 2026-06-01
updated: 2026-07-07
related: ["[[Likert Scale Development]]", "[[Item Response Theory]]", "[[Reliability]]", "[[Coefficient Alpha]]", "[[jebb-ng-tay-2021-likert-scale-advances]]"]
sources:
  - "[[jebb-ng-tay-2021-likert-scale-advances]]"
  - "[[revelle-condon-2019-reliability-alpha-to-omega]]"
---

# Coefficient Omega

Nav: [[index]] | [[log]]

## What It Is

A reliability estimator (McDonald 1999) that uses a **congeneric factor model** — it does not assume all items have equal factor loadings (tau-equivalence). Preferred over coefficient alpha for most psychological scales.

## Why Alpha Falls Short

Coefficient alpha (Cronbach 1951) assumes **tau-equivalence**: all items have identical factor loadings (i.e., equal true score variance). This assumption is "rare for psychological scales" (Dunn et al. 2014). When violated, alpha *underestimates* true reliability. The bias worsens with:
- Fewer items
- Greater between-item differences in population factor loadings

## Omega's Advantages

- Uses congeneric model — loadings allowed to vary
- Performs at least as well as alpha when alpha's assumptions hold (Zinbarg et al. 2005)
- More accurate for typical psychological scales
- Hierarchical omega available for multidimensional scales

## Two omegas (Revelle & Condon 2019)

[[revelle-condon-2019-reliability-alpha-to-omega|Revelle & Condon (2019)]] disentangle McDonald's (1999) confusingly co-named coefficients:

- **$\omega_h$ (hierarchical omega)** — variance due to the **single general factor**; answers "how much of my total score reflects one common thing?"
- **$\omega_t$ (total omega)** — total reliable (common) variance; an estimate of the **greatest lower bound (glb)**, ≈ the best split-half.

Computed via **bifactor** ($\omega_g$, slightly higher) or **Schmid–Leiman** ($\omega_h$). For very low general-factor saturation, the EFA-based estimate is positively biased — prefer a **CFA-based** estimate. Report *both* $\omega_h$ and $\omega_t$: they answer different questions, and neither collapses to α except under [[Coefficient Alpha|tau-equivalence]].

## Caveat

Omega requires a **good-fitting factor model**. If the factor model fits poorly, omega estimates are unreliable.

## Computation

- **R:** `psych` package — `omega()` function; use `omega.tot` for unidimensional scales (Revelle 2008)
- **Excel:** walkthrough in McNeish (2018)
- **Confidence intervals:** use `ci.reliability()` in the MBESS package with bootstrapped CIs (Kelley & Pornprasertmanit 2016)
- **Outlier-robust estimation:** Zhang & Yuan (2016) R package handles outliers and missing data

## Other Reliability Issues

- **Transient error:** alpha is computed at one time point and cannot correct for mood/occasion fluctuations. Alternatives: test-retest alpha (Green 2003), coefficient of equivalence and stability (Schmidt et al. 2003)
- **Standard error of measurement:** Cronbach & Shavelson (2004) argue this should be reported alongside any coefficient — especially for cut-score decisions
- **Item-level reliability:** can be computed per item to identify unreliable items (Zijlmans et al. 2018); correction for attenuation and Molenaar-Sijtsma methods perform best

## Key Papers
- McDonald (1999) — original omega
- McNeish (2018) — essential tutorial (R + Excel)
- Dunn et al. (2014) — "from alpha to omega"
- Zinbarg et al. (2005) — comparison with alpha
- Kelley & Pornprasertmanit (2016) — CIs for reliability
- Cronbach & Shavelson (2004) — limits of reliability coefficients

## Sources
- [[jebb-ng-tay-2021-likert-scale-advances]]
