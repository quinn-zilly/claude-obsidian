---
address: c-000137
type: source
title: "Replicability, Robustness, and Reproducibility in Psychological Science"
authors: ["Brian Nosek", "Tom Hardwicke", "Hannah Moshontz", "Aurélien Allard", "Katherine Corker", "Anna Dreber", "Fiona Fidler", "Joe Hilgard", "Melissa Kline Struhl", "Michèle Nuijten", "Julia Rohrer", "Felipe Romero", "Anne Scheel", "Laura Scherer", "Felix Schönbrodt", "Simine Vazire"]
year: 2022
venue: "Annual Review of Psychology"
volume: 73
pages: "719–748"
doi: "10.1146/annurev-psych-020821-114157"
tags: [open-science, replication, metascience, methodology, psychology]
status: evergreen
created: 2026-05-22
related: ["[[Brian Nosek]]","[[Replication Crisis]]","[[Preregistration]]","[[Open Science]]","[[Analytic Reproducibility]]","[[Robustness (Science)]]","[[Replication as Theoretical Commitment]]","[[Questionable Research Practices]]","[[TOP Guidelines]]","[[Registered Reports]]","[[Open Science Framework]]","[[Many Labs]]","[[Psychological Science Accelerator]]"]
---

# Nosek et al. (2022) — Replicability, Robustness, and Reproducibility in Psychological Science

*Annual Review of Psychology* | 30-page review | 16 authors

## Core Argument

Replication is important, uncommon, and misunderstood. The 2010s were psychology's decade of active confrontation with low replicability. Systematic and multi-site projects revealed surprising failures. But innovation in doing and understanding replication has positioned psychology to improve. The paper synthesizes 10 years of evidence and charts a metascience agenda.

## Conceptual Framework: The Three R's

| Term | Definition |
|---|---|
| **Reproducibility** | Same data + same analysis → same result |
| **Robustness** | Same data + different analysis → consistent result |
| **Replicability** | Different data → same finding |

All three assess credibility but test different things. A finding can be reproducible, robust, replicable — and *still* invalid (wrong construct, bad causal inference).

### Two reproducibility failure types
- **Process failure**: data/code unavailable; can't repeat analysis
- **Outcome failure**: reanalysis gets different number

Artner et al. (2020): only 70% of 232 findings successfully reproduced.

### Robustness and the multiverse
Silberzahn et al. (2018): 29 teams, same data, same question → substantial variation in results. Fragile findings = risk factor for replicability. Without preregistration, fragility amplifies p-hacking concerns.

## Replication as Theoretical Commitment

> "A study is a replication when the innumerable differences from the original study are believed to be irrelevant for obtaining the evidence about the same finding." (Nosek & Errington 2020a)

Key moves:
- No exact replication exists — every study differs in sample, setting, treatment
- Replication = theoretical claim that differences don't matter
- Every replication is a generalizability test, but not vice versa
- "Conceptual replication" often describes generalizability tests, not true replications
- Direct/conceptual replication distinction → counterproductive under this framework

## State of Replicability: The Numbers

Overall (n=307 replications): **64% statistically significant same direction; effect sizes 68% as large**.

| Project | n | Success rate | Effect size ratio |
|---|---|---|---|
| Soto 2019 (personality) | 101 | 90% | 91% |
| Camerer et al. 2018 (Nature/Science) | 21 | 62% | 50% |
| Open Sci. Collab. 2015 | 94 | 36% | 49% |
| Multi-site replications | 77 | 56% | 53% |
| Protzko et al. 2020 (best practices) | 14 | ~97% | 97% |

Replication studies used **15.1× larger samples** on average than originals.

Key conclusion: replicability challenges observed "almost everywhere that has undergone systematic examination."

## What Predicts Replication Success?

### Theoretical maturity
- Well-established theory → higher prior probability → better replication
- Underspecified theories → hidden moderators → replication failures
- Context sensitivity invoked post-hoc to explain failures, but rarely supported when tested directly (Ebersole et al. 2016a, 2020; Klein et al. 2014, 2018)

### Features of original studies
- Low prior odds: median prior probability of OSC 2015 findings = **8.8%** (Dreber et al. 2015)
- Lower p-values in originals → higher replication success (r = −0.33)
- Large observed effects in low-power studies = sign of overestimation, not truth
- Low transparency → can't replicate what you can't understand
- Errington et al. (2021): 193 cancer biology replications — **zero** could be fully designed from published materials alone
- Selective reporting, p-hacking, HARKing → reduced replicability

### Features of replication studies
- Same quality problems as originals apply
- Reverse publication bias (replications favor null) could inflate failure rate
- Expert review of replication protocols produces little/no effect size improvement (Ebersole et al. 2020, median N=1,279)

## Predicting Replicability Without Replicating

