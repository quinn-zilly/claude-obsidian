---
address: c-000758
type: source
title: "Kuncel, Klieger, Connelly & Ones (2013) — Mechanical Versus Clinical Data Combination in Selection and Admissions Decisions"
authors: ["[[Nathan R. Kuncel]]", "David M. Klieger", "Brian S. Connelly", "[[Deniz S. Ones]]"]
year: 2013
venue: "Journal of Applied Psychology, 98(6), 1060–1072"
doi: "10.1037/a0034156"
tags:
  - source
  - io-psychology
  - selection
  - meta-analysis
  - jdm
  - mechanical-vs-clinical
status: developing
created: 2026-06-30
updated: 2026-06-30
related:
  - "[[Mechanical vs Clinical Prediction]]"
  - "[[Bootstrapping (Improper Linear Models)]]"
  - "[[Lens Model]]"
  - "[[karelaia-hogarth-2008-lens-model-meta-analysis]]"
  - "[[viswesvaran-schmidt-ones-2005-general-factor-job-performance]]"
sources:
  - "[[kuncel-et-al-2013-mechanical-vs-clinical]]"
---

# Kuncel, Klieger, Connelly & Ones (2013) — Mechanical vs Clinical Data Combination

> [!abstract] One-line
> A meta-analysis (25 samples, 17 studies) showing that combining the *same* predictor data **mechanically (by formula) beats combining it holistically (by expert judgment)** for every work and academic criterion — a **>50% improvement** in predicting job performance — even when experts know the job and have *more* information than the formula.

## The setup

Two ways to combine applicant data: **mechanical** (actuarial — unit weights, optimal weights, decision trees) vs **holistic/clinical** (human judgment, insight, intuition, consensus meetings). Prior reviews (Grove & Meehl 1996; Sawyer 1966) found mechanical wins across fields, with two lessons: (1) *which* mechanical method matters less than human-vs-formula; (2) the issue is **how data are combined, not gathered** — people collect information well but combine it poorly. No prior meta-analysis had sized this gap for work/academic performance.

## Framing: the [[Lens Model]]

Kuncel et al. adopt the Brunswik Lens Model as the overarching frame for *all* selection validation. Clinical combination is degraded two ways:

- **$R_s < 1$ (low [[Judgmental Achievement and Consistency|cognitive control]])** — judges apply weights inconsistently.
- **$G < 1$** — judges don't optimally weight the cues.
- And the supposed upside, **$C$ (unmodeled/nonlinear insight), is typically ≈ 0** (citing [[karelaia-hogarth-2008-lens-model-meta-analysis|Karelaia & Hogarth 2008]]).

So inconsistency + mis-weighting aren't offset by unique clinical insight ⇒ holistic loses.

## Headline numbers (mechanical vs clinical mean validity)

| Criterion | Mechanical | Clinical |
|---|---|---|
| Job performance | .44 | .28 |
| Advancement | .42 | .36 |
| Training | .31 | .16 |
| Academic GPA | .58 | .48 |
| Academic non-grade | .47 | .46 |

- Job performance: the validity gap = a **>50% improvement** in prediction; ~**25% fewer correct hires** under holistic combination (SR = .30, Taylor–Russell).
- These are **underestimates** — no correction for range restriction or criterion unreliability (which would *widen* the gap).
- Mechanical advantage shrank but never reversed under the most stringent new-sample shrinkage estimates.

## Rebuttals to common pro-clinical arguments

- *"Jobs change, so equations go stale"* → performance dimensions are stable over time (cf. [[viswesvaran-schmidt-ones-2005-general-factor-job-performance|stable general factor]]); linear models are robust to weight changes (Dawes 1979); even then, expert subjective weights *in an equation* still beat the clinician.
- *"Small-N settings block mechanical methods"* → weight predictors from the meta-analytic literature (validity generalization) or from aggregated expert-set weights, then combine by formula.

> [!key-insight]
> The result is not "humans are useless." Humans are good at *gathering* and even *generating* cues — the failure is the *integration* step. The fix is to let experts feed cues/weights into a mechanical combiner rather than letting them do the arithmetic in their heads. This is exactly the [[Bootstrapping (Improper Linear Models)|bootstrapping]] prescription applied to selection.

## Connections

- Empirical payoff of [[karelaia-hogarth-2008-lens-model-meta-analysis|Karelaia & Hogarth (2008)]] in the selection domain; shares the [[Lens Model]] spine and the [[Bootstrapping (Improper Linear Models)|model-beats-judge]] finding.
- Shares author [[Deniz S. Ones]] with Viswesvaran et al. (2005); both use [[psychometric meta-analysis|Hunter–Schmidt psychometric meta-analysis]].
- Counters [[Highhouse 2008]]'s observation that practitioners *prefer* holistic judgment — an evidence-based-practice gap.

## Source

- Kuncel, N. R., Klieger, D. M., Connelly, B. S., & Ones, D. S. (2013). *Journal of Applied Psychology, 98*(6), 1060–1072.
