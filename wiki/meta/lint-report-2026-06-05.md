---
type: meta
title: "Lint Report 2026-06-05"
created: 2026-06-05
updated: 2026-06-05
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-06-05

## Summary
- Pages scanned: 286 (wiki/*.md, excluding meta/folds/maps/canvas assets)
- Orphan pages: 7
- Dead links (unique targets, excluding lint-reports/folds): 160
- Frontmatter gaps: 370 pages
- Empty sections: 173 pages
- Duplicate filenames: 1 group (expected — `_index.md` per folder)
- Address collisions: 6 (errors)
- Post-rollout pages missing address: 35 (errors)
- Legacy pages pending backfill: 20 (informational)
- Address-map mismatches: 2 (errors)
- Semantic tiling: skipped (ollama unreachable)
- Auto-fixed: 244 `updated:` backfills, 6 filename/link renames, 2 manifest-map repairs, 6 address collisions resolved, 35 missing addresses assigned, 3 typo dead-links fixed.

## Fixes Applied 2026-06-05
- Backfilled `updated:` on 244 pages (from `created:` or file mtime). `tags:` left untouched — many flagged pages use block-style tags the first scan missed.
- Renamed 6 files to Title-Case-with-spaces and rewrote 8 inbound wikilinks: Competency Modelling, KSA Framework, Strategic Job Analysis (SJA), Kaleidoscope Career Model, Winfred Arthur Jr., Miles and Snow Strategic Typology.
- Repaired `.raw/.manifest.json`: un-inverted the `c-000395` entry, fixed the `Norbert-Kerr` dead path, remapped renamed files. Backups at `.manifest.json.bak` / `.bak2`.
- Resolved 6 address collisions (kept earlier-created page, reassigned newer): c-000450–c-000455.
- Assigned addresses to 35 post-rollout pages: c-000456–c-000490. Counter now at 491.
- Fixed 3 typo dead-links (trailing `)` in hot.md and log.md; full-path `[[wiki/...]]` links in log.md → bare names).
- Verified: 0 remaining address collisions, manifest valid JSON (400 map entries).

### Round 2 fixes (2026-06-05)
- Created 39 stub pages (status: seed, each with a `> [!gap]` flag + source link): the core 7 concepts (Meta-Analysis, Item Response Theory, Action Learning, Communities of Practice, Mentoring, Implicit Bias, Bayesian Statistics in Psychology), 22 transactive-memory family pages, 10 kaleidoscope-career family pages. Addresses c-000491–c-000529.
- Tags gap was a **false alarm**: re-scan found 0 content pages truly missing a `tags:` key. The original 370 "frontmatter gaps" were almost all the now-backfilled `updated:` field plus block-style tags the first scanner mis-read.
- Dead-link targets dropped 160 → 108 (52 resolved by stubs + the 6 renames).
- Final state: 0 address collisions, 495 pages addressed, manifest valid JSON, counter at 530.

### Remaining (not auto-fixed)
- ~108 dead-link targets, mostly author-name references inside source pages (e.g. "Wegner, Daniel M.", "Lewis (2003)") and citation-style links — these are bibliographic, not concept gaps. Convert to entity pages or plain text as you prefer.
- The new 39 stubs are seeds and need real content.
- 3 non-content pages (log.md, an old tiling report, Book recommendations) lack an inline `tags:` key — expected, left as-is.

---

## DragonScale: Address Validation

DragonScale is active (`scripts/allocate-address.sh` + `.vault-meta/address-counter.txt` present). Counter peek = **450**. No format errors, no counter drift.

### Errors — Address collisions (6 pairs share an address)
- [[Derailment]] (`c-000442`) collides with [[yost-plunkett-2009-transition]].
- [[Effect Size Heterogeneity]] (`c-000385`) collides with [[Goal Displacement]].
- [[Operative vs Official Goals]] (`c-000384`) collides with [[Power Analysis (Replication Studies)]].
- [[Prior Knowledge]] (`c-000395`) collides with [[mainiero-sullivan-2005-kaleidoscope-careers]].
- [[Replication Types Taxonomy]] (`c-000386`) collides with [[Steven Kerr]].
- [[kerr-1995-folly-rewarding-A]] (`c-000381`) collides with [[shrout-rodgers-2018-replication-crisis]].

Fix: reassign one page in each pair a fresh address via `./scripts/allocate-address.sh`, update its frontmatter and `.raw/.manifest.json`.

### Errors — Post-rollout pages missing `address:` (35)
Pages created on/after the 2026-04-23 rollout that lack an address. The largest clusters are the 2026-06-01 team/training ingest and the 2026-06-04 career ingest. Several also have empty/missing `created:` (metadata gap too): Competency-Modelling, DEI Evaluation, Equitable Data Collection, KSA-Framework, Miles-Snow-Strategic-Typology, Strategic-Job-Analysis, approaches-dei-evaluation, Singh-2008-Job-Analysis-Changing-Workplace, KM Research Paper, Book recommendations.

2026-06-01 batch: Emergent States (Teams), Five-Factor Model, Leadership Training (Teams), Personality Dynamics (TAT), Person–Environment Fit, Psychological Safety, Situation Strength, Situational Cue Types (TAT), Team Building, Team Debriefing, Team Development Interventions, Team Training, Teamwork Processes (Marks et al. Taxonomy), Trait Activation Theory, Eduardo Salas, Robert Tett, lacerenza-et-al-2018-team-development-interventions, lepine-et-al-2008-teamwork-processes, shuffler-et-al-2011-team-development-interventions, tett-et-al-2021-trait-activation-theory.

2026-06-04 batch: Experience-Driven Development, kaleidoscope-career-model, Training as Catalyst (OJD), Training Checklist, yost-2013-experience-driven-development.

Fix: run `wiki-ingest`'s address-assignment, or manually `./scripts/allocate-address.sh` per page. Lint does not auto-assign.

### Errors — Address-map consistency (`.raw/.manifest.json`)
- `address_map` references `wiki/entities/Norbert-Kerr.md` → `c-000126`, but that page no longer exists (it's `Norbert Kerr.md`, no hyphen). A rename dropped the map update.
- One entry is inverted: key `c-000395` maps to value `wiki/sources/mainiero-sullivan-2005-kaleidoscope-careers.md` (path and address swapped). Repair the key/value order.

### Pending backfill (informational)
- 20 legacy pages (created < 2026-04-23) without addresses. Expected; backfill at your discretion via `l-NNNNNN` addresses.

---

## DragonScale: Semantic Tiling
Skipped — `tiling-check.py --peek` returned exit 10 (ollama not reachable at `http://127.0.0.1:11434`; `nomic-embed-text` not pulled). To enable: run ollama locally and `ollama pull nomic-embed-text`, then re-run lint. Thresholds remain uncalibrated (error ≥0.90, review ≥0.80).

---

## Orphan Pages
No inbound wikilinks. Five of seven are actually filename↔wikilink punctuation mismatches, not true orphans:
- [[Competency Modelling]]: "Competency Modelling" referenced 5× as a dead link. Filename/link mismatch.
- [[KSA Framework]]: "KSA Framework" referenced 5×. Mismatch.
- [[Strategic Job Analysis (SJA)]]: "Strategic Job Analysis (SJA)" referenced 6×. Mismatch.
- [[Kaleidoscope Career Model]]: "Kaleidoscope Career Model" referenced 5×. Mismatch.
- [[Winfred Arthur Jr.]]: filename lacks a period; links use "Winfred Arthur Jr." (4×). Mismatch.
- [[KM Research Paper]]: project page, likely intentionally standalone.
- [[Training Checklist]]: project page, likely fine.

Fixing the filenames (or links) resolves both the orphan and the corresponding dead links at once.

---

## Dead Links (high-value clusters)
160 unique dead targets. Top candidates (mentioned 3+ times):

- "Nosek et al. 2012 - Scientific Utopia II" (9×): the source exists as `nosek-2012-scientific-utopia-ii.md` — link-text mismatch, not a missing page. Fix the links.
- "Meta-Analysis" (6×), "Item Response Theory" (6×): genuinely missing concept pages, widely referenced. Create.
- "Strategic Job Analysis (SJA)" (6×), "KSA Framework" (5×), "Competency Modelling" (5×), "Kaleidoscope Career Model" (5×): the filename-mismatch orphans above.
- Kaleidoscope sub-concepts (5× each): "Boundaryless Career", "Authenticity (Career)", "Balance (Career)", "Challenge (Career)", "Relational Career Model", "Opt-Out Revolution", "Career Interruption". Create stubs or de-link.
- "Action Learning" (5×), "Communities of Practice" (5×), "Mentoring" (4×): missing OJD concept pages.
- "Implicit Bias" (4×), "Bezrukova et al. 2016" (4×): diversity-training cluster.
- "Bayesian Statistics in Psychology" (4×), "clinicaltrials.gov" (4×): open-science cluster.
- Transactive-memory sub-concepts from `Transactive Memory Systems` + `ren-argote-2011-tms` (2× each): Team Cognition, Shared Mental Models, Expertise Location, Task Credibility, etc. — large coherent gap; consider a batch of stubs.

Stray-character dead links to just fix (not create):
- "Technology-Based Training)" and "Multiple Goal Self-Regulation)" — trailing paren.
- "Learning Goals vs Performance Goals\" — trailing backslash.
- "wiki/index.md", "wiki/hot.md", "wiki/log.md" linked with full paths from `log.md` — use bare names.

---

## Missing Pages (recommended new concept pages)
Mentioned across 3+ pages with no page of their own: "Meta-Analysis", "Item Response Theory", "Action Learning", "Communities of Practice", "Implicit Bias", "Bayesian Statistics in Psychology", plus the transactive-memory and kaleidoscope-career sub-concept families.

---

## Frontmatter Gaps
370 pages missing ≥1 required field. Dominant patterns: missing `updated:` on concept pages (~180) and missing `tags:` on entity/source pages (~120). A handful miss core fields (`type`/`status`/`created`): Competency-Modelling, KSA-Framework, Strategic-Job-Analysis, Miles-Snow-Strategic-Typology, DEI Evaluation, Equitable Data Collection, Book recommendations, tiling-report-2026-04-24, Singh-2008-Job-Analysis-Changing-Workplace.

Safe auto-fix: backfill `updated:` = `created:` (or file mtime) and add `tags: []` where absent. Core-field gaps need your input on type/status.

---

## Empty Sections
173 pages have a heading immediately followed by another heading or EOF. Many are H1 title-only stubs with content under sub-headings (false positives). Real empties worth filling: cherry-picks.md (all 4 tier headings), getting-started.md ("Three-Step Quick Start"), Construct Validity ("Two Competing Definitions"), Diversity Training Myths ("Myth Taxonomy"), Instructional Principles ("Five Core Principles"). Full list on request.

---

## Naming Convention Issues
Filename ↔ wikilink mismatches (fix once, resolve orphan + dead links together):
- `Competency-Modelling.md` ↔ "Competency Modelling"
- `KSA-Framework.md` ↔ "KSA Framework"
- `Strategic-Job-Analysis.md` ↔ "Strategic Job Analysis (SJA)"
- `kaleidoscope-career-model.md` ↔ "Kaleidoscope Career Model"
- `Winfred Arthur Jr.md` ↔ "Winfred Arthur Jr."
- `Miles-Snow-Strategic-Typology.md` ↔ "Miles and Snow Strategic Typology"

These hyphenated/lowercased filenames also violate the "Title Case with spaces" convention. Renaming to match the wikilinks is the cleanest fix.

---

## Recommended Fix Order
1. **Address errors first** (6 collisions, 35 missing, 2 map mismatches) — DragonScale integrity errors.
2. **Naming mismatches** (6 files) — each clears one orphan + several dead links at once.
3. **Frontmatter backfill** (`updated`, `tags`) — bulk, low-risk, auto-fixable.
4. **Create high-frequency stub pages** (Meta-Analysis, Item Response Theory, Action Learning, transactive-memory family).
5. **Fix typo dead links** (trailing parens/backslashes).
