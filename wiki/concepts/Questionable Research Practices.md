---
address: c-000140
type: concept
title: "Questionable Research Practices"
aliases: ["QRPs"]
tags: [open-science, methodology, replication, publication-bias]
status: developing
created: 2026-05-22
updated: 2026-05-22
related: ["[[P-hacking]]","[[HARKing]]","[[Publication Bias]]","[[Preregistration]]","[[Replication Crisis]]","[[nosek-2022-replicability-robustness-reproducibility]]","[[Conflict of Interest in Science]]","[[Motivated Reasoning]]"]
  - "[[Open Science MOC]]"
---

# Questionable Research Practices (QRPs)

Behaviors that leverage analytic flexibility and publication incentives to inflate effect sizes, obtain statistical significance, or selectively report findings — reducing replicability without constituting outright fraud.

## Core QRPs

- **[[P-hacking]]**: trying multiple analyses, covariates, exclusion rules until p < .05
- **[[HARKing]]**: Hypothesizing After Results are Known; presenting post-hoc predictions as a priori
- **Selective outcome reporting**: conducting multiple DVs, reporting only significant ones (9–43% of researchers acknowledge this; Nosek et al. 2022 survey summary)
- **Selective study reporting**: running multiple studies, publishing only those that "worked" (25–62% acknowledgement rate)
- **Optional stopping**: collecting data until significant, then stopping

## Prevalence (14 surveys, N=7,887; Nosek et al. 2022)

| QRP | Acknowledgement range |
|---|---|
| Failed to report all outcomes | 9–43% |
| Selectively reported "working" studies | 25–62% |

QRPs are relatively common; but longitudinal trend unclear (most surveys ask "ever," not frequency; sampling varies).

## Mechanism

QRPs are **ordinary psychology under misaligned incentives** — not fraud requiring conscious intent. Publication pressure + analytic flexibility + no audit trail → rational exploitation of researcher degrees of freedom. Aligns with Giner-Sorolla (2012) [[Publication Bottleneck]] argument and Nosek et al. 2012 [[Conflict of Interest in Science]].

## Why QRPs Reduce Replicability

Original findings that result from QRPs contain inflated effect sizes or false positives. When replicated with larger samples and no QRPs, effect disappears or shrinks sharply.

## Structural Fixes (not attitude fixes)

Knowledge of QRPs and good intentions insufficient — structural solutions required:
- [[Preregistration]] eliminates opportunity for most p-hacking and HARKing
- [[Registered Reports]] removes publication pressure from analysis stage
- Open data sharing enables post-hoc detection
- Badges increase visibility of open practices

> "Structural solutions such as preregistration and transparency may be needed to mitigate the opportunity for reasoning biases to affect judgment." (Nosek et al. 2022)

## Simmons et al. (2011) Taxonomy

Four key QRPs identified:
1. Multiple DVs reflecting same outcome — report only significant one
2. **Optional stopping**: interim analysis, stop when p < .05
3. Multiple covariate models — report the one that works
4. Drop groups or levels to isolate a larger subgroup effect

These can combine to inflate Type I error grossly above α = .05 even without HARKing.

## Bakker & Wicherts (2011)

Checked 281 articles; 18% had statistical errors. The vast majority made results *more* significant — consistent with motivated or opportunistic calculation.

## Cross-References
- [[P-hacking]] — analytic flexibility
- [[HARKing]] — Kerr (1998) origin paper
- [[Publication Bias]] — file drawer; filters QRP results into literature
- [[Motivated Reasoning]] — individual mechanism
- [[Institutional Accretion]] — QRPs as accreted field norms (Micelotta connection)
- [[shrout-rodgers-2018-replication-crisis]] — comprehensive review of QRP types and their contribution to the replication crisis
