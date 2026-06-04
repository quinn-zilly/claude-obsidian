---
address: c-000180
type: source
title: "Judgment under Uncertainty: Heuristics and Biases"
author:
  - "[[Amos Tversky]]"
  - "[[Daniel Kahneman]]"
year: 1974
venue: "Science, Vol. 185, No. 4157, pp. 1124–1131"
doi: "https://www.jstor.org/stable/1738360"
tags: [source, judgment, heuristics, biases, decision-making, cognitive-psychology]
status: mature
created: 2026-05-23
updated: 2026-05-23
related:
  - "[[Representativeness Heuristic]]"
  - "[[Availability Heuristic]]"
  - "[[Anchoring and Adjustment]]"
  - "[[Base Rate Neglect]]"
  - "[[Gambler's Fallacy]]"
  - "[[Illusion of Validity]]"
  - "[[Regression to the Mean]]"
  - "[[Illusory Correlation]]"
  - "[[Heuristics and Biases Program]]"
  - "[[Amos Tversky]]"
  - "[[Daniel Kahneman]]"
---

# Judgment under Uncertainty: Heuristics and Biases

Tversky & Kahneman (1974). *Science*, 185(4157), 1124–1131.

> [!key-insight] Core claim
> People rely on a limited number of heuristic principles that reduce complex probability assessment to simpler judgmental operations. These heuristics are generally useful but lead to **severe and systematic errors** — errors that persist even in trained researchers thinking intuitively.

## Summary

8-page article (the founding document of the [[Heuristics and Biases Program]]) identifying three cognitive shortcuts people use to assess probabilities and predict values. Each heuristic is adaptive in many contexts but produces predictable biases when it misfires. The paper is empirical-demonstrative — it presents experimental vignettes and data as evidence for each claim.

The central analogy: probability judgment resembles perceptual judgment of physical quantities (distance, size). Both rely on heuristic cues with limited validity; both yield systematic distortions. Relying on object clarity to estimate distance works most of the time but fails in fog (overestimates) and high visibility (underestimates). Heuristics for probability are structurally the same.

---

## Heuristic 1: Representativeness

**When used:** Judging probability that object/event A belongs to class B, or that process B generated event A.

**Mechanism:** Probability is assessed by the degree to which A *resembles* B (matches its stereotype or prototype). High resemblance → high judged probability; low resemblance → low judged probability.

**Canonical example:** "Steve is very shy and withdrawn, invariably helpful… a meek and tidy soul, he has a need for order and structure, and a passion for detail." People rank occupations by similarity to the stereotype, not by base-rate frequency — so "librarian" beats "farmer" even though farmers vastly outnumber librarians.

**Biases produced:**

