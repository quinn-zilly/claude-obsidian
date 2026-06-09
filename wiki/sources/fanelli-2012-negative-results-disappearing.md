---
address: c-000666
type: source
title: "Negative Results Are Disappearing from Most Disciplines and Countries (Fanelli 2012)"
authors:
  - "[[Daniele Fanelli]]"
year: 2012
venue: "Scientometrics 90(3): 891–904"
doi: "10.1007/s11192-011-0494-7"
tags:
  - open-science
  - publication-bias
  - meta-science
  - replication-crisis
  - bibliometrics
status: developing
related:
  - "[[Publication Bias]]"
  - "[[Positive-Outcome Bias]]"
  - "[[File-Drawer Problem]]"
  - "[[Publish or Perish]]"
  - "[[Questionable Research Practices]]"
  - "[[Open Science MOC]]"
created: 2026-06-09
updated: 2026-06-09
---

# Negative Results Are Disappearing from Most Disciplines and Countries

> [!abstract] One-line
> By coding 4,656 hypothesis-testing papers (1990–2007), Fanelli shows the share reporting a *positive* result rose by ~22%, providing the first direct evidence that negative results are vanishing from the published literature across most fields and countries.

## Citation

Fanelli, D. (2012). Negative results are disappearing from most disciplines and countries. *Scientometrics*, 90(3), 891–904. [[Daniele Fanelli]], University of Edinburgh.

## Design

- **Sample**: 4,656 papers that declared they "tested the hypothes*", drawn at random from the ISI Essential Science Indicators database (10,837 journals, 20 disciplines). High-impact multidisciplinary journals (*Science*, *Nature*, *PNAS*) excluded.
- **Coding**: For each paper, read abstract / full text and code whether the authors concluded *positive* (full or partial support) or *negative* (null or contrary). Only the first hypothesis counted when multiple were tested.
- **Blinding**: Coding was blind to year and country (retrieved only after coding) — so those trends can't be a coding artefact.
- **Model**: Logistic regression on year + discipline + country + domain + applied/pure + single/multiple-hypothesis.

## Key Findings

| Finding | Value |
|---|---|
| Positive results, 1990–91 | 70.2% |
| Peak (2005) | 88.6% |
| 2007 | 85.9% |
| Per-year increase in odds of a positive result | ~6%/year (highly significant) |
| Overall growth 1990→2007 | >22% |

- The trend survived controlling for **all** confounds (≈5%/year in the maximal model).
- **Discipline gradient**: positive-result frequency rises physical → biological → social sciences, and applied > pure — confirming Fanelli's earlier ["hierarchy of the sciences"](#) finding ([[Positive-Outcome Bias]]). Steepest growth in Economics & Business, Clinical Medicine, Psychology/Psychiatry, Pharmacology & Toxicology. Space Science was the *only* discipline with a (slight) decline.
- **Country gradient**: US published *fewer* positives than Asian countries (esp. Japan) but *more* than Europe (esp. UK). An editorial bias story can't explain US > UK (both rich, English-speaking), suggesting stronger US bias against negatives — consistent with US having more data-manipulation retractions (Steen 2011).

## Why It Matters

Three candidate explanations; only #3 fits the data:

1. Hypotheses are increasingly likely to be *true* — i.e. researchers chase safe, confirmable questions (still a distortion).
2. Statistical power rose — *unsupported*; power is low everywhere and not growing.
3. Negative results are submitted/accepted less, or converted to positives via [[Questionable Research Practices|post-hoc reinterpretation, selection, p-hacking, fabrication]]. ← best fit.

Missing negatives inflate meta-analytic effect sizes, waste resources replicating failures, and can spawn entire fields built on non-existent phenomena (Ioannidis). The distortion is worst exactly where theory/method are loose and replication is rare — the soft sciences.

> [!key-insight]
> The strongest growth in positive results came in fields (Clinical Medicine, Pharmacology, Molecular Biology) where publication-bias *remedies* (trial registration, reporting guidelines, negative-results journals) had the longest history. Fanelli reads this as evidence those early initiatives had **not** worked — and the problem was worsening. This is the empirical baseline that the [[Registered Reports]] reform later sought to fix.

## Limitations (author-stated)

- Single database (ESI/ISI), which over-represents US journals and grows slower than the literature.
- All coding by one author (inter-rater spot-check: 18/20 agreement with an untrained assistant).
- Cannot fully separate "written-up differently" from "genuinely fewer negatives," though the lightest write-up-only scenario was not supported.

## Connections

- Provides the problem [[Registered Reports]] and [[Preregistration]] are designed to solve; cited as ref 6 in [[soderberg-et-al-2021-registered-reports-quality]].
- Mechanism-level companion to [[File-Drawer Problem]] and [[Publication Bias]].
- Driven by [[Publish or Perish]] competition and [[Questionable Research Practices]].
- Part of the empirical case behind the [[Replication Crisis]].

## See Also

- [[Positive-Outcome Bias]]
- [[Publication Bias]]
- [[soderberg-et-al-2021-registered-reports-quality]]
- [[Open Science MOC]]
