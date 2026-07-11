---
address: c-001152
type: concept
title: "Range Restriction Correction"
aliases: ["range restriction", "U ratio", "artifact distribution", "restriction of range"]
tags: [concept, psychometrics, selection, meta-analysis, validity]
status: developing
created: 2026-07-11
updated: 2026-07-11
related:
  - "[[Operational Validity (Selection)]]"
  - "[[Predictive vs Concurrent Validation]]"
  - "[[psychometric meta-analysis]]"
  - "[[Selection Bias]]"
  - "[[Criterion-Related Validity of Personality]]"
  - "[[Sackett-et-al-2022-validity-overcorrection]]"
  - "[[Recruitment MOC]]"
---

# Range Restriction Correction

Nav: [[index]] | [[concepts/_index]]

**Range restriction** = the observed validity coefficient (predictor–criterion correlation) is attenuated when the sample has a narrower range on the predictor than the applicant pool. Correcting for it estimates what validity *would* be in the full applicant population.

## The mechanics

The correction uses a **U ratio** = unrestricted SD ÷ restricted SD on the predictor. Because unrestricted (applicant-pool) SD is often unavailable, meta-analysts build an **artifact distribution** of U ratios from a subset of studies and apply its mean to the whole set. Sampling-error variance is inflated to reflect variance in U ratios (Hunter & Schmidt).

- **Direct** restriction: applicants selected *on the focal predictor x* → large effect (selection ratio .50 → restricted SD .60 → U = 1.67).
- **Indirect** restriction: selection on some other variable *z* → effect depends on the *z–x* correlation; under realistic conditions **small** (< 10% correction), and even smaller once predictor unreliability is added.

## The overcorrection problem (Sackett et al. 2022)

The routine practice violates a key assumption: the U-ratio subset (which comes almost entirely from **predictive** studies) is *not* a random draw of the full database, which is dominated by **concurrent** studies where restriction is only indirect and minimal. Applying the large predictive-study U ratio to concurrent studies **systematically overcorrects**, inflating validity by .10–.20. See [[Predictive vs Concurrent Validation]] and [[Sackett-et-al-2022-validity-overcorrection]].

**Remedy:** apply no range-restriction correction to concurrent studies absent a sound empirical basis (conservative estimation), then N-weight predictive and concurrent estimates.

## Historical roots

Pearson (1903) for range restriction; Spearman (1904) for measurement-error correction. The "textbook solution" is Hunter & Schmidt (2004).
