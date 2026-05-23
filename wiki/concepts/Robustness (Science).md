---
address: c-000138
type: concept
title: "Robustness (Science)"
aliases: ["Analytic Robustness", "Robustness Checks"]
tags: [open-science, methodology, replication]
status: developing
created: 2026-05-22
related: ["[[Analytic Reproducibility]]","[[Replicability]]","[[Multiverse Analysis]]","[[P-hacking]]","[[Preregistration]]","[[nosek-2022-replicability-robustness-reproducibility]]"]
---

# Robustness (Science)

Testing the reliability of a prior finding using the **same data and a different analysis strategy** (Nosek et al. 2022). Distinct from [[Analytic Reproducibility]] (same data, same analysis) and replicability (different data).

## Core Idea

Some findings are robust — consistent across reasonable analytic variation (different exclusion criteria, different covariates, different model specifications). Others are **fragile** — contingent on specific analytic decisions.

Fragility ≠ wrong, but fragility is a risk factor for:
- Replicability failure
- Generalizability failure
- Unacknowledged [[P-hacking]] when fragile result selected from many paths

## Key Evidence

**Silberzahn et al. (2018)**: 29 analysis teams given same data, same research question → substantial variation in results.

**Botvinik-Nezer et al. (2020)**: neuroimaging — 70 teams, one dataset → similarly divergent results.

## Robustness ↔ Preregistration

Without precommitment to analysis plan, fragile findings amplify p-hacking concerns (Simonsohn et al. 2020, Steegen et al. 2016). [[Preregistration]] separates planned from unplanned analyses, calibrating confidence appropriately.

## Tools

- **Multiverse analysis** (Steegen et al. 2016, Simonsohn et al. 2020): run all reasonable analytic specifications; display full distribution of outcomes
- **Specification curve analysis**: formal version of multiverse; tests whether effect holds across most reasonable paths
- **Robustness checks**: common informal practice; often selectively reported

## Relation to Other R's

| | Data | Analysis |
|---|---|---|
| Reproducibility | Same | Same |
| Robustness | Same | Different |
| Replicability | Different | New |

See [[nosek-2022-replicability-robustness-reproducibility]] for full framework.
