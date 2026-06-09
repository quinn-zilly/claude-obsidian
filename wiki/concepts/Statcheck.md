---
address: c-000670
type: concept
title: "Statcheck"
tags:
  - open-science
  - research-methods
  - reproducibility
  - tools
status: developing
related:
  - "[[Questionable Research Practices]]"
  - "[[Replicability]]"
  - "[[Michèle Nuijten]]"
  - "[[soderberg-et-al-2021-registered-reports-quality]]"
  - "[[Open Science MOC]]"
created: 2026-06-09
updated: 2026-06-09
---

# Statcheck

Statcheck is an R package (Epskamp & Nuijten) that extracts null-hypothesis-significance-test statistics reported in APA style (t, F, χ², r, Z, Q) from a paper and **recomputes the p-value** from the reported test statistic and degrees of freedom, flagging inconsistencies automatically.

## Error Types

| Type | Meaning |
|---|---|
| **Reporting error** | Reported p-value inconsistent with the recomputed value |
| **Decision error** | A result reported as significant (p<.05) that recomputes as non-significant, or vice versa — the consequential kind |

## Use in Meta-Research

A fast, scalable way to audit the statistical reporting integrity of a literature without manual recalculation. Validated by Nuijten et al. ([[Michèle Nuijten]]).

In [[soderberg-et-al-2021-registered-reports-quality|Soderberg et al. (2021)]], statcheck was run on Registered Reports vs comparison papers; reporting/decision errors were rare and similar across groups — a complementary *objective* quality measure alongside the subjective peer-review ratings.

## See Also

- [[Questionable Research Practices]]
- [[Replicability]]
- [[Open Science MOC]]
