---

type: source
address: c-000023
title: "A Unified Framework to Quantify the Credibility of Scientific Findings"
author: "Etienne P. LeBel, Wolf Vanpaemel, Irene Cheung, Lorne Campbell"
year: 2018
venue: "Advances in Methods and Practices in Psychological Science"
volume: 1
issue: 3
pages: "389–402"
doi: "10.1177/2515245918787489"
tags:
  - open-science
  - credibility
  - replication
  - research-methods
  - meta-science
status: ingested
ingested: 2026-05-19
related:
  - "[[Etienne LeBel]]"
  - "[[Wolf Vanpaemel]]"
  - "[[Analytic Reproducibility]]"
  - "[[Replication]]"
  - "[[Open Science]]"
  - "[[Preregistration]]"
  - "[[nosek-2018-preregistration]]"
  - "[[open-science-collaboration-2015]]"
  - "[[munafo-2017-manifesto]]"
created: unknown
updated: unknown
---

# LeBel et al. (2018) — A Unified Framework to Quantify the Credibility of Scientific Findings

> [!key-insight] Core Claim
> Scientific credibility is multidimensional. A unified framework assesses four distinct aspects — transparency, analytic reproducibility, analytic robustness, and effect replicability — each of which can be independently verified and graded. Current practice conflates them, obscuring what "credible" actually means.

## Bibliographic Details

Etienne P. LeBel, Wolf Vanpaemel, Irene Cheung, and Lorne Campbell. "A Unified Framework to Quantify the Credibility of Scientific Findings." *Advances in Methods and Practices in Psychological Science* 1, no. 3 (2018): 389–402.

The authors built curatescience.org to apply this framework in practice.

## The Four-Dimension Framework

### 1. Transparency
Can the research process be evaluated? Requires:
- Open materials (stimuli, instruments)
- Open data (raw data files)
- Open analysis code
- Ideally: preregistered design and analysis plan

Without transparency, the other three dimensions cannot be assessed.

### 2. Analytic Reproducibility
Given the same data and analysis plan, do you get the same numbers?

- Operationalized as: original results reproduced within a **10% margin** using the available data and reported method
- Sounds trivial but empirical audits show many published results cannot be reproduced from available data
- Distinct from replication (which involves new data collection)

### 3. Analytic Robustness
Do results hold under defensible alternative analytical choices?

- Also called **multiverse analysis** (Steegen et al. 2016): run all defensible alternative analytic paths and examine how stable conclusions are
- An effect that only emerges in one of many reasonable analyses is fragile; one that emerges across all is robust
- Key tool for detecting p-hacking after the fact

### 4. Effect Replicability
Does the effect appear in independent new data?

LeBel et al. provide the most granular **replication taxonomy** in the literature:

| Category | Description |
|----------|-------------|
| Exact | Identical procedure, same lab |
| Very close | Identical except for trivial differences (different RA) |
| Close (direct) | Minor procedural differences; tests the same underlying construct |
| Far | Procedural differences that test the same theoretical hypothesis |
| Very far (conceptual) | Different operationalization; tests theory not effect |

The OSC 2015 study ([[open-science-collaboration-2015]]) conducted primarily "close" replications; conceptual replications have weaker bearing on the original effect's existence.

### Application: Infidelity-Distress Study

LeBel et al. apply the framework to a specific finding — that men and women differ in jealousy response to sexual vs. emotional infidelity. They rate the finding's credibility on all four dimensions, illustrating how a finding can score high on some dimensions and low on others. The finding scores poorly on analytic robustness (the effect depends on forced-choice vs. continuous measures).

### curatescience.org

The paper introduces curatescience.org as a platform for applying this framework to published findings, crowdsourcing credibility ratings with evidence links.

## Key Entities

- [[Etienne LeBel]] — Western University (University of Western Ontario); social psychology, meta-science
- [[Wolf Vanpaemel]] — KU Leuven; mathematical psychology and Bayesian methods

## Connections to Existing Wiki

- [[Analytic Reproducibility]] concept page — directly based on this paper's second dimension
- [[open-science-collaboration-2015]] — the OSC study is primarily an assessment of effect replicability (dimension 4); LeBel's framework contextualizes what that one dimension means in a larger credibility space
- [[nosek-2018-preregistration]] — preregistration addresses transparency (dimension 1) and analytic reproducibility/robustness (dimensions 2/3)
- [[munafo-2017-manifesto]] — the manifesto proposes institutional reforms; LeBel's framework provides the measurement vocabulary
- [[bosco-2020-metabus]] — metaBUS supports dimension 2 (re-analysis from existing data) and dimension 4 (meta-analytic effect estimates)

## Key Quote

> "A finding's credibility is best understood not as a single binary attribute but as a profile across multiple dimensions that can be independently evaluated and improved."
