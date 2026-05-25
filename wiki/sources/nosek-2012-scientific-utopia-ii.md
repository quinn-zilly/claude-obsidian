---
type: source
address: c-000069
title: "Scientific Utopia II: Restructuring Incentives and Practices to Promote Truth Over Publishability"
author:
  - "[[Brian Nosek]]"
  - "Jeffrey R. Spies"
  - "Matt Motyl"
year: 2012
publication: Perspectives on Psychological Science, 7(6), 615–631
date: 2012
created: 2026-05-20
status: developing
updated: 2026-05-20
source_type: academic_paper
doi: 10.1177/1745691612459058
tags:
  - open-science
  - replication-crisis
  - publication-bias
  - scientific-reform
  - research-incentives
journal: Perspectives on Psychological Science
---

# Nosek et al. (2012) - Scientific Utopia II: Restructuring Incentives and Practices to Promote Truth Over Publishability

## Key Takeaway

Publishing incentives (seeking novel, positive results) directly conflict with accuracy incentives in science. The paper proposes that making truth-seeking competitive with publishability through reformed practices—particularly open data, methods, and workflow—can improve knowledge accumulation without sacrificing innovation.

## Core Problem: Incentive Misalignment

Nosek, Spies, and Motyl articulate a fundamental conflict of interest in academic science:

- **Professional incentive**: Get published (especially in prestigious journals with novel, positive findings)
- **Accuracy incentive**: Get it right (ensure findings are true and reproducible)

These are often at odds. Publishing success depends on novelty and positive results; accuracy is more abstract and long-term. This creates pressure toward [[HARKing|motivated reasoning]], [[P-hacking]], selective reporting, and undisclosed flexibility in analysis.

## The "True Story" Opening

The paper's opening anecdote is powerful: Nosek and Motyl conducted a study showing political extremists perceive gray shades less accurately than moderates. The effect was statistically significant (p = .01) with N=1,979. They prepared to publish in Psychological Science. But before submitting, they ran a direct replication with 1,300 participants and .995 power. **The effect vanished (p = .59).**

Their accountability to lab mates who knew about the replication prevented them from ignoring the null result and publishing the original finding. This example motivates the entire argument: incentive structures that reward publishing without penalizing false positives allow flawed findings to persist.

## Problems with Current Practices

### Novelty and Positive Results Bias

- 94% of journal editors say replications are not encouraged for submission
- Over 90% of published findings in psychology are positive effects
- Rate of positive results increasing over 50+ years
- File-drawer problem (unpublished negative results)
- [[Publication Bias]] creates a literature systematically skewed toward false positives

### Common Problematic Practices

The paper catalogs practices that increase publishability but may reduce validity:

1. Running many low-powered studies instead of high-powered ones
2. Selective dismissal of "failed" pilot studies while uncritically accepting successful ones
3. Selective reporting of positive vs. negative results
4. Stopping data collection once significance is achieved
5. Including multiple variables and reporting only those that "worked" ([[P-hacking]])
6. Maintaining flexibility in analysis, exclusion criteria, and data transformations
7. Reporting discoveries as if confirmatory (HARKing)
8. Avoiding direct replication

### Consequences

- Ioannidis (2005): "Why Most Published Research Results Are False"
- Greenwald (1975): false positive rate ~30% based on publication practices alone
- Bayer HealthCare: only 25% of attempts to reproduce published findings succeeded
- Amgen: only 11% of 53 landmark cancer studies replicated
- Venture capital assumption: >50% of academic studies cannot be replicated in industry

## Strategies That Won't Work (Or Not Enough)

### Conceptual Replication

While valuable for theoretical understanding, conceptual replication enables confirmation bias—failed conceptual replications are dismissed as "not testing the same phenomenon."

### Myth of Self-Correction

Science does self-correct eventually, but "eventually" can be decades. False findings persist and spawn entire literatures before being overturned (if at all).

### Journals of Negative Results

Defining a journal by what it publishes (negative results, replications) self-defines it as low-status. No one wants to publish there.

### Education Campaigns

Despite 30+ years of discussion about these issues, publishing norms haven't changed. Good intentions and awareness aren't sufficient.

### Raising Publication Barriers

Requiring replications could stifle innovation in domains where data collection is resource-intensive or unique.

## Solutions: Restructuring Incentives and Practices

### Short-term / Bottom-up Reforms

**Author, Reviewer, Editor Checklists**
- Disclose sample sizes, statistical tests, effect sizes, covariates
- Verify disclosure of analysis flexibility (e.g., multiple comparisons, exclusion criteria)
- Modeled on CONSORT for randomized controlled trials

**Paradigm-Driven Research**
- Systematically alter a procedure to test questions, rather than reinventing methods
- Incorporates replication and extension in a single design
- Example: Deese-Roediger-McDermott paradigm adapted to study aging, mood, and false memories
- Provides confidence via replication while extending knowledge

**Metrics for Replication Value (RV)**
- Citation impact + precision of existing evidence
- Helps identify which findings are worth replicating
- Open Science Collaboration developing RV metrics

**Crowd-sourced Replication**
- Spread replication effort across multiple labs
- Solves resource constraints for important findings
- Open Science Collaboration replication project as model

**Challenging Mindsets**
- Anecdotal evidence that publication numbers/prestige matter less in final hiring/promotion decisions than perceived
- Suggests need for systematic study: do publication metrics actually predict success?

