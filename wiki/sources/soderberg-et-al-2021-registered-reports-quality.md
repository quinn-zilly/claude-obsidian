---
address: c-000667
type: source
title: "Initial Evidence of Research Quality of Registered Reports Compared with the Standard Publishing Model (Soderberg et al. 2021)"
authors:
  - "[[Courtney K. Soderberg]]"
  - "[[Timothy M. Errington]]"
  - "[[Sarah R. Schiavone]]"
  - "[[Julia Bottesini]]"
  - "[[Felix Singleton Thorn]]"
  - "[[Simine Vazire]]"
  - "[[Kevin M. Esterling]]"
  - "[[Brian Nosek]]"
year: 2021
venue: "Nature Human Behaviour 5: 990–997"
doi: "10.1038/s41562-021-01142-4"
tags:
  - open-science
  - registered-reports
  - peer-review
  - publication-reform
  - meta-science
status: developing
related:
  - "[[Registered Reports]]"
  - "[[Publication Bias]]"
  - "[[Preregistration]]"
  - "[[In-Principle Acceptance]]"
  - "[[Statcheck]]"
  - "[[Center for Open Science]]"
  - "[[Open Science MOC]]"
created: 2026-06-09
updated: 2026-06-09
---

# Initial Evidence of Research Quality of Registered Reports

> [!abstract] One-line
> 353 researchers blind-ish peer-reviewed 29 published Registered Reports against 57 matched standard-model papers from psychology/neuroscience; RRs scored higher on all 19 quality criteria — biggest on methods/analysis rigour — with **no cost** to novelty, creativity, or importance.

## Citation

Soderberg, C. K., Errington, T. M., Schiavone, S. R., Bottesini, J., Singleton Thorn, F., Vazire, S., Esterling, K. M., & Nosek, B. A. (2021). Initial evidence of research quality of registered reports compared with the standard publishing model. *Nature Human Behaviour*, 5, 990–997. [[Center for Open Science]] et al.

## Design

- **Naturalistic quasi-experiment** (no randomization — authors self-select into RRs).
- 29 RRs (psychology + neuroscience, novel research; replication RRs *excluded* because replications are rare in the standard model and couldn't be matched). Published 2014–2018 across 102 journals offering RRs.
- 57 matched comparison papers via two preregistered matching schemes: (1) same journal + date, (2) same lead author + date.
- 353 peer reviewers (4.5% response from 7,835 invites) each rated one RR + one matched control on **19 criteria** (−4…+4 scale), in fixed order: methods → results → abstract, to isolate method evaluation from results.
- Papers lightly redacted to remove the words "Registered Report" (full blinding judged infeasible without removing rigour-relevant content). 54% of reviewers still correctly guessed RR status.
- Bayesian multilevel models, partial pooling across outcomes; within- and between-subjects estimates.

## Key Findings

| Outcome | RR advantage (raw, −4…+4) | 95% CrI |
|---|---|---|
| Methods rigour | 0.99 | [0.62, 1.35] |
| Analysis rigour | 0.96 | [0.60, 1.34] |
| Overall paper quality | 0.66 | [0.30, 1.02] |
| **Mean across all 19** | **0.46** | range 0.13–0.96 |
| Novelty of question | 0.13 | [−0.24, 0.49] (indistinguishable) |
| Creativity of methods | 0.22 | [−0.14, 0.58] (indistinguishable) |

- RRs **numerically outperformed on all 19 criteria**; standard model never numerically beat RRs on any.
- Advantage was largest exactly where it should be — methodology & analysis rigour, the things pre-results review targets.
- Advantage held within- and between-subjects, across reviewer familiarity levels, and even among reviewers who believed RRs were neutral/negative in general, and among those who *failed* to guess RR status (weaker but directionally intact).

### Objective coding (statcheck + features)

- **Open data**: 86% of RRs vs 14–18% of comparisons. **Open materials**: 59% vs 7–11%. **Preregistration**: 59% vs 0–7%.
- [[Statcheck]] reporting errors were rare and similar across groups.
- RRs had larger median sample sizes and far more sample-size justifications.
- Only 59% of RRs had a *findable* independent preregistration — flagged as a documentation gap to improve.

## Why It Matters

- Directly answers the skeptics' fear (Baumeister; Cropley) that RR planning kills novelty/creativity: **no support** for that cost.
- Confirms RRs realign incentives away from "novel, positive, clean" toward rigorous questions — addressing the very [[Publication Bias]] that [[fanelli-2012-negative-results-disappearing|Fanelli (2012)]] documented (cited here as ref 6).
- Speculated mechanism: (1) authors design harder to win [[In-Principle Acceptance]]; (2) reviewers judge methods undistracted by results; (3) review can improve the study *before* it runs.

> [!key-insight]
> "RRs are not a panacea, but the evidence suggests clear and tangible benefits." The quality gains came *with* the publication-bias reduction shown elsewhere (Scheel et al.; Allen & Mehler), not at the expense of discovery.

## Limitations (author-stated)

- Naturalistic: no random assignment of papers to RR/non-RR; authors & journals self-select. Matching reduces but cannot remove confounding.
- Early-adoption effects (the format is new) may not generalize to mature RR practice.
- Quality measured by *peer perception*, not replicability/generalizability of findings — a harder, still-needed test.
- 4.5% reviewer response; representativeness unknown.

## Connections

- The reform-side bookend to [[fanelli-2012-negative-results-disappearing|Fanelli (2012)]]: Fanelli diagnoses the disease (vanishing negatives); Soderberg evaluates the cure (RRs) and finds it works without the feared side effects.
- Operationalizes [[Registered Reports]] / [[In-Principle Acceptance]] and uses [[Statcheck]].
- From the [[Center for Open Science]] ([[Brian Nosek]], [[Timothy M. Errington]]); [[Simine Vazire]] on coding.

## See Also

- [[Registered Reports]]
- [[In-Principle Acceptance]]
- [[Publication Bias]]
- [[fanelli-2012-negative-results-disappearing]]
- [[Open Science MOC]]
