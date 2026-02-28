---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-28T00:43:40Z"
last_modified: "Fri, 27 Feb 2026 22:56:57 GMT"
source_url: "https://claude.com/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude"
title: "Using the ClinicalTrials.gov Connector in Claude | Claude"
---
- [](https://www.anthropic.com/claude/opus)
    Opus
  - [](https://www.anthropic.com/claude/sonnet)
    Sonnet
  - [](https://www.anthropic.com/claude/haiku)
    Haiku

- Platform

  - [](/platform/api)
    Overview
  - [](https://docs.claude.com/)
    Developer docs
  - [](http://claude.com/pricing#api)
    Pricing

  - [](https://platform.claude.com/)
    Console login

- Solutions

  Use cases

  - [](/solutions/agents)
    AI agents
  - [](/solutions/claude-code-security)
    Claude Code Security
  - [](/solutions/coding)
    Coding

  Industries

  - [](/solutions/customer-support)
    Customer support
  - [](/solutions/education)
    Education
  - [](/solutions/financial-services)
    Financial services
  - [](/solutions/government)
    Government
  - [](/solutions/healthcare)
    Healthcare
  - [](/solutions/life-sciences)
    Life sciences
  - [](/solutions/nonprofits)
    Nonprofits

- Pricing

  - [](/pricing)
    Overview
  - [](/pricing#api)
    API

  Pricing

  - [](/pricing/max)
    Max plan
  - [](/pricing/team)
    Team plan
  - [](/pricing/enterprise)
    Enterprise plan

- Resources

  Insights

  - [](/blog)
    Blog
  - [](/customers)
    Customer stories
  - [](https://www.anthropic.com/events)
    Events
  - [](https://www.anthropic.com/news)
    Anthropic news

  Learn

  - [](https://www.anthropic.com/learn)
    Anthropic Academy
  - [](/resources/courses)
    Courses
  - [](/resources/tutorials)
    Tutorials
  - [](/resources/use-cases)
    Use cases

  Tools

  - [](/connectors)
    Connectors
  - [](/plugins)
    Plugins

- [](https://claude.ai/login)
  Login

&nbsp;

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

[](#)

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

- Meet Claude

  Products

  - [](/product/overview)
    Claude
  - [](/product/claude-code)
    Claude Code
  - [](/product/cowork)
    Cowork

  Features

  - [](/chrome)
    Claude in Chrome
  - [](/claude-in-slack)
    Claude in Slack
  - [](/claude-in-excel)
    Claude in Excel
  - [](/claude-in-powerpoint)
    Claude in PowerPoint
  - [](/skills)
    Skills

  Models

  - [](https://www.anthropic.com/claude/opus)
    Opus
  - [](https://www.anthropic.com/claude/sonnet)
    Sonnet
  - [](https://www.anthropic.com/claude/haiku)
    Haiku

- Platform

  - [](/platform/api)
    Overview
  - [](https://docs.claude.com/)
    Developer docs
  - [](http://claude.com/pricing#api)
    Pricing

  - [](https://platform.claude.com/)
    Console login

- Solutions

  Use cases

  - [](/solutions/agents)
    AI agents
  - [](/solutions/claude-code-security)
    Claude Code Security
  - [](/solutions/coding)
    Coding

  Industries

  - [](/solutions/customer-support)
    Customer support
  - [](/solutions/education)
    Education
  - [](/solutions/financial-services)
    Financial services
  - [](/solutions/government)
    Government
  - [](/solutions/healthcare)
    Healthcare
  - [](/solutions/life-sciences)
    Life sciences
  - [](/solutions/nonprofits)
    Nonprofits

- Pricing

  - [](/pricing)
    Overview
  - [](/pricing#api)
    API

  Pricing

  - [](/pricing/max)
    Max plan
  - [](/pricing/team)
    Team plan
  - [](/pricing/enterprise)
    Enterprise plan

- Resources

  Insights

  - [](/blog)
    Blog
  - [](/customers)
    Customer stories
  - [](https://www.anthropic.com/events)
    Events
  - [](https://www.anthropic.com/news)
    Anthropic news

  Learn

  - [](https://www.anthropic.com/learn)
    Anthropic Academy
  - [](/resources/courses)
    Courses
  - [](/resources/tutorials)
    Tutorials
  - [](/resources/use-cases)
    Use cases

  Tools

  - [](/connectors)
    Connectors
  - [](/plugins)
    Plugins

- [](https://claude.ai/login)
  Login

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

- 

  Contact sales

  [Contact sales](/contact-sales)
  Contact sales

- 

  Try Claude

  [Try Claude](https://claude.ai/)
  Try Claude

1.  Tutorials

    [](/resources/tutorials)
    Tutorials

    /

2.  
    Using the ClinicalTrials.gov Connector in Claude

Explore here

- [](#)

  Ask questions about this page
- [](#)

  Copy as markdown

# Using the ClinicalTrials.gov Connector in Claude

- 

  Category

  Life Sciences

- 

  Product

- 

  Reading time

  Watch time

  5

  min

  min

- 

  Share

  [Copy link](#)
  https://claude.com/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude

The ClinicalTrials.gov connector gives Claude access to the NIH/NLM registry of 500,000+ clinical studies to search trials, analyze endpoints, and support research operations. This article explains how to set up and use the ClinicalTrials.gov integration with Claude to power clinical, regulatory, and patient-supporting workflows.

The ClinicalTrials.gov integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

‍

## **What this integration provides**

The ClinicalTrials.gov connector gives Claude access to ClinicalTrials.gov API v2, the world's largest clinical trial registry managed by the National Library of Medicine (NLM) at the National Institutes of Health (NIH). With more than 1,200 studies, the database has grown to over 500,000 registered trials across 221 countries and territories, representing the most comprehensive source of clinical research information worldwide. 

This connector provides six primary tool calls that access different dimensions of clinical trial data.

- **search_trials** is the primary discovery tool, enabling users to find trials by condition (e.g., "diabetes", "lung cancer"), intervention (drug/treatment names), location (city, state, country), sponsor, recruitment status (RECRUITING, COMPLETED, etc.), and development phase (PHASE1-PHASE4), with support for Boolean operators and medical synonym expansion.
- **get_trial_details** retrieves comprehensive protocol information for specific trials using their NCT identifier, returning full eligibility criteria (inclusion/exclusion), detailed study design and methodology, primary and secondary endpoints with measurement timeframes, all study locations with contact information, sponsor details, enrollment targets, and links to published results.
- **search_by_sponsor** enables pharmaceutical pipeline analysis by finding all trials funded by specific companies or institutions (e.g., "Pfizer", "NIH", "Mayo Clinic"), supporting competitive intelligence and drug development tracking with filtering by condition and phase.
- **search_investigators** identifies principal investigators and research sites conducting trials in specific therapeutic areas, returning investigator names, roles, institutional affiliations, facility locations, and associated trial information for site selection and investigator verification.
- **analyze_endpoints** systematically compares outcome measures across trials, operating in two modes: single-trial analysis (returns all endpoints for one NCT ID) or aggregate analysis (identifies common endpoint patterns across multiple trials in a therapeutic area), essential for protocol design benchmarking and understanding standard measures in a disease area.
- **search_by_eligibility** enables clinical research coordinators to screen for trials matching specific demographic and clinical criteria (age, sex) with support for eligibility keyword searches in inclusion/exclusion criteria text  (e.g., "BRCA mutation", "HbA1c \> 8%", "ECOG 0-1").

On the provider side, the connector queries ClinicalTrials.gov's RESTful API v2, which accesses a PostgreSQL database updated daily with trial registration data submitted by study sponsors. All interventional trials of FDA-regulated products must be registered before enrollment begins (per FDAAA 801), and results must be submitted within one year of study completion. The database includes structured data fields for conditions (using MeSH terminology), interventions, locations, eligibility criteria, outcome measures, and study design parameters.

‍

## **Who should use the ClinicalTrials.gov integration**

- **Clinical Research Coordinators & Study Recruiters:** Screen institutional patient populations for trial eligibility using demographic and clinical criteria, identify nearby recruiting studies for referral programs, verify detailed trial requirements and visit schedules, and coordinate with study sponsors to accelerate enrollment.
- **Pharmaceutical & Biotech Companies:** Conduct competitive intelligence on competitor pipelines, analyze clinical development strategies across therapeutic areas, identify partnership opportunities with active research sites, and benchmark study designs and endpoints against industry standards.
- **Principal Investigators & Site Coordinators:** Identify collaborating investigators at other institutions, understand which sites are most active in specific disease areas, verify investigator qualifications and track record, and discover trials for potential site participation.
- **Protocol Writers & Clinical Operations Teams:** Benchmark endpoint selection by analyzing outcome measures used in similar trials, design eligibility criteria based on prior study standards, identify common recruitment challenges in a therapeutic area, and estimate feasible enrollment timelines.
- **Regulatory Affairs Professionals:** Track clinical development programs for regulatory submissions, verify trial registration compliance for FDA-regulated products, analyze phase progression rates and development timelines, and identify precedent trials for regulatory strategy.
- **Clinical Trial Recruiters & Research Navigators:** Screen institutional patient populations for trial eligibility, identify appropriate trials for referral programs, coordinate with study sponsors for patient enrollment, and maintain databases of active trials at their healthcare system.
- **Medical Affairs & Health Economists:** Analyze trial completion rates and time-to-results, identify gaps in clinical evidence for specific indications, track real-world evidence studies and post-marketing trials, and support payer value dossiers with clinical trial data.

‍

## **Setting up the ClinicalTrials.gov integration**

**For Organization Owners (Team and Enterprise)**

1.  Navigate to Admin settings \> Connectors
2.  Click "Browse connectors"
3.  Click “**ClinicalTrials.gov**”
4.  Click “Add to your team”

‍

**For Individual Claude Users**

1.  Navigate to Settings \> Connectors
2.  Find “**ClinicalTrials.gov**”
3.  Click “Connect”

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

‍

**For Claude Code Users**

1.  Command: /plugin marketplace add anthropics/life-sciences
2.  Command: /plugin install clinical-trials@life-sciences
3.  Restart Claude Code
4.  Verify that the server is connected with /mcp

‍

Technical details of the ClinicalTrials.gov integration can be found in the [ClinicalTrials.gov MCP Server Documentation](http://clinicaltrials.gov).

‍

## **Example use cases**

**Clinical Trial Recruitment & Eligibility Screening**

- Scenario: Research coordinators and recruitment professionals identifying eligible trial candidates from their institutional patient populations
- Sample Prompts:\
  - *"Find recruiting Phase 3 diabetes trials with HbA1c eligibility criteria between 7-10% for our Boston research site"*
  - *"What breast cancer trials are accepting BRCA-positive candidates at academic medical centers in California?"*
  - *"Search for Alzheimer's trials with MMSE score requirements that match our memory clinic population"*
  - *"Identify pediatric leukemia trials recruiting at major children's hospitals for our referral network"*

‍

**Competitive Intelligence & Pipeline Analysis**

- Scenario: Analyzing pharmaceutical company development programs and therapeutic landscapes
- Sample Prompts:\
  - *"What Phase 3 oncology trials is Pfizer currently running? Show their cancer pipeline"*
  - *"Find all GLP-1 agonist trials for obesity. Who are the main sponsors and what endpoints are they measuring?"*
  - *"Show me Moderna's active clinical trials and their development phases"*
  - *"What companies are developing drugs for Parkinson's disease? Analyze their trial endpoints"*

‍

**Systematic Protocol Design & Endpoint Benchmarking**

- Scenario: Designing new trial protocols based on industry standards and precedent studies
- Sample Prompts:\
  - *"What are the most common primary endpoints used in Phase 3 diabetes trials?"*
  - *"Analyze endpoints for completed heart failure trials - what timeframes do they use?"*
  - *"Find principal investigators at academic medical centers conducting immunotherapy trials"*
  - *"What eligibility criteria do Phase 2 NASH trials typically use? Show me HbA1c cutoffs"*

Learn more at How to use the Clinical Trial Protocol skill with Claude

## Related tutorials

[How to use the Scientific Problem Selection Skill with Claude](/resources/tutorials/how-to-use-the-scientific-problem-selection-skill-with-claude)

How to use the Scientific Problem Selection Skill with Claude

How to use the Scientific Problem Selection Skill with Claude

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-scientific-problem-selection-skill-with-claude)

Tutorial

[How to use the scVI-Tools bioinformatics skill bundle with Claude](/resources/tutorials/how-to-use-the-scvi-tools-bioinformatics-skill-bundle-with-claude)

How to use the scVI-Tools bioinformatics skill bundle with Claude

How to use the scVI-Tools bioinformatics skill bundle with Claude

Tutorial

[Tutorial](/resources/tutorials/how-to-use-the-scvi-tools-bioinformatics-skill-bundle-with-claude)

Tutorial

[ Using the ToolUniverse Extension in Claude](/resources/tutorials/using-the-tooluniverse-extension-in-claude)

Using the ToolUniverse Extension in Claude

Using the ToolUniverse Extension in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-tooluniverse-extension-in-claude)

Tutorial

[Using the bioRxiv and medRxiv Connector in Claude](/resources/tutorials/using-the-biorxiv-and-medrxiv-connector-in-claude)

Using the bioRxiv and medRxiv Connector in Claude

Using the bioRxiv and medRxiv Connector in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-biorxiv-and-medrxiv-connector-in-claude)

Tutorial

[Homepage](https://claude.com)

Homepage

[Next](#)

Next

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

  [](#)

  Hi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Improve my writing style

  [](#)

  Hi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Brainstorm creative ideas

  [](#)

  Hi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Learn

- Explain a complex topic simply

  [](#)

  Hi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Help me make sense of these ideas

  [](#)

  Hi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Prepare for an exam or interview

  [](#)

  Hi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Code

- Explain a programming concept

  [](#)

  Hi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Look over my code and give me tips

  [](#)

  Hi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Vibe code with me

  [](#)

  Hi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

More

- Write case studies

  [](#)

  This is another test

- Write grant proposals

  [](#)

  Hi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can - an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Write video scripts

  [](#)

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

- Cowork

  [Cowork](/product/cowork)
  Cowork

- Max plan

  [Max plan](/pricing/max)
  Max plan

- Team plan

  [Team plan](/pricing/team)
  Team plan

- Enterprise plan

  [Enterprise plan](/pricing/enterprise)
  Enterprise plan

- Download app

  [Download app](/download)
  Download app

- Pricing

  [Pricing](/pricing)
  Pricing

- Log in

  [Log in](https://claude.ai/login)
  Log in

Features

- Claude in Chrome

  [Claude in Chrome](/chrome)
  Claude in Chrome

- Claude in Slack

  [Claude in Slack](/claude-in-slack)
  Claude in Slack

- Claude in Excel

  [Claude in Excel](/claude-in-excel)
  Claude in Excel

- Claude in PowerPoint

  [Claude in PowerPoint](/claude-in-powerpoint)
  Claude in PowerPoint

- Skills

  [Skills](/skills)
  Skills

Models

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

- Claude Code Security

  [Claude Code Security](/solutions/claude-code-security)
  Claude Code Security

- Code modernization

  [Code modernization](/solutions/code-modernization)
  Code modernization

- Coding

  [Coding](/solutions/coding)
  Coding

- Customer support

  [Customer support](/solutions/customer-support)
  Customer support

- Education

  [Education](/solutions/education)
  Education

- Financial services

  [Financial services](/solutions/financial-services)
  Financial services

- Government

  [Government](/solutions/government)
  Government

- Healthcare

  [Healthcare](/solutions/healthcare)
  Healthcare

- Life sciences

  [Life sciences](/solutions/life-sciences)
  Life sciences

- Nonprofits

  [Nonprofits](/solutions/nonprofits)
  Nonprofits

Claude Developer Platform

- Overview

  [Overview](/platform/api)
  Overview

- Developer docs

  [Developer docs](https://docs.claude.com/)
  Developer docs

- Pricing

  [Pricing](https://claude.com/pricing#api)
  Pricing

- Amazon Bedrock

  [Amazon Bedrock](/partners/amazon-bedrock)
  Amazon Bedrock

- Google Cloud’s Vertex AI

  [Google Cloud’s Vertex AI](/partners/google-cloud-vertex-ai)
  Google Cloud’s Vertex AI

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

- Courses

  [Courses](https://www.anthropic.com/learn)
  Courses

- Connectors

  [Connectors](/connectors)
  Connectors

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

- Startups program

  [Startups program](/programs/startups)
  Startups program

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

- Economic Futures

  [Economic Futures](https://www.anthropic.com/economic-futures)
  Economic Futures

- Research

  [Research](https://www.anthropic.com/research)
  Research

- News

  [News](https://www.anthropic.com/news)
  News

- Responsible Scaling Policy

  [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
  Responsible Scaling Policy

- Security and compliance

  [Security and compliance](https://trust.anthropic.com/)
  Security and compliance

- Transparency

  [Transparency](https://anthropic.com/transparency)
  Transparency

Help and security

- Availability

  [Availability](https://www.anthropic.com/supported-countries)
  Availability

- Status

  [Status](https://status.anthropic.com/)
  Status

- Support center

  [Support center](https://support.claude.com/en/)
  Support center

Terms and policies

Privacy choices

### Cookie settings

We use cookies to deliver and improve our services, analyze site usage, and if you agree, to customize or personalize your experience and market our services to you. You can read our Cookie Policy [here](https://www.anthropic.com/legal/cookies).

Customize cookie settings

Reject all cookies

Accept all cookies

###### Necessary

Enables security and basic functionality.

Required

###### Analytics

Enables tracking of site performance.

Off

###### Marketing

Enables ads personalization and tracking.

Off

Save preferences

Privacy policy

[Privacy policy](https://www.anthropic.com/legal/privacy)

Privacy policy

Responsible disclosure policy

[Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)

Responsible disclosure policy

Terms of service: Commercial

[Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)

Terms of service: Commercial

Terms of service: Consumer

[Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)

Terms of service: Consumer

Usage policy

[Usage policy](https://www.anthropic.com/legal/aup)

Usage policy

[x.com](https://x.com/claudeai)

x.com

[LinkedIn](https://www.linkedin.com/showcase/claude/)

LinkedIn

[YouTube](https://www.youtube.com/@anthropic-ai)

YouTube

[Instagram](https://www.instagram.com/claudeai)

Instagram

English (US)

[English (US)](/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude)

[日本語 (Japan)](/ja-jp/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude)

[Deutsch (Germany)](/de-de/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude)

[Français (France)](/fr-fr/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude)

[한국어 (South Korea)](/ko-kr/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude)
