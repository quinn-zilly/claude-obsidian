---
address: c-000756
type: source
title: "Karelaia & Hogarth (2008) — Determinants of Linear Judgment: A Meta-Analysis of Lens Model Studies"
authors: ["[[Natalia Karelaia]]", "[[Robin Hogarth]]"]
year: 2008
venue: "Psychological Bulletin, 134(3), 404–426"
doi: "10.1037/0033-2909.134.3.404"
tags:
  - source
  - jdm
  - judgment
  - lens-model
  - meta-analysis
  - bootstrapping
status: developing
created: 2026-06-30
updated: 2026-06-30
related:
  - "[[Lens Model]]"
  - "[[Lens Model Equation]]"
  - "[[Bootstrapping (Improper Linear Models)]]"
  - "[[Judgmental Achievement and Consistency]]"
  - "[[Cue Feedback Types]]"
  - "[[Policy Capturing]]"
  - "[[kuncel-et-al-2013-mechanical-vs-clinical]]"
  - "[[Judgment and Decision Making (Field)]]"
sources:
  - "[[karelaia-hogarth-2008-lens-model-meta-analysis]]"
---

# Karelaia & Hogarth (2008) — Determinants of Linear Judgment

> [!abstract] One-line
> A 5-decade meta-analysis of [[Lens Model]] studies (249 task environments, 86 articles, ~303,000 judgments) quantifying how accurate human linear judgment is, what task features move it, how feedback drives learning, and when [[Bootstrapping (Improper Linear Models)|bootstrapping]] beats the judge.

## What it is

The Brunswik [[Lens Model]], as formalized by the lens model equation ([[Lens Model Equation|Tucker 1964]]), gives a common statistical language for judgment-accuracy studies. The authors meta-analyzed the equation's components across 249 environments to make cumulative claims about linear judgment. Unit of analysis = the "average judge" per environment. Random-effects models; frequency weights (judges × judgments).

## Headline numbers (weighted means)

| Index | Symbol | Mean | 95% CI |
|---|---|---|---|
| Achievement | $r_a$ | .56 | .53–.59 |
| Matching (knowledge) | $G$ | .80 | .76–.83 |
| Environmental predictability | $R_e$ | .81 | .79–.84 |
| Response consistency | $R_s$ | .80 | .79–.82 |
| Residual correlation | $C$ | .04 | .02–.06 |
| Linear cognitive ability | $GR_s$ | .66 | .63–.69 |
| Bootstrapping validity | $GR_e$ | .65 | .61–.68 |

Linear models capture ~64% of variance in *both* environments and human judgments. Contrary to Camerer (1981), $R_s$ was **not** generally larger than $R_e$. Near-zero $C$ ⇒ little accurate nonlinear/configural cue use on average.

## Three major conclusions

1. **People achieve fairly high judgmental performance** and do so similarly in noisy and predictable environments (G uncorrelated with $R_e$).
2. **People learn best from task-information feedback** ([[Cue Feedback Types|feed-forward about true cue–criterion relations]]) — not outcome feedback. Outcome feedback alone can *degrade* consistency once some task familiarity exists, and only matters in few-cue tasks.
3. **Judgmental inconsistency is large enough that [[Bootstrapping (Improper Linear Models)|a linear model of the judge beats the judge]]** by ~.10 on average ($GR_e − r_a$). Eliminating inconsistency outweighs the loss of idiosyncratic (nonlinear) knowledge.

## What moves accuracy

- **More cues → lower $r_a$ and $G$** (worse matching). Achievement .63 (2 cues) → .52 (>3 cues).
- **Inter-cue redundancy → lower $G$ and $r_a$** (explains ~16.5% of $r_a$ heterogeneity); makes cues interchangeable.
- **Achieved (vs given) cues → slightly lower consistency**; identifying cue values is hard.
- **Nonlinear ecology → lower achievement**; configural use rarely helps (echoes Camerer & Johnson 1997).
- **Equal-weighting & redundancy-free environments are easiest** to match (equal weighting a good default; Dawes & Corrigan 1974).
- **Field studies are noisier than lab** (lower $R_e$) but report *higher* matching once task features are controlled — so lab results *underestimate* human linear knowledge.

## Expertise (a key null)

Initial expertise did **not** improve achievement or matching. Experts were somewhat more *consistent* ($R_s$), but the effect vanished once study-level features were controlled. Experts don't use more configural strategies, and "expert" here really means "experienced." Echoes Dawes, Faust & Meehl (1989): expertise can be weakly tied to performance.

## When bootstrapping wins

Bootstrapping advantage ($GR_e − r_a$) is larger when: less ecological noise (high $R_e$), low cue redundancy, differentially-weighted (noncompensatory) cues, and the judge is **less** experienced / less consistent / uses only modeled cues with no real nonlinear edge. In 30 of 236 studies bootstrapping was *inferior* to the judge — so conditions matter.

> [!key-insight]
> The lens model turns "is human judgment any good?" into separable, measurable parts: how predictable is the world ($R_e$), does the judge know the right weights ($G$), and does the judge apply them consistently ($R_s$). Most of the value of replacing judges with their own models comes from fixing the *consistency* leak, not the *knowledge* leak.

## Limitations the authors flag

Lens model methodology may mis-capture redundancy effects; "average judge" hides within-environment variation; expertise coding conflates experience with true domain expertise; tacit/intuitive expert processes may not be linearly representable.

## Connections

- Operationalizes and extends [[Lens Model]] and [[Policy Capturing]] with cumulative effect sizes.
- Directly cited by [[kuncel-et-al-2013-mechanical-vs-clinical|Kuncel et al. (2013)]] as the evidentiary base for "clinical judgment adds little ($C ≈ 0$)."
- Sits in the [[Judgment and Decision Making (Field)|JDM]] cluster alongside [[Calibration (Judgment)]], [[Illusion of Validity]].

## Source

- Karelaia, N., & Hogarth, R. M. (2008). *Psychological Bulletin, 134*(3), 404–426.
