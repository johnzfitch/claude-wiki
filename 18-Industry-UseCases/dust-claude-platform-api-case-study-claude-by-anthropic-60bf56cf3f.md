---
title: "Dust Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/dust"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:30Z"
tags: ["agents", "api", "enterprise", "prompting"]
---

# Dust enables agents to go deeper at lower cost with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Startup

Product:

Claude Platform

Claude Code

Location:

Europe

\$10k/day saved

on model spend after optimizing prompt caching

8+ tool-calling steps per agent run

up from 4–5, with no engineering changes needed

[Dust](https://dust.tt/) is a multiplayer AI platform for human-agent collaboration. It gives companies a shared workspace where teams can build, deploy, and manage model-agnostic AI agents connected to their company knowledge, tools, and workflows. The agents read from a company's stack and write back to it: updating the CRM, drafting the report, or kicking off the workflow, without writing code. Teams at companies like Datadog, Vanta, and 1Password use Dust and together have deployed more than 300,000 agents.

## With Claude, Dust achieved:

- An 18% reduction in overall model spend, roughly \$10K per day, after optimizing prompt caching
- Increased cache reads from 30% to 65% of input tokens, cutting input spend by 22%
- An increase in autonomous tool-calling depth from 4–5 to 8+ steps per agent run, with no engineering changes
- A redesigned execution loop supporting up to 24 tool calls per run
- Deep Research workflows, orchestrated by Claude, that run for 10+ minutes across data warehouses, the web, and internal sources
- A standard integration layer built on Model Context Protocol (MCP), with Dust operating as both client and server

## The challenge

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Read more

[Read more](/product/claude-code)

Read more

Claude Code


Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.


Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

## Agents enterprise teams trust with real work

Dust's premise is that the people who build the most useful AI agents are the ones closest to the work. That includes the RevOps lead automating deal prep, the chief of staff rebuilding onboarding, or the support manager who turns ticket routing into a system. Dust calls them AI operators. "They're not always engineers,” said Stanislas Polu, co-founder and CTO of Dust. “They're the people who understand the work deeply enough to build the systems that automate it." 

For that premise to hold, the agents those operators build must be able to act reliably across a company's systems. What makes this possible is the model behind them. As Polu put it: "You can't save time with AI you don't trust. Our goal was to make AI agents accurate and capable enough that enterprise teams trust them to do real work, not just answer questions."

## The solution

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Choosing the right Claude model


Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.


Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## Choosing the model agents could trust

Dust allows customers to pick the model behind any Dust agent from a dropdown menu, with no code changes required. In those comparisons, one pattern held, Paul said: “Claude consistently stood out on the criteria that matter most: instruction-following, nuanced writing, and reliable tool use.”

The difference showed up most clearly in autonomous research. As Claude's agentic capabilities improved, the number of sources it consulted for a single research task grew from five to fourteen. "The new Claude models didn't just answer the question; it proactively explored adjacent information and synthesized across sources," Polu noted. "That behavior is exactly what enterprise agents need."

## Complex workflows with optimized prompt caching 

Dust provides the orchestration, trust, and enterprise infrastructure around models like Claude. This includes an LLM picker and soon an automatic router, a retrieval pipeline connecting more than 100 data sources, a framework for delegating work across sub-agents, and the no-code agent builder itself. It also includes robust governance to control how Dust agents operate across a company’s systems: permission-aware retrieval, role-based access, and audit logs keep each agent within the data and tools its user is cleared for. Each model, including Claude, gets its own prompting and context strategy beneath the interface, so more capable models never translate into added complexity for users.

Earlier models produced truncated or unreliable results past a handful of tool calls; once Claude could chain many steps accurately, Dust raised the limit. "Our existing defaults, three tools per run with a maximum of eight, were too restrictive,” Polu said. “The model would hit the tool limit and produce truncated results." Dust redesigned its execution loop to support up to 24 tool calls per run.

That autonomy opened up complex workflows that weren't practical before. Dust's Deep Research agents now orchestrate sub-agents across data warehouses, the web, and internal sources, running for ten minutes or more to produce a single synthesized report. But the trade-off to longer runtime was increased token consumption. To offset this, Dust worked with Anthropic's Applied AI team to optimize prompt caching, landing on a three-tier structure: globally shared instructions cached for an hour, with workspace and per-user context on shorter windows. 

Dust also adopted Model Context Protocol (MCP), the open standard Anthropic created for connecting models to tools. As an MCP client, Dust's agents reach any compatible tool through one standard interface, creating an issue, updating a CRM record, or querying a database without a custom integration built for each; as a server, Dust exposes its own agents and context to other MCP-aware systems, the wiring that makes it the orchestration layer between Claude and a company's tools.

"The new Claude models didn't just answer the question; it proactively explored adjacent information and synthesized across sources."

Stanislas Polu

Co-founder and CTO of Dust


## The outcome

## \$10K a day saved, and agents that run deeper

The caching work paid off first on the bill. Cache reads doubled from about 30% to 65% of input tokens, input spend fell 22%, and overall model spend fell 18–19%: roughly \$10K saved per day. That efficiency gives Dust more capacity to run agents deeper and longer, instead of spending it on repeated context.

Use cases like deep research and workflow orchestration have helped Dust spread across teams, driving an average of 70% weekly active usage across customer organizations. That same pattern is visible inside Dust’s own team, where engineers use their day-to-day work as a testing ground for what the platform can bring to customers. "The role of an engineer at Dust is evolving from writing code to directing, reviewing, and orchestrating AI-generated output," Polu said. More attention now goes to architecture, product judgment, and quality. 

Claude Code is one of the tools driving that: a day-to-day coding partner, a GitHub Action reviewing pull requests, and a way to turn well-scoped tasks into ready-for-review PRs. One engineer built a skill that pulls company context from Dust mid-session. It is part of a broader move that took AI-written code at Dust from roughly 30% in early 2025 to between 60% and 90% today, depending on the engineer. The transition happened in weeks instead of months. “We're still figuring out what it means to be a great engineer in this paradigm," Polu said. "But we're pushing the envelope of what a small, focused team can ship when AI handles more of the mechanical work and humans focus on the decisions that actually matter."

"The role of an engineer at Dust is evolving from writing code to directing, reviewing, and orchestrating AI-generated output."

Stanislas Polu

Co-founder and CTO of Dust

## Related stories

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

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)

A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)

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
