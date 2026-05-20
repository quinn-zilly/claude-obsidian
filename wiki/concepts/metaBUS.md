---
type: concept
address: c-000052
title: "metaBUS"
tags:
  - meta-analysis
  - open-science
  - database
  - research-methods
  - knowledge-management
status: developing
related:
  - "[[Frank Bosco]]"
  - "[[Open Science]]"
  - "[[Knowledge Transfer]]"
  - "[[Analytic Reproducibility]]"
  - "[[bosco-2020-metabus]]"
---

# metaBUS

metaBUS is an open-access, curated database of research findings from applied psychology journals, designed to enable rapid, comprehensive, and reproducible meta-analysis.

## Scale and Coverage

- **1 million+ coded bivariate research findings**
- **27 journals** in applied psychology and management (1980–2018)
- **Hierarchical taxonomy** of ~5,000 constructs
- Free public access at metabus.org

## What It Contains

For each coded finding:
- Construct names (mapped to taxonomy)
- Sample size (N)
- Effect size (correlation coefficient)
- Publication year, journal, article DOI
- Moderator tags (sample type, country, measurement method)

## Two Search Modes

### Targeted Query
User specifies two constructs → system returns all coded bivariate relationships between them, with effect sizes and study-level moderators. Enables rapid, comprehensive meta-analysis.

### Exploratory (EMV — Effect Matrix Visualization)
User selects a set of constructs → system generates a heat map of all pairwise relationships. Identifies unexpected strong or weak relationships; useful for hypothesis generation.

## Significance

Traditional meta-analysis requires months of manual searching, retrieving, and coding studies. metaBUS compresses this to hours. This has several open-science implications:
1. **Completeness**: less susceptibility to selective coverage of the literature
2. **Reproducibility**: anyone can replicate a meta-analysis from the same database
3. **Registration**: meta-analytic protocols can be preregistered using the database's search architecture
4. **Knowledge accumulation acceleration**: the pace of systematic review becomes feasible for many more questions

## Limitations

- Coverage limited to 27 journals; gray literature, dissertations, book chapters excluded
- Bivariate focus: interaction effects, nonlinear relationships, mediation chains not captured
- Construct taxonomy reflects coder decisions; construct categorization is not always theory-neutral

## Knowledge Management Framing

metaBUS operationalizes **meta-level knowledge retention** — rather than storing findings in individual article PDFs (a low-integration format), it stores them in a queryable, structured database that enables the science community to know what it collectively knows. This is [[Knowledge-Based Theory of the Firm|KBT]]'s *common knowledge* concept applied to science: meta-knowledge about where scientific knowledge resides.

## See Also

- [[Frank Bosco]] — lead developer
- [[bosco-2020-metabus]] — source paper
- [[Open Science]]
- [[Analytic Reproducibility]]
