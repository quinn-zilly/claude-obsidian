---
type: paper
address: c-000490
title: KM Research Paper
tags:
  - knowledge-management
  - open-science
status: developing
updated: 2026-06-03
created: 2026-06-03
---
# Questions

- What is the ideal system for creating, sharing, and organizing knowledge in academia? 
	- What do we know from KM?
	- What is specific to academic research?
	- What is the goal of KM in academia?
- How is academia handling KM now?
	- What are the factors that contribute to this system?
	- What are the incentives, structures, and cultures that maintain the system?
- What is the difference between the ideal and reality?
	- What is going well?
	- What can continue to be built upon?
	- How can academia improve?
- What changes need to be made?
	- What are the most critical changes?
	- What are the next small wins?

# Outline

## Intro
- The primary objective of science as a discipline is to accumulate knowledge about the nature of the observable universe [[nosek-2012-scientific-utopia-ii]]. 
- Under the post-positivist paradigm of Western science, knowledge is accumulated via the objective falsification of hypotheses to reach the closest reasonable approximation of verifiable truth [[Ponterotto-2005-Qualitative-Research-Paradigms]].
- The mission of science is best served by researchers who are motivated to search for truth about nature, and disseminate their findings openly and accurately. However, individual researchers are best served by what will allow them to succeed professionally. That is, scientists must do what gets their work published in prestigious journals. The problem is that under the current incentive structure, the goals of truth and accuracy are not aligned with the goal of publishability. Historically, journals almost exclusively publish positive findings of novel results, so studies with null or replicated findings go unpublished [[nosek-2012-scientific-utopia-ii]]. 
- Despite the best intentions of all involved, one cannot hope for researchers to prioritize accuracy when they are being rewarded for publishability. People tend to behave in the ways in which they are incentivized to behave, and it is folly to expect otherwise [[kerr-1995-folly-rewarding-A]].
- Open science has become more prevalent thanks to a number of tools and communities like OSF. 
- Preliminary evidence suggests the registered reports can improve the quality of research rigor. Soderberg et al. (2018) had 353 researchers peer review and compare a published RR paper and a comparison paper from a non-RR publication. They found significant improvements in perceived methodological and analytical rigor without significant differences in novelty or creativity.
- There is a long way to go
	- Hardwick et al. (2022) examined a random sample of psychology studies from 2014-2017. They found that, although 65% of the articles were publicly available, provided access to research materials (14%), study protocols (0%), data (2%), or analysis scripts (> 1%). Furthermore, only 3% of the studies had preregistered their hypotheses.

## Problems

