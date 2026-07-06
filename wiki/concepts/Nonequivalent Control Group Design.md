---
address: c-000888
type: concept
title: "Nonequivalent Control Group Design"
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
  - "[[Nonequivalent Dependent Variable]]"
  - "[[Selection Bias]]"
  - "[[Internal Validity]]"
  - "[[Threats to Validity]]"
sources:
  - "[[shadish-cook-campbell-2002-quasi-designs-control-and-pretests]]"
---

# Nonequivalent Control Group Design

Nav: [[index]] | [[log]]

The most common quasi-experiment: a treatment group and an untreated comparison group, **both measured at pretest and posttest** on the same outcome, with groups **not** formed by random assignment.

```
NR  O₁  X  O₂
NR  O₁     O₂
```

(`NR` = nonrandom assignment.)

## Why the pretest matters

Because the groups are nonequivalent by definition, **selection bias is presumed present**. The pretest is what makes the design work: it reveals the size and direction of initial group differences, flags which selection-based threats are plausible, and sharply increases statistical power. A control group *without* a matched pretest is, in SCC's view, of minimal value. Note: absence of pretest differences is **never** proof that selection bias is absent — unmeasured variables may still differ.

## Selection-based interaction threats

The design's characteristic threats are selection compounded with another threat:

- **selection–maturation** — groups mature at different rates (fan-spread growth).
- **selection–instrumentation** — unequal scale intervals, ceiling/floor effects at group extremes.
- **selection–regression** — differential regression to the mean from extreme-score matching.
- **selection–history (local history)** — an event affects one group more than the other.

## Plausibility depends on the outcome pattern

A threat is only worth worrying about if the observed data pattern is consistent with it. SCC's five prototypical outcomes range from ambiguous (both groups grow apart in the same direction — classic selection-maturation) to highly interpretable (a **crossover** interaction, which no simple scaling or regression artifact can generate).

## Strengthening moves

Double pretest · switching replications · reversed-treatment control · cohort controls · [[Nonequivalent Dependent Variable]] · direct measurement of the suspected threat. Statistical adjustment ([[Propensity Scores and Hidden Bias]], selection-bias models) comes *only after* design controls. See [[shadish-cook-campbell-2002-quasi-designs-control-and-pretests|SCC Ch. 5]].
