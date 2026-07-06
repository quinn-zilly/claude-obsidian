---
address: c-000894
type: concept
title: "Matching (Quasi-Experiments)"
tags:
  - concept
  - research-methods
  - causal-inference
  - quasi-experiments
status: seed
created: 2026-07-06
updated: 2026-07-06
related:
  - "[[Quasi-Experimental Design]]"
  - "[[Selection Bias]]"
  - "[[Propensity Scores and Hidden Bias]]"
  - "[[Nonequivalent Control Group Design]]"
sources:
  - "[[shadish-cook-campbell-2002-quasi-designs-no-control-or-no-pretest]]"
---

# Matching (Quasi-Experiments)

Nav: [[index]] | [[log]]

Forming treatment and comparison groups so they hold similar values on likely correlates of the outcome, to reduce [[Selection Bias]] when random assignment is unavailable. **Matching** pairs units with the same score on the matching variable; **stratifying** places units into homogeneous blocks larger than the number of conditions (≈5 strata remove ~90% of the covariate's bias, Cochran 1968).

## Varieties

Exact · caliper (within a defined distance) · nearest-neighbor / Mahalanobis-distance · index, cluster, benchmark (multiple controls per treated unit) · optimal matching · **propensity-score matching** (match on a single composite; see [[Propensity Scores and Hidden Bias]]). Twin studies are a special powerful case (shared genetics + environment).

## The core danger

> [!warning] Matching can make inference *worse*
> Campbell & Erlebacher (1970): when matched groups are drawn from **non-overlapping populations** on an **unreliable** variable, matches come from opposite tails, and **regression to the mean** creates a spurious effect. Their Head Start example made a beneficial program look *harmful*; the gifted-and-talented analogue makes an ineffective program look effective.

## Principles for better matching

1. Select groups that are **already similar** (overlapping distributions) *before* matching — e.g. late-applying eligibles rather than the never-eligible.
2. Match on **stable, reliably measured** variables (gender, age; or aggregates and multi-occasion averages that cancel random error).
3. Use **bracketing** — a comparison unit just above and just below each treated unit (Millsap et al. 1997) — which also raises power cheaply.

Matching can only balance **observed** variables, so hidden bias may remain; pair it with sensitivity analysis. Simple matching on a single unreliable variable "should be left completely behind."
