---
title: "Sentry Claude Managed Agents case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/sentry"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:50Z"
tags: ["agents"]
---

# How Sentry built end-to-end bug fixing with Claude Managed Agents


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Medium

Product:

Claude Managed Agents

Location:

North America

Weeks instead of months

to ship end-to-end fix automation with Managed Agents

Over 1 million RCAs

(Root Cause Analysis) efficiently processed a year

Claude Managed Agents: Get to production 10x faster

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

Read more

[Read more](https://claude.com/blog/claude-managed-agents)

Read more

Claude Managed Agents: Get to production 10x faster


We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

Video caption


Claude Managed Agents: Get to production 10x faster

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

[Prev](#)

Prev


[Sentry](https://sentry.io/welcome/) is a software monitoring platform that ingests billions of events daily, giving development teams the context they need to debug production issues. Their AI debugging agent, Seer, already used Claude to identify root causes accurately. But telling developers what's wrong wasn't enough. They wanted Seer to fix it, too.

With [Claude Managed Agents](https://claude.com/blog/claude-managed-agents), Sentry built the infrastructure to go from bug detection to merge-ready pull request, without building a custom agent runtime from scratch.

## **With Claude, Sentry achieved:**

- End-to-end automation from bug detection to pull request, powered by Claude Managed Agents
- Ability to efficiently process over 1 million RCAs (Root Cause Analysis) a year
- Near immediate reviews provided on over 600k pull requests a month
- Initial Managed Agents integration shipped in weeks instead of months by a single engineer
- Elimination of the ongoing operational overhead of maintaining custom agent infrastructure

## **The challenge: A gap between knowing what's broken and fixing it**

Sentry provides deep context for every error: stack traces, profiling data, trace connections, logs, spans, and metrics. When Seer launched, it used Claude to analyze all that telemetry, identify root causes, and suggest code fixes. Developers at every level got faster.

"Developers are often overwhelmed by the amount of context they need to reason through to debug a problem," said Indragie Karunaratne, Senior Director of Engineering, AI/ML at Sentry. Seer helped junior developers navigate that complexity and gave senior engineers quick summaries so they could apply their expertise to validation rather than investigation.

But even with a diagnosis and a suggested fix in hand, developers still had to context-switch into their codebase, plan the implementation, write the code, and open a pull request. That handoff from diagnosis to resolution is where time and momentum were lost. Sentry wanted to close the loop: take Seer's root cause analysis and turn it into a finished PR automatically.

Building that capability meant running a coding agent. And running a coding agent meant building sandboxing, lifecycle management, and an agent runtime. For a team focused on debugging, that was a significant detour.

## **The solution: Why Sentry chose Claude and Managed Agents**

Sentry had already selected Claude for Seer after evaluating multiple AI models. Security factored heavily: running Claude through Vertex AI let Sentry minimize data shared outside Google Cloud. "We were able to preserve data residency for our customers and avoid having to add a new subprocessor by using Claude through Vertex AI,” Karunaratne said.

When it came time to extend Seer from diagnosis to automated fixing, Claude Managed Agents was a natural fit. It provided the secure agent runtime, sandboxing, and lifecycle management that Sentry would have otherwise spent months building. And there was pull from Sentry's customer base: many were already using Claude Code for local and cloud-based development and wanted an experience that bridged Sentry's debugging capabilities with Claude's coding strengths.

Managed Agents let Sentry focus on what differentiated their product, the handoff between Seer's diagnosis and the coding agent, rather than building generic agent infrastructure.

“Managed Agents not only allowed us to build the initial integration in weeks instead of months, but has also eliminated the ongoing operational overhead of maintaining bespoke agent infrastructure.”

Indragie Karunaratne

Senior Director of Engineering, AI/ML, Sentry

## **How the Seer-to-PR workflow runs on Managed Agents**

Seer root causes and fixes the most actionable bugs in the background, while also helping developers in real time, both on the same Managed Agents infrastructure.

Here's what happens when an issue is detected: Seer queries source code and telemetry to build a comprehensive root cause analysis for the issue, drawing on Sentry's rich context of errors, logs, spans, and metrics. Once it has a diagnosis, Seer hands it off to a Claude agent running on Managed Agents. That agent plans a solution, implements the code change, and creates a pull request. The developer's job shifts from writing the fix to reviewing it.

"Turns out telling developers what's wrong with their code isn't enough: they want you to fix it too," Karunaratne said. "Customers can now go from Seer's root cause analysis straight to a Claude agent that writes the fix and opens a PR."

Without Managed Agents, Sentry would have needed to build their own sandboxing capabilities and agent runtime from scratch. Instead, a single engineer shipped the initial integration. The team didn't have to build a coding agent or the infrastructure to support one. They could put that energy into building the best debugging experience and designing the handoff between Seer's analysis and the Claude agent.

"We chose Claude Managed Agents because it gives us a secure, fully managed agent runtime, allowing us to focus our efforts on building a seamless developer experience around the handoff," Karunaratne said. "Managed Agents not only allowed us to build the initial integration in weeks instead of months, but has also eliminated the ongoing operational overhead of maintaining bespoke agent infrastructure."

## **What changes for developers**

The original Seer experience already made debugging faster across the board. Junior developers got support navigating complex issues that would typically require extensive system knowledge. Senior engineers skipped hours of context review and jumped straight to validating Seer's analysis.

“Seer leverages Claude’s ability to quickly and accurately extract relevant patterns out of multimodal telemetry data," Karunaratne explained. “Developers can stay focused on using their domain context to validate the analysis rather than manually combing through events.”

With the Managed Agents integration, that benefit compounds. A developer no longer just gets a diagnosis and a suggested fix. They get a pull request they can review, test, and merge. The workflow moves from "Seer tells you what's wrong" to "Seer tells you what's wrong and proposes the code to make it right,” Karunaratne added. 

## **Looking ahead**

Sentry is building toward a workflow where the most actionable bugs are detected, diagnosed, and fixed automatically, with developers reviewing proposed changes rather than writing them. With Managed Agents handling the agent infrastructure, the team can focus on expanding what Seer covers and pushing the boundary of what automated debugging can handle, without the operational overhead of maintaining a custom runtime.

How security teams use Claude

Claude helps security teams investigate threats, validate findings, and resolve issues faster.

Read more

[Read more](https://claude.com/solutions/security)

Read more

How security teams use Claude


Claude helps security teams investigate threats, validate findings, and resolve issues faster.

Video caption


How security teams use Claude

Claude helps security teams investigate threats, validate findings, and resolve issues faster.

“Customers can now go from Seer's root cause analysis straight to a Claude agent that writes the fix and opens a PR.”

Indragie Karunaratne

Senior Director of Engineering, AI/ML, Sentry


Video caption


[Prev](#)

Prev


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
