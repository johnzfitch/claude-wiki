---
title: "OpusClip Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/opusclip"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:44Z"
tags: ["claude-code", "cli"]
---

# OpusClip builds its GTM engine with Claude Code


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Startup

Product:

Claude Code

Claude Platform

Location:

North America

100% automated sales call review coverage

up from 5–10% manual review

\$200K+ in new pipeline

surfaced from a single customer insight

[OpusClip](https://www.opus.pro/) is an AI video clipping platform used by more than 16 million creators and media companies to turn long-form content into short-form social video. Six months ago, no one on OpusClip's B2B revenue team had written production code. Today, using Claude Code, the ten-person team builds and maintains its own call intelligence, renewal automation, and customer dashboards.

## With Claude Code, OpusClip:

- Increased sales call review coverage from 5–10% manual to 100% automated, with structured coaching briefs generated for every conversation
- Surfaced \$200K+ in new pipeline after identifying a customer support routing issue from a single call transcript that had gone undetected
- Built an ROI calculator in 60 minutes after weeks of failed internal attempts, unblocking 5 enterprise deals in the first month
- Delivered a customer dashboard prototype in one week with real data, buying the engineering team time to build the production version
- Reduced renewal brief preparation from hours to minutes per account, now fully automated and visible in HubSpot

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

## Sellers stretched thin, context scattered everywhere

OpusClip's B2B team was growing fast and running into familiar pain. Franz-Josef Schrepf, Head of Enterprise Revenue and Partnerships, managed six sales and customer success reps but had visibility into only a fraction of their work. "I could sit in on maybe two or three calls per week," Schrepf said. "The rest was invisible unless someone wrote up call notes, which were unreliable and often missed the most important details."

With so few calls observed, the vast majority of rep performance went unreviewed. Renewal prep meant hours of manual work per account: screenshotting dashboards, downloading contracts, pulling transcripts, copying notes. Context was scattered across five or six tools. Patterns predicting churn existed in the sales data, but no one had the bandwidth to quantify them.

By September 2025, Schrepf had spec'd out a GTM software stack to address these gaps: revenue intelligence, sales engagement, data enrichment, signal providers, CRM middleware. Combined, the tools would have cost six figures and taken months to roll out, with significant overlap between vendors. In October, Schrepf started experimenting with Claude Code.

## The solution

Introducing Agent Skills

Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.

Read more

[Read more](https://claude.com/blog/skills)

Read more

Introducing Agent Skills


Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.


Introducing Agent Skills

Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.

## Selecting Claude Code for GTM engineering

OpusClip's engineering team was already using Claude Code, but no one had brought it to the GTM side of the business. When Schrepf saw what was possible, the software procurement conversation shifted. “Claude Code made more sense for us than buying more software,” said Blake Umlauf, GTM Engineer. “For a small team like ours, it lets us move quickly and build lightweight tools, creating workflows that fit the way we work."

For Umlauf, what made Claude Code work as a building tool was how it handled existing code. "It actually read my existing scripts before writing new ones," he said. “It behaved like a teammate who'd read the repo, not a stranger pasting snippets."

What tipped the decision was what happened when the team started feeding call transcripts into Claude Code. It surfaced a conversation where the customer had tried to upgrade their plan six times in two weeks but kept getting routed incorrectly by OpusClip's support chatbot. The customer signed a \$20K annual plan that same day, and once the routing issue was fixed, the channel generated more than \$200K in additional pipeline.

## From call transcripts to cross-functional intelligence

The core workflow is call intelligence. The weekly revenue report runs as a two-step process. First, a custom Zoom MCP server the team built with Claude Code pulls all external call transcripts automatically. Claude Code spawns parallel subagents that distill each call into a structured summary. A second session gathers those summaries along with data from HubSpot, Linear, and internal call transcripts, then writes an eight-section executive brief with coaching briefs per rep and sections tailored for product, marketing, and GTM. The whole process takes about 15 minutes. 

The move from Claude Opus 4.5 to 4.6 made a practical difference: the larger context window means the team can feed in multiple call transcripts and data exports in a single session. MCP servers connect Claude Code to HubSpot, Mixpanel, Zoom, Linear, Clay, and n8n. 

Now, feature requests surface with exact customer quotes and deal sizes attached, automatically mapped to Linear tickets. Competitive intelligence reaches product marketing from calls they were never on. The BDR team gets ICP patterns distilled from conversations they didn’t have.

“Claude will feed back the top 10 decisions I need to make this week, flag topics for my 1-on-1s with team members, and surface cross-functional updates,” Schrepf said. "Suddenly the dots between sales, product, marketing, and CS connected themselves."

The team also used Claude Code to build an ROI calculator for live sales calls. Schrepf fed the transcripts from internal meetings to Claude Code and asked it to design the calculator. Within 60 minutes, it produced a spreadsheet calculator the sales team now uses daily, detailed enough to build a business case but simple enough for customers to experiment with. It unblocked five deals in the first month.

Every workflow follows the same methodology. Each new use case starts with unstructured data: screenshots, CSVs, text files dragged into Claude Code. Once the output is validated, the process is turned into a Claude Code skill and uploaded to a shared GitHub repo. The skill includes the instructions, so it teaches the process as it runs it. When someone runs /renewal-analysis, Claude Code shows a checklist: upload the contract PDF, admin dashboard screenshot, user export CSV. Minutes later, the team has a structured renewal brief with a health scorecard, risk assessment, pricing options, and call prep scripts. No separate training doc needed.

"Claude Code behaved like a teammate who'd read the repo, not a stranger pasting snippets."

Blake Umlauf

GTM Engineer, OpusClip


## The outcome

## Revenue leaders writing production workflows

The tools the GTM team built weren't handed down from engineering. "I'm a revenue leader, not an engineer," Schrepf said. "I've never written production code. But after a few weeks with Claude Code, I was building workflows that my team uses daily."

The shift extended across the team. Umlauf went from BDR to GTM Engineer and is now the most engaged person on the team. Revenue Operations manager Patrick Donnelly automated manual renewal prep and now focuses on customer health scoring and pipeline automation. The shared GitHub repo of skills now doubles as onboarding. New team members clone it on day one and immediately have access to /renewal-analysis, /morning-brief, /call-coaching, and every workflow the team has built. The tool teaches the process as it runs it.

## What’s next 

OpusClip's next step is moving from on-demand workflows to proactive ones: agents that flag risks and surface insights continuously, rather than waiting for a slash command or a scheduled report. The team is actively building toward three use cases: an agent that triages inbound campaign replies by classifying intent and drafting responses in each AE’s voice; a pre-call research agent that listens for new calendar events and drops a brief into the meeting 12 hours before it happens; and a CSM account-health watcher that monitors usage, support, and CRM data continuously and surfaces churn risk or expansion opportunity before either side has asked. "We've already validated the workflows," Schrepf said. "Now we want them running continuously."

“Claude will feed back the top 10 decisions I need to make this week. Suddenly the dots between sales, product, marketing, and CS connected themselves."

Franz-Josef Schrepf

Head of Enterprise Revenue and Partnerships, OpusClip

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
