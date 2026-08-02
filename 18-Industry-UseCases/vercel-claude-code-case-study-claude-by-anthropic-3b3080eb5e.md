---
title: "Vercel Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/vercel-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:16Z"
tags: ["agents", "claude-code", "mcp", "skills"]
---

# How Vercel built an ecosystem on the open skills standard


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Large

Product:

Claude Enterprise

Claude Code

Location:

North America

~100 skills

power Vercel's internal data science agent

Some of skills.sh's most popular skills

are written by non-developers

How to create Skills

Follow our step-by-step guide to write custom skills that extend Claude's capabilities with real examples and practical patterns.

Read more

[Read more](https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples)

Read more

How to create Skills


Follow our step-by-step guide to write custom skills that extend Claude's capabilities with real examples and practical patterns.

Video caption


How to create Skills

Follow our step-by-step guide to write custom skills that extend Claude's capabilities with real examples and practical patterns.

[Prev](#)

Prev


[Vercel](https://vercel.com/) is a platform developers use to build and deploy web applications and agents. Its Chief of Software, Andrew Qu, built [skills.sh](http://skills.sh), a registry on top of Anthropic's open Skills spec, where developers discover and install agent skills. 

Andrew sat down with Anthropic to talk through how Vercel runs on skills internally, what surprised him about who's building them, and where the ecosystem is heading. 

## Anthropic: Vercel was one of the first companies to build a skill for Claude's directory. What made you want to move early, and what does the Deploy to Vercel skill actually do?

**Andrew Qu, Vercel:** Our Deploy to Vercel skill, which we shipped for Claude Code and Claude Desktop, is an easy way for people to go from clicking and prompting around to having a full production app deployed on Vercel. We've always wanted to shorten the time from idea to production. People are already doing most of their creative process in Claude, so it makes sense to meet them where they are and let them deploy directly from Claude to Vercel.

With any deployment provider before the skill, people went from idea to prototype/design very quickly, but then ended up spending a lot of time downloading a zip, signing up for a new account, and figuring out how to deploy.

With the skill, you can go from having your work in Claude to saying "I want this on the web" and instantly get back a shareable link. You can claim it into your own Vercel account later, or discover that Vercel is the hosting provider underneath and sign up to do more.

## Do you remember the first skill you built, and what you started with?

**Qu:** One of our web engineers decided one night to write down everything he knows about performance and making things feel fast. By the end he had a whole "web bible," and we were trying to figure out the right form factor to distribute it. Publishing it as docs on our blog felt too slow. An MCP server felt too heavy for what was basically documentation. Skills had come out only a couple of months earlier, so I helped rebundled the contents as a skill with nested directories. We announced it as a React best practices skill, and it was clear from the millions of impressions that the community was looking for skills to uplevel their agents. People wanted the best practices in a portable, quick format. I didn't create skills inside Claude itself. Anthropic published Skills as a spec, and skills.sh is the part I built on top: a place to discover skills and pull a local copy into your own codebase.

## Once you started building skills internally, what changed on your own team?

**Qu:** A lot of our focus on how to work faster, how to make agents perform better, and how to get people up to speed sooner started to center on skills. How do you do this migration? How do you debug this on-call issue? How do you match the design system? All of that became skills we built internally, checked into mini repos dedicated to internal agent skills. Anecdotally, it makes us move a lot faster.

A good example is a data science agent I maintain, named d0. I went through all the phases, sub agents, file systems, and the version we serve today runs on roughly 100 skills: aggregation, customer metrics, product metrics, time series data. Every scenario it handles is now encoded as a skill, because once we've done something accurately we can capture it and turn it into something the agent can recall later. Skills have changed how we work with agents at Vercel.

"Skills have changed how we work with agents at Vercel."

Andrew Qu

Chief of Software, Vercel

## With around 100 skills behind one agent, how does it know which skill to use when?

**Qu:** That's an ongoing thing we're figuring out. We haven't hit a ceiling where there are so many skills that the agent reaches for the wrong one. Being very descriptive with the title and the description matters a lot. We'll literally name a skill something like "aggregating product metrics month over month." So when someone in our Slack channel asks the data science agent for total user growth over the past month, that usually gets mapped to the right skill. We've found that Opus, specifically Opus 4.8, is very good at matching intent to skills. We honestly haven't reached a point where skills collide and we have to remove one, though I'm sure we'll get there eventually.

## For a team that wants to start building this way, where should they begin?

**Qu:** Figure out something you do a lot. When you open up Claude Code and you're about to implement a new feature or run some analysis, ask yourself whether you've done something similar before. In front-end design, say you're building a new page that needs authentication behind it and a header from somewhere else. It's like a loose template, because it's been done in a few places and you have to string the pieces together. That can become a skill: what to lay out, what to reuse, what to reference, how data fetching works, all embedded as a skill for how your codebase works.

The lower-lift option is to go to something like skills.sh and find skills relevant to your stack. There are good skills out there for the libraries and technologies people use, including Anthropic's official front-end design skill.

## Some people describe skills as a kind of package manager for AI coding assistants. How do you see them fitting alongside things like MCP and memory?

**Qu:** I don't think any of these are replacements for each other. For us, we ship a Vercel plugin for Claude Code that combines the Vercel MCP with skills for our libraries and platform, plus sub agents built in. They all ladder up into providing more context for coding agents so people can work faster with the tools they already know.

Skills are great right now. Honestly, we hope a lot of them eventually become obsolete. Today a React best practices skill talks about using useEffect correctly, or to refactor a component to prevent waterfalls so it's quicker. In the future those won't need to be in a skill at all, because they'll be baked into the model's preferences, and the skills we write will get more complex. The current ones are almost primitives that we'll compose into fuller experiences. It's like going from JavaScript and jQuery to React to Next.js: things get more advanced, and you stop having to worry about the layers underneath.

## How would having skills as an open standard change how people build? 

**Qu:** I like that it's open, that anyone can contribute, and that the best ideas win. About a month after we launched skills.sh, someone at Cloudflare published a spec for URL-based discovery of skills, so you could find them at something like a /.well-known/skills path on a domain. I thought it was a great idea, and because I maintain a popular installer, npx skills, I was able to implement it right away. In parallel, I watched it move up the official spec progression. When things are open and people can submit ideas, rather than everything being closed to a single-threaded roadmap, you get new and more ergonomic ways of doing things. If that person hadn't been able to share the idea and I hadn't seen it, we'd never have had that pattern for web discovery of skills.

Improving frontend design through Skills

Build richer, more customized frontend interfaces with Claude. Learn how Skills unlock better typography, animations, and design quality.

Read more

[Read more](https://claude.com/blog/improving-frontend-design-through-skills)

Read more

Improving frontend design through Skills


Build richer, more customized frontend interfaces with Claude. Learn how Skills unlock better typography, animations, and design quality.

Video caption


Improving frontend design through Skills

Build richer, more customized frontend interfaces with Claude. Learn how Skills unlock better typography, animations, and design quality.

"Skills have opened up the door for non-technical people with a background in a specific field to contribute to the AI ecosystem."

Andrew Qu

Chief of Software, Vercel

## What's surprised you most about what people are building with skills?

**Qu:** The most surprising thing, and I think it's amazing, is that some of the most popular skills are actually written by non-developers. Skills have opened up the door for non-technical people with a background in a specific field to contribute to the AI ecosystem. Some of my favorite skills come from a marketer who had never written a line of code until he got his hands on Claude Code, and then wrote a skill covering everything he knows about marketing: SEO, audits, backlinks, when to look for what. He has a couple of skills in the top 100 on skills.sh, and he's one of the few authors who isn't a developer-tools or framework person. I've seen legal skills, marketing skills, sales skills. Anything that's a process someone wants to embed into an agent, I've seen people make a skill for. Those are some of the best, most novel use cases, especially as coding agents get so good at coding that they need to get better at other things too.

## As LLMs start authoring and improving skills themselves, does that change what a registry like skills.sh is for?

**Qu:** I don't think so. It's actually in line with how I designed skills.sh from day one. I always imagined skills as a kind of mutable knowledge. Every time you install a skill from skills.sh, you get a local copy, and I've watched people edit it to fit their codebase. Take Anthropic's front-end design skill. People pull the original into their own repo and modify it for the libraries they use. The skill talks about composing CSS classes, but some people prefer Tailwind, so they remove that part and replace it with how they compose classes in Tailwind. It becomes a personalized skill built on the best practices from the original version. That's how we designed skills.sh from the start: you download knowledge that's good by default, and over time it evolves to fit your needs better than the defaults would.

## Where do you see this heading? Are teams starting to build whole agents out of skills?

**Qu:** Internally, yes, though it still feels new. We're releasing a framework for building agents, based on everything we've learned building agents at Vercel and shipping these experiences ourselves. It’s called [eve](http://eve.dev), and  one of the core pieces is skills. There are really four things that make up an agent: tools, the initial system instructions, skills, and channels, which are the interfaces for communicating with the agent. Skills are probably the biggest thing people customize. The system prompt will be dense, but the way people actually iterate, we think, is by adding and removing skills. A lot of what we're doing is skill-based, building more markdown and resource-heavy agents. I don't think it's a big industry-wide thing yet, but I think it will be.


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

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)

A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)

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
