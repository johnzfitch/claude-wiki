---
title: "AirOps Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/airops"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:19Z"
tags: ["agents", "api"]
---

# AirOps doubles team productivity and ships agents in weeks with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Startup

Product:

Claude Platform

Claude Code

Claude Enterprise

Location:

North America

2x productivity across the team

Internal consensus from org-wide Claude Enterprise and Claude Code adoption

Prototype to production in weeks

Agent SDK eliminated orchestration overhead, accelerating development velocity

[AirOps](https://www.airops.com/) helps marketing teams at Ramp, Kayak, Chime, Carta, and Rippling understand how their brand shows up in AI search and create content to win more visibility. Claude powers both sides of the platform—generating long-form content that meets a rigorous quality bar, and evaluating it before it ships. AirOps works with customers to measure AI visibility, find high-impact content opportunities, and produce outputs at scale. In the last year, AirOps 5x'd its revenue and doubled internal productivity, with engineering moving from prototype to production in weeks after adopting the Claude Agent SDK.

## With Claude, AirOps achieved:

- 2x productivity across the team, with individual employees reporting 20 to 40 hours saved per week through Claude Enterprise and Claude Code
- Org-wide adoption of Claude, including Claude Code for building internal tools and apps, shared design system skills, and Claude Enterprise as the daily operating environment across marketing, sales, and engineering
- Prototype-to-production timelines compressed from months to weeks after adopting the Agent SDK
- Measurable results for customers using the AirOps platform, including a 3x citation rate increase and 89% time reduction in content creation for Chime, and a 300% content velocity increase for Carta

## The challenge

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Read more

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

Read more

Building agents with the Claude Agent SDK


The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.


Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

## Balancing creativity, accuracy, and performance at scale

Great content needs to reflect a brand's voice, deliver genuine information gain for readers, and perform well in search to reach its intended audience. Most models struggle to hold all three requirements at once, and often fall short on quality or perform inconsistently as prompts grow more complex.

AirOps scores every piece of content against dozens of checks before it publishes: paragraph structure, source citations, whether the core answer appears in the first 150 words. The platform needed a model that could handle both sides: generating content that met these standards and evaluating content against them before publication.

"There is always a healthy tension in great organic content," Alex Halliday, AirOps CEO, explained. "It needs to be a balance between brand, performance, and information gain. Most models fail to strike that balance, either struggling with creativity or instruction adherence."

## The solution

Introducing Agent Skills

Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.

Read more

[Read more](https://claude.com/blog/skills)

Read more

Introducing Agent Skills


Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.


Introducing Agent Skills

Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.

## Selecting Claude for voice consistency and coherence

AirOps benchmarks models against an internal quality framework that balances structure, accuracy, information gain, and discoverability. Claude consistently scored highest on the dimensions that matter most for marketing content.

"Opus consistently outperformed on what matters for marketing: natural writing, instruction following, and voice consistency across long-form content," Halliday said. "The team also found that Claude reliably handled complex requirements without losing coherence. That's a key factor for content workflows where a single generation step might involve brand voice guidelines, SEO constraints, competitive positioning, and factual grounding simultaneously."

AirOps also uses Opus and Sonnet models to help design and configure content workflows for customers within their platform.

## Building an agent runtime on Claude

Claude runs through AirOps as both the engine powering customer agents and as the tool the AirOps team uses to build and ship.

The workflow builder that powered AirOps' early customer results required a human to identify which page was underperforming, decide what to do, trigger the workflow, and verify the output. That works when you're updating dozens of pages, but most teams need to scale to thousands of pieces of content across multiple brands, channels, and competitive contexts that shift daily.

To help teams meet that scale, AirOps' product shifted from workflow tool to agent runtime, built on Claude and the Claude Agent SDK. AirOps started with Claude's API for content workflows, then adopted the Agent SDK to push further. AirOps agents use "playbooks": execution instructions that give agents dynamic, adaptive behavior. Claude interprets the playbook, decides which AirOps tools to call, and executes across sections rather than following a rigid sequence. Sub-agents from the SDK handle specific subtasks like research, drafting, and evaluation with isolated context windows.

"Sub-agents are a must-have for managing the context window," Halliday noted. "Context management has been the single biggest thing that improved our quality."

Hooks let them add determinism and validation at specific points in a workflow while keeping autonomous behavior elsewhere.

On top of the SDK, AirOps built a governed environment that controls what the agent knows, how it plans, what it can act on via MCP, what brand and quality rules it follows, and how it coordinates with other agents and humans.

"Prompts are portable," Halliday explained. "Any team can copy a good prompt. The harness that governs how agents operate, the brand context they draw from, and the decision history they accumulate? That provides compounding value to customers."

AirOps went from initial SDK prototype to production in weeks. "Previous orchestration frameworks were brittle. Setup decisions sometimes required full refactors, and testing different configurations took enormous effort," Halliday said. "Development with the SDK was straightforward and more powerful. Time to quality went from 60 hours to 5 hours."

The SDK also changed how the engineering team spends its time. The team now spends that reclaimed time refining outputs and catching edge cases before customers hit them. 

"Before, we spent a lot of time rerouting LLM calls, updating schemas, and dealing with orchestration configurations whenever we made changes," Halliday said. "Now we focus on output quality and the human-to-agent experience."

"Opus consistently outperformed on what matters for marketing: natural writing, instruction following, and voice consistency."

Alex Halliday

CEO, AirOps


## The outcome

## 2x productivity and a new way of working

When AirOps polled their team on Claude's impact, the responses were specific. One team member reported completing two weeks of work in one week. Another described spending 15 to 20 hours per week in Claude Enterprise alone, plus 40 hours weekly in Claude Code. The consensus across the team was a 2x increase in productivity, with individual savings ranging from 20 to 40 hours per week.

Internally, AirOps built an org-wide skill that encompasses their full visual and web design system. Any team member can now generate on-brand assets, slide decks, and one-pagers without filing a design ticket. The AirOps MCP connector gives every employee direct access to brand voice and visual guidelines, product knowledge, and knowledge base content during creation. Infrastructure that would have taken months to build manually was embedded in daily workflows within a single quarter.

For customers on the AirOps platform, Chime saw a 3x citation increase with a 89% time reduction in content creation. Carta 4x'd quarterly top-of-funnel output (5 to 20 articles) with a 75% citation rate on AirOps-built pages. LegalZoom cut Reddit response workflows from 48 hours to under 30 minutes. 

## Looking ahead

AirOps' agent runtime is currently in alpha with customers including Ramp, Carta, Klaviyo, LegalZoom, Xero, Vanta, and AssemblyAI, with general availability planned for May 2026. AirOps is building toward a future where their agents move from surfacing gaps in AI search visibility to acting on them autonomously, with the right human checkpoints built in.

"We're building toward a world where an agent identifies an underperforming page, drafts updated content grounded in brand voice, and publishes it, with a human only needing to confirm strategy and provide edits when needed," Halliday added. "Claude is central to that vision."

"Development with the SDK was straightforward and more powerful. Time to quality went from 60 hours to 5 hours."

Alex Halliday

CEO, AirOps

## Related stories

[Dust enables agents to go deeper at lower cost with Claude](/customers/dust)

Dust enables agents to go deeper at lower cost with Claude

Dust enables agents to go deeper at lower cost with Claude

Customer story

[Customer story](/customers/dust)

Customer story

[How Vercel built an ecosystem on the open skills standard](/customers/vercel-qa)

How Vercel built an ecosystem on the open skills standard

How Vercel built an ecosystem on the open skills standard

Customer story

[Customer story](/customers/vercel-qa)

Customer story

[Box builds document creation into its AI agent with Claude](/customers/box)

Box builds document creation into its AI agent with Claude

Box builds document creation into its AI agent with Claude

Customer story

[Customer story](/customers/box)

Customer story

[Juno helps people with chronic illness find patterns in their symptoms with Claude](/customers/juno)

Juno helps people with chronic illness find patterns in their symptoms with Claude

Juno helps people with chronic illness find patterns in their symptoms with Claude

Customer story

[Customer story](/customers/juno)

Customer story

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
