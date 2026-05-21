---

type: concept
address: c-000048
title: "HARKing"
tags:
  - open-science
  - research-methods
  - statistics
  - replication-crisis
status: developing
related:
  - "[[P-hacking]]"
  - "[[Publication Bias]]"
  - "[[Preregistration]]"
  - "[[Replication Crisis]]"
  - "[[munafo-2017-manifesto]]"
  - "[[nosek-2018-preregistration]]"
created: unknown
updated: unknown
---

# HARKing

**HARKing** — Hypothesizing After Results are Known — is the practice of presenting hypotheses in a published report as if they were formulated *a priori* when they were actually generated or refined *after* observing the data.

## Definition

Coined by Norbert Kerr (1998). HARKing occurs when a researcher:
1. Collects data
2. Observes the results
3. Formulates (or adjusts) hypotheses to match the observed pattern
4. Writes up the paper presenting those hypotheses as predictions made before data collection

The result appears to be a successful prediction test; in reality it is a description of patterns that have not been independently tested.

## Why HARKing is Problematic

**Statistical**: The p-value is only valid for a pre-specified hypothesis test. A hypothesis derived from the data it will be used to "test" has a p-value with no valid sampling distribution interpretation — it is guaranteed to fit the data by construction.

**Scientific**: HARKing converts exploratory pattern-finding into a false appearance of confirmatory evidence. It inflates the apparent confirmed-hypothesis count in a field without actually increasing knowledge.

**Epistemic**: Hindsight bias makes HARKing almost invisible to the researcher doing it. After seeing a result, the hypothesis *feels* like it was always the plan. This is not typically deliberate fraud but a cognitive failure.

## Relationship to P-hacking

HARKing and [[P-hacking]] often co-occur:
- P-hacking operates at the analysis stage (choosing analyses to get p < .05)
- HARKing operates at the write-up stage (reformulating the hypothesis to match the p < .05 result)

[[munafo-2017-manifesto]] identifies HARKing as a threat at the hypothesis generation stage of the research cycle (Fig. 1).

## Remedies

- [[Preregistration]]: hypotheses are timestamped before data collection, making HARKing detectable
- [[Registered Reports]]: hypotheses reviewed by journal before data collection
- Transparent disclosure of exploratory analyses: all post-hoc hypotheses clearly labeled

## CARKing

A related concept introduced in [[munafo-2017-manifesto]] Box 3: **CARKing** — Critiquing After Results are Known — where reviewers evaluate a study's methodology differently depending on whether the results are significant. Pre-registering and reviewing designs blind to results (Registered Reports) addresses CARKing at the review stage.

## See Also

- [[P-hacking]]
- [[Publication Bias]]
- [[Preregistration]]
- [[Registered Reports]]
- [[Aesthetic Standards in Science]] — [[giner-sorolla-2012-science-or-art|Giner-Sorolla (2012)]] frames HARKing as primarily an *aesthetic and presentational* pressure (narrative conformity criterion), not just a strategic incentive; the story must look clean
