---
address: c-001011
type: concept
title: "Attenuation"
aliases: ["attenuation", "correction for attenuation", "disattenuation"]
tags:
  - concept
  - psychometrics
  - reliability
  - measurement
status: stub
created: 2026-07-07
updated: 2026-07-07
related:
  - "[[Reliability]]"
  - "[[Coefficient Omega]]"
sources:
  - "[[revelle-condon-2019-reliability-alpha-to-omega]]"
---

# Attenuation

Nav: [[index]] | [[log]]

**Attenuation** is the systematic *underestimation* of the correlation between two constructs caused by unreliability (measurement error) in their observed measures. Spearman (1904b) developed reliability theory precisely to correct for it.

The **correction for attenuation** recovers the estimated latent (construct-level) correlation:

$$\rho_{\xi\eta} = \frac{r_{xy}}{\sqrt{r_{xx}\,r_{yy}}}$$

where $r_{xy}$ is the observed correlation and $r_{xx}, r_{yy}$ the reliabilities of the two measures. Lower reliability → more attenuation → a larger upward correction.

Failing to account for attenuation retards research in many ways (Schmidt & Hunter 1996 list 26). Borsboom & Mellenbergh (2002) caution that classical corrections can themselves mislead when the true-score ≠ construct-score assumption is wrong.

Primary source: [[revelle-condon-2019-reliability-alpha-to-omega]].
