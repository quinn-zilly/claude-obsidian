---
type: concept
address: c-000384
title: "Power Analysis (Replication Studies)"
aliases:
  - Replication Power Analysis
  - Predictive Power Analysis
tags:
  - statistics
  - methodology
  - replication-crisis
  - effect-size
status: developing
created: 2026-06-03
updated: 2026-06-03
related:
  - "[[Replication Crisis]]"
  - "[[Effect Size Heterogeneity]]"
  - "[[Publication Bias]]"
  - "[[Meta-Analysis]]"
  - "[[Bayesian Statistics in Psychology]]"
  - "[[shrout-rodgers-2018-replication-crisis]]"
---

# Power Analysis (Replication Studies)

Standard power analysis for replication studies is systematically flawed. Shrout & Rodgers (2018) and Maxwell et al. (2015) show the OSC studies averaged 0.92 computed power — yet only 36% replicated. The problem: power was calculated from the original inflated effect sizes, not the true population effect.

## Three Layers of Inadequacy

### 1. Conditional Power Analysis (Standard Practice)
Treats the original reported effect size as a known fixed quantity. This is almost always wrong because:
- Original effect sizes are inflated by **publication bias** (lucky samples get published)
- Original effect sizes are inflated by **sampling variation** (especially in small-n studies)
- The nonlinearity of the power-n relationship means small effect size errors compound dramatically

### 2. Effect Size Nonlinearity
The sample-size requirement is highly nonlinear at small effect sizes (Cohen's d):
- d=0.8→0.7: need 26 more total participants (for 95% power)
- d=0.4→0.3: need 252 more participants
- d=0.3→0.2: need thousands more participants

Taking the midpoint of a plausible effect size range systematically underpowers because of this nonlinearity. Shrout & Rodgers recommend using the **lower bound of the confidence interval** on the effect size.

### 3. Effect Size Heterogeneity Ignored
Even a "true" effect size varies across labs, samples, and contexts (see [[Effect Size Heterogeneity]]). A power analysis that ignores this variance will be underpowered on average. McShane & Böckenholt (2014): when heterogeneity is taken into account, required n is often *considerably* larger.

## Corrected Approaches

- **Safeguard power** (Perugini et al. 2014): power based on lower CI bound of effect size
- **Predictive power** (Anderson & Maxwell 2017; McShane & Böckenholt 2014): integrates over distribution of possible effect sizes
- **Bayesian predictive power**: uses prior distribution (e.g., original study's posterior) to compute expected power — natural fit for replication context
- **Equivalence testing**: to claim no effect, need n of 1,000–10,000 per group (Maxwell et al. 2015)

## Implications for Replication Design

Maxwell et al. (2015) key recommendation: **stop treating replication as a binary pass/fail from a single study**. Instead:
- Run multiple replications
- Pool data across replications via meta-analysis
- Estimate effect size *distributions*, not point estimates
- Focus on characterizing moderators of effect size variation

## Cross-References

- [[Effect Size Heterogeneity]] — variance ignored by standard power analysis
- [[Publication Bias]] — inflates effect sizes used in power calculations
- [[Meta-Analysis]] — the preferred alternative to single-study replication decisions
- [[Bayesian Statistics in Psychology]] — predictive power estimation
- [[Replication Crisis]] — underpowered studies as root cause
- [[shrout-rodgers-2018-replication-crisis]] — primary source
