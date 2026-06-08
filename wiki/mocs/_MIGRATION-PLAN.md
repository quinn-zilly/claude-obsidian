---
type: meta
title: "LYT Migration Plan"
created: "2026-06-06"
tags:
  - meta
  - migration
status: proposal
related:
  - "[[Home MOC]]"
updated: 2026-06-06
---

# LYT Migration Plan — proposal (not yet executed)

The vault is now in **LYT mode** (`.vault-meta/mode.json`). Six MOCs exist under `wiki/mocs/` and link to notes **in place** — nothing has been moved. This document proposes how to migrate the existing 409 pages toward the canonical LYT layout. **No files will be moved without your approval.**

## Current vs. target layout

| | Current | LYT target (`mode.json`) |
|---|---|---|
| MOCs | `wiki/mocs/` (new) | `wiki/mocs/` ✓ already correct |
| Atomic notes | `wiki/concepts/`, `wiki/entities/`, `wiki/comparisons/` | `wiki/notes/` (flat) |
| Sources | `wiki/sources/` | keep as-is (sources are raw refs, not atomic notes) |
| Infra | `wiki/meta/`, `wiki/references/`, `wiki/folds/` | keep as-is |

## Recommendation: **don't fully migrate. Adopt a hybrid.**

A pure LYT flat `wiki/notes/` would dump ~490 concept+entity+comparison files into one folder. With MOCs providing navigation, the folders add little friction and moving them risks breaking the ~1000+ existing wikilinks, dataview queries, and the `index.md`/`hot.md` machinery. The valuable half of LYT — MOCs as navigation hubs — is already done.

Three options, least to most disruptive:

### Option A — Hybrid (recommended)
- Keep `concepts/`, `entities/`, `sources/` where they are.
- MOCs (done) are the LYT navigation layer.
- New notes from `wiki-ingest`/`save`/`autoresearch` go to `wiki/notes/` per `mode.json` going forward.
- Result: zero broken links today; LYT conventions apply to new growth.

### Option B — Migrate concepts only
- Move `wiki/concepts/*` → `wiki/notes/`. Leave entities and sources.
- Requires rewriting any links/queries that hard-code the `concepts/` path (most links are bare `[[Title]]`, which survive a move in Obsidian — but dataview `FROM "wiki/concepts"` queries break).
- Steps if you choose this:
  1. Branch/backup: `git checkout -b lyt-migration`
  2. `mkdir -p wiki/notes && git mv wiki/concepts/*.md wiki/notes/`
  3. Grep for path-based references: `grep -rn 'wiki/concepts' wiki .obsidian` and fix dataview/index queries.
  4. Run `lint the wiki` to catch orphans.
  5. Verify in Obsidian that graph + links resolve, then merge.

### Option C — Full flat LYT
- Move concepts + entities + comparisons all into `wiki/notes/`.
- Highest link/query-rewrite cost; only worth it if you want strict LYT purity.
- Same steps as B but across all three folders, plus reconcile name collisions.

## What I'd do next (pending your call)
1. You pick A, B, or C.
2. If B or C: I create a git branch, do the moves, fix path-based queries, run the linter, and report broken links before anything merges.
3. Either way: confirm `index.md` and `hot.md` still resolve and add the Home MOC to the index's navigation line.

## Note on MOC backlinks
The MOCs currently link *out* to notes. For full LYT, notes should also reference their MOC (a `related: [[X MOC]]` line or an inline link). This can be batch-added during whichever migration option you choose, or skipped — Obsidian's backlinks panel already surfaces the MOC from each linked note.
