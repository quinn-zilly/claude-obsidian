---
type: source
address: c-000022
title: "The Preregistration Revolution"
author: "Brian A. Nosek, Charles R. Ebersole, Alexander C. DeHaven, David T. Mellor"
year: 2018
venue: "Proceedings of the National Academy of Sciences"
volume: 115
issue: 11
pages: "2600–2606"
doi: "10.1073/pnas.1708274114"
tags:
  - open-science
  - preregistration
  - research-methods
  - replication-crisis
  - statistics
status: ingested
ingested: 2026-05-19
related:
  - "[[Brian Nosek]]"
  - "[[Preregistration]]"
  - "[[Open Science]]"
  - "[[Center for Open Science]]"
  - "[[Open Science Framework]]"
  - "[[Registered Reports]]"
  - "[[Publication Bias]]"
  - "[[open-science-collaboration-2015]]"
  - "[[munafo-2017-manifesto]]"
  - "[[foster-deardorff-2017-osf]]"
---

# Nosek et al. (2018) — The Preregistration Revolution

> [!key-insight] Core Claim
> Preregistration — committing to a research design and analysis plan before observing data — separates confirmatory from exploratory research, reduces flexibility-driven false positives, and makes null-hypothesis significance testing interpretable as a prediction test rather than a post-hoc description.

## Bibliographic Details

Brian A. Nosek, Charles R. Ebersole, Alexander C. DeHaven, and David T. Mellor. "The Preregistration Revolution." *Proceedings of the National Academy of Sciences* 115, no. 11 (2018): 2600–2606.

## Summary

### The Core Problem

NHST (null-hypothesis significance testing) is designed for prediction: given a pre-specified hypothesis, what is the probability of observing data at least this extreme if the null is true? But in practice, most psychology research uses NHST *after* looking at data — a practice called **HARKing** (Hypothesizing After Results are Known) or the **garden of forking paths** (Gelman & Loken). This converts a prediction test into a description test, which inflates false-positive rates dramatically.

Three cognitive biases drive the problem:
- **Hindsight bias** — past events feel inevitable once known; we can't reconstruct what we would have predicted before seeing data
- **Confirmation bias** — we pursue analyses consistent with expected findings
- **Garden of forking paths** — hundreds of defensible but undisclosed analytical decisions (exclusions, covariates, operationalizations) each slightly tune results toward significance

### What Preregistration Solves

Preregistration requires researchers to document — before collecting or analyzing data:
1. Research design (participants, measures, procedure)
2. Primary outcomes
3. Analysis plan (statistical tests, exclusion rules, covariates)

This makes the distinction between **confirmatory** and **exploratory** analysis unambiguous. Confirmatory tests are hypothesis-testing; exploratory analyses are hypothesis-generating. Both are scientifically valuable, but conflating them inflates the false discovery rate.

### 9 Practical Challenges Addressed

The paper addresses common objections and practical barriers, including:
1. Unanticipated outcomes requiring deviation from pre-registered plan
2. Exploratory analyses being forbidden (they are not — just clearly labeled)
3. Overhead and time cost (minimal with OSF infrastructure)
4. Preregistration as a credentialing system rather than a scientific tool

### Registered Reports

The strongest preregistration format: **Registered Reports** commit journals to publish results regardless of outcome (p < .05 or not), provided the pre-registered design was implemented. This directly attacks publication bias at the editorial decision point. As of 2018, over 100 journals had adopted Registered Reports (see [[munafo-2017-manifesto]] Box 3).

### OSF as Infrastructure

The [[Open Science Framework]] (osf.io) provides free, permanent, timestamped preregistration. Preregistrations are publicly archived and linked to eventual publications. The paper discusses the OSF Prereg Challenge — an incentive program awarding $1,000 to researchers who complete a Registered Report.

## Key Entities

- [[Brian Nosek]] — University of Virginia / Center for Open Science; founder of COS and principal architect of the open science reform movement
- [[Center for Open Science]] — non-profit; operates OSF; leads Registered Reports initiative
- [[Open Science Framework]] — platform/infrastructure

## Connections to Existing Wiki

- [[open-science-collaboration-2015]] — Nosek is the corresponding author on both papers; the 2015 OSC paper demonstrated the scale of the reproducibility problem that preregistration aims to prevent
- [[munafo-2017-manifesto]] — preregistration is the first major category of proposed reforms; the papers are complementary
- [[foster-deardorff-2017-osf]] — OSF is the infrastructure platform for preregistration
- [[LeBel et al. 2018|lebel-2018-credibility-framework]] — preregistration maps to the "transparency" and "analytic reproducibility" dimensions of LeBel's credibility framework

## Key Quote

> "Preregistration is not a promise that the predictions will be correct. It is a commitment to report the result regardless of what it is." (paraphrased)
