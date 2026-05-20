---
type: concept
address: c-000050
title: "DBpedia"
tags:
  - knowledge-graphs
  - semantic-web
  - linked-open-data
  - information-retrieval
status: developing
related:
  - "[[Linked Open Data]]"
  - "[[Jens Lehmann]]"
  - "[[Christian Bizer]]"
  - "[[Knowledge Transfer]]"
  - "[[Tacit vs Explicit Knowledge]]"
  - "[[lehmann-2015-dbpedia]]"
---

# DBpedia

DBpedia is a community project that extracts structured knowledge from Wikipedia and publishes it as Linked Open Data (LOD), serving as a central hub connecting hundreds of datasets in the LOD cloud.

## What DBpedia Does

Wikipedia contains vast amounts of semi-structured information in infoboxes, categories, and inter-language links. DBpedia's extraction framework systematically converts this implicit structure into explicit RDF (Resource Description Framework) triples — the atomic unit of semantic web knowledge representation: *subject — predicate — object*.

Example: `dbpedia:Barack_Obama rdf:type dbo:Person` and `dbpedia:Barack_Obama dbo:birthPlace dbpedia:Honolulu`

## Scale (English edition, 2015)

- **3.7 million entities** described
- **400+ million RDF triples**
- **20 million links** to external data sources
- Available in **111 language editions**
- Ontology: **320 classes**, **1,650 properties**

## Architecture

**Extraction pipeline:**
1. Wikipedia XML dumps → specialized extractors per markup type
2. Ontology mapping: human-curated class/property definitions applied
3. Entity linking: DBpedia Spotlight links free text mentions to URIs

**DBpedia Live:** real-time synchronization with Wikipedia edits (near-live updates)

**SPARQL endpoint:** `dbpedia.org/sparql` — public query interface

## Position in the LOD Cloud

DBpedia is **second in the LOD cloud by incoming links** — serving as the central connecting hub between hundreds of specialized datasets (MusicBrainz, GeoNames, Freebase, OpenCyc, etc.). It provides stable URIs for entities that other datasets can reference.

## Applications

- **IBM Watson / Jeopardy**: entity background knowledge
- **Question answering**: SPARQL-based factual QA
- **NLP**: entity recognition and disambiguation via DBpedia Spotlight
- **Knowledge graph completion**: training data for embedding models

## Knowledge Management Perspective

DBpedia is a large-scale operationalization of **knowledge codification**: converting implicit structure (Wikipedia editorial conventions) into explicit, machine-readable knowledge. This is the fundamental move in the [[Tacit vs Explicit Knowledge]] distinction — DBpedia makes tacit web knowledge explicit at scale.

From an [[Organizational Learning]] perspective, DBpedia implements a **codification strategy** for web knowledge — analogous to Alavi & Leidner's people-to-document KMS type ([[alavi-leidner-2001-knowledge-management]]).

## See Also

- [[Linked Open Data]] — the publishing framework
- [[Jens Lehmann]] — primary architect
- [[Christian Bizer]] — co-developer
- [[lehmann-2015-dbpedia]] — source paper
