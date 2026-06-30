---
type: source
address: c-000192
title: "Judgment and Decision Making"
author:
  - "[[Terry Connolly]]"
  - "[[Lisa Ordóñez]]"
  - "Steven Barker"
year: 2012
source_file: ".raw/Connolly et al. - 2012 - Judgement and Decision Making.pdf"
venue: "Handbook of Psychology (2nd ed.), Vol. 12: Industrial and Organizational Psychology, Ch. 19"
tags: [source, jdm, decision-making, judgment, heuristics, prospect-theory, emotion, groups]
status: ingested
created: 2026-05-23
updated: 2026-06-30
---

# Connolly, Ordóñez & Barker (2012) — Judgment and Decision Making

Chapter 19 of Weiner's *Handbook of Psychology* (2nd ed., Vol. 12, Industrial and Organizational Psychology). A selective, application-oriented survey of the judgment-and-decision-making (JDM) field, written for an organizational-psychology audience by [[Terry Connolly]] and [[Lisa Ordóñez]] (both Arizona) with Steven Barker. The authors are explicit that the chapter is *not* comprehensive: they bias toward "actual or potential application rather than toward theory building," flag methodology only where it is "special to, or especially serious for, JDM," and allow themselves room to speculate on where the field is heading.

> [!abstract] One-line takeaway
> JDM is irreducibly two fields at once — a descriptive science of how people actually judge and choose, and a normative/prescriptive enterprise about how they *should*. The chapter's organizing claim is that the two cannot be pursued separately: serious descriptive work keeps surfacing normative questions, and prescriptive models are only as good as the psychological realism of their assumptions.

## The Central Tension: Descriptive vs. Normative/Prescriptive

JDM "includes elements of both description and prescription" more than almost any other area of human science. The prescriptive thread descends from 18th-century French court mathematicians pricing gambles (via Bernstein, Stigler); the descriptive thread is younger, effectively launched by Edwards' (1954, 1961) review papers. Connolly et al. argue the two themes are *built into the subject matter*: study how a physician makes a hard diagnosis and you cannot help asking the evaluative questions — is she right? could a computer do better? how could she be helped? Conversely, a decision analyst's "optimal" investment advice is only actionable if the manager can actually state coherent preferences and probabilities and trust the analysis enough to act.

This interplay is the field's main source of interest — but the authors warn it bred an "undue interest in decision errors." They push back hard on the error-cataloguing reflex: an observed "error" exists *only if* the invoked normative rule is genuinely appropriate and accepted, and most error studies never assessed how *general* or how *frequent* the errors are in the wild. Their stance is even-handed rather than debunking: when handed a normative recommendation, always ask whether its assumptions are descriptively accurate; when handed a descriptive finding, always ask how well the person is actually doing.

> [!key-insight] Editorial posture
> The chapter's skepticism toward the heuristics-and-biases "error catalog" is itself a substantive position, and it recurs in every section — policy capturing is "widely abused," sunk-cost effects may be "several rather different effects" lumped together, confirmation bias is largely a misread "positive-test strategy," and so on. This is a survey written by authors who distrust tidy bias inventories.

## 1. Inference Processes

### The Lens Model

[[Lens Model]] (Brunswik 1952, extended to judgment by Hammond 1955). Brunswik diagrammed perception as the integration of multiple imperfect **cues** — none perfectly correlated with the true quantity, but redundantly informative — into a valid estimate, like a convex lens focusing diverging rays. Hammond's move was to treat *judgment* the same way: a job applicant's true ability is inferred from cues (test scores, references, claimed experience). The model's great value is that it puts **judge and environment on the same picture simultaneously**: accuracy requires both that cues be informative about the criterion *and* that the judge weight them well. The Lens Model Equation (Tucker 1964) decomposes overall achievement into these components.

A core methodological precept is **representative design** (Brunswik 1955): cue sets shown to subjects must preserve the cue ranges and intercorrelations of a real environment. This forbids factorial/orthogonal crossing of cue values — orthogonal designs destroy naturally occurring intercorrelations and can produce cue combinations the judge "finds incredible" (e.g., applicants whose test scores, GPA, and references are mutually uncorrelated would strike a real employer as fraudulent).

