---
type: meta
title: "Lint Report 2026-05-30"
created: 2026-05-30
updated: 2026-05-30
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-05-30

## Summary

- Pages scanned: 290
- Orphan pages: 1
- Dead links (total raw): 94 → categorized below
- Dead links needing action: 65 concept/entity stubs
- Frontmatter gaps: 24 pages (all missing `created:`)
- Address errors: 1 post-rollout page missing address
- Address collisions: 0
- Counter drift: 0
- Semantic tiling: skipped (tiling-check.py not available; exit 127)
- Auto-fixed: 0 (awaiting review)

---

## Orphan Pages

- [[Book recommendations]]: no inbound links. Low-priority; either link from [[overview]] or leave as personal note.

---

## Dead Links — By Category

### Category A: Session links (intentional stubs, low priority)
These reference session log pages that don't exist in the wiki. Expected; ignore or delete links.

- `[[2026-04-14-claude-seo-v190-session]]` in [[Pro Hub Challenge]], [[Claude SEO]]
- `[[2026-04-15-release-report-session]]` in [[Claude SEO]]
- `[[2026-04-15-slides-and-release-session]]` in [[Claude SEO]]

### Category B: Comma-style author refs (fixable — convert to entity page links)
Pages using "Last, First" citation style instead of wikilinks to entity pages.

- `[[Argote, Linda]]` in [[ren-argote-2011-tms]] → should be `[[Linda Argote]]`
- `[[Hollingshead, Andrea]]` in [[ren-argote-2011-tms]] → create [[Andrea Hollingshead]] stub or remove
- `[[Bastardi, Uhlmann, & Ross (2011)]]` in [[Motivated Reasoning]] → citation, not a page link; remove brackets
- `[[Buckheit & Donoho (1995)]]` in [[Open Workflow]] → citation; remove brackets
- `[[John, Loewenstein, & Prelec 2012]]` in [[nosek-2012-scientific-utopia-ii]] → citation; remove brackets
- `[[Lewis (2003)]]`, `[[Liang et al. (1995)]]`, `[[McCall 2010]]` — citations; remove brackets

### Category C: Test placeholder
- `[[Foo]]` in [[DragonScale Memory]] (×2) — test artifact; safe to remove.

### Category D: Concept/entity stubs needing pages (65 unique targets)

High-priority (referenced in 3+ pages):
- `[[Nosek et al. 2012 - Scientific Utopia II]]` (9 refs) → should link to `[[nosek-2012-scientific-utopia-ii]]`
- `[[clinicaltrials.gov]]` (3 refs) → add wikilink to external resource or remove brackets
- `[[Group Training]]` (3 refs in TMS pages) → concept stub needed

