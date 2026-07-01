---
address: c-000767
type: concept
title: "Mechanical vs Clinical Prediction"
aliases: ["actuarial vs clinical", "mechanical vs holistic data combination", "statistical vs clinical prediction"]
tags: [concept, jdm, io-psychology, selection, prediction]
status: developing
created: 2026-06-30
updated: 2026-06-30
related: ["[[Bootstrapping (Improper Linear Models)]]", "[[Lens Model]]", "[[Judgmental Achievement and Consistency]]", "[[Job Performance (Outcomes of Job Attitudes)]]", "[[kuncel-et-al-2013-mechanical-vs-clinical]]", "[[karelaia-hogarth-2008-lens-model-meta-analysis]]"]
---

# Mechanical vs Clinical Prediction

The decades-old question of how best to **combine** predictor data into a decision:

- **Mechanical** (actuarial, algorithmic): apply a fixed formula/algorithm identically to every case — unit weights, optimal weights, decision trees.
- **Clinical** (holistic, judgmental, intuitive): a human combines the data using insight/judgment, individually or by committee.

The key distinction is the **combination** step, not data gathering — humans gather and generate cues well but integrate them poorly.

## The verdict

Mechanical combination consistently wins (Meehl 1954; Sawyer 1966; Grove & Meehl 1996). [[kuncel-et-al-2013-mechanical-vs-clinical|Kuncel et al. (2013)]] sized it for selection/admissions:

| Criterion | Mechanical | Clinical |
|---|---|---|
| Job performance | .44 | .28 |
| Advancement | .42 | .36 |
| Training | .31 | .16 |
| Academic GPA | .58 | .48 |

Job performance: **>50% prediction improvement**, ~25% more correct hires — and these are *underestimates* (no range-restriction or criterion-reliability correction). The mechanical edge held even where experts knew the job and had *more* information than the formula.

> [!tip] Converges with expertise research
> [[ericsson-lehmann-1996-expert-exceptional-performance|Ericsson & Lehmann (1996)]] reach the same conclusion from cognitive psychology: in judgment domains lacking rapid feedback, the *amount of experience* is poorly related to accuracy, and statistical models combining a few cues match or beat expert prediction (Dawes, Faust & Meehl 1989). Both literatures agree — [[Expert Performance (Ericsson Definition)|experience is not expertise]] absent feedback-rich [[Deliberate Practice|deliberate practice]].

## Why clinical loses (lens-model account)

Holistic judgment is degraded by inconsistency ($R_s<1$, low [[Judgmental Achievement and Consistency|cognitive control]]) and sub-optimal weighting ($G<1$), without a compensating gain in unique nonlinear insight ($C \approx 0$; [[karelaia-hogarth-2008-lens-model-meta-analysis|Karelaia & Hogarth 2008]]). It's the [[Bootstrapping (Improper Linear Models)|bootstrapping]] result applied to selection.

## Rebuttals to pro-clinical arguments

- *Jobs change* → performance structure is stable; linear models are weight-robust (Dawes 1979).
- *Small N* → borrow weights from meta-analysis or expert-set weights, then combine mechanically.

## The practice gap

Practitioners still prefer holistic judgment ([[Highhouse 2008]]) — an evidence-based-practice problem the field keeps re-litigating.

## Source

- [[kuncel-et-al-2013-mechanical-vs-clinical]]; theoretical basis in [[karelaia-hogarth-2008-lens-model-meta-analysis]].
