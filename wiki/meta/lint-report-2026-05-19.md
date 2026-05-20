---
type: meta
title: "Lint Report 2026-05-19"
created: 2026-05-19
updated: 2026-05-19
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-05-19

## Summary

- Pages scanned: 99
- Orphan pages: 0
- Dead links: 21 (5 unique targets mentioned 2+ times → missing pages)
- Stale index entries: 5
- Frontmatter gaps: 37 pages (all missing `created` / `updated`)
- Empty sections: 34 pages
- Address errors: 4 (1 collision, 3 missing post-rollout addresses)
- Manifest errors: 0
- Legacy pending backfill: 21 pages
- Semantic tiling: skipped (ollama not reachable)

---

## Orphan Pages

✅ None found. All pages have at least one inbound wikilink.

---

## Dead Links

21 broken wikilinks found. Several are test/placeholder links, others are real gaps.

### Missing Pages (linked 2+ times — candidates to create)

- `Wolf Vanpaemel`: referenced in [[Etienne LeBel]] and [[lebel-2018-credibility-framework]]. Suggest: create entity stub.
- `Wiki Map`: referenced in [[getting-started]] and [[index]]. Note: `Wiki Map.canvas` exists but there's no `Wiki Map.md`. Suggest: create a redirect/stub or update links to point to the canvas.

### Placeholder / Example Links (safe to ignore or clean)

- `[[notes/Foo]]` in `wiki/log.md` and `wiki/concepts/DragonScale Memory.md` — test link from docs/examples.
- `[[Foo]]` in `wiki/concepts/DragonScale Memory.md` — example link.
- `[[wiki-fold]]` in `wiki/folds/fold-k3-from-2026-04-23-to-2026-04-24-n8.md` — references a skill page that doesn't exist as a wiki page.
- `[[fold-template]]` in `wiki/folds/fold-k3-from-2026-04-23-to-2026-04-24-n8.md` — template reference, not a wiki page.
- `[[dashboard.base]]` in `wiki/meta/dashboard.md` — `.base` files aren't `.md`; wikilink won't resolve.

### Real Gaps to Fix

- `[[How does the LLM Wiki pattern work?]]` in `wiki/log.md` — page exists as `How does the LLM Wiki pattern work` (missing `?`). Suggest: rename the file or fix the link.
- `[[claude-obsidian-presentation]]` in `wiki/overview.md` — missing. Suggest: create stub or remove link.
- `[[AI Marketing Hub Cover Images Canvas]]` in `wiki/overview.md` — missing. Suggest: remove link or create canvas.
- `[[wikilinks]]` in `wiki/concepts/cherry-picks.md` — no wiki page for "wikilinks". Suggest: create concept page or link to [[Obsidian]] docs.
- `[[Three laws of motion]]` in `wiki/concepts/Persistent Wiki Artifact.md` — unrelated/example link. Suggest: remove.
- `[[Zahra et al. 2020]]` in `wiki/sources/barney-felin-2013-microfoundations.md` — source page exists as `zahra-2020-knowledge-integration`. Suggest: fix link to `[[zahra-2020-knowledge-integration]]`.
- `[[hot.md]]` in `wiki/sources/bosco-2020-metabus.md` — should link to `[[hot]]` (drop `.md` extension).
- `[[Kogut & Zander]]` in `wiki/sources/grant-1996-knowledge-based-theory.md` — no page for this entity. Suggest: create entity stub.
- `[[LeBel et al. 2018]]` in `wiki/sources/nosek-2018-preregistration.md` — source exists as `lebel-2018-credibility-framework`. Suggest: fix link.

---

## Stale Index Entries

5 broken entries in `wiki/index.md`:

- `[[Wiki Map]]` (×2) — no `.md` page for Wiki Map; canvas exists but isn't wikilink-navigable.
- `[[concepts/_index]]` — index pages use underscored path format not resolvable as wikilinks; Obsidian resolves by filename, not path. Suggest: change to `[[_index]]` in concepts section context, or remove.
- `[[entities/_index]]` — same issue.
- `[[sources/_index]]` — same issue.

---

## Missing Pages

Concepts mentioned in multiple pages but lacking their own wiki page:

- **Wolf Vanpaemel** (2 mentions): [[Etienne LeBel]], [[lebel-2018-credibility-framework]]. Suggest: create entity stub.
- **Wiki Map** (2 mentions): [[getting-started]], [[index]]. Suggest: create a `Wiki Map.md` stub that embeds/links the canvas.

(Remaining dead links appear once each or are placeholder/example content.)

---

## Frontmatter Gaps

37 pages are missing `created` and `updated` dates. These are all pre-rollout (legacy) pages. No other required fields are missing.

**Concepts (14):** Analytic Reproducibility, DBpedia, HARKing, Knowledge-Based Theory of the Firm, Linked Open Data, Microfoundations, Open Science Framework, Open Science, P-hacking, Preregistration, Publication Bias, Registered Reports, Replication Crisis, metaBUS

**Entities (13):** Brian Nosek, Center for Open Science, Christian Bizer, Ella Miron-Spektor, Etienne LeBel, Frank Bosco, Jay Barney, Jens Lehmann, John Ioannidis, Marcus Munafò, Open Science Collaboration, Robert Grant, Teppo Felin

