---
type: source
address: c-000021
title: "Advancing Meta-Analysis With metaBUS"
author: "Frank A. Bosco, Piers Steel, Michael A. Oswald, Tanner Aguinis, Annette Dunleavy"
year: 2020
venue: "Advances in Methods and Practices in Psychological Science"
volume: 3
issue: 1
pages: "124–137"
doi: "10.1177/2515245919882793"
tags:
  - meta-analysis
  - open-science
  - knowledge-management
  - research-methods
  - databases
status: ingested
ingested: 2026-05-19
related:
  - "[[Frank Bosco]]"
  - "[[metaBUS]]"
  - "[[Open Science]]"
  - "[[Knowledge Transfer]]"
  - "[[nosek-2018-preregistration]]"
  - "[[open-science-collaboration-2015]]"
---

# Bosco et al. (2020) — Advancing Meta-Analysis With metaBUS

> [!key-insight] Core Claim
> metaBUS is a curated database of 1 million+ research findings from 27 applied psychology journals (1980–2018) that enables rapid, comprehensive, and reproducible meta-analysis — replacing laborious manual literature searches.

## Bibliographic Details

Frank A. Bosco, Piers Steel, Michael A. Oswald, Tanner Aguinis, and Annette Dunleavy. "Advancing Meta-Analysis With metaBUS." *Advances in Methods and Practices in Psychological Science* 3, no. 1 (2020): 124–137.

## Summary

### The Problem metaBUS Addresses

Traditional meta-analysis requires researchers to manually search, retrieve, and code individual studies — a process that takes months to years and introduces selection and coding errors. The result is a fragmented literature where cumulative synthesis is rare, replication is inconsistent, and findings are not easily compared across subfields.

### What Is metaBUS?

metaBUS is a centralized database of coded research findings from applied psychology journals:
- **Coverage**: 27 journals, 1980–2018
- **Scale**: 1 million+ curated bivariate findings
- **Taxonomy**: hierarchical construct taxonomy with ~5,000 constructs covering individual differences, job attitudes, performance dimensions, leadership styles, and more

### Two Search Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| **Targeted query** | User specifies two constructs → system returns all coded bivariate relationships | Replaces traditional literature search for specific relationships |
| **Exploratory (EMV)** | Effect Matrix Visualization — heat map of all relationships for a set of constructs | Hypothesis generation; identifying unexpected patterns |

### Key Technical Features

- Hierarchical taxonomy allows searches at varying levels of specificity (e.g., "job satisfaction" → "facet satisfaction" → "pay satisfaction")
- All findings are tagged with moderator variables (publication year, sample type, measurement method) enabling moderated meta-analysis
- Data are publicly accessible, enabling reproducible re-analyses
- DOI linkage back to source articles for verification

### Implications for Open Science

The paper argues that metaBUS advances open science in organizational research by:
1. Making the full evidence base discoverable (reduces publication bias effects on meta-analyses)
2. Enabling rapid cumulation — a meta-analysis that took 2 years can be done in hours
3. Supporting registration of meta-analytic protocols (pre-registerable search strategies)

This connects metaBUS to the broader open science infrastructure discussed in [[open-science-collaboration-2015]], [[nosek-2018-preregistration]], and [[munafo-2017-manifesto]].

### Limitations Acknowledged

- Coverage limited to journals in the taxonomy — specialized outlets, book chapters, dissertations not included
- Bivariate focus misses interaction effects and nonlinear relationships
- Construct taxonomy reflects authors' decisions; users may categorize constructs differently

## Key Entities

- [[Frank Bosco]] — Virginia Commonwealth University; lead developer of metaBUS
- Kai Larsen — University of Colorado Boulder; database infrastructure

## Connections to Existing Wiki

- [[Knowledge Transfer]] — metaBUS is a tool for transferring cumulated research knowledge across time and subfields
- [[Open Science]] — metaBUS is an open-science infrastructure for meta-science
- [[zahra-2020-knowledge-integration]] — metaBUS is particularly relevant for knowledge integration research; it holds thousands of findings on the variables Zahra et al. review
- The bosco et al. paper was previously noted as skipped in [[hot.md]] (no PDF attached in the earlier Zotero batch); now ingested with PDF available
