---
address: c-000993
type: concept
title: "Configural Relationships"
status: developing
tags:
  - concept
  - methods
  - configural
created: 2026-07-07
updated: 2026-07-07
related:
  - "[[Criterion Profile Analysis]]"
  - "[[Situation Strength]]"
  - "[[Ability-Motivation-Opportunity Model]]"
sources:
  - "[[wiernik-et-al-2021-meta-analytic-cpa]]"
---

# Configural Relationships

A relationship among variables is **configural** (or *pattern*) when "the interpretation of one item of information is contingent on another" (Hoffman 1960). Configuration can take infinitely many mathematical forms, but two matter most:

## Two types

- **Interactive** — multiplicative form ($X_1 \cdot X_2$). The relationship between $X_1$ and $Y$ *changes as a function of* $X_2$. Tested via product terms in moderated/polynomial regression. Example question: is a trait a stronger predictor when situational pressure is weak vs strong (cf. [[Situation Strength]])?
- **Contrastive** — difference form ($X_1 - X_2$). Concerns decomposing predictor variance into **between-person** (profile level/elevation) and **within-person** (relative pattern, irrespective of elevation) components, then relating those to $Y$. **Ipsative** patterns ($X_1 = 1 - \sum X_j$) are a special contrastive case where a score is interpreted relative to the person's own mean.

> [!key-insight] They are independent
> One, both, or neither can be present for a given predictor set. A **null interaction does not imply no configuration** — a contrastive pattern effect can exist even where the multiplicative term adds nothing. Van Iddekinge et al.'s (2018) ability×motivation data showed exactly this when reanalyzed with [[Criterion Profile Analysis|CPA]].

## Contrastive vs interactive — the key distinction

Contrastive relationships **decompose** an existing predictor set (into level + pattern). Interactive relationships **expand** the predictor set (add multiplicative composites). [[Criterion Profile Analysis]] targets the contrastive type.

## Fungible profile analysis

A sensitivity technique (Waller 2008): slightly perturb the input correlation matrix and check whether the estimated criterion pattern's **shape** is robust. Wiernik et al. (2021) recommend running it **routinely** before interpreting a criterion pattern.
