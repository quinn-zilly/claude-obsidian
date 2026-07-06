---
address: c-000892
type: concept
title: "Case-Control Design"
tags:
  - concept
  - research-methods
  - causal-inference
  - quasi-experiments
  - epidemiology
status: seed
created: 2026-07-06
updated: 2026-07-06
related:
  - "[[Quasi-Experimental Design]]"
  - "[[Selection Bias]]"
  - "[[Coherent Pattern Matching]]"
  - "[[Threats to Validity]]"
sources:
  - "[[shadish-cook-campbell-2002-quasi-designs-no-control-or-no-pretest]]"
---

# Case-Control Design

Nav: [[index]] | [[log]]

A retrospective design (also **case-referent**, **case-comparative**, **case-history**) invented in and widely used in epidemiology. Instead of sampling on the *cause* and looking forward at effects, it **samples on the outcome** — a group of **cases** who have the outcome and a group of **controls** who do not — then looks **backward** to see whether cases experienced the hypothesized cause more often than controls. The outcome is typically dichotomous (diseased/healthy, relapsed/drug-free).

## When it beats an experiment

Preferable — sometimes the only option — when the outcome is **rare** or **slow to develop**, or when experimentation would be **unethical**. It is cheaper, faster, lowers participant risk, and lets you examine multiple candidate causes at once. Classic discoveries via case-control: smoking–cancer, birth-control pills–thromboembolism, and DES–vaginal cancer (Herbst et al. 1971: 7 of 8 cases exposed to DES, 0 of 32 matched controls).

## What it is good for

**Generating** causal hypotheses, more than confirming them. Because exposure is reconstructed retrospectively from fallible sources (memory, records), and because cases and controls are selected by different mechanisms, the design is bias-prone.

## The bias catalogue

SCC reproduce Sackett's (1979) list of **~35 biases** across six stages (reading the field, sampling, executing exposure, measuring, analyzing, interpreting) — e.g. recall bias, admission-rate (Berkson) bias, prevalence-incidence (Neyman) bias, diagnostic-suspicion bias. Selection of controls is the hardest problem; **multiple control groups** (general-population + neighborhood + same-source-of-care) help index and bracket the hidden bias. This makes the logic of ruling out [[Threats to Validity]] apply to case-control studies just as to other [[Quasi-Experimental Design|quasi-experiments]].
