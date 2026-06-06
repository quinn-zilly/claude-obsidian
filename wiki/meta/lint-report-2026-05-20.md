---
type: meta
title: "Lint Report 2026-05-20"
created: 2026-05-20
updated: 2026-05-20
tags:
  - meta
  - lint
status: developing
---

# Lint Report: 2026-05-20

## Summary

- Pages scanned: 111
- Issues found: 9 (2 errors, 7 informational/low-priority)
- Auto-fixed: 0
- Needs review: 2

---

## Dead Links

These wikilinks appear in wiki pages but have no matching page file. Grouped by severity:

**Genuine missing pages (worth creating):**

- `[[Kogut & Zander]]` — referenced in [[grant-1996-knowledge-based-theory]] and [[lint-report-2026-05-19]]. Kogut & Zander (1992) is a foundational KM source. Suggest: create a source stub or concept page.
- `[[nosek-bar-anan-2012-scientific-utopia-ii]]` — referenced in [[nosek-bar-anan-2012-scientific-utopia-i]]. The source page was written expecting its companion to exist. Will be created when Utopia II is ingested.
- `[[Replication]]` — referenced in [[Etienne LeBel]] and [[lebel-2018-credibility-framework]]. Likely meant to link to [[Replication Crisis]] or a new concept page for replication as a method. Suggest: replace links with `[[Replication Crisis]]` or create a redirect/stub.

**File-type / infrastructure links (not real wiki pages):**

- `[[Wiki Map.canvas]]` — referenced in [[Wiki Map]]. Obsidian canvas file; if it exists on disk it's fine. Not a broken wiki page.
- `[[dashboard.base]]` — Obsidian Bases file; referenced in [[dashboard]] and prior lint reports. Non-markdown artifact.
- `[[fold-template]]` — referenced in fold page and prior lint report. Fold template file, not a wiki page.

**Legacy / session-specific dead links (in old meta/session pages):**

- `[[AI Marketing Hub Cover Images Canvas]]`, `[[Claude Canvas]]`, `[[Claude Obsidian]]`, `[[E-commerce SEO]]`, `[[Karpathy LLM Wiki Pattern]]`, `[[Rankenstein]]`, `[[claude-obsidian-presentation]]` — all in `wiki/meta/` session notes from 2026-04. These are historical references to assets that no longer exist or were renamed. Low priority; meta pages are not expected to be fully live.
- `[[Three laws of motion]]`, `[[Foo]]`, `[[notes/Foo]]` — example/placeholder links from [[DragonScale Memory]] and log; used for illustration. Ignore.
- `[[hot.md]]`, `[[wikilinks]]`, `[[LeBel et al. 2018]]`, `[[Zahra et al. 2020]]` — appear only in prior lint report (`lint-report-2026-05-19`), not in live wiki pages.
- `[[How does the LLM Wiki pattern work?]]` (with `?`) — referenced in [[Persistent Wiki Artifact]], [[Query-Time Retrieval]], [[Source-First Synthesis]]. The actual page is [[How does the LLM Wiki pattern work]] (no `?`). **Fix:** remove the trailing `?` from these three wikilinks.

**Actionable count: 3 genuine missing pages, 1 wikilink typo to fix.**

---

## Orphan Pages

None. All non-meta wiki pages have at least one inbound wikilink.

---

## Frontmatter Gaps

None. All scanned pages pass the required-fields check (type, status, created, updated, tags).

---

## Missing Pages

The following concepts or people are mentioned in multiple wiki pages without a dedicated page:

- **Kogut & Zander (1992)** — mentioned in [[grant-1996-knowledge-based-theory]]; foundational KM paper ("Knowledge of the Firm, Combinative Capabilities, and the Replication of Technology"). Low urgency until a KM source batch ingest includes it.
- **Wolf Vanpaemel** — has a page ([[Wolf Vanpaemel]]) but it is marked `status: seed` and is missing an address (see Address Validation below). Page exists and is linked; no action needed beyond address assignment.

---

## Cross-Reference Gaps

- [[Replication]] linked from [[Etienne LeBel]] and [[lebel-2018-credibility-framework]] should resolve to [[Replication Crisis]] — update those two links.

---

## Empty Sections

The empty-section scan produced many false positives (H1 page-title headings, subsections with content on the next line that the regex missed). Genuine stub pages with empty body content after the H1:

