---
address: c-000187
type: concept
title: "Gambler's Fallacy"
tags: [concept, cognitive-bias, judgment, probability, randomness]
status: developing
created: 2026-05-23
updated: 2026-05-23
related:
  - "[[Representativeness Heuristic]]"
  - "[[Heuristics and Biases Program]]"
  - "[[Regression to the Mean]]"
  - "[[Amos Tversky]]"
  - "[[Daniel Kahneman]]"
  - "[[tversky-kahneman-1974-heuristics-biases]]"
---

# Gambler's Fallacy

## Definition

The erroneous belief that in a random process, a deviation from expected outcomes in one direction will be corrected by a deviation in the opposite direction in subsequent trials.

**Classic form:** After observing a long run of red on a roulette wheel, believing that black is "due" — more likely than 50% on the next spin.

## Mechanism (Tversky & Kahneman 1974)

The gambler's fallacy is a consequence of the [[Representativeness Heuristic]] operating at the level of *local sequences*.

People expect that short sequences of random events will be *locally representative* of the underlying process — balanced, alternating, "random-looking." A long run of heads violates this expectation, so tails feels more probable (to restore local balance).

This is distinct from the true self-correcting property of random processes: in the long run, deviations *are* diluted — but not because subsequent outcomes correct them. Deviations are diluted because they become proportionally smaller relative to a growing sample. Early outcomes are not corrected; they are simply outweighed.

> "Chance is commonly viewed as a self-correcting process in which a deviation in one direction induces a deviation in the opposite direction to restore the equilibrium. In fact, deviations are not 'corrected' as a chance process unfolds, they are merely diluted." — Tversky & Kahneman (1974)

## Sequence Preferences

Subjects judge H-T-H-T-T-H more likely than H-H-H-T-T-T (non-random-looking) and H-H-H-H-T-H (unfair-looking). But for a fair coin, all sequences of length 6 are equally likely.

## Law of Small Numbers

Related belief: even small samples are highly representative of their populations (a flip-side of the gambler's fallacy applied to research). Experienced psychologists show this — they put too much faith in small-sample results and grossly overestimate replicability. See [[Replication Crisis]].

## Connection to Research Methodology

The gambler's fallacy manifests in sequential data collection: a researcher who sees p = .06 after N subjects may believe that the "true" result will emerge with a few more observations — in fact, the probability that adding more participants will push the p-value below .05 given the current result is not well-calibrated by intuition. This underlies some forms of [[P-hacking]] (optional stopping).
