---

type: concept
address: c-000048
title: "HARKing"
tags:
  - open-science
  - research-methods
  - statistics
  - replication-crisis
  - questionable-research-practices
status: mature
related:
  - "[[P-hacking]]"
  - "[[Publication Bias]]"
  - "[[Preregistration]]"
  - "[[Replication Crisis]]"
  - "[[Norbert Kerr]]"
  - "[[kerr-1998-harking]]"
  - "[[munafo-2017-manifesto]]"
  - "[[nosek-2018-preregistration]]"
  - "[[Aesthetic Standards in Science]]"
created: unknown
updated: 2026-05-21
---

# HARKing

**HARKing** — Hypothesizing After Results are Known — is the practice of presenting hypotheses in a published report as if they were formulated *a priori* when they were actually generated or refined *after* observing the data. Coined by [[Norbert Kerr]] in [[kerr-1998-harking|Kerr (1998)]].

## Three Forms (Kerr 1998)

| Form | Description |
|------|-------------|
| **Type 1 (Classic)** | Present post-hoc hypothesis as if it was predicted before data collection |
| **Type 2 (Omission)** | Drop unsupported a priori hypotheses from the write-up; only report what "worked" |
| **Type 3 (Pirating)** | Incorporate others' unexpected findings into one's own report as one's own a priori predictions |

## Why HARKing is Problematic

**Statistical**: The p-value is only valid for a pre-specified hypothesis test. A hypothesis derived from the data it will "test" has no valid null distribution — it is guaranteed to fit the data by construction. Type I error rates inflate well above nominal α; effect sizes are systematically overestimated.

**Scientific**: HARKing converts exploratory pattern-finding into false confirmatory evidence. Theories accumulate support they have not earned. Type 2 HARKing hides failures, letting weak theories persist.

**Epistemic**: Hindsight bias makes HARKing cognitively invisible. After seeing a result, the hypothesis *feels* like it was always the plan. This is usually not deliberate fraud — it is a cognitive failure, which makes it especially hard to address through ethics appeals alone.

## Mechanisms That Enable HARKing

- **Hindsight bias**: Post-hoc hypotheses feel a priori after the fact
- **Hypothetico-deductive norm**: Science *should* look hypothesis-driven, creating pressure to conform
- **Publication bias**: Confirmatory results are more publishable; HARKing manufactures confirmation
- **No audit trail**: Reviewers cannot see what hypotheses were originally specified; there is no timestamp

## Relationship to Other QRPs

HARKing and [[P-hacking]] often co-occur:
- P-hacking operates at the **analysis stage** (choosing analyses to get p < .05)
- HARKing operates at the **write-up stage** (reformulating the hypothesis to match the significant result)

[[munafo-2017-manifesto]] places HARKing as a threat at the hypothesis generation stage of the research cycle (Fig. 1), showing it interacts with all downstream threats.

## Remedies

- [[Preregistration]]: hypotheses timestamped before data collection, making HARKing detectable
- [[Registered Reports]]: hypotheses reviewed by journal *before* data collection; publication committed regardless of result (strongest form)
- Transparent reporting: all post-hoc hypotheses clearly labeled as exploratory
- Replication norm: confirmatory evidence requires independent replication

## CARKing

A related concept introduced in [[munafo-2017-manifesto]] Box 3: **CARKing** — Critiquing After Results are Known — where reviewers evaluate a study's methodology differently based on whether results are significant. Registered Reports (blind review before results) address CARKing.

## Cross-Domain Connections

- **[[Aesthetic Standards in Science]]**: [[giner-sorolla-2012-science-or-art|Giner-Sorolla (2012)]] frames HARKing as primarily an *aesthetic and presentational* pressure (narrative conformity criterion) rather than pure strategic incentive — the story must look clean and theoretically motivated. Researchers may not consciously choose to HARK; they are conforming to genre expectations.
- **[[Motivated Reasoning]]**: HARKing is the write-up expression of the same "ordinary psychology under misaligned incentives" that [[nosek-2012-scientific-utopia-ii|Nosek et al. (2012)]] diagnose as [[Conflict of Interest in Science]]. Both are non-malicious but structurally distorting.
- **[[Publication Bottleneck]]**: [[giner-sorolla-2012-science-or-art|Giner-Sorolla (2012)]] argues HARKing is downstream of the bottleneck — if there were room to publish exploratory findings, the pressure to dress them up as confirmatory would diminish.

## See Also

- [[kerr-1998-harking]] — origin paper
- [[shrout-rodgers-2018-replication-crisis]] — reviewed HARKing as central QRP; framing: conflates exploratory/confirmatory, violates NHST assumptions
- [[Norbert Kerr]] — author
- [[P-hacking]]
- [[Publication Bias]]
- [[Preregistration]]
- [[Registered Reports]]
- [[Replication Crisis]]
- [[Aesthetic Standards in Science]]
- [[Motivated Reasoning]]
- [[Publication Bottleneck]]
