---
category: "15-Claude-AI-Features"
fetched_at: "2026-03-17T10:27:13Z"
last_modified: "Tue, 17 Mar 2026 04:11:29 GMT"
source_url: "https://www.claude.com/customers/greptile"
title: "Customer story | Greptile | Claude"
---

# Greptile builds truly agentic code review with Claude Agent SDK


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Get started

[Get started](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)

Get started

Industry:

Software

Company size:

Small

Product:

Claude Platform

Partner:

Location:

North America

~90% cache hit rates

Prompt caching through the Agent SDK dramatically reduces costs and increases compute efficiency

1 million

Issues caught per month

Read more

[Read more](#)

Read more


Video caption


Read more

[Read more](#)

Read more


Video caption


[Prev](#)

Prev


[**Greptile**](https://greptile.com) builds AI agents that review pull requests with full codebase context. The company serves more than 2,000 organizations, from startups to enterprises like NVIDIA, Brex, and Coinbase, helping engineering teams catch bugs and anti-patterns before they ship to production.

## With Claude Agent SDK, Greptile:

- Achieves ~90% cache hit rates, dramatically reducing costs for both Greptile and self-hosting customers
- Enables multi-hop code investigation that follows leads across git history, similar functions, and pull request context
- Ships new capabilities faster by focusing engineering time on specialized tooling rather than harness infrastructure
- Powers autonomous code review that iteratively investigates issues rather than following rigid workflows
- Provides enterprise customers with cost-effective self-hosting options through efficient compute usage

## The problem

In the AI code review space, most tools follow predetermined paths. They scan a pull request, run through a fixed checklist, and surface findings in a predictable sequence. But Greptile sees code review as an investigation, not a checklist. When a skilled engineer spots something unusual, they don't follow a script. They dig deeper, examine context, trace history, and connect dots across the codebase.

Greptile's team recognized this gap. They had built specialized tools for the investigative work: utilities for grabbing codebase context, finding semantically similar functions, retrieving git history, and more. But their orchestration layer forced these tools into a rigid flowchart. Each step revealed new information, but the system couldn't act on those discoveries because it was locked into a predetermined sequence.

"We wanted to build a system where Greptile could be truly multi-hop and autonomous—where every step reveals new information, and the next step can be based on that information instead of following a rigid flowchart," says Daksh Gupta, Co-founder and CEO, at Greptile.

The team needed an orchestration layer as intelligent as their tooling—one that would let their code review agent think like a skilled engineer.

## Building an agentic code review system with the Agent SDK

The Greptile team considered building their own agent harness but quickly realized where their time would be better spent. "It became clear to us that the value was to spend all of our time building better tools for code review," Gupta says. For a team of 10 engineers, that focus matters.

The Claude Agent SDK offered a powerful orchestration layer that would let them focus on their domain expertise rather than infrastructure. The decision also reflected a technical intuition: agent harnesses and models are tightly coupled. "It was clear to us that models and harnesses would be coupled, and the models were the best," Gupta explains. "That was a really big advantage for the Anthropic SDK."

## Greptile uses Claude for multi-hop code investigation

Claude now powers Greptile's investigative approach to code review. When the agent spots a calculation that looks unusual or a function that differs from similar ones across the codebase, it can autonomously decide what to investigate next. It might examine git history to understand why something changed, trace a commit back to its original pull request to read the context, or compare the code against patterns elsewhere in the repository. "It's acting like an investigative reporter or detective," Gupta explains. "We have all the tooling for the detective, and what we wanted was a really powerful orchestrator for it."

Greptile runs on Opus 4.5. “We believe it to be the best coding model for everything we're trying to achieve with detecting bugs and anti-patterns in code,” Gupta said. “The prompt caching works well for our use case, and the integration with MCP has been valuable."

Greptile also makes heavy use of the SDK's sub-agent capabilities. One sub-agent handles memory retrieval, pulling from a bank of information that includes coding standards the team has expressed, idiosyncrasies Greptile has learned about the codebase, and context from documentation, claude.md files, and cursor rules. This accumulated knowledge informs every review.

The team also uses hooks to inject determinism where it matters. For code review, this means ensuring that every file in a pull request gets examined—a guarantee that's essential for enterprise customers who need thorough, consistent coverage.

## The outcome


The shift to the Agent SDK delivered immediate efficiency gains. Greptile now achieves cache hit rates close to 90%, which translates to meaningful cost savings across their operation. For customers who self-host Greptile using their own Anthropic instances, this efficiency means they can roll out AI code review at larger scale without proportional cost increases. "Now with the Agent SDK, we have true autonomy—every step creates new information, and the next step can be based on that information," Gupta says. "This has fundamentally changed how our code review agent operates."

The deeper impact is in what Greptile can now build. "The Agent SDK has allowed us to ship faster with far more cost effectiveness and allows us to focus deeply on building specialized tooling," Gupta says."We can focus all our energy on building highly specialized tools for the specific types of things we want to achieve."

Rather than maintaining harness infrastructure, the team invests that engineering time in the tools that make code review genuinely useful: better codebase understanding, smarter similarity detection, richer git history analysis.

The results show up in production. In one example from an NVIDIA open-source repository, Greptile flagged an issue that the reviewing engineer initially disputed. The agent responded with additional evidence—comparisons to similar functions across the codebase, relevant git history—and the engineer acknowledged the catch was correct. That kind of multi-step investigation, where the agent can defend its findings with evidence, is exactly what the agentic architecture enables.\
\
Customers have noticed the difference. "Despite having a tech stack that has repeatedly proven difficult for AI to grasp, Greptile has delivered consistent review insights with a good signal-to-noise ratio that has won over even our most discerning engineers," says Jarrod Ruhdland, Principal Engineer at Brex.

Greptile continues to expand what's possible with the Agent SDK, building new capabilities that would have been far more difficult to develop and maintain without it. For a company reviewing over a billion lines of code each month, the ability to focus on domain expertise rather than infrastructure has become a strategic advantage.

"The Agent SDK has allowed us to ship faster with far more cost effectiveness and allows us to focus deeply on building specialized tooling."

Daksh Gupta

Co-founder and CEO, Greptile


Video caption


[Prev](#)

Prev


## Related stories

[Postman automates the API development lifecycle with Claude for 40 million developers](/customers/postman)

Postman automates the API development lifecycle with Claude for 40 million developers

Postman automates the API development lifecycle with Claude for 40 million developers

Customer story

[Customer story](/customers/postman)

Customer story

[How CircleCI built a code validation agent with Claude](/customers/circleci)

How CircleCI built a code validation agent with Claude

How CircleCI built a code validation agent with Claude

Customer story

[Customer story](/customers/circleci)

Customer story

[Descript brings creative taste to agentic video editing with Claude ](/customers/descript)

Descript brings creative taste to agentic video editing with Claude

Descript brings creative taste to agentic video editing with Claude

Customer story

[Customer story](/customers/descript)

Customer story

[How Slack, a Salesforce company, unlocks organizational knowledge with Claude](/customers/slack)

How Slack, a Salesforce company, unlocks organizational knowledge with Claude

How Slack, a Salesforce company, unlocks organizational knowledge with Claude

Customer story

[Customer story](/customers/slack)

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


  Hi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Improve my writing style


  Hi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Brainstorm creative ideas


  Hi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Learn

- Explain a complex topic simply


  Hi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Help me make sense of these ideas


  Hi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Prepare for an exam or interview


  Hi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Code

- Explain a programming concept


  Hi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Look over my code and give me tips


  Hi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

- Vibe code with me


  Hi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

More

- Write case studies


  This is another test

- Write grant proposals


  Hi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.\
  \
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

- Max plan

  [Max plan](/pricing/max)
  Max plan

- Team plan

  [Team plan](/pricing/team)
  Team plan

- Enterprise plan

  [Enterprise plan](/pricing/enterprise)
  Enterprise plan

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

- Claude for Slack

  [Claude for Slack](/claude-for-slack)
  Claude for Slack

- Claude for Excel

  [Claude for Excel](/claude-for-excel)
  Claude for Excel

- Claude for PowerPoint

  [Claude for PowerPoint](/claude-for-powerpoint)
  Claude for PowerPoint

- Skills

  [Skills](/skills)
  Skills

Models

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

- Claude Code Security

  [Claude Code Security](/solutions/claude-code-security)
  Claude Code Security

- Code modernization

  [Code modernization](/solutions/code-modernization)
  Code modernization

- Coding

  [Coding](/solutions/coding)
  Coding

- Customer support

  [Customer support](/solutions/customer-support)
  Customer support

- Education

  [Education](/solutions/education)
  Education

- Financial services

  [Financial services](/solutions/financial-services)
  Financial services

- Government

  [Government](/solutions/government)
  Government

- Healthcare

  [Healthcare](/solutions/healthcare)
  Healthcare

- Life sciences

  [Life sciences](/solutions/life-sciences)
  Life sciences

- Nonprofits

  [Nonprofits](/solutions/nonprofits)
  Nonprofits

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

- Marketplace

  [Marketplace](/platform/marketplace)
  Marketplace

- Amazon Bedrock

  [Amazon Bedrock](/partners/amazon-bedrock)
  Amazon Bedrock

- Google Cloud’s Vertex AI

  [Google Cloud’s Vertex AI](/partners/google-cloud-vertex-ai)
  Google Cloud’s Vertex AI

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

- Startups program

  [Startups program](/programs/startups)
  Startups program

- Tutorials

  [Tutorials](/resources/tutorials)
  Tutorials

- Use cases

  [Use cases](/resources/use-cases)
