---
category: "15-Claude-AI-Features"
fetched_at: "2026-02-28T00:43:27Z"
last_modified: "Fri, 27 Feb 2026 22:56:43 GMT"
source_url: "https://claude.com/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork"
title: "How to build a plugin from scratch in Cowork | Claude"
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
    How to build a plugin from scratch in Cowork

Explore here

- [](#)

  Ask questions about this page
- [](#)

  Copy as markdown

# How to build a plugin from scratch in Cowork

Build a Cowork plugin from scratch to encode your team's workflows, institutional knowledge, and tool connections into a repeatable, shareable process.

- 

  Category

  Professional

- 

  Product

  Cowork

- 

  Reading time

  Watch time

  5

  min

  min

- 

  Share

  [Copy link](#)
  https://claude.com/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork

A Cowork plugin is a group of files that can teach Claude how to do a specific job — encoding your methodology, your workflows, your tool connections.\
\
Anthropic publishes [pre-built plugins](https://claude.com/plugins) for common roles like [Sales](https://claude.com/plugins/sales), [Finance](https://claude.com/plugins/finance), and [Legal](https://claude.com/plugins/legal). Customizing those with your company's context can help tailor the plugin to your needs. Building from scratch is for when your team has workflows, processes, or institutional knowledge that existing plugins don't cover.

*To learn more about installing and using plugins in Cowork,* [*visit here*](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)*.*

## Why build from scratch

- **Your workflow doesn't map to an existing plugin.** Your workflow has specifics that an existing plugin doesn't cover, and customizing one doesn't close the gap.
- **You want to encode institutional knowledge for your team.** The way your team actually does things — your standards, your judgment calls, your process docs — packaged so everyone works from the same playbook.
- **You need Claude to coordinate across your tools.** Your workflow pulls from a particular combination of data sources, applies particular criteria, and produces a particular deliverable.

## What's inside a plugin

A plugin can include a few types of components. Claude builds the right combination based on what you describe.

#### **Skills —** domain knowledge Claude draws on based on relevance.

A skill might be a few lines describing a formatting preference, or a detailed methodology covering your full review framework.

Skills can also carry supporting reference documents — playbooks, compliance frameworks, pricing matrices — that Claude loads when relevant. Claude reads each skill's description and draws on it when it matches what you're working on.

#### **Commands** — structured workflows triggered by typing `/` in your prompt.

Commands can instruct Claude how to complete a process or produce an output. A single plugin often includes several commands for different parts of the same function.

Commands can accept inputs, so `/close-package North America` and `/close-package Europe` run the same process with different scope. Recurring commands can run as [scheduled tasks](https://support.claude.com/en/articles/13345190-get-started-with-cowork#h_260d21b5b3) with your criteria applied each time. Commands can also chain to each other, where the output of one feeds the next.

#### **Connectors** — link Claude to your tools.

A plugin works without connectors — you can upload data manually or describe the situation — but connected tools let Claude pull what it needs mid-workflow and write results back.

You can direct Claude to search broadly across a connected tool or look in a specific place, depending on what the workflow needs.

#### **Sub-agents** — specialized helpers for complex tasks.

One agent might research a company while another pulls data from your CRM and a third scans Slack for context. They can run in parallel or in sequence, each with its own focus and fresh context window.

## How to create a plugin

Understanding the components within a plugin can give you a framework for what to share while building one: your **knowledge and judgment calls** become skills, your **repeatable tasks** become commands, your **data sources** become connectors. If you have existing documents or examples of deliverables you've been happy with, share them — Claude maps it to the relevant parts of the plugin.

In Cowork, describe the plugin you want to build — even a sentence is enough to start.

A simpler start works too — Claude will follow up with questions about your workflow, your tools, your standards, and how you handle edge cases.

> *"I need a plugin for our customer success team"*

## What changes with a plugin

With detailed instructions, Claude can handle many of these workflows. A plugin packages them into commands anyone on the team can run.

‍

### [Finance](https://claude.com/plugins/finance)

> *"Here's our P&L. Materiality threshold is \$25K. Decompose by price, volume, and mix. Check these GL accounts against the subledger. Format the JE with debits on top."*

###### **Without a plugin: **Claude can handle it, but restating your full close methodology every session is overhead that compounds, and the output might vary depending on who's giving Claude the instructions.

> `/monthly-close` North America

###### **With your plugin:** Skills load your chart of accounts, materiality thresholds, close calendar, and narrative standards. Connectors pull from your data warehouse. The command runs the full process — a new analyst runs it and gets consistent rigor.

### [Sales](https://claude.com/plugins/sales)

> *"Pull usage data for Meridian Health from our analytics dashboard. Check for support escalations in the last 90 days. Compare their current contract against our pricing tiers. Score the renewal risk and flag expansion opportunities."*

###### **Without a plugin:** You're directing Claude to each source, restating your scoring criteria, and specifying the output format every time.

> `/renewal-score` Meridian Health

###### **With your plugin:** Skills hold your scoring criteria and competitive positioning. Connectors pull from your CRM and analytics dashboard. Claude scores the account and flags expansion opportunities — consistent quality whether a senior rep or a new hire runs it.

### [Legal](https://claude.com/plugins/legal)

> *"Review this vendor agreement. Our standard on indemnification is capped at 2x contract value. Flag auto-renewals over 12 months. Use GREEN/YELLOW/RED."*

###### **Without a plugin:** This prompt covers a few checks on one contract. A full review applies dozens of standard positions across every clause type, and you'd need to restate all of them for each new agreement.

> `/due-diligence`

###### **With your plugin:** Skills hold your standard positions across every clause type and your severity classifications. A connector accesses the data room. Claude reviews every document against your playbook and produces a risk-rated summary.

## Refining your plugin

- **Use it on real work and refine as you go.** If you run a command and something's off — a step is missing, the criteria need adjusting, the output format isn't right — tell Claude and it can update the plugin files directly. Looking through the files after Claude builds them can also help spot gaps early.
- **Show Claude the deliverable.** Upload an example or point Claude to one in a connected drive. Claude picks up the structure, emphasis, and formatting directly.
- **Keep skills focused.** Claude composes multiple skills when a task spans several areas, and focused skills with specific descriptions tend to activate more reliably than broad ones. If a skill isn't loading when you expect, its description is likely too vague — structure it as *what it does, when to use it, what it covers.*
- **Consider sub-agents for multi-source or long-running tasks.** If a workflow pulls from several tools at once, or if a task regularly hits context limits from processing too much in one pass, sub-agents let Claude split the work across separate context windows.

## Things to know

- **Plugins work in Cowork, not Chat.** Your plugin's skills and commands are active in the Cowork tab.
- **Plugins live on your machine.** They don't sync across devices or to teammates automatically. You can share them as a compressed file, host them on GitHub for automatic updates, or have an admin provision them across your org. [*Learn more about sharing plugins.*](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)
- **Skills and connectors can also live outside plugins.** If you have personal context that applies across everything you do in Cowork — not tied to one plugin — you can add standalone skills and connectors in settings.

*Cowork with plugins is available as a research preview for all paid Claude plans (Pro, Max, Team, Enterprise) on macOS and Windows. Browse* [*available plugins*](https://claude.com/plugins)*.*

## Learn more

- ‍[Getting started with Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork)
- [Using plugins in Cowork](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork)
- [‍](https://code.claude.com/docs/en/plugins)[Browse plugins](https://claude.com/plugins)

## Related tutorials

[How to customize plugins in Cowork](/resources/tutorials/how-to-customize-plugins-in-cowork)

How to customize plugins in Cowork

How to customize plugins in Cowork

Tutorial

[Tutorial](/resources/tutorials/how-to-customize-plugins-in-cowork)

Tutorial

[Navigating the Claude desktop app: Chat, Cowork, Code](/resources/tutorials/navigating-the-claude-desktop-app)

Navigating the Claude desktop app: Chat, Cowork, Code

Navigating the Claude desktop app: Chat, Cowork, Code

Tutorial

[Tutorial](/resources/tutorials/navigating-the-claude-desktop-app)

Tutorial

[Get the most from Claude Opus 4.6](/resources/tutorials/get-the-most-from-claude-opus-4-6)

Get the most from Claude Opus 4.6

Get the most from Claude Opus 4.6

Tutorial

[Tutorial](/resources/tutorials/get-the-most-from-claude-opus-4-6)

Tutorial

[How to use Claude in Excel for accounting: Revenue model validation](/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation)

How to use Claude in Excel for accounting: Revenue model validation

How to use Claude in Excel for accounting: Revenue model validation

Tutorial

[Tutorial](/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation)

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

[English (US)](/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork)

[日本語 (Japan)](/ja-jp)

[Deutsch (Germany)](/de-de)

[Français (France)](/fr-fr)

[한국어 (South Korea)](/ko-kr)
