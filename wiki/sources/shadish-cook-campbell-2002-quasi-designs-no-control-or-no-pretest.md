---
address: c-000885
type: source
title: "Shadish, Cook & Campbell (2002) — Quasi-Experimental Designs That Either Lack a Control Group or Lack Pretest Observations"
authors: ["William R. Shadish", "Thomas D. Cook", "Donald T. Campbell"]
year: 2002
venue: "Experimental and Quasi-Experimental Designs for Generalized Causal Inference, Ch. 4"
tags:
  - source
  - research-methods
  - causal-inference
  - quasi-experiments
  - study-design
status: seed
created: 2026-07-06
updated: 2026-07-06
related:
  - "[[Quasi-Experimental Design]]"
  - "[[Nonequivalent Dependent Variable]]"
  - "[[Coherent Pattern Matching]]"
  - "[[Case-Control Design]]"
  - "[[Matching (Quasi-Experiments)]]"
  - "[[Internal Validity]]"
  - "[[Threats to Validity]]"
  - "[[shadish-cook-campbell-2002-quasi-designs-control-and-pretests]]"
  - "[[shadish-cook-campbell-2002-statistical-conclusion-internal-validity]]"
---

# Shadish, Cook & Campbell (2002) — Quasi-Designs That Lack a Control Group or Lack Pretests

Nav: [[index]] | [[log]] | [[Open Science MOC]]

Chapter 4 of *Experimental and Quasi-Experimental Designs for Generalized Causal Inference* ("SCC"). Catalogues the **weakest** quasi-experimental designs — those missing either a pretest or a control group — and shows how thoughtfully added design elements strengthen each. Opens with the 1966 Ontario PKU screening program: no control group, no randomization, yet a clear and durable causal conclusion, because much specific background knowledge made alternative causes implausible. The lesson of the chapter: weak designs are occasionally sufficient and often the only feasible option, but researchers should know the internal-validity costs they incur.

## The logic of quasi-experimentation in brief

A [[Quasi-Experimental Design]] lacks random assignment but shares the structure and purpose of a randomized experiment. To make alternative explanations implausible without randomization, SCC lean on three related principles:

1. **Identify and study plausible threats to internal validity** — probe each threat to see how likely it is to explain the treatment–outcome covariation.
2. **Primacy of control by design** — add design elements (extra pretests, extra control groups) to *prevent* confounds rather than statistically adjust them away afterward. Use statistics only for whatever residual difference design controls leave.
3. **[[Coherent Pattern Matching]]** — predict a complex pattern of results that few alternative explanations could produce.

## Designs without control groups

Progression from weakest to stronger (each adds one element):

- **One-group posttest-only** (`X O`) — nearly all internal-validity threats apply; useful only when background knowledge makes alternatives implausible (e.g. a calculus post-test after a calculus course).
- **One-group posttest-only with multiple substantive posttests** — enables the detective/pathologist [[Coherent Pattern Matching|pattern-matching]] logic, but only when the cause's signature is known and uniquely predicted (retrospective cause-search vs. prospective effect-search; prospective use risks Type I errors because humans over-find patterns).
- **One-group pretest-posttest** (`O₁ X O₂`) — weak counterfactual; maturation and history are live. Duckart's (1998) lead-abatement study is the model of *plausibility* reasoning: a threat must both be shown likely to have occurred **and** to produce an effect of the same size and direction as observed.
- **Double pretest** (`O₁ O₂ X O₃`) — the first interval is a "dry run" for maturation/regression bias.
- **[[Nonequivalent Dependent Variable]]** — add a second measure expected *not* to respond to treatment but to respond to the same threats; divergence supports the causal inference.
- **Removed-treatment design** (`O₁ X O₂ O₃ ~X O₄`) — outcome should rise and fall with treatment; interpretable only if effects dissipate on removal; removal may be unethical or breed resentful demoralization.
- **Repeated-treatment design** (`O₁ X O₂ ~X O₃ X O₄`) — introduce, remove, reintroduce (the ABAB logic); strong for internal validity when the investigator controls timing; watch cyclical maturation and construct-validity reactivity. Best with transient effects and unobtrusive treatments.

## Designs with a control group but no pretest

- **Posttest-only with nonequivalent groups** (`NR X O` / `NR O`) — selection and treatment effects are nearly inseparable without pretest data.
- **Independent pretest sample** — pretest drawn from an independent random sample of the same population (cross-sectional panels); common in epidemiology/polling; vulnerable to population composition change over waves.
- **Proxy pretests** — a pre-treatment variable correlated with the outcome stands in for a true pretest (weaker; e.g. algebra score as proxy for calculus baseline).
- **[[Matching (Quasi-Experiments)|Matching or stratifying]]** — form comparable groups on correlates of the outcome. Matching can *harm* inference (Campbell & Erlebacher 1970 Head Start example) when done on unreliable variables and non-overlapping populations → regression artifacts. Better: pick already-similar groups, match on stable/reliable/aggregated variables, use bracketing (a match above and below each treated unit).
- **Internal vs. external controls** — internal controls (same pool, e.g. late registrants) typically carry fewer selection biases than external controls.
- **Multiple control groups** — systematic-variation and bracketing controls index hidden bias and can bracket the effect (Zabin et al. abortion study).
- **Predicted interaction** — a differentiated theoretical prediction (Seaver's sibling/teacher-expectancy study) rules out threats incapable of generating the pattern — though it can still hide regression artifacts.

## Constructed contrasts (weak, last resort)

When no independent control group is available, mimic one with (1) **regression extrapolation** (observed vs. projected posttest), (2) **normed comparison** (vs. test-manual norms — a very weak counterfactual, threatened by selection/history/regression), or (3) **secondary-source contrasts** (clinical series, national datasets). Use only as adjuncts within a larger design.

## The case-control design

The [[Case-Control Design]] (case-referent / retrospective) is imported from epidemiology: sample on the *outcome* (cases vs. controls) and look backward for exposure. Excellent for **generating** causal hypotheses when outcomes are rare or slow (smoking–cancer, DES–vaginal cancer) but riddled with biases — Sackett's (1979) catalogue of ~35 biases is reproduced in the chapter (Table 4.3).

## Vault links

Direct successor chapter: [[shadish-cook-campbell-2002-quasi-designs-control-and-pretests|Ch. 5]] (designs that use *both* control groups and pretests). Threat vocabulary from [[shadish-cook-campbell-2002-statistical-conclusion-internal-validity|Ch. 2]] ([[Internal Validity]], [[Threats to Validity]]).

## Source

- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference* (Ch. 4). Houghton Mifflin.
