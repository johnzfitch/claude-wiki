---
title: "LG CNS Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/lg-cns"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:40Z"
tags: ["claude-code"]
---

# LG CNS modernizes 20-year-old enterprise systems with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Professional services

Company size:

Large

Product:

Claude Code

Partner:

AWS

Location:

Asia Pacific

99.1% API conversion completion

2,888 of 2,913 APIs migrated from a 20-year-old legacy system

7-month full migration

delivered at roughly 50% of the cost of a conventional rebuild

LG CNS is the IT services and digital transformation arm of LG Group, with approximately 7,000 employees and \$4.2 billion in 2025 revenue. The company has built and operated mission-critical systems for financial institutions, manufacturers, and public-sector organizations for more than 35 years. Claude Code is the engine of its newest offering: LG CNS Build Factory, a turn-key software development service that modernizes decades-old enterprise systems at production scale.

## With Claude, LG CNS:

- Converted 2,888 of 2,913 APIs from a 20-year-old legacy system, a 99.1% completion rate
- Delivered a multi-million dollar system migration in seven months, at roughly 50% of the cost of a conventional rebuild
- Migrated 1,340 screens from a proprietary legacy frontend platform to React, with backend and frontend converted simultaneously on 24/7 parallel tracks
- Adopted Claude Code as the standard development approach across the 200-engineer Build Center
- Made a new category of project viable: modernizations that customers had deferred for years because of cost, risk, and specialist shortages

## The challenge

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

Claude on Amazon Bedrock


Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.


Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

## The modernization projects that never get started

The migration requests landing at LG CNS follow a pattern. Customers need stored procedures over 10,000 lines long moved to a modern database, or Oracle Forms screens rebuilt in React. Many need to retire MiPlatform, proprietary UI platforms that dominated Korean enterprise IT two decades ago and have now reached end of service.

These systems are mission-critical, but the engineers who understand them are scarce and the documentation is thin. "From the customer's perspective, modernization is clearly necessary, but cost, timeline, and quality risks make it difficult to initiate," explained Hyosup Bae, Director and Head of Build Center at LG CNS.

One engagement made the bind concrete. A Korean construction company ran its projects on a 20-year-old project management system covering everything from winning an order through final settlement. The company needed to move onto a modern stack, with a fixed deadline and a tightly constrained budget.

Conventional delivery would have taken at least twice the available time and money, at an estimated cost of several billion Korean won. Offshore development did not change the math: dozens of developers writing in parallel against a poorly documented codebase makes consistency harder, not easier. Without a different approach, the project was not going to start.

## The solution

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Read more

[Read more](/product/claude-code)

Read more

Claude Code


Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.


Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

## A software factory built around Claude Code

LG CNS tested multiple models, starting from the position that public benchmarks are useful only as a reference point. The criterion that mattered most was task completion: does the model finish what it was asked to do? The team evaluated planning capability, to-do sequencing, tool-calling behavior, and what happened when a model hit an error. Could it find an alternative path, or did it stall?

Claude stood out for understanding intent, not just instructions. "While other models were able to execute given tasks reasonably well, Claude often interpreted what was not explicitly stated and proposed outputs that were more closely aligned with the underlying objective of the problem," Bae said. The difference was clearest in architecture design for large projects, where Claude behaved "less like a code generator and more like a consultant that could understand the problem and propose a direction for solving it."

Access mattered as much as capability. LG CNS reaches Claude through Amazon Bedrock, which lets the team run Claude inside the AWS security configurations its enterprise customers already have in place. For clients in regulated industries such as financial services, that changed the nature of the adoption discussion. "The conversation shifts from 'Can we trust this model?' to 'How can we use a technology that is already within our security boundary?'" Bae noted.

Selecting the model was only half the equation. Enterprise customers need far more than generated code: they expect security, compliance, testing, and uniform quality across thousands of APIs and screens.

To deliver that, the Build Center, LG CNS's 200-engineer technology delivery organization, built an engineering orchestration layer around Claude Code. The harness connects legacy analysis, business logic extraction, code generation, testing, verification, and quality management.

A typical project runs in pods of five to seven people: a Solution Owner, Architect, Engineers, and DevOps. Work starts with planning, where the team presents the project objective and intent to Claude and asks it to propose an approach.