| Bias | Description |
|------|-------------|
| [[Base Rate Neglect]] | Prior probabilities ignored when any descriptive information is present — even uninformative ("Dick is 30, married, high ability") information wipes out base-rate sensitivity |
| Insensitivity to sample size | Judged probability of a sample statistic is independent of N; "law of small numbers" — researchers over-trust small samples |
| Misconceptions of chance | Local representativeness: H-T-H-T-T-H feels more "random" than H-H-H-T-T-T; leads to [[Gambler's Fallacy]] |
| Insensitivity to predictability | Predictions mirror evaluation of favorableness of description regardless of reliability or predictive validity |
| [[Illusion of Validity]] | High confidence produced by good match between input and predicted outcome, even when accuracy is known to be low |
| Misconceptions of regression | [[Regression to the Mean]] not intuited; spurious causal stories invented to explain it |

**Key finding (engineers/lawyers):** Subjects told group was 70% engineers vs. 30% engineers gave essentially identical probability judgments for the same personality description, violating Bayes' rule (correct ratio of odds should be 5.44:1). When *no* description was given, base rates were used correctly. When an *uninformative* description was given, base rates were ignored entirely.

**Hospital study (sample size):** Large hospital (45 births/day) vs. small hospital (15 births/day). Which records more days with >60% boys? 53% said "about the same"; correct answer is the small hospital (larger variance with smaller N). Fundamental sampling principle not in people's intuitive repertoire.

**Instructor fallacy (regression):** Flight instructors conclude punishment works better than praise because praised good landings are followed by worse ones and criticized poor landings are followed by better ones — pure regression to the mean, causally misattributed.

---

## Heuristic 2: Availability

**When used:** Assessing frequency of a class or probability of an event.

**Mechanism:** Frequency/probability estimated by the ease with which instances can be brought to mind (retrieved, constructed, or associated).

**Why it works:** Instances of frequent classes are indeed recalled more easily. But ease of retrieval is also influenced by salience, recency, familiarity, and imaginability — factors unrelated to actual frequency.

**Biases produced:**

| Bias | Description |
|------|-------------|
| Retrievability bias | More famous names judged more numerous (sex-famous personality lists: the gender with more famous names judged larger even when equal in count) |
| Search set bias | Words starting with R judged more common than words with R in 3rd position — opposite of reality; search by first letter is easier |
| Imaginability bias | Small committees seem more numerous than large ones because it's easier to mentally construct them; committees of 2 estimated at 70, committees of 8 at 20 (correct: 45 both) |
| [[Illusory Correlation]] | Co-occurrence of events judged by strength of associative bond; clinical lore (suspiciousness → peculiar eyes) "rediscovered" in data where correlation was actually negative |

**Real-world implication:** Risk assessment for complex projects or expeditions is inflated by vividly imaginable dangers and deflated by hard-to-conceive hazards — neither systematically related to actual probability.

---

## Heuristic 3: Anchoring and Adjustment

**When used:** Numerical estimation when a starting value is available (given externally or from partial computation).

**Mechanism:** Estimates begin from an anchor and are adjusted toward a final answer. Adjustments are systematically insufficient — final estimates stay too close to the starting point.

**Biases produced:**

| Bias | Description |
|------|-------------|
| Insufficient adjustment | Wheel-of-fortune anchor (random 10 or 65) → median estimates of % African UN members: 25 vs. 45; arbitrary anchors shift estimates even when subjects know they're arbitrary |
| Factorial product underestimation | 8×7×6×5×4×3×2×1 median = 2,250; 1×2×3×4×5×6×7×8 median = 512; correct = 40,320; descending sequence anchors on a larger partial product |
| Conjunctive event overestimation | P(all 7 draws red from 90% urn) = .48 preferred over P(single draw red from 50% urn) = .50; anchoring on elementary event probability, under-adjusting downward |
| Disjunctive event underestimation | P(at least 1 red in 7 draws from 10% urn) = .52 avoided in favor of .50 simple event; anchoring leads to under-adjusting upward |
| Overconfident probability distributions | Experts' confidence intervals are too narrow (actual values outside stated X₀₁–X₉₉ interval ~30% of the time vs. expected 2%); anchoring on best estimate and under-adjusting outward |

**Planning fallacy implication:** Complex undertakings (new product development) have conjunctive structure — all N steps must succeed. Even if each step is 90% likely, P(success) < 0.35 for 12 steps. Anchoring on elementary step probability causes unwarranted optimism.

**Risk assessment implication:** Complex systems (nuclear reactor, human body) have disjunctive failure structure — failure if *any* component fails. Anchoring on individual component probability causes underestimation of overall failure risk.

---

## Discussion Points

- Biases are **not motivational** (not wishful thinking); they persist with accuracy incentives and financial payoffs for correct answers.
- Biases affect **experienced researchers** thinking intuitively, not just naive subjects. Sophisticated respondents avoid elementary errors (gambler's fallacy) but show same biases in more opaque problems.
- Statistical principles are **not learned from experience** because relevant instances are not coded appropriately (no one tracks average word length per line; no one groups predictions by assigned probability to check calibration).
- Subjective probability coherence (internal consistency) is insufficient for rationality — must also be compatible with the full web of one's beliefs.

---

## Key Quotes

> "These heuristics are quite useful, but sometimes they lead to severe and systematic errors."

> "Chance is commonly viewed as a self-correcting process in which a deviation in one direction induces a deviation in the opposite direction to restore the equilibrium. In fact, deviations are not 'corrected' as a chance process unfolds, they are merely diluted."

> "The human condition is such that, by chance alone, one is most often rewarded for punishing others and most often punished for rewarding them."

> "Statistical principles are not learned from everyday experience because the relevant instances are not coded appropriately."

---

## Pages Created

[[Amos Tversky]] | [[Daniel Kahneman]] | [[Representativeness Heuristic]] | [[Availability Heuristic]] | [[Anchoring and Adjustment]] | [[Base Rate Neglect]] | [[