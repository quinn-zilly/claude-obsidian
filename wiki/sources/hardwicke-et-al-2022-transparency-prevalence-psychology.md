---
type: source
address: c-000661
title: "Estimating the Prevalence of Transparency and Reproducibility-Related Research Practices in Psychology (2014–2017)"
author:
  - "[[Tom Hardwicke]]"
  - "[[Robert T. Thibault]]"
  - "[[Jessica E. Kosie]]"
  - "[[Joshua D. Wallach]]"
  - "[[Mallory C. Kidwell]]"
  - "[[John Ioannidis]]"
year: 2022
venue: "Perspectives on Psychological Science"
volume: 17
pages: "239-251"
doi: "10.1177/1745691620979806"
tags:
  - open-science
  - reproducibility
  - transparency
  - meta-science
  - psychology
  - prevalence-study
status: ingested
ingested: 2026-06-09
related:
  - "[[Transparency & Reproducibility Indicators]]"
  - "[[Meta-Research]]"
  - "[[Open Science]]"
  - "[[Open Access]]"
  - "[[Preregistration]]"
  - "[[Replication]]"
  - "[[Replication Crisis]]"
  - "[[Questionable Research Practices]]"
  - "[[Open Science Framework]]"
  - "[[Conflict of Interest in Science]]"
  - "[[Meta-Analysis]]"
  - "[[open-science-collaboration-2015]]"
  - "[[simmons-et-al-2011-false-positive-psychology]]"
  - "[[thibault-2023-open-science-2-0]]"
  - "[[Open Science MOC]]"
sources:
  - "[[hardwicke-et-al-2022-transparency-prevalence-psychology]]"
created: 2026-06-09
updated: 2026-06-09
---

# Hardwicke et al. (2022) — Prevalence of Transparency & Reproducibility Practices in Psychology

> [!key-insight] Core Finding
> In a random sample of 250 psychology articles (2014–2017), open-access availability was common (65%), but the substrate of reproducible science was nearly absent: protocols 0%, raw data 2%, analysis scripts 1%, materials 14%, preregistration 3%. Reform initiatives had **not yet** reached routine practice. The numbers are a deliberate **baseline** for tracking future change.

## Bibliographic Details

Hardwicke TE, Thibault RT, Kosie JE, Wallach JD, Kidwell MC, Ioannidis JPA. "Estimating the Prevalence of Transparency and Reproducibility-Related Research Practices in Psychology (2014–2017)." *Perspectives on Psychological Science* 17(1): 239–251 (2021/2022). Open Access (CC BY). DOI: [10.1177/1745691620979806](https://doi.org/10.1177/1745691620979806).

Preregistered ([osf.io/q96eh](https://osf.io/q96eh)); all data, materials, and scripts shared on OSF; manuscript built as a reproducible Code Ocean container. The study practices what it measures.

## Design

Retrospective observational, cross-sectional. Sampling unit = article. 250 articles drawn by random-number generator from 224,556 Scopus documents (ASJC psychology codes 3200–3207, document type "article"/"review", 2014–2017, 1,323 journals). 228 were English-language and accessible → eligible for in-depth extraction. Manual coding by three investigators + double-coding for reliability; coding differences resolved by discussion. Indicators modeled on prior biomedicine (Iqbal 2016; Wallach 2018) and social-science (Hardwicke, Wallach et al. 2020) sweeps.

## Prevalence Results

Denominators differ per indicator (applicability depends on study design). CIs are Sison-Glaz multinomial 95%.

| Indicator | Prevalence | Count | 95% CI |
|---|---|---|---|
| Public availability (open access) | 65% | 154/237 | 59–71% |
| Paywall-only | 31% | 74/237 | 25–38% |
| Materials availability statement | 14% | 26/183 | 10–19% |
| Protocol availability | 0% | 0/188 | 0–1% |
| Raw data availability | 2% | 4/188 | 1–4% |
| Analysis-script availability | 1% | 1/188 | 0–1% |
| Preregistration | 3% | 5/188 | 1–5% |
| Funding disclosure statement | 62% | 142/228 | 56–69% |
| Conflict-of-interest statement | 39% | 88/228 | 32–45% |
| Claimed replication study | 5% | 10/188 | 3–8% |
| Included in systematic review | 11% | 21/183 | 8–16% |
| Included in meta-analysis | 7% | 12/183 | 4–10% |

## Notable Detail

- **Link-rot is real.** Of 26 articles claiming available materials, 7 were inaccessible (broken links). Reporting ≠ availability.
- **Disclosure ≠ rare** because journals mandate it. Funding (62%) and COI (39%) statements beat every sharing practice — likely because journals require them, not because of open-science norms.
- **Protocols = 0%.** Authors note psychology may lack a separate-protocol norm (unlike biomedicine), so the protocol variable may be less meaningful here — retained for cross-discipline comparison.
- **COI under-disclosure.** Of 88 COI statements, 86% reported none; only 12 reported ≥1 conflict.

## Cross-Discipline Comparison

| Indicator | Psychology | Social sciences | Biomedicine |
|---|---|---|---|
| Open access | 65% | 40% | 25% |
| Materials | 14% | 11% | 33% |
| Funding disclosure | 62% | 31% | 69% |
| COI disclosure | 39% | 15% | 65% |
| Claimed replication | 5% | 1% | 5% |

Psychology leads on open access, trails biomedicine on COI/funding disclosure. Social sciences lowest on disclosure (less journal mandating).

## Limitations

Random sample of 250 → no per-subfield/per-journal generalization. Adoption ≠ sufficiency (poorly documented data still blocks reproducibility; weak preregistrations don't constrain degrees of freedom). Published info only — no author data requests (those typically fail; Vanpaemel 2015 couldn't get 62% of 394 requested datasets). Time-lag may undercount replications, meta-analyses, and preregistrations. Snapshot of one window; post-period reforms (e.g. SIPS founding) invisible.

## Why It Matters

This is a **meta-research baseline map**. Reform efficacy can only be judged against a known prior; Hardwicke et al. supply the prior for psychology. Companion to the social-science sweep (Hardwicke, Wallach et al. 2020) and biomedicine sweeps (Wallach 2018; Iqbal 2016). See [[Transparency & Reproducibility Indicators]] for the indicator framework and [[Meta-Research]] for the genre.

## Related Reading

- [[open-science-collaboration-2015|Reproducibility Project: Psychology (OSC 2015)]] — the replication-failure shock this baseline contextualizes.
- [[simmons-et-al-2011-false-positive-psychology|False-Positive Psychology]] — the QRP/[[Researcher Degrees of Freedom]] case that motivated reform.
- [[thibault-2023-open-science-2-0|Open Science 2.0]] — Thibault's later "openness necessary but not sufficient" thesis; this paper is the empirical floor it builds on.
