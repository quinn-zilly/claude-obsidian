---
type: concept
address: c-000196
title: "Prospect Theory"
aliases: ["Kahneman-Tversky 1979", "PT"]
tags: [concept, jdm, decision-making, risk, loss-aversion, framing]
status: developing
created: 2026-05-23
updated: 2026-05-23
related: ["[[Framing Effects]]", "[[Judgment and Decision Making (Field)]]", "[[Heuristics and Biases Program]]", "[[Daniel Kahneman]]", "[[Amos Tversky]]", "[[connolly-2012-jdm]]", "[[tversky-kahneman-1974-heuristics-biases]]"]
---

# Prospect Theory

Descriptive model of risky choice. Kahneman & Tversky (1979). Developed to explain systematic violations of Expected Utility Theory (EUT), including the Allais Paradox.

## Core Modification from EUT

Value of a prospect = Σ v(xᵢ) · π(pᵢ)

Where v(·) is the **value function** and π(·) is the **decision weight function** — both departing from EUT.

## Value Function

Three key features:

1. **Reference-point based**: value defined relative to a reference point (often status quo), not absolute wealth
2. **Loss aversion**: value function steeper in loss domain than gain domain → losses more painful than equal gains are pleasurable
3. **Shape asymmetry**: concave above reference point (risk averse for gains) → convex below (risk seeking for losses)

```
Value
  |      /  (gains: concave, risk averse)
  |    /
  |  /
  |/____________ Reference point
  |\
  |  \  (losses: convex, risk seeking)
  |    \
       Outcome
```

This explains why framing a choice as losses vs. gains shifts risk preference.

## Decision Weight Function

- **Low probabilities overweighted**: people overestimate small risks (botulism > heart disease)
- **High probabilities underweighted**: certainty valued disproportionately
- **Nonlinear**: π(.9) − π(.89) ≠ π(.01)

Explains: preference for certainty (Allais paradox), overreaction to small risks in insurance/gambling.

## Implications

| Phenomenon | PT Explanation |
|---|---|
| Loss aversion | Steeper loss function |
| Endowment effect | Giving up = loss → overvalued |
| Status quo bias | Change = loss framing |
| Sunk cost escalation | Loss domain → risk seeking to avoid certain loss |
| Insurance purchase | Overweight of small p |
| [[Framing Effects]] | Same outcome, different reference point → different risk preference |

## Limitations as Descriptive Model

- Tversky (1969): transitivity violations not fully explained
- SP/A model (Lopes 1987) does better on some evidence
- [[Naturalistic Decision Making]]: expert decisions not primarily prospect-based

## CPT Extension and Empirical Status

[[Cumulative Prospect Theory]] (Tversky & Kahneman 1992) extended PT with rank-dependent probability weighting (addressing stochastic dominance violations).

**Fischhoff & Broomell 2020 update**: CPT parameters (including loss aversion) are highly variable across studies. Meta-analysis (Walasek et al. 2018) found weak overall evidence of loss aversion. [[Decision by Sampling]] model offers mechanistic alternative without stable parameters.

## Source

- [[connolly-2012-jdm]] — §Single-Choice Events: Prospect Theory
- [[fischhoff-broomell-2020-jdm-review]] — CPT empirical status update
- Original: Kahneman & Tversky (1979), Psychological Review
- Authors: [[Daniel Kahneman]], [[Amos Tversky]]
- See also: [[Cumulative Prospect Theory]], [[Loss Aversion]], [[Decision by Sampling]]
