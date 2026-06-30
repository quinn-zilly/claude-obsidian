---
type: concept
address: c-000772
title: "Subjective Expected Utility"
aliases: ["SEU", "subjective expected utility theory"]
tags: [jdm, decision-making, normative-model, utility, probability, savage]
status: developing
created: 2026-06-30
updated: 2026-06-30
related: ["[[Prospect Theory]]", "[[Multiattribute Utility Theory]]", "[[Framing Effects]]", "[[Heuristics and Biases Program]]", "[[wiki/sources/connolly-2012-jdm|Connolly et al. 2012]]"]
---

# Subjective Expected Utility

Nav: [[index]] | [[Prospect Theory]]

The dominant **normative** model of choice under uncertainty: a decision maker should value each option as the sum, over its possible outcomes, of each outcome's **subjective utility** weighted by its **subjective probability**, and choose the option with the highest total.

$$
SEU = \sum_i s(p_i)\, u(x_i)
$$

where $u(x_i)$ is the decision maker's utility for outcome $x_i$ and $s(p_i)$ is their (personal, belief-based) probability that it occurs.

## Lineage

SEU is the endpoint of a progression from objective to fully subjective valuation:

| Model | Values outcomes by | Probabilities | Key figure |
|---|---|---|---|
| Expected Value (EV) | objective amount $x$ | objective | (classical) |
| Expected Utility (EU) | subjective utility $u(x)$ | objective | von Neumann & Morgenstern (1947) |
| **Subjective Expected Utility (SEU)** | subjective utility $u(x)$ | **subjective** $s(p)$ | **Savage (1954)** |

- **EV → EU**: Bernoulli's (1738) **St. Petersburg Paradox** — a coin-flip game paying \$2ⁿ has infinite EV, yet people pay under \$4 — showed people value prospects by *utility*, not objective amount. von Neumann & Morgenstern axiomatized EU via "probabilistic in-betweenness."
- **EU → SEU**: Savage (1954) added *subjective probabilities*, so the model can value not just monetary gambles but any uncertain event by the decision maker's **degree of belief**. This extended decision theory to the vast class of decisions where no objective probabilities exist.

## Why It Matters as a Normative Standard

SEU's axioms (e.g., **transitivity** — if A ≻ B and B ≻ C then A ≻ C; and **independence**) are individually "strict but perfectly reasonable." Their appeal is what makes SEU the yardstick against which descriptive deviations are measured. The model also gives a single, consistent metric for every node of a decision tree, letting complex choices be evaluated by one logic.

## Empirical Violations → Descriptive Successors

SEU is a good *normative* but weak *descriptive* model. Documented axiom violations drove the field's main descriptive theories:

- **Transitivity** violated in certain designs (Tversky 1969).
- **Independence** violated by the **Allais Paradox** (Allais 1953).
- **Ambiguity** sensitivity (Ellsberg 1961) — people avoid unknown probabilities, which SEU's subjective $s(p)$ should not predict.

[[Prospect Theory]] (Kahneman & Tversky 1979) keeps SEU's "evaluate, discount, add" form but replaces its functions with psychologically descriptive ones: value defined over **changes from a reference point** (not total wealth), **loss aversion**, risk-aversion in gains / risk-seeking in losses, and a **decision-weight** function that overweights low and underweights high probabilities. [[Framing Effects]] follow directly from this reference-dependence — something SEU, being description-invariant, cannot accommodate.

> [!note] Relation to MAUT
> [[Multiattribute Utility Theory]] is the *riskless* multi-attribute cousin: it sums weighted utilities across an option's attributes, where SEU sums weighted utilities across an option's uncertain outcomes. Both are compensatory, normatively complete, and effortful.

## Cross-References

- [[wiki/sources/connolly-2012-jdm|Connolly, Ordóñez & Barker (2012)]] — situates SEU in the EV→EU→SEU→Prospect Theory arc (§4, Single-Choice Events).
- [[Prospect Theory]] — the leading descriptive alternative.
- [[Multiattribute Utility Theory]] — riskless multi-attribute analog.
- [[Heuristics and Biases Program]] — the research program built on documenting deviations from normative models like SEU.
