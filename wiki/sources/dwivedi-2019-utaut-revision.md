---
type: source
title: "Dwivedi et al. (2019) — Re-examining UTAUT: Towards a Revised Theoretical Model"
created: 2026-06-07
updated: 2026-06-07
address: c-000611
tags:
  - technology-acceptance
  - information-systems
  - meta-analysis
  - source
status: developing
source_type: paper
author: "Yogesh K. Dwivedi; Nripendra P. Rana; Anand Jeyaraj; Marc Clement; Michael D. Williams"
date_published: 2017-06-08
related:
  - "[[UTAUT]]"
  - "[[Revised UTAUT Model]]"
  - "[[Attitude as Mediator]]"
  - "[[MASEM]]"
  - "[[Yogesh Dwivedi]]"
  - "[[Viswanath Venkatesh]]"
---

# Dwivedi et al. (2019) — Re-examining UTAUT

> [!info] Citation
> Dwivedi, Y. K., Rana, N. P., Jeyaraj, A., Clement, M., & Williams, M. D. (2019). Re-examining the Unified Theory of Acceptance and Use of Technology (UTAUT): Towards a Revised Theoretical Model. *Information Systems Frontiers, 21*(3), 719–734. Open access (published online 8 June 2017).

## What it does

A critical review of [[UTAUT]] that formalizes an alternative model and tests it with **meta-analytic structural equation modelling** ([[MASEM]]). The core move: put the *individual* back into the model by adding [[Attitude as Mediator|attitude]] as a mediating construct, drop the four moderators, and add the missing facilitating-conditions → behavioural-intention path. See [[Revised UTAUT Model]].

## Method

- Meta-analysis of **1600 observations** across **21 relationships** among 7 constructs, coded from **162 prior studies** (96 journal articles, 49 conference papers, 16 dissertations, 1 book chapter).
- Effect sizes corrected for measurement error (construct reliabilities) and sampling error, then pooled into a correlation matrix.
- Path analysis on the pooled matrix in AMOS 21 using the **minimum sample size** (N = 4319); harmonic and average sample sizes used for validation.
- Paths dropped when critical ratio < 1.96; emergent paths added when modification index ≥ 10 *and* theoretically justified.

## Three models compared

| Metric | Basic UTAUT | Proposed (w/ attitude) | Emergent (final) |
|---|---|---|---|
| R² behavioural intention | 0.38 | 0.45 | 0.45 |
| R² usage behaviour | 0.21 | 0.22 | 0.27 |
| R² attitude | — | 0.52 | 0.55 |
| RMSEA | 0.111 | 0.146 | **0.041** |
| CFI | 0.974 | 0.955 | 0.998 |

The emergent model added three data-driven paths beyond the hypothesized set: **AT → UB** (MI = 138.47), **FC → AT** (MI = 122.63), and **SI → AT** (MI = 59.17). Final fit was excellent (RMSEA < 0.05).

## Key findings

Attitude is central to acceptance and use: it (a) is influenced by facilitating conditions and social influence as well as by performance and effort expectancy, (b) directly drives behavioural intention while partially mediating the four exogenous constructs, and (c) directly drives usage behaviour — beyond the indirect route through intention. The four exogenous constructs had **stronger direct effects on attitude than on behavioural intention** (e.g., PE → BI = 0.11 vs PE → AT = 0.47), suggesting attitude is where these perceptions actually land.

## Implications

For theory: attitude should be reinstated as an integral UTAUT construct; data-driven direct effects (esp. FC → BI) currently missing from UTAUT deserve theorizing; moderators are context-dependent, not universal. For practice: because attitude drives both intention and use, managers should shape attitudes directly via clean design, accurate communication of capabilities, training, help desks, and managed social influence (champions, forums, counter-messaging).

## Limitations

Only studies reporting Pearson-convertible statistics were included (regression/SEM-only studies excluded). Missing reliabilities/SDs were imputed with averages. The four UTAUT moderators were not modelled because primary studies rarely reported them — so the original model was not tested in full.

> [!key-insight]
> The headline is parsimony-vs-explanation. Venkatesh dropped attitude from UTAUT for parsimony; Dwivedi et al. show that reinstating it buys a meaningful jump in explained variance and a much better-fitting model. Attitude is the construct where technology attributes and contextual factors converge before becoming intention and behaviour.
