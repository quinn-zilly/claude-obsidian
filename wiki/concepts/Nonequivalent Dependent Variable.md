---
address: c-000889
type: concept
title: "Nonequivalent Dependent Variable"
tags:
  - concept
  - research-methods
  - causal-inference
  - quasi-experiments
status: seed
created: 2026-07-06
updated: 2026-07-06
related:
  - "[[Quasi-Experimental Design]]"
  - "[[Nonequivalent Control Group Design]]"
  - "[[Coherent Pattern Matching]]"
  - "[[Internal Validity]]"
  - "[[Threats to Validity]]"
sources:
  - "[[shadish-cook-campbell-2002-quasi-designs-no-control-or-no-pretest]]"
  - "[[shadish-cook-campbell-2002-quasi-designs-control-and-pretests]]"
---

# Nonequivalent Dependent Variable

Nav: [[index]] | [[log]]

A design element that adds a **second outcome measure (B)** alongside the target outcome (A), where B is:

- **not** expected to change in response to the treatment, but
- **is** expected to respond to the same salient [[Threats to Validity|internal-validity threats]] as A (history, maturation, testing…).

```
{O₁ₐ, O₁ᵦ}  X  {O₂ₐ, O₂ᵦ}
```

If the target A changes but the nonequivalent DV B does not, the inference that treatment caused the change is **strengthened** — a threat like history should have moved both. If both change, the effect is more likely due to the shared threat.

## Examples

- Robertson & Rossiter (1976): advertised toys rose in desirability (A) more than non-advertised toys (B) over the Christmas period — cultural gift-focus (history) should lift preference for *all* toys.
- McNees et al. (1979): feedback cut theft of potato chips (A) but not of ice cream, milk, or sandwiches (B).
- Minton (1975): Sesame Street watchers improved on *taught* letters (A) more than *untaught* letters (B), addressing maturation.

## Why it works

It is a form of [[Coherent Pattern Matching]]: the predicted A-changes-but-B-doesn't pattern is one that most alternative causes cannot generate. Rosenbaum frames the same idea statistically — "a systematic difference on an outcome the treatment does not affect must be a hidden bias." The design is broadly useful whenever both DVs are plausibly exposed to the same environmental causes to the same degree. Introduced in [[shadish-cook-campbell-2002-quasi-designs-no-control-or-no-pretest|SCC Ch. 4]]; used to strengthen cohort designs in [[shadish-cook-campbell-2002-quasi-designs-control-and-pretests|Ch. 5]].
