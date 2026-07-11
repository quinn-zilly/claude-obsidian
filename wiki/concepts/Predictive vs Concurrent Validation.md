---
address: c-001155
type: concept
title: "Predictive vs Concurrent Validation"
aliases: ["predictive validity design", "concurrent validity design", "validation design"]
tags: [concept, psychometrics, selection, methods, validity]
status: developing
created: 2026-07-11
updated: 2026-07-11
related:
  - "[[Range Restriction Correction]]"
  - "[[Operational Validity (Selection)]]"
  - "[[Selection Bias]]"
  - "[[Sackett-et-al-2022-validity-overcorrection]]"
  - "[[Recruitment MOC]]"
---

# Predictive vs Concurrent Validation

Nav: [[index]] | [[concepts/_index]]

Two designs for establishing the [[Criterion-Related Validity of Personality|criterion-related validity]] of a selection procedure — distinguished by *when* the predictor is measured relative to hiring.

| | Predictive | Concurrent |
|---|---|---|
| Sample | Job **applicants** | Current **incumbents** |
| Timing | Predictor at hire, criterion later | Predictor & criterion measured together |
| Range restriction possible | **Direct** (if selected on x) or indirect | **Only indirect** (incumbents not hired on x) |
| Applicant-pool SD | Obtainable → can compute a U ratio | Unavailable by definition |

## Why the distinction is decisive (Sackett et al. 2022)

The [[Range Restriction Correction|U-ratio]] artifact distribution can only be built from **predictive** studies. But the **vast majority of validation research is concurrent** (typically 75–98% of studies in a given meta-analysis). Applying a predictive-derived U ratio to concurrent studies — where restriction is indirect and small — is the mechanism of **systematic overcorrection**. See [[Sackett-et-al-2022-validity-overcorrection]].

The practical upshot: report predictive and concurrent subsets separately; correct predictive studies for range restriction; leave concurrent studies uncorrected absent an empirical basis; then N-weight the two.
