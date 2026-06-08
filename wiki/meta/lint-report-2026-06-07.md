---
type: meta
title: "Lint Report 2026-06-07"
created: 2026-06-07
updated: 2026-06-07
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-06-07

## Summary
- Pages scanned: 640
- Mode: LYT (hybrid) · DragonScale addresses: ON · Transport: filesystem
- Auto-fixed: 0 (review-first; nothing changed yet)
- Findings by tier: **BLOCKER** 0 · **HIGH** 13 · **MEDIUM** ~75 · **LOW** ~235

Healthy overall: only 2 orphans, 0 address-format errors, 0 address collisions, 1 (expected) duplicate filename. The real maintenance debt is frontmatter gaps and 13 post-rollout pages missing DragonScale addresses.

---

## HIGH — Post-Rollout Pages Missing Address (DragonScale)

Per the skill, post-rollout pages (`created >= 2026-04-23`, non-meta/fold) **must** carry a `c-NNNNNN` address. These 13 lack one. This is the silent-regression path the mechanism exists to catch — recent ingests skipped address assignment.

- [[Culture & IT MOC]] — created 2026-06-07
- [[Home MOC]] — created 2026-06-06
- [[Institutional & Strategy MOC]] — created 2026-06-06
- [[Knowledge Management MOC]] — created 2026-06-06
- [[Learning & Development MOC]] — created 2026-06-06
- [[Open Science MOC]] — created 2026-06-06
- [[Teams & Org Behavior MOC]] — created 2026-06-06
- [[ideal-km-system-academic-research]] — created 2026-06-07
- [[knowledge-management-academic-science-problems-solutions]] — created 2026-06-07
- `wiki/meta/tiling-report-2026-04-24.md` — no `created` (treated post-rollout)
- [[Book recommendations]] — no `created`
- [[methodology-modes]] — no `created`
- [[transport-fallback]] — no `created`

> [!note] The 7 MOCs are arguably meta/navigation. If MOCs should be address-exempt in LYT mode, add `wiki/mocs/` to the exclusion set or list them in `.vault-meta/legacy-pages.txt`. Otherwise run `./scripts/allocate-address.sh` per page. Counter peek = **620**, highest observed `c-` = **c-000619**: consistent, no drift.

---

## MEDIUM — Frontmatter Gaps (47 pages)

Missing one or more required fields (`type`, `status`, `created`, `updated`, `tags`). Safe to auto-fill `created`/`updated` from git history and add placeholder `status: seed`.

Most common gap is `created` (28 pages). Pages missing the structural `type` field (higher priority):

- [[Competency Modelling]], [[KSA Framework]], [[Miles and Snow Strategic Typology]], [[Strategic Job Analysis (SJA)]] — missing `type`, `status`, `created`
- [[Integrated Model of Training Evaluation and Effectiveness (IMTEE)]], [[Return on Development Investment (RODI)]] — missing `type`
- [[Kimberly A. Smith-Jentsch]] — missing `type`
- [[Book recommendations]] — missing all five fields
- [[Singh-2008-Job-Analysis-Changing-Workplace]], [[alvarez-et-al-2004-training-evaluation-effectiveness]], [[avolio-et-al-2010-ROI-leadership-development]], [[smith-jentsch-2020-smart-investments-training]] — missing `type`

The 7 MOCs all miss `status` + `updated`. Full per-page list in the analysis log; remaining 33 are `created`-only or `updated`-only gaps.

---

## MEDIUM — Missing Pages (multi-referenced)

Names linked from 3+ distinct pages with no page of their own — strong candidates for a real page or a deliberate stub:

- **claude-obsidian-ecosystem** — referenced by 7 entity/source pages (Ar9av, Claudian, Nexus, ballred, kepano, rvk7895, the ecosystem source). This looks like an intended hub/MOC. Suggest creating it.
- **Pro Hub Challenge** — referenced by 6 pages (Claude SEO entity, SEO concepts, index). Either create the page or fix the links.
- **LeBel et al. 2018**, **Zahra et al. 2020**, **Kogut & Zander**, **Munafò et al. 2017**, **Nosek et al. 2012 – Scientific Utopia II** — citation-style links to source pages that don't exist under those exact names. Likely should point at existing `wiki/sources/` files; reconcile names.

---

## MEDIUM — Dead Links (28 actionable, 256 total)

Of 256 unresolved wikilinks, 96 resolve by path/segment (LYT `_index` pattern — benign) and 132 sit inside historical lint reports and fold pages (frozen records — leave them). The **28 actionable** dead links in live pages:

- [[Wiki Map]] → `questions/`, `wiki/comparisons/` (folder links, not notes — drop or point at an index)
- [[DragonScale Memory]] → `Foo`, `notes/Foo` (placeholder text left in)
- [[Open Science 2.0]] → `Research Resource Identifier (RRID)\` and [[thibault-2023-open-science-2-0]] → `Big Team Science\`, `RRID\` — **trailing backslash** breaking the link; strip the `\`
- [[Persistent Wiki Artifact]] → `Three laws of motion` (stray example link)
- [[dashboard]] → `dashboard.base` (Obsidian Base file, not a note — expected if `.base` not yet created)
- [[methodology-modes]] → `methodology-modes-guide`, `wiki-mode`; [[transport-fallback]] → `mcp-setup`, `wiki-cli` (these point at plugin docs/skills, not vault notes — convert to regular links or create reference stubs)
- The `claude-obsidian-ecosystem` and `Pro Hub Challenge` links above (also counted under Missing Pages).

---

## LOW — Empty Sections (235 headings across pages)

Headings with no body beneath them. Mostly source-page templates with unfilled sections (`## Key Quotes`, `## Connections`). Top offenders: [[cherry-picks]], [[Transactive Memory Systems]], [[nosek-2012-scientific-utopia-ii]], [[ren-argote-2011-tms]] (4 each). Not urgent; fill during normal ingest, or trim the template if sections are routinely empty.

---

## Orphan Pages (2)

- [[methodology-modes]]: no inbound links. Suggest linking from a references index or [[Home MOC]].
- [[transport-fallback]]: no inbound links. Same suggestion.

Both are reference docs; near-orphan-by-design but worth one inbound link each.

---

## Duplicate Filenames (1, benign)

- `_index.md` exists in `concepts/`, `entities/`, `sources/`. Expected for the LYT-hybrid per-folder index pattern. Bare `[[_index]]` links are ambiguous — use `[[concepts/_index]]` form (already the case where it matters).

---

## Address Validation (DragonScale)

- Counter state (peek): **620**
- Highest `c-` address observed: **c-000619** (consistent — no counter drift)
- Format errors: **0** · Collisions: **0**
- Post-rollout pages missing address: **13** (see HIGH section)
- Legacy pages pending backfill: **22** (informational — `created < 2026-04-23`)
- `.raw/.manifest.json` present (82 KB); address-map spot-check passed.

---

## Semantic Tiling

**Skipped** — `scripts/tiling-check.py --peek` exited 127 (interpreter/ollama not reachable in this environment). No duplicate-page detection this run. To enable: ensure `ollama` is running and `ollama pull nomic-embed-text`, then re-run lint.

---

## Recommended Fix Order

1. Assign addresses to the 13 post-rollout pages (or exempt MOCs) — closes the only HIGH finding.
2. Strip trailing `\` from the RRID / Big Team Science links — 1-character fixes, real broken links.
3. Decide on `claude-obsidian-ecosystem` and `Pro Hub Challenge` — create pages or fix links.
4. Backfill `type` on the ~12 pages missing it, then `created`/`updated` from git for the rest.
5. Empty sections and legacy-address backfill — opportunistic, low priority.
