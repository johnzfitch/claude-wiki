---
title: "Descript Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/descript"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:41:57Z"
tags: ["agents", "api"]
---

# Descript brings creative taste to agentic video editing with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Small

Product:

Claude Platform

Location:

North America

13–23% higher intent adherence than leading competitors

Claude Opus 4.6 outperformed other frontier models on Descript's evaluation criteria for translating creative intent

Two thirds of users select a Claude model in Descript’s agent

Descript also ships Claude Sonnet as the default model for its agent

Descript makes video editing work like editing a document: users change the text, and the video updates to match. Last year, the team launched Underlord, an AI agent powered by Claude, that automates complex edits users would otherwise do manually. In January 2026, Descript shipped major updates to Underlord, with Claude Sonnet 4.5 as the default model for self-serve, and Opus 4.6 for enterprise customers.

## With Claude, Descript achieved:

- 13–23% higher intent adherence for Claude Opus 4.6 over leading frontier models in internal evaluations, measured across 100+ real-world test cases
- Two-thirds of models manually selected in the model picker are Claude models
- 9% higher export rate for agent users compared to non-agent users, with nearly 50% more edits made per export demonstrating a deeper creative process
- 46% higher free-to-paid conversion among users who engaged with Underlord compared to otherwise active free users who did not
- 30%+ of all Descript projects now using its agent Underlord at some point in the project lifecycle
- Integration of new Claude models in as little as half a day
- Opus 4.6 outperformed other frontier models on Descript's "Do What I Asked" evaluation criteria, which measures how well the model translates a user's creative intent into concrete editing actions.

## The challenge

Developer Platform

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

Read more

[Read more](/platform/api)

Read more

Developer Platform


Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.


Developer Platform

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

## From workflows to an open-world agent

Descript's AI journey didn't start with agents. The team initially built structured AI workflows: features like "Edit for clarity" or "Create clips" that ran through predetermined orchestration steps, using an LLM as an API call within a fixed pipeline. Descript first integrated Claude in mid-2024 for these workflows, where it excelled at understanding the flow of content and creating compelling clips from longer videos.

These workflows worked for their specific use cases but broke down at the edges. The old system had hard-coded pipelines for specific tasks: "Edit for clarity" would chunk a script, send it to an LLM, and batch-apply cuts. But if a user wanted something slightly different, like targeting only a few paragraphs for edits, or putting edits in a new composition instead of changing the original, the rigid orchestration couldn't accommodate it. "Sometimes users would want something that was a little bit different, and even with an open prompt box, it just wasn't going to work,” said Rachel Bloch Mellon, Head of AI Engineering. 

## The solution

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Introducing Claude Opus 4.6


We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.


Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

## Selecting Claude for creative intent

Building Underlord as a fully agentic system meant the underlying model needed to reason about creative intent, coordinate dozens of tools, and make judgment calls about narrative flow.

Descript evaluated frontier models using an internal framework built around three dimensions: "Don't break things," "Do what I asked," and "Do it well." The team ran more than 100 test cases drawn from real user queries, weighted toward nuanced and difficult edits. Each test is scored by an LLM-as-judge that the team has calibrated against human reviewers. Opus 4.6 outperformed other leading frontier models by 13–23% on intent adherence, with corresponding advantages on quality.

That first dimension—whether it preserves the integrity of the user's project—mattered most. Users are far more tolerant of Underlord not quite nailing their creative preferences than of it overstepping, the team shared. "The degree of anger you see when people say 'it did too much' is much greater than when it didn't quite get the taste right," said Aleks Mistratov, Head of AI Product.

A lot of video editing comes down to taste. "We've found that Claude models do a better job converting very vague and high-level descriptions of taste into concrete edits that are holistically aligned with the user's intent," said Mistratov. "This produces more polished final videos with less required direction from the user."


## The outcome

## How Underlord with Claude changes the editing process

Descript offers all three Claude model tiers through Underlord's model picker: Sonnet models as the default for most users, Opus for enterprise customers who prioritize quality, and Haiku for fast, iterative sessions. More than two thirds of Underlord users default to or select a Claude model.

The advantages show up most clearly on tasks that require creative reasoning. A user uploads a hypnotherapy recording and asks Underlord to recommend where to lengthen or shorten pauses for therapeutic effect. A podcast host provides a detailed list of audio refinements: adjusting music transitions, balancing levels between speakers, adding chapter markers. "Opus outperforms the other leading models on those sorts of things," said Mistratov.

The collaborative workflows are where Underlord really comes alive. A user might ask: ‘Can you highlight parts of the script where an infographic might help me deliver my point?’ Then they review the suggestions and push back where they disagree. "Those types of collaborative workflows were impossible with one-shotting and workflows, and are far more possible now with the agent," Mistratov said.

Descript's philosophy is that Underlord should be a "co-editor to assist in creation, rather than a tool that can one-shot to a final result." That keeps users in the director's chair while Underlord handles the tedious work. "There is so much more of a positive reception of cutting out the drudgery, but keeping the user and the creator in control," Mistratov said.

The numbers tell a similar story. Agent users export at an 8.6% higher rate than non-agent users and make nearly 50% more edits per export, suggesting Underlord isn't replacing the creative process but deepening it. Over 30% of Descript projects now involve agentic editing at some point in the project lifecycle.

## Looking to the future

Descript's thesis was that building a generalized agent with broad context and low-level tools would let them ride improvements in frontier model intelligence. That bet has paid off: when Descript upgraded from Opus 4.5 to 4.6, quality metrics improved across the board on offline evals—with no changes to the agent harness. Opus 4.6 was also their fastest model integration yet: half a day from release to understanding the model's strengths and weaknesses. The team is now focused on multi-turn success metrics, moving beyond single-query evaluations to understanding how well the agent performs across entire collaborative editing sessions.

For the Descript team, the most meaningful impact isn't efficiency gains for power users. It's expanding who can make videos in the first place.

“Underlord might make a pro user who produces five videos a week much more efficient,” Mellon said. “But it’s an even bigger unlock for the teacher who wants to make engaging content for their students but doesn’t have the time to learn complex NLE software, or the time-constrained small business owner who wants to elevate their brand messaging.”

"It’s an unlock for the teacher who wants to make engaging content for their students but doesn’t have the time, or the time-constrained small business owner who wants to elevate their brand messaging."

Rachel Bloch Mellon

Head of AI Engineering, Descript

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
