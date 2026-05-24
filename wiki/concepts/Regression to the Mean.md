---
address: c-000189
type: concept
title: "Regression to the Mean"
tags: [concept, statistics, cognitive-bias, judgment, causal-inference]
status: developing
created: 2026-05-23
updated: 2026-05-23
related:
  - "[[Representativeness Heuristic]]"
  - "[[Heuristics and Biases Program]]"
  - "[[Gambler's Fallacy]]"
  - "[[Amos Tversky]]"
  - "[[Daniel Kahneman]]"
  - "[[tversky-kahneman-1974-heuristics-biases]]"
---

# Regression to the Mean

## Statistical Definition

When two variables X and Y have the same distribution and individuals are selected based on extreme X scores, their Y scores will, on average, be less extreme — closer to the mean of Y by less than k units when X scores deviate from the mean by k units.

Galton first documented this phenomenon over 100 years before Tversky & Kahneman (1974). It is a mathematical consequence of imperfect correlation, not a causal mechanism.

## Why Intuition Fails

The [[Representativeness Heuristic]] leads people to expect that predicted outcomes should be *as extreme* as their inputs. Regression toward the mean violates this expectation — it seems wrong that a top performer should be expected to do worse next time, or that a poor performer should be expected to improve, absent any intervention.

Two failures of intuition (Tversky & Kahneman 1974):
1. People **do not expect** regression in contexts where it is bound to occur.
2. When they **recognize** regression, they invent spurious causal explanations for it.

## The Instructor Fallacy

> "In a discussion of flight training, experienced instructors noted that praise for an exceptionally smooth landing is typically followed by a poorer landing on the next try, while harsh criticism after a rough landing is usually followed by an improvement on the next try." — Tversky & Kahneman (1974)

The instructors concluded: verbal rewards are detrimental to learning; verbal punishment is beneficial.

**Correct interpretation:** Both outcomes are regression to the mean. An exceptionally good landing is partly luck; the next will likely be closer to average. An exceptionally poor landing is partly bad luck; the next will likely be closer to average. The instructor's praise/punishment is incidental — the regression would have occurred either way.

**Pernicious consequence:** Reinforcement of punishment as a management/training strategy, contrary to psychological evidence that reward is generally more effective for skill learning.

## Social Implications

> "By regression alone, behavior is most likely to improve after punishment and most likely to deteriorate after reward. Consequently, the human condition is such that, by chance alone, one is most often rewarded for punishing others and most often punished for rewarding them."

This creates a structural illusion across many domains (parenting, coaching, management, medicine) that punishment/harsh intervention "works" — not because it does, but because it is administered when performance is worst, which is precisely when regression-to-mean improvement is most likely.

## Research Implications

- **Decline effect** ([[Yarkoni & Westfall 2017]]): Effect sizes shrink as a literature matures — initial studies select extreme estimates (partly by chance); subsequent replication finds lower values. This is regression to the mean at the literature level, compounded by publication bias.
- **Pre-post designs without control groups**: Patients selected for treatment because their symptoms are worst (floor-effect selection) will improve on average via regression, which may be misattributed to the intervention.
- **[[Replication Crisis]]**: Grossly overestimated effect sizes in small-sample studies partly reflect selection of extreme estimates; replication finds regression to the true effect.
