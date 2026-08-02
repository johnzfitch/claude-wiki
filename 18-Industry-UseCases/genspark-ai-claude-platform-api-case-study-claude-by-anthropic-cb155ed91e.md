---
title: "Genspark.ai Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/genspark"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:43:26Z"
tags: ["agents", "api"]
---

# Genspark's Super Agent orchestrates 150+ tools with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


[Play video](#)

Play video

Industry:

Software

Company size:

Startup

Product:

Claude Platform

Location:

North America

\$250M ARR since pivoting to the Super Agent

in early 2025

150+ specialized tools orchestrated by Claude

inside a single agent

[Genspark](https://genspark.ai/) is an AI workspace where one prompt produces slides, spreadsheets, documents, design posters, or websites for non-technical knowledge workers. The product is built around the Super Agent, which uses Claude to coordinate more than 150 specialized tools in response to whatever a user asks for.

## With Claude, Genspark:

- Surpassed \$250 million in annual recurring revenue after pivoting to the Super Agent in early 2025
- Orchestrates 150+ specialized tools end-to-end with its Super Agent architecture
- Creates AI slides, spreadsheets, and documents driven by Claude's coding capability
- Built an internal engineering culture where 100% of code is written by AI

## The challenge

The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

Read more

[Read more](https://claude.com/problem-solvers)

Read more


The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.


The most driven founders are problem solvers. Watch their unscripted conversations with the Anthropic engineers.

## A rigid workflow that couldn't keep up

Genspark launched out of stealth in mid-2024 as an AI search product, then steadily expanded into parallel search and asynchronous deep research that would email users a finished analysis after running for several minutes. "If we positioned the product as search, it needed to return to the user in one second, or at most ten seconds," said Kay Zhu, co-founder and CTO at Genspark. "Ten seconds was too short for the system to do meaningful work." 

The team kept expanding the runtime—first to parallel queries, then to background workflows running for minutes—because each expansion let them tackle harder problems for users. One paying user spent a week using a traditional search engine to compare credit cards against a long list of personal criteria, then handed the same question to Genspark's asynchronous agent and got the same conclusion in 15 minutes.

The architecture underneath, though, was a directed graph of predefined workflow nodes, and that design was hitting a ceiling. "It was too rigid," Zhu said. "It often broke on edge cases." Search satisfaction in the field has hovered around 80% for a decade, Zhu noted, no matter how much better the underlying systems get. Users adapt: as the system handles more, they ask harder questions, and the satisfaction rate stays flat. Genspark was seeing the same pattern. Simple questions ran through too many steps. Hard questions hit walls the workflow didn't know how to route around. The system that had taken Genspark to millions of users could no longer go where users wanted to go.

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

##  An agent loop that finally worked

The ReAct-style agentic loop, in which a model decides each next step rather than following a fixed plan, had been on Zhu’s mind since 2023. "The idea is very elegant," he said. "If the model is powerful enough, it should be able to know when to call which tool and when to stop." He tested it against every new frontier model that came out, roughly every three months, for two years. The failures were always the same: the model fell into infinite loops, hit the same error repeatedly, or failed to recognize when it had enough information to stop.

In early 2025, Zhu tried again at home with Claude Sonnet 3.7, the newest Claude release at the time. "To my surprise, it was very intelligent," he explained. "It knew when to stop and knew which tools to call. When some tool returned an error message, it would know what alternative way to try." That recovery behavior was the missing piece. Genspark rewrote the product around it.

The Super Agent that launched in early 2025 is model-agnostic by design, with different frontier models doing different jobs. Claude plays two central roles. The first is the agent loop itself: at each step in a task, Claude decides which of the 150+ available tools to call next, when to gather more information, when to backtrack, and when to summarize and return a result. For the most demanding planning problems, Genspark fans out to multiple frontier models in parallel and uses Claude to reconcile their plans into one. The second is code generation. Behind the AI slides, AI spreadsheets, and AI documents that users see, Claude generates the code that produces the final artifact.

"The old way was running on a rail," Zhu said of the original architecture. "If everything goes well, the train runs very fast. But if something goes wrong, the train gets flipped. The Super Agent is more like an experienced driver with a GPS and a goal in mind. It will try every means to reach the goal, and if there are detours or obstacles in between, it will find a way out."

That shift, from architecture as constraint to architecture as adaptive runtime, changes what a startup competes on. "Nobody really has a moat anymore," Zhu said. "The moat is execution speed." That belief shapes how Genspark operates internally. Roughly 50 engineers produce all of the company's code through AI tools. Some have built what they call a "lights-out factory" where issue creation, pull request composition, code review, merging, and testing all run automatically. Zhu personally writes code in Claude Code's plan mode. "It's like talking to a very experienced software engineer, someone who's super intelligent and knows the codebase really well," he said.

"Claude knew when to stop and knew which tools to call. When some tool returned an error message, it would know what alternative way to try."

Kay Zhu

Co-founder and CTO, Genspark


## The outcome

## From experiment to \$250M ARR

The Super Agent helped Genspark grow past \$200 million in annualized revenue. The feedback the team hears most from users, Zhu said, is from people who realize "other AI tools just chat. Genspark actually works." With a team of roughly 50 engineers, the company has been shipping major versions of AI Workspace on a roughly two-month cadence, with 3.0 the most recent release, and 4.0 already in planning.

Users invented use cases nobody at Genspark had planned for. A New York real estate analyst now produces investor pitch decks in hours, work that used to take weeks of multi-person research, and has started winning contracts away from larger firms. Japanese seafood industry CEOs use Genspark to analyze domestic demand and source new leads. One customer used Genspark’s agent to resign from a job he found too uncomfortable to quit in person. 

Where Zhu sees model capability heading in 2026 shapes what Genspark is building next: effectively infinite context built through scaffolding around the model, long-horizon agents that can run for hours or days on complex tasks instead of minutes, and orchestration models capable of driving fleets of sub-agents in parallel. Genspark has internal experiments running against each.

Genspark spells out the bet on a billboard along US-101 in San Francisco: a three-day work week. The premise is that AI can handle the busywork, aligning slide bullets, building pivot tables, formatting documents, so people can spend their time on what they actually value. "We want to bring the Claude Code experience that software engineers have to all white-collar workers," Zhu said. "The model is so intelligent right now. The distribution is super uneven. Some people experience the latest capability and their lives change totally. A lot of people haven't experienced that yet. We want to accelerate that transition."

"It's like talking to a very experienced software engineer, someone who's super intelligent and knows the codebase really well."

Kay Zhu

Co-founder and CTO, Genspark

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
