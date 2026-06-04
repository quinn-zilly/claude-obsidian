---
address: c-000350
type: concept
title: "Ant Colony Optimization (Scale Shortening)"
tags: [concept, psychometrics, scale-development, short-forms, algorithms]
status: evergreen
created: 2026-06-01
related: ["[[Likert Scale Development]]", "[[Item Response Theory]]", "[[Coefficient Omega]]", "[[jebb-ng-tay-2021-likert-scale-advances]]"]
---

# Ant Colony Optimization (Scale Shortening)

Nav: [[index]] | [[log]]

## What It Is

A computational algorithm (Dorigo 1992; Dorigo & Stützle 2004) adapted for psychology to create optimal short forms of longer scales. Introduced to psychology by Leite et al. (2008).

## The Ant Analogy

Ants find the shortest path to food by: (a) randomly sampling paths and (b) laying pheromones that attract other ants. Better paths accumulate pheromone faster → positive feedback loop → convergence on optimal path. ACO mirrors this: items are "paths," statistical performance metrics are "pheromones."

## How It Works

1. Randomly sample N items from the full scale (target short-form length = N)
2. Evaluate the short form on one or more criteria (reliability, CFA fit, criterion correlation, etc.)
3. Increase selection probability ("pheromone") for items that performed well
4. Repeat over many iterations until convergence

Unlike exhaustive search, ACO does not test all possible subsets — it uses probabilistic guided search.

## Advantages Over Alternatives

Olaru et al. (2015) compared ACO to: maximizing factor loadings, minimizing modification indices, genetic algorithm, PURIFY. For a mixture of criteria (CFA fit, latent correlations), ACO equaled or surpassed all alternatives. Key insight: maximizing factor loadings alone leads to items with *similar content* (attenuation paradox — Loevinger 1954), reducing content coverage.

## Real-World Uses

- Proactive personality and supervisor support scales (Janssen et al. 2015)
- Psychological situational characteristics (Parrigon et al. 2017)
- Big Five short forms (Olaru et al. 2015; Olderbak et al. 2015)
- Schroeders et al. (2016) — further comparisons

## Limitations & Requirements

1. **Does NOT guarantee content coverage** — final items must always be manually reviewed for sufficiency
2. Requires specifying an external criterion variable — results depend on this choice
3. Requires subjective judgment on "sufficient content"
4. Authors must report: (a) evaluation criteria, (b) how criteria map to pheromone weights, (c) software, (d) number of iterations

## Software

R package — see Leite et al. (2008); Jebb et al. (2021) Supplementary Material provides full walkthrough.

## Key Papers
- Dorigo (1992), Dorigo & Stützle (2004) — original algorithm
- Leite et al. (2008) — introduction to psychology
- Olaru et al. (2015) — comparison study
- Janssen et al. (2015) — real-scale application
- Schroeders et al. (2016) — further comparisons
- Marcoulides & Drezner (2003) — additional resources

## Sources
- [[jebb-ng-tay-2021-likert-scale-advances]]
