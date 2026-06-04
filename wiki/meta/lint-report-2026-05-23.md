---
type: meta
title: "Lint Report 2026-05-23"
created: 2026-05-23
updated: 2026-05-23
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-05-23

## Summary

- Pages scanned: 239
- Issues found: 188
- Auto-fixed: 0
- Needs review: 188

---

## 1. Orphan Pages

Pages with no inbound wikilinks. Everything else is well-connected.

- [[Norbert-Kerr]]: no inbound links. Note: `[[Norbert Kerr]]` (with space) is linked from 9 pages but resolves to a missing page — the actual file uses a hyphen. Suggest: rename file to `Norbert Kerr.md` to match link targets, then all 9 dead links will resolve automatically.

**Total orphans: 1**

---

## 2. Dead Links

Links pointing to pages that do not exist. Filtered to non-meta pages. Highest-priority entries listed.

### Structural / navigation dead links
- `[[Wiki Map.canvas]]` in [[Wiki Map]], [[lint-report-2026-05-20]], [[lint-report-2026-05-21]]: canvas file referenced but not a wiki page — not a real issue.
- `[[wiki/comparisons/]]`, `[[questions/]]` in [[Wiki Map]]: folder links — Obsidian doesn't support these as wikilinks.
- `[[dashboard.base]]` in [[dashboard]]: `.base` files aren't `.md` — not a real dead link.
- `[[hot.md]]` in [[index]], [[lint-report-2026-05-21]]: using `.md` suffix in wikilinks doesn't work in Obsidian. Suggest: change to `[[hot]]`.

### Concept stubs needed (see also Section 4)
- `[[Social Cognitive Theory]]`: linked from 7 pages — no page exists.
- `[[Replication]]`: linked from 4 pages — no page exists (distinct from [[Replication Crisis]]).
- `[[Nosek et al. 2012 - Scientific Utopia II]]`: linked from 4 pages — the source page is `[[nosek-2012-scientific-utopia-ii]]`. Suggest: add an alias or update links.
- `[[Testing Effect]]`, `[[New Theory of Disuse]]`, `[[Judgment of Learning]]`: each linked from 3 pages.
- `[[Transfer of Training]]`, `[[Self-Directed Learning]]`: each linked from 3 pages.
- `[[Norbert Kerr]]`: linked from 9 pages but file is `Norbert-Kerr.md` — rename file (see Orphans above).
- `[[clinicaltrials.gov]]`: linked from 3+ pages — minor; this is an external resource, not a wiki concept.

### Citation-style dead links (old short-form citations)
These are informal citation wikilinks that should either be removed or replaced with proper source page links:
- `[[Yarkoni & Westfall 2017]]` → should be `[[yarkoni-westfall-2017-prediction-vs-explanation]]`
- `[[Giner-Sorolla 2012]]` → should be `[[giner-sorolla-2012-science-or-art]]`
- `[[Munafò et al. 2017]]` → should be `[[munafo-2017-manifesto]]`
- `[[LeBel et al. 2018]]` → should be `[[lebel-2018-credibility-framework]]`
- `[[Zahra et al. 2020]]` → should be `[[zahra-2020-knowledge-integration]]`
- `[[Open Science Collaboration (2015)]]` → should be `[[open-science-collaboration-2015]]`
- `[[Kogut & Zander]]`: no source page for this; stub or remove.

### Entity dead links (people without pages)
- `[[Robert A. Bjork]]`, `[[Kurt Kraiger]]`, `[[J. Kevin Ford]]`: researchers linked from sources but no entity pages.
- `[[Bita Fayaz-Farkhad]]`, `[[Javier A. Granados Samayoa]]`: co-authors on Albarracín paper, no pages.

### Broken internal references (test artifacts)
- `[[Foo]]` / `[[notes/Foo]]`: appears in [[DragonScale Memory]], [[log]], and several lint reports — these are test stubs from DragonScale development. Suggest: remove these links from concept and log pages.

**Total pages with dead links: 38 (excluding meta/lint-report pages)**

---

## 3. Stale Claims

No explicit contradictions detected between pages in this scan. The vault is relatively young and sources are primary. Recommend running a targeted review when new sources contradict older synthesis pages.

*No stale claim issues flagged.*

---

## 4. Missing Pages

Concepts or entities mentioned in 2+ pages but lacking their own wiki page. Highest-priority candidates:

| Missing Page | Mentions | Suggest |
|---|---|---|
| Social Cognitive Theory | 7 | Create concept stub |
| Norbert Kerr | 9 (dead links) | Rename `Norbert-Kerr.md` → `Norbert Kerr.md` |
| Replication | 4 | Create concept stub (distinct from [[Replication Crisis]]) |
| Testing Effect | 3 | Create concept stub |
| New Theory of Disuse | 3 | Create concept stub |
| Judgment of Learning | 3 | Create concept stub |
| Transfer of Training | 3 | Create concept stub |
| Self-Directed Learning | 3 | Create concept stub |
| Synthetic Learning Environments | 2 | Create concept stub |
| Open Data | 2 | Create concept stub |
| File-Drawer Problem | 2 | Create concept stub or alias to [[Publication Bias]] |
| Robert A. Bjork | 2 | Create entity stub |
| Kurt Kraiger | 2 | Create entity stub |
| J. Kevin Ford | 2 | Create entity stub |
| Open Science Collaboration (2015) | 2 | Alias to [[open-science-collaboration-2015]] |

**Total priority missing pages: 27**

---

## 5. Missing Cross-References

Pages that mention a concept by name in prose but don't link to it.

