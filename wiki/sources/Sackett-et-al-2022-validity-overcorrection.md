---
address: c-001142
type: source
title: "Sackett, Zhang, Berry & Lievens (2022) — Revisiting Meta-Analytic Estimates of Validity in Personnel Selection"
authors: ["Paul R. Sackett", "Charlene Zhang", "Christopher M. Berry", "Filip Lievens"]
year: 2022
venue: "Journal of Applied Psychology, 107(11), 2040–2068 (advance online 2021)"
doi: "10.1037/apl0000994"
status: developing
tags:
  - source
  - selection
  - validity
  - meta-analysis
  - range-restriction
  - personality
related:
  - "[[Range Restriction Correction]]"
  - "[[Operational Validity (Selection)]]"
  - "[[Predictive vs Concurrent Validation]]"
  - "[[Validity–Diversity Tradeoff]]"
  - "[[Criterion-Related Validity of Personality]]"
  - "[[Selection Bias]]"
  - "[[psychometric meta-analysis]]"
  - "[[Five-Factor Model]]"
  - "[[Paul R. Sackett]]"
  - "[[Charlene Zhang]]"
  - "[[Christopher M. Berry]]"
  - "[[Filip Lievens]]"
  - "[[Frank L. Schmidt]]"
  - "[[Recruitment MOC]]"
  - "[[Personality at Work MOC]]"
mocs:
  - "[[Recruitment MOC]]"
  - "[[Personality at Work MOC]]"
---

# Sackett, Zhang, Berry & Lievens (2022) — Revisiting Meta-Analytic Estimates of Validity in Personnel Selection

Nav: [[index]] | [[sources/_index]] | [[Recruitment MOC]]

> [!abstract] One-line
> The field has **systematically overcorrected for range restriction** for decades; recalibrating drops most selection-procedure validities by **.10–.20**, and **structured interviews (ρ = .42)** — not cognitive ability (ρ revised .31, down from .51) — emerge as the top-ranked predictor of job performance.

## The core argument

Meta-analytic corrections for [[Range Restriction Correction|range restriction]] typically apply a **U-ratio artifact distribution** (built from a subset of studies) to *all* studies in the meta-analysis. Sackett et al. show this rests on an assumption that is routinely violated: that the studies supplying U ratios are a random draw of the full set.

Three propositions drive the critique:

1. In **concurrent** studies (test given to incumbents), any range restriction is **indirect** — incumbents were not hired on the focal predictor.
2. The selection variable *z* used at hire is rarely highly correlated with the focal predictor *x* (highest observed inter-predictor r ≈ **.37**; cognitive-domain × noncognitive ≈ .10).
3. Indirect range restriction shrinks predictor SD only **modestly** — under realistic conditions the correction factor is **< 10%**, often much less (and even smaller once predictor unreliability is added, per Hunter et al. 2006).

Because the **vast majority of validation studies are concurrent** (e.g., 98% in Roth et al.'s work-sample meta-analysis; 95% McDaniel SJT; 76% Ones integrity; 78–85% cognitive ability), applying a large U ratio derived from the few predictive studies to the whole database produces **large overcorrection**. See [[Predictive vs Concurrent Validation]].

The authors' remedy endorses **conservative estimation**: absent a sound empirical basis, apply **no range-restriction correction** to concurrent studies rather than knowingly overcorrect. An N-weighted average of separately-corrected predictive and no-correction concurrent estimates gives revised [[Operational Validity (Selection)|operational validity]].

## Five flawed approaches to building U-ratio artifact distributions

1. **Subset of studies** ("textbook solution") — biased because U-supplying subset is predictive-only.
2. **Hiring-rate → U ratio** — assumes predictor is sole selection basis & all offers accepted; both wrong (SAT example: true U = 1.2 but hiring-rate method implies 1.54).
3. **Incumbent data pooled across jobs** (Hunter 1983 GATB) — yields workforce SD, not job-applicant SD; NAS committee skeptical.
4. **Test-publisher norm data** — needs applicant-specific norms; often only workplace norms reported.
5. **Made-up assumed distribution** (Dye et al. 1993; Huffcutt et al. 2014's 5% assumption) — no empirical basis.

## Revised validity estimates (Table 3, selected)

| Selection procedure | Schmidt & Hunter (1998) ρ | Revised ρ | B–W *d* |
|---|---|---|---|
| **Structured interviews** | .51 | **.42** | .23 |
| Job knowledge tests | .48 | .40 | .54 |
| Empirically keyed biodata | .35 | .38 | .33 |
| Work sample tests | .54 | .33 | .67 |
| **Cognitive ability (GMA)** | .51 | **.31** | .79 |
| Integrity tests | .41 | .31 | .10 |
| Assessment centers | .37 | .29 | .52 |
| Conscientiousness (overall) | .31 | .19 | −.07 |
| Unstructured interviews | .38 | .19 | .32 |

> [!note] Structured interviews now #1
> The ranking is largely preserved (procedures that ranked high still rank high) but magnitudes drop. Cognitive ability's fall from .51 → .31 is the headline reversal of the [[Frank L. Schmidt|Schmidt]] & Hunter (1998) canon.

## Validity–diversity tradeoff

The paper pairs each revised validity with a mean **Black–White subgroup difference** (Cohen's *d*, mostly from Dahlke & Sackett 2017), giving practitioners the data to weigh a [[Validity–Diversity Tradeoff]]: cognitive ability is high-validity but high-adverse-impact (*d* = .79); structured interviews and integrity tests offer better balance.

## Why it matters for the vault

This is the modern **recalibration of selection validity** — the source that dislodges the long-cited Schmidt & Hunter (1998) numbers. It directly lowers the [[Criterion-Related Validity of Personality|personality validity]] benchmarks used elsewhere in the [[Personality at Work MOC]] cluster, and reframes [[Selection Bias|range-restriction]] artifacts.