Human judgment (surveys, elicitations, prediction markets) predicts outcomes:
- Prediction markets: r = 0.52 with success, 72% accuracy
- Surveys: r = 0.48, 64% accuracy  
- Elicitations (IDEA protocol): r = 0.75

Machine learning (Yang et al. 2020, Altmejd et al. 2019): narrative text > statistical features. ML ≈ prediction markets in accuracy. Potential for scalable replicability screening.

## What Degree Should Be Expected?

100% replicability ≠ healthy science. Conservative agenda → zero progress. Nonreplicability should **decline** with research maturity, but early-stage generative science will include failures. Key: always prefer designs that improve replicability, even for risky hypotheses.

## Cultural and Structural Barriers

### Social/structural
- Publication = currency of advancement
- Positive, novel, tidy > negative, replication, messy
- Researchers' reputations tied to *findings* not *rigor* → replication failure = personal attack
- Bakker et al. (2012): under publish-or-perish, rational to run many underpowered studies
- Smaldino & McElreath (2016): poor methods persist "with no deliberate cheating… only that publication is a principal factor for career advancement"
- Adding replications alone insufficient — structural change required

### Individual
- Motivated reasoning: confirmation bias, hindsight bias, outcome bias
- Intellectual humility needed but may not overcome structural incentives
- Preregistration + transparency = structural mitigation for bias

Optimistic note: researchers *value* rigor when asked directly. Researchers who acknowledge replication failures improve their reputation more than those whose findings replicate (Ebersole et al. 2016b).

## Evidence of Change (as of 2021)

### Tools and infrastructure
- OSF, AsPredicted: exponential growth in preregistrations and data sharing
- statcheck, GRIM: error detection tools
- By 2017: 44% of psychologists had preregistered; 51% had shared data (self-report)
- Audit studies: only 2% of 2014–2017 published studies shared data; 3% preregistered — large gap

### Journal policies (TOP Guidelines audit)
- 83% of journals at policy level 0 (no adoption) across standards
- Most common policies: data citation (36%), reporting guidelines (36%)
- Least common: preregistration of studies (12%), analysis plans (13%)
- High-impact journals slightly more likely to adopt any policy

### Institutions
- 2.2% of German psychology job ads mentioned replicability (2017–2020), rising from 1% → 3.8%
- Institutional change = lagging indicator

### Culture change strategy: Rogers diffusion model (COS extension)
Five interdependent levels, each necessary, none sufficient:
1. **Infrastructure** — make it possible
2. **User experience** — make it easy
3. **Communities** — make it normative
4. **Incentives** — make it rewarding
5. **Policy** — make it required

## Open Metascience Questions

1. What is the optimal replicability rate at different stages of research maturity?
2. What is replicability's role in cumulative science (vs. measurement, causal inference, theory, generalizability)?
3. Are interventions to improve replicability actually effective? (Too little causal evidence)
4. What's working in culture change? Are there unintended negative consequences?

## Key Figures

- **Figure 1**: Replication outcomes scatter plots across 5 projects (n=307 total)
- **Figure 2**: Prediction accuracy across markets, surveys, elicitations, ML (n=264 ML scores)
- **Figure 3**: Rogers diffusion + COS 5-level intervention model
- **Figure 4**: OSF/AsPredicted exponential growth 2012–2020
- **Figure 5**: TOP policy adoption across random (n=40) and high-impact (n=50) journals

## Authors & Affiliations
16 authors. Lead: [[Brian Nosek]] (UVA + COS). Also: [[Tom Hardwicke]] (Amsterdam), [[Simine Vazire]] (Melbourne), [[Michèle Nuijten]] (Tilburg Meta-Research Center), [[Anna Dreber]] (Stockholm School of Economics — prediction markets work).

## Cross-References
- [[Replication Crisis]] — primary empirical foundation
- [[Preregistration]] — key intervention discussed throughout
- [[Registered Reports]] — structural solution; associated with null results and higher quality
- [[HARKing]] — one QRP reducing replicability (cites Kerr 1998)
- [[P-hacking]] — garden of forking paths; Gelman & Loken 2013
- [[Publication Bias]] — mechanism driving low replicability
- [[Many Labs]] — primary multi-site replication data source
- [[Open Science Collaboration (2015)]] — 36% benchmark
- [[LeBel et al. (2018)]] — credibility framework cited throughout
- [[TOP Guidelines]] — journal policy audit
- [[Psychological Science Accelerator]] — large-scale collaboration mentioned
- [[Open Science Framework]] — infrastructure layer
- [[Robustness (Science)]] — one of three R's; multiverse/many analysts
- [[Replication as Theoretical Commitment]] — conceptual framework
- [[Questionable Research Practices]] — 14 surveys summarized
- [[Prediction Markets (Science)]] — r=0.52 with outcomes
