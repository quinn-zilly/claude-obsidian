---
title: Open Workflow
address: c-000072
created: 2026-05-20
type: concept
status: developing
updated: 2026-05-20
tags:
  - open-science
  - transparency
  - research-practice
---

# Open Workflow

Transparency in the scientific research process: public documentation and accessibility of study registration, hypotheses, analysis plans, and results throughout the project lifecycle—not just the published report.

## Definition

Open workflow means researchers make visible and accessible:

- **Pre-registration**: Study design, hypotheses, and analysis plans before data collection
- **Materials and protocols**: Detailed experimental procedures, participant instructions, measurement tools
- **Analysis decisions**: The specific steps taken, including choices made along the way
- **Results**: Both confirmatory and exploratory findings, successful and failed analyses
- **Workflow documentation**: How decisions evolved, what was tried and abandoned

## Rationale

In current practice, "openness" occurs almost entirely through a single mechanism: **the journal article**. But journals present a polished narrative of what the researcher learned, not how learning occurred.

Buckheit & Donoho (1995) captured this:

> "A scientific publication is not the scholarship itself, it is merely advertising of the scholarship"

The actual research—measures, methods, analysis choices—is largely opaque to readers. The published report is the authors' perspective on what happened and what it means.

## Problems Solved by Open Workflow

### 1. Reduces HARKing

[[HARKing]] (Hypothesizing After Results are Known) is common when researchers can reconstruct their research history to match findings. [[nosek-2012-scientific-utopia-ii|Nosek et al. 2012 - Scientific Utopia II]] note:

> People are more likely to presume that what they know now was how they conceived it at the beginning

Pre-registration clarifies: What did we hypothesize at the start? What did we discover along the way?

**Both are valuable.** Discovery drives science forward. But discoveries leverage chance more than confirmatory tests—so conflating them inflates confidence in findings.

### 2. Addresses File-Drawer Problem

Registry reveals what research was done but not published. Companies and funders can see whether studies with negative results were simply never written up or published.

Clinical trials example (clinicaltrials.gov):
- 2005: ICMJE required preregistration for RCTs
- Finding: 31% of registered trials showed discrepancies between registered and published outcomes
- Of these, 82% of discrepancies favored statistically significant results

### 3. Enables Accountability

[[nosek-2012-scientific-utopia-ii|Nosek et al. 2012 - Scientific Utopia II]] argue that knowing "someone could look" improves scientific practice even if no one actually does.

Their opening anecdote: Motyl and Nosek ran a replication of their own surprising finding (political extremists see gray literally) and found the effect vanished. They didn't publish the original because **lab mates knew about the replication.** Accountability to peers prevented ignoring the null result.

### 4. Clarifies Confirmatory vs. Exploratory Research

Without a registry, the distinction collapses in hindsight. With open workflow:

- Confirmatory findings: Predicted a priori, higher confidence
- Exploratory findings: Discovered during analysis, lower confidence until replicated
- Both are published and valuable; reader knows which is which

## Implementation Model

clinicaltrials.gov serves as a proof of concept:

- National Institutes of Health–sponsored registry
- Trial registration required before data collection (since 2005)
- Requires disclosure of primary and secondary outcomes
- Enables post-hoc comparison: what was planned vs. what was reported?

**Result**: Substantial evidence of outcome switching favoring statistical significance.

For broader science, implementations include:

- [[Open Science Framework]]: Web-based project management for archiving materials, analysis scripts, data, and study registration
- **Preregistration at OSF**: Timestamp-locked records of hypotheses and analysis plans
- **Public registries**: For specific domains (clinical trials, lab-registered studies)

## Barriers and Responses

### Researcher Concerns

**"I don't know what I'll find; how can I preregister?"**
- Answer: Preregister the planned analysis, even if exploratory work follows. Distinguish: confirmatory test vs. exploratory follow-ups.

**"This stifles creativity and discovery."**
- Answer: Discovery is valuable. Registering confirmatory work doesn't prevent exploration. Distinction enables both; it doesn't eliminate discovery research.

**"Competitors might scoop my work."**
- Answer: Private preregistration exists; embargo periods are negotiable. Benefit of transparency outweighs scoop risk.

### Benefits Outweigh Barriers

The transparency gained enables:
- Error detection and correction
- Increased confidence in accurate findings
- Reduced waste on false leads
- Clearer cumulation of knowledge

## Related Concepts

- [[Preregistration]]: Formal pre-registration of hypotheses and analysis plans
- [[HARKing]]: The problem open workflow addresses
- [[Registered Reports]]: Journal format combining preregistration with early peer review
- [[Open Science]]: Broader framework including open data, open methods, open workflow

## Sources

- [[nosek-2012-scientific-utopia-ii|Nosek et al. 2012 - Scientific Utopia II]]
- Mathieu, S., Boutron, I., Moher, D., Altman, D. G., & Ravaud, P. (2009). Comparison of registered and published primary outcomes in randomized controlled trials. Journal of the American Medical Association, 302, 977–984.
- Schooler 2011: Unpublished results hide the decline effect
