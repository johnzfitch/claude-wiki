---
title: "Customer story | Wiz | Claude"
source_url: "https://www.claude.com/customers/wiz"
category: "15-Claude-AI-Features"
fetched_at: "2026-03-17T10:27:46Z"
---

# Wiz migrates a 50,000-line codebase with Claude Code, achieving 2x performance gains


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Large

Product:

Claude Code

Partner:

AWS

Location:

EMEA

50,000 lines of Python to Go in ~20 hours

A migration estimated at 2–3 months of specialized engineering effort

1.5x increase in merged PRs

among top 100 contributors, with 90%+ of engineers using Claude Code daily

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

[Prev](#)

Prev


[Wiz](https://www.wiz.io/) is a cloud security platform with over 2,000 employees that helps security teams gain visibility into their cloud environments, manage security posture, and take remediation steps across the full development lifecycle. Wiz’s Data Security Posture Management (DSPM) team is responsible for scanning customer files across every environment and reading their contents to identify security issues like exposed credentials or sensitive data. 

## With Claude, Wiz achieved: 

- **~1 day of active development** to migrate a 50,000-line Python library to Go — a project estimated at 2-3 human months manually
- **2x+ faster PDF processing in production**, with the new Go library fully replacing the sandboxed Python solution
- **Full codebase ownership**, enabling bug fixes and customizations impossible in the original open-source library (including Hebrew language support)
- **A 20,000-line C++ library migrated to Go in 2 days**, with Claude Code generating Go assembly code as part of the process
- **20-30x estimated output multiplication** as the team integrates Claude Code across engineering workflows

## The challenge: Parsing PDF files at scale

Wiz's entire codebase is written in Go, a programming language known for its memory safety and security properties. But for one critical task—parsing PDF files—no adequate Go library existed. The PDF specification is decades old, with hundreds of different implementations across applications and devices, making comprehensive parsing extremely complex. As Liron Levin, a software engineer on the DSPM team, explained: “If you go to Reddit or any other blog, you will see tons of questions like ‘how do I solve this in Go?’ and they will tell you, you can’t.”

The only reliable solution was pypdf, a Python library with over 20 years of development and more than 50,000 lines of code. But running Python inside a Go environment meant wrapping it in a resource-intensive sandbox—essentially a mini virtual machine—that hurt performance and couldn’t run everywhere. Some environments used the sandboxed Python approach; others relied on incomplete Go packages. The result was inconsistency: different tools producing different results for the same file.

“We had a large discrepancy,” Levin said. “It made the code more complicated, and I never felt safe just running it. I wanted to fix this for two years, but the manual effort to port 50,000 lines of a 20-year-old Python library to Go would have taken two to three months of a highly specialized engineer's time. No product manager would ever prioritize that." The project stayed on the backlog.

## The solution: From experiment to production in 20 hours

The team’s initial use of Claude Code was simple: understand unfamiliar code faster. But within a short time, the use case expanded. They use it to review code, plan architecture, and get up to speed on codebases they’ve never touched.

When Levin evaluated tools for the migration project specifically, Claude Code’s contextual understanding was the differentiator. “Its problem-solving abilities are on another level compared to other tools,” he said.

Levin tried the migration on a Saturday. Within one hour of prompting, the basic functionality was working against hundreds of test PDFs. After roughly ten hours of iterative development, the new Go library handled all 500 of his pathological test cases. “I was amazed,” Levin said. “It reminds me of the best developer in the world.”

Claude Code migrated the 50,000-line Python library into an 18,413-line Go codebase in roughly 20 hours—10 hours of active development and 10 hours of testing. Liran Benodis, the DSPM team lead, put it simply: “This project would never have happened without Claude Code. The amount of effort and time that we would have needed to invest—we just wouldn’t do it.”

But migrating the code was only part of the challenge. When Levin deployed the new library to production with a feature flag, 99% of results matched the original—but the remaining 1% required debugging against real customer data. Since this sensitive data had to remain on-premises, Levin developed what his team calls 'polymorphic zero-knowledge debugging.' He would ask Claude Code to generate a diagnostic tool that extracts only structural, non-sensitive information about a problematic file, run that tool in a secure sandbox environment, and feed the redacted output back to Claude.

Through five to ten iterations per file, Claude could identify and fix bugs without ever seeing customer data. The team resolved 20 to 30 distinct issues this way.

## The results: Impact across the engineering organization

The new library was deployed to production within days and now processes PDFs at least 2x faster than the original Python implementation, while eliminating the resource-intensive sandboxing that had constrained the team. The partnership with Anthropic runs across several layers — the team uses Claude Code for engineering work, and Wiz’s broader AI platform (including its ASKI agentic platform and Mikaii assistant) is built on Claude models via Amazon Bedrock. 

The migration gave the team full ownership of their PDF parsing for the first time. They consolidated fragmented implementations into a single codebase that runs consistently across all environments—CLI tools, cloud buckets, and virtual machines. For customers, this means consistent, faster scanning results regardless of where their files live, which is core to the DSPM promise. Issues that were previously unfixable in the open-source library, like inadequate Hebrew language support, could now be patched directly.

Levin then completed a second migration: converting fastText, a 20,000-line C++ data classification library, to Go in just two days—including Claude Code writing Go assembly code. The resulting 5,434 lines of verified Go code passed 100% of model validation tests. Across Wiz more broadly, the top 100 contributors have seen a 1.5x increase in merged PRs since adopting AI coding tools, with more than 90% of engineers now using Claude Code as part of their daily workflow.

“It enables us to do stuff that we wouldn’t even consider,” said Benodis. “Nowadays, when we’re planning our workload, we just multiply it. We can do 20 to 30 times the things we did before.”

Wiz’s engineers now consult Claude Code before reaching out to colleagues, use it to plan and execute new features, and review code with it as a standard part of their workflow. Some developers have moved away from traditional IDEs entirely, working primarily through Claude Code. The team has also built custom MCP connectors for their monitoring systems, enabling Claude Code to help detect and debug issues in production and test environments.

Benodis sees the current mission as embedding Claude Code into every part of the development process. The team is also building an agent powered by Claude that monitors code in production, detects bugs and anomalies, and surfaces issues before they escalate. Individual developers now run multiple Claude Code instances simultaneously, each working on separate features in parallel. “It can't get any better than this,” said Levin. “It makes things that were impossible, possible.” 


Claude Code on the web

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

Read more

[Read more](https://claude.com/blog/claude-code-on-the-web)

Read more

Claude Code on the web


Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

Video caption


Claude Code on the web

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

"This project would never have happened without Claude Code. The amount of effort and time that we would have needed to invest—we just wouldn’t do it.”

Liran Benodis

Team Lead, Data Security Posture Management, Wiz

Piloting Claude in Chrome

We're testing browser-based AI capabilities while building the safety measures needed for wider release. See how Claude works inside your browser.

Piloting Claude in Chrome


We're testing browser-based AI capabilities while building the safety measures needed for wider release. See how Claude works inside your browser.

Video caption


Piloting Claude in Chrome

We're testing browser-based AI capabilities while building the safety measures needed for wider release. See how Claude works inside your browser.

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