Medium-priority (referenced in 2 pages):
- `[[Expertise Location]]` → TMS concept stub
- `[[Giner-Sorolla 2012]]` → should link to `[[giner-sorolla-2012-science-or-art]]`
- `[[Knowing-Doing Gap]]` → concept stub needed (referenced in Kraiger-Ford + Soderstrom-Bjork)
- `[[Memory Differentiation]]` → TMS concept stub
- `[[Shared Mental Models]]` → concept stub
- `[[Strategic Frame]]` → concept stub (see Cornelissen & Werner — surprising it's missing)
- `[[Team Cognition]]` → concept stub
- `[[Team Mental Models]]` → concept stub
- `[[Yarkoni & Westfall 2017]]` → should link to `[[yarkoni-westfall-2017-prediction-vs-explanation]]`
- `[[Open Science Collaboration (2015)]]` and `[[Open Science Collaboration 2015]]` → should link to `[[open-science-collaboration-2015]]`
- `[[LeBel et al. (2018)]]` and `[[LeBel et al. 2018]]` → should link to `[[lebel-2018-credibility-framework]]`
- `[[Munafò et al. 2017]]` → should link to `[[munafo-2017-manifesto]]`

Source page cross-ref fixes (link-style only, no new page needed):
- `[[nosek-bar-anan-2012-scientific-utopia-ii]]` in [[nosek-bar-anan-2012-scientific-utopia-i]] → typo; should be `[[nosek-bar-anan-2012-scientific-utopia-i]]` (self-link) or `[[nosek-2012-scientific-utopia-ii]]`
- `[[Learning Goals vs Performance Goals\]]` in [[Goal-Setting Theory]] → escaped backslash in table pipe; fix wikilink syntax

Lower-priority stubs (single reference each):
- `[[Confirmation Bias]]`, `[[Hindsight Bias]]`, `[[Overconfidence]]` — common JDM concepts; worth creating
- `[[Multiverse Analysis]]` in [[Robustness (Science)]] — concept stub
- `[[Replicability]]` in [[Robustness (Science)]] — surprising gap given Open Science coverage
- `[[Shared Experience]]`, `[[Task Coordination]]`, `[[Task Credibility]]` — TMS-cluster stubs
- `[[Team Creativity]]`, `[[Team Learning]]`, `[[Team Reflexivity]]`, `[[Team Member Satisfaction]]` — TMS stubs
- `[[Organizational Memory]]`, `[[Knowledge Specialization]]`, `[[Metaknowledge]]` — KM stubs
- `[[Conflict of Interest]]` in [[nosek-2012-scientific-utopia-ii]] → should be `[[Conflict of Interest in Science]]`
- `[[Illusions of Competence]]` in [[Learning vs Performance Distinction]] — concept stub
- `[[Multiattribute Utility Theory]]`, `[[Image Theory]]` — JDM stubs (connolly-2012)
- `[[Transactive Memory]]` in [[ren-argote-2011-tms]] → should be `[[Transactive Memory Systems]]`
- `[[alav]]` in [[grant-1996-knowledge-based-theory]] → likely `[[Maryam Alavi]]`; fix link
- `[[wikilinks]]` in [[cherry-picks]] — meta reference; harmless

---

## Frontmatter Gaps

24 pages missing `created:` field. All are SDT-cluster concepts and entities written before the `created:` convention was enforced. **Safe to auto-add with placeholder date 2026-05-29** (their ingest date).

Missing `created:`:
- [[Autonomy (SDT)]], [[Basic Psychological Needs (SDT)]], [[Basic Psychological Needs Theory]], [[Causality Orientations Theory]], [[Cognitive Evaluation Theory]], [[Competence (SDT)]], [[Extrinsic Motivation]], [[Goal Contents Theory]], [[Internalization (SDT)]], [[Intrinsic Motivation]], [[Need Frustration (SDT)]], [[Organismic Integration Theory]], [[Perceived Locus of Causality]], [[Relatedness (SDT)]], [[Relationships Motivation Theory]], [[Self-Determination Theory]]
- [[Edward Deci]], [[Emma Bradshaw]], [[Jasper Duineveld]], [[Richard Ryan]], [[Stefano Di Domenico]]

Also: 3 additional pages missing `created:` not shown above (check [[wiki/entities/_index.md]] area).

---

## Address Validation

- Counter state (peek): `285`
- Highest c- address observed: `c-000284` (Gary Latham entity, this session)
- Counter file value: 285 ✓ (consistent)
- Post-rollout pages checked: 268 (267 passing, 1 error)
- Legacy pages pending backfill: 21
- Address collisions: 0
- Counter drift: none

### Errors

- [[Spacing Effect]] (`wiki/concepts/Spacing Effect.md`): missing `address:`. Page created 2026-05-23 (post-rollout). Run `./scripts/allocate-address.sh` and add to frontmatter.

### Pending backfill (informational)

21 legacy pages without addresses (created pre-2026-04-23). No action required until deliberate backfill pass.

---

## Semantic Tiling

Skipped — `scripts/tiling-check.py` returned exit 127 (not found). No semantic duplicate detection this run.

---

## Recommended Actions (Prioritized)

**Immediate fixes (safe to auto-apply):**
1. Fix escaped wikilink `[[Learning Goals vs Performance Goals\|learning goals]]` in [[Goal-Setting Theory]] → remove backslash
2. Fix `[[Conflict of Interest]]` → `[[Conflict of Interest in Science]]` in [[nosek-2012-scientific-utopia-ii]]
3. Fix `[[Transactive Memory]]` → `[[Transactive Memory Systems]]` in [[ren-argote-2011-tms]]
4. Fix `[[alav]]` → `[[Maryam Alavi]]` in [[grant-1996-knowledge-based-theory]]
5. Add `address:` to [[Spacing Effect]] (next counter value after 284)
6. Add `created: 2026-05-29` to 24 SDT-cluster pages missing it

**Source link fixes (citation refs that became wikilinks):**
7. Fix `[[Nosek et al. 2012 - Scientific Utopia II]]` → `[[nosek-2012-scientific-utopia-ii]]` (×9)
8. Fix `[[Giner-Sorolla 2012]]` → `[[giner-sorolla-2012-science-or-art]]` (×2)
9. Fix `[[Yarkoni & Westfall 2017]]` → `[[yarkoni-westfall-2017-prediction-vs-explanation]]` (×2)
10. Fix `[[Open Science Collaboration (2015)]]` / `[[Open Science Collaboration 2015]]` → `[[open-science-collaboration-2015]]`
11. Fix `[[LeBel et al. (2018)]]` / `[[LeBel et al. 2018]]` → `[[lebel-2018-credibility-framework]]`
12. Fix `[[Munafò et al. 2017]]` → `[[munafo-2017-manifesto]]`

**Concept stubs to create (next ingest cycle):**
- [[Strategic Frame]] — referenced in Cornelissen & Werner; should exist given framing coverage
- [[Knowing-Doing Gap]] — referenced in Kraiger-Ford and Soderstrom-Bjork
- [[Replicability]] — surprising gap in Open Science cluster
- [[Confirmation Bias]], [[Hindsight Bias]] — common JDM concepts
- [[Shared Mental Models]], [[Team Mental Models]] — TMS adjacents
- [[Multiverse Analysis]] — Open Science methods concept

**Orphan:**
- [[Book recommendations]]: link from [[overview]] or keep as intentional personal note.
