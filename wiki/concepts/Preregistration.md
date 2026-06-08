---

type: concept
address: c-000043
title: "Preregistration"
tags:
  - open-science
  - research-methods
  - statistics
  - reproducibility
status: mature
related:
  - "[[Brian Nosek]]"
  - "[[Registered Reports]]"
  - "[[Open Science Framework]]"
  - "[[Center for Open Science]]"
  - "[[Publication Bias]]"
  - "[[P-hacking]]"
  - "[[HARKing]]"
  - "[[Researcher Degrees of Freedom]]"
  - "[[simmons-et-al-2011-false-positive-psychology]]"
  - "[[Open Science]]"
  - "[[nosek-2018-preregistration]]"
  - "[[munafo-2017-manifesto]]"
  - "[[Open Science MOC]]"
created: unknown
updated: unknown
---

# Preregistration

Preregistration is the practice of publicly committing to a research design, primary outcomes, and analysis plan *before* collecting or observing data, in a timestamped and immutable record.

## Core Purpose

Preregistration makes a fundamental distinction:
- **Confirmatory research** (hypothesis testing): uses NHST legitimately; preregistration required for valid inference
- **Exploratory research** (hypothesis generation): can examine unexpected patterns; must be clearly labeled as exploratory

Without preregistration, the distinction between confirmatory and exploratory is lost in the published record. NHST p-values are only valid as prediction tests; when applied to post-hoc hypotheses they inflate false-positive rates dramatically (see [[HARKing]], [[P-hacking]]).

## What Is Registered

A complete preregistration documents:
1. **Research question and hypotheses** (specific, directional where possible)
2. **Design**: participants, materials, procedures, conditions
3. **Primary outcomes**: which variables, how measured, what constitutes the key test
4. **Analysis plan**: statistical tests, exclusion rules, covariates, planned comparisons
5. **Sample size rationale**: power analysis or stopping rule

## Platforms

| Platform | Primary Use |
|----------|-------------|
| [[Open Science Framework]] (osf.io) | General social/behavioral sciences; most widely used |
| AsPredicted.org | Lightweight preregistration for quick studies |
| ClinicalTrials.gov | Clinical trials (required by many journals and FDA) |
| PROSPERO | Systematic reviews and meta-analyses |

## Registered Reports

The strongest preregistration format: journals review and commit to publishing *before* results are known (see [[Registered Reports]]). As of 2018, >100 journals adopted this format.

## Common Objections Addressed

| Objection | Response |
|-----------|----------|
| "It prevents exploration" | Exploratory analyses remain allowed; just labeled as such |
| "Too much overhead" | OSF preregistration takes ~30 minutes for a standard study |
| "What if we need to deviate?" | Deviations are acceptable if reported transparently |
| "I can't pre-specify everything" | Partial preregistration of primary outcomes is better than none |

## Empirical Evidence for Effectiveness

- Registered Reports show smaller effect sizes and more null results than conventional publications — consistent with pre-registration eliminating publication bias
- Nosek et al. (2018): preregistered replications in [[open-science-collaboration-2015]] had no selection or reporting bias; enabled unbiased estimates of replication rates
- [[munafo-2017-manifesto]]: preregistration was listed as the single most effective reform across methods and reporting categories

## Relationship to Knowledge Management

Preregistration is, at its core, a **knowledge management intervention**: it creates an immutable record of prior beliefs that prevents post-hoc revision of history, a form of institutional memory that constrains subsequent analysis and interpretation. This connects to [[Source-First Synthesis]] in the wiki pattern — the principle that sources should remain immutable while analysis is layered on top.

## See Also

- [[Registered Reports]]
- [[Publication Bias]]
- [[P-hacking]]
- [[HARKing]]
- [[nosek-2018-preregistration]]
