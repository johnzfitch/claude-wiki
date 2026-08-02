---
title: "PwC Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/pwc-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:47Z"
tags: ["claude-code"]
---

# How PwC trained 400 consultants on Claude Code in a single session


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Professional services

Company size:

Large

Product:

Claude Code

Claude Enterprise

Location:

North America

6 weeks → 2.5 days

Legacy code analysis compressed

30,000-person training rollout

underway across PwC

Legacy code analysis compressed

Read more

[Read more](#)

Read more


Legacy code analysis compressed

Video caption


6 weeks → 2.5 days

Legacy code analysis compressed

[Prev](#)

Prev


[Pricewaterhouse Coopers](https://www.pwc.com/us/en.html), or PwC, is a global professional services firm offering audit, tax, and consulting services to businesses and organizations worldwide. PwC and Anthropic [recently announced an expanded alliance](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html), driving impact across client work and the firm. Partner Ussama Baggili leads legacy and mainframe modernization at PwC, where he built systemized Claude Code workflows that have spread to a firm-wide training initiative. We spoke with Baggili about why PwC puts business users on Claude Code from day one and how a single training session got 400 leaders and consultants building apps in under an hour, and what that means for the firm.

## Anthropic: You've been one of the more active Claude Code users inside PwC. What were you trying to solve when you started?

**Ussama Baggili, PwC:** Everybody's trying to figure out how to get ahead with AI, but not everybody is able to use AI effectively. Claude is giving us the ability to re-energize the AI mindset in our people. It's a lot more relatable. People feel that they're getting to results faster that are both higher fidelity and also more in tune with where they're going.

We have these blind spots in our organization that we weren't able to connect. Claude Code is how we started connecting those.

What we're trying to do is get people thinking differently by treating Claude as a capable colleague. We started with coding, which is the obvious entry point. But I discovered that a lot of what Claude Code is really good at is analysis: working through the problem before you even get to the coding part. The early realization was that the analysis itself was the deliverable. You could take it and then make it polished. And once I saw that, it changed how I thought about who should be using it.

## What do you mean by that? There's a common assumption that Claude Code is for developers and that non-technical users should start somewhere simpler.

**Baggili:** People say, "Maybe we’ll start with chat and then graduate to Claude Code. It’s too complicated for people to want to use it right away" But I think that's very limited. I think starting with Claude Code at the beginning is actually a more optimal and natural segway for continued progress into more technical realms. When we were first planning our internal training, the thought was that it’s best to use the Claude  chat version. However, believing in choice and not assuming we know best how the Claude products set will be used, we decided to run the training in Claude Code CLI within VS Code to start building muscle memory on more technical usage from which point the trainees can decide which one they preferred for their regular usage. 

## That's a bold bet with a non-technical audience. How did you set that up to succeed?

**Baggili:** Installing Claude Code can be complex if there are restrictions on package installations. We managed to get it down to a single-line script that people could run to get everything installed. 

Then the question become, how do we get 400 people to pace through a real training in about an hour and walk out energized? If things go wrong on the install, if they stumble on their prompting, they may not feel the benefit of using Claude Code.

So I thought, couldn't we build a skill or plugin within the training itself that helps people pace forward as they type their prompts? Think of it as a coach plugin within Claude Code. It tells people: great, here's what we're going to take you through in this training and helps set the training structure.  

Then, the second most notable thing is to coach on how to work with Claude with the outcome in mind first, and then working backwards from there. The Claude Code coach plugin is wired into a project distribution that has a [CLAUDE.md](http://claude.md) that points to a coaching workflow for Claude. It is triggered upon session start and is visible to the user upon first interaction. It walks them through the steps to ‘here's your first prompt.’

## What did the training actually walk people through?

**Baggili:** It simulates a day in the life of three key tasks we do often. One, we respond to proposals. Two, we produce functional and technical specs for the things we're going to build. And three, we build applications or mobile applications. 

The coach plugin walks them through their first prompt. And within 15 to 20 minutes, people had their initial draft RFP responses ready for their review. Within another 15 to 20 minutes, they had their functional and technical draft specs. By the time we finished the hour, people were posting screenshots of the mobile apps they had built with Claude Code in the team chat.

Regardless of whether it was perfect, people walked out positive and optimistic about Claude Code and why they needed it.

"Claude is giving us the ability to re-energize the AI mindset in our people."

Ussama Baggili

Partner, PwC

## What was the reaction after the session?

**Baggili:** People were already planning what to do next. We did a round of Q&A at the end, and people said things like: ‘Monday, this is what we're doing.’ Or, ‘Tonight I'm going to talk to my teams. I need everybody on this.’ 

My thinking was: how do I get this to be enticing enough for people to be yearning for it, so that they could do more with it *immediately*? Not tomorrow, not next week. We had already taken down the barriers to installation, dealt with the security hurdles, and made it as frictionless as possible.

## You mentioned that the shift from coding to analysis was a turning point for you. What does that look like in your day-to-day practice?

**Baggili:** Once I started producing decks and HTML deliverables with Claude Code, clients gravitated toward them. They were no longer shelfware. Clients could click through them quickly. So what started as 100% coding work shifted toward a non-coding output that was actually more valuable for our clients.

## Can you walk through a specific example?

**Baggili:** I lead our legacy and mainframe modernization practice. We often get these projects last minute where a client says, "We run AS400," or they have an ERP system for supply chain, or a healthcare TPA system. Systems that don’t have documentation or code that nobody can read anymore because the people who wrote it are retired.

With Claude Code, if they give us access to their code, we know how to run the analysis and give you a point of view very quickly in a package that's deliverable-worthy. We can show them previous examples and say, "Don't worry, you don't have to spend a fortune to get there. We'll help you see what you need to know." You're going to have documentation now.

The crazy part is what used to be six weeks' worth of engagements is now about two and a half days of doing that. The typical discovery process required significant effort towards collecting, manually reviewing documentation, interviewing stakeholders, reviewing findings, iterating over interim-deliverables and shaping the recommendation.  With Claude Claude, the majority of these activities can be performed by the agent. That’s made us very credible with clients.

## Anthropic: Where did you take it from there?

**Baggili:** That’s when I started to see other use cases. If it can do this, can it also produce all this daunting work that we don't care to do? We started systemizing our proposals and offerings with Claude skills and Claude plugins. By packaging them into a systemized way of working, we built what's essentially an executive assistant in Claude Code. If you give me any question, I give it to my executive assistant and it spits out a deck with our branding, diagrams, workflows, and content—in minutes. We also started providing it to our leaders so they could use it across the organization.

## Anthropic: What's next?

**Baggili:** Now the idea is becoming global and the question is: how do we keep this going? How do we take this across all of our offerings for our 400,000 people and repeat the success we are witnessing in the US?

training rollout underway across PwC

Read more

[Read more](#)

Read more


training rollout underway across PwC

Video caption


30,000-person

training rollout underway across PwC

"What used to be six weeks' worth of analysis is now about two and a half days."

Ussama Baggili

Partner, PwC


Video caption


[Prev](#)

Prev


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
