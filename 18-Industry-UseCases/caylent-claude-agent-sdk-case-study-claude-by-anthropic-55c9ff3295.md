---
title: "Caylent Claude Agent SDK case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/caylent"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:41:52Z"
tags: ["agents", "sdk"]
---

# Caylent turns months of migration work into days with Claude Agent SDK


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Professional services

Company size:

Medium

Product:

Claude Platform

Partner:

AWS

Location:

North America

90% reduction in engineering hours

on a 2,500-procedure database migration

\$600,000 in annual licensing eliminated

alongside a 58% faster migration

One database migration can cost more than 10,000 hours of engineering work before a single workload is validated. For years, that math priced modernization out of reach. Caylent, a cloud consultancy that helps more than 1,200 customers build and run their systems on Amazon Web Services, built Caylent Accelerate™ to break that math: an agentic delivery system that runs hundreds of Claude instances in parallel, finishing migrations in days instead of months.

## With Claude, Caylent:

- Cut engineering hours by 90% on a 2,500-procedure database migration
- Eliminated \$600,000 in annual licensing for a global enterprise SaaS customer
- Completed database migrations 58% to 82% faster across four additional customer engagements
- Compressed pre-sales environment analysis from weeks to hours
- Expedited 70% of cloud operations remediation work and cut mean time to resolution by 40%
- Reached more than 85% daily Claude use across its 900-plus-person team, with Claude Code as the primary development environment

## The challenge

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

Read more

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

Read more

Building agents with the Claude Agent SDK


The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.


Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

## Migration math that priced out modernization

Caylent's work centers on getting customer systems onto AWS and modernizing what already runs there, and database migration was the sharpest pain. When a customer moves from a legacy commercial database to a modern open-source one on AWS, thousands of stored procedures have to be translated one by one — roughly four hours each, by engineers fluent in both platforms. That expertise is rare, and many customers deferred entirely, letting technical debt compound.

Cloud migration assessments had a parallel problem: mapping application and server dependencies for a mid-sized environment consumed months of analysis before a single server moved. "Human bandwidth set a hard ceiling on how many engagements we could accurately scope," the team explained.

## The solution

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

Claude on Amazon Bedrock


Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.


Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

## Proven on Caylent first

The route to Accelerate started inside Caylent. "We became our own first customer before we built anything for anyone else," the team said. More than 85% of the 900-plus-person company uses Claude daily, and DevBench, an internal harness for large engineering backlogs, compresses hundreds of hours of effort into 10 to 20.

"Caylent runs on Claude," said Randall Hunt, Chief Technology Officer at Caylent. "We’ve deployed Claude Enterprise company-wide and made Claude Code our engineers’ primary development tooling. We’ve already instrumented Claude Tag in several workstreams across departments and we built our global context management and autonomous backlog development systems entirely on Claude models. This daily operating experience, combined with Anthropic’s pace of innovation, has convinced us that we’re building on a compounding technology stack. Through Caylent Accelerate and ACE, our Anthropic consulting division, we put these same patterns to work for our customers."

Model selection for customer deployments started from one constraint: as an AWS Premier Tier Services Partner, Caylent runs Accelerate inside customers' own AWS environments through Amazon Bedrock, so models unavailable on Bedrock were excluded from the start. Caylent then tested frontier and fine-tuned open-source models on security, enterprise suitability, and task performance. Claude stood out on instruction-following, code generation across database dialects, and reasoning over the long contexts migrations produce. "In production, inconsistent outputs are expensive, and Claude's reliability was the deciding factor," the team noted.

## How it works: Specialized agents inside a customer's own AWS account

With the model chosen, the question became orchestration. The first version of Accelerate, Caylent's agentic delivery system, ran on a homegrown harness. It proved the concept but was brittle: custom orchestration code, hard to maintain, and slow to extend.

