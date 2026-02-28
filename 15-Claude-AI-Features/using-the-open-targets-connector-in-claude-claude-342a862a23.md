---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-28T00:43:42Z"
last_modified: "Fri, 27 Feb 2026 22:56:52 GMT"
source_url: "https://claude.com/resources/tutorials/using-the-open-targets-connector-in-claude"
title: "Using the Open Targets Connector in Claude | Claude"
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
    Using the Open Targets Connector in Claude

Explore here

- [](#)

  Ask questions about this page
- [](#)

  Copy as markdown

# Using the Open Targets Connector in Claude

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
  https://claude.com/resources/tutorials/using-the-open-targets-connector-in-claude

This connector provides access to the Open Targets Platform for identifying and prioritizing therapeutic drug targets based on disease associations. This article explains how to set up and use the Open Targets integration with Claude to more quickly explore supporting data and prioritize drug targets and assess disease associations.

The Open Targets integration relies upon Claude's ability to [use remote connectors](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory).

‍

## **What this integration provides**

The Open Targets connector provides a purpose-built interface and instruction to access and interpret the data and analyses within the [Open Targets Platform](http://platform.opentargets.org). 

The Open Targets Platform is a comprehensive tool that supports systematic identification and prioritization of potential therapeutic drug targets, integrating publicly available datasets to build and score target-disease associations. It also integrates relevant annotation information about targets, diseases/phenotypes, drugs, variants, GWAS and molecular QTL studies, and credible sets as well as their most relevant relationships.

This tool makes the Open Targets Platform GraphQL API accessible as read-only, and includes all sources listed in the [Open Targets Platform documentation](http://platform-docs.opentargets.org).

‍

## **Who should use the Open Targets integration**

- **Target Discovery Scientists:** Identifying novel therapeutic targets
- **Research Directors/Team or Project Leads/Portfolio Managers:** Strategic decision-making and portfolio management
- **Academic researchers at all levels:** contrasting their data against existing data, e.g. viewing associations evidence and prioritization analyses for a list of targets they have generated
- **Bioinformaticians/Data Engineers/Machine Learning Engineers/R&D IT teams:** Integrating Open Targets data with proprietary datasets, building internal data platforms and solutions, training models on biological data

‍

## **Who can access the Open Targets integration**

The Open Targets Platform data available through the connector is available for academic and commercial use. Open Targets Platform is marked with CC0 1.0; this dedicates the data to the public domain, allowing downstream users to consume the data without restriction. For more information, refer to the [Open Targets Platform licensing documentation.](https://platform-docs.opentargets.org/licence)

The connector code itself is licensed with Apache 2.0.

More details on accessing the integration can be found in [Open Targets’ MCP Server Documentation](https://github.com/opentargets/open-targets-platform-mcp).

‍

## **Setting up the Open Targets integration**

**For Organization Owners (Team and Enterprise)**

1.  Navigate to Admin settings \> Connectors
2.  Click "Browse connectors"
3.  Click “**Open Targets**”
4.  Click “Add to your team”

**For Individual Claude Users**

1.  Navigate to Settings \> Connectors
2.  Find “**Open Targets**”
3.  Click “Connect”

Learn about [finding and connecting tools](https://support.claude.com/en/articles/11724452-browsing-and-connecting-to-tools-from-the-directory) in Claude.

**For Claude Code Users**

1.  Command: `/plugin marketplace add anthropics/life-sciences`
2.  Command: `/plugin install open-targets@life-sciences`
3.  Restart Claude Code
4.  Verify that the server is connected with /mcp

Technical details of the Open Targets integration can be found in [Open Targets’ MCP Server Documentation](https://github.com/opentargets/open-targets-platform-mcp).

‍

## **Example use cases**

- **Target Discovery Researcher Studying a Disease**\
  - A neuroscience researcher at a pharmaceutical company’s early discovery team, exploring novel therapeutic targets for Alzheimer’s disease. They need to assess which targets show the strongest evidence of association with the disease and understand the types of supporting evidence. They may then want to further prioritize targets based on the evidence.\
    - Example Prompt: *"What are the top five targets associated with Alzheimer disease?"*
  - The Platform provides a ranked list of targets based on overall association scores and a breakdown of the evidence across multiple data types. From there, they can ask further questions about the targets and the evidence.

&nbsp;

- **Statistical Geneticist Browsing Studies**\
  - A statistical geneticist at an academic research institute is investigating genetic variants associated with early onset Alzheimer’s disease. They are reviewing existing genetic evidence for PSEN1 and need to understand what genome wide association studies (GWAS) have been conducted and the most likely causal variants, which populations were studied, and how these findings compare across studies.\
    - Example Prompt: *"Do you have any GWAS evidence for PSEN1? What studies are there?"*
  - The Platform can provide a list of studies and credible sets containing PSEN1 with variant-level information and study metadata, and links to original publications. The user can further query the information in these studies and credible sets. 

&nbsp;

- **Target Prioritisation Using Safety Data**\
  - A translational scientist on a target selection committee is evaluating potential drug targets for an anti-inflammatory programme. They need to understand the safety profile associated with targeting this protein to inform risk-benefit discussions, including known adverse events and safety issues, evidence from clinical trials, post-marketing surveillance, and genetic studies. \
    - Example Prompt: *"Are there known safety events associated with targeting PTGS2?"*
  - The Platform provides comprehensive safety information from multiple sources, which the user can explore in more detail, and compare information for different targets.

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

[Using the ClinicalTrials.gov Connector in Claude](/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude)

Using the ClinicalTrials.gov Connector in Claude

Using the ClinicalTrials.gov Connector in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-clinicaltrials-gov-connector-in-claude)

Tutorial

[ Using the ToolUniverse Extension in Claude](/resources/tutorials/using-the-tooluniverse-extension-in-claude)

Using the ToolUniverse Extension in Claude

Using the ToolUniverse Extension in Claude

Tutorial

[Tutorial](/resources/tutorials/using-the-tooluniverse-extension-in-claude)

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

[English (US)](/resources/tutorials/using-the-open-targets-connector-in-claude)

[日本語 (Japan)](/ja-jp)

[Deutsch (Germany)](/de-de)

[Français (France)](/fr-fr)

[한국어 (South Korea)](/ko-kr)