**Sources (10):** argote-miron-spektor-2011-org-learning-journal, barney-felin-2013-microfoundations, bosco-2020-metabus, foster-deardorff-2017-osf, grant-1996-knowledge-based-theory, lebel-2018-credibility-framework, lehmann-2015-dbpedia, munafo-2017-manifesto, nosek-2018-preregistration, open-science-collaboration-2015

Suggest: auto-fix with placeholder dates (`created: unknown`, `updated: unknown`) or use the file's git mtime.

---

## Empty Sections

34 pages have headings with no content beneath them. Top candidates to fill:

- [[Wiki vs RAG]] — the main heading has no body; entire page may be empty.
- [[Hot Cache]] — `# Recent Context` has no content (this page is auto-updated but currently empty).
- [[Knowledge Management]], [[Knowledge Retention]], [[Knowledge Transfer]], [[Knowledge-Based View of the Firm]], [[Learning Curves]], [[Organizational Learning]], [[Tacit vs Explicit Knowledge]], [[Transactive Memory Systems]] — all have empty top-level headings. These appear to be seed stubs.
- [[cherry-picks]] — Tier 1/2/3 sections all empty.
- [[SVG Diagram Style Guide]] — `## Color Palette` section empty.
- [[Linda Argote]], [[Maryam Alavi]] — entity pages with only a heading.
- [[Ar9av-obsidian-wiki]], [[ballred-obsidian-claude-pkm]], [[Claudian-YishenTu]] — `## Key Innovations` / `## Key Features` empty.

---

## Cross-Reference Gaps

No systematic scan run (would require NLP entity extraction). The dead link scan above captures the most obvious gaps. Recommend a targeted pass on the seed-stub pages listed under Empty Sections.

---

## Address Validation

- Counter state (peek): `55`
- Highest `c-` address observed: `c-000054`
- Post-rollout pages checked: 20 (17 passing, 3 errors)
- Legacy pages pending backfill: 21
- Manifest errors: 0 ✅

### Errors

- **ADDRESS COLLISION**: [[Maryam Alavi]] (`wiki/entities/Maryam Alavi.md`) and [[Knowledge Retention]] (`wiki/concepts/Knowledge Retention.md`) both have address `c-000017`. One of these must be re-assigned. Run `./scripts/allocate-address.sh` to get a fresh address, then update the one that was incorrectly set.

- **MISSING ADDRESS** (post-rollout): [[Persistent Wiki Artifact]] (`wiki/concepts/Persistent Wiki Artifact.md`) — created 2026-04-24, address required. Run wiki-ingest or manually run `./scripts/allocate-address.sh` and add to frontmatter.

- **MISSING ADDRESS** (post-rollout): [[Query-Time Retrieval]] (`wiki/concepts/Query-Time Retrieval.md`) — created 2026-04-24, address required.

- **MISSING ADDRESS** (post-rollout): [[Source-First Synthesis]] (`wiki/concepts/Source-First Synthesis.md`) — created 2026-04-24, address required.

### Pending Backfill (informational — 21 legacy pages)

All pages created before 2026-04-23 without addresses. No action required until backfill phase:
claude-obsidian-ecosystem, Wiki vs RAG, cherry-picks, Compounding Knowledge, Hot Cache, LLM Wiki Pattern, Pro Hub Challenge, Search Experience Optimization, Semantic Topic Clustering, SEO Drift Monitoring, SVG Diagram Style Guide, Analytic Reproducibility, DBpedia, HARKing, Knowledge-Based Theory of the Firm, Linked Open Data, Microfoundations, Open Science Framework, Open Science, P-hacking, and others.

---

## Semantic Tiling

Skipped — ollama not reachable at `http://127.0.0.1:11434`. Exit code: 10 (ollama unreachable). Start ollama and run `ollama pull nomic-embed-text` to enable this check.

---

## Recommended Actions

### High priority (errors)
1. Fix **address collision** between [[Maryam Alavi]] and [[Knowledge Retention]] — both have `c-000017`.
2. Assign addresses to 3 post-rollout pages: [[Persistent Wiki Artifact]], [[Query-Time Retrieval]], [[Source-First Synthesis]].
3. Fix dead link `[[hot.md]]` → `[[hot]]` in [[bosco-2020-metabus]].
4. Fix dead link `[[Zahra et al. 2020]]` → `[[zahra-2020-knowledge-integration]]` in [[barney-felin-2013-microfoundations]].
5. Fix dead link `[[LeBel et al. 2018]]` → `[[lebel-2018-credibility-framework]]` in [[nosek-2018-preregistration]].

### Medium priority (review)
6. Create entity stub for **Wolf Vanpaemel** (2 links point to it).
7. Create `Wiki Map.md` stub to resolve 2 dead links + 2 stale index entries.
8. Add content to 8+ empty seed-stub pages (Knowledge Management, Learning Curves, etc.).
9. Auto-fill `created`/`updated` frontmatter on 37 legacy pages.

### Low priority (informational)
10. Remove placeholder links (`[[Foo]]`, `[[notes/Foo]]`, `[[Three laws of motion]]`) from example content.
11. Fix `[[_index]]` wikilink format in `wiki/index.md`.
12. Start ollama + pull `nomic-embed-text` to enable semantic tiling on next lint run.

---

*Should I auto-fix any of these? Safe to auto-fix: missing frontmatter placeholders, simple link corrections, Wolf Vanpaemel stub. Needs review: collision resolution, empty section content.*
