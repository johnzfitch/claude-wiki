---
title: "eSentire Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/esentire"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:41:50Z"
tags: ["agents", "api", "security"]
---

# How eSentire runs expert-level threat investigations at scale with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Cybersecurity

Company size:

Medium

Product:

Claude Platform

Partner:

AWS

Location:

North America

99.96% ransomware containment before encryption

more than double the industry average of 44%

120,000+ autonomous investigations in 12 months

each averaging 44 tool calls across endpoint, identity, network, and cloud telemetry

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Read more

[Read more](#)

Read more

Introducing Claude Opus 4.6


We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Video caption


Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Read more

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

Read more

Building agents with the Claude Agent SDK


The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Video caption


Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Prev](#)

Prev


eSentire is a managed detection and response (MDR) provider that protects millions of endpoints across thousands of customers worldwide. Its Atlas platform uses Claude to run autonomous threat investigations, analyzing signals across endpoint, identity, network, and cloud telemetry to catch and contain attacks in minutes.

## With Claude, eSentire achieved:

- 99.96% ransomware containment before any file encryption, more than double the industry average of 44%
- Over 120,000 autonomous investigations across its full customer base in 12 months, each averaging 44 tool calls across endpoint, identity, network, and cloud telemetry
- Above 90% alignment with top SOC experts in continuous production evaluation, matching or exceeding human analyst performance
- 6-minute average agentic investigation, where the industry median attacker dwell time is 11 days
- 41% more confirmed attacks detected per customer after deploying agentic investigations, with overall alert volume down 11%

## The challenge: Matching attacker speed without sacrificing depth

AI-powered attacks now run at thousands of requests per second, a pace no human SOC team can match. eSentire needed to investigate live threats across thousands of heterogeneous customer environments, correlating signals across endpoint, identity, network, and cloud layers, and reasoning about attacker intent with incomplete information. The challenge was doing this with the same depth a senior analyst would bring to every signal, not just the ones flagged as critical.

"When attackers can run AI agents that move faster than any human SOC, the only viable response is AI that defends at the same speed and depth," said Dustin Hillard, CPTO of eSentire. "That's what we built on Claude."

## The solution: Why eSentire chose Claude for security reasoning

Standard cybersecurity benchmarks had become saturated, with leading models scoring near-perfect, but those benchmarks present defined problems with verifiable answers. eSentire's production work is fundamentally different: the agent receives a detection event and telemetry sources, but no predefined answer, and has to decide what tools to call, how to interpret contradictory evidence, and what verdict to reach. 

When eSentire evaluated multiple models across real-world security scenarios, Claude provided the highest performance for complex security reasoning. Its agentic capabilities excelled at orchestrating multi-tool workflows while maintaining investigative coherence, essential for MDR work, and each successive model generation has improved on that.

"Benchmarks measure whether a model can solve a known problem in a controlled environment," said Hillard. "We needed Claude to solve unknown problems in live customer environments, thousands of times a day, with expert-level depth on every single one. That's a fundamentally different challenge, and Opus 4.6 is meeting it."

## How eSentire runs agentic investigations with Claude

eSentire's Atlas platform runs Claude Opus 4.6 on Amazon Bedrock through Agent SDK in a multi-agent architecture that mirrors the workflow of a senior SOC analyst. Each investigation averages 44 autonomous tool calls: querying threat intelligence, correlating signals across SIEM and endpoint telemetry, analyzing identity activity, reconstructing attacker behavior across process and network data, and connecting findings across workflows. Over 12 months, the platform executed more than 5 million tool calls, representing 468,000 hours of equivalent expert effort, with each call averaging roughly 5 minutes of analyst work.

Each case follows a structured analytical workflow that would take a senior analyst hours to replicate manually, with multiple sub-agents collaborating on each case.

Where this shows up most clearly is in ambiguous cases. An identity compromise where the attacker's activity overlaps with a legitimate user's normal behavior requires the agent to weigh timing, geography, user agent strings, and email forwarding rules before making a judgment call. Opus 4.6 consistently handles these cases at a level that matches eSentire's best human investigators. And it has to reason effectively across 3,600+ distinct investigation workflows spanning every major EDR, SIEM, and identity platform.

After deploying agentic analysis, eSentire detected 41% more confirmed attacks per customer while reducing overall alert volume by 11%. More real threats caught, less noise. Senior analysts review and act on every critical finding, providing a trust layer that automation alone doesn't provide. The AI analyzes at depth on every signal, freeing the human team to focus on the judgment calls that matter most: customer engagement, containment decisions, and remediation strategy.

"Before agentic investigations, we had to choose between depth and speed," said Hillard. "Now every investigation gets the deep analytical rigor our best experts would apply. That's what changes outcomes."

## The outcome: Measurable containment at production scale

eSentire measures this rigor through continuous production evaluation: senior SOC experts independently review a sample of the same cases the agent has investigated, and alignment is measured across dimensions like whether compromise occurred, severity classification, and recommended response. Across more than 500 adjudicated outcomes, Claude consistently achieves above 90% alignment with senior experts on the final verdict. When compared against junior analysts using the same methodology, the agent outperforms them.

Across 12 months of production, the results are concrete. Of nearly 10,000 escalated incidents across more than 1,400 customers: 

- 31% were blocked before execution, 
- 18% were attempted attacks that failed, 
- 36% were identity compromises detected and remediated before attackers accessed business data, and 
- 14% were device compromises where the SOC detected activity, isolated the host, and drove remediation.

Across nearly two million protected endpoints, attackers achieved lateral movement to a second device in fewer than 0.5% of incidents. Ransomware encrypted files in less than 0.04%. Every one of those cases was detected. The question was never whether the attack was found, but how fast it could be stopped. For context, the global median attacker dwell time is 11 days, and only 44% of ransomware attacks industry-wide are stopped before encryption.

## Looking ahead

The platform is expanding to ingest and respond across any security technology a customer runs, regardless of vendor stack. Each new integration deepens both the investigative context and the response capabilities available to every investigation.

"We're building a platform where every security signal, regardless of vendor, gets the same depth of analysis and quality of outcome," Hillard said. As the threat landscape accelerates, eSentire's bet is that depth and speed aren't a tradeoff anymore.


"We needed Claude to solve unknown problems in live customer environments, thousands of times a day. That's a fundamentally different challenge, and Opus 4.6 is meeting it."

Dustin Hillard

CPTO, eSentire


Video caption


[Prev](#)

Prev


## Related stories

[Kai delivers preemptive exposure management with Claude ](/customers/kai)

Kai delivers preemptive exposure management with Claude

Kai delivers preemptive exposure management with Claude

Customer story

[Customer story](/customers/kai)

Customer story

[How Artemis helps security teams cut incident resolution time by 96%](/customers/artemis)

How Artemis helps security teams cut incident resolution time by 96%

How Artemis helps security teams cut incident resolution time by 96%

Customer story

[Customer story](/customers/artemis)

Customer story

[Cogent resolves security threats 97% faster with Claude](/customers/cogent)

Cogent resolves security threats 97% faster with Claude

Cogent resolves security threats 97% faster with Claude

Customer story

[Customer story](/customers/cogent)

Customer story

[Vanta streamlines compliance remediation with Claude](/customers/vanta)

Vanta streamlines compliance remediation with Claude

Vanta streamlines compliance remediation with Claude

Customer story

[Customer story](/customers/vanta)

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
