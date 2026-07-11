---
type: concept
address: c-001118
title: "Aggregation Justification Indices"
aliases: ["rwg", "ICC(1)", "ICC(2)", "eta-squared", "WABA", "within-group agreement", "justifying aggregation"]
tags:
  - concept
  - multilevel-theory
  - measurement
  - statistics
status: developing
created: 2026-07-11
updated: 2026-07-11
related:
  - "[[Global, Shared, and Configural Unit Properties]]"
  - "[[Levels of Analysis Fallacies]]"
  - "[[Multilevel Research Design and Sampling]]"
  - "[[klein-kozlowski-2000-micro-to-meso]]"
---

# Aggregation Justification Indices

Nav: [[index]] | [[Multilevel Theory & Methods MOC]]

Before averaging individual data to represent a **[[Global, Shared, and Configural Unit Properties#Shared unit properties|shared unit property]]**, a researcher must demonstrate the data are homogeneous *within* units (the composition/isomorphism assumption). Several indices do this — each answering a subtly different question.

## Consensus vs consistency

| Index | Approach | Question answered | Notes |
|---|---|---|---|
| **$r_{wg}$** (James, Demaree & Wolf 1984) | **Consensus** — *construct-by-group* | How high is within-group agreement on one variable in **one** unit? | Compares within-unit variance to an **expected variance (EV)**. Assesses each unit separately → avoids per-group misspecification. Rectangular-EV overstates agreement; alternatives: bias-based EV (Kozlowski & Hults 1987), random group resampling (Bliese 2000). Rule-of-thumb cutoff ≈ **.70** (only a rule of thumb). |
| **$\eta^2$** | **Consistency** — *construct-by-sample* | What proportion of total variance is between-unit vs within-unit? | Inflated for small groups (<25/group; Bliese & Halverson 1998). |
| **ICC(1)** | Consistency | Proportion of variance explained by unit membership; interchangeability of raters | Unlike $\eta^2$, does **not** vary with group size. |
| **ICC(2)** | Consistency | Reliability of the **unit mean** | Analogous to a reliability of the aggregated score. |
| **WABA** | Consistency | Level of variables (WABA I) and of relations (WABA II) — within, between, or both | Dansereau et al. 1984; extends to multivariate. |

> [!key-insight]
> **Consensus** approaches ($r_{wg}$) treat "is it shared?" and "does it relate to other things?" as **separate** questions — avoiding misspecification but risking insufficient between-group variance for testing relations. **Consistency** approaches (η², ICC, WABA) fold both into one and guarantee between-unit variance, but can mask groups where the construct isn't actually shared. Neither is universally preferable — **choice follows theory and data.**

Item **referent** also matters: unit-referent wording ("Employees' work here is rewarding") produces less within-group variance than self-referent wording ("My work here is rewarding") (Klein, Conn, Smith & Sorra) — see [[Referent-Shift Consensus]].

Source: [[klein-kozlowski-2000-micro-to-meso|Klein & Kozlowski (2000)]].
