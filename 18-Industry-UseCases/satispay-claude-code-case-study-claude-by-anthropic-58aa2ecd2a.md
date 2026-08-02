---
title: "Satispay Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/satispay"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:50Z"
tags: ["agents", "claude-code"]
---

# How Satispay's engineers write 75% of their code with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Financial services

Company size:

Medium

Product:

Claude Code

Claude Enterprise

Claude Cowork

Location:

EMEA

75%+ of code committed each month

is generated with Claude

10x faster core payment service modernization

from a four-week estimate to under four days

[Satispay](https://www.satispay.com/en-it/) is Italy's leading independent payment network, with 6 million consumers and more than 450,000 merchants using its app to pay in stores, send money, and manage everyday finances. Behind the product is an engineering organization maintaining a mature Java and Spring estate that processes every payment on the network. Claude Code now runs on every engineering laptop, and Claude Cowork has spread organically across several business units.

## With Claude, Satispay:

- Generates over 75% of code committed to Satispay's repositories each month
- Achieved 10x faster modernization of the core transaction service, safely completing a Java 8 to Java 21 and major Spring upgrade in under four days against a four-week estimate
- Cut data transformation lambdas from three to five days to under an hour
- Completed an 18-month code update roadmap in 7 months
- Saw over 90% Claude Code adoption across engineering, with full rollout in 30 days managed  by IT support 

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

## A junior team on a mature payments codebase

When Chief Technology Officer Fabio Rapposelli joined in 2025, the team was weighted toward earlier-career engineers and the codebase had some legacy services that were hard to maintain. With much of the work focused on maintenance and incremental development, early-career engineers spent more time reading than writing and senior review had become the bottleneck.

"A junior engineer facing an unfamiliar service needs help understanding the system, not help finishing a line of code," Rapposelli said. Earlier experiments with autocomplete-style AI coding tools had stayed in pockets and never addressed that gap.

The default workflow showed the strain. An engineer would pick up a ticket, spend significant time orienting in a service they had never touched, draft a change, and wait for a senior to review it. That review was carrying three jobs at once: teaching, quality gate, and context transfer. Roadmap velocity suffered, and senior time was going to enable others rather than building.

## The solution

Claude Code on the web

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

Read more

[Read more](https://claude.com/blog/claude-code-on-the-web)

Read more

Claude Code on the web


Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.


Claude Code on the web

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

## Making Claude available from day one

Satispay ran a structured 30-day evaluation in mid-2025 comparing Claude Code against another AI coding tool on real tickets across its Java and Spring services. The rubric covered code generation quality, refactoring, adherence to internal patterns, multi-file context understanding, test generation, and documentation. Claude won on every dimension except IDE integration. "Claude Code's output, both the code it wrote and the reviews it produced, was considered best across the board,” explained Rapposelli. “Claude's reviews caught real issues, with real explanations, at a quality our engineers recognized as genuinely useful," Rapposelli said. "Other tools weren't playing in the same league."

Rollout took 30 days from decision to full coverage and was handled by IT support. Claude Code ships to every engineering laptop through Satispay's managed device fleet, so it is available on an engineer's first day with nothing to configure. Engineers use it to write new code, modify existing services, navigate unfamiliar parts of the codebase, and run a Claude review pass before human review. They reach for Opus or Sonnet depending on the task, with full access to the 1M-token context window. Spend is managed at the budget level rather than per seat, so no one pauses mid-task to justify reaching for a more capable model.

The cultural work mattered as much as the rollout. Satispay added AI proficiency to its engineering performance framework, and the operating rule is explicit: engineers own what lands in the repository. "The model is an accelerator, not an authority," Rapposelli said.

Beyond the default tooling, the team builds reusable assets. Standard Java scaffolding for new services and tests starts from an encoded pattern instead of a blank file. Modernization approaches get packaged into subagents so the next team inherits the work. The most concrete example is data transformation: AWS Lambda functions that engineers used to write by hand are now generated from a specification by an internal subagent connected to an MCP server. "Lambdas would routinely take over three days to build," Rapposelli explained. "Now it takes less than an hour."

The expansion beyond engineering surprised even Rapposelli. Once Claude skills became visible internally, requests came in at a rate of roughly 20 a day from finance, legal, marketing, and operations, including the CFO asking for access to financial analysis skills he had spotted himself. "People across the company knew they had AI-shaped problems," Rapposelli said. "When the tool showed up, they didn't need permission to solve them."

"Claude Code's output, both the code it wrote and the reviews it produced, was considered best across the board."

Fabio Rapposelli

Chief Technology Officer, Satispay


## The outcome

## Updating the system behind every payment 

The clearest single proof point is the evolution of Satispay's core transaction service, the system that runs every payment on the network. The team took it from Java 8 to Java 21 and through a major Spring upgrade in under four days, when the original estimate was four weeks. The broader update program tells the same story at a larger scale: goals the team had set for an 18-month horizon were complete in 7, fast enough that an external consulting engagement brought in for the work was no longer needed.

Across the organization, more than 75% of code committed each month is generated with Claude, and adoption sits above 90% of engineers. Senior engineers are spending more of their time on architecture, and early-career engineers are operating with far more independence on a codebase that used to slow them down. The team is now planning to ship roughly 50% more features in the first half of the year..

"We're moving to a model where the engineer becomes an engineering manager of agents," said Rapposelli. "Individual engineers are operating above their years because the agents close the gap."

## Looking ahead: From task automation to agentic workflows

Two pilots already running point to what comes next. Issue-to-PR automation has Claude draft pull requests from tickets filed by other teams, with engineers owning the review and the merge. Agentic fraud investigation moves a workflow tied directly to financial loss from human-in-every-step to agent-led, with people kept in the loop on the decisions that warrant it. "Right now we're focused on automating the task and keeping a human in the loop for critical decisions," Rapposelli said. "The work ahead is understanding which decisions genuinely need a person, and which ones we've simply been used to making ourselves."

"We're moving to a model where the engineer becomes an engineering manager of agents. Individual engineers are operating above their years because the agents close the gap."

Fabio Rapposelli

Chief Technology Officer, Satispay

## Related stories

[OffDeal powers every stage of M&A advisory with one Claude-based agent](/customers/offdeal)

OffDeal powers every stage of M&A advisory with one Claude-based agent

OffDeal powers every stage of M&A advisory with one Claude-based agent

Customer story

[Customer story](/customers/offdeal)

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
