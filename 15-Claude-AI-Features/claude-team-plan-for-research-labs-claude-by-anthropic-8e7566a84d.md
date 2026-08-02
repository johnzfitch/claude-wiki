---
title: "Claude Team plan for research labs | Claude by Anthropic"
source_url: "https://www.claude.com/programs/claude-team-plan-for-research-labs"
category: "15-Claude-AI-Features"
fetched_at: "2026-08-02T05:43:55Z"
tags: ["search"]
---

# Claude Team plan for research labs

A thinking partner for academic and nonprofit labs to advance scientific discovery and innovation.

Get started

[Get started](#pricing)

Get started

## Made for scientific research

### A collaborator for your whole lab

Claude writes code, reads the literature, and reasons through experiments alongside your team.

### Grounded in science and research

Claude pulls directly from PubMed, Benchling, and other connectors, so answers are grounded in verifiable references.

### Verifiable with citations

Claude cites its sources, shows its work, and flags uncertainty. Your research data stays yours.

### One plan for your organization

Replace scattered individual subscriptions with a single Team plan. Everyone in your lab gets the same access at an affordable rate to support academic and nonprofit labs.

Video

[Play video](#)

Play video

Jonah Cool and Eric Kauderer-Abrams share their vision for making Claude the go-to AI research assistant for scientists.


## How labs use Claude

Research code

Data analysis

Literature synthesis

Numerical experiments

Active

Prompt

\> use the scRNA-qc skill to perform QC and filtering on the raw_feature_matrix from my experiment

- Now let me run the QC analysis on the raw feature matrix:
- Bash(python3 scripts/qc_analysis.pypbmc_test_data/raw_feature_bc_matrix.h5)  
  ↳===========================================================  
  Single-Cell RNA-seq Quality Control AnalysisFollowing scVerse Best Practices  
  … +60 lines (ctrl+o to expand)


- Excellent! The QC analysis completed successfully. Let me update the visualizations:
- Read(qc_metrics_before_filtering.png)↳ Read image (732.3KB)
- Read(qc_filtering_thresholds.png)↳ Read image (210KB)
- Read(qc_metrics_after_filtering.png)↳ Read image (1.1MB)
- Perfect! I've successfully completed the QC analysis on your raw feature matrix using the scRNA-qc skill. Here's a summary of the results:QC Analysis SummaryDataset: 2,700 cells × 32,738 genes (raw)Quality Metrics Detected:
  - 13 mitochondrial genes
  - 106 ribosomal genes
  - 13 hemoglobin genes

  MAD-Based Filtering Thresholds:
  - Total counts: 709 - 6,812
  - Genes detected: 367 - 1,821
  - Mitochondrial %: MAD threshold 3.65%, Hard threshold 8.0%

  Filtering Results:
  - 266 cells removed as outliers (9.9%)
  - 2,434 cells retained (90.1%)
  - Gene filtering reduced from 32,738 to 9,487 genes (29.0%)

  Key Observations from Visualizations:
  1.  Before Filtering: The data shows typical scRNA-seq quality with most cells having 1,000-2,000 counts and detecting 500-1,000 genes. Mitochondrial content is generally low (\<5%), which is excellent.
  2.  Thresholds: The MAD-based thresholds are permissive (5 MADs for counts/genes, 3 MADs for MT%), following scverse best practices to avoid over-filtering.
  3.  After Filtering: The filtered dataset shows cleaner distributions with tighter clustering, lower mitochondrial content (mostly \<3%), and good cell-gene correlation.

  Output Files Created:
  - raw_feature_bc_matrix_filtered.h5ad - Clean filtered dataset ready for downstream analysis
  - raw_feature_bc_matrix_with_qc.h5ad - Original data with QC annotations
  - QC visualization PNGs (before/thresholds/after)

  The data quality looks excellent! You can now proceed with downstream analysis like normalization, dimensionality reduction, and clustering using the filtered dataset.

### Turn ideas into working code

Claude Code writes, debugs, and runs scripts for analysis from your terminal. Build pipelines, prototype methods, and QC data without waiting on the person who knows the repository.

Prompt

Look in this folder and pull together the results CSV and sample metadata. Run treatment vs. control comparisons on every measured endpoint, flag anything significant after multiple-comparison correction, and generate a figure I can drop straight into my slides.

Working folder

~/Data/cytokine_study/

# Treatment vs. control: cytokine panel

Welch's t-test · Benjamini–Hochberg FDR · n = 12 per group

4 of 6 Significant

**Figure 1.** Mean ± SEM serum concentration (pg/mL) at 72h post-dose. Treatment significantly reduced IL-6, TNF-α, CXCL10, and CCL2 after FDR correction.

\* q \< 0.05  ·  \*\* q \< 0.01  ·  \*\*\* q \< 0.001

### From dataset to figure, on your desktop

Hand Claude Cowork a dataset and a question. Fit models, run stats, generate publication-ready figures locally, with your own files and environment.

Read guide

[Read guide](https://claude.com/resources/use-cases/genomic-data-analysis)

Read guide

Prompt

I'm preparing a review on CAR-T cell exhaustion mechanisms. Search PubMed for recent papers on transcriptional regulators of T cell exhaustion in solid tumors. Summarize which transcription factors are consistently implicated, where the field disagrees on their roles, and create a figure I can use in my review draft.

Transcriptional regulators of T cell exhaustion

Reported role across 47 papers on solid tumors, 2021–2025 · 6 representative studies shown

 
Chen  
2024

Scott  
2023

Beltra  
2023

Giles  
2022

Zebley  
2024

Wang  
2025

TOX

drives

drives

drives

drives

drives

drives

TCF1

restrains

restrains

restrains

restrains

context

restrains

NR4A

drives

drives

context

drives

—

drives

BATF

drives

restrains

drives

context

restrains

context

IRF4

drives

context

drives

restrains

drives

context

BLIMP-1

drives

drives

—

context

drives

restrains

T-bet

restrains

restrains

context

restrains

—

restrains

Drives exhaustion

Restrains exhaustion

Context-dependent

Not assessed

Source: PubMed

### Survey an entire field in an afternoon

Pull from PubMed and bioRxiv, find contradictions across papers, and surface testable hypotheses with real citations you can check.

Read guide

[Read guide](https://claude.com/resources/tutorials/using-the-pubmed-connector-in-claude)

Read guide

Prompt

Benchmark our MC integrator on the 24-dim Genz test function. Sweep sample sizes 10² to 10⁷, 200 replicates each for 95% CIs, compare against the analytical value (μ = 1.5). Publication-ready convergence figure with a summary strip — final estimate, relative error, wall time.

Attachments

mc_integrator

14.2 KB

PY

genz_testfunctions

3.8 MB

NPZ

# Monte Carlo convergence: high-dimensional integrand

Sample mean Î vs. sample size N across 200 independent replicates · d = 24

Final estimate 1.4994± 0.0021

Relative error 0.04%

Samples 10⁷

Replicates 200

Wall time 12.7s

Sample mean Î

95% CI (200 replicates)

Theoretical mean

**Figure 3.** Monte Carlo estimator Î of a 24-dimensional integrand plotted against sample size N, with 95% confidence bands from 200 independent replicates. The estimator converges to the theoretical mean (μ = 1.5000) within 0.04% relative error at N = 10⁷.

### Test hypotheses computationally

Run large-scale numerical experiments, compare results against theoretical predictions, and generate publication-ready figures in a fraction of the time.

## Claude connects to your tools

Work across your literature databases, lab platforms, and productivity tools in one place.

Explore connectors

[Explore connectors](/connectors)

Explore connectors

## Why scientists choose Claude

"After collaborating with Claude Code for the past 3 months, turning one idea after another into research projects, I am totally hooked. I cannot imagine research anymore without it! Claude's coding and reasoning capabilities are out of this world, and it's dramatically expanded my conception of what's possible."

David Shih, Professor of Physics, Rutgers University

“Claude has helped our lab identify promising research directions to hone in on by enabling rapid preliminary analysis and statistical power prediction for complex, highly specialized experimental designs.”

Silvia Domke, Assistant Professor, University of Zurich

“\[Claude\] was extraordinarily useful for my research -- both a larger, purely empirical project with a complicated codebase, and some more basic research projects and idea seeds where I needed to prototype something quickly. It definitely changed the game for me, and I re-subscribed!"

Hannah Lawrence, Computer Science Ph.D. student, Massachusetts Institute of Technology

“We have taken data harmonization projects and standards development efforts that would have taken a decade to complete and realized them in months. Claude has fundamentally changed how we interact with domain experts and the content we can deliver, such as for rare disease diagnostics and drug repurposing.”

Melissa Haendel, Director of Precision Health & Translational Informatics at University of North Carolina at Chapel Hill

"Over the last six months, Claude has become a crucial collaborator for our lab, from designing computer processors, to programming languages, to operating systems. As a team of computer systems builders, we can engage in high-risk, engineering-heavy prototyping which would be difficult to justify in the past."

Jonathan Balkind, Assistant Professor of Computer Science, University of California, Santa Barbara

“I use Opus as an intellectual partner to find holes in my ideas before I commit resources to experiments. At the bench, I generate protocols and troubleshoot logistics in real time. With Claude Code, I automate data transformations and build analysis pipelines. As an MD-PhD student juggling course work, lab experiments, analysis, collaborations and scientific writing, having a tool this versatile has been transformative.”

Maia Madison, MD PhD Student, University of California, San Francisco

"Claude has changed the way that I do science, from the way that I explore the literature and brainstorm for a new hypothesis, to our ability to analyze large-scale datasets and integrate diverse information sources at a scale that would be difficult to achieve otherwise. It has accelerated my work, but has also allowed me to generate testable and verifiable ideas and to think about the science in fundamentally new ways. Claude passes the scientific “deletion test” - it has become an essential tool for our work.”

Iain Cheeseman, Herman and Margaret Sokol Professor of Biology; Core Member, Whitehead Institute; Associate Department Head

"I’ve been able to take advantage of Claude’s broad knowledge to connect a research problem in theoretical particle physics to techniques developed for industrial systems engineering and number theory. Claude Code has allowed me to identify and integrate well developed libraries into our niche problem setting and explore bespoke solutions that leverage advanced reasoning capabilities. It has dramatically changed the pace and ambition of this research project."

Kyle Cranmer, Professor and Director of the Data Science Institute, University of Wisconsin, Madison

"'I figured out how to do \[insert X\] with Claude' has become a frequent refrain in discussions with my team. Claude is enabling my academic research group to acquire new skills and accomplish analysis tasks far more quickly."

Abby Buchwalter, Assistant Professor, University of California, San Francisco

[Prev](#)

Prev

0/5


## Get Claude for your lab

Principal investigators from labs with fewer than 75 people can get started by verifying their lab status. For larger labs, reach out to our sales team.

### Standard

\$15 /user

Per month

Verify your lab

[Verify your lab](https://claude.ai/labs-verification/attestation)

Verify your lab

- Access to Claude Code & Cowork
- Life sciences connectors and skills
- Shared projects and file creation
- Access to Research
- Central billing and administration
- Single sign-on (SSO)
- Minimum 2 seats

### Premium

\$75 /user

Per month

Verify your lab

[Verify your lab](https://claude.ai/labs-verification/attestation)

Verify your lab

Everything in Standard, plus:

- 5x more usage\*
- Higher limits for long-running analyses

\*Extra [usage limits](https://support.anthropic.com/en/articles/9797557-usage-limit-best-practices) apply. Prices shown don’t include applicable tax.

Price and plans are subject to change at Anthropic’s discretion.

## More resources

[Getting started with Claude for life sciences](https://claude.com/resources/tutorials/getting-started-with-claude-for-life-sciences)

Getting started with Claude for life sciences

Getting started with Claude for life sciences

Tutorial

[Tutorial](https://claude.com/resources/tutorials/getting-started-with-claude-for-life-sciences)

Tutorial

[Advancing Claude in Life Sciences](https://www.anthropic.com/news/healthcare-life-sciences)

Advancing Claude in Life Sciences

Advancing Claude in Life Sciences

Blog

[Blog](https://www.anthropic.com/news/healthcare-life-sciences)

Blog

[Explore the full range of Claude’s capabilities for scientific research](https://claude.com/solutions/life-sciences)

Explore the full range of Claude’s capabilities for scientific research

Explore the full range of Claude’s capabilities for scientific research

Learn

[Learn](https://claude.com/solutions/life-sciences)

Learn

[Learn about the AI for Science program by Anthropic](https://www.anthropic.com/news/ai-for-science-program)

Learn about the AI for Science program by Anthropic

Learn about the AI for Science program by Anthropic

Learn

[Learn](https://www.anthropic.com/news/ai-for-science-program)

Learn

## FAQ

### Who is eligible for the grant-funded research discount?

The discounted Claude Team plan for research labs plan is available to active scientific labs at academic institutions and nonprofit research organizations. Specifically, biomedical and basic science labs are being prioritized in addition to the hard sciences including chemistry, math, computer science, and physics. Eligibility is verified through the lab’s principal investigator.

If you are a for-profit company, contract research organization, or industry R&D team, please see [our Team and Enterprise plans](https://claude.com/pricing#team-&-enterprise).

### What’s included in this discounted Claude Team plan?

The Claude Team plan for research labs includes everything in Claude Team: shared projects, Claude Code, Cowork, file creation, built-in connectors to research databases, single sign-on, and central billing and administration with a minimum purchase of 2 seats.

### If I don’t qualify, which plan is right for me?

If you're at a for-profit organization or don't meet the eligibility criteria, Claude Team and Claude Enterprise offer the same capabilities at standard pricing. Visit [claude.com/pricing](https://claude.com/pricing#team-&-enterprise) to compare plans, or contact our sales team for help choosing the right fit.

### What resources are available to help me get started?

We have [tutorials](https://claude.com/resources/tutorials-category/life-sciences) covering common research use cases, including a walkthrough of sample agent skills and MCP connectors. You can also explore life sciences guides and documentation at [claude.com/lifesciences](http://claude.com/lifesciences), and connect research tools like PubMed, Benchling, and 10X Genomics through built-in connectors.

### Does Claude train on my data?

No. Claude does not train on your conversations, uploaded files, or research data. Your unpublished findings, grant drafts, and proprietary datasets stay private. Admins can configure data retention policies for their team.

[Prev](#)

Prev


[Homepage](https://claude.com)

Homepage


Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

Write

[Button Text](#)

Button Text

Learn

[Button Text](#)

Button Text

Code

[Button Text](#)

Button Text

Write

- Help me develop a unique voice for an audience


  Hi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Improve my writing style


  Hi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Brainstorm creative ideas


  Hi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Learn

- Explain a complex topic simply


  Hi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Help me make sense of these ideas


  Hi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Prepare for an exam or interview


  Hi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Code

- Explain a programming concept


  Hi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Look over my code and give me tips


  Hi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Vibe code with me


  Hi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

More

- Write case studies


  This is another test

- Write grant proposals


  Hi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.  
    
  Please execute the task as soon as you can - an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Write video scripts


  this is a test

[Anthropic](https://www.anthropic.com/)

Anthropic

© \[year\] Anthropic PBC

Products

- Claude

  [Claude](/product/overview)
  Claude

- Claude Code

  [Claude Code](/product/claude-code)
  Claude Code

- Claude Code for Enterprise

  [Claude Code for Enterprise](/product/claude-code/enterprise)
  Claude Code for Enterprise

- Claude Cowork

  [Claude Cowork](/product/cowork)
  Claude Cowork

- @Claude

  [@Claude](/product/tag)
  @Claude

- Claude Design

  [Claude Design](/product/design)
  Claude Design

- Claude Science

  [Claude Science](/product/claude-science)
  Claude Science

- Claude Security

  [Claude Security](/product/claude-security)
  Claude Security

- Download app

  [Download app](/download)
  Download app

- Pricing

  [Pricing](/pricing)
  Pricing

- Log in

  [Log in](https://claude.ai/login)

Features

- Claude for Chrome

  [Claude for Chrome](/claude-for-chrome)
  Claude for Chrome

- Claude for Microsoft 365

  [Claude for Microsoft 365](/claude-for-microsoft-365)
  Claude for Microsoft 365

- Skills

  [Skills](/skills)
  Skills

Models

- Mythos

  [Mythos](https://www.anthropic.com/claude/mythos)
  Mythos

- Fable

  [Fable](https://www.anthropic.com/claude/fable)
  Fable

- Opus

  [Opus](https://www.anthropic.com/claude/opus)
  Opus

- Sonnet

  [Sonnet](https://www.anthropic.com/claude/sonnet)
  Sonnet

- Haiku

  [Haiku](https://www.anthropic.com/claude/haiku)
  Haiku

Solutions

- AI agents

  [AI agents](/solutions/agents)
  AI agents

- Code modernization

  [Code modernization](/solutions/code-modernization)
  Code modernization

- Coding

  [Coding](/solutions/coding)
  Coding

- Customer support

  [Customer support](/solutions/customer-support)
  Customer support

- Cybersecurity

  [Cybersecurity](/solutions/cybersecurity)
  Cybersecurity

- Enterprise

  [Enterprise](/solutions/enterprise)
  Enterprise

- Financial services

  [Financial services](/solutions/financial-services)
  Financial services

- Government

  [Government](/solutions/government)
  Government

- Healthcare

  [Healthcare](/solutions/healthcare)
  Healthcare

- Higher education

  [Higher education](/solutions/education)
  Higher education

- K-12 teachers

  [K-12 teachers](/solutions/teachers)
  K-12 teachers

- Legal

  [Legal](/solutions/legal)
  Legal

- Life sciences

  [Life sciences](/solutions/life-sciences)
  Life sciences

- Nonprofits

  [Nonprofits](/solutions/nonprofits)
  Nonprofits

- Small business

  [Small business](/solutions/small-business)
  Small business

Claude Platform

- Overview

  [Overview](/platform/api)
  Overview

- Developer docs

  [Developer docs](https://platform.claude.com/docs)
  Developer docs

- Pricing

  [Pricing](https://claude.com/pricing#api)
  Pricing

- Ecosystem

  [Ecosystem](/ecosystem)
  Ecosystem

- Marketplace

  [Marketplace](/platform/marketplace)
  Marketplace

- Claude on AWS

  [Claude on AWS](/partners/claude-on-aws)
  Claude on AWS

- Google Cloud

  [Google Cloud](/partners/google-cloud)
  Google Cloud

- Microsoft Foundry

  [Microsoft Foundry](/partners/microsoft-foundry)
  Microsoft Foundry

- Regional compliance

  [Regional compliance](/regional-compliance)
  Regional compliance

- Console login

  [Console login](https://platform.claude.com/)
  Console login

Resources

- Blog

  [Blog](/blog)
  Blog

- Claude partner network

  [Claude partner network](/partners)
  Claude partner network

- Community

  [Community](/community)
  Community

- Connectors

  [Connectors](/connectors)
  Connectors

- Courses

  [Courses](https://www.anthropic.com/learn)
  Courses

- Customer stories

  [Customer stories](/customers)
  Customer stories

- Engineering at Anthropic

  [Engineering at Anthropic](https://www.anthropic.com/engineering)
  Engineering at Anthropic

- Events

  [Events](https://www.anthropic.com/events)
  Events

- Plugins

  [Plugins](/plugins)
  Plugins

- Powered by Claude

  [Powered by Claude](/partners/powered-by-claude)
  Powered by Claude

- Service partners

  [Service partners](/partners/services)
  Service partners

- Tutorials

  [Tutorials](/resources/tutorials)
  Tutorials

- Use cases

  [Use cases](/resources/use-cases)
  Use cases

Company

- Anthropic

  [Anthropic](https://www.anthropic.com/)
  Anthropic

- Careers

  [Careers](https://www.anthropic.com/careers)
  Careers

- Policy

  [Policy](https://www.anthropic.com/policy)
  Policy

- Economic Futures

  [Economic Futures](https://www.anthropic.com/economic-futures)
  Economic Futures

- Research

  [Research](https://www.anthropic.com/research)
  Research

- News

  [News](https://www.anthropic.com/news)
  News

- Policy on the AI Exponential