### Scientific Communication is Inefficient
Five inefficiencies of scientific communication [[nosek-bar-anan-2012-scientific-utopia-i]]
1. **No communication** — file-drawer problem; negative/null results unpublished
2. **Slow communication** — avg 677 days from submission to print (Nosek's own 62 manuscripts)
3. **Incomplete communication** — page limits force omission of methods detail, data, materials
4. **Inaccurate communication** — publication bias; HARKing; errors undetectable in final product
5. **Unmodifiable communication** — corrections difficult; errors persist; post-publication updating rare

### Publishability Incentivized Over Accuracy and Replication
Misaligned incentives, "Openness is not needed because we are untrustworthy; it is needed because we are human." [[nosek-2012-scientific-utopia-ii]]
- Scientists need to get published in prestigious journals to get jobs
- Top journals prioritize positive and novel results over accuracy and transparency of methods.
- Motivated reasoning justifies questionable practices in the service of personal motives.
- This creates questionable practices, which increases the proportion of false results

- The OSC conducted direct replications of 100 experimental and correlational studies published in three 2008 issues of major psychology journals. Of those 100 replication attempts, only 36 produced statistically significant results in the same direction and replication effects were half the magnitude of originals [[open-science-collaboration-2015]]

- Publication bottleneck (too many studies, too few publication outlets) forces researchers to master the *art* of producing perfect-looking results. Articles cannot pass through by showing theoretical meaning and methodological rigor alone; their results must _appear_ to support the hypothesis perfectly. This favors aesthetic criteria over scientific ones [[giner-sorolla-2012-science-or-art]].
	- Statistical perfection (p<.05)
	- Harking
	- Novelty

### Questionable Research Practices
Questionable practices:
1. Running many low-powered studies instead of high-powered ones
2. Selective dismissal of "failed" pilot studies while uncritically accepting successful ones
3. Selective reporting of positive vs. negative results
4. Stopping data collection once significance is achieved
5. Including multiple variables and reporting only those that "worked" ([[P-hacking]])
6. Maintaining flexibility in analysis, exclusion criteria, and data transformations
7. Reporting discoveries as if confirmatory (HARKing)
8. Avoiding direct replication

## Solutions

### Improving Communication Efficiency

### Restructuring Incentives

**Journals Focused on Soundness, Not Importance**
- PLoS ONE model: peer review evaluates research soundness, not perceived importance
- Since 2006: 13,798 articles (2011), 70% acceptance rate, 2011 impact factor 4.41 (top 25%)
- Shows importance is not predictive of citation impact
### Crowdsourcing Science

### Open Science 2.0

Four ingredients of an ideal ecosystem-wide implementation:

1. **A modular and dynamic research record** — share components (hypotheses, protocols, data, code, manuscripts, reviews) when each is ready, not at the end. Linked via persistent identifiers, with version control and forking. A "record of versions" rather than a static "version of record." GitHub/open-source is the working model; protocols.io, Figshare, Dryad, Octopus, ResearchEquals are partial instances.
2. **Standardization and interoperability** — agreed data structures, vocabularies, metadata so humans *and machines* can integrate datasets. GenBank/UniProt/AlphaFold show the payoff. Custom spreadsheets are the anti-pattern.
3. **Ongoing quality control** — distributed and partly automated, throughout the cycle (like manufacturing QC), not just at the end. AI could flag missing info, retracted references, bad RRIDs, protocol inconsistencies.
4. **Reorganization of scientific labor** — task specialization across larger teams (Data Manager, Systematic Reviewer, Statistician), rewarded as such. Distributed collaborations like [[Big Team Science\|Psychological Science Accelerator]] and ManyBabies as models.


## Institutional Change
- Given the clear benefits of proposed changes, one might wonder why academia uses the inefficient system of publishing.
- At one time, publishers served an important function. They took on the costs and work associated with reviewing, printing, and disseminating academic research. At the same time, publication in top academic journals became the standard for assessing the legitimacy of organizations and researchers.
- Although the internet removed the need for publishers to disseminate academic research, the standard for assessing the importance and validity of that research was already deeply embedded in the field.
- Institutional theory suggests that organizational structure is shaped by the institutional environment, such that formal organizations increase their legitimacy by incorporating the prevailing institutional norms defined by rationalized concepts of organizational work.
- Organizations must ceremonially conform to these norms to be seen as legitimate and survive, even when they often conflict with the technical criteria of efficiency.
- Over time, institutional norms can become so deeply embedded in organizational culture that they are taken for granted as external facts.
- Prestige is the primary currency being traded in academic research.
- Because publishing is the primary method of gaining and maintaining prestige, it creates normative pressure to conform to standards of publishability, which outweighs any competitive pressures to improve accuracy [[dimaggio-powell-1983-institutional-isomorphism]].
- Forces individual researchers to conform to institutionally embedded publishing standards

# Sources

[[nosek-bar-anan-2012-scientific-utopia-i]]

[[nosek-2012-scientific-utopia-ii]]

[[dimaggio-powell-1983-institutional-isomorphism]]

[[uhlmann-2019-crowdsourcing-science]]

[[open-science-collaboration-2015]]

[[munafo-2017-manifesto]]

[[thibault-2023-open-science-2-0]]

[[lebel-2018-credibility-framework]]

[[giner-sorolla-2012-science-or-art]]

[[alavi-leidner-2001-knowledge-management]]

[[leidner-kayworth-2006-culture-is-review]]

[[micelotta-2017-pathways-institutional-change]]

[[basson-et-al-2022-oa-dimensions-wos]]

[[Ponterotto-2005-Qualitative-Research-Paradigms]]


