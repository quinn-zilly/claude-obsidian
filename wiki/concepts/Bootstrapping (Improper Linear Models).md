---
address: c-000766
type: concept
title: "Bootstrapping (Improper Linear Models)"
aliases: ["bootstrapping judges", "model of man", "paramorphic model"]
tags: [concept, jdm, judgment, prediction, linear-models]
status: developing
created: 2026-06-30
updated: 2026-06-30
related: ["[[Lens Model]]", "[[Lens Model Equation]]", "[[Mechanical vs Clinical Prediction]]", "[[Judgmental Achievement and Consistency]]", "[[Policy Capturing]]", "[[karelaia-hogarth-2008-lens-model-meta-analysis]]", "[[kuncel-et-al-2013-mechanical-vs-clinical]]"]
---

# Bootstrapping (Improper Linear Models)

> [!note] Not the statistical resampling "bootstrap"
> In JDM, **bootstrapping** means replacing a human judge with a *linear model of that judge's own past judgments* (the "model of man"), then using the model to make future predictions.

## The paradox

The model of the judge routinely **outperforms the judge it was built from** (Goldberg 1970; Dawes 1971). Why? Because the model captures the judge's valid linear *policy* ($G$) but strips out their **inconsistency** ($R_s < 1$) — the random noise in applying that policy from case to case. In [[Lens Model Equation|lens-model]] terms, bootstrapping validity is $GR_e$ (the judge applied with perfect consistency, $R_s = 1$), which generally exceeds achievement $r_a = GR_eR_s$.

## When it wins (Karelaia & Hogarth 2008)

Mean advantage $GR_e − r_a \approx .10$. Larger when:

- low ecological noise (high $R_e$),
- low cue redundancy,
- differentially (noncompensatory) weighted cues,
- the judge is **less** experienced, **less** consistent, uses only modeled cues, and has **no** real nonlinear edge ($C \approx 0$).

In 30 of 236 studies bootstrapping was *inferior* — so it's conditional, not automatic. Experts with genuine tacit/configural knowledge are the boundary case.

## Why it works conceptually

Eliminating inconsistency outweighs the loss of idiosyncratic knowledge, because that idiosyncratic knowledge (the residual $C$) is on average near zero. Equal-weighting "improper" models are themselves a robust default (Dawes & Corrigan 1974) — precise weights matter less than consistent application.

## Applied payoff

This is the mechanism behind [[Mechanical vs Clinical Prediction|mechanical > clinical prediction]]: [[kuncel-et-al-2013-mechanical-vs-clinical|Kuncel et al. (2013)]] show that formula-combining the *same* cues beats holistic expert combination by >50% for job performance. The practical prescription: let experts identify/weight cues, then **combine mechanically**.

## Source

- [[karelaia-hogarth-2008-lens-model-meta-analysis]] (§Bootstrapping); [[kuncel-et-al-2013-mechanical-vs-clinical]]; Goldberg (1970); Dawes (1971); Camerer (1981).
