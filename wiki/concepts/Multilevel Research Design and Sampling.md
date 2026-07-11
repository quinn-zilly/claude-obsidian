---
type: concept
address: c-001121
title: "Multilevel Research Design and Sampling"
aliases: ["multilevel sampling", "multilevel research design", "multilevel analysis strategies"]
tags:
  - concept
  - multilevel-theory
  - methodology
  - research-design
status: developing
created: 2026-07-11
updated: 2026-07-11
related:
  - "[[Multilevel Theory in Organizations]]"
  - "[[Cross-Level Models]]"
  - "[[Aggregation Justification Indices]]"
  - "[[Entrainment]]"
  - "[[kozlowski-klein-2000-multilevel-approach]]"
  - "[[klein-kozlowski-2000-micro-to-meso]]"
---

# Multilevel Research Design and Sampling

Nav: [[index]] | [[Multilevel Theory & Methods MOC]]

The design counterpart to multilevel theory: sampling and analysis must be **aligned** with the levels of the constructs and the type of [[Cross-Level Models|model]].

## Sampling

> [!key-insight]
> Multilevel research generally requires sampling **many individuals in many units nested in many higher units** — not many people in one organization. Testing a cross-level model in a single organization risks **range restriction** on the higher-level construct (context constrains between-unit variance), precluding a fair test. "It is not reasonable to whine about range restriction in mixed-level data after the fact."

- **Shared constructs** need samples with **within-unit homogeneity** *and* **between-unit variability** — e.g., established teams that have developed shared norms, not newly formed groups.
- **Configural constructs** need units that **vary in their pattern/dispersion** (you can only study correlates of within-unit variability if units differ in it).
- **Time**: top-down effects → cross-sectional/short longitudinal designs suffice; bottom-up **emergent** effects → long-term longitudinal; **[[Entrainment|entrained]]** phenomena → sample on the theoretical time cycle.

## Analytic strategies (no single best technique)

- **ANCOVA / contextual analysis (OLS)** — earliest; contextual analysis contrasts individual predictors with unit means to detect a contextual effect. Aggregation often atheoretical; isomorphism not evaluated.
- **Cross-level / multilevel OLS regression** — treats aggregation as **construct validity** (evaluate emergence *before* aggregating).
- **WABA** (Dansereau et al. 1984) — decomposes within/between variance; establishes level of variables and relations.
- **MRCM / HLM** (Bryk & Raudenbush) — for nested data; Level-1 intercepts/slopes become Level-2 outcomes (intercepts → direct cross-level effects; slopes → cross-level moderation). GLS + EM estimation; statistical advantages over OLS.
- **MCSA** (Muthén 1994) — multilevel covariance structure analysis.

> [!note]
> Any of these can be **misused** to establish "the" level atheoretically. The conceptual meaning of an aggregation must have an **a priori theoretical foundation**. Selection depends on (a) consistency among construct type, data, and question, and (b) each technique's assumptions and limits.

Sources: [[kozlowski-klein-2000-multilevel-approach|Kozlowski & Klein (2000)]]; [[klein-kozlowski-2000-micro-to-meso|Klein & Kozlowski (2000)]].
