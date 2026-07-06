---
address: c-000874
type: source
title: "Shadish, Cook & Campbell (2002) — Statistical Conclusion Validity and Internal Validity"
authors: ["William R. Shadish", "Thomas D. Cook", "Donald T. Campbell"]
year: 2002
venue: "Experimental and Quasi-Experimental Designs for Generalized Causal Inference, Ch. 2"
tags:
  - source
  - research-methods
  - causal-inference
  - validity
  - experiments
  - quasi-experiments
status: seed
created: 2026-07-06
updated: 2026-07-06
related:
  - "[[Validity Typology]]"
  - "[[Statistical Conclusion Validity]]"
  - "[[Internal Validity]]"
  - "[[Threats to Validity]]"
  - "[[shadish-cook-campbell-2002-construct-external-validity]]"
---

# Shadish, Cook & Campbell (2002) — Statistical Conclusion Validity and Internal Validity

Nav: [[index]] | [[log]] | [[Open Science MOC]]

Chapter 2 of *Experimental and Quasi-Experimental Designs for Generalized Causal Inference* (the "SCC" successor to Cook & Campbell 1979). Lays out the theory of validity underlying generalized causal inference, then details the first two of four validity types with their threat lists.

## Validity: the core stance

Validity = the **approximate truth of an inference**. Key claims:

- Validity is a property of **inferences**, not of designs or methods. A randomized experiment does not "have" internal validity — attrition, low power, or bad statistics can still vitiate the inference. See [[Validity Typology]].
- No method guarantees a valid inference. Because methods map to validity types many-to-many, one design choice affects several validity types at once (e.g. randomization aids internal validity but can hamper external validity).
- The theory draws pragmatically on all three classical theories of truth (correspondence, coherence, pragmatism) rather than endorsing one.

## The four-type typology (history)

Campbell (1957) → Campbell & Stanley (1963): internal vs external validity. Cook & Campbell (1979) split these into four: statistical conclusion, internal, construct, external. This book keeps SCV/IV definitions ~unchanged (adding effect-size concerns) and broadens construct/external validity per Cronbach (1982). Full detail: [[Validity Typology]].

## [[Statistical Conclusion Validity]]

Validity of inferences about whether presumed cause and effect **covary** and **how strongly**. Two inference errors: existence of covariation (Type I / Type II) and magnitude of covariation. The book prefers reporting **effect sizes + 95% CIs** followed by exact p-values, over dichotomous NHST.

### Nine threats to SCV

1. **Low Statistical Power** — underpowered study wrongly concludes no relationship.
2. **Violated Assumptions of Statistical Tests** — e.g. non-independence (nested units) inflates Type I error.
3. **Fishing and the Error Rate Problem** — uncorrected multiple tests inflate significance (3 tests → α≈.14; 50 tests → α≈.92).
4. **Unreliability of Measures** — measurement error attenuates bivariate relations; unpredictable with 3+ variables.
5. **Restriction of Range** — floor/ceiling effects, dichotomizing continuous vars, similar treatments.
6. **Unreliability of Treatment Implementation** — inconsistent delivery across sites/persons.
7. **Extraneous Variance in the Experimental Setting** — noise, distraction inflate error.
8. **Heterogeneity of Units** — within-condition variability obscures covariation.
9. **Inaccurate Effect Size Estimation** — outliers, wrong ES metric for dichotomous outcomes. (New threat added in this edition.)

Note on **accepting the null**: you cannot prove the null (any nonzero effect emerges with enough power). Remedies: maximize power, specify a minimally interesting effect size, use equivalence testing.

## [[Internal Validity]]

Validity of inferences about whether observed A–B covariation reflects a **causal** relationship from A to B. Requires: A precedes B, A covaries with B, no plausible alternative explanation.

### Nine threats to IV

1. **Ambiguous Temporal Precedence** — unclear which variable came first (esp. correlational designs).
2. **Selection** — systematic pre-existing differences between conditions.
3. **History** — concurrent external events cause the outcome.
4. **Maturation** — natural change over time mistaken for treatment effect.
5. **Regression** (to the mean) — extreme-score selection yields less extreme retest scores.
6. **Attrition** — differential dropout correlated with condition.
7. **Testing** — prior test exposure affects later scores.
8. **Instrumentation** — measure changes over time/conditions.
9. **Additive and Interactive Effects of Threats** — threats compound or depend on each other.

## Threats method

A threat matters only if: (1) it plausibly (not just possibly) applies, and (2) it operates in the same direction as the observed effect. SCC prefer **design controls over statistical adjustment** for ruling threats out. See [[Threats to Validity]].

## Source

- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference* (Ch. 2). Houghton Mifflin.
