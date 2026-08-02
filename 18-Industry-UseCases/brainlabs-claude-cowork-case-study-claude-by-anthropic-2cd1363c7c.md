---
title: "Brainlabs Claude Cowork case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/brainlabs"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:41:42Z"
tags: ["agents", "skills"]
---

# How Brainlabs gave 1k+ marketers at its media agency an AI coworker with Claude Cowork and skills


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Professional services

Company size:

Large

Product:

Claude Cowork

Claude Enterprise

Location:

North America

~400 Skills

authored by employees in four weeks

91% adoption rate

in North America

[Brainlabs](https://www.brainlabsdigital.com/) is a media agency with offices across the US, UK, LATAM, and APAC, running media and advertising campaigns for mid-sized and enterprise clients across industries. Over four weeks, the company rolled out Claude Cowork to its full workforce, with employees authoring hundreds of their own skills and automations.

## With Claude, Brainlabs built:

- A library of roughly 400 skills authored by employees in four weeks
- A Cowork deployment reaching about 1,000 employees across the agency
- A Notion-based repository of Cowork skills that non-developers can use directly 
- A Claude-powered "skills auditor" that reviews skills to find more efficiencies and consolidate the growing library
- A Managed Agents setup inside Notion that triggers Claude when work changes state
- A "suggest a skill" process so any employee can propose a new automation

## The challenge

How to create Skills

Follow our step-by-step guide to write custom skills that extend Claude's capabilities with real examples and practical patterns.

Read more

[Read more](https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples)

Read more

How to create Skills


Follow our step-by-step guide to write custom skills that extend Claude's capabilities with real examples and practical patterns.


How to create Skills

Follow our step-by-step guide to write custom skills that extend Claude's capabilities with real examples and practical patterns.

## Scaling repeatable work across a large agency

An agency at Brainlabs's size produces a steady cadence of campaign work with dozens of recurring workflows. The company's roughly 1,000 strategists, media planners, data scientists, and creative leads spend significant chunks of their day on repeatable work: drafting creative briefs, QA-ing media plans, pulling client reporting, summarizing campaign data. Across that many people, every team rebuilding the same things by hand starts to add up fast.

For Brainlabs's CTO Ben Vincent, the principle was simple. "If you're doing something more than three times, you should try to automate it," Vincent said. The company's CEO Dan Gilbert wanted that principle applied across the whole business, not just the engineering org. The original target was to have Claude live across the entire workforce in a week.  

## The solution

Skills explained

Where do Skills fit in the Claude stack alongside prompts, Projects, MCP, and subagents? Learn what tool to use when—and how they work together.

Read more

[Read more](https://claude.com/blog/skills-explained)

Read more

Skills explained


Where do Skills fit in the Claude stack alongside prompts, Projects, MCP, and subagents? Learn what tool to use when—and how they work together.


Skills explained

Where do Skills fit in the Claude stack alongside prompts, Projects, MCP, and subagents? Learn what tool to use when—and how they work together.

## An authoring layer for skills

Brainlabs treated Cowork as the foundation, and skills as the layer on top. Over four weeks, Cowork went live across the workforce, with workshops to walk strategists, planners, and creative leads through how Claude could plug into the tools they were already using.

For skills, Brainlabs needed an authoring layer the same audience could actually use. The company made Notion the home for its org-wide skills library: employees store skills directly inside Notion, where the company’s knowledge base, meeting notes, and team workflows already sit. Notion packages each Skill and pushes it to GitHub for revision, while the Notion page stays as the source of truth.

"We've made all of them open,” Vincent said. “Anyone in the company can go in and read the details of any skill.” A "suggest a skill" process gave any employee a way to propose a new automation without going through engineering, and an org-wide skills guideline set the bar for quality. The rollout to get Claude live across the whole company took four weeks, during which time roughly 400 skills landed in the library.

The library spans the agency’s full range of work. Two examples Brainlabs has invested in heavily: an SEO audit skill, refined across thousands of iterations from the SEO team and built on a context layer drawn from over a decade of agency work; and a brand skill that produces presentation decks, social graphics, and one-pagers that stay on-brand without a designer in the loop. The audit skills alone number in the dozens, each with its own context layer.

Keeping the quality bar high as the library grew into the hundreds required a second piece, and Brainlabs built it as a skill itself: an auditor that reviews every other skill for duplication, overlapping instructions, and token inefficiency, then proposes consolidations and rewrites. “The skills auditor checks: have you done this in a clean way, is it concise?” Vincent explained. “We built it after versions 2, 3, and 4 of the library got unwieldy from over-enthusiastic agent creation across the company.” The team is also using the analytics API to see which skills are actually getting used inside chains of thought, so the library can grow on the basis of evidence rather than enthusiasm.

Security and governance were handled the same way, cautiously, and in stages. Data stays isolated by design: a Skill only pulls what the person running it is already authorized to access. Every skill also has a designated owner who reviews and approves changes before it goes live, so quality and access controls keep pace as the library grows.  
  
The newest addition sits on top of all of this. Brainlabs is one of the early customers running Managed Agents inside Notion. "We use actions. We get them to look at the Notion boards, and when something is happening it fires off to Claude," Vincent said. One example is a task agent called Get Stuff Done that works tickets on a Kanban-style board: a Notion agent tags a task with “Claude” when it judges the work complex enough, and the managed agent picks it up from there, drawing on the company’s skills library and connectors to Slack, Google Calendar, and other platforms to produce outputs like PowerPoints and research documents. 

The team has put the agent to work on its own projects, including managing the Cowork rollout itself. The team is also evaluating the Claude Agent SDK for more complex server-side agents that would sit alongside the Notion-hosted ones.

"If you're doing something more than three times, you should try to automate it."

Ben Vincent

CTO, Brainlabs


## The outcome

## ~400 skills in four weeks, with agents on top

Four weeks after the rollout began, Brainlabs employees had authored roughly 400 skills covering everything from presentation-building to client reporting, with the library still growing as more people determined which parts of their own work fit the "more than three times" rule. Cowork sits underneath all of it, with about 1,000 employees handing off recurring tasks inside the tools they already use and picking up finished work on the other side. "We're automating all the mundane tasks so employees can do the more strategic things," Vincent added.

For Dan Gilbert, Brainlabs’s Global CEO, the biggest gains have been in the depth and consistency of the work itself. SEO audits used to vary in quality depending on which strategist ran them. The SEO audit skill changed that. “It’s one skill, refined across thousands of iterations from our SEO team, that captures the full universe of what to look for and what good looks like,” Gilbert said. “It doesn’t rely on what any one strategist happens to remember on the day.” Client reporting saw the same shift. “The strategists in the loop spend their hours on judgement, prioritization, and client strategy instead of mechanical assembly,” Gilbert added. For clients, this lands as a different service, not a faster one, with real-time coverage and expanded capability that wasn't possible before.

Writing tasks see the same lift agency-wide, which matters because writing is a daily part of almost everyone’s job at Brainlabs. Cowork is preloaded with the company’s style guide and each person’s individual writing style, so drafts come out around 80% of the way there in Brainlabs’s voice rather than starting from a blank page. “That’s a real quality lift, especially for people whose core job isn’t writing,” Gilbert said.

Vincent uses Cowork as his own ideation tool. “I have a bunch of random ideas that I never have the time to explore,” Vincent explained. “Now I can write the idea down in Cowork, and Claude will go investigate, build me a document, and I have all the information I need.” With Managed Agents now firing inside Notion when work changes state, Brainlabs is seeing what proactive, not just reactive, automation looks like inside a working agency.

For Vincent, this is the foundation, not the finish line. "I think it's going to go so far beyond where we are now," Vincent said. "We're going to have a bunch of agents hosted in a variety of places, which will expand our team's capabilities for the deep strategic work that grows our clients' businesses.”

“Now I can write the idea down in Cowork, and Claude will go investigate, build me a document, and I have all the information I need.”

Ben Vincent

CTO, Brainlabs

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

[LG CNS modernizes 20-year-old enterprise systems with Claude](/customers/lg-cns)

LG CNS modernizes 20-year-old enterprise systems with Claude

LG CNS modernizes 20-year-old enterprise systems with Claude

Customer story

[Customer story](/customers/lg-cns)

Customer story

[How Blank Metal, a lean professional services firm, runs on Claude Cowork](/customers/blank-metal-qa)

How Blank Metal, a lean professional services firm, runs on Claude Cowork

How Blank Metal, a lean professional services firm, runs on Claude Cowork

Customer story

[Customer story](/customers/blank-metal-qa)

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
