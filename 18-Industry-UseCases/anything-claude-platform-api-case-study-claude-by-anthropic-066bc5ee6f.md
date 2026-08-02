---
title: "Anything Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/anything"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:41:46Z"
tags: ["agents", "api", "prompting"]
---

# Anything builds coding agent for 1.5 million users with Claude Agent SDK


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Startup

Product:

Claude Platform

Location:

North America

800,000+ apps

created in five months

91-96% agent success rate

with complex product builds from databases to App Store deployment

A non-technical founder built and is already selling a full recruiting platform. A creator with no engineering background published a social app to the App Store. Across [Anything's](https://anything.com) platform, 1.5 million users are turning ideas into working software products without writing code. Anything’s AI agent, powered by Claude and the Agent SDK, handles the full build: databases, backend logic, mobile deployment, App Store submission, and payments. 

## With Claude, Anything achieved:

- 800,000+ apps built in the last five months by users, many of whom have never written code
- 91-96% agent success rate—measured by completion rates, agent self-reports, and user feedback—with complex product builds from databases to App Store deployment
- Evolution from simple single-page tools to full-stack, multi-platform applications with backends, mobile apps, API and AI integrations, and product paywalls
- Implementation in days rather than weeks
- Internal adoption of Claude across support, inbound sales, product feedback analysis, and codebase improvement

## The challenge

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Choosing the right Claude model


Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.


Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## Closing the gap between idea and working product

The goal of helping non-technical people create software predates Anything's current stack. Before Claude, the models they relied on were prone to outages. The team ended up building multi-stage code generation pipelines—calling separate agents to produce code and manually splicing it in—and relying on RAG pipelines to locate relevant code and package documentation, leaving little room to focus on the actual product. Single-page applications were achievable. But a production-quality product with databases, integrations, and mobile deployment was a different problem entirely.

Serving a non-technical audience raised the bar further. The agent couldn't just produce code: it needed to handle complex workflows reliably, correct its own errors across long building sessions, and maintain quality throughout. "It was unclear how to go from simple tools to something much deeper," says Marcus Lowe, co-founder of Anything. “Once AI models reached the level of reliable instruction following, parallel tool-calling, and consistent tool reliability, it became clear how it could fit into our stack and help us evolve from simple solutions to something that could support more complex product creation.”

## The solution

agent success rate


agent success rate


91-96%

agent success rate

## Why Anything chose Claude

Anything ran structured evaluations across several criteria: compliance with user instructions, ability to build relatively complex applications, performance across many rounds of tool calling and error correction in long conversations, and precision and recall with minimal hallucinations. "Claude models came out on top in those evaluations, so they became the best fit for our agent architecture," Lowe said.

The evaluation went beyond raw generation quality. Anything's architecture gives the agent full visibility into the user's stack, including runtime behavior, not just the codebase. That design requires a model with strong tool calling, reliable reasoning across many steps, and consistent coding quality. “Anthropic's specific focus around coding abilities is what drove Claude to the top for us,” said software engineer Ahmad Jiha. “The warmth and personality of Claude models resonates with our users. That's why we default to Claude in the product.”

Claude's performance in those areas let the team shift their focus from keeping the AI functional to launching a better agent experience. "Reliability at scale was also important, and that allowed us to focus more on building the agent and solving the full user job rather than just making the AI function,” Lowe said. “The warmth and personality of Claude models resonates with our users. That's why we default to Claude in the product.” 

Built with the Agent SDK, the team had Claude integrated in a day. Opus 4.6's performance was strong enough from the start that they didn't need the weeks of testing and iteration they'd typically budget for a new model.

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Building agents with the Claude Agent SDK


The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.


Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

## The outcome

## From prompt to a published app

Claude runs throughout Anything's stack: the core product-building agent, subroutines within it, and internal processes that improve development workflows. What distinguishes Anything from simpler code-generation tools is scope. Rather than producing isolated snippets, the agent handles entire product-building workflows end to end.

"There is a baseline level of quality needed to move from simple or single-page applications to multi-page, full-stack apps that integrate many libraries and cover a wide range of use cases," Lowe said. In practice, that meant unlocking full-stack, multi-platform applications with backends, mobile apps, API and AI integrations, and product paywalls. "Claude helped us reach that level of quality, which allowed us to support much more complex applications and deliver a better overall user experience."

The results show up in what users ship: Shane, a non-technical founder, used Anything to build PipelinePro, a recruiting ATS and client-intelligence platform with Zoho Recruit sync, candidate scoring, AI interview bots, and a client portal. He's already demoing and selling to customers. Laurent, a French film director, launched Telefan, a streaming app helping people discover thousands of hard-to-find French TV films, with voice-driven discovery. A user with no engineering background built The Collective, a social app for making friends and meeting people in the Philadelphia area. Another user is creating an AI radio station where listeners can generate music through the ElevenLabs API and earn royalties when their tracks are played, with a discovery marketplace in development.

In the last five months alone, users have built more than 800,000 apps, with the agent maintaining a 91-96% success rate as measured by generation completion rates, agent self-reports, and in-product user feedback. Beyond the customer-facing product, Anything uses Claude internally to power agentic workflows across support, inbound sales, product feedback analysis, and improving parts of the company's own codebase with Claude Code. 

## Looking ahead: Long-running agents at scale

Anything is building toward more advanced agents capable of massive parallelization and long-running processes. The team expects user-built apps to increasingly become self-improving as the agents grow sophisticated enough to handle complexity that users previously managed themselves.

"We're building toward agents that can work on multiple parts of a product simultaneously," Lowe said. "We're just seeing the beginning. The apps our users build will start improving themselves."

"The warmth and personality of Claude models resonates with our users. That's why we default to Claude in the product.” 

Ahmad Jiha

Software Engineer, Anything

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
