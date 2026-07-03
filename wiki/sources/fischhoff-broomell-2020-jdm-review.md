---
address: c-000233
type: source
title: "Judgment and Decision Making"
authors: ["Baruch Fischhoff", "Stephen B. Broomell"]
year: 2020
venue: "Annual Review of Psychology"
volume: 71
pages: "331–355"
doi: "10.1146/annurev-psych-010419-050747"
tags: [source, JDM, decision-making, judgment, behavioral-decision-research]
status: evergreen
created: 2026-05-26
updated: 2026-06-30
related: ["[[connolly-2012-jdm]]", "[[tversky-kahneman-1974-heuristics-biases]]"]
---

# Fischhoff & Broomell 2020 — Judgment and Decision Making

*Annual Review of Psychology* 71:331–355. A state-of-the-field review of behavioral decision research (a.k.a. decision science) by [[Baruch Fischhoff]] and [[Stephen Broomell]] (Carnegie Mellon). It is deliberately programmatic rather than encyclopedic: instead of cataloguing every result, it argues for *how the field works* — by analyzing tasks before describing behavior, then designing interventions — and uses each topic to illustrate that integrative strategy.

> [!abstract] One-line thesis
> Decision science = **analysis of tasks** (what a good decision objectively requires) + **description of behavior** (what people actually do) + **intervention** (how to close the gap). Each leg is weak without the other two: without task analysis you can't define "better"; without behavioral research you can't see what's failing; without intervention evidence the science stays abstract.

## Intellectual Roots

The field is framed as psychology's contribution to the post-von Neumann & Morgenstern (1944) rational-choice moment. Edwards (1954, 1961) set the founding commitment: study **the properties of tasks** — as posed by life or by researchers — *in tandem with* studying people's responses to them.

Early descriptive work used highly structured tasks where optimal behavior was definable, which exposed real regularities (people have little insight into their own processes; they over-extract information from some cues and under-extract from others) but also hit a wall, captured in Slovic & Lichtenstein's (1971) "terminal review" of two programs:

- **Regression modeling of repeated decisions** (e.g., rating grad-school applicants on fixed attributes) — predictive but couldn't discriminate among competing psychological accounts.
- **Stylized Bayesian urn tasks** (70% blue vs. 70% red balls) — clarified experimental design but were too unrealistic to engage natural cognition.

Recognizing these limits opened three richer-yet-still-task-grounded programs that organize modern JDM: judgment heuristics read against Bayesian norms ([[tversky-kahneman-1974-heuristics-biases|Tversky & Kahneman 1974]]); orderly-but-nonrational choice read against utility theory ([[Prospect Theory|Kahneman & Tversky 1979]]); and cognitive-capability modeling that accommodates properties of both people and tasks (Karelaia & Hogarth 2008).

## Core Elements of a Decision

The review's spine: every decision decomposes into three things, each with its own performance standard.

| Element | Question it answers | Performance standard(s) |
|---|---|---|
| **Judgment** | What outcomes will follow each option? | Accuracy **and** consistency |
| **Preference** | How much do those outcomes matter? | Consistency only (no accuracy criterion) |
| **Choice** | How are judgments + preferences combined? | Modeled, not normatively scored |

A key subtlety: accuracy and consistency are independent. You can hold accurate beliefs about one topic yet inconsistent beliefs across related ones, or be perfectly consistent while knowing almost nothing.

### Judgment — Accuracy

Studied four ways, each with a characteristic weakness:

1. **Knowledge / literacy tests.** Simplest approach (e.g., "True or false? The center of the Earth is very hot"), but item selection is rarely grounded in a task analysis of what people *need* to know. Even when scores predict behavior, they give little insight into how knowledge is acquired or used. The decision-science alternative starts from the facts a *specific* decision requires — sometimes summary estimates (treatment risks/benefits), sometimes **mental models** of how a process works (how HIV transmits, how a pandemic unfolds). Mental-model studies span HIV/AIDS, climate, contraceptives, energy, pandemics, radon (Bruine de Bruin & Bostrom 2013) and begin with open-ended interviews to capture intuitive formulations.
2. **Calibration.** Does confidence match accuracy? Perfect calibration = correct x% of the time when x% confident. Global and local confidence must be measured separately (people can think they got 6/10 right while their per-item probabilities imply more). A current focus is **incentivizing candor**: the US National Weather Service uses **scoring rules** (Murphy & Winkler 1974) to fight "umbrella bias" (overstating rain so no one gets caught out). But scoring rules are so abstract they need heavy feedback to master — practical only in multi-round settings like the [[Good Judgment Project]].
3. **Pooling (wisdom of crowds).** A crowd beats its best member when members' judgments correlate with the criterion but *not* with each other (Davis-Stober et al. 2014). Its weakness is **opacity**: accuracy arrives without an explanation, so recipients can't tell what evidence supports a prediction — a problem the review explicitly links to explaining black-box machine-learning predictions.