### Multiple-Cue Probability Learning (MCPL)

A large literature — in "more-or-less complete violation" of representative design — tested whether people can *learn* to use probabilistic cues from trial-by-trial outcome feedback. The verdict: except for the simplest tasks, MCPL is **very hard to learn**. "Simple" means one or two cues, strongly and linearly related to the criterion, under low feedback error:

- Slovic (1974): a single linear cue at r = 0.80 → near-optimal performance by trial 100. But flip the cue validity to −0.80 and learning after 100 trials is less than half that.
- Deane, Hammond & Summers (1972): a three-cue task is learned reasonably in ~150 trials when all relations are positive, but almost not at all when relations are U-shaped. Warning subjects about nonlinearities helps somewhat (Earle 1970); two-cue interactions are learned only with helpful verbal hints (Camerer 1981).
- Connolly & Miklausich (1978): even after high performance under low-error feedback, performance collapses when feedback error rises.

As Klayman (1988) put it, outcome feedback is **"learning the hard way."** The organizational kicker: real-world feedback is *worse* than the lab's — it is delayed (you learn about a hire only after months on the job), noisy (supervisor ratings add error), and crucially **truncated** (you only observe the applicants you actually hired; cf. Einhorn 1980 on waiters who "know" they can spot good tippers). So outcome feedback is unlikely to be the route to real-world expertise, and lab interest in MCPL has largely subsided.

### Policy Capturing

[[Policy Capturing]] (a.k.a. judgment analysis, Stewart 1988): build a quantitative — usually first-order linear regression — model of a *specific* person making a *specific* judgment (e.g., a department head scoring grad applications 0–100). Widely used in organizational settings: salary raises, alternative work arrangements, cross-cultural compensation, applicant ratings. But "widely abused": the approach looks trivially simple, which hides subtleties that vitiate conclusions. Cue identification is itself hard — asking judges what cues they use can mislead (they may be unaware of, or unwilling to admit, a bias toward/against women, minorities, left-handers), and coding what counts as a "strong" GPA takes real work. The deepest unsolved problem is again **representative design**: orthogonal cue designs are prohibited, but the right environment to sample is conceptually slippery (comparing predictions to actual performance restricts you to the *hired* subset, whose cue ranges are truncated).

Robust generalizations (Brehmer & Brehmer 1988; Slovic & Lichtenstein 1971) — to be treated as *working hypotheses, not settled fact*:

- Judges use **few cues**, well-modeled by simple linear first-order models.
- Judges *describe themselves* as using cues in complex, nonlinear, interactive ways.
- Judges show only **modest test–retest reliability**.
- Inter-judge agreement is often moderate-to-low even among established experts.

This last cluster motivates **bootstrapping** as decision aid: capture a judge's linear policy from past cases, then apply it mechanically to future ones — often *more reliable than the judge herself*.

### Heuristics and Biases

[[Heuristics and Biases Program]] (Tversky & Kahneman). The paradigm grew from "conservatism" findings (Edwards 1968: subjects revise toward the Bayesian direction but insufficiently) into the dominant 1970s–80s account of judgment under uncertainty. Its three ingredients: a well-structured probabilistic task, a sensible normative model (often Bayes), and a *systematic* deviation. Crucially the program was "more than a simple catalog" — Tversky & Kahneman argued the errors were manifestations of generally-effective, low-cost cognitive shortcuts (availability, representativeness, anchoring) that misfire in unusual circumstances.

