---
title: "Box Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/box"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:43:17Z"
tags: ["api", "skills"]
---

# Box builds document creation into its AI agent with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Large

Product:

Claude Platform

Location:

North America

Concept to customer-facing capability in weeks using the Claude Skills API

instead of building document generation in-house

2-minute contract redline

when Box's team tested jurisdiction changes on a contract

[Box](https://www.box.com/) securely connects enterprise content to AI, enabling organizations to manage files and automate business processes. Its agent, the Box Agent, recently gained the ability to support document creation through Anthropic's Skills API.

## With Claude, Box:

- Saved months of development time by using the Skills API instead of building document generation in-house
- Went from concept to customer-facing document creation in weeks by using the Skills API instead of building in-house
- Redlined a contract in 2 minutes instead of an afternoon of manual review
- Generates multiple document formats from a single conversation: the same source material returned as a slide, a spreadsheet, or a written brief
- Creates PowerPoint, Excel, Word, and PDF files inside the Box agent without a separate code-execution environment
- Analyzes spreadsheets using their full structure rather than extracted text
- Maintains enterprise security through Box's existing LLM gateway, with only 2 new data paths added

## The challenge

Redlined a contract vs. an afternoon of manual review


Redlined a contract vs. an afternoon of manual review


2 minutes

Redlined a contract vs. an afternoon of manual review

## Bringing document creation inside Box

Box customers could already create, collaborate on, and sign documents inside the platform. Early customers of the new Box Agent consistently requested the ability to generate presentations, documents, and other file formats. Building that capability in-house didn’t make sense from a timing, effort, or focus standpoint. It would have meant standing up a distributed code-execution environment across Box's data centers and meeting the 5-nines reliability bar Box's customers expect. Box's team estimated the work for the in-house path would take months of engineering time.

“Box's strength is in how enterprise content is managed, governed, and put to work,” said Darryl Sladden, Staff Product Manager for AI at Box. “The intelligence to make a good slide is a different problem, and it's one Anthropic has already solved.”

## The solution

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Choosing the right Claude model


Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.


Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## Pre-built skills connected to the path Box already trusted

Box turned to Anthropic's Skills API for the generation itself. Anthropic's pre-built skills for PowerPoint, Excel, Word, and PDF deliver packaged expertise: they encode what makes a slide visually appealing, how to structure analytical spreadsheets, and how to handle complex Word edits cleanly.

“Using the API, we’re able to show the customers very early how they can save work and time, and start to change their processes very quickly,” Darryl says.

The integration principle was to change as little as possible. Box already routes all LLM requests through a production gateway that handles logging, request counting, and access control. Rather than create a separate path for document generation, the team added exactly two things: file upload on the way in, file download on the way out.

“We ran this through our main production path and added the file upload, file download capabilities,” Darryl says. “Everything else: the same file versioning, the same ownership. The only difference we have to talk about is those two paths.”

Inside the agent, Box routes work across Claude models by difficulty. Sonnet typically interprets the user's request, searches Box for relevant source files, and assembles context, while file generation often goes to the more capable Opus model. That flips the common pattern of using the larger model as planner and a smaller one as executor, but it matches where the difficulty sits: orchestrating over Box content is well-bounded, while producing a document that looks right demands more from the model.

The pre-built skills are also what made the speed possible. Spreadsheet analysis benefits from the full structure of a spreadsheet rather than just text extracted by RAG, and PowerPoint generation depends on judgment that's hard to specify, let alone replicate. “PowerPoint files have a lot of taste,” Darryl said. “It's really the designer's mind that I always find is most valuable, that it's actually been trained in.”

The capability runs under Box's existing Anthropic agreement, which contractually ensures customer data isn't used for training. Containers that execute skill code are short-lived, lasting only minutes. For Box's security team, the review was about two new data paths, not a new trust boundary.

How enterprises are building AI agents in 2026

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

How enterprises are building AI agents in 2026


New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.


How enterprises are building AI agents in 2026

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

## The outcome

## Redlining a contract in 2 minutes

Using the Skills API, Box went from concept to customer-facing capability in weeks. A member of Box's internal team tested the agent on a real contract, asking it to show redlines for changing the governing jurisdiction from New York to California. “We just waited two minutes, and it output the entire document,” Darryl said. “It was smart enough to change not only the state, but the city and all the additional clauses that talked about court.”

The financial summary flow works the same way: a user asks for a slide summarizing a company's financial position; the agent searches their Box folders, finds the previous quarterly report and recent monthly updates, pulls the relevant figures, and returns a formatted draft slide with the initial work done, ready for the team to add insights. A follow-up request for the same output as a spreadsheet reuses what the agent already found.

Box went from concept to customer-facing document creation capability in about a month, a timeline that wouldn't have been possible building from scratch. The time that didn't go into infrastructure went into making the agent actively useful inside the enterprise.

The principle that emerged: use pre-built skills where the expertise is general and already trained in; build your own where the knowledge is yours. “The trajectory of AI is really what we're betting on for this,” Darryl said. “Our advice is to look at each capability not only how it is now, but how it will be in six months.”

“Using the API, we’re able to show the customers very early how they can save work and time, and start to change their processes very quickly."

Darryl Sladden

Staff Product Manager for AI, Box

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

[Juno helps people with chronic illness find patterns in their symptoms with Claude](/customers/juno)

Juno helps people with chronic illness find patterns in their symptoms with Claude

Juno helps people with chronic illness find patterns in their symptoms with Claude

Customer story

[Customer story](/customers/juno)

Customer story

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)

A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)

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
