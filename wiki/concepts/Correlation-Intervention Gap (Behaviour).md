---
address: c-000168
type: concept
title: "Correlation-Intervention Gap (Behaviour)"
tags: [concept, methodology, behaviour-change, meta-analysis, causal-inference]
status: developing
created: 2026-05-23
updated: 2026-05-23
related:
  - "[[Behaviour Change Determinants]]"
  - "[[albarracin-2024-determinants-behaviour-change]]"
  - "[[Prediction vs Explanation (Psychology)]]"
---

# Correlation-Intervention Gap (Behaviour)

The systematic pattern whereby the correlation between a behavioural determinant and behaviour (in observational studies) overestimates how much intervening on that determinant will change behaviour (in experimental/quasi-experimental studies). A core methodological finding of Albarracín et al. (2024).

## The Pattern

For every individual determinant reviewed, correlational effect sizes exceed intervention effect sizes:

| Determinant | Correlation (mean OR) | Intervention (mean OR) |
|---|---|---|
| Knowledge | ~2.0 | ~1.11 |
| General skills | ~1.81 | ~1.23 |
| General attitudes | ~2.58 | ~1.35 |
| Beliefs | ~1.89 | ~1.43 |
| Emotions | ~2.52 | ~1.60 |
| Behavioural skills | ~3.43 | ~1.99 |
| Behavioural attitudes | ~3.70 | ~2.09 |
| Habits | ~6.17 | ~2.65 |

The gap is largest for general attitudes, habits, and beliefs — exactly the targets most commonly selected based on correlational rationale.

## Explanations

1. **Reverse causation / rationalisation**: people may *report* attitudes/beliefs that rationalise their already-performed behaviour (cognitive dissonance, self-perception theory), rather than attitudes causing behaviour.

2. **Confounding**: third variables (demographics, access, structural conditions) simultaneously drive both the determinant and the behaviour, inflating correlations.

3. **Laboratory vs. field context**: correlational studies often measure behaviour in artificial/laboratory contexts where the measured attitude dominates (fewer competing factors). Real-world behaviour involves multiple determinants simultaneously.

4. **Statistical artefacts**: regression to the mean, shared method variance, temporal ordering in correlational designs.

## Implications

> [!key-insight] Do Not Use Correlational Evidence to Select Intervention Targets
> This is the operational lesson of Albarracín et al. 2024. Correlational evidence tells you what *predicts* behaviour — not what *changes* it. These are different questions. See also [[Prediction vs Explanation (Psychology)]] for the general principle.

Policymakers who select intervention targets based on what "correlates with" the desired behaviour will systematically over-invest in knowledge, attitude, and belief interventions — the weakest levers — and under-invest in access and social support — the strongest.

## Connection to Open Science / Prediction vs. Explanation

The correlation-intervention gap is a domain-specific instance of the broader tension between prediction and explanation (see [[Prediction vs Explanation (Psychology)]], Yarkoni & Westfall 2017). Correlational social science is optimised for explanatory models; it conflates predictive accuracy with causal intervention potential.

## Sources

- [[albarracin-2024-determinants-behaviour-change]]
- [[yarkoni-westfall-2017-prediction-vs-explanation]] (related general principle)