- [[Replication Crisis]] mentions "p-hacking" but doesn't link `[[P-hacking]]`.
- [[Publication Bias]] likely mentions "file-drawer problem" — suggest adding `[[File-Drawer Problem]]` stub or alias.
- [[HARKing]] mentions "Norbert Kerr" in prose without a wikilink (all links use the broken hyphenated form).
- [[Transactive Memory Systems]]: mentions many sub-concepts (Team Mental Models, Shared Mental Models, etc.) in prose that each deserve their own links once pages exist.

*These are secondary priority; address after resolving missing page stubs.*

---

## 6. Frontmatter Gaps

97 pages are missing one or more required frontmatter fields. The `updated` field is the most common gap (94 pages). 5 pages are missing `type` and `status` as well.

### Pages missing `type`, `status`, AND `updated` (highest priority):
- [[Conflict of Interest in Science]]: missing `type`, `status`, `updated`
- [[Motivated Reasoning]]: missing `type`, `status`, `updated`
- [[Open Workflow]]: missing `type`, `status`, `updated`
- [[Paradigm-Driven Research]]: missing `type`, `status`, `updated`
- [[ren-argote-2011-tms]]: missing `type`, `status`, `updated`
- [[nosek-2012-scientific-utopia-ii]]: missing `status`, `updated`
- [[Spacing Effect]]: missing ALL fields (`type`, `status`, `created`, `updated`, `tags`)

### Pervasive gap: `updated` field
94 concept, entity, and source pages are missing the `updated` field. This field was likely not included in the original ingest templates. Safe to auto-fill with `created` date as the initial value.

**Total pages with frontmatter gaps: 97**

> Safe to auto-fix: Add `updated: <created date>` to all pages missing only `updated`. Recommend review before adding `type`/`status` to pages missing those fields.

---

## 7. Empty Sections

79 pages have headings with no content beneath them. These are mostly source and concept pages where sections were scaffolded but not yet populated.

### High-priority empties (core source pages):
- [[nosek-2012-scientific-utopia-ii]]: 4 empty sections including "Problems with Current Practices" and "Solutions"
- [[ren-argote-2011-tms]]: 4 empty sections including "Key Contributions" and "Four Key Research Directions"
- [[Transactive Memory Systems]]: 4 empty sections including the page title heading
- [[fulmer-2023-compensation-performance]]: 3 empty sections
- [[micelotta-2017-pathways-institutional-change]]: 2 empty sections

### Low-priority / intentional stubs (single top-level empty heading):
Many concept pages (e.g., [[Base Rate Neglect]], [[Gambler's Fallacy]], [[Glass Cliff]], etc.) have a top-level heading with no body — these appear to be stubs. Total stub-style empties: ~30 pages.

**Total pages with empty sections: 79**

---

## 8. Stale Index Entries

`wiki/index.md` contains 3 links pointing to non-existent pages:

- `[[motivated reasoning]]`: should be `[[Motivated Reasoning]]` (case mismatch — the page exists as `Motivated Reasoning.md`)
- `[[clinicaltrials.gov]]`: external resource linked in index; no wiki page will ever exist for this — suggest removing or converting to a plain URL.
- `[[Norbert Kerr]]`: page exists as `Norbert-Kerr.md` — will resolve once file is renamed (see Orphans).

**Total stale index entries: 3**

---

## 9. Address Validation (DragonScale)

DragonScale detected (`allocate-address.sh` + `address-counter.txt` present).

- Counter state (peek): `207`
- Highest `c-` address observed: `c-000206`
- Post-rollout pages checked: all passing (0 missing addresses)
- Legacy pages pending backfill: **21**

### Errors

- [[ren-argote-2011-tms]] and [[DragonScale Memory]] share address `c-000001`. This is a duplicate address — one of these must be reassigned. Run `./scripts/allocate-address.sh` to get a new address and update the frontmatter of one page.

### Pending backfill (informational)

21 legacy pages (created before 2026-04-23) have no `address:` field. These are backfill-eligible and do not require immediate action. Use `l-NNNNNN` format when backfilling.

---

## 10. Semantic Tiling

Skipped — ollama not reachable (exit code 10). `nomic-embed-text` model not present at `http://127.0.0.1:11434`.

To enable: run `ollama serve` and `ollama pull nomic-embed-text`, then re-run lint.

---

## Recommended Actions (Priority Order)

1. **Rename `Norbert-Kerr.md` → `Norbert Kerr.md`** — fixes 1 orphan + 9 dead links + 3 stale index entries at once.
2. **Fix duplicate address `c-000001`** — reassign either [[ren-argote-2011-tms]] or [[DragonScale Memory]].
3. **Auto-fill `updated` field** on 94 pages missing only that field — safe to auto-fix.
4. **Fix case in index**: `[[motivated reasoning]]` → `[[Motivated Reasoning]]`.
5. **Create stubs** for top missing pages: Social Cognitive Theory, Replication, Testing Effect, New Theory of Disuse, Transfer of Training, Self-Directed Learning.
6. **Fix citation-style dead links** in concept and source pages (replace short-form citations with source page wikilinks).
7. **Populate empty sections** in high-priority source pages (nosek-2012-scientific-utopia-ii, ren-argote-2011-tms, Transactive Memory Systems).
8. **Remove `[[Foo]]` / `[[notes/Foo]]` links** from [[DragonScale Memory]] and [[log]] — these are test artifacts.

---

*Report generated by wiki-lint on 2026-05-23. Previous reports: [[lint-report-2026-05-21]], [[lint-report-2026-05-20]], [[lint-report-2026-05-19]].*
