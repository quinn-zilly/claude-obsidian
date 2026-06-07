---
type: source
address: c-000381
title: "Psychology, Science, and Knowledge Construction: Broadening Perspectives from the Replication Crisis"
authors:
  - Patrick E. Shrout
  - Joseph L. Rodgers
year: 2018
journal: Annual Review of Psychology
volume: 69
pages: 487–510
doi: 10.1146/annurev-psych-122216-011845
tags:
  - replication-crisis
  - methodology
  - open-science
  - statistics
  - psychology
status: ingested
created: 2026-06-03
updated: 2026-06-03
---

# Shrout & Rodgers (2018) — Psychology, Science, and Knowledge Construction

Annual Review of Psychology review article covering the replication crisis in psychology: causes, statistical responses, and constructive reforms.

## Core Argument

The "replication crisis" is partly real (QRPs inflate false-positive rates) and partly artifact of statistical misunderstanding (36% replication rate is not surprising given underpowered studies and effect size heterogeneity). The response should be methodological reform, not panic. Open science and preregistration are the most important outcomes.

## Nine Questions Framework

The paper works through nine questions:
1. Why do people say there is a crisis?
2. How did scientific conventions evolve?
3. What are the specific problems with scientific practices?
4. What procedural steps address these problems?
5. How can statistical theory help?
6. How can psychological theory inform effect size variation?
7. How can replicable findings become more common?
8. Do new norms cause collateral damage?
9. What is the take-home message?

## Why the Crisis? Three Sets of Events

1. **Scientific fraud** — Diederik Stapel, Marc Hauser, Lawrence Sanna
2. **QRP critiques** — Ioannidis (2005), Kerr (1998, HARKing), Simmons et al. (2011)
3. **Open Science Collaboration (2015)** — replicated 100 findings; only 36% significant; effect sizes ~half original; social > cognitive replication failures

## Historical Origins: Fisher, Neyman-Pearson, NHST

- Wilhelm Wundt (1879): psychology as scientific method
- Mill (1843): method of differences as basis for experiment
- Fisher (1925): randomization to equate groups probabilistically; α=0.05 as a flexible guideline, not a universal standard
- Neyman & Pearson (1928, 1933): combined with Fisher → NHST
- Fisher's original concern was NOT whether results replicate — replication was a mechanism to equate groups

## Questionable Research Practices (QRPs)

See [[Questionable Research Practices|Questionable Research Practices (QRPs)]] for full taxonomy. Key types:
- **HARKing** (Kerr 1998): Hypothesizing After Results are Known — conflates exploratory/confirmatory; see [[HARKing]]
- **p-hacking** (Simmons et al. 2011): multiple DVs, optional stopping, covariate fishing, dropping groups
- **fMRI double-dipping** (Vul et al. 2009): circular analysis inflating brain-behavior correlations
- **Statistical errors** (Bakker & Wicherts 2011): 18% of articles had errors; nearly all made results *more* significant

## Practical Reforms

- **Preregistration + OSF** (Nosek 2013): most important outcome of the crisis; separates confirmatory from exploratory
- **Open Science Framework**: (a) preregister hypotheses, (b) preregister design/sample size, (c) open data and analysis syntax
- **Badges** (Psychological Science, Kidwell et al. 2016): acknowledge preregistration, open materials, open data
- **Increased sample sizes**: ~90 per group recommended (Vazire 2016)
- **Registered Reports**: in-principle acceptance before results known

## Statistical Responses

### Power Analysis for Replication
- OSC studies averaged 0.92 power — but calculated from *original* (likely inflated) effect sizes
- Correct power analysis accounts for **effect size uncertainty** (Maxwell et al. 2015) and **heterogeneity** (McShane & Böckenholt 2014)
- Sample sizes for meaningful equivalence tests: 1,000–10,000 per group
- Recommendation: move from single replications to **multiple studies estimating effect distributions**
- See [[Power Analysis (Replication Studies)]]

### Meta-Analysis
- Meta-analysis handles variation across studies naturally; Schmidt & Oh (2016)
- Random effects models require 20+ studies for stable variance estimates
- Must guard against summarizing p-hacked literatures (Braver et al. 2014)
- Integrative data analysis / individual patient data meta-analysis useful when few replications available

