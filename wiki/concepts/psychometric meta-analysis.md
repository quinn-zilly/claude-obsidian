---
address: c-000816
type: concept
title: "psychometric meta-analysis"
aliases: [Hunter-Schmidt Meta-Analysis, Validity Generalization, Psychometric Meta-Analysis]
tags:
  - concept
  - research-methods
  - meta-analysis
  - measurement
  - io-psychology
status: developing
created: 2026-07-03
updated: 2026-07-03
related:
  - "[[Effect Size Heterogeneity]]"
  - "[[MASEM]]"
  - "[[Construct Validity]]"
  - "[[Meta-Research]]"
  - "[[General Factor in Job Performance]]"
  - "[[Frank L. Schmidt]]"
  - "[[Chockalingam Viswesvaran]]"
  - "[[Deniz S. Ones]]"
  - "[[viswesvaran-schmidt-ones-2005-general-factor-job-performance]]"
  - "[[kuncel-et-al-2013-mechanical-vs-clinical]]"
---

# psychometric meta-analysis

**Psychometric meta-analysis** — the **Hunter–Schmidt** method — pools effect sizes across studies and *corrects* them for statistical and measurement **artifacts** so that the estimate reflects the true construct-level relationship rather than the messy observed one. Its signature application is **validity generalization**: showing that a predictor's validity (e.g. a selection test's) holds across settings once artifactual variation is removed, rather than varying situationally.

## The Core Idea

Ordinary (bare-bones) meta-analysis averages observed correlations and attributes leftover variance to real moderators. Hunter and Schmidt argued that most of the *apparent* variation across studies is not real — it is produced by **artifacts** that attenuate and scatter observed effects. Correct for the artifacts first, and much of the "situational specificity" disappears.

## Artifacts Corrected

The method corrects observed effect sizes for, among others:

- **Sampling error** — the dominant source of spurious between-study variance, especially with small samples.
- **Measurement unreliability** — in both the predictor and the criterion; corrected via reliability coefficients (attenuation correction).
- **Range restriction** — restricted variance in the sample (e.g. only hired applicants) shrinks correlations.
- **Dichotomization / imperfect construct measurement** and other study imperfections.

After correction, the mean is a **construct-level** estimate and the residual variance (often summarized by credibility intervals) indicates whether true moderators remain.

## Validity Generalization

The framework's original purpose (Schmidt & Hunter, late 1970s onward) was to refute **situational specificity** — the belief that a test valid in one job/site said nothing about its validity elsewhere. By showing that corrected validities are stable across settings, validity generalization justified using cumulative meta-analytic evidence rather than re-validating a test in every local sample. This reshaped personnel selection practice.

## Why It Matters in This Vault

Psychometric meta-analysis is the **engine** behind several sources here:

- [[viswesvaran-schmidt-ones-2005-general-factor-job-performance|Viswesvaran, Schmidt & Ones (2005)]] pool 90 years of performance-rating intercorrelations and net out four error sources (halo, leniency, random, transient) to isolate a real construct-level [[General Factor in Job Performance|general factor]] — a measurement-model application of the same corrective logic.
- [[kuncel-et-al-2013-mechanical-vs-clinical|Kuncel et al. (2013)]] use Hunter–Schmidt meta-analysis to compare mechanical vs. clinical prediction, correcting for unreliability in predictor and criterion.
- Work-design meta-analyses in the vault (e.g. Humphrey, Nahrgang & Morgeson 2007) likewise use "Schmidt–Hunter psychometric meta-analysis," correcting for unreliability and using composite correlations to avoid double-counting.

## People

- [[Frank L. Schmidt]] — with **John Hunter**, co-developed the method.
- [[Chockalingam Viswesvaran]] and [[Deniz S. Ones]] — prominent appliers (performance measurement, personnel selection, personality at work). Ones bridges the two selection sources above.

## Related Methods

- [[MASEM]] — meta-analytic structural equation modeling, which fits path/SEM models to a meta-analytically pooled correlation matrix (a descendant that goes beyond bivariate correction).
- [[Effect Size Heterogeneity]] — the general question of when residual variance signals real moderators; psychometric correction is one way of accounting for *artifactual* heterogeneity.
- [[Construct Validity]] — artifact correction is fundamentally a move from observed scores toward construct-level (true-score) relationships.

## Caveat

Corrections depend on the **quality of artifact information** (reliability estimates, range-restriction ratios). Poor or borrowed artifact distributions can over- or under-correct, and "construct-level" estimates remain model-dependent — they are corrected *observed* relationships, not ground truth.

## See Also

- [[viswesvaran-schmidt-ones-2005-general-factor-job-performance]]
- [[kuncel-et-al-2013-mechanical-vs-clinical]]
- [[General Factor in Job Performance]]
- [[MASEM]]
- [[Effect Size Heterogeneity]]
- [[Meta-Research]]
