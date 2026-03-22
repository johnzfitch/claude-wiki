---
category: "15-Claude-AI-Features"
fetched_at: "2026-03-17T10:27:24Z"
last_modified: "Tue, 17 Mar 2026 04:26:08 GMT"
source_url: "https://www.claude.com/customers/n8n"
title: "Customer story | n8n | Claude"
---

# n8n turns natural language into workflow automations with Claude


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

EMEA

2 months

From concept to first production of the AI Workflow Builder, powered by Claude

Cuts 80% of the work

out of building a workflow, leaving engineers to handle the final refinements

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

Developer Platform

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

Read more

[Read more](/platform/api)

Read more

Developer Platform


Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

Video caption


Developer Platform

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

[Prev](#)

Prev


[n8n](https://n8n.io) empowers technical teams to build, orchestrate, and deploy reliable AI workflows and agents, combining the speed of a visual builder with the flexibility of custom code. Their platform has earned more than 170,000 GitHub stars, putting it in the top 50 projects of all time, and customers span from solo founders to Fortune 100 companies.

**With Claude, n8n:**

- Built its AI Workflow Builder product on Claude in two months from concept to production, with the architecture since evolving into a multi-agent system with specialized agents managing different tasks
- Developed a chat-based workflow creator and debugger that replaces the two-tab workflow of switching between an LLM and the n8n interface
- Cuts 80% of the work out of building a workflow, leaving engineers to handle the final refinements
- Built reliable function calling for complex multi-step workflow assembly, with Claude performing best among other models for precise instruction following 

## The challenge: Getting a model to generate a precise structured format

Before n8n built its AI Workflow Builder, many users had a familiar two-tab setup: n8n on one side, a chat-based LLM on the other. They'd describe what they wanted to automate, copy a suggested workflow, paste it into n8n, hit an error, and repeat. It worked, but the external model lacked context about what was actually happening inside the tool.

n8n had been shipping AI features since 2023. But the next step was more ambitious: what if building a workflow felt like having a conversation?

The challenge was structural. An n8n workflow is a precise object: nodes that need to be found, connected in a specific order, and configured with the right parameters. The team's first approach was to have the model generate the workflow's underlying JSON directly. "That turned out to be quite a big challenge for models," said JP van Oosten, Engineering Manager of n8n's AI team. Generating a complete workflow in one shot required the model to understand the full schema, all node definitions, and all connection logic simultaneously. "These models haven't seen more than maybe 10,000 n8n workflows, compared to millions of TypeScript code files," van Oosten said.

## Selecting Claude for precise instruction following

To solve the JSON generation problem, the team shifted to a tool-based architecture where Claude adds nodes one at a time, connects them, and configures them through discrete function calls. This played to the model's strengths and made the process, as van Oosten described it, "much more digestible for the model."

The team evaluated multiple models. Claude stood out in particular for instruction following. Other models either over-relied on function calls or ignored them entirely. Claude sat in what the team called a "sweet spot": consistently following instructions while using tools as intended.

"Latency and quality were really good,” said Oleg Ivaniv, Lead Engineer on the AI Workflow Builder. “Workflows can be a bit of a challenge to understand.” 

Claude's documentation also helped with specifics like prompt caching, and Anthropic's team reviewed n8n's implementation to ensure the launch went smoothly from a rate-limiting perspective. The first iteration of the AI Workflow Builder took roughly two months from concept to production.

## The results: How n8n assembles workflows through conversation

The AI Workflow Builder gives n8n users something familiar, a chat interface, to do something that used to require understanding node types, connection logic, and configuration options. Users describe what they want to automate, and Claude figures out which pieces to assemble and how. The first generation of a workflow typically takes three minutes instead of the usual 10-30 minutes it takes to build one manually.

"Tool calling is top-notch in Claude, as well as its coding capabilities," van Oosten said. "These are essential to our approach in the AI Workflow Builder."

The clearest before-and-after is the two-tab experience. Users who previously moved back and forth between n8n and an external LLM now have that conversation inside the product. The AI Workflow Builder has context about what's actually happening in their workflow, which makes errors more diagnosable and suggestions more relevant. "Claude has enabled us to provide a familiar chat-based interface to go from idea to fully functional workflows," van Oosten said.

Since launch, the architecture has evolved into a multi-agent system where specialized agents manage different parts of the workflow creation process. The team's prompts are now heavily tailored to Claude Sonnet 4.5, and early experiments with a code-based approach, where Claude generates code rather than making tool calls, have shown promising results with more capable models.

For experienced users, the value is speed. The AI Workflow Builder delivers roughly 80% of a target workflow without manual assembly, so engineers can focus on refinement rather than construction. For first-time users, the value is different. n8n has thousands of templates, but its strength is flexibility, and many users choose the platform for unique use cases that templates don't cover. The AI Workflow Builder gives them a starting point. "It helps first-time users get over that initial mental hump of 'I don't know what I don't know,'" said Ophir Prusak, from the Product Marketing team.

The same interface also helps users debug: when a workflow breaks, they can describe the problem and get help fixing it, rather than relying purely on  documentation or community forums. The team recently saw this play out internally when the AI Workflow Builder assembled a complex workflow for tracking engineering progress. It correctly used multiple form nodes on the first attempt, a result van Oosten attributed to the team's ongoing work on optimizing prompts for specific node types.

## Future use cases 

Looking ahead, the team is exploring whether building node-by-node or subgraph-by-subgraph, mirroring how experienced users actually construct automations, might offer a tighter feedback loop during the creation process. The current version presents a completed workflow at the end; a more incremental approach could let users shape it as it takes form.

n8n is continuing to expand the AI Workflow Builder's capabilities and deepen its work with Claude. The multi-agent architecture opens up new possibilities for handling increasingly complex automation requests, and the team's experiments with code-based generation suggest further quality improvements ahead. 

"The AI Workflow Builder allows us to lower the bar to entry for users to start building with n8n,” van Oosten said, “but also allows more technical users to iterate faster on their ideas.”


"Tool calling is top-notch in Claude, as well as its coding capabilities."

JP van Oosten

AI Engineering Manager, n8n

AI agents

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

AI agents


Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

Video caption


AI agents

Build powerful AI agents that reason through complex problems and execute tasks autonomously with reliable results.

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
