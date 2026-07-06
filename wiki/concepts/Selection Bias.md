---
address: c-000893
type: concept
title: "Selection Bias"
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
  - "[[Nonequivalent Control Group Design]]"
  - "[[Propensity Scores and Hidden Bias]]"
  - "[[Matching (Quasi-Experiments)]]"
  - "[[Internal Validity]]"
sources:
  - "[[shadish-cook-campbell-2002-quasi-designs-control-and-pretests]]"
  - "[[shadish-cook-campbell-2002-quasi-designs-no-control-or-no-pretest]]"
---

# Selection Bias

Nav: [[index]] | [[log]]

Systematic pre-existing differences between the groups being compared, arising because units were **not** randomly assigned to conditions. It is the defining threat of the [[Nonequivalent Control Group Design]] and, more broadly, the central obstacle to causal inference in any [[Quasi-Experimental Design]]. Listed among the nine threats to [[Internal Validity]].

## Why it is hard

Selection interacts with other threats — **selection-maturation, selection-history, selection-regression, selection-instrumentation** — so the same nonequivalence can masquerade as several different alternative explanations. Absence of *observed* pretest differences never proves selection bias is absent, because unmeasured variables may still differ.

## Two lines of remedy

- **By design** (preferred): pretests to gauge its size/direction, [[Matching (Quasi-Experiments)|matching]] on stable correlates, internal rather than external controls, multiple control groups to bracket the bias, cohort controls, cutoff-based assignment (regression discontinuity).
- **By statistics** (after design): [[Propensity Scores and Hidden Bias|propensity scores]] adjust for *observed* selection; **selection-bias models** (Heckman) attempt to reach *unobserved* selection via a selection equation, but are assumption-sensitive and often fail to match randomized benchmarks (LaLonde 1986). Neither removes **hidden bias** from unmeasured confounders.

SCC's stance: reach for design controls first; use statistics only for the residual.