### Judgment — Consistency

The familiar standard is **Bayesian inference**, the norm behind the conjunction fallacy (Tversky & Kahneman 1983) and base-rate neglect ([[tversky-kahneman-1974-heuristics-biases|Tversky & Kahneman 1974]]). The review takes its critics seriously:

- The **subjective vs. frequentist** debate: Bayesians argue a subjective judgment is always needed to decide two events are "the same enough" to count as repeated, so there are no purely objective probabilities.
- The **completeness objection**: Bayes demands you allocate 100% of probability across a fixed hypothesis set. People often feel their hypotheses are incomplete and want to reserve probability for unimagined possibilities — motivating **Dempster–Shafer** inference, which scores the *conclusiveness* of evidence rather than its balance (Shafer & Tversky 1986).

> [!tip] Methodological shift to watch
> Three converging trends, all driven by the worry that *people construe tasks differently than researchers assume*: (1) **multiple tasks** to triangulate lay perspectives; (2) **open-ended tasks** letting people speak in their own terms; (3) replacing formal constructs with tractable approximations (e.g., "**known unknowns**," Walters et al. 2017, instead of second-order probabilities). Related finding: people say "**confidence**" for uncertainty about their *knowledge* and "**likelihood**" for uncertainty about the *world* (Ülkümen et al. 2016) — mirroring the Bayesian "assess vs. estimate" split.

### Preferences

No accuracy criterion — people may prefer whatever they want (shared with neoclassical economics). The only standard is **consistency with the utility axioms** (Edwards 1954): completeness, transitivity, willingness to trade off, and description-invariance.

Economists assume rationality and run **revealed-preference** inference (stable preferences, known perception, sometimes efficient markets). Psychologists are free to test the axioms, and violations drive theory:

- **Reference dependence** ([[Prospect Theory]]): preferences shift with how outcomes are framed, violating description-invariance.
- **Decoy / asymmetric-dominance effects**: adding an inferior third option flips the ranking of two others; strongest when prior preferences are weak and contextual cues are salient — conditions marketers actively manipulate (Huber et al. 2014).
- **Constructed preferences**: abstract axiom-based elicitations (standard gambles, willingness-to-pay for non-market goods) are so hard that studies routinely *discard* large fractions of responses — Edwards (1961) already lamented a study that "threw out 61 percent of subjects." Rather than a nuisance, these failures are evidence that people **infer** preferences for unfamiliar choices from context rather than retrieving stable ones (Lichtenstein & Slovic 2006). This has revived **process-tracing** (think-aloud, concurrent verbal protocols) over the emergent coding of [[Grounded Theory]].
- **Sacred / protected values**: refusals to trade off are *nonrational* (violate the trade-off axiom) yet legitimate and central to thoughtful decisions — studied with mixed methods, with applications to overcoming psychic numbing about genocide (Slovic & Slovic 2015) and discouraging violent extremism (Atran 2016).

### Choice

Birnbaum (2011)'s two complementary approaches: **experiments** (piecemeal — vary a few factors, hold the rest fixed) vs. **modeling** (statistically estimate the weight of each option-describing factor). Because recent reviews already covered experiments, Fischhoff & Broomell focus on modeling, using **Cumulative Prospect Theory (CPT)** as the worked example.

CPT bundles several principles into one model with a parameter each: **loss aversion**, **risk tolerance**, **probability weighting**, **choice stochasticity**. The catch is empirical:

