---
type: meta
title: "Dead-Link Fix Plan 2026-06-05"
created: 2026-06-05
updated: 2026-06-05
tags: [meta, lint, plan]
status: developing
---

# Dead-Link Fix Plan — 2026-06-05

108 dead-link targets remain after lint round 2. This plan sorts them into four actions: **rewrite** (link-text points to an existing page), **create-entity**, **create-concept**, and **purge** (junk / external / wrong-syntax). Do them in the order below; each phase shrinks the next.

---

## Phase A — Rewrite citation links to existing pages (no new pages)

These link strings are citations, but the page already exists under a different filename. Fix the link text, not the vault. ~13 targets, ~30 links.

| Dead link text | Real page |
|---|---|
| Nosek et al. 2012 - Scientific Utopia II (9×) | `nosek-2012-scientific-utopia-ii` |
| Nosek and Bar-Anan 2012 - Scientific Utopia I | `nosek-bar-anan-2012-scientific-utopia-i` |
| Open Science Collaboration (2015) / 2015 | `open-science-collaboration-2015` |
| Bezrukova et al. 2016 (4×) | `bezrukova-et-al-2016-diversity-training-meta-analysis` |
| Alvarez et al. (2004) (3×) | `alvarez-et-al-2004-training-evaluation-effectiveness` |
| Kraiger & Ford 2021 | `kraiger-ford-2021-workplace-instruction` |
| Tversky and Kahneman (1974) / Tversky & Kahneman 1974 | `tversky-kahneman-1974-heuristics-biases` |
| LeBel et al. 2018 / (2018) | `Etienne LeBel` (or make a source page — see note) |
| Smith-Jentsch (2020) | `Kimberly A. Smith-Jentsch` |
| Arthur et al. 2003 Training Meta-Analysis | `arthur-et-al-2003-training-meta-analysis` |
| Avolio et al. (2010) | `Bruce J. Avolio` |
| McCall 2010 | `Morgan McCall` |

Mechanism: use Obsidian alias links — `[[real-page|Nosek et al. 2012]]` — so display text stays readable while the link resolves. Safe, scriptable.

Note: LeBel/Smith-Jentsch/Avolio/McCall currently resolve only to the *author* page, not a *source* page. If you want the citation to land on the paper, those source pages need creating first (Phase C).

---

## Phase B — Create entity (person) pages

Real co-authors cited across source pages, no entity page yet. ~22 people. Make light entity stubs (name, affiliation-if-known, `> [!gap]`, link back to the source that cites them).

High-value (cited 3-4×): Lisa Mainiero, Sherry Sullivan, Marissa Shuffler.

Single-cite: Winston Bennett Jr., Lisa A. Burke, Holly M. Hutchins, John Ford, Christina Lacerenza, Jeffery LePine, John Mathieu, James Beck, Deborah DiazGranados, Parbudyal Singh, Juan Sanchez, Nicholas C. Soderstrom, Margaret Toich, Burak Ozkum, Shmuel Ellis, Inbar Davidi, Bita Fayaz-Farkhad, Javier A. Granados Samayoa.

Also fold in the **author-last-first** bucket (rename to `First Last` style to match convention): Wegner, Daniel M. → Daniel M. Wegner; Argote, Linda → Linda Argote (already exists!); Lewis, Kristina; Moreland, Richard; Hollingshead, Andrea.

Caution: "Argote, Linda" and "Linda Argote" both already have/should-have a single page — dedupe, don't make twins.

---

## Phase C — Create concept (and source) pages

Genuine missing concepts worth real pages. ~10 targets.

Concept stubs: Learning from Experience (3×), Mental Models (Learning) (3×), Failure-Driven Learning (3×), Knowing-Doing Gap (2×), Questionable Research Practices (QRPs) (2×), Stakeholder Engagement (Evaluation) (3×), Cross-Cultural Communication (Evaluation) (2×), Type I and Type II Errors (Medicine) (2×), First 90 Days Framework (2×), Training Transfer — Three-Factor Model.

Misclassified-as-person concepts (also create or rewrite to existing): Instructional Design, Confirmation Bias, Hindsight Bias, Signal Detection Theory, Operant Conditioning, Image Theory, Multiattribute Utility Theory, Overconfidence, Multiverse Analysis, Replicability, Principal-Agent Problem, Incentive Compatibility, Construct Proliferation, Illusions of Competence, Scoring Rules, Open Methods and Tools, Strategic Frame, Traditional Job Analysis, Leadership Transitions, Training Design and Delivery. — Check each first; several may already exist under a near-name and only need a rewrite.

Optional source pages (if Phase A should land on the paper not the author): LeBel et al. 2018, Smith-Jentsch 2020, Avolio et al. 2010, plus the older one-cite citations (Baldwin and Ford 1988, Colquitt LePine Noe 2000, Ford and Weissbein 1997, Buckheit & Donoho 1995, etc.).

---

## Phase D — Purge / convert (no page wanted)

Junk, demo leftovers, externals, wrong syntax. Delete the link or convert to plain text/URL. ~15 targets.

- Demo/test junk: Foo, alav, wikilinks, Three laws of motion, AI Marketing Hub Cover Images Canvas, claude-obsidian-presentation, wiki-map, E-commerce SEO, boundaryless-career (dup of Boundaryless Career stub now created).
- Old SEO session logs (never existed in this vault): 2026-04-14-claude-seo-v190-session, 2026-04-15-slides-and-release-session, 2026-04-15-release-report-session.
- External names → plain text or URL, not wikilinks: clinicaltrials.gov (4×), PLoS ONE.
- Wrong link syntax (path instead of note name): notes/Foo, dashboard.base, wiki/comparisons/, questions/, wiki/sources, Wiki Map.canvas, .raw/Output/Yost-2013-ExperienceDrivenDevelopment.md.
- Question-style link: "How does the LLM Wiki pattern work?" → page exists as `How does the LLM Wiki pattern work` (no `?`). Rewrite.

---

## Suggested execution order
1. **Phase A** (rewrite ~30 links) — biggest drop, zero new pages, fully scriptable via alias links.
2. **Phase D purge** — removes noise so the real gap count is honest.
3. **Phase B** entity stubs (~22, dedupe Argote).
4. **Phase C** concept stubs — but first re-check each against existing pages to avoid duplicates.

Estimated result: 108 → roughly 0 live dead-links, ~30-35 new stub pages, ~45 links rewritten, ~15 purged.

---

## EXECUTED 2026-06-05 — all phases complete

- **Phase A:** rewrote 12 citation strings to alias links → existing pages (18 files).
- **Phase D:** converted externals to plain text (clinicaltrials.gov, PLoS ONE), fixed `?`/path-style links, removed dead SEO session-log `related:` entries, repointed boundaryless-career. Left code-span/embed examples untouched (not real links).
- **Phase B:** created 26 entity stubs (c-000530–555); deduped `Argote, Linda` → existing `Linda Argote`; normalized 4 `Last, First` links.
- **Phase C:** created 26 concept stubs (c-000556–581); rewrote 4 links to existing pages (QRPs, Signal Detection Theory, Mental Models, Training Transfer 3-factor); fixed nosek-bar-anan typo.
- **Final sweep:** converted 13 bibliographic citation strings to plain text; fixed inverted aliases; repaired `alav` truncated link; removed dead `.raw/` frontmatter link.

**Result: 160 → 0 true live dead-links.** (Remaining flagged items were false positives: correctly-aliased links, a valid `.base` embed, and intentional folder nav-aliases in Wiki Map.) 52 new stub pages total. Integrity: 0 address collisions, 547 addressed pages, manifest valid JSON, counter 582.
