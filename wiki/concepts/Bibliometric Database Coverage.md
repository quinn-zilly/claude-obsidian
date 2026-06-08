---
type: concept
address: c-000640
title: "Bibliometric Database Coverage"
tags:
  - bibliometrics
  - scientometrics
  - measurement
  - meta-science
status: developing
created: 2026-06-08
updated: 2026-06-08
related:
  - "[[Web of Science]]"
  - "[[Dimensions]]"
  - "[[Geographic Bias in Indexing]]"
  - "[[Open Access]]"
  - "[[basson-et-al-2022-oa-dimensions-wos]]"
---

# Bibliometric Database Coverage

What a bibliometric database indexes determines what any study built on it can measure. Coverage is an upstream design choice that silently shapes downstream findings — including "how much science is open."

## Two inclusion philosophies

**Selective** — index only journals meeting quality/impact criteria (citations, reputation). [[Web of Science]] and Scopus. Smaller, curated, Western-skewed corpus.

**Comprehensive** — index everything meeting one mechanical criterion. [[Dimensions]] keys on **DOI presence** (via Crossref). Much larger; pulls in smaller national journals and non-Western platforms (AJOL, AmeliCA, SciELO).

Coverage hierarchy (from the literature): Dimensions > Scopus > WoS. Scopus indexes more than WoS, and is less English-biased (Mongeon & Paul-Hus 2016).

## The measurement consequence

A metric computed over a selective corpus answers "...among the most-cited core journals," not "...across all of science." The shared core of two databases tends to agree; databases diverge precisely on the **extra** material the broader one adds. In [[basson-et-al-2022-oa-dimensions-wos]] that extra material is disproportionately OA, so Dimensions reports more OA — see [[Geographic Bias in Indexing]].

## The trade-off

Breadth is not free. Comprehensive databases carry messier metadata: missing affiliations (Dimensions standardizes via GRID + ORCID, historically thin for the global South) and no document-type disaggregation. So broader coverage buys representativeness at the cost of cleanliness, constraining fine-grained comparative work.
