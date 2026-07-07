---
type: source
address: c-000934
title: "Obloj & Zenger (2022): The influence of pay transparency on (gender) inequity, inequality and the performance basis of pay"
authors: ["Tomasz Obloj", "Todd Zenger"]
year: 2022
venue: "Nature Human Behaviour"
citation: "Obloj, T., & Zenger, T. (2022). The influence of pay transparency on (gender) inequity, inequality and the performance basis of pay. Nature Human Behaviour, 6(5), 646–655."
doi: "10.1038/s41562-022-01288-9"
tags: [source, compensation, pay-transparency, gender-pay-gap, pay-equity, pay-dispersion, pay-for-performance, natural-experiment]
status: developing
created: 2026-07-06
updated: 2026-07-06
related:
  - "[[Pay Transparency]]"
  - "[[Performance Basis of Pay]]"
  - "[[Pay Dispersion]]"
  - "[[Pay-for-Performance]]"
  - "[[Gender Gap in Rewards vs Performance]]"
  - "[[Distributive Justice]]"
  - "[[Tomasz Obloj]]"
  - "[[Todd Zenger]]"
---

# Obloj & Zenger (2022): Pay Transparency on Equity, Equality & the Performance Basis of Pay

> [!abstract] One-line
> A staggered natural experiment on ~100,000 US academics (1997–2017) showing pay transparency causally **raises pay equity and equality** but **weakens the link between pay and individual performance** — the first empirical test of transparency's *systemic* effect on all three attributes of pay at once.

## The question

Prior work studied transparency's effect on single dimensions (mostly pay *equality*/compression: Mas 2017; Baker et al.; Cullen & Pakzad-Hurson). But equity, equality, and pay-for-performance are interrelated. This paper asks how transparency reshapes an organization's **whole** pay practice: the performance-conditioned gender pay gap (**pay equity** — fairness/consistency of pay-to-performance matching), wage dispersion ([[Pay Dispersion|equality]]), and the **[[Performance Basis of Pay]]**.

## Design & data

- **Setting:** US public-university academics — a rare context where individual productivity (publications, books, grants, patents, awards) and rank are observable, enabling estimation of *both* discriminatory and non-discriminatory wage differentials.
- **Data:** Academic Analytics productivity data merged (name-matching) with FOIA/Sunshine-law salary histories. Final merged panel: **676,055 individual–year observations; 97,839 individuals; 139 institutions; 8 states** (CA, CT, FL, NY, PA, TX, VA, WV), 1997–2017. Gender coded dichotomously from first names.
- **Identification:** staggered shocks to salary accessibility — public-salary **websites** appearing state-by-state (after FOIA/Sunshine laws already in place). OLS with individual + institution + year + field fixed effects; dynamic difference-in-differences; robustness via stacked DiD, IV (2SLS instrumenting a covariate with a one-year lead), dropping earliest-treated states, and unconstrained lead/lag models to address pre-trends.

## Three headline findings

### 1. Equity ↑ — the conditional gender pay gap shrinks

- Pre-transparency conditional gap (controls for rank + productivity) ≈ **7.7% (2010)**, narrowing to **2.6% by 2017**.
- Transparency shocks close the conditional gap by an estimated **2–5.9 percentage points** (comparable to Baker et al.'s ~2pp Canadian estimate).
- Kernel-density plots: pre-shock, women are more likely underpaid and less likely overpaid vs. market wage; post-shock the male/female residual distributions become substantially more aligned.
- Broader equity: variance in market-wage residuals within institution–field fell **~11%** — pay became more *consistently* matched to productivity/rank.

### 2. Equality ↑ — wage dispersion compresses ~20%

- Transparency reduced within-department [[Pay Dispersion|pay variance]] by **nearly 20%** (Table 2: treatment on ln-wage variance β = −0.065, p<.001).
- Compression comes from shrinking *both* positive and negative residuals — pay simply becomes more equal, with institution/department affiliation predicting a larger share of pay.

### 3. Performance basis of pay ↓ — the discussed-less consequence

- Marginal returns to observable performance **weaken substantially** after transparency. For a star academic (95th percentile across metrics), the performance premium drops **~42%**.
- Marginal returns to rank advancement also fall discretely at the shock (e.g., promotion-to-associate premium 14.5%→8.7%; promotion-to-full 31.9%→25.2%).
- Pattern holds across all disciplines (awards the sole exception, always ~nil). Publications, books, grants all see weakened sensitivity.

## Mechanisms (three explored)

1. **Pressure to weaken pay-for-performance** — direct: σ coefficients on productivity×treatment are negative.
2. **Targeted remediation** — institutions raise the pay of the most *underpaid* (by equity **and** equality). Post-transparency, underpaid academics' raises rise 3.8%→4.3%; overpaid unchanged. Attention to both fairness and compression.
3. **Mobility** — the underpaid may exit, leaving a more equal/equitable remainder. Rerunning on the **non-mobile** workforce keeps results (slightly smaller magnitudes) → mobility contributes but does not drive the effects.

## The trade-off framing

> [!key-insight] The core tension
> Transparency delivers what advocates want (more equity, less inequality) but at a cost advocates rarely discuss: a **weaker performance basis of pay**. One way an org gets *both* more equal and more equitable pay is to make pay more precisely *and* more weakly linked to individual performance. Policymakers must weigh how much they value equity/equality vs. pay-for-performance incentives.

Mechanism for *why* transparency pressures allocators: humans **socially compare**; revealed inequity/inequality triggers envy/injustice → turnover, reduced effort, politicking → pressure on employers to equalize. (Consistent with [[Distributive Justice]] and social-comparison accounts.)

## Scope & limitations

- Academia has unusually **observable** individual performance; authors argue effects should be *stronger* where performance is less visible (per Cullen & Pakzad-Hurson theory) — but generalization is the key limitation.
- Gender coded dichotomously from names (no full gender-identity spectrum).
- Equity operationalized as deviation from a productivity-predicted "market wage"; discrimination upstream in hiring/promotion/task-allocation is invisible to this measure.
- Notes that firms/policymakers often prefer *partial* transparency (ranges by rank, group aggregates) that may raise fairness while preserving pay-for-performance — an untested alternative.

## Why it matters here

Upgrades [[Pay Transparency]] from a review-cited claim (the note previously cited "Obloj & Zenger 2017") to a large-N causal primary source. Provides the **[[Performance Basis of Pay]]** concept and a concrete equity/equality/PFP trade-off. Companion to [[shaw-2014-pay-dispersion|Shaw (2014)]] (dispersion) and [[joshi-son-roh-2015-women-close-the-gap|Joshi et al. (2015)]] (gender rewards gap) — Obloj shows transparency is one lever that *moves* both.