No pages with a completely empty body after the H1 were found. Some pages (e.g., [[Knowledge Retention]], [[Transactive Memory Systems]]) have solid content. The false-positive sections were caused by the detection script — not actual content gaps.

One genuine stub to note: `[[How does the LLM Wiki pattern work]]` — the page exists but is marked `status: developing` and has sparse content. Not a blocker.

---

## Stale Claims

No direct contradictions detected in this pass. One potential area to watch:

- [[Knowledge-Based View of the Firm]] (Alavi & Leidner) and [[Knowledge-Based Theory of the Firm]] (Grant 1996) are closely related but distinct. Both pages currently treat these as separate. The distinction is correct — KBV is Penrose/Kogut/Zander-lineage; KBT is Grant's specific integration-mechanism framework. No stale claim, but the two pages should cross-link more explicitly.

---

## Address Validation

- **Counter state:** peek = 68
- **Highest c- address observed:** c-000067
- **Post-rollout pages checked:** all pages with `created:` ≥ 2026-04-23
- **Counter consistency:** all observed `c-NNNNNN` satisfy NNNNNN < 68 ✓
- **Uniqueness:** no collisions ✓
- **Address-map consistency:** all 63 `address_map` entries match their page frontmatter ✓

### Errors

- **[[Wolf Vanpaemel]]**: missing address. Page `created: 2026-05-19` (post-rollout). Address required. Run `./scripts/allocate-address.sh` and add to frontmatter and manifest `address_map`.

### Pending backfill (informational — 21 legacy pages)

These pages predate the 2026-04-23 DragonScale rollout. Addresses not required until a deliberate backfill pass.

  - [[Andrej Karpathy]] (created: 2026-04-07)
  - [[Ar9av-obsidian-wiki]] (created: 2026-04-08)
  - [[ballred-obsidian-claude-pkm]] (created: 2026-04-08)
  - [[cherry-picks]] (created: 2026-04-08)
  - [[Claude SEO]] (created: 2026-04-14)
  - [[Claudian-YishenTu]] (created: 2026-04-08)
  - [[claude-obsidian-ecosystem]] (created: 2026-04-08)
  - [[claude-obsidian-ecosystem-research]] (created: 2026-04-08)
  - [[Compounding Knowledge]] (created: 2026-04-07)
  - [[Hot Cache]] (created: 2026-04-07)
  - [[How does the LLM Wiki pattern work]] (created: 2026-04-07)
  - [[kepano-obsidian-skills]] (created: 2026-04-08)
  - [[LLM Wiki Pattern]] (created: 2026-04-07)
  - [[Nexus-claudesidian-mcp]] (created: 2026-04-08)
  - [[Pro Hub Challenge]] (created: 2026-04-14)
  - [[rvk7895-llm-knowledge-bases]] (created: 2026-04-08)
  - [[SEO Drift Monitoring]] (created: 2026-04-14)
  - [[SVG Diagram Style Guide]] (created: 2026-04-14)
  - [[Search Experience Optimization]] (created: 2026-04-14)
  - [[Semantic Topic Clustering]] (created: 2026-04-14)
  - [[Wiki vs RAG]] (created: 2026-04-07)

---

## Semantic Tiling

Skipped: ollama not reachable (exit 10). Run `ollama serve` and `ollama pull nomic-embed-text` to enable.

---

## Recommended Actions

**Errors (fix before next ingest):**

1. **Assign address to [[Wolf Vanpaemel]]** — post-rollout page missing address. Run `./scripts/allocate-address.sh`, add `address: c-000068` to frontmatter, update `address_map` in manifest.
2. **Fix `?` in three wikilinks** — [[Persistent Wiki Artifact]], [[Query-Time Retrieval]], [[Source-First Synthesis]] all link to `[[How does the LLM Wiki pattern work?]]`; should be `[[How does the LLM Wiki pattern work]]`.

**Low-priority suggestions (next maintenance pass):**

3. Fix `[[Replication]]` → `[[Replication Crisis]]` in [[Etienne LeBel]] and [[lebel-2018-credibility-framework]].
4. Add cross-links between [[Knowledge-Based View of the Firm]] and [[Knowledge-Based Theory of the Firm]] to clarify their relationship.
5. Create [[nosek-bar-anan-2012-scientific-utopia-ii]] source page when Utopia II is ingested.
6. Consider stub for [[Kogut & Zander]] if KM source batch expands.
