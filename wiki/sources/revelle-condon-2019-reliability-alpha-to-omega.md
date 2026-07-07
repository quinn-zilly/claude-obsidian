---
address: c-000999
type: source
title: "Revelle & Condon (2019) — Reliability From α to ω: A Tutorial"
authors: ["William Revelle", "David M. Condon"]
year: 2019
venue: "Psychological Assessment, 31(12), 1395–1411"
doi: "10.1037/pas0000754"
status: developing
tags:
  - source
  - psychometrics
  - reliability
  - measurement
  - methods
created: 2026-07-07
updated: 2026-07-07
related:
  - "[[Reliability]]"
  - "[[Coefficient Omega]]"
  - "[[Coefficient Alpha]]"
  - "[[William Revelle]]"
  - "[[David M. Condon]]"
---

# Revelle & Condon (2019) — Reliability From α to ω: A Tutorial

Nav: [[index]] | [[log]] | [[Coefficient Omega]]

> [!abstract] One-line
> A practitioner tutorial arguing there is **no single reliability**: the right estimate depends on what you measure, whom, where, and when — and model-based **omega** ($\omega_h$, $\omega_t$) should replace the routinely-reported **alpha**.

## Core framing

Reliability is a **variance ratio** — reliable (signal) variance over total variance — following Spearman's (1904b) decomposition $X = \tau + \epsilon$. Crucially, reliability of test scores is **not a property of the test** but a *joint function of the test and the people taking it*: increasing between-person variance (without increasing error) raises reliability. Correcting an observed correlation for [[Attenuation|attenuation]] recovers the latent correlation: $\rho_{\xi\eta} = r_{xy}/\sqrt{r_{xx}r_{yy}}$.

Reliable between-person variance is itself a mixture of **Trait + State + specific** variance (Cattell's data box: consistency across occasions = reliability, across items = homogeneity, across people = transferability). So different designs isolate different things.

## The many reliabilities

Two-occasion (test–retest) measures separate:

- **Dependability** — immediate/short retest (mostly trait + state + specific).
- **Stability** — long-delay retest (mostly trait). With ≥3 time points, SEM/path tracing can decompose trait vs state.

Single-occasion (**internal consistency**) measures borrow from **domain sampling**:

- Split-half (Spearman–Brown corrected), but not all splits are equal — the paper shows the *distribution* of all possible split halves (worst = Guttman $\lambda_1$/$\beta$; best = $\lambda_4$).
- Guttman's (1945) $\lambda_1..\lambda_6$; $\lambda_3 = $ **coefficient alpha** = KR-20 generalization.

## Two problems with α

1. **α is not an estimate of reliability** except under **tau-equivalence** (equal loadings) — a "rare" condition. Otherwise it *underestimates* total reliability but can *overestimate* the general-factor saturation.
2. **α does not measure internal consistency / unidimensionality.** It is just a function of the number of items and the average inter-item correlation; two unrelated homogeneous subtests can yield a high α.

## Model-based estimates: omega

Factor-analytic decomposition splits item variance into a **general factor (g)**, **group factors**, and **item-unique** variance. This yields:

- $\omega_h$ (**hierarchical omega**) — proportion of variance due to the **single general factor**; the meaningful "how unidimensional is my total score" index.
- $\omega_t$ (**total omega**) — total reliable (common) variance; an estimate of the **greatest lower bound (glb)**, ≈ the best split-half $\lambda_4$.
- Found via **bifactor** ($\omega_g$, tends slightly higher) or the **Schmid–Leiman** transformation ($\omega_h$). For very low general-factor saturation the EFA-based estimate is positively biased and a **CFA-based** estimate is more accurate. McDonald (1999) confusingly labeled both $\omega_t$ and $\omega_g$ as "omega."

## Ratings and categorical data

- Continuous ratings → **intraclass correlations (ICC1–ICC3)**, single- vs multiple-rater forms (Shrout & Fleiss 1979). Choice depends on whether raters are fixed/random and absolute/relative agreement is wanted.
- Categorical / nominal agreement → **Cohen's κ** (weighted κ ≡ ICC; Fleiss & Cohen 1973).

## Recommendation (Table 2 flowchart)

Ask *what/whom* before collecting data. One test / one occasion: report $\omega_h$, $\omega_t$, worst split-half. Given twice: test–retest (dependability vs stability) + variance components. Many times: multilevel reliability. Ratings: the appropriate ICC. All implemented in the R **`psych`** package (`omega`, `alpha`, `splitHalf`, `guttman`, `testRetest`, `multilevel.reliability`, `ICC`, `cohen.kappa`). The paper's stance: **report multiple estimates and explain which one matters for your inference.**

## Why it's in the vault

The primary-source upgrade behind [[Coefficient Omega]] (previously footed only on a Likert-scale review). Extends the vault's measurement/psychometrics spine and the [[Reliability]] concept; a natural companion to construct-validity material ([[Construct Validity]], [[binning-barrett-1989-validity-personnel-decisions|Binning & Barrett]]) since **reliability is a necessary but insufficient condition for validity**.
