---
type: meta
title: "Hot Cache"
updated: 2026-05-19T00:00:00
tags:
  - meta
  - hot-cache
status: evergreen
related:
  - "[[index]]"
  - "[[log]]"
  - "[[Wiki Map]]"
  - "[[getting-started]]"
  - "[[DragonScale Memory]]"
---

# Recent Context

Navigation: [[index]] | [[log]] | [[overview]]

## Last Updated

2026-05-19. Batch ingest of 10 PDFs from Zotero KMBI/Research Paper collection. 37 new pages created. Wiki now spans four research domains: (1) claude-obsidian ecosystem, (2) organizational knowledge management, (3) open science / replication crisis, and (4) semantic web / knowledge graphs.

## Key Recent Facts

- 10 PDFs ingested: Grant 1996, Barney & Felin 2013, Argote & Miron-Spektor 2011 (journal), Bosco et al. 2020, Nosek et al. 2018, LeBel et al. 2018, Lehmann et al. 2015, Foster & Deardorff 2017, Open Science Collaboration 2015, Munafò et al. 2017
- DragonScale counter now at 54 (c-000054 was last address assigned)
- Total wiki pages: 88 | Sources ingested: 16
- Argote & Miron-Spektor 2011 now has TWO source pages: [[argote-2011-org-learning-experience]] (book chapter, from prior session) and [[argote-miron-spektor-2011-org-learning-journal]] (journal article, this session)
- Bosco et al. 2020 (metaBUS) was previously skipped for missing PDF — now ingested

## Key Insights from This Batch

**Knowledge Management sub-domain:**
- Grant (1996) extends existing KM pages with micro-level integration mechanics: four coordination mechanisms (rules/directives, sequencing, routines, group problem-solving) and the *common knowledge* concept that maps directly onto [[Transactive Memory Systems]]
- Barney & Felin (2013) provide vocabulary for the micro-macro gap identified in [[zahra-2020-knowledge-integration]]: additive vs. emergent aggregation; microfoundations are not reductionism

**Open Science sub-domain (new):**
- [[open-science-collaboration-2015]]: 36% replication rate in psychology; replication effects half the magnitude of originals; cognitive > social psychology
- [[nosek-2018-preregistration]]: preregistration separates confirmatory (prediction) from exploratory (description) research; garden of forking paths; [[Registered Reports]] as strongest form
- [[lebel-2018-credibility-framework]]: four credibility dimensions — transparency, analytic reproducibility, analytic robustness, effect replicability; replication taxonomy from exact to conceptual
- [[munafo-2017-manifesto]]: five reform categories (methods, reporting, reproducibility, evaluation, incentives); badges 10× data sharing; >40 journals adopted Registered Reports

**Semantic Web sub-domain (new):**
- [[lehmann-2015-dbpedia]]: DBpedia extracts 400M+ structured facts from 111 Wikipedia editions; LOD cloud hub; used in IBM Watson, NLP pipelines
- DBpedia/LOD connects to KM domain: codification strategy, common knowledge, tacit→explicit conversion at scale

## Cross-Domain Connections

- [[metaBUS]] (open science) ↔ [[Knowledge Retention]] (KM): metaBUS is meta-level knowledge retention for science
- [[Preregistration]] (open science) ↔ [[Source-First Synthesis]] (wiki): both enforce temporal ordering of claims — commit before observe; source before synthesis
- [[Knowledge-Based Theory of the Firm]] (KM) ↔ [[DBpedia]] (semantic web): both instantiate "common knowledge" — Grant's integration prerequisite; DBpedia's ontology as shared schema
- [[Microfoundations]] (KM) ↔ [[Replication Crisis]] (open science): both demand causal transparency — microfoundations requires specifying individual-level mechanisms; open science requires specifying analysis decisions before outcomes

## Active Threads

- Quinn is building a research wiki spanning organizational KM and research methodology
- Open science / replication crisis is a new domain; four tightly linked sources now ingested
- Semantic web is a new domain; single source (DBpedia paper); could expand with Wikidata, schema.org
- v1.6.0 still not pushed to GitHub (from prior session — local commits only, no git tag)
- Wolf Vanpaemel (KU Leuven, co-author LeBel 2018) — entity page not created; could add if domain expands

## Domain Map

This wiki now has four distinct research domains:
1. **claude-obsidian ecosystem** — LLM Wiki pattern, DragonScale, plugin ecosystem
2. **Organizational KM** — KBV, KBT, organizational learning, knowledge integration (Argote, Zahra, Alavi, Grant, Barney)
3. **Open Science** — replication crisis, preregistration, Registered Reports (Nosek, Munafò, LeBel, OSC, OSF, metaBUS)
4. **Semantic Web** — DBpedia, Linked Open Data (Lehmann, Bizer)

A domain scaffold (wiki/domains/) has not yet been created — would help separate and cross-reference them cleanly.

## Plugin State (from prior session, unchanged)

- Version: 1.6.0 (all four DragonScale mechanisms shipped and opt-in)
- Skills: wiki, wiki-ingest, wiki-query, wiki-lint, wiki-fold, save, autoresearch, canvas, defuddle, obsidian-bases, obsidian-markdown
- Tests: make test was green at last session
