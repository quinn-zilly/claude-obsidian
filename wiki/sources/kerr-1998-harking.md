---
type: source
address: c-000125
title: "HARKing: Hypothesizing After the Results are Known"
author: "[[Norbert Kerr]]"
year: 1998
publication: "Personality and Social Psychology Review"
volume: 2
issue: 3
pages: "196–217"
doi: "10.1207/s15327957pspr0203_4"
tags:
  - open-science
  - research-methods
  - replication-crisis
  - questionable-research-practices
  - statistics
status: evergreen
related:
  - "[[HARKing]]"
  - "[[P-hacking]]"
  - "[[Publication Bias]]"
  - "[[Preregistration]]"
  - "[[Replication Crisis]]"
  - "[[Norbert Kerr]]"
created: 2026-05-21
updated: 2026-05-21
---

# Kerr 1998 — HARKing: Hypothesizing After the Results are Known

Nav: [[index]] | [[Open Science]] | [[HARKing]]

## Core Argument

Published scientific papers frequently present hypotheses as *a priori* predictions when they were actually generated or refined *after* observing the data. Kerr coins the term **HARKing** — Hypothesizing After the Results are Known — for this practice and argues it is widespread, largely unconscious, and deeply damaging to scientific progress.

HARKing is not outright fraud. It exploits a cognitive and social gap: hindsight bias makes post-hoc hypotheses *feel* like a priori ones, and reviewers cannot detect the difference.

## Three Forms of HARKing

Kerr distinguishes three variants:

| Form | Description |
|------|-------------|
| **Type 1 (Classic HARKing)** | Formulate hypothesis post-hoc; present it as if predicted before data collection |
| **Type 2 (Omission HARKing)** | Drop originally predicted hypotheses that were not supported; only report the ones that worked |
| **Type 3 (Pirating)** | Incorporate others' serendipitous findings into one's own report as if they were one's own a priori predictions |

All three distort the confirmatory appearance of the literature.

## Mechanisms That Enable HARKing

### Cognitive: Hindsight Bias
Once a result is known, it is psychologically difficult to *not* see it as predictable. Researchers may genuinely believe their post-hoc hypothesis was a priori. This is a cognitive failure, not a moral one — making HARKing especially resistant to correction through appeals to ethics alone.

### Social: Norms of Science as Hypothetico-Deductive
The standard narrative of science (hypothesis → test → result) creates strong pressure to conform to that structure in publications. Papers that report exploratory finding-driven research are viewed as scientifically inferior. This social norm rewards HARKing.

### Structural: Publication Bias
Journals prefer confirmatory results. A null result on an original hypothesis is less publishable. HARKing transforms a messy mixed-result study into a clean "confirmation" — which is then more publishable.

### Detection Barrier
Reviewers and readers cannot see what hypotheses were originally specified. There is no timestamp. No audit trail. The researcher has complete control over the narrative.

## Statistical Consequences

A p-value is only valid for a hypothesis specified *prior* to seeing the data it is tested against. A hypothesis derived from the same data it "tests" has:
- No valid null distribution
- An inflated Type I error rate (the result *always* looks significant because it was derived from the data)
- A suppressed apparent Type II error rate

When HARKing becomes widespread:
- The literature's false positive rate inflates dramatically above the nominal α level
- Effect sizes are systematically overestimated (the observed effect in the HARKed result is always at least as large as the threshold that inspired the hypothesis)
- Replication failures become expected, not anomalous

## Scientific and Epistemic Consequences

- **False theory confirmation**: Theories accumulate support they have not earned
- **Inhibited progress**: Theories that should have been revised or abandoned persist because their failures are hidden (Type 2 HARKing)
- **Corrupted literature**: The published record increasingly represents researcher degrees of freedom, not real effects
- **Hindered meta-analysis**: Effect size estimates are upward biased; cumulative science misfires

> [!key-insight] The Base Rate Problem
> If most published confirmations are HARKed, then the literature is a catalog of exploratory pattern-matches. Each needs independent replication to count as evidence. Most never get it. The field mistakes a pattern library for a body of established knowledge.

## Remedies Proposed

Kerr anticipates several reform directions that later become the open science movement's core tools:

1. **Preregistration**: Timestamp hypotheses before data collection. Makes HARKing detectable.
2. **Explicit separation of confirmatory and exploratory research**: Label post-hoc hypotheses as such in publications.
3. **Registered Reports**: Submit hypothesis and method *before* data collection; journal commits to publication regardless of result.
4. **Replication requirement**: Treat confirmatory evidence as requiring at least one independent replication.
5. **Normative change**: Reward well-designed studies, not confirmatory outcomes.

## Relationship to Other QRPs

HARKing is part of a broader cluster of **Questionable Research Practices (QRPs)**:

| QRP | Stage | Mechanism |
|-----|-------|-----------|
| [[P-hacking]] | Analysis | Try multiple tests until p < .05 |
| HARKing | Write-up | Reframe hypothesis to match result |
| [[Publication Bias]] | Dissemination | Journals reject null results |
| Selective reporting | Write-up | Report only significant outcomes |

These QRPs often co-occur and compound: P-hacking finds a significant result; HARKing makes it look predicted; publication bias ensures only the HARKed version reaches the literature.

## Significance

Kerr 1998 is the **origin paper** for the concept of HARKing. It predates the replication crisis by over a decade and anticipates nearly every reform that the open science movement later proposes. The paper is frequently cited in:
- [[Replication Crisis]] literature
- [[Preregistration]] methodology papers
- Debates about [[Registered Reports]]
- The [[munafo-2017-manifesto|Munafò 2017 manifesto]] (cites Kerr explicitly in the research cycle diagram)

## See Also

- [[HARKing]] — concept page
- [[Norbert Kerr]] — author
- [[P-hacking]] — complementary QRP
- [[Publication Bias]] — structural enabler
- [[Preregistration]] — primary remedy
- [[Registered Reports]] — strongest remedy
- [[giner-sorolla-2012-science-or-art]] — frames HARKing as aesthetic/presentational pressure (narrative conformity), not just strategic incentive
- [[nosek-2018-preregistration]] — operationalizes the preregistration remedy
- [[munafo-2017-manifesto]] — places HARKing in the full research cycle threat map
