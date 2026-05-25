---

type: source
address: c-000026
title: "Estimating the Reproducibility of Psychological Science"
author:
  - "[[Open Science Collaboration]]"
year: 2015
venue: "Science"
volume: 349
issue: 6251
pages: "aac4716"
doi: "10.1126/science.aac4716"
tags:
  - open-science
  - replication-crisis
  - reproducibility
  - psychology
  - meta-science
status: ingested
ingested: 2026-05-19
related:
  - "[[Open Science Collaboration]]"
  - "[[Brian Nosek]]"
  - "[[Replication Crisis]]"
  - "[[Open Science]]"
  - "[[Preregistration]]"
  - "[[Center for Open Science]]"
  - "[[Open Science Framework]]"
  - "[[munafo-2017-manifesto]]"
  - "[[nosek-2018-preregistration]]"
  - "[[lebel-2018-credibility-framework]]"
created: unknown
updated: unknown
---

# Open Science Collaboration (2015) — Estimating the Reproducibility of Psychological Science

> [!key-insight] Core Claim
> Only 36% of 100 attempted replications of published psychology studies produced statistically significant results in the same direction; replication effects were half the magnitude of originals. Replication success was predicted by strength of original evidence, not team expertise.

## Bibliographic Details

Open Science Collaboration. "Estimating the Reproducibility of Psychological Science." *Science* 349, no. 6251 (2015): aac4716.

Corresponding author: Brian A. Nosek (nosek@virginia.edu). 270 contributing authors. Funded by the Center for Open Science and the Laura and John Arnold Foundation. Data and materials: https://osf.io/ezcuj

## Summary

### Design

The OSC conducted replications of 100 experimental and correlational studies published in three 2008 issues of major psychology journals:
- *Psychological Science* (PSCI, n=40 replications)
- *Journal of Personality and Social Psychology* (JPSP, n=32)
- *Journal of Experimental Psychology: Learning, Memory, and Cognition* (JEP:LMC, n=28)

Teams used original materials, consulted original authors on design fidelity, pre-registered their analysis plans, and archived all materials on OSF. Analyses were independently audited and reproduced in R.

### Five Reproducibility Indicators

| Indicator | Overall Result |
|-----------|---------------|
| Replication p < .05 in same direction | 36% (35/97) |
| Replication effect size in original 95% CI | 47% (45/95) |
| Meta-analytic estimate p < .05 | 68% (51/75) |
| Original effect size in replication 95% CI | 41% |
| Subjective "Did it replicate?" (team rating) | 39% |

### Effect Size Decline

Original studies: M effect size r = 0.403 (SD = 0.188)
Replications: M effect size r = 0.197 (SD = 0.257)

82 of 99 study pairs showed a stronger effect in the original. Effect sizes were positively correlated across original/replication (Spearman's r = 0.51) — but original effects were substantially inflated.

### Predictors of Replication Success

Replication success was predicted by **strength of original evidence** (lower p, larger effect size), not by characteristics of the replication teams (expertise, self-assessed quality). Cognitive psychology replicated better than social psychology (50% vs 25% significant).

### Interpretation

The authors resist two easy conclusions:
1. "Failure to replicate means the original was a false positive" — replication can fail for many legitimate reasons
2. "Success means the theory is correct" — a replication only establishes reliability, not validity

The most plausible explanation for the systematic effect-size decline: **publication bias** inflates original effect sizes; replication studies, with confirmed methodology and pre-registered analyses, are unbiased. Low-powered original studies are particularly affected.

### Implications

This paper is the empirical anchor of the replication crisis narrative in psychology. It motivated:
- Widespread adoption of preregistration ([[nosek-2018-preregistration]])
- The Manifesto for Reproducible Science ([[munafo-2017-manifesto]])
- LeBel's multi-dimensional credibility framework ([[lebel-2018-credibility-framework]])

### Methods Innovation

The project demonstrated that large-scale, transparent, collaborative replication is feasible. All 270+ collaborators, materials, and results are publicly archived — itself a demonstration of open science norms.

## Key Entities

- [[Open Science Collaboration]] — collective author; 270 contributors
- [[Brian Nosek]] — coordinating corresponding author; UVA / COS
- [[Center for Open Science]] — organizational support and funding
- [[Open Science Framework]] — platform for preregistration and archival (https://osf.io/ezcuj)

## Connections to Existing Wiki

- [[Replication Crisis]] — this is the paper that definitively established the scale of the crisis
- [[Preregistration]] — the replication protocols were pre-registered; the paper is a key argument for preregistration
- [[lebel-2018-credibility-framework]] — LeBel's framework names "effect replicability" as one of four credibility dimensions; OSC 2015 assessed this dimension for 100 studies
- [[munafo-2017-manifesto]] — cites OSC 2015 as motivating evidence; the manifesto proposes systemic reforms in response
- [[bosco-2020-metabus]] — metaBUS enables rapid checking of which effects have strong replication track records vs. fragile originals

## Key Quote

> "After this intensive effort to reproduce a sample of published psychological findings, how many of the effects have we established are true? Zero. And how many of the effects have we esta