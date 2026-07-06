---
address: c-000886
type: source
title: "Shadish, Cook & Campbell (2002) — Quasi-Experimental Designs That Use Both Control Groups and Pretests"
authors: ["William R. Shadish", "Thomas D. Cook", "Donald T. Campbell"]
year: 2002
venue: "Experimental and Quasi-Experimental Designs for Generalized Causal Inference, Ch. 5"
tags:
  - source
  - research-methods
  - causal-inference
  - quasi-experiments
  - study-design
status: seed
created: 2026-07-06
updated: 2026-07-06
related:
  - "[[Quasi-Experimental Design]]"
  - "[[Nonequivalent Control Group Design]]"
  - "[[Nonequivalent Dependent Variable]]"
  - "[[Propensity Scores and Hidden Bias]]"
  - "[[Selection Bias]]"
  - "[[Internal Validity]]"
  - "[[Threats to Validity]]"
  - "[[shadish-cook-campbell-2002-quasi-designs-no-control-or-no-pretest]]"
  - "[[shadish-cook-campbell-2002-statistical-conclusion-internal-validity]]"
---

# Shadish, Cook & Campbell (2002) — Quasi-Designs That Use Both Control Groups and Pretests

Nav: [[index]] | [[log]] | [[Open Science MOC]]

Chapter 5 of *Experimental and Quasi-Experimental Designs for Generalized Causal Inference* ("SCC"). The stronger cousin of [[shadish-cook-campbell-2002-quasi-designs-no-control-or-no-pretest|Ch. 4]]: designs with **both** a pretest and a comparison group. The chapter's thesis — a control group is of minimal value unless paired with a **pretest on the same outcome variable**, because the pretest reveals initial group differences, flags which selection-based threats are likely, and powers the statistical analysis.

## The untreated control group design with dependent pretest and posttest

The **[[Nonequivalent Control Group Design]]** (`NR O₁ X O₂ / NR O₁ O₂`) — the most common of all quasi-experiments. Because groups are nonequivalent by definition, selection bias is presumed; the pretest lets the researcher gauge its size and direction. The joint pretest + comparison group makes several **selection-based interaction threats** examinable:

- **selection-maturation** — groups grow at different rates (the "fan-spread" pattern);
- **selection-instrumentation** — unequal scale intervals + ceiling/floor effects;
- **selection-regression** — differential regression from extreme-score matching;
- **selection-history (local history)** — an event hits one group more than the other.

### Reading the outcome pattern

Threat *plausibility* depends on the observed data pattern, not just design. SCC walk through five prototypical outcomes of the pretest-posttest comparison-group design and show how each makes selection-maturation more or less credible — e.g. a **crossover** (Outcome 5, groups reverse rank order) is the most causally interpretable because no simple scaling/regression artifact can produce it, though it is statistically hard to detect.

## Ways to strengthen the design

- **Double pretest** (`O₁ O₂ X O₃`) — pre-treatment growth rate tests the selection-maturation assumption.
- **Switching replications** — the control group later receives treatment; probes internal *and* external validity (does the effect replicate in a new context?).
- **Reversed-treatment control group** — a conceptually opposite treatment (X₊ vs. X₋, e.g. job enrichment vs. impoverishment); a strong construct-validity design when an interaction results.
- **Direct measurement of threats** — measure the suspected history/selection process itself.
- **Cohort controls** — successive groups moving through an institution (siblings, grade cohorts, trainee classes); assumed less nonequivalent than arbitrary comparison groups. Strengthened by adding pretests, the recurrent institutional cycle design, and [[Nonequivalent Dependent Variable|nonequivalent dependent variables]].

## Combining many design elements

Exemplars (Reynolds & West's lottery "Ask for the Sale" study; Farquhar/Blackburn community cardiovascular trials with double pretest + independent-and-dependent samples) show that stacking elements — matching, multiple pre/posttests, nonequivalent DVs, removed/repeated treatments — can make quasi-experiments rival randomized experiments.

## The elements of design (Table 5.2)

Quasi-experiments are just **combinations of design elements** chosen to suit circumstances, in four families: **assignment** (random, cutoff-based, other nonrandom, matching/stratifying, masking), **measurement** (pre/posttests, retrospective and proxy pretests, nonequivalent DVs, moderator interactions, threat measurement), **comparison groups** (single/multiple nonequivalent, cohorts, internal vs. external, constructed contrasts), and **treatment** (switching replications, reversed, removed, repeated). SCC endorse R. A. Fisher's "make your theories elaborate" and Holland's advice to gather *more data* rather than make *more assumptions*.

## Appendix: statistical analysis of nonequivalent groups

Motto: **"statistical adjustment only after the best possible design controls have been used."** Three families of methods, all detailed on [[Propensity Scores and Hidden Bias]] and [[Selection Bias]]:

- **[[Propensity Scores and Hidden Bias|Propensity scores]]** — logistic-regression predicted probability of treatment; match/stratify/covary on it. Adjusts only for **observed** covariates → leaves hidden bias. Paired with **sensitivity analysis** (Rosenbaum) to ask how large a hidden bias would overturn the result.
- **Selection-bias models** (Heckman) — a selection equation + outcome equation; can model correlated errors, but highly assumption-sensitive and often fail to match randomized benchmarks (LaLonde 1986). Related to regression-discontinuity's fully-known selection model.
- **Latent-variable SEM** — adjusts for measurement unreliability; still only as good as the design underneath.

## Vault links

Predecessor: [[shadish-cook-campbell-2002-quasi-designs-no-control-or-no-pretest|Ch. 4]] (weaker designs). Threat vocabulary: [[shadish-cook-campbell-2002-statistical-conclusion-internal-validity|Ch. 2]], [[Internal Validity]], [[Threats to Validity]].

## Source

- Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference* (Ch. 5). Houghton Mifflin.