Once the direction is set, work is decomposed into small, clearly scoped tasks defined in YAML. Context is chained through the local file system, with each stage's output stored as files and passed to the next. The team relies on Claude Opus 4.6 for core work: architecture design, legacy analysis, complex code generation, and multi-step workflow execution.

The file-mediated approach began as a workaround. Before the 1M-token context window and memory features arrived, preventing quality degradation as context accumulated was the team's hardest engineering problem. The patterns LG CNS designed to solve it, persistent file-based memory and multi-agent coordination through file handoffs, anticipated capabilities Anthropic later shipped natively.

The team still treats decomposition and context chaining as core strategy. At enterprise scale, maintaining context taxonomy and output consistency matters more than raw context length.

The design philosophy is deliberately restrained. "Trust the model," Bae advised. "Building an overly thick harness to prevent every possible failure constrains the model's performance and increases token consumption." Instead, LG CNS uses a thin, multi-layered harness, with lightweight layers for validation, context scoping, and quality checks that preserve Claude's ability to reason while providing the stability enterprise projects require.

"The ROI is not simply that we did it faster. The ROI is that we made a previously difficult-to-start project possible."

Hyosup Bae

Director and Head of Build Center, LG CNS


## The outcome

## Proof on a real customer system

The approach was validated on the construction PMS itself: a multi-billion-won, next-generation rebuild delivered between November 2025 and June 2026, at roughly 50% of the cost of a conventional rebuild. The system is in final testing ahead of its scheduled launch in June 2026.

The project achieved a 99.1% API mapping completion rate, with 2,888 of 2,913 APIs converted. On the frontend, 1,340 screens moved from MiPlatform to React across a main portal and a partner portal. Backend and frontend conversion ran simultaneously through 24/7 parallel-track operations.

"The ROI is not simply that we did it faster," Bae said. "The ROI is that we made a previously difficult-to-start project possible."

The work itself has shifted for senior engineers. Their role now centers on setting direction: defining the tasks a large-scale project requires, decomposing them along the right boundaries, and establishing the work sequence and chaining strategy between them. "Once the strategy and direction are set correctly, the details are then refined to fit the on-site situation and the nature of each individual task," Bae explained.

For customers, the most meaningful change is not speed. Migrations they had deferred for years are now realistic options, discussed not as open-ended risks but as executable transformation roadmaps. "The most memorable customer reaction has been the realization that this is now possible," Bae said.

LG CNS plans to develop LG CNS Build Factory into a rigorous, verifiable modernization discipline, investing in deterministic validation through decision-making, automated quality measurement against golden datasets, and a harness that improves itself over time. As the team sees it, the two layers compound.

"The model gets more capable, the harness becomes more sophisticated, and as the two evolve together, the quality and scale of modernization outcomes we can deliver to customers will continue to improve," Bae said.

"The model gets more capable, the harness becomes more sophisticated, and as the two evolve together, the quality and scale of modernization outcomes we can deliver to customers will continue to improve."

Hyosup Bae

Director and Head of Build Center, LG CNS

## Related stories

[Caylent turns months of migration work into days with Claude Agent SDK](/customers/caylent)

Caylent turns months of migration work into days with Claude Agent SDK

Caylent turns months of migration work into days with Claude Agent SDK

Customer story

[Customer story](/customers/caylent)

Customer story

[How can a two-person fabrication studio make room for problems it’s never solved before?](/customers/bla-studios)

How can a two-person fabrication studio make room for problems it’s never solved before?

How can a two-person fabrication studio make room for problems it’s never solved before?

Customer story

[Customer story](/customers/bla-studios)

Customer story

[How Blank Metal, a lean professional services firm, runs on Claude Cowork](/customers/blank-metal-qa)

How Blank Metal, a lean professional services firm, runs on Claude Cowork

How Blank Metal, a lean professional services firm, runs on Claude Cowork

Customer story

[Customer story](/customers/blank-metal-qa)

Customer story

[Quantium scales Claude across Australia's largest enterprises](/customers/quantium-qa)

Quantium scales Claude across Australia's largest enterprises

Quantium scales Claude across Australia's largest enterprises

Customer story

[Customer story](/customers/quantium-qa)

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
