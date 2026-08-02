---
title: "OffDeal Claude Agent SDK case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/offdeal"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:03Z"
tags: ["agents", "sdk", "subagents"]
---

# OffDeal powers every stage of M&A advisory with one Claude-based agent


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Financial services

Company size:

Small

Product:

Claude Agent SDK

Claude Platform

Location:

North America

25% to 85% internal eval accuracy

after migrating to the Claude Agent SDK and refining MCP design and prompting

5 to 8 concurrent deals managed by each banker,

with AI handling work across every phase of the deal lifecycle

[OffDeal](https://offdeal.io/) is an AI-native investment bank that helps founder-led businesses sell their companies. By pairing bankers with software engineers, the firm brings full-service M&A advisory to businesses making \$1 to \$20 million in annual profit, the largest segment of the market by deal count but historically the least served.

## With Claude, OffDeal:

- Increased eval accuracy from 25% to 85% after switching to the Claude Agent SDK and iterating on MCP design and prompting
- Dropped failed API calls from context overflow to zero overnight
- Consolidated 12+ independent agentic workflows into a single general-purpose agent, Archie
- Achieved 5 to 8 concurrent deals managed by each banker, with AI handling work across every phase of the deal lifecycle
- Built a buyer sourcing agent that runs autonomously for up to 4 hours, researching potential acquirers across 10 different sourcing methods
- Equipped each banker to meet 2 to 3 new potential clients per day, supported by AI-generated prep and materials 
- Closed 8 deals totaling \$91M in transaction value in the firm’s first year, with a team of two bankers

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

## Context, not intelligence, as the bottleneck

OffDeal uses AI across virtually every stage of a deal, from originating new clients to finding buyers, preparing materials, and running diligence. "I think we're the only investment bank in the world that has more engineers than bankers," said Ori Eldarov, CEO and founder at OffDeal. "We have 5 engineers and 4 bankers right now." Before the Claude Agent SDK, each of these workstreams ran on its own dedicated agentic workflow: one for building seller lists, another for buyer lists, another for creating confidential investment memorandums, and so on.

"Each individual API call was smart,”  Eldarov explained. “But because we had to define the best way to solve a certain problem in advance, if we came across a problem outside the predefined instructions, the models did very poorly." The brittleness compounded with scale: OffDeal was growing fast, and every time a standard operating procedure changed, the corresponding workflow broke.

But the deepest constraint was context. A single deal can involve more than a hundred million tokens of relevant information: buyer profiles, past transactions, financial documents, market data. "The gap was coming not from the model intelligence, but from context, lack of context," Eldarov said. The team had been using a long-context model from another provider, packing the full context into each call to preserve accuracy over RAG. That approach worked until they hit the million-token limit, at which point API calls simply failed.

## The solution

Financial services

Accelerate financial due diligence, modeling, and analysis with enterprise-grade AI built for compliance and security.

Read more

[Read more](/solutions/financial-services)

Read more

Financial services


Accelerate financial due diligence, modeling, and analysis with enterprise-grade AI built for compliance and security.


Financial services

Accelerate financial due diligence, modeling, and analysis with enterprise-grade AI built for compliance and security.

## Claude Agent SDK for subagent orchestration

The team started investigating solutions: custom compaction, auto-summarization, and structured note-taking. Then they came across an early blog post about the Claude Agent SDK. "It seems like this is a solved problem with coding when you're traversing super large codebases," Eldarov noted. "How different is really traversing a bunch of files on different buyers from that?"

The Agent SDK's built-in context management, including subagent orchestration and automatic compaction, meant the team could stop building workarounds and focus on banking workflows.

## One agent across the entire deal lifecycle

Since December, OffDeal has consolidated nearly all of its AI workloads into Archie, a single general-purpose agent built on the Claude Agent SDK. Archie is connected to more than 20 data sources and handles work across every phase of a deal. 

Instead of hardcoding each workflow, the team now builds modular capabilities they call "skills," self-contained instructions that Archie can combine and apply flexibly. Take buyer sourcing: finding the right 300 to 400 potential acquirers out of millions of companies and tens of thousands of private equity firms. An experienced banker would typically use roughly 10 different approaches, from checking past deal activity to scanning company websites for active acquisition mandates and current portfolio investments and works across all of them simultaneously, using findings from one to refine another.

OffDeal encoded that expertise into a buyer sourcing skill. A long-running agent now handles the work autonomously for up to 4 hours, researching buyers across all 10 methods, cross-referencing findings, and recursively refining its search with a level of depth and individual vetting that would be difficult to sustain manually across hundreds of candidates. The same buyer list would traditionally take a team of analysts more than a week to assemble and cost upward of \$12,000. The agent produces it for roughly \$200 in compute. And because it can programmatically sweep every permutation of sector, geography, and acquisition history, “it surfaces buyers that a human team would be unlikely to find regardless of time or budget,” Eldarov added.

The skill architecture also opened up iteration to non-engineers. When OffDeal needed branded presentation capabilities, it was a banker, not an engineer, who built the skill. The banker taught Claude the firm's design system: fonts, margins, indentation, and 20 different slide templates. "End-to-end, no engineering was required, and now every banker on the team can use it," Eldarov said. “We’ve created hundreds of decks since then.” Each deck takes about an hour with Archie, compared to the 30 to 40 hours a traditional team would spend on research, production, and review cycles.

“It surfaces buyers that a human team would be unlikely to find regardless of time or budget.”

Ori Eldarov

CEO and founder


## The outcome

## A step change in accuracy and capacity

The impact showed up immediately. Context overflow failures, previously a persistent source of broken workflows, dropped to zero. "We basically never ran out of tokens after that," Eldarov said. "We just stopped getting that error."

With reliability solved, the accuracy gains followed. "Just switching to the SDK moved our score on that eval from 25% to 60%," Eldarov said. "That's a massive climb on an eval, just from switching a few lines of code." The eval is an internal benchmark that scores Archie’s accuracy on complex, multi-part M&A queries executed over real production data, often spanning 10 million to more than 100 million tokens of deal context. Each test case is evaluated against actual deal outcomes and human-verified data. He noted that 60% represents a composite score across complex qualitative and quantitative rubrics, not a simple pass/fail rate. Since then, improvements to MCP design and prompting have pushed the score to 85%.

Each OffDeal banker now manages five to eight concurrent deals and meets two to three new potential clients per day, supported by Archie's ability to rapidly prepare materials and generate analysis. In its first year, the firm closed eight deals totaling \$91M in transaction value with a team of two, in a market where a single deal typically takes 9 to 12 months. In 2026, OffDeal’s average deal size climbed from \$11M to over \$20M. The team can now prototype new capabilities in Claude Code and push them to production almost overnight, because both environments run on the same SDK.

A year in, the new process is working. Businesses that historically couldn’t attract investment banking coverage now get the same rigor of process, from buyer sourcing to deal execution, that was once reserved for much larger transactions. OffDeal plans to expand beyond its current focus on sell-side M&A, adding buy-side advisory, capital raises, and debt origination as it works toward becoming a full-service investment bank. “Effectively, Archie is your deal team,” Eldarov said. “You basically get the hive mind of the firm available to you.”

“Just switching to the SDK moved our score on that eval from 25% to 60%. That's a massive climb just from switching a few lines of code.”

Ori Eldarov

CEO and founder

## Related stories

[How Satispay's engineers write 75% of their code with Claude](/customers/satispay)

How Satispay's engineers write 75% of their code with Claude

How Satispay's engineers write 75% of their code with Claude

Customer story

[Customer story](/customers/satispay)

Customer story

[Money Forward builds an AI-native engineering organization with Claude Code](/customers/money-forward)

Money Forward builds an AI-native engineering organization with Claude Code

Money Forward builds an AI-native engineering organization with Claude Code

Customer story

[Customer story](/customers/money-forward)

Customer story

[Nevis accelerates advisor productivity with Claude](/customers/nevis)

Nevis accelerates advisor productivity with Claude

Nevis accelerates advisor productivity with Claude

Customer story

[Customer story](/customers/nevis)

Customer story

[How Parcha built a universal customer diligence agent in two weeks with Claude Agent SDK](/customers/parcha)

How Parcha built a universal customer diligence agent in two weeks with Claude Agent SDK

How Parcha built a universal customer diligence agent in two weeks with Claude Agent SDK

Customer story

[Customer story](/customers/parcha)

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
