---
type: concept
address: c-000385
title: "Effect Size Heterogeneity"
tags:
  - statistics
  - methodology
  - replication-crisis
  - meta-analysis
status: developing
created: 2026-06-03
updated: 2026-06-03
related:
  - "[[Power Analysis (Replication Studies)]]"
  - "[[Meta-Analysis]]"
  - "[[Replication Crisis]]"
  - "[[Replication Types Taxonomy]]"
  - "[[shrout-rodgers-2018-replication-crisis]]"
---

# Effect Size Heterogeneity

Effect sizes in psychology are NOT fixed population parameters — they vary systematically across persons, settings, labs, and time periods. This variation is theoretically meaningful, not mere noise, and has major implications for how replication is designed and interpreted.

## Sources of Effect Size Variation

- **Person-level**: individual differences in susceptibility, reactivity, baseline levels
- **Context-level**: lab vs. field; task demand; culture; demographic composition of sample
- **Temporal**: ego depletion effects may vary with societal norms around willpower
- **Measurement**: operationalization choices affect size of observed effects
- **Moderator variables**: theory should predict *where* effects are largest, not just whether effects exist (Van Bavel et al. 2016)

## Implications for Replication

A single failed replication may reflect:
1. The original was a false positive (QRP inflation)
2. The replication sampled from a population/context where the effect is genuinely smaller
3. Both

Without modeling heterogeneity, these two interpretations are indistinguishable from a single study.

**Key case**: Ego depletion (Hagger et al. 2016 multilab preregistered replication) — near-zero average effect but substantial between-lab variance. The theoretical question shifts from "does the effect exist?" to "what moderates it?"

## Implications for Meta-Analysis

- Random effects meta-analysis (vs. fixed effects) explicitly models heterogeneity as a parameter (τ²)
- Requires 20+ studies for stable τ² estimates (frequentist); Bayesian methods with prior work with fewer
- Moderator analysis (meta-regression) can explain systematic heterogeneity
- Important caveat: meta-analysis of a p-hacked literature summarizes biased heterogeneity (Braver et al. 2014)

## Implications for Power Analysis

Heterogeneity inflates required sample sizes for replication. Standard conditional power analysis treats effect size as fixed → systematically underpowered. See [[Power Analysis (Replication Studies)]].

## Theoretical Opportunity

Shrout & Rodgers (2018): heterogeneity is *scientifically interesting*. Psychological theory should develop predictions about where effects are maximized. Two modeling strategies:
1. **Random effects for persons × situations** (Westfall et al. 2015): crossed random effects in multilevel models
2. **Predicting effect maxima**: identify boundary conditions and moderators theoretically before testing empirically

## Cross-References

- [[Power Analysis (Replication Studies)]] — heterogeneity inflates required n
- [[Meta-Analysis]] — primary tool for characterizing heterogeneity distributions
- [[Replication Crisis]] — heterogeneity misunderstood as replication failure
- [[Replication Types Taxonomy]] — conceptual replications probe moderators of heterogeneity
- [[shrout-rodgers-2018-replication-crisis]] — primary source
