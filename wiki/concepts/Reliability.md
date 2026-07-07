---
address: c-001000
type: concept
title: "Reliability"
aliases: ["reliability theory", "test reliability", "reliability coefficient"]
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
  - "[[Coefficient Alpha]]"
  - "[[Construct Validity]]"
  - "[[Attenuation]]"
sources:
  - "[[revelle-condon-2019-reliability-alpha-to-omega]]"
---

# Reliability

Nav: [[index]] | [[log]]

**Reliability** is the ratio of reliable (signal) variance to total (signal + noise) variance in a set of measurements — the extent to which scores taken at one time/place with one instrument predict scores at another (Spearman 1904b; [[revelle-condon-2019-reliability-alpha-to-omega|Revelle & Condon 2019]]). Formally, decomposing $X = \tau + \epsilon$, reliability $= \sigma^2_\tau / \sigma^2_X$.

## Not a property of the test

Reliability is a **joint function of the test AND the sample**. Because it is a variance ratio, increasing between-person variance (without increasing error) raises it, and restricting range lowers it. The same instrument has different reliabilities in different populations.

## Consequences of low reliability

- **Attenuates observed correlations**: the correlation between latent constructs is recovered by correction for [[Attenuation|attenuation]], $\rho_{\xi\eta} = r_{xy}/\sqrt{r_{xx}r_{yy}}$.
- **Biases individual scores** and widens confidence intervals via the standard error of measurement $\sigma_e = \sigma_x\sqrt{1-r_{xx}}$.
- Schmidt & Hunter (1996) list 26 ways failing to correct for reliability retards research progress. (Borsboom & Mellenbergh 2002 dissent: classical corrections can themselves mislead.)

## There is no single reliability

Reliable between-person variance mixes **Trait + State + specific** variance. Different designs isolate different pieces:

- **Internal consistency** (one test, one occasion): [[Coefficient Alpha]], Guttman's $\lambda$'s, split-half, and model-based [[Coefficient Omega|omega]].
- **Test–retest**: *dependability* (short delay) vs *stability* (long delay).
- **Inter-rater**: intraclass correlations (ICC) for continuous ratings, Cohen's κ for categorical.

The right estimate depends on what is measured, whom, where, and when.

## Relation to validity

Reliability is **necessary but not sufficient** for [[Construct Validity|validity]]. A perfectly reliable score can still measure the wrong construct; an unreliable one caps the validity coefficient (an inference cannot be more valid than the measure is reliable — the [[binning-barrett-1989-validity-personnel-decisions|Binning & Barrett]] inferential chain presupposes reliable measures at each node).

Primary source: [[revelle-condon-2019-reliability-alpha-to-omega]].
