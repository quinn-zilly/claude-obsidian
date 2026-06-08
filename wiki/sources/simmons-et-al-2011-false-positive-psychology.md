---
type: source
address: c-000643
title: "False-Positive Psychology: Undisclosed Flexibility in Data Collection and Analysis Allows Presenting Anything as Significant"
author:
  - "[[Joseph P. Simmons]]"
  - "[[Leif D. Nelson]]"
  - "[[Uri Simonsohn]]"
year: 2011
publication: "Psychological Science"
volume: 22
issue: 11
pages: "1359–1366"
doi: "10.1177/0956797611417632"
tags:
  - open-science
  - research-methods
  - replication-crisis
  - questionable-research-practices
  - statistics
status: evergreen
related:
  - "[[Researcher Degrees of Freedom]]"
  - "[[P-hacking]]"
  - "[[Questionable Research Practices]]"
  - "[[Preregistration]]"
  - "[[Replication Crisis]]"
  - "[[Motivated Reasoning]]"
  - "[[kerr-1998-harking]]"
  - "[[Open Science MOC]]"
created: 2026-06-08
updated: 2026-06-08
---

# False-Positive Psychology

> [!abstract] One-line
> The paper that coined **[[Researcher Degrees of Freedom]]** and showed that undisclosed analytic flexibility lets researchers present *anything* as statistically significant — then proposed a low-cost disclosure fix.

A field-defining methods paper by [[Joseph P. Simmons]], [[Leif D. Nelson]], and [[Uri Simonsohn]]. It is one of the founding documents of the [[Replication Crisis]] reform movement, supplying both the diagnosis (researcher degrees of freedom) and an early, practical remedy (disclosure requirements).

## Core argument

Psychologists nominally accept a 5% false-positive rate ($p \le .05$), but **flexibility in data collection, analysis, and reporting drives the *actual* false-positive rate far higher**. Because researchers face many ambiguous, defensible analytic choices and are motivated (via [[Motivated Reasoning]]) to reach significance, they explore alternatives and report only "what worked." Running many implicit tests while reporting one inflates false positives well beyond .05.

## The four researcher degrees of freedom (simulations)

15,000 simulations per scenario, normal data, two-condition design, 20 obs/cell baseline. False-positive rate at $p < .05$:

| Researcher degree of freedom | FP rate |
|---|---|
| A: two correlated DVs (r = .50) | 9.5% |
| B: add 10 obs/cell then re-test (optional stopping) | 7.7% |
| C: control for gender / gender × treatment | 11.7% |
| D: drop one of three conditions | 12.6% |
| A + B | 14.4% |
| A + B + C | 30.9% |
| **A + B + C + D (all four)** | **60.7%** |

Using all four common degrees of freedom, **a researcher is more likely than not (61%) to obtain a false positive.** The authors note these estimates are *conservative* — they omit many other common RDFs (more DVs, more covariates, trial/participant exclusions, pilot-vs-proper ambiguity). Optional stopping alone, tested after every observation starting from n=10, hits ~22%.

## The demonstration: "chronological rejuvenation"

To prove the point on a deliberately absurd hypothesis, the authors ran two real experiments showing songs change listeners' age. **Everything reported actually happened.**

- **Study 1:** "Hot Potato" (The Wiggles) made undergrads *feel* older than control "Kalimba." ANCOVA controlling for father's age, $F(1,27)=5.06$, $p=.033$.
- **Study 2:** "When I'm Sixty-Four" (Beatles) made people *chronologically younger* (by birth date) than "Kalimba," $F(1,17)=4.92$, $p=.040$ — a necessarily false result.

The Study 2 effect only "worked" via undisclosed RDFs: father's age as covariate (without it, $p=.33$), optional stopping (re-tested every ~10 participants, no ex-ante rule), n<20/cell, and a long list of redacted measures (see Table 3).

## The solution: disclosure, not new statistics

The fix is transparency, imposing minimal burden. **Six requirements for authors:**

1. Decide and report the data-collection termination rule **before** collecting.
2. Collect ≥20 observations per cell (or justify the cost).
3. List **all** variables collected (begin with "only").
4. Report **all** experimental conditions, including failed manipulations.
5. If observations are excluded, report results **with** them included too.
6. If a covariate is used, report results **without** it too.

**Four guidelines for reviewers:** enforce the requirements; tolerate imperfect/messy results (distrust suspiciously perfect underpowered studies); require robustness across arbitrary analytic choices; if justifications are weak, require an exact replication.

The mechanism turns inconsequential **sins of omission** into career-threatening **sins of commission**, realigning incentives toward honesty.

## Rejected non-solutions

- **Correcting alpha (Bonferroni-style):** unclear which/how many RDFs apply; adjustment introduces new RDFs.
- **Bayesian statistics:** *increases* RDFs (new analyses to try; prior choices).
- **Conceptual replications:** don't bind analytic choices across studies — actively misleading (it's what the authors themselves did).
- **Posting materials/data:** too costly for readers/reviewers to audit in real time; redaction could extend to the data too.

## Why this source matters

- Coins and operationalizes **[[Researcher Degrees of Freedom]]** — the keystone concept for [[P-hacking]] and [[Questionable Research Practices]].
- A foundational driver of the [[Preregistration]] movement (Requirement 1 is preregistration in embryo).
- The self-parody demo made the abstract problem viscerally legible and is among the most-cited methods papers in psychology.

## Links

- Concept: [[Researcher Degrees of Freedom]]
- Related QRPs: [[P-hacking]], [[HARKing]], [[Questionable Research Practices]], [[File-Drawer Problem]]
- Remedies: [[Preregistration]], [[Registered Reports]]
- Context: [[Replication Crisis]], [[Motivated Reasoning]]
- Map: [[Open Science MOC]]
