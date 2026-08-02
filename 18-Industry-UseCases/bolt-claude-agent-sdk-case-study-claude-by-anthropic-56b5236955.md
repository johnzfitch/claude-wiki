---
title: "Bolt Claude Agent SDK case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/bolt"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:41:50Z"
tags: ["agents", "rag", "sdk"]
---

# Bolt builds autonomous design system agent on the Claude Agent SDK


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Startup

Product:

Claude Agent SDK

Location:

North America

~53-minute average autonomous agent workflow

powered by Claude Opus 4.7, resolving conflicts and mapping tokens across thousands of components

~90% cache efficiency on the Agent SDK

reducing inference costs across high-traffic workflows

[Bolt](https://bolt.new) is a vibe coding tool that lets users build full applications in natural language, with built-in integrations for databases, payments, and deployment. Built by StackBlitz and powered by the Claude Agent SDK, Bolt's newest capability is a design system agent that lets PMs and designers generate production-ready, on-brand prototypes without writing code.

## With Claude, StackBlitz achieved:

- 10,000+ users uploading their own design systems to Bolt
- ~53-minute design system generation, then unlimited on-brand prototypes in ~5 minutes each, with minimal engineer rework needed to ship
- Autonomous design system generation that consolidates Storybook, GitHub repos, npm packages, Figma tokens, and documentation into a unified system
- ~90% cache efficiency on the Agent SDK, reducing inference costs across high-traffic workflows

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

## The problem with fragmented design systems

Most companies don't have their design system in one place. Typography lives in a Google Doc. Components are scattered across Figma files, Storybook instances, and GitHub repositories. Spacing and layout guidelines might be in a wiki, or just in an engineer's head.

That gap has become a major barrier to enterprise adoption of AI development tools. PMs and designers can prototype ideas in tools like Bolt, but without access to the company's actual design language, the result looks generic. "Oftentimes if you just use Bolt, it doesn't have any idea about your company's design system," said Dominic Elm, Founding Engineer at StackBlitz. "And a design system is a somewhat complex system. It has guidelines, typography, spacing, layout, all these things."

The tools can generate code quickly, but the output doesn't match a company's internal standards. Prototypes end up as throwaways: a PM builds something to communicate an idea, but an engineer rewrites it entirely before it can ship. That distance between prototype and production code keeps non-engineers on the sidelines of the development lifecycle.

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

## Why StackBlitz built on the Claude Agent SDK

StackBlitz had built its own internal agent to power Bolt, but as the team planned a major overhaul, the Claude Agent SDK arrived at the right moment. "We were looking at making a ton of improvements to our agent, looking at a v2," Elm explained. "But then the Agent SDK came and it just made a lot of sense to go with something that is already used by so many people."

The decision shifted the team's focus from building and maintaining agent infrastructure to product innovation. StackBlitz's AI team is small. "We have a couple people, but it's probably still nowhere near the people that are working on Claude Code," Elm added. Claude Code's established user base was part of the appeal: the Agent SDK meant StackBlitz didn't need to match that investment to get the same underlying capabilities. The Agent SDK is built on the same harness that powers Claude Code, so StackBlitz could inherit those capabilities without having to match that investment.

## Building a design system agent with Claude

StackBlitz was one of the earliest teams to go all in on the Agent SDK, and the extended experience building on it has shown Elm how flexible the platform is. "The way it's currently shaped just allows you to build almost any workflow," he said.

The design system agent is a case in point. It starts by taking in everything a company has: Storybook sites, GitHub repositories, npm packages, Figma tokens, documentation files. Users point the agent at all their sources and it does a thorough pass across each one, resolving conflicts, mapping design tokens, and understanding component variants. What comes out is a consolidated intermediate representation of the full design system. The agent uses Claude Opus 4.7, which Elm said "showed the best results overall" for the sustained reasoning this research phase demands.

This research phase can run for 40 minutes to an hour and a half depending on how many sources are connected, averaging around 53 minutes. That's a different kind of task than a typical five-minute prototype build. The SDK's hooks made that feasible. With the stop hook, the team can keep an agent running across a long workflow, pass feedback back in, and change the agent's trajectory mid-run. Custom sub-agents handle parallel tasks while keeping the main agent's context clean. "It helps with overall speed because you can parallelize things," Elm noted. "Also, what the sub-agent does isn't polluting the main context window."

The result lives inside Bolt as a browsable library of all the company's components, sections, and pages in one place. StackBlitz was deliberate about not making Bolt the source of truth for a company's design system. Instead, when a team updates their design system on their end, they can come back to Bolt and reindex, and the agent does an incremental update. Once the design system is in place, a user selects it, prompts Bolt to build something, say a car configurator or a comparison page, and the output follows the company's actual components, typography, and spacing. The agent then checks its own work in a review loop. "You build something and then you check again: does this match what it's supposed to look like?" Elm said, comparing the process to how a developer would verify output against a Figma file.

"Agent SDK just allows you to build almost any workflow."

Dominic Elm, Founding Engineer

Stackblitz


## The outcome

## From throwaway prototypes to production code

The design system agent changes what PMs and designers can deliver. The design system is generated once in an autonomous run averaging 53 minutes. From that point on, any team member can prompt Bolt to produce on-brand prototypes in roughly five minutes, generating code that can go to production with minimal rework. "The idea is that Bolt can generate a prototype that is not just a throwaway," Elm said. "You can take it and hand it to an engineer and they can ship that code almost as-is to production and just connect the business logic to the components."

StackBlitz sees roughly 90% cache efficiency on the Agent SDK, keeping inference costs manageable across these long-running workflows. More than 10,000 users have already uploaded their own design systems to Bolt.

## Looking ahead

StackBlitz is focused on broader adoption among companies shipping production code through Bolt. "The goal is to get PMs and designers actually integrated into the development lifecycle and able to contribute to production code," Elm said. "That's the holy grail for almost everyone."

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
