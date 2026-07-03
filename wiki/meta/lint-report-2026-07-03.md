---
type: meta
title: "Lint Report 2026-07-03"
created: 2026-07-03
updated: 2026-07-03
tags:
  - meta
  - lint
status: developing
---

# Lint Report: 2026-07-03

Transport: filesystem. Mode: LYT (hybrid). DragonScale addresses: ON.

## Corrections (post-verification, 2026-07-03)

After verifying each flagged item against the filesystem, most findings below were **false positives** from an initial scan that only looked inside `wiki/`. Verified reality:

- **Tags gap (254 pages): NOT REAL.** Those pages already carry `tags:` as a YAML list; the scanner misread the empty inline value on the `tags:` header line. Only two pages genuinely lacked tags: `retrieval-benchmark-v1.7.md` (fixed — tags added) and `tiling-report-2026-04-24.md` (has no frontmatter at all — still open).
- **5 "doc-name" links: NOT DEAD.** They point at real files in `.raw/` (immutable source docs), which the wiki-only scan didn't see. Left as-is.
- **[[Foo]] and [[Three laws of motion]]: NOT DEAD.** Both are illustrative examples inside inline code explaining wikilink resolution. Left as-is.
- **[[grounded theory]] → [[Grounded Theory]]: fixed** (case correction in `fischhoff-broomell-2020-jdm-review`).

**Genuinely open** after this pass: the remaining truly-missing concept/source stubs ([[Distributive Justice]], [[psychometric meta-analysis]], [[Highhouse 2008]], APA-standard stubs, [[Job Demands–Control–Support Model]], [[claude-obsidian-ecosystem]]); the 5 plugin-`docs/` cross-references; the 3 DragonScale address backfills; the 3 orphans; the author-stub entity pages; and frontmatter on `tiling-report-2026-04-24.md`. The original (partially inaccurate) findings are retained below for reference.

## Summary
- Pages scanned: 825 (`wiki/**/*.md`)
- Real dead links: 21 (down from 103 raw hits after filtering lint-report/fold/`.raw` prose quotes)
- Orphan pages: 3
- Frontmatter gaps: 257 (almost entirely missing `tags`)
- Post-rollout pages missing `address`: 3
- Auto-fixed: 0 (nothing changed — awaiting your go-ahead)

## Orphan Pages
No inbound wikilinks point at these:

- [[Domain 24 - Motivation - Survey Design]] — project page, nothing links in. Suggest linking from a Motivation MOC or the related source page.
- [[Domain 24 - Motivation - Work Design]] — same.
- `wiki/mocs/_MIGRATION-PLAN.md` — scaffolding/meta file; likely fine to leave or archive.

## Dead Links (21)

Case-only fix (target exists under different casing):

- [[grounded theory]] in `fischhoff-broomell-2020-jdm-review` → should be [[Grounded Theory]].

Truly missing target pages:

- [[Distributive Justice]] — referenced in `hot`, `Scientist-Practitioner-Humanist (S-P-H) Model`, `lefkowitz-2008-values-organizational-psychology`. 3 inbound → strong candidate for a real concept page.
- [[psychometric meta-analysis]] — referenced in `Chockalingam Viswesvaran`, `Deniz S. Ones`, `Frank L. Schmidt`, `kuncel-et-al-2013-mechanical-vs-clinical`, `viswesvaran-schmidt-ones-2005-general-factor-job-performance`. 5 inbound → strong candidate for a concept page.
- [[Highhouse 2008]] — in `Mechanical vs Clinical Prediction`, `kuncel-et-al-2013-mechanical-vs-clinical`. Likely a source stub needed.
- [[Informed Consent]], [[Avoiding Harm (Standard 3.04)]], [[Publication Credit]] — all in `apa-2017-ethical-principles-code-of-conduct`. APA-standard concept stubs.
- [[Job Demands–Control–Support Model]] — in `log`.
- [[claude-obsidian-ecosystem]] — in `claude-obsidian-v1.4-release-session` (note: `claude-obsidian-ecosystem-research` exists; may be a rename).
- [[Three laws of motion]] — in `Persistent Wiki Artifact` (looks like leftover example text).
- [[Foo]] — in `DragonScale Memory` (test/placeholder artifact; safe to remove).

