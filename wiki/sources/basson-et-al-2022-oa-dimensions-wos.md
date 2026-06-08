---
type: source
address: c-000631
title: "The effect of data sources on the measurement of open access: A comparison of Dimensions and the Web of Science"
author:
  - "[[Isabel Basson]]"
  - "[[Marc-André Simard]]"
  - "[[Zoé Aubierge Ouangré]]"
  - "[[Cassidy R. Sugimoto]]"
  - "[[Vincent Larivière]]"
year: 2022
venue: "PLOS ONE"
volume: 17
pages: "e0265545"
doi: "10.1371/journal.pone.0265545"
tags:
  - open-science
  - open-access
  - bibliometrics
  - scientometrics
  - meta-science
  - measurement
status: ingested
ingested: 2026-06-08
related:
  - "[[Open Access]]"
  - "[[OA Type Classification]]"
  - "[[Bibliometric Database Coverage]]"
  - "[[Geographic Bias in Indexing]]"
  - "[[Dimensions]]"
  - "[[Web of Science]]"
  - "[[Unpaywall]]"
  - "[[thibault-2023-open-science-2-0]]"
---

# The effect of data sources on the measurement of open access

> [!abstract] One-line
> The measured prevalence of open access depends heavily on which bibliometric database you use — Dimensions reports more OA than Web of Science, and the gap is largest for publications from outside North America and Europe.

## Core claim

OA measurement is database-dependent. Same world, different number, depending on the lens. [[Web of Science]] (WoS) and [[Dimensions]] disagree on what fraction of the literature is open — and the disagreement is not random. It tracks geography: small for the developed West, large for the global South.

Therefore: choice of database is a policy-relevant methodological decision, not a neutral one. Inclusive databases give a fairer picture of OA uptake beyond the West.

## Method

- All journal publications in WoS and Dimensions, **2015–2019**, with first-author country affiliation.
- OA status from [[Unpaywall]]. WoS linked to Unpaywall (per Simard et al.); Dimensions ships Unpaywall status in-data.
- [[OA Type Classification|Unpaywall five-category scheme]]: gold / green-only / hybrid / bronze / closed. One category per paper, journal-based OA prioritized over self-archiving.
- One country per paper (first-author affiliation), mapped to region via World Bank classification, joined on ISO-2 codes.
- Document types: WoS = articles + reviews; Dimensions = "articles" (Dimensions labels **all** journal docs as articles, incl. meeting abstracts — cannot filter). This asymmetry is a known limitation.
- WoS corpus: **8,053,050** pubs. Dimensions corpus: **10,743,016** pubs.

## Headline results

| Metric | WoS | Dimensions |
|---|---|---|
| Overall % OA | 43.4% | 46.6% |
| Biggest category gap (WoS higher) | green-only | — |
| Biggest category gap (Dimensions higher) | — | bronze |

Regional OA gap (Dimensions minus WoS), developed regions ≈ equal; less-developed regions much higher in Dimensions:

- South Asia **+57.9%**
- Latin America & Caribbean **+36.6%**
- Middle East & North Africa **+33.5%**
- Sub-Saharan Africa **+12.4%**
- Europe & Central Asia, North America: ~equal

By OA type:
- Gold is the single most abundant OA type in every region **except North America** (where it's green-only in WoS, bronze in Dimensions).
- Gold much higher in Dimensions for South Asia (+28.3%), LAC (+22.6%), MENA (+19.9%).
- **Green-only is the one type consistently higher in WoS** — esp. North America, Europe, Central Asia.
- Bronze higher in Dimensions for **every** region.
- Hybrid <10% everywhere; higher in WoS for North America (+24.4%) and Europe.

Country level (Fig 4): for most countries Dimensions shows higher % OA than WoS, most pronounced for Asia and the global South.

## Why the gap (authors' explanation)

WoS has a [[Geographic Bias in Indexing|Western indexing bias]] — its journals are mostly also in Dimensions, so the shared core agrees. The *extra* journals Dimensions indexes (smaller national journals, often via Crossref/DOI inclusion) are disproportionately OA. See [[Bibliometric Database Coverage]].

- **Green-only higher in WoS** → WoS-represented countries (West) lean on self-archiving (mandates + repositories like PubMed). Repositories are scarcer in developing countries.
- **Bronze higher in Dimensions everywhere** → broad inclusion pulls in many non-DOAJ journals; messy/non-standard metadata blocks DOAJ listing → classified bronze not gold. Some may be predatory journals or excluded doc types (editorials).
- Southern OA platforms — **AJOL** (Africa), **AmeliCA** (Latin America), **SciELO** (Brazil) — are indexed by Dimensions, boosting visible OA there.

## Caveats the authors raise

> [!warning] Dimensions limitations
> - Larger share of records with **missing affiliation metadata**; standardized via GRID + ORCID. Many countries (Africa, South America, Central Asia) historically absent from GRID → country-level studies constrained by GRID coverage.
> - **No document-type disaggregation** for journal pubs → can't cleanly exclude meeting abstracts/editorials. So the study can't fully rule out that doc-type differences drive part of the OA gap.

## Why it matters for the wiki

Concrete, quantified demonstration that "% of science that is OA" is not a single fact — it is a measurement contingent on infrastructure. Strengthens [[Open Access]] with a measurement layer, and connects OA equity to database politics. Pairs with [[thibault-2023-open-science-2-0]] on building a fairer research ecosystem.

## Sources

- DOI: [10.1371/journal.pone.0265545](https://doi.org/10.1371/journal.pone.0265545)
- Underlying country data (Figshare): [10.6084/m9.figshare.18319238](https://doi.org/10.6084/m9.figshare.18319238)
- Conference precursor: Basson et al., ISSI 2021, pp. 93–98.
- Funder: IDRC Science Granting Councils Initiative, project 109272 (Open access in Africa).
