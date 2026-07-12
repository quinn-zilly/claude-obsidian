---
type: meta
title: "Lint Report 2026-07-11"
created: 2026-07-11
updated: 2026-07-11
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-07-11

## Summary
- Pages scanned: 1205
- Issues found: 32 (across categories below)
- Auto-fixed: 0 (awaiting your go-ahead)
- Needs review: 32

Transport: `filesystem`. Mode: `lyt`. DragonScale addresses: **ON** (counter peek 1193, max observed `c-001192`, no drift, no collisions).

The headline finding is a cluster of **7 template-leak pages** under `wiki/projects/` that were created from the comps-outline template but never filled in — they carry unrendered `<% tp.date.now() %>` Templater syntax, an empty `address:` field, and no inbound links. One root cause explains most of the errors below.

---

## Template Leaks (root cause — HIGH)

These pages still contain literal Templater code instead of rendered values, empty `created`/`updated`/`address`:

- [[Domain 9 - Criterion Theory and Development]]
- [[Domain 10 - Groups & Teams - Q3]]
- [[Domain 13 - Individual Differences - Q1]]
- [[Domain 14 - Job Evaluation]]
- [[Domain 21 - Performance Management]]
- [[Domain 23 - Training]]
- [[Domain 23 - Training - Q2]]

> [!warning] Fix
> Replace `<% tp.date.now("YYYY-MM-DD") %>` with a real date, assign an address via `./scripts/allocate-address.sh`, and link each from its domain MOC. Or, if these are abandoned stubs, delete them.

---

## Address Validation (DragonScale)
- Counter state: 1193
- Highest c- address observed: `c-001192`
- Post-rollout pages checked: 5 errors (missing address)
- Legacy pages pending backfill: 22 (informational)
- Collisions: 0 · Counter drift: 0 · Bad format: 0

### Errors — post-rollout pages missing `address:`
- The 7 template-leak project pages above (empty `address:`).
- [[Personality at Work MOC]] — created 2026-07-11, no address.
- [[Recruitment MOC]] — created 2026-07-11, no address.
- [[Selection & Work Analysis MOC]] — created 2026-07-11, no address.
- [[Social Exchange & Organizational Justice MOC]] — created 2026-06-15, no address.

New MOCs created today skipped address assignment. Run wiki-ingest or `./scripts/allocate-address.sh` and add to frontmatter. (Lint only observes — no auto-assign.)

### Pending backfill (informational)
- 22 legacy pages (created < 2026-04-23) without addresses. Expected.

---

## Orphan Pages (25 — review)

Author entities with no inbound links (likely need linking from co-authored sources or a team MOC):

- [[Bradford S. Bell]], [[Burak Ozkum]], [[Christina Lacerenza]], [[David Sullivan]], [[Deborah DiazGranados]], [[Heidi Baumann]], [[James Beck]], [[Jeffery LePine]], [[John Mathieu]], [[Junhyok Yim]], [[Margaret Toich]], [[Matthew J. Pearsall]]

Concept/source orphans:

- [[Cross-Cultural Communication (Evaluation)]], [[Stakeholder Engagement (Evaluation)]], [[Training Design and Delivery]], [[locke-latham-2002-goal-setting-theory]]

Project orphans (the 7 template leaks) + [[Domain 8 - Career Development]], plus [[_MIGRATION-PLAN]] (probably orphan-by-design).

> [!note]
> `locke-latham-2002-goal-setting-theory` is orphaned as a page yet referenced 15× by full path — see Dead Links. Cross-reference mismatch, not a true orphan.

---

## Dead Links (12 live targets — review)

Dead links inside old lint-reports and folds are excluded as self-referential noise. (An earlier pass flagged 23; on verification, ~11 were aliased links using escaped-pipe `\|` syntax — e.g. `[[Research Resource Identifier (RRID)\|RRIDs]]` — which are **valid**, not broken. The 12 below are genuine.)

**Citation-style links to non-existent pages:**
- `[[Landy & Farr]]` (5×) — [[Performance Appraisal]], [[denisi-murphy-2017-100-years-appraisal]], hot.md
- `[[Murphy & Cleveland]]` (3×) — [[Three Assumptions of Performance Rating]], [[pulakos-2019-evolution-of-pm]]
- `[[Job Demands–Control–Support Model]]` (2×), `[[O*NET]]`, `[[Three laws of motion]]` in [[Persistent Wiki Artifact]]

**Path/config artifacts:**
- `[[dashboard.base]]` in dashboard.md · `[[wiki/comparisons/]]`, `[[questions/]]` in Wiki Map.md · `[[.raw/Morgeson and Humphrey - 2006...]]` in [[morgeson-humphrey-2006-work-design-questionnaire]] · `[[Title]]`, `[[X MOC]]`, `[[wikilinks]]` in template/migration pages

---

## Frontmatter Gaps (6 — low)
Six pages missing one or more required fields (type/status/created/updated/tags). Overlaps heavily with the template-leak set; fixing those clears most.

---

## Fixes applied 2026-07-11 (issues 1–3)

**1. Template leaks — done.** Rendered `<% tp.date.now() %>` to real git-derived dates and assigned addresses to all 7 project pages: [[Domain 9 - Criterion Theory and Development]] `c-001193`, [[Domain 10 - Groups & Teams - Q3]] `c-001194`, [[Domain 13 - Individual Differences - Q1]] `c-001195`, [[Domain 14 - Job Evaluation]] `c-001196`, [[Domain 21 - Performance Management]] `c-001197`, [[Domain 23 - Training]] `c-001198`, [[Domain 23 - Training - Q2]] `c-001199`. Also fixed Q2's empty `title:` and wrong `type: concept` → `comps outline`. [[Domain 8 - Career Development]] addressed `c-001200` and title typo (`Domain8` → `Domain 8`) fixed. No leaks remain.

**2. New MOCs addressed — done.** [[Personality at Work MOC]] `c-001201`, [[Recruitment MOC]] `c-001202`, [[Selection & Work Analysis MOC]] `c-001203`, [[Social Exchange & Organizational Justice MOC]] `c-001204`.

**3. Citation stubs — done.** Created entity stubs [[Landy & Farr]] `c-001205` and [[Murphy & Cleveland]] `c-001206` (recurring foundational appraisal citations). The other flagged targets (`O*NET`, `Job Demands–Control–Support Model`) only appear in running logs (`log.md`/`hot.md`), left untouched by design; `O-NET.md` and `Job Demands-Control Model.md` already exist for live references.

Result: orphans 25 → 0; live dead links 12 → 10 (remaining 10 are folder-links, log/migration artifacts, and doc-example text — not fixable content links). Address counter consistent (peek 1207, max `c-001206`), no collisions, no bad formats.

---

## Recommended fix order
1. **Template leaks** — fill or delete the 7 project pages (clears leaks + 7 address errors + orphans + frontmatter gaps in one pass).
2. **Address the 4 new MOCs** created 2026-06-15/07-11.
3. **Citation stubs** — decide: create pages for `Landy & Farr`, `Murphy & Cleveland`, etc., or unlink (12 dead links).
5. Backfill 22 legacy addresses when convenient (not urgent).