- Parameter estimates are **highly variable** across studies (Davis-Stober et al. 2016; Regenwetter & Robinson 2017). A qualitative review tied loss-aversion magnitude to framing, stakes, and run length (Ert & Erev 2013); a meta-analysis found **weak overall evidence of loss aversion** — though possibly lost in methodological noise (Walasek et al. 2018).
- **Decision by Sampling (DbS)** (Stewart et al. 2006) recasts the parameters as products of sampling prior evaluations from memory, so task features (outcome/probability distributions, time to reflect) shape what gets sampled — meaning estimates aren't comparable across differently-presented choices.

> [!example] Description vs. experience gap
> **Description-based** choices (summary probabilities) yield standard CPT predictions; **experience-based** choices (learning from trials) lead people to *underweight* small probabilities — the opposite of CPT (Hertwig et al. 2004). The twist: Broomell & Bhatia (2014) used **information theory** to prove that the stimuli typically used to deliver "experience" *cannot in principle* identify CPT parameters — so they could never have revealed underweighting even if it occurred. This reframes an apparent behavioral contradiction as a measurement artifact, and has since guided better task designs (Glöckner et al. 2016) and re-analyses (Kellen et al. 2016).

## Sources of Heterogeneity

### Individual Differences

Early JDM found almost no stable individual differences — partly because varying tasks across studies (good for studying "people in general") is the opposite of the standardization individual-difference measures need; Huber (1983) recommended abandoning the search. The breakthrough was recognizing that **risk-taking is domain-specific**: someone who takes health risks needn't take financial ones, formalized in the **DOSPERT** scale (Weber et al. 2002). Related instruments: the Medical Maximizer–Minimizer Scale (Scherer et al. 2016) and Jackson et al.'s (2017) style+performance battery.

Fischhoff's own line developed **[[Decision-Making Competence]] (DMC)** — tasks drawn from the experimental literature, using both accuracy and consistency standards, designed to reduce shared-method variance. Embedded in the **CEDAR** longitudinal cohort (followed age 10→30):

- The Youth version (**Y-DMC**, age 18) correlated sensibly with real outcomes: *higher* with SES, social support, positive peers, intelligence; *lower* with antisocial disorder, delinquency, marijuana use, multiple sexual partners — patterns surviving semi-partial correlations that control for fixed and fluid intelligence (Parker & Fischhoff 2005).
- **A-DMC ↔ Y-DMC correlated 0.50** at age 30, evidence of stable individual differences (Parker et al. 2018).
- The single **strongest predictor** of both was **neighborhood disadvantage at age 10** — even controlling for IQ — consistent with Mullainathan & Shafir's (2013) scarcity argument that resource constraints pervasively degrade decision making.

### Life Span

Decision science here **collaborates with developmental psychology**, lending analytical methods while borrowing social/affective/physiological context. Two populations:

**Adolescents.** The folk "invulnerability bias" (Elkind 1967) often fails on analysis. In Goldberg et al. (2009), the best predictor of trying marijuana was *not* a sense of invulnerability but the **correct** belief that it might prove "so good they couldn't stop" — i.e., an **affective-forecasting** failure, not overconfidence. The paradoxical implied health message: emphasize how unimaginably good it can be. The review stresses the discipline of analyzing *how a fully informed teen would view the decision* before judging competence — citing Scalia's *Roper v. Simmons* dissent (where APA called teens competent in one case, incompetent in another; both can be true given different decisions). [[Fuzzy-Trace Theory]] (Reyna) supplies the intervention lever: extracting the **gist** ("even low risks add up to 100% if you keep doing it") improved a sexual-behavior program.

**Aging.** Where teen research asks how skills are *acquired*, aging research asks how they're *lost* (Levy et al. 2018) — teens "flailing in a supportive world," elders "struggling in a hostile one." A structural-equation study (Del Missier et al. 2015) found **age-related working-memory decline** the strongest predictor of performance decrements, net of sensory function, processing speed, and education.

> [!note] Guarded life-span conclusions
> By mid-teens (15–16) adolescents have adult-level (imperfect) *cognitive* decision skills, but less emotional/social control and more appetite for experimentation. With age, basic skills persist absent health impairment, but applying them to **complex or unfamiliar** decisions declines. A proposed future direction: compare the *decisions people face* across the lifespan, not just their *skills*.