Doc-name links pointing at prose titles instead of the page stem (fix the link to use the real filename):

- `[[Morgeson and Humphrey - 2006 - The Work Design Questionnaire...]]` → [[morgeson-humphrey-2006-work-design-questionnaire]]
- `[[Oldham and Fried - 2016 - Job design research and theory...]]` → [[oldham-fried-2016-job-design-past-present-future]]
- `[[Parker et al. - 2017 - One hundred years of work design research...]]` → [[parker-morgeson-johns-2017-100-years-work-design]]
- `[[Ponterotto - 2005 - Qualitative research...]]` → [[Ponterotto-2005-Qualitative-Research-Paradigms]]
- `[[Humphrey et al]]` → [[humphrey-nahrgang-morgeson-2007-work-design-meta-analysis]]

Cross-references to plugin docs (live under `docs/`, not `wiki/`, so they don't resolve as wikilinks):

- [[mcp-setup]], [[wiki-cli]], [[wiki-mode]], [[methodology-modes-guide]], [[wikilinks]]. These point at plugin/reference docs. Either create redirect stubs in `wiki/references/` or convert to standard markdown links.

## Frontmatter Gaps (257)

Systemic issue: 254 of 257 gaps are a **missing `tags` field**. This spans nearly every `concepts/`, `entities/`, `mocs/`, and `sources/` page. Because the vault requires `tags` per the lint spec, this is the single highest-leverage cleanup — a batch backfill (even with a coarse tag derived from folder, e.g. `#domain/concept`) would clear the vast majority.

Three pages are missing more than just tags:

- `wiki/meta/retrieval-benchmark-v1.7.md` — missing `created`, `tags`.
- `wiki/meta/tiling-report-2026-04-24.md` — missing `type`, `status`, `created`, `updated`, `tags` (no frontmatter at all).
- `wiki/sources/basson-et-al-2022-oa-dimensions-wos.md` — missing `created`, `updated`, `tags`.
- `wiki/projects/Domain 24 - Motivation - Survey Design.md` / `...Work Design.md` — missing `status`, `tags`.

## Address Validity (DragonScale)

Three post-rollout pages (created ≥ 2026-04-23) lack an `address:` field and are not on the legacy manifest:

- `wiki/projects/Domain 24 - Motivation - Survey Design.md`
- `wiki/projects/Domain 24 - Motivation - Work Design.md`
- `wiki/questions/seven-job-design-dimensions.md`

These should be backfilled via `bash scripts/allocate-address.sh` or added to the legacy manifest if intentionally exempt.

## Empty Sections (advisory, noisy)

204 headings were flagged as having no content directly beneath them. Most are **false positives** — atomic notes where an `# Title` H1 is immediately followed by an `## H2` (a legitimate LYT pattern). Genuine empties worth checking are the stubbed entity pages that contain only a title heading, e.g. [[Daniel Levinthal]], [[Dorothy Leidner]], [[Eric Uhlmann]], [[Linda Argote]], [[Maryam Alavi]], [[Wesley Cohen]], and similar author stubs — these are content gaps, not formatting bugs.

## Recommended Actions (in priority order)

1. **Batch-backfill `tags`** across the 254 pages — biggest single win.
2. **Fix the 21 dead links**: 1 case fix, 5 doc-name relinks, 5 plugin-doc links, and ~8 genuinely missing concept/source stubs to create.
3. **Create the two high-inbound concept pages**: [[Distributive Justice]] (3 refs) and [[psychometric meta-analysis]] (5 refs).
4. **Backfill 3 DragonScale addresses.**
5. **Remove test artifacts**: [[Foo]] link and [[Three laws of motion]] leftover.
6. **Develop or link the 3 orphans**, and flesh out the author-stub entity pages.
