---
type: concept
address: c-000644
title: "Researcher Degrees of Freedom"
aliases: ["RDFs", "Researcher Degrees of Freedom"]
tags:
  - open-science
  - research-methods
  - replication-crisis
  - questionable-research-practices
  - statistics
status: developing
related:
  - "[[P-hacking]]"
  - "[[Questionable Research Practices]]"
  - "[[HARKing]]"
  - "[[Preregistration]]"
  - "[[Motivated Reasoning]]"
  - "[[Replication Crisis]]"
  - "[[simmons-et-al-2011-false-positive-psychology]]"
  - "[[Open Science MOC]]"
created: 2026-06-08
updated: 2026-06-08
---

# Researcher Degrees of Freedom

The many defensible, often unmade-in-advance decisions a researcher faces while collecting and analyzing data — each of which can be chosen, consciously or not, to push results toward statistical significance. Coined by [[Joseph P. Simmons]], [[Leif D. Nelson]], and [[Uri Simonsohn]] in [[simmons-et-al-2011-false-positive-psychology|False-Positive Psychology (2011)]].

## The decisions

Should more data be collected? Should observations be excluded? Which conditions combined or compared? Which covariates included? Should measures be combined or transformed? None of these is *necessarily* wrong — and that is exactly the problem. Because every option is justifiable, [[Motivated Reasoning]] lets a researcher self-servingly land on whichever choice yields $p \le .05$.

## Why they inflate false positives

Exploring multiple analytic paths while reporting only the one that "worked" means running many implicit tests but disclosing one. The probability that *at least one* of many analyses crosses $p < .05$ necessarily exceeds 5%. Simmons et al. quantified four common RDFs via simulation:

| RDF | False-positive rate ($p<.05$) |
|---|---|
| Two correlated DVs | 9.5% |
| Optional stopping (+10 obs, re-test) | 7.7% |
| Flexible covariate (gender) | 11.7% |
| Dropping a condition | 12.6% |
| **All four combined** | **60.7%** |

This is the mechanistic engine behind [[P-hacking]] — RDFs are the *raw material*; p-hacking is the act of exploiting them.

## Relationship to neighboring concepts

- **[[P-hacking]]:** the behavior of exploiting RDFs at the analysis stage. RDFs name the choice points; p-hacking is walking the [[P-hacking#The Garden of Forking Paths (Gelman & Loken)|garden of forking paths]].
- **[[HARKing]]:** exploiting RDFs at the *write-up* stage (reframing hypotheses post hoc).
- **[[Questionable Research Practices]]:** RDF exploitation is the common substrate of most QRPs.
- **[[Motivated Reasoning]]:** the psychological mechanism that makes RDF exploitation feel principled rather than dishonest — "not driven by a willingness to deceive."

## Remedies

RDFs cannot be eliminated (some analytic choices are genuinely ambiguous), only **constrained or disclosed**:

- **[[Preregistration]]** / [[Registered Reports]]: fix the analysis plan before seeing data, collapsing the forking paths.
- **Disclosure requirements** (Simmons et al.): list all variables, all conditions, results with/without exclusions and covariates — making the exercised degrees of freedom visible.
- **Multiverse / robustness analysis:** report results across *all* defensible specifications; real effects survive, RDF-driven ones fragment.

## See also

- [[simmons-et-al-2011-false-positive-psychology]] — origin paper
- [[P-hacking]], [[HARKing]], [[Questionable Research Practices]]
- [[Preregistration]], [[Replication Crisis]]
- [[Open Science MOC]]
