---
address: c-000157
type: concept
title: "Procedural Overfitting"
aliases: ["Analytic Overfitting", "Researcher Degrees of Freedom Overfitting"]
tags: [concept, machine-learning, methodology, open-science, psychology]
status: developing
created: 2026-05-22
related: ["[[Overfitting]]", "[[P-hacking]]", "[[Bias-Variance Tradeoff]]", "[[Cross-Validation]]", "[[Preregistration]]", "[[HARKing]]", "[[Questionable Research Practices]]", "[[Prediction vs Explanation (Psychology)]]", "[[yarkoni-westfall-2017-prediction-vs-explanation]]"]
---

# Procedural Overfitting

A reframing of p-hacking and flexible analytic practices as a form of [[Overfitting]] that occurs *prior to or in parallel with* model estimation — during data cleaning, model selection, covariate inclusion, and choice of which analyses to report.

**Primary source:** [[yarkoni-westfall-2017-prediction-vs-explanation]] (Yarkoni & Westfall, 2017)

## Core Idea

Whether a machine or a human draws the inference, the fundamental problem is the same:

> Every pattern that could be observed in a given dataset reflects some (generally unknown) combination of signal and error. The more flexible a statistical model or human investigator is willing to be — the wider the range of patterns they are willing to "see" — the greater the risk of hallucinating a pattern that is not there.

Like a 10th-order polynomial fit to linearly-generated data, a procedurally overfitted analysis tells an interesting story that fits the initial sample well but cannot be corroborated in future samples.

## Relationship to [[P-hacking]]

P-hacking (Simmons et al., 2011) / data-contingent analysis (Gelman & Loken, 2013) is the specific mechanism of procedural overfitting. The analyst selects procedures based — at least partly — on their results. This is structurally identical to a flexible model fitting noise: the human is the flexible model.

**Key evidence (John et al., 2012 survey):**
- 56% of psychologists admitted to optional stopping
- 46% selectively reported studies that "worked"
- 38% decided on exclusions after examining results

## Difficulty of Quantification

Unlike estimation-stage overfitting (quantifiable via cross-validation), procedural overfitting requires documenting *every* analysis step taken — something most researchers do not do. The extra "researcher degrees of freedom" are often invisible even to the authors themselves.

## Bias-Variance Framing

| Analytic strategy | Bias | Variance |
|-------------------|------|----------|
| Highly flexible data analysis | Low | High — almost any pattern can be detected, at cost of spurious identifications |
| Strict adherence to fixed procedures | High | Low — limited patterns identified, but hallucination risk is low |

Choosing how much flexibility to allow = choosing where to sit on the [[Bias-Variance Tradeoff]].

## Solutions

1. **[[Preregistration]]** — commits to analysis plan before data collection; constrains researcher df; shifts toward high-bias/low-variance
2. **[[Cross-Validation]] within the analysis loop** — embed all model selection decisions inside the CV procedure, not just the final estimator
3. **Hold-out test sets** — set aside a true test sample that is not inspected until all analysis is complete; allows full analytic flexibility on training data with guaranteed out-of-sample accountability
4. **Registered Reports** — in-principle acceptance before results; decouples publication from outcomes

## Connections

- [[P-hacking]] — the specific behavior that procedural overfitting conceptualizes
- [[HARKing]] — procedural overfitting at the write-up stage (post-hoc hypotheses presented as a priori)
- [[Overfitting]] — estimation-stage version of the same problem
- [[Replication Crisis]] — procedural overfitting is a primary mechanism explaining widespread replication failure
- [[Questionable Research Practices]] — broader category; procedural overfitting is the statistical framing
- [[Institutional Accretion]] — p-hacking and HARKing may be accreted field norms: micro-level practices adopted pragmatically that accumulated into field-level replication crisis (see [[micelotta-2017-pathways-institutional-change]])