The team rebuilt Accelerate on the Claude Agent SDK, adopting the same agent loop and tool infrastructure that powers Claude Code. Heavier orchestration frameworks added abstraction the pipelines didn't need, while the Claude Agent SDK let the team define agent behavior directly in markdown, keeping orchestration logic in prompts rather than application code. That made Accelerate, in the team's words, "faster to build, easier to iterate, and simpler to debug."

Each workflow Accelerate runs for a customer is now a pipeline of stages assigned to specialized Claude agents, each scoped to only the tools it needs: an inventory parser, a dialect translator, a guardrail validator, a summary generator. An orchestrator routes work between them and selects the right model for each task, Haiku for high-volume parsing, Sonnet for synthesis and executive output. In database modernization, the pipeline parses the full inventory, classifies every object by complexity, and retires dead code before translation begins. Claude translates the active objects into the target dialect and tests them, the guardrail agent validates each translation before it commits, and a summary agent turns the results into a business-ready assessment with time and cost projections. The division of labor is deliberate. "Deterministic scripts handle precision tasks," the team explained. "Claude handles everything requiring reasoning, judgment, or language, which is most of the work." Engineers validate edge cases and final output.

Everything stays inside the customer's AWS account: no data transit to external systems, no customer data used for model training, and an AWS CloudTrail audit log capturing every AI-assisted action. Accelerate also runs before a contract is signed. In hours rather than weeks, it produces a complexity breakdown, a time estimate, and projected savings, so the first sales conversation starts from evidence.

"Caylent runs on Claude."

Randall Hunt,

Chief Technology Officer, Caylent


## The outcome

## 90% fewer hours and a cleaner database

The flagship engagement, one of Accelerate's earliest, cut migration hours by 90% for Arborgold. The software company had carried its SQL Server estate for more than a decade: 2,500 stored procedures across five database clusters, the kind of technical debt a founder-owned software business keeps deferring because the bill never pencils out. The target was Amazon Aurora PostgreSQL, and translated by hand, the work ran to roughly 2,600 hours.

Accelerate started by reading the whole estate, and the first finding changed the project: 1,850 of the 2,500 procedures were dead code no workload had touched in years, objects a manual team would have translated anyway. Claude classified every object, retired the dead ones, translated the active procedures, and validated each through the guardrail agent. The migration finished in about 220 hours instead of 2,600, with active procedures translated 66% faster than the general-purpose AI tools tried without Accelerate. With projected database costs down 77%, Arborgold ended with a cleaner database than it started with and a modernization path that had been priced out the week before.

A software asset management company brought a smaller version of the same problem: 257 Oracle objects scoped at roughly 1,486 hours. Accelerate finished in about 268 hours, an 82% cut worth \$202,000 in savings. "The economics hold whether the migration is large or small," the team said. The pattern repeats: migrations 73% faster at a healthcare IT provider, 75.7% faster at a data services firm that saved 2,374 engineering hours, and 58% faster at a global enterprise SaaS company that also eliminated \$600,000 in annual licensing. 

## Looking ahead: A practice built on Claude from day one

The architecture reaches past migration too: in Accelerate for Agentic Cloud Operations, Caylent's new managed services offering, Claude on Amazon Bedrock AgentCore expedites 70% of remediation work and has cut mean time to resolution by 40%, while Caylent's engineers focus on the work that moves the business forward.

Caylent's newest practice is Claude-powered from day one: in April 2026, the company launched ACE, its Anthropic Consulting and Engineering practice, advancing its role as a Preferred Services Partner in the Claude Partner Network. Forward-deployed teams embed inside customer organizations to build the integrations and internal capabilities that make AI adoption stick. Every stage of the engagement runs on Claude Code, and DevBench is now available to ACE customers. Demand for that work is concentrating among software-intensive enterprises, and the team sees the question changing: "They have stopped asking whether AI belongs in the software development lifecycle and started asking how to operationalize it."

## Related stories

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

[Quantium scales Claude across Australia's largest enterprises](/customers/quantium-qa)

Quantium scales Claude across Australia's largest enterprises

Quantium scales Claude across Australia's largest enterprises

Customer story

[Customer story](/customers/quantium-qa)

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
