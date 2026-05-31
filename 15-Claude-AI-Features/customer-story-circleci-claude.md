---
title: "Customer story | CircleCI | Claude"
source_url: "https://www.claude.com/customers/circleci"
category: "15-Claude-AI-Features"
fetched_at: "2026-03-17T10:27:02Z"
---

# How CircleCI built a code validation agent with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Medium

Product:

Claude Platform

Partner:

Location:

North America

90% of the engineering team uses Claude Code

with daily usage jumping 9x since structured adoption began

75% reduction in average test run time

when customers use CircleCI's Smarter Testing feature

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Read more

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

Read more

Building agents with the Claude Agent SDK


The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Video caption


Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Introducing Claude Code

See Claude Code in action—from concept to commit in one seamless workflow.

Read more

[Read more](https://claude.com/product/claude-code)

Read more

Introducing Claude Code


See Claude Code in action—from concept to commit in one seamless workflow.

Video caption


Introducing Claude Code

See Claude Code in action—from concept to commit in one seamless workflow.

[Prev](#)

Prev


[CircleCI](https://circleci.com/), whose CI/CD platform processes billions of jobs annually for teams at Okta, Hinge, Kalshi and Hugging Face, set out to tackle the growing maintenance burden that slows engineering teams down. The result is CircleCI’s autonomous AI agent [Chunk](https://circleci.com/product/chunk/), built with Claude, which identifies and resolves CI/CD-related maintenance issues with minimal human intervention.

## With Claude, CircleCI achieved:

- 75% reduction in average test run time when customers use CircleCI's Smarter Testing feature
- 90% of the engineering team on Claude Code, with daily usage jumping 9x since structured adoption began
- 90%+ prompt cache efficiency in production, meaning context is reused rather than reprocessed across workflows.
- Multi-quarter internal projects completed in weeks, including an AI-powered PR review system. 
- More than 4 in 5 agent tasks now triggered automatically at the point of failure, with the rate of tasks converted into completed pull requests more than doubling since launch

## The challenge: Maintenance backlogs that slow teams

CircleCI's customers are engineering teams where delivery speed directly determines competitive outcomes. Those teams face a persistent tension: test optimization, build fixes, and pipeline improvements all pile up in backlogs while everyone focuses on shipping new features. Technical debt compounds, and the velocity teams are trying to protect gradually erodes.

CircleCI sees this problem intensifying as AI tools accelerate code output across the industry, generating code faster than teams can maintain it. The company needed to solve this internally before they could credibly help their customers solve it too. The goal: build an autonomous agent that could pick up routine maintenance and validate its own fixes before a human ever sees them.

## A decision driven by developer experience

CircleCI's work with Claude started broadly. The company encouraged teams across engineering, operations, and go-to-market to experiment for prototyping, iteration, and analysis. "We encouraged teams to use AI to reimagine the art of what's possible," said JP Leblanc, SVP Engineering. "By providing a single, robust platform for AI exploration, we saw adoption numbers soar."

When the team selected Claude to power Chunk, the deciding factor was the Claude Agent SDK's developer experience: a clean, well-documented interface that made it fast to build. MCP integration meant connecting to existing development tools without coordination overhead. The team found Claude's security posture met their enterprise requirements and rated it the strongest general-purpose model available. 

## A closed loop from task to validated pull request

CircleCI’s agent Chunk operates as a closed loop: a natural language task goes in, a validated pull request comes out. Because customers have already described their build environment in their CI configuration, Chunk can spin up those environments as sandboxes with confidence because Claude has access to the right dependencies and tools. For build failures, Claude receives logs as context. For tests, it gets results from previous runs. Claude generates a fix, and CircleCI pipelines validate it. If the pipeline fails, Claude reattempts. The customer receives a PR that is already "green," with the CI pipeline serving as attestation that the change meets testing, linting, and static analysis standards.

"We could not have built Chunk without the Claude Agent SDK," explained Michael Webster, Principal Engineer at CircleCI. "If we had tried to do this three years ago, the amount of work to support all the language variations, framework integrations, and toolchain connections would have been prohibitive. Now we can build really powerful tools very quickly without all the traditional coordination overhead and custom integration work."

A team of 8 engineers built Chunk, moving from working prototypes in days to production-ready capabilities in weeks. Tasks can trigger automatically (periodic runs to fix flaky tests), be user-initiated (fixing a failed build), or come as ad-hoc prompts through Chunk's chat interface. Predictive test selection, which CircleCI calls Smarter Testing, runs only what is new or impacted. This cut time-to-feedback by an average of 75% and up to 97%. 

Beyond Chunk, Claude Code has become the daily driver for CircleCI's engineering team, with 90% of engineers engaged. Daily usage has jumped 9x since adoption. One team built an AI-powered PR review system that scans for code issues, analyzes downstream SQL dependencies, flags query optimizations, and generates impact summaries. It deployed in weeks rather than the multiple quarters it would previously have required.

## The results

More than 4 in 5 Chunk tasks now trigger automatically at the point of failure, without a human needing to step in. The rate at which Chunk converts tasks into completed pull requests has more than doubled since launch, meaning Chunk is getting better at knowing when it has enough confidence to propose a fix. For one large enterprise customer, analysis time dropped from 14 hours to 18 minutes. A team that previously waited until the following morning to know whether a change was safe now gets that answer in minutes.

CircleCI's roadmap builds on Claude's advancing reasoning capabilities: automated test management, build optimization, and predictive maintenance that anticipates issues before they affect workflows. As code output accelerates, autonomous validation is what keeps the system from falling behind.

"Claude allowed us to bring Chunk to market faster than we would have otherwise," said Webster. "We've put autonomous maintenance, test optimization, and continuous improvement within reach of every developer by giving them an agent that picks up these tasks automatically. Issues that would sit in backlogs for months are now resolved automatically, and customers can stay in flow and focus on innovation rather than dealing with toil."


"We could not have built Chunk without the Claude Agent SDK."

Michael Webster

Principal Engineer, CircleCI


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

[Attention automates sales operations and accelerates revenue with Claude](/customers/attention)

Attention automates sales operations and accelerates revenue with Claude

Attention automates sales operations and accelerates revenue with Claude

Customer story

[Customer story](/customers/attention)

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

  [Opus](claude-opus-4-6-anthropic.md)
  Opus

- Sonnet

  [Sonnet](claude-sonnet-4-6-anthropic.md)
  Sonnet

- Haiku

  [Haiku](claude-haiku-4-5-anthropic.md)
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

  [Console login](../04-API-Reference/Other/platform-claude-com.md)
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