## Applications

Two evaluation criteria run throughout: does an intervention produce **better choices**, or **better decision-making processes** (from which better choices should follow)?

**Improving individual decisions.** **Libertarian paternalism** (Thaler & Sunstein 2008) engineers choice architecture toward what a fully-informed rational agent would pick — but the review insists this is only legitimate after analyzing the *target individual's* decision (e.g., default organ donation only where survivors would accept it; stock-market defaults only where expected returns beat the psychological cost of downturns). Since per-person analysis rarely scales, medical decision research targets the **modal patient** with sensitivity analyses across patient distributions, plus tools like NIH's **PROMIS** validated self-report scales. The process-improvement alternative — **warning people about biases** — has limited value (Milkman et al. 2009): people lack the cognitive structures to act on warnings, slip into intuitive mode, or think themselves immune. What *does* work is the classic learning recipe: **prompt, unambiguous feedback; proper incentives; instruction in unintuitive processes** (the conditions under which weather forecasters and auditors become well-calibrated).

> [!example] Good Judgment Project (IARPA)
> Thousands of forecasters, hundreds of geopolitical questions, scoring-rule feedback that separated **knowledge / resolution / calibration**. Built on Lichtenstein & Fischhoff (1980), where concentrated feedback (200 judgments/round) improved calibration *beyond* the training tasks. Findings: (a) a brief intense dose of training + scoring-rule feedback produced **sustained** gains; (b) remote interaction helped somewhat; (c) **superforecasters** emerged as a stable individual difference; (d) self-selected stayers were already better-calibrated than typical lab samples. Directly relevant to expert elicitation in policy ([[Signal Detection Theory (Decision)|see below]]).

> [!example] Night Shift (ED transfer decisions)
> ~60% of severely injured patients at local EDs aren't transferred to trauma centers in time (archetype: an elder who fell, no obvious injury, possible intracranial bleed; the local ED orders a CAT scan that confirms too late). In **[[Signal Detection Theory (Decision)|SDT]]** terms (Lynn & Barrett 2014), some physicians have **good discrimination but poor decision rules**, others the reverse (Mohan et al. 2012). Two **serious games** — differing in learning theory (narrative engagement vs. analogical reasoning) — made atypical-severe cases feel more *representative* of the underlying pathology and supplied missing feedback. Both beat equal doses of standard ACS training on a third simulation, **sustained at 6 months**. A cautionary contrast: anti-phishing training proved impossible to evaluate externally because malware vulnerability depended on the user's computer/browser/ISP, not vigilance (Canfield et al. 2017).

**Cost–Risk–Benefit analysis.** Triggered by mandates (US Executive Order 12291: cost-benefit for federal policies over $100M). Decision science plays three roles: improving expert judgments, translating behavior into analytic terms, and communicating between organizations and stakeholders.

- *Judgment in analysis* — every analysis carries **expert judgments** (the inputs) and **value judgments** (the terms). Expert **elicitation** ranges from the GJP's many-forecaster discrete-event method to day-long structured interviews probing internal consistency (Morgan 2017). Whether experts behave "like everyone else once they run out of evidence" is flagged as open.
- *Value judgments* — defining "risk" is inherently value-laden (mortality vs. morbidity; fatalities vs. life-years-lost; statistical vs. identifiable lives). **Psychometric risk perception** (Slovic) identifies **dread** and **uncertainty** as the dominant public concern dimensions; often dismissed as irrational, they can be legitimate policy inputs (dread has real psychological/physiological consequences; lay uncertainty may flag problems analysts miss).
- *Human behavior in analysis* — **SDT** packages behavior into analysis-friendly quantities (false-negative rates) that vary across people and respond to interventions. Applications span triage transfer, phishing susceptibility (Canfield & Fischhoff 2018, motivated by the Podesta/DNC spear-phishing hack), and undergraduate men's perception of women's sexual intent (Farris et al. 2008).

**Communication** (two-way, internal and external):

