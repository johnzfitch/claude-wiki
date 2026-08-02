---
title: "Notion Q&amp;A | Claude Managed Agents | Claude by Anthropic"
source_url: "https://www.claude.com/customers/notion-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:43Z"
tags: ["agents", "skills"]
---

# How Notion is building a workspace where teams and agents collaborate


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


[Play video](#)

Play video

Industry:

Software

Company size:

Large

Product:

Claude Managed Agents

Location:

North America

30+ concurrent agent tasks

from a single task board

Self-improving skills database

maintained by Claude after every completed task

Case Study: Notion

Learn how Notion uses Claude to power enterprise AI search, reduce costs by 90% with prompt caching, and build agent workflows.

Read more

[Read more](http://claude.com/customers/notion)

Read more

Case Study: Notion


Learn how Notion uses Claude to power enterprise AI search, reduce costs by 90% with prompt caching, and build agent workflows.

Video caption


Case Study: Notion

Learn how Notion uses Claude to power enterprise AI search, reduce costs by 90% with prompt caching, and build agent workflows.

[Prev](#)

Prev


Notion is a collaborative AI workspace where teams and agents work together. With the launch of [Claude Managed Agents](https://claude.com/blog/claude-managed-agents), a suite of composable APIs for building and deploying agents at scale, Notion product manager Eric Liu and his team have been building agent orchestration that lets Notion users delegate real work to coding and knowledge work agents from their task boards. He spoke with Anthropic about what's hard about deploying agents across an organization and what surprised him when he started using it himself. 

## Most agent tools today are designed for a single person working with a single agent. What breaks when organizations try to scale that?

**Eric Liu, Notion:** The challenge of deploying agents at scale is really about collaboration. Right now, agents feel very one-to-one. It's you and an agent in an interface. But what does it look like for your whole team, with all of the approval processes and everything required to actually use agents at scale? That's fundamentally the same problem we've solved before at Notion, which is human collaboration. Now it's agent and human collaboration, and it turns out a lot of the same patterns around suggested edits, version history, and shared knowledge bases are really critical. Agents are doing so much of the work now that people are spending more of their time as editors and reviewers.

## Why did you decide to add Managed Agents into Notion? 

**Liu:** Our customers don't want to use one agent to talk to another agent to do a backflip to get things connected. They just want to be in Notion and say, "Claude, help me make this website." Managed Agents was great because we just pull in the API and it works within the product. 

Our agent is good at using Notion, but it's not the best at coding, and Claude models are very good at that. We also don't generate the long tail of artifacts. We focus on what's native to Notion: your company knowledge. But there's a whole world of other files that Claude is really good at generating.

## Walk us through what you built.

**Liu:** The way I think about it is that you’re creating these software building blocks in Notion and you can construct them into any workflow you want. For example, we created a task board that acts as an orchestrator. You create a task, move it to "ready to start," and it invokes a Claude session. You can mention the task, and it exists in all the surfaces you're collaborating with your team on. Claude picks up context from connected pages, our design system, API docs, and product requirements documents. In other words, you're working with Claude just like a colleague.

The nice thing is that you're not limited to one task. For our customers, what that means is that they can kick off a ton of jobs in Notion, 30 or 40 at the same time, and our platform routes them to the right person for approvals. That's what makes doing it in Notion so valuable. 

“You're working with Claude just like a colleague.”

Eric Liu

Product Manager, Notion

## How is Managed Agents integrated into Notion’s Custom Agents? 

**Liu:** Having an infrastructure layer that can do long-running tasks is really essential. You might need to run a coding agent for 20 minutes, an hour, or for a really long time. That ability to continue to run it, to manage memory, to have high quality outputs over time is a layer that's super critical on top of the model itself. The Managed Agents product is like a playground for me. Even with the early prototype, we saw 12 hours of prototyping work collapse into about 20 minutes. Then your whole team can jump in and refine it together. 

Underneath, all agents are basically coding agents. And that's unlocking a lot of non-coding use cases. If you're creating a presentation for marketing or sales, you're taking knowledge and generating an artifact, whether that's a PDF, slides, or something else. That synthesis of information into an artifact is roughly the same workflow that works really well in coding. We're seeing that transition into the rest of knowledge work. 

## What’s the experience like for users?

**Liu:** Working with agents in a place that people are already familiar with can be a huge unlock. People now see Claude show up in their Notion task doing work, and they give a thumbs up or thumbs down. That's an interface they already understand. 

When I was prototyping new features for Notion using the task board workflow I mentioned, I had about 30 tasks. I took all of them and just dragged them to start. I went and got a snack, came back, and all the prototypes were made. Then I tagged in somebody on my team, and we jammed on the same output together right in Notion. We've turned AI solo work into a collaborative moment.

That was the point where I was like, everybody should be doing this. It's something that feels very foreign right now, where it's usually just you and an agent. This is everybody building something together.

## One of the more interesting things you've built is a skills database that updates itself. How does that work?

**Liu:** Once there's a merged pull request or a completed task, Claude identifies the lessons the agent can learn and feeds them back into the skills as updates. A lot of these skills are basically auto-maintained. Every time you say "this is a great prototype" or "this is a great PDF," that feeds into the skills. The quality keeps improving without someone manually updating the knowledge base.

## How do you think Notion changes over the next six months or so as a result of this?

**Liu:** It will have a lot more agents. The interface we built for Notion has really been about humans doing the tasks. But the interface is becoming more about human beings reviewing the work of agents. Approval flows, suggested edits, all those things that humans already understand, we are the translation layer to agents. We'll keep the same primitives around the page and the database, but we're going to build a lot more around version control, human in the loop, and reviews. 

I think the question becomes: how can humans become the reviewers of agentic work rather than directly the doers? I think that paradigm applies to a lot of AI.

Claude Managed Agents: Get to production 10x faster

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

Read more

[Read more](https://claude.com/blog/claude-managed-agents)

Read more

Claude Managed Agents: Get to production 10x faster


We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

Video caption


Claude Managed Agents: Get to production 10x faster

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

“We saw 12 hours of prototyping work collapse into about 20 minutes. Then your whole team can jump in and refine it together.”

Eric Liu

Product Manager, Notion


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