### Medium-term / Systemic Reforms

**Journals Focused on Soundness, Not Importance**
- [[PLoS ONE]] model: peer review evaluates research soundness, not perceived importance
- Since 2006: 13,798 articles (2011), 70% acceptance rate, 2011 impact factor 4.41 (top 25%)
- Shows importance is not predictive of citation impact

**Post-Publication Peer Review**
- Make publication trivial (anyone can publish)
- Peer review becomes evaluation, not gatekeeping
- Models: arXiv (physics), SSRN, RePEc
- Shifts incentives from "getting published" to "having impact on future research"
- Removes barrier to publishing replications and negative results

### Long-term / Core Reforms: Open Science

The "ultimate solution" involves three dimensions of openness:

#### Open Data

**Benefits:**
- Enables confirmation, critique, extension of prior research
- Detects and corrects errors (Bakker & Wicherts 2011: 15% of papers contain statistical errors)
- Allows meta-analysis and data aggregation
- Creates opportunities for novel methodologies and insights

**Barriers (and responses):**
- Concerns about revealing errors → counterargument: errors persist when hidden
- Data archiving burden → addressed by planning for sharing from project start
- Confidentiality concerns → handled via exceptions with clear justification
- Default: openness; exception: closure with documented reason

**Infrastructure emerging:**
- Field-specific: OpenfMRI, INDI, OASIS
- General: Dataverse Network, Dryad
- Some journals requiring data deposit

#### Open Methods and Tools

**Why needed:**
- Published methodology lacks sufficient detail for replication
- Many factors unreported: room temperature, experimenter identity, time of day, verbal vs. written instructions
- Paradigm-driven research requires precision in intentional modifications

**Solutions:**
- Video of experimental setting and procedure
- Figshare for archiving data and methods
- Open Science Framework for project management and archiving
- Makes methods citable contributions (not just papers)
- Enables reuse, reducing wasted effort recreating tools

#### Open Workflow

**Principle:**
- Scientific workflow (study registration, analysis plans, results) should be transparent
- Accountability mechanism: knowing someone could look improves practices

**Model:**
- [[clinicaltrials.gov]]: registry for clinical trials
- 2005: ICMJE required preregistration of RCTs
- Evidence: 31% of registered trials showed discrepancies with published outcomes; 82% favored significant results

**Benefits:**
- Clarifies confirmatory vs. exploratory findings (reduces hindsight bias and HARKing)
- Reveals file-drawer problem (what research was done but not published?)
- Makes false outcome reporting harder to hide

**Addresses hindsight bias:**
- Without registry, researchers (and readers) reconstruct what was planned based on what was found
- Registry separates: "What did we hypothesize?" from "What did we discover?"
- Both are valuable; discovery should be labeled as such

## Key Concepts Introduced or Developed

- [[Motivated Reasoning]]: Using reasoning to justify conclusions we already want to reach
- [[Conflict of Interest]]: Personal incentives (publishing) vs. institutional goals (accuracy)
- [[File-Drawer Problem]]: Selective reporting of positive results; negative results hidden
- [[P-hacking]]: Multiple analysis choices that inflate false positive rate
- [[Replication Crisis]]: Growing realization that many published findings are false
- [[Open Science]]: Transparency in data, methods, workflow to improve accountability
- [[Registered Reports]]: Pre-registration of hypotheses and analysis plans

## Relation to Prior Work

**Follows from:**
- [[Nosek and Bar-Anan 2012 - Scientific Utopia I|Scientific Utopia I]] (same year): proposes opening scientific communication
- [[John, Loewenstein, & Prelec 2012]]: Measuring prevalence of questionable research practices
- [[Simmons, Nelson, & Simonsohn 2011]]: False-positive psychology
- Greenwald (1975), Rosenthal (1979): Long-standing concerns about publication bias

**Influences and is cited by:**
- [[Munafò et al. 2017]]: Manifesto for reproducible science
- [[LeBel et al. 2018]]: Credibility framework
- [[Open Science Collaboration 2015]]: Reproducibility of psychological science project

## Critical Arguments

1. **On why solutions must address incentives, not just education:** People aren't untrustworthy; they're human. Accuracy motives are abstract and distal; publishing incentives are concrete and immediate. Changing practices requires making accuracy competitive with publishing.

2. **On replication as fundamental to science:** From Bacon to present, replication is the demarcation criterion between science and non-science. Its dismissal as "not newsworthy" is a fundamental error.

3. **On the conflict of interest:** Scientists have strong accuracy motives, but under present incentives, getting it published wins out when the two conflict. The solution isn't to eliminate professional incentives but to restructure them.

## Practical Implementation

The authors model the advice they give:

- Post unpublished manuscripts on personal web pages and repositories (SSRN)
- Share study materials and tools publicly
- Contribute data to repositories (Dataverse Network)
- Help design Open Science Framework for comprehensive project management

## Concluding Insight

> "Openness is not needed because we are untrustworthy; it is needed because we are human."

The paper reframes the problem: not fraud or incompetence, but ordinary human psychology meeting misaligned incentives. The solution is structural (changing what we reward) and transparent (making it easier to see what we're doing).

## Impact and Legacy

Published in 2012, this paper became foundational to the open science movement. It connected the replication crisis to incentive structures and proposed concrete, implementable reforms. Unlike previous calls for better practices, it acknowledged the power of incentives and proposed soluti