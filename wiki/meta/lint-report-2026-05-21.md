---
type: meta
title: "Lint Report 2026-05-21"
created: 2026-05-21
updated: 2026-05-21
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-05-21

Nav: [[dashboard]] | [[index]] | [[log]]

## Summary

- Pages scanned: 156
- Dead-link targets: 91 unique (see breakdown below — most are expected)
- Orphan pages: 4 (all meta/system — expected)
- Frontmatter gaps: 6 pages missing `type` and/or `status`
- Address validation: ✅ no errors (no duplicates, no bad format, no missing on post-rollout pages)
- Semantic tiling: skipped (Python not installed)
- Issues needing action: **16** (8 dead links, 6 frontmatter gaps, 2 link-casing fixes)
- Note: Soderstrom & Bjork (2015) ingest was **interrupted** by this lint run; 3 of 9 planned pages created so far

---

## Orphan Pages

All orphans are intentional meta/system files:

- `[[2026-04-10-backlink-empire-session]]` — meta session note, no inbound links (expected)
- `[[lint-report-2026-05-20]]` — prior lint report (expected; consider linking from dashboard)
- `[[tiling-report-2026-04-24]]` — tiling output (expected)
- `[[fold-k3-from-2026-04-23-to-2026-04-24-n8]]` — fold page (expected)

**Verdict:** No action needed.

---

## Dead Links (Actionable)

### Missing pages from incomplete ingest (Soderstrom & Bjork 2015)

These 7 pages were planned but not yet created. Will be resolved when ingest resumes.

| Dead link | Referenced in |
|---|---|
| `[[Spacing Effect]]` | soderstrom-bjork-2015, Learning vs Performance Distinction, Desirable Difficulties |
| `[[Testing Effect]]` | same 3 pages |
| `[[New Theory of Disuse]]` | same 3 pages |
| `[[Judgment of Learning]]` | same 3 pages |
| `[[Illusions of Competence]]` | Learning vs Performance Distinction |
| `[[Robert A. Bjork]]` | soderstrom-bjork-2015, Desirable Difficulties |
| `[[Nicholas C. Soderstrom]]` | soderstrom-bjork-2015 |

**Action:** Resume ingest — create remaining 6 pages (Spacing Effect, Testing Effect, New Theory of Disuse, Judgment of Learning, Robert A. Bjork, Nicholas C. Soderstrom). Illusions of Competence can fold into Judgment of Learning.

### Missing entity pages (pre-existing gap)

| Dead link | Referenced in | Notes |
|---|---|---|
| `[[Wolf Vanpaemel]]` | Etienne LeBel, lebel-2018, lint-2026-05-20 | Flagged in hot.md as pending |
| `[[Kurt Kraiger]]` | Science of Workplace Instruction, kraiger-ford-2021 | Co-author of ingested source |
| `[[J. Kevin Ford]]` | same 2 pages | Co-author of ingested source |

**Action:** Create stubs for Wolf Vanpaemel, Kurt Kraiger, J. Kevin Ford.

### Missing concept pages (pre-existing gap)

| Dead link | Referenced in | Priority |
|---|---|---|
| `[[Knowing-Doing Gap]]` | kraiger-ford-2021, soderstrom-bjork-2015 | Medium — cross-referenced across domains |
| `[[Organizational Memory]]` | ren-argote-2011-tms | Low — granular TMS concept |

**Action:** Create stubs for Knowing-Doing Gap (medium priority), Organizational Memory (low).

### TMS over-granular stubs (ren-argote-2011-tms only)

These concepts are referenced only in the TMS source page and represent granular sub-concepts unlikely to need their own pages at current wiki scale. Suggest removing wikilinks and using plain text instead.

`[[Group Training]]`, `[[Group Performance]]`, `[[Shared Experience]]`, `[[Task Coordination]]`, `[[Task Credibility]]`, `[[Team Familiarity]]`, `[[Team Reflexivity]]`, `[[Member Personality]]`, `[[Member Turnover]]`, `[[Memory Differentiation]]`, `[[Team Mental Models]]`, `[[Shared Mental Models]]`, `[[Team Cognition]]`, `[[Team Learning]]`, `[[Team Creativity]]`, `[[Team Member Satisfaction]]`, `[[Metaknowledge]]`, `[[Knowledge Specialization]]`, `[[Transactive Memory]]` (bare, vs `[[Transactive Memory Systems]]`)

**Action:** Propose: remove wikilinks from ren-argote-2011-tms for these granular stubs; keep plain text. Ask before auto-fixing.

---

## Link Casing / Format Errors (Easy Fixes)

| Current link | Correct link | Location |
|---|---|---|
| `[[motivated reasoning]]` | `[[Motivated Reasoning]]` | wiki/index.md |
| `[[nosek-bar-anan-2012-scientific-utopia-ii]]` | `[[nosek-2012-scientific-utopia-ii]]` | nosek-bar-anan-2012-scientific-utopia-i.md |

**Action:** Fix both. Safe to auto-fix.

---

## Source Citation Format Issues (Informational)

Several pages use verbose citation strings as wikilinks instead of slugs. These are dead links but low impact since they're in source/reference sections:

