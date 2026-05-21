---

type: concept
address: c-000049
title: "Publication Bias"
tags:
  - open-science
  - statistics
  - meta-science
  - replication-crisis
status: developing
related:
  - "[[P-hacking]]"
  - "[[HARKing]]"
  - "[[Preregistration]]"
  - "[[Registered Reports]]"
  - "[[Replication Crisis]]"
  - "[[open-science-collaboration-2015]]"
  - "[[munafo-2017-manifesto]]"
created: unknown
updated: unknown
---

# Publication Bias

Publication bias (also called the **file drawer problem**) is the tendency for studies with statistically significant or positive results to be published at higher rates than studies with null or negative results, causing the published literature to systematically overestimate effect sizes and false-positive rates.

## The File Drawer Problem

Robert Rosenthal (1979) named the underlying phenomenon: researchers conduct many studies; those with null results are filed away rather than published. The published record represents a biased sample of the full evidence base.

## Mechanisms

| Mechanism | Actor |
|-----------|-------|
| **Researcher non-submission** | Authors don't submit null results, expecting rejection |
| **Journal rejection bias** | Editors and reviewers favor novel, significant findings |
| **Outcome switching** | Authors report the significant outcomes from a multi-outcome study |
| **Replication aversion** | Journals deprioritize direct replications ("we already know this") |

## Consequences

1. **Inflated effect sizes**: only the large-effect tail of the distribution gets published; meta-analyses overestimate true effects
2. **False-positive accumulation**: systematic overrepresentation of Type I errors in the literature
3. **Non-replication**: when a replication is run without publication bias, the smaller true effect (or null) appears — this is a major contributor to the [[Replication Crisis]]

## Evidence

[[open-science-collaboration-2015]]: replication effect sizes averaged half the original effect sizes. The authors note this is consistent with publication bias inflating originals; replications with preregistered designs and no selection pressure showed unbiased estimates.

[[munafo-2017-manifesto]]: 90% of Nature survey respondents agreed there is a reproducibility crisis; 85% of biomedical research estimated as wasted.

## Detection Methods

- **Funnel plot asymmetry**: in a meta-analysis, small studies should scatter symmetrically around the true effect; asymmetry indicates publication bias
- **p-curve analysis**: a right-skewed p-curve (many p values just below .05) suggests selective reporting
- **Comparison of registered vs. published outcomes**: [[munafo-2017-manifesto]] cites studies showing 70% of published psychology reports failed to mention one or more pre-registered outcome measures

## Remedies

- [[Preregistration]]: all studies discoverable regardless of outcome
- [[Registered Reports]]: in-principle acceptance before results; eliminates editorial publication bias
- **Study registration requirements**: clinical trials must be registered on ClinicalTrials.gov
- **Data-sharing requirements**: funders increasingly require deposition of all results
- **Replication incentives**: dedicated journals, funding mechanisms for replication studies

## See Also

- [[Replication Crisis]]
- [[P-hacking]]
- [[Preregistration]]
- [[Registered Reports]]
- [[Publication Bottleneck]] — structural origin: tight publication markets make non-significant results feel career-threatening; [[giner-sorolla-2012-science-or-art|Giner-Sorolla (2012)]] argues the bottleneck is the root cause of file-drawer suppression
