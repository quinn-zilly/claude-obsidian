---
type: concept
address: c-000194
title: "Lens Model"
aliases: ["Brunswik lens model", "lens model equation"]
tags: [concept, jdm, judgment, inference, policy-capturing]
status: developing
created: 2026-05-23
updated: 2026-05-23
related: ["[[Policy Capturing]]", "[[Judgment and Decision Making (Field)]]", "[[connolly-2012-jdm]]"]
---

# Lens Model

Framework for studying judgment accuracy. Originally from Brunswik (1952) on visual perception; Hammond (1955) extended to human judgment.

## Core Structure

```
Environment side          Judge side
Criterion (Y_e) ←── Cues (X_i) ──→ Judgment (Y_s)
```

- **Left side**: underlying variable of interest generates imperfect *cues*
- **Right side**: judge combines cues into a judgment
- **Achievement**: correlation between Y_e and Y_s

Both cue validities (environment side) and cue utilization (judge side) affect accuracy. **Lens Model Equation** (Tucker 1964) decomposes overall achievement mathematically.

## Representative Design

Brunswik's methodological precept: cue ranges and intercorrelations in experiments must reflect the natural environment being studied. Factorial crossing of cues destroys natural intercorrelations → distorts judge's normal policy → produces incredible stimuli.

In practice this is hard to satisfy: truncated ranges (only hired applicants observed), changing pools, selection effects.

## Policy Capturing

Specific application: develop regression model of an individual judge. See [[Policy Capturing]] for full treatment.

Key generalizations (with caution):
- Judges use few cues
- Linear models adequate
- Judges claim nonlinear, interactive strategies (but models show linear)
- Low test-retest reliability
- Low inter-judge agreement even among experts

## Source

- [[connolly-2012-jdm]] — §Inference Processes
- Original: Brunswik (1952); Hammond (1955)
