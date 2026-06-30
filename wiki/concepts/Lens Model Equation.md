---
address: c-000765
type: concept
title: "Lens Model Equation"
aliases: ["LME", "Tucker lens model equation"]
tags: [concept, jdm, judgment, lens-model, methodology]
status: developing
created: 2026-06-30
updated: 2026-06-30
related: ["[[Lens Model]]", "[[Policy Capturing]]", "[[Judgmental Achievement and Consistency]]", "[[Bootstrapping (Improper Linear Models)]]", "[[karelaia-hogarth-2008-lens-model-meta-analysis]]"]
---

# Lens Model Equation

The algebraic decomposition of judgmental accuracy in the [[Lens Model]], due to Tucker (1964). It splits **achievement** — the correlation $r_a$ between the criterion $Y_e$ and the judgment $Y_s$ — into interpretable components:

$$
r_a = G \cdot R_e \cdot R_s + C\sqrt{1-R_e^2}\sqrt{1-R_s^2}
$$

| Term | Name | Meaning |
|---|---|---|
| $r_a$ | Achievement | How well judgment tracks the criterion |
| $G$ | Matching / knowledge | Correlation between the *linear models* of environment and judge — does the judge weight cues like the world does? |
| $R_e$ | Environmental predictability | How linearly predictable the criterion is from cues |
| $R_s$ | Response consistency | How consistently the judge applies their own policy |
| $C$ | Residual correlation | Correlation of the two models' residuals — nonlinear/configural or omitted-cue accuracy |

When residuals are independent ($C = 0$), achievement is simply the product $G \cdot R_e \cdot R_s$ — cleanly separating **task** factors ($R_e$) from **cognitive** factors ($G$, $R_s$).

## Composite indices

- **Linear cognitive ability** $GR_s$ — the human contribution to achievement, independent of how predictable the environment is.
- **Bootstrapping validity** $GR_e$ — validity of replacing the judge with their own linear model (i.e. $R_s$ set to 1). See [[Bootstrapping (Improper Linear Models)]].

## Why it matters

The LME is what makes the lens model *meta-analyzable*: every component is a correlation, so results aggregate across studies (the basis of [[karelaia-hogarth-2008-lens-model-meta-analysis|Karelaia & Hogarth 2008]], who found mean $G=.80$, $R_e=.81$, $R_s=.80$, $C=.04$). Caution: large $G$ does **not** require the judge's weights to match the ecology's — high inter-cue correlation can produce high $G$ with quite different weights (Castellan 1992; Dawes & Corrigan 1974).

## Source

- Tucker (1964); decomposition used throughout [[karelaia-hogarth-2008-lens-model-meta-analysis]].
