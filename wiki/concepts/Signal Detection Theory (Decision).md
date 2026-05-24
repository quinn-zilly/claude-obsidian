---
type: concept
address: c-000206
title: "Signal Detection Theory (Decision)"
aliases: ["TSD", "signal detection theory", "ROC curve", "theory of signal detection"]
tags: [concept, jdm, decision-making, diagnostic, threshold, signal-detection]
status: developing
created: 2026-05-23
updated: 2026-05-23
related: ["[[Judgment and Decision Making (Field)]]", "[[Policy Capturing]]", "[[connolly-2012-jdm]]"]
---

# Signal Detection Theory (Decision) (TSD)

Framework for threshold-setting in diagnostic decisions with two mutually exclusive outcomes. Roots in radar operator guidance (WWII); extended to medical diagnosis, personnel selection, quality control, legal decisions.

## Core Structure

An evidence system produces a probabilistic score. Decision maker sets a **threshold**: act as if signal present (positive) if score exceeds threshold.

Four outcomes:

|  | Signal Present | Signal Absent |
|---|---|---|
| **Respond Positive** | True Positive (hit) | False Positive (false alarm) |
| **Respond Negative** | False Negative (miss) | True Negative (correct rejection) |

## ROC Curve

Plot of true-positive rate vs. false-positive rate across all possible thresholds.

- Strict threshold → few false positives, few true positives
- Lax threshold → many true positives, many false positives
- Better evidence system → curve higher and to the left

**Accuracy** = area under ROC curve.

## Threshold Setting

Optimal threshold depends on:
1. **Base rate** of signal in population
2. **Cost of false positive** vs. **cost of false negative**

Same evidence system, different costs → different thresholds. Example: HIV test for blood donation (false positive = wasted pint of blood) vs. patient diagnosis (false positive = life-altering wrongful diagnosis) → very different thresholds warranted.

## Drug Testing Example (Connolly et al.)

1% drug prevalence + 90% accurate test:
- P(user | positive test) = **8.3%** (not 90%)
- Most positives are false positives
- Ignoring base rate → massive overestimation of test accuracy

→ Base rate neglect (also in [[Heuristics and Biases Program]] / Representativeness section).

## Organizational Underuse

> "Although it is easy to imagine the value of a TSD approach to a wide range of organizational decisions such as hiring, termination, new product development or R&D project selection, this potential does not appear to have been much tapped." — Connolly et al. 2012

Exception: Puranam, Powell & Singh (2006) on M&A due diligence.

TSD largely ignored in JDM research despite high applied relevance.

## Cross-References

- [[Heuristics and Biases Program]] — base rate neglect is the TSD failure mode for representativeness
- [[Policy Capturing]] — contrasting diagnostic approach: model judge's cue weights
- [[connolly-2012-jdm]] — §Single-Choice Events: TSD