Connolly et al. document its **decline**, for three reasons: (1) it became an ever-growing error catalog with little theory predicting *when* a heuristic fires; (2) growing doubt about whether the invoked normative models were appropriate; (3) recognition that some "errors" were subjects solving a *different problem* than the experimenter intended. The center of gravity shifted toward studying the mechanisms behind good performance, including expert performance in real settings. (Cf. [[Replication Crisis]] — the paradigm's waning prefigures later replication concerns.) See [[tversky-kahneman-1974-heuristics-biases]] for the founding paper.

## 2. Prediction

The three prediction heuristics, with mechanisms and organizational cases:

**Anchoring and adjustment.** Start from an anchor (e.g., current sales), adjust for trends. Two failure modes: the anchor may be *wrong* (using all-staff average when a new incentive hit only a subset), and adjustment is typically *insufficient* (Bolger & Harvey 1993). Epley & Gilovich (2006) locate the mechanism in **inadequate search effort** — at least when the subject generated the anchor themselves — which incentives and forewarnings can partly overcome.

**Availability.** Likelihood judged by ease of recall/imagination. Misfires when we attend to vivid or recent instances over base rates: people who recently experienced a disaster overestimate similar future events (Kunreuther et al. 1978); performance appraisals overweight vivid episodes from the prior ~3 months (Bazerman 1998). Encouragingly, people can *discount* availability when the source of the bias is made obvious to them (Oppenheimer 2004; Sjöberg & Engelberg 2010).

**Representativeness.** Likelihood judged by similarity to a stereotype. Spawns: the gambler's fallacy (expecting small samples to mirror the population); **nonregressive prediction** from unreliable predictors; and **base-rate neglect**. The worked drug-test example is the chapter's centerpiece: 1% of employees use drugs, a test is 90% accurate, yet **P(user | positive) = 8.3%** — because real users are so rare that most positives are false. The Israeli flight-instructor case (Tversky & Kahneman 1974) is pure regression-to-the-mean misread as causation: praise "hurts" and reprimands "help" only because performance after an extreme episode regresses anyway. The same fallacy underlies the belief that this year's top salesperson will top next year's list, and investors' faith in past stock performance.

**[[Overconfidence]].** Subjective confidence intervals are far too narrow — Klayman et al. (1999) found ~45% miss rates for 90%-intervals vs. ~5% for two-choice items. Overconfidence is **stable across domains within a person** (overconfident about shampoo prices → overconfident about life expectancies), men > women in investment (Barber & Odean 2001 — men traded more and earned less), and it appears in managers' new-product decisions (Simon & Houghton 2003). It *declines* with experience (Keren 1987) and with the instruction to **"think of ways the estimate might be wrong"** (Fischhoff 1982) — a rare, portable debiasing lever with direct payoff for timelines, costs, and strategy.

**Learning failures.** [[Hindsight Bias]] (Fischhoff & Beyth 1975) — the "knew-it-all-along" effect — destroys the pre-event uncertainty needed to learn the true decision→outcome relationship. Bare warnings don't help; inducing people to generate reasons they might be wrong does (Fischhoff 1977), and a source-confusion procedure (Marks & Arkes 2010) may debias. Compounding this, confirmation bias (Wason 1960) and the naturally **hidden structure** of feedback (we rarely observe outcomes for applicants we *didn't* hire) starve us of disconfirming data.

**Idea generation / brainstorming.** Before you can predict an outcome you must *generate* it, and we under-generate (Gettys & Fisher 1979). Osborn's (1953) face-to-face (F2F) brainstorming is intuitively appealing but inferior: **nominal groups** (the same number of people working alone) produce more ideas at equal quality (McGrath 1984), chiefly because of **production blocking** — only one person can speak at a time, so others forget or self-censor (Diehl & Stroebe 1987). Electronic brainstorming (EBS), where members type simultaneously and read each other's files, overcomes blocking and beats nominal groups when groups are large (~8+); anonymity raises idea quantity and the number of controversial ideas (Connolly, Jessup & Valacich 1990) but can lower task satisfaction. Yet businesses keep using F2F — partly intuitive appeal, partly equipment access, and partly because managers value **group well-being and member support** (Dennis & Reinicke 2004) over raw idea count. A telling bias: subjects *predict and perceive* F2F as superior even when nominal groups objectively outperformed (Paulus et al. 1993).

## 3. Preferences

### Constructed, Not Retrieved

Following Fischhoff (1991), the chapter sides against the "articulated values" assumption (that people carry fully-formed preferences for all states): for most unfamiliar choices, preferences are **constructed** from a few basic values, and the construction is sensitive to **framing, timing, order, and context**:

