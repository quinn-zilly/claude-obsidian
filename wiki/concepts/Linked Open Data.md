---

type: concept
address: c-000051
title: "Linked Open Data"
tags:
  - semantic-web
  - knowledge-graphs
  - information-retrieval
  - data-sharing
status: developing
related:
  - "[[DBpedia]]"
  - "[[Jens Lehmann]]"
  - "[[Christian Bizer]]"
  - "[[Knowledge Transfer]]"
  - "[[lehmann-2015-dbpedia]]"
created: unknown
updated: unknown
---

# Linked Open Data

Linked Open Data (LOD) is a set of best practices for publishing and connecting structured data on the Web using open standards (RDF, SPARQL, HTTP URIs) so that data from different sources can be automatically combined and traversed.

## The Four LOD Principles (Berners-Lee)

1. Use URIs as names for things
2. Use HTTP URIs so things can be looked up
3. When someone looks up a URI, provide useful information using standards (RDF, SPARQL)
4. Include links to other URIs so more things can be discovered

These four principles ensure that any dataset following them can be automatically linked to and from any other LOD-compliant dataset.

## The LOD Cloud

The LOD cloud is the network of datasets that have been published following LOD principles and interlinked. As of 2015:
- **Hundreds of datasets** covering encyclopedic knowledge, life sciences, geography, government data, media, and more
- **[[DBpedia]]** is the central hub (2nd by incoming links)
- Other major nodes: Freebase, GeoNames, OpenCyc, MusicBrainz, Wikidata

## RDF: The Data Model

Resource Description Framework (RDF) is the W3C standard for LOD:
- Data expressed as **triples**: subject — predicate — object
- Both subjects and predicates are URIs; objects can be URIs or literals
- Triples form a directed labeled graph
- SPARQL is the query language for RDF graphs

## Relevance to Knowledge Management

LOD is an infrastructure for **knowledge transfer at web scale**: it enables any application to query, combine, and reason over knowledge from hundreds of sources without central coordination. This is the semantic web vision of knowledge integration ([[Knowledge Integration]]) applied globally.

The codification strategy of LOD — making tacit editorial structure in web content explicit as RDF — connects to the [[Tacit vs Explicit Knowledge]] distinction and [[Knowledge-Based Theory of the Firm|KBT]]'s concept of common knowledge (shared schema enabling integration).

## Current Status

LOD had its peak of hype ~2010–2015. Since then, the ecosystem has evolved:
- **Wikidata** has largely supplanted DBpedia as the primary structured knowledge source extracted from Wikimedia projects
- **Schema.org** has become the dominant structured data standard for web search
- Knowledge graphs (Google KG, Microsoft Satori, Amazon KG) use LOD principles internally without necessarily publishing as open LOD

The principles remain foundational; the implementation ecosystem has consolidated.

## See Also

- [[DBpedia]] — the LOD hub
- [[Jens Lehmann]] — architect
- [[Christian Bizer]] — LOD principles co-developer
- [[lehmann-2015-dbpedia]]
