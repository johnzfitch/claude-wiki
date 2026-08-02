---
title: "Duvo Claude Agent SDK case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/duvo"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:41:57Z"
tags: ["agents", "enterprise", "sdk"]
---

# Duvo automates enterprise operations across legacy systems with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Startup

Product:

Claude Platform

Location:

EMEA

€2.8M+ in annualized savings

captured in three months for one multi-billion-euro retailer

Eight weeks from first conversation to production deployment

with measured savings, on average

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


[Duvo](https://www.duvo.ai/) builds AI agents that run procurement, supply chain, and category management processes for multi-billion-euro retail and CPG companies. The agents work across every system involved: ERPs, supplier portals, spreadsheets, email, even phone calls. Duvo is built entirely on Claude, using the Agent SDK to orchestrate across workflows, with every API call running under Anthropic's Zero Data Retention mode.

## **With Claude, Duvo achieved:**

- €2.8M+ in annualized savings within three months for its customer Rohlik Group, across processes that had never been systematically run
- Annual supplier negotiations shortened by one month at Rohlik Group, with approximately 80% automated from preparation through contract generation to ERP write-back
- 40%+ of team capacity freed up on average across enterprise procurement, supply chain, and retail operations by reducing manual work
- Eight weeks on average from first conversation to production deployment with measured savings
- Production deployment within days of adopting the Claude Agent SDK

## **The challenge: The cost of "abandoned work" in enterprise operations**

Duvo's customers have operations teams that know exactly what needs to happen but can't get to all of it. Buyers manage ordering across SAP, supplier portals, and email. Category managers track commodity prices in spreadsheets they built themselves. Procurement coordinators chase confirmations by copying status between systems. These teams cover the top 20 suppliers and the most urgent issues. But the long tail, hundreds of smaller actions worth millions in aggregate, never get touched.

"The real process lives in people's heads: which supplier needs chasing, which portal field actually matters, which exception to escalate and which to just fix," said Marek Paris, co-founder and CPTO at Duvo. “The reason no one has automated these processes before is that the work crosses too many systems.” 

The blocker isn't a missing dashboard. The work spans systems that don't connect, and no two companies use the same stack. Traditional automation stalls because there are no clean APIs, the IT backlog is years long, and every exception requires judgment. Duvo calls this "abandoned work": processes worth millions that nobody runs because there aren't enough hours in the day.

## **The solution: Selecting Claude for messy, multi-step work**

After evaluating multiple model providers, Duvo committed to a single-provider architecture on Claude. The product defaults to Sonnet 4.6, with browser-use agents often using Opus 4.6.

"What set Claude apart was its performance on messy, ambiguous tasks," explained Tomas Čupr, co-founder and CEO. "Parsing a supplier email that half-confirms a delivery while raising a pricing dispute. Navigating a SAP GUI screen with dozens of fields. Making judgment calls on exceptions without hallucinating business rules."

Two factors cemented the decision: First, the model’s reasoning depth was especially strong for multi-step work. Second, the developer tooling then closed the gap. MCP, the Agent SDK, and computer use gave Duvo a complete foundation for running agents in production, with structured human-in-the-loop workflows and Zero Data Retention on every API call. Building on a single provider's stack meant fewer integration seams and a consistent security model across every agent run. "Other providers offer a model. Anthropic offers the infrastructure to run agents in production with the governance enterprises require," Paris said. "When we saw all of these working together, with Claude's model quality as the foundation, going all-in was straightforward.”

“When we saw all of these working together, with Claude's model quality as the foundation, going all-in was straightforward.”

Marek Paris

Co-founder and CPTO, Duvo

## **Agents that cross every system boundary**

Duvo's agents operate these systems through their actual interfaces, not through APIs that may not exist. "Claude's computer use and MCP integrations are what made this technically possible," said Ondrej Romancov, Head of Product Engineering. "Before that, the heterogeneity of enterprise stacks was an unsolvable problem for automation." 

A single agent run might log into a supplier portal, extract delivery status for 50 purchase orders, cross-reference against SAP, identify discrepancies, check contract terms, decide whether to escalate or auto-correct, send follow-up emails, and log the outcome—all in one session.

"Before the SDK, critical context disappeared between agent handovers," Romancov said. "Now we run one capable agent per job with access to all the tools it needs. Context stays intact across the entire operation."

High-risk actions require human approval. When a human responds, the agent persists that decision for future runs. Over time, the system accumulates the operational judgment that used to exist only in people's heads.

## **The outcome: Recovering millions in abandoned work**

The results from Rohlik Group, Europe's leading online grocer with more than €1.5 billion in revenue, illustrate what becomes possible. The retailer tracks thousands of commodity-linked SKUs across five markets. Before Duvo, this happened quarterly at best, often not at all. Duvo now monitors continuously, builds negotiation cases, and initiates supplier outreach. The result: €1.45M in annualized savings in the first week, from continuous price monitoring and automated supplier outreach across 120+ SKUs and 15+ suppliers. Not from a process that was slow, but from one the company had never been able to run. "This is the clearest example of 'abandoned work' becoming real value," Paris said.

“That was one process,” said Olin Novák, CRO at Rohlik Group. “We're now running dozens." Across three months, that number grew to €2.8M+ in annualized savings. 

Across other Rohlik workflows, promotional setup dropped 65-70%, supplier onboarding chasing fell 50-70%, and supply chain planning moved product availability from 78% to 93% in two weeks. “Not because someone built an integration,” Paris said. “Duvo works through the same screens the team was using. It just doesn't forget, doesn't deprioritize, and doesn't stop at the top 20 suppliers.” Annual supplier negotiations shortened by one month, with approximately 80% of the process automated. Inbound delivery confirmations jumped from 52% to 90%, covering every supplier daily. 

With routine execution handled, operations teams can focus on the work their expertise was built for: supplier negotiations, exception strategy, cost optimization, and the judgment calls that require institutional knowledge.

Expansion within accounts happens naturally. Automated ordering surfaces supplier lead-time issues that the returns team can act on. Cost monitoring reveals pricing discrepancies that ordering can prevent upstream. On average, Duvo moves from first conversation to production deployment with measured savings in eight weeks. The team also estimates that 40% of team capacity is freed up on average across enterprise procurement, supply chain, and retail operations by reducing manual work.

Duvo is doubling down on retail and CPG, with manufacturing and logistics next. "There are dozens of high-value operational processes in this industry that have never had a proper system of action," Paris said. "We wanted to close that gap between knowing what should happen and actually making it happen. Across every transaction, every supplier, every system."

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

“What set Claude apart was its performance on messy, ambiguous tasks.”

Tomas Čupr

Co-founder and CEO, Duvo


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
