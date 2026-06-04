---

type: concept
address: c-000053
title: "Analytic Reproducibility"
tags:
  - open-science
  - research-methods
  - reproducibility
  - meta-science
status: developing
related:
  - "[[Replication Crisis]]"
  - "[[Open Science]]"
  - "[[P-hacking]]"
  - "[[Preregistration]]"
  - "[[metaBUS]]"
  - "[[Etienne LeBel]]"
  - "[[lebel-2018-credibility-framework]]"
  - "[[nosek-2022-replicability-robustness-reproducibility]]"
  - "[[Robustness (Science)]]"
created: unknown
updated: unknown
---

# Analytic Reproducibility

Analytic reproducibility is the ability to reproduce the reported numerical results of a published study using the same data and the same analysis procedure. It is one of the four dimensions in [[lebel-2018-credibility-framework|LeBel et al.'s credibility framework]].

## Definition

A finding is analytically reproducible if: given the publicly available data and the reported analysis method, an independent analyst reaches the same results *within a specified tolerance* (LeBel et al. define **10% margin** as the operationalization).

This is distinct from:
- **Replication** (new data, independent study) — a stronger test
- **Analytic robustness** (alternative defensible analyses of same data) — a broader test
- **Transparency** (data and code availability) — a prerequisite for analytic reproducibility

## Two Failure Modes (Nosek et al. 2022)

- **Process reproducibility failure**: original analysis can't be repeated — data, code, or software unavailable
- **Outcome reproducibility failure**: reanalysis gets different number — error in original or reproduction

Process failure = can't verify. Outcome failure = suggests original may be wrong. Either undermines credibility and reduces case for investing in replication. Artner et al. (2020): only 70% of 232 findings successfully reproduced.

## Why It Matters

Analytic reproducibility should be trivially achievable — same data, same code, same result. Yet audits consistently find failures:
- Erroneous calculations
- Incorrect application of statistical procedures
- Data management errors
- Rounding and transcription errors
- Software version differences

These are not fraud but mundane mistakes. Their prevalence in the literature suggests that analytic reproducibility is not currently the norm.

## Empirical Evidence of Failure

- Nuijten et al. (2016): 49.6% of psychology articles contained at least one inconsistency between reported test statistic and p-value (using STATCHECK)
- Hardwicke et al. (2018): only 50% of 35 psychology papers with open data could be reproduced within 10%

## Relationship to P-hacking

Analytic reproducibility is a detective tool: if you can reproduce every analysis in a paper from the data, you can also check whether the reported analysis was the only one run — or whether alternative specifications were tried and suppressed (evidence of [[P-hacking]]). This is the logic behind multiverse analysis: run all defensible paths and compare.

## Infrastructure for Analytic Reproducibility

- **Open data**: public deposition of raw data files (prerequisite)
- **Open code**: analysis scripts in R, Python, SPSS, etc.
- **[[metaBUS]]**: for effect sizes in coded databases, independent re-estimation is possible
- **Containerization**: Docker/Binder for computational reproducibility across software environments

## Relationship to LeBel's Framework

In the [[lebel-2018-credibility-framework|four-dimension credibility framework]]:
1. Transparency (prerequisite)
2. **Analytic reproducibility** ← this concept
3. Analytic robustness (multiverse)
4. Effect replicability (new data)

Analytic reproducibility is necessary but not sufficient for high credibility: a paper can be analytically reproducible but analytically fragile (results change under alternative defensible analyses) or unreplicable (the effect doesn't appear in new data).

## See Also

- [[lebel-2018-credibility-framework]]
- [[P-hacking]]
- [[Open Science]]
- [[Preregistration]]
