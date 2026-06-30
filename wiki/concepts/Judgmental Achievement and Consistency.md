---
address: c-000771
type: concept
title: "Judgmental Achievement and Consistency"
aliases: ["cognitive control", "response consistency", "judgmental achievement"]
tags: [concept, jdm, judgment, lens-model]
status: developing
created: 2026-06-30
updated: 2026-06-30
related: ["[[Lens Model]]", "[[Lens Model Equation]]", "[[Bootstrapping (Improper Linear Models)]]", "[[Mechanical vs Clinical Prediction]]", "[[karelaia-hogarth-2008-lens-model-meta-analysis]]", "[[kuncel-et-al-2013-mechanical-vs-clinical]]"]
---

# Judgmental Achievement and Consistency

Two of the core [[Lens Model Equation|lens-model]] quantities describing *how good* a judge is and *why*.

- **Achievement ($r_a$)** — the correlation between the judge's predictions and the actual criterion. The bottom-line accuracy number. Meta-analytic mean ≈ **.56**.
- **Response consistency / cognitive control ($R_s$)** — how reliably the judge applies their *own* policy across cases (correlation between the judge and the linear "model of the judge"). Mean ≈ **.80**. Also called **cognitive control** (Hammond & Summers 1972).

## Why consistency is the lever

A judge can know the right weights ($G$ high) yet still lose accuracy by applying them noisily ($R_s < 1$). Because $r_a = GR_eR_s$ (when $C=0$), inconsistency directly taxes achievement. This is the leak that [[Bootstrapping (Improper Linear Models)|bootstrapping]] plugs: modeling the judge sets $R_s = 1$ and recovers the lost accuracy.

## Empirical regularities (Karelaia & Hogarth 2008)

- Consistency is the lens component **least sensitive to learning** — it barely improves over trials.
- Consistency is **lower** when cues are achieved (not given), when redundancy is high, and when cue weights are noncompensatory.
- **Experts are somewhat more consistent than novices**, but the effect disappears once study features are controlled — and more expertise does **not** raise achievement or matching.
- Judges *describe* themselves as using complex nonlinear strategies but are well-modeled as linear with poor self-insight (see [[Policy Capturing]]).

## Applied significance

Low cognitive control is the mechanistic reason clinical judgment underperforms formulas in [[Mechanical vs Clinical Prediction|selection]]: holistic combination is degraded by $R_s<1$ and $G<1$ with no offsetting nonlinear insight ($C \approx 0$).

## Source

- [[karelaia-hogarth-2008-lens-model-meta-analysis]]; [[kuncel-et-al-2013-mechanical-vs-clinical]].
