---
address: c-000186
type: concept
title: "Base Rate Neglect"
aliases: ["Base Rate Fallacy", "Prior Probability Neglect"]
tags: [concept, cognitive-bias, judgment, probability, bayesian-reasoning]
status: developing
created: 2026-05-23
updated: 2026-05-23
related:
  - "[[Representativeness Heuristic]]"
  - "[[Heuristics and Biases Program]]"
  - "[[Amos Tversky]]"
  - "[[Daniel Kahneman]]"
  - "[[tversky-kahneman-1974-heuristics-biases]]"
---

# Base Rate Neglect

## Definition

The tendency to **ignore or underweight prior probabilities (base rates)** when evaluating the probability of an individual event or category membership, especially when individuating (descriptive) information is present.

Produced by the [[Representativeness Heuristic]]: representativeness is insensitive to prior probability, so when probability is assessed by representativeness, base rates drop out.

## Key Evidence (Tversky & Kahneman 1974)

**Engineer/lawyer study:**
- Group A: 70 engineers, 30 lawyers. Group B: 30 engineers, 70 lawyers.
- Same personality description ("Steve: very shy, withdrawn, helpful, passion for detail") → essentially identical probability judgments in both groups.
- Violates Bayes' rule: the correct odds ratio across conditions should be (.7/.3)² = 5.44:1.
- When *no* description was given: base rates correctly used (.7 and .3).
- When *uninformative* description given ("Dick": 30, married, high ability, well-liked): P(engineer) judged = .5 in *both* conditions — base rates fully ignored.

**Key asymmetry:** Base rates are used when they're the *only* information. They're discarded — even completely — when *any* descriptive information is present, even worthless information.

## Why It Matters

- Medical diagnosis: doctors underweight disease prevalence (base rate) when presented with vivid symptom descriptions.
- Hiring/selection: interviewers underweight base rates of success in a role when given detailed candidate descriptions.
- Research: tendency to predict outcomes that best represent the data, with insufficient regard for prior probability (even in statistically trained researchers).
- Screening tests: false positive rate is determined partly by disease prevalence, which is often ignored in intuitive probability assessment.

## Normative Standard

Bayes' theorem requires that posterior probability = prior probability × likelihood ratio. Base rate neglect is a systematic violation of Bayesian updating — it amounts to treating the likelihood ratio as if the prior were uniform.

## Related Concepts

- [[Representativeness Heuristic]] — the mechanism that produces base rate neglect
- [[Correlation-Intervention Gap (Behaviour)]] — selecting intervention targets based on correlational salience without accounting for base rate of effectiveness is a structural analog