- Medical-treatment preferences flip with mortality-vs-survival framing (McNeil, Pauker & Tversky 1988).
- Willingness-to-pay to clean Ontario lakes was ~the same for one, several, or all lakes (Kahneman, Knetsch & Thaler 1986) — scope insensitivity.
- Snack preferences predicted a week ahead diverge from those at consumption (Simonson 1990).
- Life-satisfaction ratings were unrelated to dating frequency when asked in that order, but strongly correlated (r = 0.66) when dating was asked first (Strack et al. 1988).
- MBA students' satisfaction with and fairness of salary offers shifted with *peers'* offers (Ordóñez, Connolly & Coughlan 2000) — a comparison effect.

The open question: is this imperfect *measurement*, or imperfect *development* of the preferences themselves?

### Utility, Value Trees, and Comparison

"Utility" is used two ways: the formal von Neumann–Morgenstern sense (numbers summarizing transitive, consistent choices via "probabilistic in-betweenness") and the looser psychological sense of felt desirability. Many people reject positive-EV bets (e.g., 0.5 win $10 / 0.5 lose $5, EV +$2.50) — **risk aversion** plausibly explained by declining marginal utility, though that "may have little connection to the actual churn of feeling the gambler experiences." Risk tolerance as a *stable personality trait* finds little support (Lopes 1987). Complex values organize into **value trees / hierarchies** (Edwards & Newman 1982): high-level goals (job knowledge, motivation, growth potential) decompose into operational measures. **Comparison processes** are central — a $3,000 raise feels different if a rival got more or less, if you expected $5,000, or if it was merit vs. cost-of-living — linking to equity theory (Adams 1965; Greenberg 1988's status-office field study) and to regret/disappointment theories below.

### Choice Rules and the Effort–Accuracy Tradeoff

| Rule | Compensatory? | Mechanism |
|---|---|---|
| [[Multiattribute Utility Theory]] (MAUT) | Yes | Weight × value across all attributes, sum, pick the max. Most normatively complete; most effortful. |
| **Satisficing** (Simon 1955) | — | Accept the first option acceptable on all important dimensions; aspiration level may shift during search. |
| **Conjunctive** | No | Any below-threshold attribute kills the option (army physical: flat feet → reject). |
| **Lexicographic** | No | Compare on the most important attribute; ties broken by the next; sequential. |
| **Elimination by Aspects (EBA)** (Tversky 1972) | No | Pick an aspect (probabilistically), eliminate options failing its threshold; repeat. |
| **Additive difference** (Tversky 1969) | Yes | Compare one dimension at a time, accumulate signed differences. |

The unifying frame (Payne, Bettman & Johnson 1993): rule choice is an **effort–accuracy tradeoff**. Full MAUT maximizes consideration but demands heavy processing; cheaper non-compensatory rules save effort but don't guarantee the best option. Decision makers adaptively switch rules to manage that tradeoff.

## 4. Deciding: Single-Choice Events

### From EV to SEU

Expected Value (EV = Σ pᵢxᵢ) is the simplest valuation but a poor descriptive *and* normative guide for single cases. The **St. Petersburg Paradox** (Bernoulli 1738) — a coin-flip game paying $2ⁿ has infinite EV yet most people pay < $4 — drove Bernoulli to **subjective value (utility)**: people value prospects by u(x), not x. von Neumann & Morgenstern (1947) axiomatized **Expected Utility** (EU = Σ pᵢu(xᵢ)); Savage (1954) added **subjective probabilities**, yielding **Subjective Expected Utility (SEU)** = Σ s(pᵢ)u(xᵢ) — the normative standard, extending decision theory from objective-probability gambles to belief-based uncertainty.

### Prospect Theory

[[Prospect Theory]] (Kahneman & Tversky 1979) keeps the "evaluate, discount, add" form but makes the value and probability functions psychologically descriptive, accommodating the **Allais Paradox** (an Independence-axiom violation) and Tversky's (1969) transitivity violations. Its value function:

1. Defined over **changes from a reference point** (often the status quo), not total wealth.
2. **Steeper for losses than gains** → **loss aversion** (losses hurt more than equal gains please).
3. **Concave (risk-averse) above** the reference point, **convex (risk-seeking) below** it.

Its **decision-weight function** overweights low probabilities and underweights high ones (Lichtenstein et al. 1978: rare risks like botulism overestimated, common ones like heart disease underestimated) and is nonlinear (weights don't sum the way probabilities do).

### Framing

Because the same option can be cast against different reference points, **[[Framing Effects]]** follow directly from the value function's kinked shape. Risky-choice framing: Hogarth's (1987) MBAs preferred a riskless option when outcomes were "money saved" but the risky option when "losses" — **risk-averse in gains, risk-seeking in losses**. Attribute framing on riskless options: ground beef rated better as "75% lean" than "25% fat" (Levin & Gaeth 1988, though the gap shrank after tasting); the credit-card lobby's "cash discount" vs. "surcharge" (Thaler 1980). Kuvaas & Selart (2004) suggest negative framing may work by *stimulating more effortful processing*, not merely shifting valence — a mechanism that matters for whether framing is "bias" or signal.

### Non-SEU Models

- **[[Image Theory]]** (Beach 1990): the decision maker maintains consistency among a *value image*, *trajectory image*, and *strategic image*; most action is **screening** options against the value image for compatibility (counting "violations"), with explicit comparative evaluation (the "profitability test") reserved for the rare case where several options survive.
- **SP/A model** (Lopes 1987): "security-potential/aspiration." Assessing a gamble pits worst-case against best-case; *security-minded* people fixate on the downside (prefer tight outcome clusters), *potential-minded* on the upside (prefer wide spreads), modulated by an **aspiration level**. A full alternative to Prospect Theory that fits some data better (Schneider 1992).
- **[[Naturalistic Decision Making]] / RPD** (Klein; Orasanu & Connolly 1993): in complex, time-pressured, high-stakes, dynamic settings, experts use **recognition-primed decision** — rapid situation assessment, then selecting an action that *matches* the situation — "thinking much less, rapid matching much more." This may be a *different phenomenon* from deliberative "decision making" altogether: experts doing what they know differ from novices searching for any workable action.

### Signal Detection Theory

[[Signal Detection Theory (Decision)|Theory of Signal Detection (TSD)]] — rooted in WWII radar — is "largely ignored in JDM research" despite huge applied generality (crack detection, breast-cancer screening, hiring, HIV/drug/lie testing). It separates two things the decision maker controls separately: **system accuracy** (the ROC curve plotting true-positive vs. false-positive probability — pushing it up-and-left is a genuine accuracy gain) and **threshold placement** (where to act, which should depend on the **base rate** and on the *asymmetric costs* of false positives vs. false negatives). The HIV-test illustration is sharp: the right threshold for screening blood donations (a false positive merely wastes a pint) differs from that for telling a real patient they may have a life-threatening disease. Organizational uptake is thin — Puranam, Powell & Singh (2006) on M&A due diligence is a rare exception — making TSD "a promising research opportunity."

## 5. Emotion and Decision Making

Early JDM ran on a "mind as computer" model where emotion was noise or an active impediment. Two waves revised this.

**Valence-based (visceral) view.** Negative affect → more pessimistic expectations and **more analytic processing**; positive affect → more optimistic expectations and **more heuristic processing** (Forgas 2003; Schwarz & Clore 1983). Slovic et al.'s (2007) **affect heuristic** lets the felt good/bad of options drive evaluation directly, in place of weighing pros and cons.

**[[Appraisal-Tendency Framework]] (ATF)** (Lerner & Keltner 2000/2001). The key advance: emotions of the *same valence* have *different* effects, because each emotion carries distinct **appraisal dimensions** (Smith & Ellsworth's six: certainty, pleasantness, attentional activity, control, anticipated effort, responsibility) and core themes that bias subsequent, even unrelated, judgments:

- **Fear** (appraisals of uncertainty, low control) → more **risk-averse** risk estimates.
- **Anger** (certainty, individual control) → more **risk-seeking**; angry people see situations as *less* risky than fearful people (Lerner & Keltner 2001).
- **Sadness** vs. anxiety diverge (Raghunathan & Pham 1999: anxious → low-risk/low-reward; sad → high-risk/high-reward).
- **Disgust** can *eliminate the endowment effect* (Lerner, Small & Loewenstein 2004); **guilt** → more cooperation; **envy** → more deception in negotiation.
- Kugler, Connolly & Ordóñez (2012): the fear/anger risk pattern *reverses* when the risk source is other people's choices rather than chance.

**Integral vs. incidental.** *Integral* emotions attach to the decision itself and may have normative standing (anticipating regret over a choice is a legitimate input). *Incidental* emotions come from outside and have **no normative relevance**, yet carry over — e.g., weather-driven moods shifting college-admission weightings (Simonsohn 2007). Peters et al. (2006) catalog four roles for affect: information, common currency, spotlight, motivation.

### Regret and Decision Justification Theory

Regret/disappointment are the most-studied decision emotions. The **action effect** (Kahneman & Tversky 1982): 95% judged the investor who *switched* stocks and lost as more regretful than one who *held* and lost — suggesting bad outcomes of *action* sting more than identical outcomes of *inaction*, and an "omission bias" (e.g., parents deterred from vaccinating). But the picture is more complex: the action–regret link **reverses over time** (Gilovich & Medvec 1994 — short run we regret actions, long run we regret inactions), and reverses with *role framing* (entrepreneurs taking action are "justified"; Seta et al. 2001) and *prior experience* (switching brands is justified if the old brand was bad; Inman & Zeelenberg 2002).

[[Decision Justification Theory]] (Connolly & Zeelenberg 2002) resolves this by splitting regret into **two components**:

- **Outcome regret** — comparison of the actual outcome to a reference point (the unchosen alternative, the status quo, the expected outcome, or another person's outcome).
- **Process / self-blame regret** — was the decision itself *justified*?

DJT explains the moderators above as shifts in *justification*: changing a winning soccer team is unjustified (and regrettable), changing a losing one is justified (Zeelenberg et al. 2002); careful "vigilant" processes (Janis & Mann 1977) are regret-reducing across contexts (Reb & Connolly 2010, mothers' vaccination decisions).

The practical payoff is striking and runs *both directions*: making regret salient **improves decision processes**. Regret-primed subjects invested more effort, acquired more information, and made better choices (Reb 2008); regret priming drove more rational game play (Kugler, Connolly & Kausel 2009). But the *type* matters — unconscious **outcome-regret** priming caused "myopic regret avoidance" (rejecting painful feedback on unchosen options, impeding learning), while **process-regret** priming led subjects to accept feedback, learn, and earn more (Reb & Connolly 2009). And regret salience can **eliminate Reason-Based Choice Effects** (decoy, accept/reject, most-important-attribute; Shafir, Tversky & Simonson 1993) by prompting scrutiny of "shallow but nice-sounding rationales" — "a relatively rare example of a theoretically grounded technique that effectively eliminates a class of decision biases."

## 6. Deciding: Multiple Related Events

### Information Search and Purchase

When one decision's output is the next decision's information environment (ordering tests before diagnosing; commissioning a survey before a launch), the question becomes how much information to *buy*. Methodologies range from implicit cost (Russo & Dosher 1983 eye-tracking; Payne's 1976 information board; "Mouselab") to explicit cost (buying poker chips before betting which bag; Wason's four-card task). Findings (Einhorn & Hogarth 1981): partial sensitivity to normatively relevant variables (cost per chip, diagnosticity), but also sensitivity to **irrelevant** ones (information order, total information available); substantial monetary losses that persist with little learning; and *both* over- and under-purchase.

The applied bottom line: optimal purchase requires accurately assessing each source's accuracy, selecting the best subset, and combining optimally — all three hard — so real-world deviations are expected. Two organizational signatures: patients **under-purchase** (reluctance to seek second opinions before major treatment) while unstructured job interviews are a massive **over-purchase** of decision-*irrelevant* information (Guion 1975 on their "predictive uselessness") — and are used anyway. On confirmation bias, the chapter again resists the error reading: Klayman & Ha (1987) show the four-card pattern is a generally appropriate **positive-test strategy** that fails only in rare, specially-constructed cases.

### Sunk Costs and Escalation of Commitment

[[Sunk Cost Effect]]: prescriptively, sunk (unrecoverable) costs should be irrelevant to future decisions; descriptively we finish bad meals, sit through bad movies, and stay in failed relationships to avoid "wasting" the prior investment. Arkes & Blumer's (1985) clever field test: theater patrons who paid **full price** attended more performances than those given discounts (effect faded later in the season). Escalation appears organizationally — loan officers who made the *initial* problem-loan decision were likelier to keep funding it than officers who inherited it (Staw, Barsade & Koput 1997) — and in persuasion (foot-in-the-door; Freedman & Fraser 1966) and the NBA draft (Staw & Hoang 1995, though confounded by performance-model error).

The chapter's characteristic move: the explanations **conflict and may describe different effects**. Candidates include Prospect Theory's loss function (the sunk cost puts you below the reference point → risk-seeking → continue; Thaler 1980), a general **waste aversion** (Arkes 1996; Arkes & Ayton 1999), self-justification (Staw 1976), behavioral commitment (Kiesler 1971), decision-related regret (Ku 2008), and regulatory promotion/prevention (Higgins 2002). When project completion and expenditure are independently manipulated, only *completion* drives the effect (Conlon & Garland 1993). Verdict: "obviously worrying, possibly widespread," but probably "several rather different effects" wrongly lumped together.

### Dynamic Decision Making

[[Dynamic Decision Making]] (Edwards 1962): the decision maker acts repeatedly on an environment that responds to their actions *and* changes on its own. Hard for researchers (inherent complexity; the situation at time *t* is partly a consequence of the subject's *own* earlier choices, costing the experimenter control). Representative findings from simulated worlds:

- **Simulated medical diagnosis** (Kleinmuntz & Kleinmuntz 1981): computationally intensive Bayesian revision yielded only *modest* gains over a heuristic hypothesis-testing strategy, and even trial-and-error did well on some cases.
- **Firefighting / artificial worlds** (Brehmer 1990): subjects start poorly but learn with repeated play; **feedback delays impede learning substantially**, and opportunities to offset delay by decentralizing were mostly ignored.
- **System dynamics** (Sterman 1987, 1989): coupled feedback loops make response over time deeply non-intuitive — capital-budgeting subjects generated **large, costly oscillations** despite instruction in the system's linkages.

Findings tend to be task-specific and hard to aggregate (amateurs are overwhelmed; experts object to the unreality), and expert performance is often RPD-based rather than deliberative.

## 7. Multiple Decision Makers

### Group Decision Making

Groups can raise decision quality but at the cost of more complex processes — information must be shared, beliefs and preferences combined, conflict managed. **Information-flow impediments** (Thompson 2011): message tuning, the *curse of knowledge* (assuming receivers know what you know), the *transparency illusion*, the *uneven communication* problem (a few members dominate), and the **common information effect** (Gigone & Hastie 1997 — groups discuss what they already share). The sharpest failure is the **hidden profile** task (Stasser 1988): when the best option is identifiable only by *pooling members' unique* information, groups routinely miss it; requiring members to **rank-order** options rather than state a top choice helps (Hollingshead 1996).

Are groups better than individuals? **It depends on demonstrability** (Tindale 1993): if one solution can be unambiguously *shown* correct, groups adopt it; otherwise they decide by majority and individual errors survive (Tindale & Davis 1985). Groups don't reliably reduce biases — hindsight bias slightly reduced in one study but null in another (Bukszar & Connolly 1988); representativeness in the cab problem was *worse* in groups (Argote et al. 1986); groups can be *more* overconfident yet also *more* economically rational (lower ultimatum offers, more strategic signaling-game play). Kerr, MacCoun & Kramer (1996): biases can be smaller, equal, or larger in groups depending on the task, members' initial values, and the **aggregation rule** — formalized in the **Social Decision Scheme** model (Davis 1973). Heterogeneity of initial frames can *eliminate* framing effects in groups, but shared frames *polarize* (Yaniv 2011).

**Conditions that help:** member heterogeneity (personality, gender, experience) aids creativity and effectiveness (Jackson et al. 1995); delaying emotional expression until after alternatives are aired preserves group energy (Guzzo & Waters 1982); task cohesion offsets time pressure. The "wisdom of crowds" (Surowiecki 2004) needs diversity, independence, decentralization, and aggregation — but Kostakos (2009) found real rating crowds are dominated by a few experts, so crowd wisdom may really be **expert** wisdom. **Groupthink** (Janis 1972, Bay of Pigs) is the degradation case: highly cohesive groups under external threat and low self-esteem suppress realistic appraisal — though mere familiarity isn't sufficient to cause it (Watson et al. 1991 found long-working groups *more* effective).

### Group Decision Support Systems

GDSSs (networked, often anonymous systems) yield **more equal participation and task focus** but also **less interaction, more time, lower consensus, and lower satisfaction** (Hollingshead & McGrath 1995). Anonymity makes members more critical and probing (Jessup, Connolly & Tansik 1990) and can reduce the common-information effect (Shirani 2006). **Which is better, F2F or GDSS? It depends on the task** — GDSS wins for idea generation, F2F for problem solving and conflict resolution — and some GDSS benefit may come from the *structure it imposes* rather than the technology itself (Archer 1990 found no quality difference once a complex process was rationally managed). Caveats: much research uses ad-hoc student teams and needs replication on intact, experienced groups; organizations increasingly decide in **globally dispersed** groups requiring computer-mediated communication (Shim et al. 2002).

## Cross-Cutting Themes

> [!tip] What recurs across all eight sections
> 1. **Descriptive ⇄ normative tension** is the field's engine, and the authors distrust treating deviations as plain "errors."
> 2. **Feedback is the villain of learning** — delayed, noisy, truncated, and hidden — across MCPL, hindsight, dynamic DM, and information search.
> 3. **Construction over retrieval** — preferences, like emotional and regret effects, are assembled in the moment and shift with frame, reference point, and comparison.
> 4. **Specific beats valence** — the ATF/DJT move (distinct emotions, two-component regret) mirrors the field's maturation from coarse to mechanism-level accounts.
> 5. **Theoretically grounded debiasing is rare but real** — "consider how you might be wrong," vigilant process, and **regret salience** are the standout portable levers.

## Key Figures

- [[Terry Connolly]] — author; U of Arizona; regret/DJT, electronic brainstorming, dynamic DM, information purchase.
- [[Lisa Ordóñez]] — author; U of Arizona; regret, equity, emotions and framing in decisions.
- [[Daniel Kahneman]] — [[Prospect Theory]], heuristics-and-biases program, action effect.
- [[Amos Tversky]] — Prospect Theory, heuristics and biases, EBA, additive difference.
- Egon Brunswik — [[Lens Model]], representative design.
- Kenneth Hammond — lens model applied to judgment.
- Herbert Simon — satisficing, bounded rationality.
- Lola Lopes — SP/A model; skepticism about stable risk traits.
- Lee Roy Beach — [[Image Theory]].
- Gary Klein — [[Naturalistic Decision Making]] / RPD.
- Jennifer Lerner & Dacher Keltner — [[Appraisal-Tendency Framework]].
- Baruch Fischhoff — hindsight bias, constructed preferences, "consider-the-opposite" debiasing.

## Cross-References

- [[tversky-kahneman-1974-heuristics-biases]] — founding heuristics-and-biases paper; deep dive on representativeness, availability, anchoring.
- [[Heuristics and Biases Program]] — the paradigm whose decline the chapter documents.
- [[Daniel Kahneman]], [[Amos Tversky]] — entity pages.
- [[Replication Crisis]] — heuristics-and-biases waning prefigures replication concerns.
- [[Behaviour Change Determinants]] — Albarracín 2024 on the correlation–intervention gap parallels the chapter's caution that descriptive findings don't auto-license intervention.
- [[Correlation-Intervention Gap (Behaviour)]] — normative-vs-actual mirrors this chapter's central descriptive/prescriptive tension.
