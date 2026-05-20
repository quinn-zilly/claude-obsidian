---
type: meta
title: "Hot Cache"
updated: 2026-05-20T00:00:00
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

2026-05-20. Nosek & Bar-Anan 2012 (Scientific Utopia I) + Nosek et al. 2012 (Scientific Utopia II) ingested — 9 new pages total. Counter at c-000073. Total pages: 102 | Sources ingested: 19. Still ingesting: 2 more new sources queued (Giner-Sorolla, Uhlmann).

## Key Recent Facts

- **2026-05-19 batch (backfilled to manifest):** Grant 1996, Barney & Felin 2013, Argote & Miron-Spektor 2011 (journal), Bosco et al. 2020, Nosek et al. 2018, LeBel et al. 2018, Lehmann et al. 2015, Foster & Deardorff 2017, Open Science Collaboration 2015, Munafò et al. 2017, claude-obsidian-ecosystem-research.md
- **2026-05-20 (1):** DiMaggio & Powell 1983 — 5 new pages: [[dimaggio-powell-1983-institutional-isomorphism]], [[Institutional Isomorphism]], [[Organizational Field]], [[Paul DiMaggio]], [[Walter Powell]]
- **2026-05-20 (2):** Nosek & Bar-Anan 2012 (Utopia I) — 4 new pages: [[nosek-bar-anan-2012-scientific-utopia-i]], [[Open Access]], [[Scientific Communication Reform]], [[Yoav Bar-Anan]]
- **2026-05-20 (3):** Nosek et al. 2012 (Utopia II) — 5 new pages: [[nosek-2012-scientific-utopia-ii]], [[Conflict of Interest in Science]], [[Motivated Reasoning]], [[Open Workflow]], [[Paradigm-Driven Research]]
- DragonScale counter: c-000073
- Argote & Miron-Spektor 2011 has TWO source pages: [[argote-2011-org-learning-experience]] (book chapter) and [[argote-miron-spektor-2011-org-learning-journal]] (journal article)

## Key Insights from This Batch

**Knowledge Management sub-domain:**
- Grant (1996) extends existing KM pages with micro-level integration mechanics: four coordination mechanisms (rules/directives, sequencing, routines, group problem-solving) and the *common knowledge* concept that maps directly onto [[Transactive Memory Systems]]
- Barney & Felin (2013) provide vocabulary for the micro-macro gap identified in [[zahra-2020-knowledge-integration]]: additive vs. emergent aggregation; microfoundations are not reductionism

**Open Science sub-domain (new):**
- [[open-science-collaboration-2015]]: 36% replication rate in psychology; replication effects half the magnitude of originals; cognitive > social psychology
- [[nosek-2018-preregistration]]: preregistration separates confirmatory (prediction) from exploratory (description) research; garden of forking paths; [[Registered Reports]] as strongest form
- [[lebel-2018-credibility-framework]]: four credibility dimensions — transparency, analytic reproducibility, analytic robustness, effect replicability; replication taxonomy from exact to conceptual
- [[munafo-2017-manifesto]]: five reform categories (methods, reporting, reproducibility, evaluation, incentives); badges 10× data sharing; >40 journals adopted Registered Reports
- **[[nosek-2012-scientific-utopia-ii]]** (NEW): core insight: [[Conflict of Interest in Science]] is not character flaw but ordinary human psychology under misaligned incentives; publishing rewards novelty+positive results; accuracy is abstract/distal. Solutions: [[Preregistration]] (separates confirmatory from exploratory), [[Open Workflow]] (makes research visible, enables accountability), [[Paradigm-Driven Research]] (reuses methods, reduces waste), PLoS ONE model (judge soundness not importance)

**Semantic Web sub-domain (new):**
- [[lehmann-2015-dbpedia]]: DBpedia extracts 400M+ structured facts from 111 Wikipedia editions; LOD cloud hub; used in IBM Watson, NLP pipelines
- DBpedia/LOD connects to KM domain: codification strategy, common knowledge, tacit→explicit conversion at scale

## Cross-Domain Connections

- [[metaBUS]] (open science) ↔ [[Knowledge Retention]] (KM): metaBUS is meta-level knowledge retention for science
- [[Preregistration]] (open science) ↔ [[Source-First Synthesis]] (wiki): both enforce temporal ordering of claims — commit before observe; source before synthesis
- [[Knowledge-Based Theory of the Firm]] (KM) ↔ [[DBpedia]] (semantic web): both instantiate "common knowledge" — Grant's integration prerequisite; DBpedia's ontology as shared schema
- [[Microfoundations]] (KM) ↔ [[Replication Crisis]] (open science): both demand causal transparency — microfoundations requires specifying individual-level mechanisms; open science requires specifying analysis decisions before outcomes
- **NEW: [[Institutional Isomorphism]] (inst. theory) ↔ [[Replication Crisis]] (open science):** normative isomorphism in science — shared methodological training, journal conventions, and credential filtering — may produce correlated errors and shared blind spots across labs, structurally contributing to the replication crisis
- **NEW: [[Institutional Isomorphism]] ↔ [[Knowledge Transfer]] (KM):** normative isomorphism is a mechanism of inter-organizational tacit knowledge transfer via personnel flows and professional communities; mimetic isomorphism is vicarious organizational learning
- **NEW: [[Motivated Reasoning]] (open science) ↔ [[Conflict of Interest in Science]] ↔ [[Institutional Isomorphism]]:** explains HOW incentive misalignment causes systemic bias — motivated reasoning is the psychological mechanism; happens unconsciously under normal conditions when situation is complex + information ambiguous + multiple defensible actions exist

## Active Threads

- Quinn is building a research wiki spanning organizational KM, research methodology, and institutional theory
- 4 more sources queued for ingest today: Nosek Scientific Utopia II, Giner-Sorolla 2012, Uhlmann et al. 2019, Klein et al. 2014
- Semantic web domain: single source (DBpedia paper); could expand with Wikidata, schema.org
- Wolf Vanpaemel (KU Leuven, co-author LeBel 2018) — entity page not yet created

## Domain Map

This wiki now has five distinct research domains:
1. **claude-obsidian ecosystem** — LLM Wiki pattern, DragonScale, plugin ecosystem
2. **Organizational KM** — KBV, KBT, organizational learning, knowledge integration (Argote, Zahra, Alavi, Grant, Barney)
3. **Open Science** — replication crisis, preregistration, Registered Reports (Nosek, Munafò, LeBel, OSC, OSF, metaBUS)
4. **Semantic Web** — DBpedia, Linked Open Data (Lehmann, Bizer)
5. **Institutional Theory** — isomorphism, organizational fields (DiMaggio, Powell) [NEW]

A domain scaffold (wiki/domains/) has not yet been created — would help separate and cross-reference them cleanly.

## Plugin State (from prior session, unchanged)

- Version: 1.6.0 (all four DragonScale mechanisms shipped and opt-in)
- Skills: wiki, wiki-ingest, wiki-query, wiki-lint, wiki-fold, save, autoresearch, canvas, defuddle, obsidian-bases, obsidian-markdown
- Tests: make test was green at last session
