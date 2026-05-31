---
title: "Customer story | Carta Healthcare | Claude"
source_url: "https://www.claude.com/customers/carta-healthcare"
category: "15-Claude-AI-Features"
fetched_at: "2026-03-17T10:27:00Z"
tags: ["cli"]
---

# Carta Healthcare cuts clinical data processing time by 66% with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Get started

[Get started](https://claude.com/solutions/healthcare#pricing-section)

Get started

Industry:

Healthcare

Company size:

Medium

Product:

Claude Platform

Partner:

AWS

Location:

North America

Up to 66% reduction

in time required for clinical data abstraction

+50% cost savings

on abstraction work while maintaining the industry's highest quality data

Advancing Claude in healthcare and the life sciences

Transform healthcare from insight to action

Read more

[Read more](../19-Reference/advancing-claude-in-healthcare-and-the-life-sciences-anthropic.md)

Read more

Advancing Claude in healthcare and the life sciences


Transform healthcare from insight to action

Video caption


Advancing Claude in healthcare and the life sciences

Transform healthcare from insight to action

Claude for Healthcare

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

Read more

[Read more](https://claude.com/healthcare)

Read more

Claude for Healthcare


Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

Video caption


Claude for Healthcare

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

[Prev](#)

Prev


[Carta Healthcare](https://www.carta.healthcare/) began with a simple frustration at Stanford Children’s Hospital: slow, manual data collection was holding back meaningful progress. That challenge sparked a new idea to pair AI with clinical expertise, to make clinical data abstraction faster, higher quality and lower cost, what Carta refers to as “hybrid intelligence.” 

## With Claude, Carta Healthcare:

- Reduces clinical data abstraction time by up to 66% while improving data quality
- Enabled processing of clinically complex questions that were previously impossible to automate
- Achieve 98-99% Inter-rater Reliability (IRR) scores, which is the healthcare industry's gold standard for data quality
- Transformed clinicians from manual data hunters into high-value validators and users of data to drive healthcare improvement

## The problem

Every day, hospitals generate mountains of clinical documentation, including physician notes, lab results, medication records, surgical reports, and more. Buried in these records are answers to critical questions that clinical registries need: Did this surgical patient develop an infection within 30 days? What was their BMI at admission? Were antibiotics administered within the correct window before incision? What was the door-to-balloon time?

Extracting these answers is called clinical data abstraction, and it is painstaking work. Trained abstractors spend, on average, one hour per case manually combing through clinical notes and documents, hunting for specific details buried in the electronic medical record. For complex cases, that time can stretch to five or six hours. A single health system might need to abstract more than 22,000 surgical cases per year, spending over 11,000 hours of labor annually.

But the challenge is not only the volume. Clinical documentation is messy, inconsistent, and often scattered across multiple systems and formats. Even within the same hospital, the “right answer” to a registry question may require interpretation, reconciliation of conflicting notes, and deep understanding of clinical intent. That complexity is why traditional automation attempts often fall short, and why purely manual workflows remain expensive and difficult to sustain.

“Hospital information systems are very complex and traditional data extraction and integration workflows inside hospitals are notoriously brittle, vary widely from system to system, and often break when electronic medical records are upgraded,” said Andrew Crowder, Vice President of Engineering and CISO at Carta Healthcare. “We needed an approach that insulated us from these inconsistencies and allowed us to deliver value without being tied to fragile, site-specific processes.”

## Choosing Claude

Security was the deciding factor in Carta Healthcare's model selection. Handling sensitive medical information, including protected health information, requires rigorous data privacy controls. Claude's availability in Amazon Bedrock provided the confidence Carta Healthcare needed with data privacy protections and assurance that customer data wouldn't be used for model training.

"While other models were available in Amazon Bedrock, no other model showed the capability for reasoning and understanding we found in Anthropic's models," said Crowder. "In addition, the published research on bias and model alignment has allowed us to pass rigorous hospital AI reviews."

That combination of security infrastructure, reasoning capability, and documented research on model alignment allowed Carta Healthcare to clear the high bar of hospital IT and AI review boards, a prerequisite for any system handling patient data.

## Building a clinical-grade AI system

Claude powers Carta Healthcare's Lighthouse platform, serving as the AI engine for clinical registry abstraction. Claude interprets both structured and unstructured medical data semantically, understanding the clinical context to formulate answers, provide justifications, and surface direct citations from medical records. The system can find evidence that's easy to miss in manual reviews, such as documentation buried deep in a chart or originating from encounters years earlier.

Carta Healthcare implemented a two-phase extraction pipeline. In the first phase, Claude Haiku 3.5 and Sonnet 4 extracted relevant information from medical documentation, processing both structured data and unstructured clinical notes. In the second phase, Claude Sonnet synthesized all extracted evidence to formulate suggested answers to registry questions, scoring and ranking the evidence. This approach improved accuracy and reduced the validation burden for abstractors. They now validate findings rather than hunt for them.

Because the system is built around Claude's ability to understand natural language, clinical experts can improve it directly. When abstractors notice an issue, the team adjusts prompts rather than rewriting code—changes that can be tested in production the same day. This keeps the people who understand clinical nuance in control of how the system behaves.

## The outcome

For one large health system abstracting over 22,000 surgical cases annually across 14 hospitals, the results were immediate. Time per case dropped from 30 minutes to 15-22 minutes for routine cases. For complex cases—the ones that used to consume five or six hours of an abstractor's day—time dropped to 90 minutes. Annual time savings reached between 3,667 and 6,050 hours, with Inter-rater Reliability consistently at 99%.

At a large multi-entity health system, manual abstraction for NSQIP cases was a constant strain. With over 22,000 cases annually across 14 hospitals, each taking about 30 minutes to abstract, the workload was immense leading to more than 11,000 hours of labor every year. The process was slow, expensive, and prone to human error. Before using Carta Healthcare’s Lighthouse platform, one experienced abstractor was quite skeptical of AI. She was experienced and clinically sharp, and worried that AI would not meet her expectations.

But she saw potential. She met with Carta Healthcare’s product team, shared detailed feedback, and worked closely with engineering to refine the platform. Her clinical expertise was critical—she knew when something didn’t look right, and her input helped shape Lighthouse into a tool she could rely on.

Today, she trusts Lighthouse completely. For complex cases, she even uses it as a second set of eyes, double-checking occurrences as well as catching subtle details like post-op medications that might otherwise slip through. As she puts it, “Lighthouse doesn’t replace my judgment, it enhances it.” The impact has been dramatic:

Selecting Claude as the core LLM has fundamentally changed Carta Healthcare's business model. By automating the cognitive work of abstracting unstructured clinical data, Claude and Lighthouse transformed the company's clinicians “from manual data hunters into high-value validators,” explained Crowder. Carta Healthcare reports 100% customer retention; 90% of customers also expand their engagement over time.

Looking ahead, Carta Healthcare plans to expand their AI capabilities to handle more complex registry scenarios, including cases with multiple procedures. "We are excited to grow both our usage of Anthropic's models." Crowder said. "We also look forward to expanding our technical relationship as we explore new possibilities with Claude."

“Carta Healthcare's implementation of Anthropic models via Amazon Bedrock has allowed for rapid and secure deployment of the newest models.”

Andrew Crowder

VP of Engineering, Carta Healthcare 

Livestream

Tune in to watch Anthropic CEO and Co-founder Dario Amodei share his vision for AI in healthcare and life sciences, along with an executive customer panel.

Livestream


Tune in to watch Anthropic CEO and Co-founder Dario Amodei share his vision for AI in healthcare and life sciences, along with an executive customer panel.

Video caption


Livestream

Tune in to watch Anthropic CEO and Co-founder Dario Amodei share his vision for AI in healthcare and life sciences, along with an executive customer panel.

[Prev](#)

Prev


## Related stories

[A conversation with Seth Hain about Epic’s internal AI adoption](/customers/epic-systems)

A conversation with Seth Hain about Epic’s internal AI adoption

A conversation with Seth Hain about Epic’s internal AI adoption

Customer story

[Customer story](/customers/epic-systems)

Customer story

[Medgate accelerates healthcare innovation with Claude Code](/customers/medgate)

Medgate accelerates healthcare innovation with Claude Code

Medgate accelerates healthcare innovation with Claude Code

Customer story

[Customer story](/customers/medgate)

Customer story

[Elation Health delivers faster clinical insights with Claude](/customers/elation-health)

Elation Health delivers faster clinical insights with Claude

Elation Health delivers faster clinical insights with Claude

Customer story

[Customer story](/customers/elation-health)

Customer story

[Qualified Health and the University of Texas System use Claude to identify patients who need life-saving care](/customers/qualified-health)

Qualified Health and the University of Texas System use Claude to identify patients who need life-saving care

Qualified Health and the University of Texas System use Claude to identify patients who need life-saving care

Customer story

[Customer story](/customers/qualified-health)

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
