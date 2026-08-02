---
title: "Juno Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/juno"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:38Z"
tags: ["api", "testing"]
---

# Juno helps people with chronic illness find patterns in their symptoms with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Software

Company size:

Startup

Product:

Claude Platform

Claude Code

Claude Cowork

Location:

North America

10% increase in next-day retention

after using Claude for their onboarding flow

100,000 users onboarded

after launching in October 2025

[Juno](https://junocompanion.com/) is an AI health assistant for people living with chronic illness. People talk to it by voice or text about how they're feeling each day, and it draws on the medical history and biometrics they bring in to turn those conversations into symptom patterns and doctor-ready summaries. Its voice and text agents run on Claude. The product took shape during Y Combinator's Spring 2026 batch, when a two-person team had to ship fast.

## With Claude, Juno:

- Increased next-day retention 10% across 4,000 users after using Claude's large context window to process its onboarding flow.
- Lifted first-conversation conversions 3-4% after moving from Claude Sonnet to Claude Opus.
- Built automatic symptom tracking with Claude Haiku to infer severity from how users describe their day.
- Created voice and text agents with access to roughly 50 tools, for tasks like medication tracking and calendar management.
- Onboarded more than 100,000 patients since launching in October, with the app built and maintained by a two-person team using Claude Code.

## The challenge

Claude for Healthcare

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

Read more

[Read more](https://claude.com/healthcare)

Read more

Claude for Healthcare


Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.


Claude for Healthcare

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

## Building for a community many tools overlook

The apps built for people with chronic illness can often be thin and fragmented, aimed at what many treat as a niche. "A lot of people treat this as a minority community, when in fact one in three adults live with a chronic condition," said Marshall Gould, co-founder and CEO of Juno.

People with chronic illness often manage several symptoms a day, many of them correlated with environmental factors. Finding what drives a flare-up means tracking everything, and most people won't keep a manual log. They also tend to be less than fully candid with the professionals meant to help them, leaving out what feels embarrassing or beside the point. The people with the most to gain from pattern detection are often the least likely to produce the data that makes it possible.

Gould and his co-founder both live with chronic conditions, and while earning a master's in genomic medicine at Oxford, Gould researched how people with chronic illness use social media. "When people think about chronic illness, they think about someone looking obviously ill," he said. "The reality is many people with a chronic condition look fine on the outside, but it's just a mask for trying to live a normal life.”

## The solution

Cowork

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

Read more

[Read more](/product/cowork)

Read more

Cowork


Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.


Cowork

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

## Reading symptoms in how people talk

To pick a model, Juno's founders ran a head-to-head usability test with 100 people living with chronic illness. Each user asked a real health question, like describing a symptom and asking what to do, then scored how useful each model's answer was. Claude Opus scored highest of the models they tried. Early on, the team relied on a fine-tuned model, but found that prompting Claude, and moving to each newer release, beat what fine-tuning gave them. So they shifted to a system prompt, refining it to roughly 4,000 lines over three to four months to consistently perform well for their users.

The product runs on a mix of Claude models, each doing a different job. Claude Sonnet carries the everyday conversation, the daily check-ins where someone describes how they're feeling. Claude Opus takes the tool calls where accuracy matters most, drawing on the roughly 50 tools the voice and text agents share: a user can tell Juno they have taken their morning medications and have it update the log, ask what they have missed, or, on a low-energy day, have it reshape the calendar around the most important tasks and push the rest to later in the week.

The agents work from the health data each person chooses to share. Users upload their medical history, records, diagnoses, and medications directly into Juno, and the app pulls in data from connected devices and wearables where available. A newly-available Gmail connection lets users import the test results and referral letters buried in their inboxes, and direct integrations with health systems’ electronic records are in development.

Underneath each conversation, Claude Haiku reads the transcript and extracts symptoms and patterns, scoring them on Juno's own severity scale. Someone who mentions their head hurts and wonders whether it's the coffee gets a headache logged with the time and a likely trigger, no form required. Logging a symptom as a five out of ten, with the time and a probable cause, is the kind of structured chore patients tend to abandon. Juno reads it from the conversation instead, learning each person's baseline way of speaking and inferring how bad a day is from the words they use.

The tone is a deliberate choice, too. Because Juno stays non-judgmental, people tell it the things they might hold back from a live conversation, surfacing patterns a clinical intake might miss. The same closeness creates a risk, though. A model that agrees with whatever a user says can also be highly retentive and quietly harmful. "It creates a cascade that's almost limitless," Gould explained.

Juno's prompts draw on motivational theory, guiding people toward their own realizations rather than naming what's wrong. The prompts also rely on Gould's Oxford research showing that people with chronic illness engage roughly eight times more with encouragement and small wins than with negative content. "Our aim isn't to be the nicest chatbot in the world," he said. "It's to create something more actionable, to make people healthier." Juno's semantic analysis shows the pattern: mood often dips over the first few sessions, when Juno isn't simply telling people what they want to hear, then climbs over time.

## Building and testing the app as a team of two

The founders lean on Claude Code and Claude Cowork to move fast. "Being a team of two, you have to be extremely efficient," Gould said. Cowork can take a task like building a pitch deck most of the way to done on its own, and for heavier work the team kicks off large batches of agents, sometimes around 100 at once, to work a complex build in parallel. The front end started in Claude Design, where the team wrote a design.md spec covering fonts, structure, and colors that Claude follows when generating new screens. "We like to give Claude some free rein to experiment with what would be good UX and UI," Gould said, "and then, using our own taste, we make it better." In practice that means letting Claude draft ten layouts before they pick one and refine it by hand.

Mobile testing is the hardest part for a two-person team, with a long list of devices and screen sizes to cover. Juno connects Claude Code through the Model Context Protocol (MCP) to mobile simulators that run in the cloud around the clock. When a bug appears, Claude Code reproduces it across devices, applies a fix, runs CI/CD checks with a Claude Code review, and confirms the fix before it ships.

"We want to take the average time to diagnosis from 7.6 years down to just a couple of months, if not days."

Marshall Gould

Co-founder and CEO, Juno

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Claude Code


Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.


Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

## The outcome

## Higher usability, and users who stay

Since launching in October, Juno has grown to more than 100,000 users, and the founders run five to ten user calls a day to shape what comes next. Half of its users manage more than three conditions at once. 

On the first conversation, moving from Claude Sonnet to Claude Opus lifted conversion by 3 to 4%, as new users reached a moment of value sooner. That same move helped retention: once Opus could take in Juno's full onboarding, about 50 slides of personal history, through its large context window in one pass, next-day retention rose by 10%. "The more that you do, the less useful the app becomes," Gould said. A generalist app can only stretch so far, which is why Juno is moving toward generative UI that reshapes itself per condition: a period-tracking section for endometriosis, live blood pressure tied to energy for POTS.

The larger goal is diagnosis. "The one thing every person with a chronic illness has in common is that they were once undiagnosed," Gould said. By Juno's own figures, getting that diagnosis in the U.S. is often slow and expensive, on the order of \$30,000 per patient. For rare conditions, the path is longest: studies have found it takes an average of 7.6 years in the U.S. to reach a correct diagnosis, through visits to as many as eight physicians and two to three misdiagnoses along the way. By structuring a long medical history, lab results, and daily conversation into something a doctor can read in a page, Juno wants to compress that. "We want to take the average time to diagnosis from 7.6 years down to just a couple of months," Gould said, "if not days."

"Our aim isn't to be the nicest chatbot in the world. It's to create something more actionable."

Marshall Gould

Co-founder and CEO, Juno

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