- *Intelligence analysis* — from Kent's (1964) classic essay on the ambiguity of verbal quantifiers ("likely"), through Heuer (1999), to a National Research Council (2011) consensus report backing IARPA's behavioral initiative; the US Navy now has a chief decision scientist.
- *Drug regulation* — the FDA (2018) **restructured drug/biologics evaluation around a decision-science benefit-risk framework** (separating scientific from value judgments, encouraging uncertainty expression, accommodating diverse evidence) — though regulatory inertia stalled the decision-science "drug facts box."
- *Climate change* — behavioral/decision scientists engaged since the late Carter administration but had little communication role until the late George W. Bush era, "when the limits to letting the science speak for itself became painfully evident."

## Conclusion — The Field's Productive Tension

Two bridging activities (Baddeley 1979) drive progress: **applied basic psychology** (testing theories in real settings) and **basic applied psychology** (domesticating real-world phenomena for the lab). The distinctive move — **analyze tasks before describing behavior or designing interventions** — pays off in common terms across diverse tasks, clear performance standards, and a shared language with other analytic fields. The review is candid about three limits of that strategy:

1. **Analytically sound but cognitively intractable tasks** (unfamiliar-health-state standard gambles) — productive only if researchers stay alert to the possibility.
2. **Over-emphasizing anomalies**, breeding a "**bias meme**" where people are seen as the sum of their failings and their competence is obscured.
3. **Excluding analysis-averse researchers** — countered by accessible conceptual (not technical) introductions to SDT, Bayesian inference, etc.

> [!key-insight] Why this review matters in the vault
> It is the cleanest articulation of the **task-analysis → description → intervention** loop, and it deliberately *re-frames* several famous behavioral findings (loss aversion, description–experience gap, teen invulnerability) as artifacts of weak task analysis or measurement — a corrective lens to apply when reading the heuristics-and-biases canon.

## Key Concepts

| Concept | Definition |
|---|---|
| Task analysis | Formal characterization of what a decision objectively requires, done *before* studying behavior |
| Calibration | Match between confidence and accuracy; global ≠ local |
| Scoring rule | Procedure incentivizing truthful probability reports (fights umbrella bias / hedging) |
| Constructed preference | Preference inferred at decision time from context, not retrieved from stable storage |
| Sacred / protected value | Value held immune to trade-offs — nonrational yet legitimate |
| CPT | Cumulative Prospect Theory — parameters for loss aversion, risk tolerance, probability weighting, stochasticity |
| Decision by Sampling | Recasts CPT parameters as memory-sampling of prior comparisons |
| DMC | Decision-Making Competence — measurable, stable individual difference |
| Superforecaster | Stably superior calibration identified in the Good Judgment Project |
| Dread / uncertainty | Dominant psychometric dimensions of public risk perception |
| Applied basic vs. basic applied psychology | Theory-in-the-world vs. world-in-the-lab (Baddeley 1979) |

## Key Figures

- [[Baruch Fischhoff]] — Carnegie Mellon (Engineering & Public Policy; Politics & Strategy); lead author; founder-era figure in risk analysis
- [[Stephen Broomell]] — Carnegie Mellon (Social & Decision Sciences); co-author; information-theoretic critique of CPT estimation

## Links In

- [[Judgment and Decision Making (Field)]] — this review updates/supplements the field overview
- [[Prospect Theory]] — CPT coverage and the loss-aversion critique
- [[Signal Detection Theory (Decision)]] — Night Shift, phishing, sexual-intent applications
- [[Good Judgment Project]] — extended case study
- [[Calibration (Judgment)]] — accuracy framework
- [[Constructed Preference]] — preference section
- [[Loss Aversion]] — CPT critique
- [[Decision-Making Competence]] — individual-differences section
- [[Fuzzy-Trace Theory]] — life-span section
- [[Libertarian Paternalism]] — applications section

## Connections to Vault

- [[connolly-2012-jdm]] — earlier JDM handbook chapter; this Annual Review is the more recent, more programmatic complement
- [[tversky-kahneman-1974-heuristics-biases]] — foundational program this review contextualizes *and* critiques (recasting several biases as task-analysis failures)
- [[Prospect Theory]] — the dominant choice model reviewed and challenged here
- [[Representativeness Heuristic]], [[Availability Heuristic]] — consistency-standard backdrop for the judgment section; representativeness is the lever in the Night Shift games
- [[Heuristics and Biases Program]] — placed in historical context; the "bias meme" critique is aimed partly at its reception
