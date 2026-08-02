---
title: "Bubble Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/bubble"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:25Z"
tags: ["api", "prompting"]
---

# How Bubble powers an AI agent that turns prompts into production apps with Claude


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

North America

~30% increase in user satisfaction

With the Claude-powered AI editing agent, compared to the previous model provider

2x first-week user activation rate

After launching the Claude-powered AI app generator

[Bubble](https://bubble.io/) is a no-code AI app development platform with more than six million users who've built more than seven million web and native mobile apps. Its Claude-powered AI agent builds in Bubble’s visual development language, so users can move between AI chat and visual editing to launch and scale applications.

## With Claude, Bubble:

- Doubled first-week activation rate and first-month retention after launching the Claude-powered AI app generator
- Increased user satisfaction with the AI editing agent by ~30% compared to the previous model provider, with positive feedback rates rising from ~70% to ~90%
- Adopted Claude Code across the majority of the engineering team, with all new hires now onboarded to it on day one
- Reduced inference costs while maintaining app generation quality
- Shipped backlog items previously not worth the effort, including a frontend migration from jQuery to SolidJS

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

## Closing the gap between first prompt and first app

Bubble has always believed that the best way for non-coders to build apps is to speak to a computer in their language, not in code. But before AI, visual development languages required a significant time investment to learn, and new users often churned before reaching the moment where things clicked.

"The \#1 business challenge we solved was showing value to users faster," said Zachary Tessler, AI Engineering Lead at Bubble. The team started with a page generator, then built a Claude-powered AI app generator that created full working apps from prompts. The results were immediate: first-week activation doubled, and twice as many users were still active at the end of their first month. But generating a complete app in one pass wasn't enough: users needed to iterate on what the generator produced, to move past prototypes into real products. That's why the team built the Bubble AI Agent, a Claude-powered assistant that helps users refine and extend their apps from within the editor.

## The solution

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Choosing the right Claude model


Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.


Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## Selecting Claude for reasoning quality 

Bubble's team evaluated multiple model providers before choosing Claude, prioritizing reasoning quality, low latency, and user control. "Reasoning quality is a top consideration," Tessler explained. "It helps a user decompose complex and potentially ambiguous requests into discrete actions that address their query." Latency mattered because the agent needed to keep pace with users building apps in real time. And the team wanted users to stay in the driver's seat, with the agent surfacing its plan and letting users approve changes before anything was applied.

The experience also needed to feel native. "Not a separate AI tool bolted on, but a natural extension of the way people already build on Bubble," Tessler noted.

After switching from their previous provider to Claude, Bubble built an internal evaluation suite to benchmark each model upgrade. When they moved to Sonnet 4.6, it matched the output quality of larger models at lower cost and faster response times. "The resulting apps still have all the sophistication and visual quality we were previously seeing, but with much faster responses," Tessler said.

## From chat window to working app

The Bubble AI Agent is a chat window inside the editor. Users type what they want, whether that's a question about how Bubble works or a request to add a feature to their app. On the backend, Bubble enriches each message with context about the user's app: its elements, data schemas, and logic. Claude also receives extensive instructions about Bubble's visual development language and a set of Bubble-specific tools for modifying apps.

The agent proposes changes, the user approves them, and the edits are applied. Users move fluidly between chatting with the agent and editing their app with Bubble's point-and-click tools. The agent can access broad editor functionality, from the built-in issue checker (similar in spirit to a type-checker on source code) to the full range of Bubble components and workflows, so it can generate complete user interfaces, data schemas, and executable logic, all visually editable afterward.

"Our agent is built in langchain and langgraph, so migrating from other models over to the Claude API itself was a minimal amount of work," Tessler added. The bigger investment was the evaluation suite: testing each model swap against quality, latency, and cost to make sure nothing regressed.

"It's less about things we couldn't do and more about things that weren't worth attempting before. The effort-to-reward ratio has shifted significantly."

Zoe Lapomme

Engineering Manager, Bubble


## The outcome

## Cleared backlogs and a growing builder ecosystem

After switching to Claude, user satisfaction with AI-driven edit requests increased by approximately 30%, with positive feedback rates climbing from roughly 70% to 90%. Latency improvements and better component and UI generation quality both contributed.

Internally, Claude Code has changed how Bubble's engineering team thinks about what's worth building. The majority of engineers use it, and all new hires are now onboarded to it on day one. "It's less about things we couldn't do and more about things that weren't worth attempting before," said Zoe Lapomme, Engineering Manager. "The effort-to-reward ratio has shifted significantly."

The Notes panel and style variables subtab in the Bubble editor, for instance, had been sitting on the backlog because the migration work wasn't justified. Using Claude Code to move the frontend from jQuery to SolidJS and implement new designs lowered the bar enough that the team actually shipped it. Onboarding has shifted too: bringing new engineers and contractors up to speed on an unfamiliar codebase is meaningfully faster. "Everyone's had Claude Code from the start, but it's hard to imagine doing it the old way now," Tessler said.

Beyond Bubble's own product, builders in the ecosystem are shipping Claude-powered apps through the platform: chatbots, content generation tools, document analysis workflows. Agency partners are building Claude-powered templates and plugins that other Bubble users can deploy, so the adoption compounds. Claude API integrations have trended upward over the past year, with Q1 2026 the strongest quarter to date.

Looking ahead, Bubble is integrating its app debugging tools with Claude so users can fix logic bugs directly, and adding multi-modal features like sharing app screenshots to iterate on generated UIs. "A Bubble user can connect to the Anthropic API, design a full conversational UI, and ship a Claude-powered product in hours rather than weeks," said Theo Goldberg, Partnerships Lead. "The compound effect across six million builders is what excites us most."

"A Bubble user can connect to the Anthropic API, design a full conversational UI, and ship a Claude-powered product in hours rather than weeks."

Theo Goldberg

Partnerships Lead, Bubble

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
