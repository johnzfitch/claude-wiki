---
title: "Delight.ai Claude Code case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/delightai-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:41:48Z"
tags: ["agents", "claude-code"]
---

# Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Startup

Product:

Claude Code

Partner:

AWS

Location:

North America

1 week → 1–2 days

Time to fix and redeploy a production AI agent issue

Every customer deployment regression-tested

through Claude Code-built internal tooling

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

Read more

[Read more](#)

Read more

Claude on Amazon Bedrock


Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

Video caption


Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

[Prev](#)

Prev


[Delight.ai](http://delight.ai) builds AI agents for customer support on top of Sendbird's messaging, voice, and video infrastructure, which handles 7 billion monthly conversations for enterprise companies. With Claude as its primary model, its AI concierge resolves complex, high-stakes interactions across retail, travel, B2B SaaS, and marketplaces that previously needed human escalation.

We sat down with Clara Park, a software engineer on Sendbird's AI/ML team. Using Claude Code, she builds the internal tooling that gets every customer's agent ready for production.

## Anthropic: For people who aren't familiar with Delight AI, what does the product do, and where does Claude Code fit into your team's work?

**Clara Park, Sendbird:** We deploy AI agents for companies like Mixpanel and on-demand services across retail and travel, handling high-volume conversations around subscription changes, order support, and the kinds of edge cases that used to get escalated to a human. Claude is one of the primary models powering those agents. On the AI/ML team, Claude Code is also what we use to build the internal tooling that gets every Delight AI deployment ready for production. We've essentially built our whole debugging and regression testing workflow on Claude Code. It lets us test agents at scale and catch issues before they reach customers, which we couldn't really do before.

## After Claude Code, the time to fix a production AI agent issue dropped from about a week to one or two days. Walk us through what changed.

**Park:** AI agent conversations are never perfect, and errors like wrong pricing or incorrect legal language would demand an immediate fix. After an agent goes into production, it used to take us about a week to fix issues, test, and deploy. Now it takes just one or two days max. The week was mostly manual work. Every AI engineer had their own Python notebook for generating test conversations and labeling them, which was inefficient. After we integrated everything into one tool all the engineers use, the time dropped. If we see a conversation in production with issues now, we can fix it directly.

Since adopting Claude Code in November, our weekly pull request creation and PR merge counts have roughly doubled. In early November, we had around 700 PRs created and 600 merged per week; by May, we were closer to 1.6K PRs created and 1.3K merged per week. This also aligns with our Claude Code token usage growth.

"Since adopting Claude Code in November, our weekly pull request creation and PR merge counts have roughly doubled."

Clara Park

Software engineer, Delight.ai

## How has Delight.ai’s approach to AI evolved to get to where you are now?

**Park:** Early on, our agents were plain RAG chatbots. Then the industry moved into a deflection era, where the goal was keeping tickets away from human agents, with AI resolving the simple ones. As models got better at tool calling, longer context, and reasoning through multi-step problems, our agents evolved to covering the full lifecycle of a request. For example, a customer comes in to change their plan, realizes they were overcharged last month, and wants to update their payment method. The agent handles all three in one conversation. 

Anthropic: You're running a multi-model architecture. How do you decide which model handles what?

**Park:** Different tasks have different criteria. During support conversations, we run safeguards against prompt injection, like someone falsely claiming a paid membership is free, for example. After the conversation ends, we run a separate analytics pass: classifying topics, analyzing sentiment, and checking for hallucinations.

The tradeoffs shift depending on the task. Summary generation needs to be fast. Hallucination detection can afford to be slower, but accuracy matters more there. We maintain an internal test set built from real examples of the behaviors we care about: hallucinations, out-of-scope handling, and intent classification edge cases. Whichever model performs best on a given task is what we use.

## You've built a system that clusters issues from production conversations and surfaces AI suggestions to customers about what to fix. Why Claude Opus for that work?

**Park:** Analyzing production conversations is genuinely complex work. As an engineering team, we cluster issues by topic across thousands of conversations, then generate suggested fixes. Not one-off patches, but general improvements the customer can act on. That output goes directly to the customer, so it has to be right. We tested lower-cost models first. They produced repetitive labels and kept surfacing minor issues while missing the critical ones. For a multi-step pipeline like that (cluster, synthesize, recommend) where the result is what the customer sees and acts on, we needed a model that could hold the whole thing together. That's why we use Opus 4.8.

## Walk us through the internal tooling your team has built with Claude Code.

**Park:** The first is a conversation debugger. When an agent has a problem in production, the tool fetches the conversation log, surfaces the system prompt, and shows us expected versus actual behavior side by side. We run that analysis through Opus to pinpoint where to fix it. The second is our regression testing tool. You give it a user persona and a scenario to test, and it automatically generates conversations and runs them at scale. We use it to validate every customer's agent before it goes into production. After that, the customer's own QA team runs through it and gives us the go-ahead to ship.

## Beyond the tools, how has Claude Code changed your day-to-day as an engineer?

**Park:** Volume, mostly. Before, I could get through one or two tickets a day. Now I can hand something off to Claude Code, step away, and come back when it's done. It's also changed how I approach architectural decisions. I used to take those straight to my manager or a senior engineer. Now I work through them with Claude Code first and come to the conversation with options already on the table. That's been genuinely useful.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Read more

[Read more](/product/claude-code)

Read more

Claude Code


Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Video caption


Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

"We've essentially built our whole debugging and regression testing workflow on Claude Code. It lets us test agents at scale and catch issues before they reach customers, which we couldn't really do before."

Clara Park

Software engineer, Delight.ai

## What does Delight's infrastructure look like behind the scenes?

**Park:** We run Claude on Amazon Bedrock and the direct Anthropic API as peer routes. An internal proxy picks between them per request based on real-time latency, error rates, and capacity. Whichever path is responding faster and cleaner gets the request. Rate limit errors are critical for us: customers buy an AI agent specifically because they want 24/7 support, so any gap there is a product failure. 

Bedrock is valuable because it gives us additional enterprise-ready infrastructure, regional flexibility, compliance alignment for some customers, and another capacity path for reliability.

Running both paths improves reliability in two ways. It gives us provider-level redundancy, so a slowdown or throttling event on one route doesn't automatically reach the customer. And it gives us more regional and infrastructure flexibility than running on a single path. On the integration side, once a model is set up, adding a new version is straightforward. We update the model name, set parameters for new features like extended thinking, and we're running.

## Has the Claude Platform shipped any capabilities recently that impressed you?

**Park:** The [advisor tool in Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool) launched last month. A faster, cheaper model handles the work from start to finish. When it hits something too complex to figure out on its own, it pauses, consults Opus, gets a plan or a correction, and keeps going. Opus only steps in at the hard moments, not for every response.

That was exactly what we were trying to build ourselves. For lighter tasks, you don't need Opus on every turn. But for genuinely complex queries, you need that reasoning power, and we wanted a system that could tell the difference automatically. It solves the exact problem we were going after.

## What's next? Where is the team taking this?

**Park:** The biggest is what we call Zero-Touch Improvement, which is really AI improving AI: the agent learns continuously, customers can see what's going wrong and why, and fixes happen without a human in the loop. Today they have to come to us to diagnose and deploy a fix. We want them to own that themselves.

Voice is the other push, where latency isn't just a metric, it's the product. A small delay breaks the feeling of a real conversation.

Finally, there’s  memory. Most agents in the market still start every conversation from zero. When a customer comes back, the agent should already know their history and what's been resolved. That's the shift from a support interaction to a relationship with the brand.

Claude Code on the web

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

Claude Code on the web


Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

Video caption


Claude Code on the web

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

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
