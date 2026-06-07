---

type: source
address: c-000024
title: "DBpedia – A Large-scale, Multilingual Knowledge Base Extracted from Wikipedia"
author:
  - "[[Jens Lehmann]]"
  - "Robert Isele"
  - "Max Jakob"
  - "Anja Jentzsch"
  - "Dimitris Kontokostas"
  - "Pablo N. Mendes"
  - "Sebastian Hellmann"
  - "Mohamed Morsey"
  - "Patrick van Kleef"
  - "Sören Auer"
  - "[[Christian Bizer]]"
year: 2015
venue: "Semantic Web"
volume: 6
issue: 2
pages: "167–195"
doi: "10.3233/SW-140134"
tags:
  - knowledge-graphs
  - semantic-web
  - linked-open-data
  - dbpedia
  - information-retrieval
status: ingested
ingested: 2026-05-19
related:
  - "[[Jens Lehmann]]"
  - "[[Christian Bizer]]"
  - "[[DBpedia]]"
  - "[[Linked Open Data]]"
  - "[[Knowledge Transfer]]"
  - "[[Knowledge Management MOC]]"
created: unknown
updated: unknown
---

# Lehmann et al. (2015) — DBpedia

> [!key-insight] Core Claim
> DBpedia extracts structured knowledge from Wikipedia across 111 language editions, creating a multilingual, interlinked knowledge base of 400M+ facts (English) that serves as the hub of the Linked Open Data cloud and enables downstream applications from NLP to question answering.

## Bibliographic Details

Jens Lehmann et al. "DBpedia – A Large-scale, Multilingual Knowledge Base Extracted from Wikipedia." *Semantic Web* 6, no. 2 (2015): 167–195.

## Summary

### What Is DBpedia?

DBpedia is a community project that systematically extracts structured data from Wikipedia's semi-structured markup (infoboxes, categories, links) and makes it available as RDF triples under open licenses. It is the central hub of the Linked Open Data (LOD) cloud.

**Scale (English edition)**:
- 400M+ facts about 3.7M things (people, places, organizations, concepts)
- 20M+ links to external data sources
- Ontology: 320 classes, 1,650 properties

**Coverage**: 111 Wikipedia language editions, each producing a separate DBpedia dataset linked via interlanguage links.

### Architecture

**Extraction pipeline:**
1. Wikipedia dumps → custom extractors for different markup types
2. Ontology-based extraction: structured classes and properties defined by human ontology editors
3. DBpedia Spotlight: entity recognition and linking for free text

**DBpedia Live**: real-time extraction synchronized with Wikipedia edits, allowing near-live updates to the knowledge base.

**SPARQL endpoint**: public query interface allowing any user to query the knowledge base using standard semantic web query language.

### The Ontology

The DBpedia ontology is manually curated and hierarchically organized:
- Classes: Person, Organization, Place, Work, Event, Species, ...
- Each class has defined properties (e.g., Person → birthDate, birthPlace, occupation)
- Mapped to schema.org, UMBEL, Cyc, and other ontologies for interoperability

### Applications

The paper describes deployment in:
- **IBM Watson** (Jeopardy): DBpedia provided entity background knowledge
- **NLP pipelines**: named entity recognition and disambiguation
- **Question answering systems**: structured querying of entity properties
- **Knowledge exploration**: browser-based exploration of entity neighborhoods

### Linked Open Data Position

DBpedia is ranked 2nd in the LOD cloud by incoming links, serving as a "glue layer" connecting disparate datasets. It links to Freebase, GeoNames, OpenCyc, MusicBrainz, and hundreds of other datasets.

### Relevance to Knowledge Management

DBpedia operationalizes what knowledge management theorists call **knowledge codification and transfer at scale** — the problem of taking tacit knowledge (implicit in Wikipedia's editorial decisions) and making it explicit (RDF triples with formal semantics). The DBpedia Ontology is a formal attempt to create the "common knowledge" that [[grant-1996-knowledge-based-theory]] identifies as the precondition for knowledge integration.

## Key Entities

- [[Jens Lehmann]] — University of Leipzig / University of Bonn; primary architect of DBpedia
- [[Christian Bizer]] — University of Mannheim; Semantic Web researcher, LOD pioneer

## Connections to Existing Wiki

- [[DBpedia]] concept page
- [[Linked Open Data]] concept page
- [[Knowledge Transfer]] — DBpedia as infrastructure for transferring knowledge across applications and communities
- [[Tacit vs Explicit Knowledge]] — DBpedia's extraction project is fundamentally about codifying implicit structure in Wikipedia into explicit RDF
- [[alavi-leidner-2001-knowledge-management]] — KMS perspect