- `[[Zahra et al. 2020]]` → `[[zahra-2020-knowledge-integration]]`
- `[[LeBel et al. 2018]]` → `[[lebel-2018-credibility-framework]]`
- `[[Munafò et al. 2017]]` → `[[munafo-2017-manifesto]]`
- `[[Open Science Collaboration 2015]]` → `[[open-science-collaboration-2015]]`
- `[[Nosek and Bar-Anan 2012 - Scientific Utopia I]]` → `[[nosek-bar-anan-2012-scientific-utopia-i]]`
- `[[Nosek et al. 2012 - Scientific Utopia II]]` → `[[nosek-2012-scientific-utopia-ii]]`
- `[[Argote, Linda]]` → `[[Linda Argote]]` (in some source pages)

Not blocking; fix during next ingest round.

---

## Dead Links (Expected / Spurious — No Action)

These are either system references, canvas files, external URLs, or links from older Claude SEO sessions:

- `[[Wiki Map.canvas]]`, `[[dashboard.base]]`, `[[dashboard.md]]`, `[[hot.md]]` — system refs
- `[[concepts/_index]]`, `[[entities/_index]]`, `[[sources/_index]]` — index files (Obsidian resolves these fine)
- `[[AI Marketing Hub Cover Images Canvas]]`, `[[Claude Canvas]]`, `[[Claude Obsidian]]`, `[[Rankenstein]]` — SEO session artifacts
- `[[E-commerce SEO]]`, `[[Three laws of motion]]`, `[[Karpathy LLM Wiki Pattern]]` — SEO session
- `[[clinicaltrials.gov]]`, `[[PLoS ONE]]`, `[[Obsidian]]` — external refs, not pages
- `[[Scientific Utopia]]`, `[[Self-Directed Learning]]`, `[[Transfer of Training]]`, `[[Synthetic Learning Environments]]` — series name / concepts from kraiger source (not linked from multiple places)
- `[[Buckheit & Donoho (1995)]]`, `[[Bastardi, Uhlmann, & Ross (2011)]]`, `[[Simmons, Nelson, & Simonsohn 2011]]`, `[[Schooler 2011]]`, `[[John, Loewenstein, & Prelec 2012]]` — inline citations, not pages
- `[[fold-template]]`, `[[wiki-fold]]`, `[[wikilinks]]`, `[[Foo]]`, `[[notes/Foo]]`, `[[questions/]]` — dev artifacts

---

## Frontmatter Gaps

Six pages missing required fields:

| Page | Missing |
|---|---|
| `wiki/concepts/Conflict of Interest in Science.md` | `type`, `status` |
| `wiki/concepts/Motivated Reasoning.md` | `type`, `status` |
| `wiki/concepts/Open Workflow.md` | `type`, `status` |
| `wiki/concepts/Paradigm-Driven Research.md` | `type`, `status` |
| `wiki/sources/ren-argote-2011-tms.md` | `type`, `status` |
| `wiki/sources/nosek-2012-scientific-utopia-ii.md` | `status` |

All were created in the 2026-05-19 to 2026-05-21 batch ingests before the `type`/`status` frontmatter standard was fully enforced. Safe to auto-fix (add `type: concept` / `type: source` and `status: developing`).

**Action:** Add missing fields. Safe to auto-fix — ask before proceeding.

---

## Stale Claims

No contradictions detected between pages. One potential staleness flag:

- `[[hot.md]]` still lists "Pages: 135" and "Sources: 24" — the Soderstrom ingest is in progress and these counts will be outdated. Update after ingest completes.

---

## Address Validation (DragonScale Mechanism 2)

- Counter state (next to allocate): `c-000125`
- Highest c- observed: `c-000118` (on Desirable Difficulties — xargs/spaces bash issue prevented seeing c-000117/118 in initial scan, verified by direct grep)
- Post-rollout pages checked: 31 addressed pages — **all passing**
- Duplicate addresses: **none**
- Bad format addresses: **none**
- Counter drift: **none** (c-000118 < c-000125)
- Legacy pages pending backfill: many (pre-2026-04-23 pages, expected)

Note: Addresses c-000119 through c-000124 were reserved during the interrupted Soderstrom ingest. 6 pages not yet created will need those addresses when ingest resumes.

**Verdict:** ✅ No address errors.

---

## Semantic Tiling

**Skipped** — `python3` resolves to Windows Store stub (not a real installation). Install Python 3 to enable.

---

## Recommended Actions (in priority order)

1. **Resume Soderstrom & Bjork ingest** — create 6 remaining pages (Spacing Effect, Testing Effect, New Theory of Disuse, Judgment of Learning, Robert A. Bjork, Nicholas C. Soderstrom)
2. **Fix 2 link-casing errors** — `[[motivated reasoning]]` and wrong Nosek slug (safe to auto-fix)
3. **Fix 6 frontmatter gaps** — add `type`/`status` to 6 pages (safe to auto-fix)
4. **Create 3 entity stubs** — Wolf Vanpaemel, Kurt Kraiger, J. Kevin Ford
5. **Create Knowing-Doing Gap concept page** — linked from 2 domains
6. **Clean TMS over-granular links** — remove wikilinks for 19 micro-concepts in ren-argote (review first)
7. **Update hot.md counts** after ingest completes
