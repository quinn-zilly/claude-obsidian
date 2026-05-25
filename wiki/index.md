---
type: meta
title: "Wiki Index"
updated: 2026-04-07
tags:
  - meta
  - index
status: evergreen
related:
  - "[[overview]]"
  - "[[log]]"
  - "[[hot]]"
  - "[[dashboard]]"
  - "[[Wiki Map]]"
  - "[[concepts/_index]]"
  - "[[entities/_index]]"
  - "[[sources/_index]]"
  - "[[LLM Wiki Pattern]]"
  - "[[Hot Cache]]"
  - "[[Compounding Knowledge]]"
  - "[[Andrej Karpathy]]"
---

# Wiki Index

Last updated: 2026-05-23 | Total pages: 222 | Sources ingested: 31

Navigation: [[overview]] | [[log]] | [[hot]] | [[dashboard]] | [[Wiki Map]] | [[getting-started]]

---

## Concepts

- [[LLM Wiki Pattern]] — the pattern for building persistent, compounding knowledge bases using LLMs (status: mature)
- [[Hot Cache]] — ~500-word session context file, updated after every ingest and session (status: mature)
- [[Compounding Knowledge]] — why wiki knowledge grows more valuable over time, unlike RAG (status: mature)
- [[cherry-picks]] — prioritized feature backlog from ecosystem research; 13 features to add to claude-obsidian (status: current)
- [[SVG Diagram Style Guide]] — canonical visual style for all diagrams: Space Grotesk, #0A0A0A dark theme, #E07850 accent, full design tokens (status: evergreen)
- [[Pro Hub Challenge]] — community challenge pattern for building claude-seo/claude-blog extensions; first challenge produced 6 submissions, 5 integrated in v1.9.0 (status: evergreen)
- [[Semantic Topic Clustering]] — SERP-based keyword grouping replacing paid tools; hub-spoke architecture with interactive visualization (status: evergreen)
- [[Search Experience Optimization]] — "read SERPs backwards" methodology for page-type mismatch detection and persona scoring (status: evergreen)
- [[SEO Drift Monitoring]] — "git for SEO" baseline/diff/track with 17 comparison rules and SQLite persistence (status: evergreen)
- [[DragonScale Memory]] — memory-layer spec inspired by the Heighway dragon curve; fold operator, deterministic page addresses, semantic tiling, boundary-first autoresearch (status: shipped v0.4, all four mechanisms opt-in)
- [[Persistent Wiki Artifact]]: durable Markdown page as the LLM's memory object, distinct from ephemeral chat turns (status: developing)
- [[Source-First Synthesis]]: provenance discipline; raw sources stay immutable while the wiki layer is synthesized and cited (status: developing)
- [[Query-Time Retrieval]]: wiki query path synthesizes with citations; complementary to Obsidian's in-vault search (status: developing)
- [[Knowledge Integration]] — organizational capability for combining distributed specialist knowledge; six-dimension framework (mature)
- [[Organizational Learning]] — change in organizational knowledge as a function of experience; four processes: search, creation, retention, transfer (mature)
- [[Knowledge Management]] — deliberate management of knowledge assets; process view; grounded in KBV (mature)
- [[Learning Curves]] — performance improves at decreasing rate with cumulative experience; knowledge depreciates (mature)
- [[Transactive Memory Systems]] — distributed group memory: who knows what and how to access it (developing)
- [[Knowledge Transfer]] — moving knowledge across people, units, organizations; barriers include causal ambiguity and tacitness (mature)
- [[Tacit vs Explicit Knowledge]] — central distinction shaping KM design, transfer strategy, and retention risk (mature)
- [[Knowledge-Based View of the Firm]] — firm exists to integrate specialist knowledge; knowledge is the primary source of sustainable competitive advantage (mature)
- [[Knowledge Retention]] — embedding knowledge in distributed repositories so it persists over time (developing)
- [[Knowledge-Based Theory of the Firm]] — Grant (1996); firm as knowledge integrator; four integration mechanisms; common knowledge (developing)
- [[Microfoundations]] — individual-level mechanisms underlying collective outcomes; additive vs. emergent aggregation (developing)
- [[Institutional Isomorphism]] — three mechanisms (coercive, mimetic, normative) by which organizations in a field converge structurally without efficiency gains (developing)
- [[Organizational Field]] — the totality of relevant actors constituting a recognized area of institutional life; unit of analysis for isomorphism theory (developing)
- [[Institutional Change Pathways]] — 2×2 typology: scope (transformational/developmental) × pace (revolutionary/evolutionary) yields Displacement, Alignment, Accommodation, Accretion (developing)
- [[Institutional Entrepreneurship]] — agentic turn in institutional theory; paradox of embedded agency; cultural vs. disruptive strategies; key blind spots (developing)
- [[Institutional Displacement]] — revolutionary + transformational: field-level overhaul via shocks or disruptive mobilization (developing)
- [[Institutional Alignment]] — evolutionary + developmental: gradual embedding of innovation without displacing existing arrangements (developing)
- [[Institutional Accommodation]] — revolutionary + developmental: disruptive forces dampened into incremental settlement (understudied) (developing)
- [[Institutional Accretion]] — evolutionary + transformational: micro-level improvisations accumulate to produce field-level transformation (least studied) (developing)
- [[Prediction vs Explanation (Psychology)]] — statistical and pragmatic tension between explanatory and predictive science; machine learning as solution; Yarkoni & Westfall 2017 (developing)
- [[Overfitting]] — model fitting sample-specific noise; training error ≠ test error; primary ML problem (developing)
- [[Training vs Test Error]] — fundamental gap between in-sample fit and out-of-sample prediction accuracy (developing)
- [[Bias-Variance Tradeoff]] — total prediction error = bias² + variance; unavoidable tradeoff; deliberate bias can reduce total error (developing)
- [[Procedural Overfitting]] — p-hacking reframed as human-analyst overfitting; constraining researcher df is regularization (developing)
- [[Cross-Validation]] — K-fold CV; estimates test error without new data; standard in ML, largely absent from psychology ca. 2017 (developing)
- [[Regularization]] — penalized regression (lasso, ridge); deliberate bias to reduce variance; shrinkage methods (developing)
- [[Replication Crisis]] — systematic failures of replication in psychology; root causes: publication bias, p-hacking, HARKing (mature)
- [[Open Science]] — transparency, open data, preregistration; reform movement for credible knowledge accumulation (mature)
- [[Preregistration]] — committing to research design before data collection; separates confirmatory from exploratory (mature)
- [[Conflict of Interest in Science]] — fundamental tension between personal incentive (publication) and institutional goal (accuracy); misalignment causes [[Motivated Reasoning]] and [[P-hacking]]; resolved via [[Open Workflow]], open data, incentive restructuring (developing)
- [[Motivated Reasoning]] — unconscious cognitive bias toward conclusions we're motivated to reach; ordinary human psychology that explains how [[Publication Bias]] becomes systematic despite ethical intent (developing)
- [[Open Workflow]] — transparency in research process (preregistration, analysis plans, workflow documentation); solves [[HARKing]], file-drawer effect, outcome switching; model: [[clinicaltrials.gov]] (developing)
- [[Paradigm-Driven Research]] — systematic variation of single established procedure rather than wholesale methodology reinvention; incorporates replication + extension; reduces waste, increases cumulation (developing)
- [[Registered Reports]] — in-principle journal acceptance before results known; eliminates publication bias (developing)
- [[Publication Bias]] — file drawer problem; positive results disproportionately published; inflates effect sizes (developing)
- [[P-hacking]] — analytic flexibility inflating false-positive rates; garden of forking paths (developing)
- [[HARKing]] — Hypothesizing After Results are Known; post-hoc hypotheses presented as a priori; three forms: classic, omission, pirating (mature)
- [[Analytic Reproducibility]] — reproducing published results from same data; second dimension of credibility framework (developing)
- [[Open Access]] — freely accessible scientific literature; gold vs green OA models; $900M savings argument; pillar of open science (developing)
- [[Scientific Communication Reform]] — unbundling registration, dissemination, peer review, and archiving; six reforms from Nosek & Bar-Anan (developing)
- [[Open Science Framework]] — osf.io; platform for preregistration, open data, and research collaboration (developing)
- [[metaBUS]] — 1M+ curated bivariate findings from applied psychology; rapid meta-analysis infrastructure (developing)
- [[DBpedia]] — structured knowledge from 111 Wikipedia editions; 400M+ facts; central LOD hub (developing)
- [[Linked Open Data]] — RDF/SPARQL-based best practices for publishing and connecting structured web data (developing)
- [[On-the-Job Development]] — OJD; 70% of leadership development; experiences over training; ten catalysts to hardwire into HR (developing)
- [[Behaviour Change Determinants]] — taxonomy of individual and social-structural determinants; correlational vs. intervention effect size hierarchy; Albarracín et al. 2024 (developing)
- [[Descriptive Norms]] — perceived frequency of a behaviour in a population; small intervention effect (OR≈2.20); role models most effective; Albarracín et al. 2024 (developing)
- [[Injunctive Norms]] — perceived approval of a behaviour by others; small intervention effect (d=0.34); distinct from descriptive norms (developing)
- [[Habits (Behaviour)]] — automated, repeated behaviours persisting without rewards; largest individual-level intervention target (medium, OR≈2.65); Albarracín et al. 2024 (developing)
- [[Behavioural Access Interventions]] — material/logistic resources enabling behaviour; largest overall intervention effect (large, OR≈4.89); Albarracín et al. 2024 (developing)
- [[Social Support (Behaviour)]] — informational/instrumental help for a specific behavioural goal; medium intervention effect (OR≈2.53); distinct from norms (developing)
- [[Reasoned Action Approach]] — Fishbein & Ajzen 2011; beliefs → attitudes → intentions → behaviour; injunctive norms; perceived behavioural control (developing)
- [[Information-Motivation-Behavioural Skills Model]] — Fisher & Fisher 1992/2006; IMB model; information + motivation + behavioural skills → behaviour; HIV prevention origins (developing)
- [[Correlation-Intervention Gap (Behaviour)]] — systematic pattern where correlational effect sizes overestimate intervention efficacy for every behavioural determinant; Albarracín et al. 2024 (developing)
- [[Judgment and Decision Making (Field)]] — JDM field overview; dual descriptive/normative theme; major research programs; Connolly et al. 2012 (developing)
- [[Lens Model]] — Brunswik/Hammond; cue combination model for judgment; representative design requirement (developing)
- [[Policy Capturing]] — regression model of individual judge; few cues, linear, low reliability; organizational applications (developing)
- [[Prospect Theory]] — Kahneman & Tversky 1979; reference-point value function; loss aversion; decision weight distortions; dominant descriptive model of risky choice (developing)
- [[Framing Effects]] — logically equivalent options described differently → different risk preferences; gain vs. loss framing; attribute framing (developing)
- [[Decision Justification Theory]] — Connolly & Zeelenberg 2002; two-component regret: outcome + process/self-blame; regret priming → better decisions (developing)
- [[Appraisal-Tendency Framework]] — Lerner & Keltner 2000/2001; distinct emotions (fear, anger, disgust) have distinct, predictable decision effects beyond simple valence (developing)
- [[Signal Detection Theory (Decision)]] — TSD; ROC curve; threshold-setting under uncertainty; base rate dependence; underused in organizational research (developing)
- [[Naturalistic Decision Making]] — NDM/RPD; expert decision = recognition-primed matching, not deliberation; Klein; Orasanu & Connolly (developing)
- [[Sunk Cost Effect]] — prior unrecoverable costs influence subsequent decisions; escalation of commitment; multiple competing explanations (developing)
- [[Dynamic Decision Making]] — repeated decisions on changing environment; feedback delays impede learning; systems dynamics oscillations (developing)
- [[Electronic Brainstorming]] — EBS; large EBS > nominal groups > F2F brainstorming; production blocking; anonymity effects; Connolly, Dennis, Valacich (developing)
- [[Pay-for-Performance]] — PFP; links pay to performance via two mechanisms: incentive effect and sorting effect; most-used compensation design in private sector (developing)
- [[Incentive Effect (Compensation)]] — how PFP changes current employee behavior through motivation; +0.54 SD in meta-analysis; but likely underestimates total impact (developing)
- [[Sorting Effect (Compensation)]] — how PFP changes workforce composition; high performers attracted/retained, low performers exit; Cadsby 2007: sorting = 74% of total PFP advantage (developing)
- [[PFP Intensity]] — magnitude of pay-performance gradient; annual merit = low intensity (3–4%); promotion channel = high intensity; higher intensity → more motivation AND more unintended consequences (developing)
- [[Equal Compensation Principle]] — Milgrom & Roberts 1992; incentivizing some tasks but not others distorts effort allocation toward incentivized metrics; multitasking problem (developing)
- [[Pay Dispersion]] — variation in pay within a group; horizontal vs. vertical; source matters: PFP-based = legitimate + positive effects; politically-based = illegitimate + negative effects (developing)
- [[Pay Transparency]] — four dimensions: pay outcomes, pay determination, discussion policies, communication modes; more transparency ≠ universally better; relative pay standing is key moderator (developing)
- [[Heuristics and Biases Program]] — Tversky & Kahneman research program; three heuristics (representativeness, availability, anchoring) produce systematic, predictable errors; biases persist in experts thinking intuitively (developing)
- [[Representativeness Heuristic]] — probability judged by resemblance to prototype; produces base rate neglect, insensitivity to sample size, illusion of validity, regression misconceptions (developing)
- [[Availability Heuristic]] — frequency/probability judged by ease of retrieval or mental construction; produces retrievability, search-set, imaginability biases, illusory correlation (developing)
- [[Anchoring and Adjustment]] — numerical estimates start from anchor, adjust insufficiently; produces overconfident distributions, conjunctive overestimation, disjunctive underestimation (developing)
- [[Base Rate Neglect]] — prior probabilities ignored when any individuating information is present, even worthless information; violates Bayes' rule (developing)
- [[Gambler's Fallacy]] — belief that random deviations will be corrected; follows from local representativeness expectation; "deviations are diluted, not corrected" (developing)
- [[Illusion of Validity]] — unwarranted confidence from good input-outcome match; persists despite knowledge of low validity; redundant inputs increase confidence, decrease accuracy (developing)
- [[Regression to the Mean]] — extreme observations regress toward mean on re-measurement; intuition fails because representativeness predicts outcome extremity should match input extremity (developing)
- [[Illusory Correlation]] — perceived co-occurrence based on associative strength rather than actual frequency; sustains unfounded clinical lore; resists contradictory evidence (developing)

### Entities (new)

- [[Tal Yarkoni]] — UT Austin; psychoinformatics, ML in psychology, Yarkoni & Westfall 2017
- [[Jacob Westfall]] — UT Austin; quantitative methods, statistical power, Yarkoni & Westfall 2017
- [[Evelyn Micelotta]] — UNM; institutional change, institutional logics
- [[Michael Lounsbury]] — U of Alberta; institutional logics perspective, cultural entrepreneurship
- [[Royston Greenwood]] — U of Alberta; professional firms, organizational archetypes, institutional complexity
- [[Leadership Map]] — four-dimension taxonomy: experiences, competencies, key relationships, learning agility; Yost & Plunkett (developing)
- [[Learning Agility]] — dispositional capacity to extract lessons from experience; determines OJD yield (developing)
- [[Developmental Experiences]] — curated work assignments that produce leadership growth; turnarounds, start-ups, cross-functional roles (developing)
- [[70-20-10 Rule]] — 70% OJD, 20% relationships, 10% training; heuristic from McCall et al. 1988 / Lombardo & Eichinger 1988 (developing)
- [[Personal Advisory Board]] — 5–7 person developmental network replacing single mentor; Higgins & Kram (developing)
- [[Transition Checklist]] — structured tool for role transitions; leverages high-openness-to-learning moments (developing)
- [[Complex Visibility]] — three-state model (hypervisibility, invisibility, managed visibility) mediating minority status → career success disparity; Beigi et al. 2025 (developing)
- [[Hypervisibility]] — excess scrutiny and tokenism imposed on minority employees; mistakes amplified, successes discounted (developing)
- [[Invisibility (Career)]] — contributions overlooked, voice suppressed, excluded from informal networks; co-exists with hypervisibility (developing)
- [[Managed Visibility]] — behavioral adaptation: code-switching, identity concealment, strategic self-presentation; cognitive tax on minority employees (developing)
- [[Outsider-Within Status]] — structural insider / experiential outsider; Collins (1986); minority employees in organizations (developing)
- [[Subjective Career Success]] — one's own evaluation of career outcomes; expanded dimensions for minority employees: authenticity, survival, collective good, adjustability (developing)
- [[Glass Cliff]] — minority appointment to precarious leadership roles in crisis; Ryan & Haslam 2005; savior effect (developing)
- [[Crowdsourcing Science]] — horizontal distribution of research ownership, expertise, resources; complement to standard model; Uhlmann et al. 2019 (developing)
- [[Publication Bottleneck]] — information-economic structural condition: too many researchers, too few slots; root cause of replication crisis per Giner-Sorolla 2012; Anna Karenina conjunction rules (developing)
- [[Aesthetic Standards in Science]] — three criteria (statistical perfection, narrative conformity, novelty) that distort science under bottleneck conditions; Giner-Sorolla 2012 (developing)
- [[Vertical Integration (Science)]] — standard small-team model; full pipeline within one lab; philosopher-scholar credit model (developing)
- [[Horizontal Distribution (Science)]] — crowdsourcing model; distributed components, pooled resources; complement to vertical integration (developing)
- [[Many Labs]] — multilab replication initiative; 36–125 labs; non-replicable effects fail consistently across populations (developing)
- [[Matthew Effect (Science)]] — cumulative advantage; early resource advantages compound; Merton 1968; motivation for crowdsourcing democratization (developing)
- [[Robustness (Science)]] — same data + different analysis; tests analytic fragility; multiverse/many-analysts; Silberzahn 2018 (developing)
- [[Replication as Theoretical Commitment]] — Nosek & Errington 2020; replication = claim that contextual differences are irrelevant; dissolves direct/conceptual distinction (developing)
- [[Questionable Research Practices]] — QRPs; p-hacking, HARKing, selective reporting; ordinary psychology under misaligned incentives; 7,887 surveyed (developing)
- [[Prediction Markets (Science)]] — r=0.52 with replication success; Anna Dreber; 72% accuracy; scalable pre-replication credibility screen (developing)
- [[TOP Guidelines]] — 10 transparency standards, 3 levels each; 83% of journals at level 0; COS/Nosek 2015 (developing)
- [[Psychological Science Accelerator]] — PSA; massively multisite collaborative network; Moshontz et al. 2018 (stub)
- [[Replication]] — attempt to repeat a study and obtain the same results; direct vs. conceptual; fundamental mechanism of scientific reliability (seed)
- [[File-Drawer Problem]] — systematic non-publication of null results; inflates effect sizes; addressed by preregistration and registered reports (seed)
- [[Open Data]] — making research datasets publicly available; cornerstone of analytic reproducibility; enabled by OSF and TOP Guidelines (seed)
- [[Social Cognitive Theory]] — Bandura; triadic reciprocal determinism; self-efficacy, modelling, outcome expectations; foundational to behaviour change (seed)
- [[Testing Effect]] — retrieval practice enhances long-term retention more than restudy; desirable difficulty; Roediger & Karpicke (seed)
- [[New Theory of Disuse]] — Bjork & Bjork 1992; storage vs. retrieval strength; theoretical backbone of desirable difficulties (seed)
- [[Judgment of Learning]] — metacognitive monitoring of learning; systematically miscalibrated under massed practice; tracks performance not storage strength (seed)
- [[Transfer of Training]] — degree to which trained skills transfer to job performance; near vs. far transfer; Baldwin & Ford 1988 (seed)
- [[Self-Directed Learning]] — learner-controlled pace, sequence, content; andragogy; key in workplace and digital learning contexts (seed)
- [[Synthetic Learning Environments]] — simulations and high-fidelity environments for training without real-world risk; fidelity paradox (seed)
- [[Spacing Effect]] — spaced practice produces better long-term retention than massed practice; desirable difficulty (seed)

---

## Entities

- [[Amos Tversky]] — Hebrew University / Stanford; co-founder of heuristics and biases program with Kahneman; 1937–1996 (developing)
- [[Daniel Kahneman]] — Hebrew University / Princeton; co-founder of heuristics and biases program; Nobel Prize in Economics 2002; *Thinking, Fast and Slow* (developing)
- [[Terry Connolly]] — U of Arizona; JDM researcher; regret/DJT, electronic brainstorming, naturalistic DM, information purchase (developing)
- [[Lisa Ordóñez]] — U of Arizona; JDM researcher; regret, equity, emotion in decisions, fear/anger reversal (developing)
- [[Andrej Karpathy]] — AI researcher, creator of the LLM Wiki pattern, former Tesla AI director (status: developing)
- [[Linda Argote]] — Carnegie Mellon; leading organizational learning researcher; learning curves, knowledge repositories (developing)
- [[Shaker Zahra]] — University of Minnesota; knowledge integration, dynamic capabilities, absorptive capacity (developing)
- [[Maryam Alavi]] — Emory University; knowledge management systems, IT and organizational knowledge (developing)
- [[Paul DiMaggio]] — Yale/Princeton/NYU sociologist; co-developer of institutional isomorphism theory and organizational field concept (developing)
- [[Walter Powell]] — Yale/Stanford sociologist; co-developer of institutional isomorphism; later work on network forms and biotech knowledge networks (developing)
- [[Ar9av-obsidian-wiki]] — multi-agent compatible LLM Wiki plugin; delta tracking manifest (status: current)
- [[Nexus-claudesidian-mcp]] — native Obsidian plugin + MCP bridge; workspace memory, task management (status: current)
- [[ballred-obsidian-claude-pkm]] — goal cascade PKM; auto-commit hooks, /adopt command (status: current)
- [[rvk7895-llm-knowledge-bases]] — 3-depth query system, Marp slides, parallel deep research (status: current)
- [[kepano-obsidian-skills]] — official skills from Obsidian creator; defuddle, obsidian-bases (status: current)
- [[Claudian-YishenTu]] — native Obsidian plugin embedding Claude Code; plan mode, @mention (status: current)
- [[Claude SEO]] — Tier 4 Claude Code skill for SEO analysis; 23 skills, 17 agents, 30 scripts at v1.9.0 (status: evergreen)
- [[Robert Grant]] — Georgetown University; knowledge-based theory of the firm; four integration mechanisms (developing)
- [[Jay Barney]] — University of Utah; resource-based view; microfoundations of capabilities (developing)
- [[Teppo Felin]] — University of Oxford; microfoundations, strategic management; Barney co-author (developing)
- [[Ella Miron-Spektor]] — Bar-Ilan University; organizational learning, creativity, teams (developing)
- [[Frank Bosco]] — Virginia Commonwealth University; metaBUS lead developer (developing)
- [[Brian Nosek]] — UVA / Center for Open Science; OSC 2015; preregistration revolution; Scientific Utopia series (developing)
- [[Yoav Bar-Anan]] — Ben-Gurion University; social psychologist; co-author Scientific Utopia I (developing)
- [[Etienne LeBel]] — Western University; credibility framework; curatescience.org (developing)
- [[Jens Lehmann]] — Leipzig/Bonn; DBpedia primary architect (developing)
- [[Christian Bizer]] — Mannheim; Linked Open Data pioneer; DBpedia co-developer (developing)
- [[Marcus Munafò]] — University of Bristol; manifesto for reproducible science (developing)
- [[John Ioannidis]] — Stanford / METRICS; "Why Most Published Research Findings Are False" (developing)
- [[Center for Open Science]] — non-profit; Charlottesville VA; OSF; open science reform movement (developing)
- [[Open Science Collaboration]] — collective author (270 members); OSC 2015 replication project (developing)
- [[Paul Yost]] — SPU I-O psychologist; OJD researcher; ten catalysts framework (developing)
- [[Mary Plunkett]] — Heineken International; Head of People & Org Development; Yost co-author (developing)
- [[Morgan McCall]] — USC; foundational OJD research; *Lessons of Experience* (developing)
- [[Mina Beigi]] — University of Southampton; career success and minority status; complex visibility framework (developing)
- [[Melika Shirmohammadi]] — University of Houston; career development, diversity; Beigi co-author (developing)
- [[Eric Uhlmann]] — INSEAD Singapore; crowdsourcing science; Silberzahn many-analysts project; Scientific Utopia III lead author (developing)
- [[Roger Giner-Sorolla]] — University of Kent; social psychologist; "Science or Art?" 2012; information-economic bottleneck account of replication crisis (developing)
- [[Norbert Kerr]] — Michigan State University; social psychologist; coined HARKing (1998); foundational to open science reform literature (stub)
- [[Simine Vazire]] — University of Melbourne; open science reform; "credibility revolution" framing; Nosek 2022 co-author (stub)
- [[Tom Hardwicke]] — University of Amsterdam; analytic reproducibility; open data policy audits; Nosek 2022 co-author (stub)
- [[Anna Dreber]] — Stockholm School of Economics; prediction markets for science; replication forecasting (developing)
- [[Dolores Albarracín]] — University of Pennsylvania; social psychologist; attitude change, persuasion, behaviour change interventions; HIV prevention meta-analysis (developing)
- [[Ingrid Smithey Fulmer]] — U of Illinois UIUC; compensation, pay transparency, Compensation Activation Theory; Fulmer et al. 2023 (developing)
- [[Barry Gerhart]] — UW-Madison; strategic compensation; incentive/sorting framework; Gerhart & Milkovich foundational work; Fulmer et al. 2023 (developing)
- [[JiHyun Kim]] — NUS Business School; PFP meta-analysis lead author (Kim et al. 2022); Fulmer et al. 2023 (developing)
- [[Robert A. Bjork]] — UCLA; New Theory of Disuse; desirable difficulties; testing effect and spacing effect research (seed)
- [[Kurt Kraiger]] — Colorado State; workplace instruction science; Kraiger & Ford 2021 (seed)
- [[J. Kevin Ford]] — Michigan State; transfer of training; Baldwin & Ford 1988 transfer model; Kraiger & Ford 2021 (seed)

---

## Sources

- [[connolly-2012-jdm|Connolly, Ordóñez & Barker (2012)]] — Handbook of Psychology Ch. 19 | JDM comprehensive survey | 2026-05-23
- [[claude-obsidian-ecosystem-research]] — 2026-04-08 | web research across 16+ repos | 8 wiki pages created
- [[zahra-2020-knowledge-integration|Zahra et al. (2020)]] — Academy of Management Annals | knowledge integration review | 2026-05-15
- [[argote-2021-organizational-learning|Argote et al. (2021)]] — Management Science | organizational learning processes review | 2026-05-15
- [[argote-2011-org-learning-experience|Argote & Miron-Spektor (2011)]] — Organization Science | experience-to-knowledge framework | 2026-05-15
- [[alavi-leidner-2001-knowledge-management|Alavi & Leidner (2001)]] — MIS Quarterly | KMS conceptual foundations | 2026-05-15
- [[grant-1996-knowledge-based-theory|Grant (1996)]] — SMJ | knowledge-based theory of the firm; four integration mechanisms | 2026-05-19
- [[barney-felin-2013-microfoundations|Barney & Felin (2013)]] — AMP | microfoundations; additive vs. emergent aggregation | 2026-05-19
- [[argote-miron-spektor-2011-org-learning-journal|Argote & Miron-Spektor (2011, journal)]] — Org Science | experience × context → knowledge (journal article version) | 2026-05-19
- [[bosco-2020-metabus|Bosco et al. (2020)]] — AMPPS | metaBUS; 1M+ curated findings; rapid meta-analysis | 2026-05-19
- [[nosek-2018-preregistration|Nosek et al. (2018)]] — PNAS | preregistration revolution; prediction vs. postdiction | 2026-05-19
- [[lebel-2018-credibility-framework|LeBel et al. (2018)]] — AMPPS | credibility framework; four dimensions; replication taxonomy | 2026-05-19
- [[lehmann-2015-dbpedia|Lehmann et al. (2015)]] — Semantic Web | DBpedia; 400M+ facts; LOD hub | 2026-05-19
- [[foster-deardorff-2017-osf|Foster & Deardorff (2017)]] — JMLA | OSF resource review; preregistration infrastructure | 2026-05-19
- [[open-science-collaboration-2015|Open Science Collaboration (2015)]] — Science | 100 replications; 36% success rate; replication crisis benchmark | 2026-05-19
- [[munafo-2017-manifesto|Munafò et al. (2017)]] — Nature Human Behaviour | manifesto for reproducible science; five reform categories | 2026-05-19
- [[nosek-bar-anan-2012-scientific-utopia-i|Nosek & Bar-Anan (2012)]] — Psychological Inquiry | Scientific Utopia I; six communication reforms; barriers are social not technical | 2026-05-20
- [[yost-plunkett-2010-ten-catalysts|Yost & Plunkett (2010)]] — Industrial and Organizational Psychology | ten catalysts to embed OJD in HR systems | 2026-05-21
- [[beigi-2025-career-success-minority|Beigi et al. (2025)]] — Journal of Management | career success and minority status; complex visibility; 337 articles; 4 minority groups | 2026-05-21
- [[uhlmann-2019-crowdsourcing-science|Uhlmann et al. (2019)]] — Perspectives on Psychological Science | Scientific Utopia III; crowdsourcing as complement to standard model; 2×2 typology; structural reforms | 2026-05-21
- [[giner-sorolla-2012-science-or-art|Giner-Sorolla (2012)]] — Perspectives on Psychological Science | publication bottleneck as root cause of replication crisis; three aesthetic criteria; information-economic account | 2026-05-21
- [[kerr-1998-harking|Kerr (1998)]] — Personality and Social Psychology Review | HARKing origin paper; three forms; cognitive/social mechanisms; proposed preregistration reforms | 2026-05-21
- [[nosek-2022-replicability-robustness-reproducibility|Nosek et al. (2022)]] — Annual Review of Psychology | 10-year review; three R's; 307 replications (64% success); Rogers diffusion model for culture change | 2026-05-22
- [[albarracin-2024-determinants-behaviour-change|Albarracín et al. (2024)]] — Nature Reviews Psychology | meta-review of behavioural determinants; access > social support > habits > … > knowledge; correlation-intervention gap | 2026-05-23
- [[fulmer-2023-compensation-performance|Fulmer et al. (2023)]] — Personnel Psychology | 30-year review of compensation→performance research; PFP incentive/sorting effects; pay transparency; pay dispersion; endogeneity | 2026-05-23

---

## Questions

- [[How does the LLM Wiki pattern work]] — how the pattern works and why it outperforms RAG at human scale (status: developing)

---

## Comparisons

- [[Wiki vs RAG]] — when to use a wiki knowledge base versus RAG; verdict: wiki wins at <1000 pages
- [[claude-obsidian-ecosystem]] — feature matrix of 16+ Claude+Obsidian projects; where claude-obsidian wins and gaps

---

## Decisions

- [[2026-04-14-community-cta-rollout]] - Skool community CTA footer added to 6 skill repos with per-tool frequency rules (status: active)
- [[2026-04-15-slides-and-release-session]] - Claude SEO v1.9.0 slides (15-slide HTML deck) + GitHub release v1.9.0 with PDF asset (status: complete)
- [[2026-04-15-release-report-session]] - Claude SEO v1.9.0 Release Report PDF: dark theme, 13 pages, WeasyPrint layout fixes, Challenge v2 added (status: complete)
- [[2026-04-14-claude-seo-v190-session]] - Claude SEO v1.9.0 Pro Hub Challenge integration: 5 submissions, 4 new skills, 4 review rounds, cybersecurity audit (status: complete)

---

## Folds

- [[fold-k3-from-2026-04-23-to-2026-04-24-n8]] — k=3, 8 entries, 2026-04-23 to 2026-04-24, DragonScale Phases 1–4 + v1.6.0 validation
- [[fold-k4-from-2026-04-08-to-2026-04-24-n16]] — k=4, 16 entries, 2026-04-08 to 2026-04-24, DragonScale Phases 0–4 + claude-obsidian v1.4–v1.6.0 + Claude SEO v1.9.0

---

## Domains

<!-- Add domain entries here after scaffold -->
