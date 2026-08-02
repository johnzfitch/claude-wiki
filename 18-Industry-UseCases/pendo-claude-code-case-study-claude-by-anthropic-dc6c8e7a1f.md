---
title: "Pendo Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/pendo-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:43:37Z"
tags: ["agents", "claude-code"]
---

# Pendo closes the gap between shipping fast and shipping well with Claude Managed Agents


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Medium

Product:

Claude Managed Agents

Claude Code

Location:

North America

90% success rate

On PM-reviewed evaluation sets for Claude-powered agent tasks

3 months to build an AI-native product

processing billions of data points using Claude Managed Agents and Claude Code

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

[Prev](#)

Prev


[Pendo](https://www.pendo.io/) provides product analytics and AI tools that help companies understand user behavior and act on it to drive product adoption. Over the past few months, the company has been building Novus, a product that detects and fixes usability issues in customer applications. The system runs on Claude Managed Agents. We spoke with Zain Lakhani, Pendo's Chief AI Officer, about how Managed Agents powers their AI-native product. 

## What is Pendo building with Claude?

**Zain Lakhani, Pendo:** Our users used to be product managers looking at dashboards. Now they're product engineers shipping code. That changed everything about what we needed to build. Most of what we're building now is around detecting what's going on inside your application, then cross-referencing that with your codebase to suggest fixes. A sample use case: we see a drop-off in a funnel, look at the code, and say, "This button is positioned below the fold. There's a lot of drop-off here. Here's a fix." The underpinnings of all that are deployed with Managed Agents.

## Tell me about Novus. What problem is it solving?

**Lakhani:** Product managers are becoming developers now. They're coding, they're shipping fast, and quite frankly, a lot of what's going out is difficult-to-use software that struggles to meet its adoption and retention goals. And it's not just PMs. Even developers using AI coding tools are shipping faster and doing so many multi-threaded tasks, four tickets at once, that a lot of code is hitting production without the user acceptance testing it would have received before. The velocity is there, but the feedback loop isn’t keeping up.

Novus is our answer to that. The idea is: you've shipped something, but you don't know what to ship next. You know something is broken, but you don't know what. Our approach isn't to slow anyone down. It’s: keep going fast and we'll fix it right after. Let's see how users are responding and try to optimize within minutes.

We're building this for what we call "product engineers." If we were building a tool from scratch for that persona, this is what it would look like.

## You tried building this before Managed Agents. What did that look like?

**Lakhani:** We learned pretty quickly that we're not a coding agent company. We don't want to be a coding agent company. The bulk of our intelligence, we want to offload onto a cloud agent and inject our own expertise: how do you instrument product analytics for a rapidly evolving product, what's the best way to use that data and what does good product usage look like. Then we lean on Claude's intelligence for the heavy lifting.

We spent about three months trying to get there on our own. We tried different homegrown solutions and it didn't work for us. Without Managed Agents, we were responsible for all the infrastructure around the agent itself. Session management, for example: sessions were stored on disc, and we had to locate them, retrieve them, upload them, and re-download them for every interaction. The shared memory layer required the same kind of manual work.

## How quickly did Managed Agents get you to production?

**Lakhani:** About three days. We'd been asking for the things Managed Agents provide. Session management, shared memory, sandboxing. Those were all gaps we had to fill ourselves before. Now every time we start a customer workflow, we spin up a Managed Agents session on the cloud. We don't route through our own infrastructure for the intelligence anymore. We go directly to Claude. We give it a copy of the customer's question, the intelligence insights, what we learned from past sessions, and we pair that with our Pendo data. Then it returns results.

Three days versus months of trying to build it ourselves.

"We don't route through our own infrastructure for the intelligence anymore. We go directly to Claude."

Zain Lakhani

Chief AI Officer, Pendo

## Walk me through how Novus works when it finds an issue.

**Lakhani:** A user links their codebase on GitHub and installs a Novus snippet that detects clicks and records session replays. Novus surfaces insights continuously. It might say, "We noticed a drop in this funnel from checkout to order confirmation. There are a bunch of flags. Here's a PR." That pull request is generated by Managed Agents.

Behind the scenes, every time the agent runs on top of a customer's codebase, we give it MCP tools to talk to the underlying Novus data. So if it's looking at the checkout page, it also knows that page gets a thousand clicks a day but the funnel conversion to order confirmation is only 3%. It looks at the click data, the session replays, the funnel metrics, and then reviews the code files between those steps to find fixes.

We also expose everything in Novus as an audit trail. When developers are looking at a ticket that says "checkout page is broken," they can talk to Novus to figure out the exact details: where were the rage clicks, where did the session replay go blank, what's happening in the funnel. When you call our MCP from Claude Code, we spin up a managed agent session behind the scenes to do that research and return results.

Over 90% of our customers who use the MCP and skills are using them inside Claude Code. We found that skills are really important, because otherwise you're kind of guessing on how to use the MCP effectively.

## What made you confident enough to use Managed Agents for Novus?

**Lakhani:** We actually started with a different provider and tried to build our own harness. Then we noticed that internally, nobody on our engineering team was using that provider for their own coding. So we looked at Claude Code, and then we found Claude Managed Agents.

A few things stood out. The sub-agent architecture lets us define agents in plain language. We tried other frameworks where you have to write a ton of code, construct your own graphs and nodes. With Claude, our designers and PMs are the ones defining the sub-agents and how the intelligence should work. They don't need to be engineers to do it.

We also have a very large tool set. We collect billions of data points daily, trillions total. We needed the agent to manage its own tool searching and routing across more than 150 tools without us defining every decision path. With other providers, we had to build that routing logic ourselves. With Claude, we gave it 150 tools and said, "Here's what to call when." It handled it. We know what we do best, which is product analysis. We leave the coding and reasoning to Claude.

And then the evaluation results made the decision clear. Our eval sets are a little different from traditional evals. Rather than running against synthetic benchmarks, we have actual product managers going through the results line by line and saying yes or no. That’s a much harder bar than a benchmark score because these are the same people who would reject the output in production. The agent had a 90%+ success rate against that standard. 

We looked at that number and said, why would we switch? Right now all of our tasks use the most capable model. We're OK with burning token spend in exchange for intelligence. Whatever is the smartest, all the time. We'll figure out optimization later.

The benchmarks blew us away to the point where even the naysayer PMs couldn't tell if it was a human that did it or the agent.

## How did Novus go from idea to product?

**Lakhani:** Novus started as me and our CEO building together. Just the two of us were able to ship production software with the Agent SDK. That's what convinced us this was real. If two people, one of whom is also running a company, can build and launch a product, the barrier to entry is much lower than people think.

## Beyond the product, how is Pendo using Claude internally?

**Lakhani:** All of our engineers are on Claude Code. But it goes well beyond engineering. We've got an in-house package of skills that we distribute to employees: finance skills, Excel skills, some from the public library and some custom. We've set it up so everyone can code inside Claude Code through a virtual desktop.

Our finance and people analytics teams use it for everyday work. They're querying financial data, building board memos, creating dashboards. One thing we found is that Claude Code produces higher fidelity outputs than alternatives for presentations and internal tools. People are building web pages and dashboards that get deployed and shared internally. These aren't one-off analyses. They stick around.

The pace of progress for our strongest adopters is stunning. It makes our people feel powerful. You don't need a full dev team to build something useful. Build like an engineer. Think like a team of ten.

For Pendo, building Novus was more than a product decision. It was a signal about where software development is heading. As teams ship faster with AI, the gap between what's deployed and what's understood grows. Novus exists to close that gap automatically. With Claude handling the infrastructure, reasoning, and tool routing, Pendo's team can focus on what they know best: turning real user behavior into better products.

AI agents

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

Read more

[Read more](/solutions/agents)

Read more

AI agents


Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

Video caption


AI agents

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

"The benchmarks blew us away to the point where even the naysayer PMs couldn't tell if it was a human that did it or the agent."

Zain Lakhani

Chief AI Officer, Pendo


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
