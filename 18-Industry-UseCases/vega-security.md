---
title: "Vega Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/vega-security"
category: "18-Industry-UseCases"
fetched_at: "2026-08-18T06:26:22Z"
tags: ["agents", "api", "bedrock", "case-studies", "security", "skills"]
---

# Vega's cyber defense platform returns 67% of analysts' time with Claude


[Try Claude](https://claude.ai)


[Contact sales](https://www.claude.com/contact-sales)


Industry:

Cybersecurity

Company size:

Startup

Product:

Claude Agent SDK

[Claude Platform](https://claude.com/platform/api)

Partner:

AWS

Location:

North America

Completes investigations up to 44 times faster with 82% lower costs

than legacy SIEMs

Cut triage from 25 minutes to less than 3 minutes

at a Fortune 500 company

[Vega](https://vega.io/) is an agentic cyber defense platform for enterprises, including Fortune 200 companies, global banks, and leading healthcare providers. The Vega platform runs an agentic cyber defense loop of detection, triage, investigation, and optimization directly on security data where it lives, without ingestion or centralization, with Claude as a reasoning engine behind it.

## With Claude, Vega:

- Completes investigations up to 44 times faster with 82% lower costs than legacy SIEMs 
- Cuts triage from 25 minutes to \<3 minutes for a Fortune 500 company
- Reclaims roughly 67% of cyber defense engineering team’s time 

## The challenge

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

Claude on Amazon Bedrock


Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.


Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

## Security teams could defend and reason across only what they could afford to ingest

Most large enterprises have security data spread across dozens of tools and cloud environments. In theory they could ingest everything into a security information and event management (SIEM) platform, but this is often too complex and cost-prohibitive at enterprise scale. Security teams typically ingest only the fraction they can afford, and everything outside it becomes a blind spot. That can make it difficult to run queries, detection, or investigation at scale.

AI made the tradeoff sharper. "AI agents are only as effective as the data they can access, and most security architectures are either too fragmented or too slow to support agentic cyber defense at scale," explained Eli Rozen, Co-founder and CTO. A security operations center (SOC) that only sees a sampled slice of the environment inherits every blind spot the sampling created. For one top-four global bank, visibility into Amazon VPC Flow Logs, AWS CloudTrail, and Microsoft 365 telemetry sat out of reach, as ingesting it into a legacy SIEM would have cost an additional \$6 million.

## The solution

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Choosing the right Claude model


Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.


Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## One model family, the right depth at every layer

Vega set out to build agentic cyber defense: agents that detect cyberattacks, then triage, investigate and optimize themselves against the whole environment. The team chose Claude to power those agents in production. “As an AI-native company, we built Vega to work with best-in-class frontier models like Claude from day one, establishing that level of reasoning as the baseline for our platform,” Rozen said. 

Reasoning a security team will act on has to clear a high bar, and Vega set a baseline of accuracy using the most capable Claude model, then worked backward to optimize for cost and efficiency without losing quality.

The deciding factor is the range. "Claude gives us the ability to work within a single model family and apply the right level of intelligence exactly where it’s needed across Haiku, Sonnet, and Opus," Rozen explained.

Vega matches each layer of the pipeline to the Claude model tier that fits it: the deepest reasoning goes to confirmed alerts, where the stakes are highest, while high-volume work like log analysis and summarization runs on lighter, faster tiers. "Customers feel this as speed and precision at scale; our own team feels it as being able to keep unit economics reasonable, while ensuring cyber defense engineers have frontier-level answers where it counts," Rozen noted.

## Building on Agent Skills

Within the platform, Vega built on Anthropic’s Agent Skills format to introduce [detection skills](https://vega.io/blog/vega-introduces-detection-skills), an open standard that allows cyber defense engineers to codify their expertise as an agentic loop: how to triage, investigate, and optimize a detection, written when it is authored and applied to every alert. Vega released the standard at [detectionskills.io](http://detectionskills.io), enabling security teams across platforms to encode and share their judgment with the community. 

When a detection fires, the loop runs on that judgment. Triage skills decide whether the alert escalates to an incident, with the reasoning attached. Investigation skills analyze the incident before a human looks: forming a hypothesis, gathering evidence, and drafting an explainable conclusion with recommended next actions. Optimization skills write approved verdicts back into the detection, so it fires sharper next time. Engineers sign off on every change, so the judgment stays theirs while the repetitive work finishes before they arrive. 

## Running it in production: Amazon Bedrock, EU residency, and resilience

Inference reaches customers through Amazon Bedrock, with zero data retention, no training on customer data, VPC endpoints keeping traffic off the public internet, and pass-through pricing; the direct Claude API runs alongside it for internal tooling and Claude Code. As usage has scaled, Amazon Bedrock's cross-region inference has absorbed load spikes without Vega having to build that capacity itself.

As a global company, Vega needs to serve organizations with compliance, privacy, and data sovereignty requirements in every region. When a customer needed EU data residency for GDPR, Vega stood up a dedicated control plane in Frankfurt, running Amazon Bedrock's EU-hosted Claude models, in under three weeks. 

"As an AI-native company, we built Vega to work with best-in-class frontier models like Claude from day one, establishing that level of reasoning as the baseline for our platform."

Eli Rozen,

Co-founder & CTO, Vega Security


## The outcome

## Two-thirds of analyst time back

Across production deployments, customers reclaim roughly 67% of analyst time, complete investigations up to 44 times faster, and pay up to 82% less for data than legacy SIEM ingestion. One Fortune 500 insurer cut mean time to triage from 25 minutes to under 3, and the top-four global bank gained the \$6 million worth of telemetry it previously couldn't afford. Underneath those numbers sits the full picture: The Vega platform completes a scan across more than 1 billion CloudTrail logs spanning 17 AWS regions in 41 seconds, against a 30-minute manual baseline, ensuring frontier AI can reason across the entire environment, rather than a sample of it.

"Scaling frontier reasoning to every detection is the ultimate win for our customers,” Rozen explained. "With adversaries using AI to bypass static rules in legacy SIEMs, we’re bringing the judgement of your best cyber defense engineers to every alert, in real time.” At a leading cybersecurity company, Vega uncovered a live malware infection that signature-based tools had missed entirely. An investment banking firm ran a proof of value and decided to replace its legacy SIEM with Vega's platform. A Fortune 500 technology manufacturer brought Vega in to monitor a large-scale Claude Code deployment for AI agent-specific risks such as prompt-based privilege escalation and unauthorized MCP installations.

Next, Vega is shipping agentic search, which lets AI agents execute complete multi-step threat hunts across an organization's entire security environment. “Choose the right model for each task instead of defaulting to the largest model,” Rozen advised. “Rigorously measure quality in production, and build durable platform capabilities that outlast any single foundation model."

"Claude gives us the ability to work within a single model family and apply the right level of intelligence exactly where it’s needed."

Eli Rozen,

Co-founder & CTO, Vega Security

## Related stories

[Cyera on making Claude Cowork the front door to 40 tools](cyera-qa.md)

Cyera on making Claude Cowork the front door to 40 tools

Cyera on making Claude Cowork the front door to 40 tools

Customer story

[Customer story](cyera-qa.md)

Customer story

[Cyera scales agentic AI across 1,500 employees with Claude Enterprise ](cyera.md)

Cyera scales agentic AI across 1,500 employees with Claude Enterprise

Cyera scales agentic AI across 1,500 employees with Claude Enterprise

Customer story

[Customer story](cyera.md)

Customer story

[Kai delivers preemptive exposure management with Claude ](kai.md)

Kai delivers preemptive exposure management with Claude

Kai delivers preemptive exposure management with Claude

Customer story

[Customer story](kai.md)

Customer story

[How Artemis helps security teams cut incident resolution time by 96%](artemis.md)

How Artemis helps security teams cut incident resolution time by 96%

How Artemis helps security teams cut incident resolution time by 96%

Customer story

[Customer story](artemis.md)

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

  [Claude](../15-Claude-AI-Features/product-overview.md)
  Claude

- Claude Code

  [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
  Claude Code

- Claude Code for Enterprise

  [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
  Claude Code for Enterprise

- Claude Cowork

  [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
  Claude Cowork

- @Claude

  [@Claude](../14-Connectors/claude-for-slack.md)
  @Claude

- Claude Design

  [Claude Design](../15-Claude-AI-Features/product-design.md)
  Claude Design

- Claude Science

  [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
  Claude Science

- Claude Security

  [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
  Claude Security

- Download app

  [Download app](https://www.claude.com/download)
  Download app

- Pricing

  [Pricing](../17-Billing-Plans/pricing.md)
  Pricing

- Log in

  [Log in](https://claude.ai/login)

Features

- Claude in Chrome

  [Claude in Chrome](https://www.claude.com/claude-in-chrome)
  Claude in Chrome

- Claude for Microsoft 365

  [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)
  Claude for Microsoft 365

- Skills

  [Skills](https://www.claude.com/skills)
  Skills

Models

- Mythos

  [Mythos](../15-Claude-AI-Features/claude-mythos.md)
  Mythos

- Fable

  [Fable](../15-Claude-AI-Features/claude-fable.md)
  Fable

- Opus

  [Opus](https://www.claude.com/15-Claude-AI-Features/claude-opus-4-6-anthropic.md)
  Opus

- Sonnet

  [Sonnet](https://www.claude.com/15-Claude-AI-Features/claude-sonnet-4-6-anthropic.md)
  Sonnet

- Haiku

  [Haiku](https://www.claude.com/15-Claude-AI-Features/claude-haiku-4-5-anthropic.md)
  Haiku

Solutions

- AI agents

  [AI agents](agents.md)
  AI agents

- Code modernization

  [Code modernization](code-modernization.md)
  Code modernization

- Coding

  [Coding](coding.md)
  Coding

- Customer support

  [Customer support](customer-support.md)
  Customer support

- Cybersecurity

  [Cybersecurity](cybersecurity.md)
  Cybersecurity

- Enterprise

  [Enterprise](enterprise.md)
  Enterprise

- Financial services

  [Financial services](finance.md)
  Financial services

- Government

  [Government](government.md)
  Government

- Healthcare

  [Healthcare](healthcare.md)
  Healthcare

- Higher education

  [Higher education](education.md)
  Higher education

- K-12 teachers

  [K-12 teachers](teachers.md)
  K-12 teachers

- Legal

  [Legal](legal.md)
  Legal

- Life sciences

  [Life sciences](life-sciences.md)
  Life sciences

- Nonprofits

  [Nonprofits](nonprofits.md)
  Nonprofits

- Small business

  [Small business](small-business.md)
  Small business

Claude Platform

- Overview

  [Overview](https://www.claude.com/platform/api)
  Overview

- Developer docs

  [Developer docs](../04-API-Reference/Other/home.md)
  Developer docs

- Pricing

  [Pricing](../17-Billing-Plans/pricing.md#api)
  Pricing

- Ecosystem

  [Ecosystem](https://www.claude.com/ecosystem)
  Ecosystem

- Marketplace

  [Marketplace](https://www.claude.com/platform/marketplace)
  Marketplace

- Claude on AWS

  [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
  Claude on AWS

- Google Cloud

  [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
  Google Cloud

- Microsoft Foundry

  [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
  Microsoft Foundry

- Regional compliance

  [Regional compliance](https://www.claude.com/regional-compliance)
  Regional compliance

- Console login

  [Console login](../04-API-Reference/Other/usage-limits.md)
  Console login

Resources

- Blog

  [Blog](https://www.claude.com/blog)
  Blog

- Claude partner network

  [Claude partner network](../04-API-Reference/Other/partners.md)
  Claude partner network

- Community

  [Community](https://www.claude.com/community)
  Community

- Connectors

  [Connectors](../04-API-Reference/Other/partners-mcp.md)
  Connectors

- Courses

  [Courses](https://www.anthropic.com/learn)
  Courses

- Customer stories

  [Customer stories](customers.md)
  Customer stories

- Engineering at Anthropic

  [Engineering at Anthropic](https://www.anthropic.com/engineering)
  Engineering at Anthropic

- Events

  [Events](https://www.anthropic.com/events)
  Events

- Plugins

  [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
  Plugins

- Powered by Claude

  [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
  Powered by Claude

- Service partners

  [Service partners](../04-API-Reference/Other/partners-services.md)
  Service partners

- Tutorials

  [Tutorials](https://www.claude.com/resources/tutorials)
  Tutorials

- Use cases

  [Use cases](https://www.claude.com/resources/use-cases)
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

  [Research](../19-Reference/anthropic-com-research.md)
  Research

- News

  [News](../19-Reference/news.md)
  News

- Policy on the AI Exponential