### Bayesian Analysis
- More natural scientific formulation: P(hypothesis | data) vs. P(data | null)
- Bayes factors for quantifying replication evidence (Verhagen & Wagenmakers 2014)
- Bayesian estimation preferred over NHST for continuous effect characterization
- Works with smaller N when prior specified; prior from original study is natural choice

### Resampling Methods
- Bootstrapping for CI estimation without distributional assumptions
- Permutation tests as exact frequentist alternatives
- Particularly useful when effect size distributions unknown

## Psychological Theory and Effect Size Variation

Key insight: effect sizes are NOT fixed population parameters — they vary systematically by person, context, and setting. This variation is theoretically interesting, not a problem.

- **Moderator modeling**: random effects for persons and situations (Westfall et al. 2015); contextual sensitivity (Van Bavel et al. 2016)
- **Predicting effect size maxima**: theory should predict where effects are largest, not just whether effects exist
- **Developmental and clinical**: effect sizes vary by age, disorder severity, treatment context
- **Ego depletion example**: multilab preregistered replication (Hagger et al. 2016) showed near-zero average effect but substantial between-lab variation → theoretical question about moderators

## Broader Solutions

1. **Replication types**: direct/exact → systematic → conceptual (a continuum); all informative; see [[Replication Types Taxonomy]]
2. **Multiple replications over single**: estimate effect distributions rather than binary pass/fail
3. **Coordinated replications**: Many Labs project (Klein et al. 2014); pipeline project (Schweinsberg et al. 2016)
4. **Broadened scope**: clinical, applied, and health psychology also affected (Tackett et al. 2017)
5. **Publication reform**: journals publishing null results; Psychological Science badges; Registered Reports

## Collateral Damage Concerns

- Replication culture can harm early career researchers, minority scholars, clinical scientists
- "Name and shame" policing (Francis 2012c, Simonsohn 2013) is controversial
- Applied fields (clinical, organizational) need to adapt reforms to practical constraints
- Risk of over-generalizing suspicion from fraud cases to honest researchers

## Take-Home Message

1. QRPs are real and have inflated false-positive rates
2. But the crisis has been over-interpreted — 36% replication rate is explicable, not catastrophic
3. **Preregistration and open science** are the most important reforms
4. **Multiple replications** should replace single-study conclusions
5. **Sophisticated power analyses** must account for effect size uncertainty
6. **Full disclosure** of all results (significant and not) is essential
7. Effect size variation is theoretically interesting — psychology should model it, not ignore it

## Key Figures and Organizations

- **Patrick E. Shrout** (NYU) — quantitative psychologist; measurement, power analysis
- **Joseph L. Rodgers** (Vanderbilt) — quantitative psychologist; developmental methods
- **Brian Nosek** — Center for Open Science, OSF; see [[Brian Nosek]]
- **Open Science Collaboration (2015)** — 270+ authors; replicated 100 studies; see [[open-science-collaboration-2015]]
- **Diederik Stapel** — fraud case; social psychology; see context in [[Replication Crisis]]

## Cross-References

- [[Replication Crisis]] — parent concept page; update with Shrout & Rodgers framing
- [[Open Science]] — preregistration as most important reform
- [[HARKing]] — ← new page from this source
- [[Questionable Research Practices|Questionable Research Practices (QRPs)]] — ← new page from this source
- [[Publication Bias]] — file drawer; half-size effect sizes in OSC
- [[P-hacking]] — Simmons et al. (2011) taxonomy
- [[Power Analysis (Replication Studies)]] — ← new page
- [[Effect Size Heterogeneity]] — ← new page
- [[Replication Types Taxonomy]] — ← new page
- [[Open Science Framework]] — OSF; Nosek (2013)
- [[Registered Reports]] — in-principle acceptance
- [[Meta-Analysis]] — Schmidt & Oh; random effects; integrative data analysis
- [[Bayesian Statistics in Psychology]] — Verhagen & Wagenmakers; Bayes factors
- [[open-science-collaboration-2015]] — the 100-study replication project
