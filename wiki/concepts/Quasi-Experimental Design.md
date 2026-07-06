---
address: c-000887
type: concept
title: "Quasi-Experimental Design"
tags:
  - concept
  - research-methods
  - causal-inference
  - quasi-experiments
status: seed
created: 2026-07-06
updated: 2026-07-06
related:
  - "[[Nonequivalent Control Group Design]]"
  - "[[Nonequivalent Dependent Variable]]"
  - "[[Coherent Pattern Matching]]"
  - "[[Case-Control Design]]"
  - "[[Internal Validity]]"
  - "[[Threats to Validity]]"
sources:
  - "[[shadish-cook-campbell-2002-quasi-designs-no-control-or-no-pretest]]"
  - "[[shadish-cook-campbell-2002-quasi-designs-control-and-pretests]]"
---

# Quasi-Experimental Design

Nav: [[index]] | [[log]]

An experiment that **manipulates a treatment** but **lacks random assignment** of units to conditions, while otherwise sharing the structure and purpose of a randomized experiment. Because randomization is absent, alternative explanations for a treatment–outcome relationship are *not* automatically distributed across conditions, so causal inference depends on actively ruling them out.

## The three principles (SCC)

Without randomization, [[William R. Shadish|SCC]] reduce the plausibility of alternative causes through:

1. **Identifying and studying plausible threats to [[Internal Validity]]** — treat each threat as a hypothesis and probe whether it could explain the observed covariation.
2. **Primacy of control by design** — prevent confounds with added design elements before reaching for statistical adjustment.
3. **[[Coherent Pattern Matching]]** — predict a complex outcome pattern that few alternatives can mimic.

## Quasi-experiments are combinations of design elements

There is usually **no single best quasi-experimental design**. Each study assembles elements to fit its hypotheses, feasible controls, and the contextually salient threats. SCC's four families of elements:

| Family | Elements |
|--------|----------|
| **Assignment** | random, cutoff-based (see regression discontinuity), other nonrandom, [[Matching (Quasi-Experiments)|matching/stratifying]], masking |
| **Measurement** | pre/posttests, retrospective + proxy pretests, [[Nonequivalent Dependent Variable]], moderator interactions, direct threat measurement |
| **Comparison groups** | single/multiple nonequivalent, cohorts, internal vs. external controls, constructed contrasts |
| **Treatment** | switching replications, reversed, removed, repeated (ABAB) |

## Design spectrum (weak → strong)

- No control + no pretest: one-group posttest-only → + multiple posttests → pretest-posttest → + double pretest / [[Nonequivalent Dependent Variable|NEDV]] / removed / repeated treatment. See [[shadish-cook-campbell-2002-quasi-designs-no-control-or-no-pretest|Ch. 4]].
- Control **and** pretest: the [[Nonequivalent Control Group Design]] and its extensions. See [[shadish-cook-campbell-2002-quasi-designs-control-and-pretests|Ch. 5]].

## Guiding maxims

Fisher: *"make your theories elaborate."* Holland: causal inference in nonrandomized studies needs **more data** and **more assumptions** than randomized studies — put the weight on gathering more data (design) over making more assumptions (statistics).
