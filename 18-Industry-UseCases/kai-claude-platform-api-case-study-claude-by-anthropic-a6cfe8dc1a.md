---
title: "Kai Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/kai"
category: "18-Industry-UseCases"
fetched_at: "2026-08-02T05:42:05Z"
tags: ["api"]
---

# Kai delivers preemptive exposure management with Claude


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Cybersecurity

Company size:

Startup

Product:

Claude Platform

Partner:

AWS

Location:

North America

99.5% of 2.5 million software composition analysis findings eliminated

as false positives, with true findings auto-remediated

Investigated and triaged 250 million vulnerabilities

surfaced by enterprise scanners in 20 hours, eliminating 83% as benign and triggering auto-remediation for the exploitable findings

AI has made attackers fast: the window between a vulnerability's discovery and its exploitation has shrunk from weeks to hours, and sometimes minutes. Defenders, meanwhile, face more findings than any human team can investigate.  [Kai](https://www.kai.security/) is a cybersecurity company with an AI-native platform for autonomous defense. Using Claude as the analysis layer, the platform autonomously investigates, triages, and remediates security findings across application security, enterprise and infrastructure.

## With Claude, Kai: 

- Investigated and triaged 250 million vulnerabilities surfaced by enterprise scanners in 20 hours, eliminating 83% as benign and triggering auto-remediation for the exploitable findings
- Eliminated 99.5% of false positives across 2.5 million findings from Software Composition Analysis (SCA) of 5,000 container images within one hour, saving 3 million hours annually
- Reduced zero-day and supply-chain attack response from days or weeks to a few minutes, with all affected assets identified, mitigation steps generated, and threat hunting launched autonomously 

## The challenge

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

Claude on Amazon Bedrock


Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.


Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

## A human-led process built for a threat environment that no longer exists 

Inside a large enterprise, security scanners never stop producing findings, and every finding waits on a human security team to investigate it. "A skilled security analyst can thoroughly investigate 10 to 20 vulnerabilities per day," said Damiano Bolzoni, Kai's co-founder and CTO. "Our customers were sitting on millions of findings." AI-enabled attackers are moving faster than human defenders can resolve their backlog, creating an exploitable time gap that is structurally impossible to close with human-led workflows alone. 

The industry's answer to that backlog is Continuous Threat Exposure Management, or CTEM, a process of identifying, prioritizing, validating, and remediating exposures. The process was designed to close the gap, but was also designed to be executed by humans. Every phase that depends on human investigation or coordination becomes a bottleneck. The vulnerability stays exploitable for as long as the cycle is stalled, and a process measured in weeks never catches up to attackers who move in hours.

Kai's goal was to run every phase of that cycle autonomously, as fast as attackers move and as accurately as a senior analyst. The obstacle was distilling intelligence from unstructured data at scale. That intelligence informs how inputs are selected and enriched, how context is gathered and applied across millions of findings, and how outputs translate directly into remediation plans and mitigating detection rules. Kai needed a model that could produce analyst-grade intelligence from that data, across millions of signals, without sacrificing the accuracy that makes the output actionable. 

## The solution

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

Choosing the right Claude model


Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.


Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## Selecting Claude as the analysis layer 

Kai's founding bet was that defending against AI-enabled attacks required collapsing and replacing the fragmented stack of security tools rather than adding AI on top of it. "When the foundation is fragmented, AI makes fragments faster," Bolzoni explained. "It does not close the gaps between them." 

Many security platforms carry the weight of architecture decisions made before the AI era. "For us, there was no before," Bolzoni said. "Kai was conceived and built at a moment when Claude and frontier models already existed." 

That put the weight on model selection. At Kai's scale a single model error does not stay contained; it propagates through the pipeline, leaving a real vulnerability unremediated or an asset misattributed. The bar, Bolzoni added, was commercial as much as technical: “The CISOs we spoke with were not going to act autonomously on findings from a system that could not function at the level of their best analysts,” Bolzoni said.

To find the right model, the team ran side-by-side tests against representative CTEM tasks, measuring extraction accuracy, schema compliance, hallucination rate, latency, cost, and how much human cleanup each result required. “What stood out about Claude was its consistency,” Bolzoni said. "The combination of analysis, depth, and instruction-following held up across the volume and variety of inputs our customers bring to the platform every day." 

Trust shaped the access path as much as the model choice. Kai builds for Fortune 500 and Global 2000 enterprises, and the vulnerability data, asset metadata, and environment context those customers put into the platform come with hard requirements about where it goes and who can access it. "For a security platform handling sensitive data at the scale Kai handles it, the access path to the model is not an implementation detail," Bolzoni noted. "It is a security decision in its own right." Kai's decision was Amazon Bedrock. 

"Bedrock gave us the access controls, monitoring, and compliance framework that made autonomous execution at enterprise scale something our customers could approve, not just evaluate," Bolzoni said. The setup paid off in the evaluation itself: with identity, access control, and logging patterns already in place, the team spent its time testing model quality against real workflows rather than on procurement and security setup. Consolidation mattered too. "Using fewer vendors means leaner infrastructure and tighter control over how customer data is handled," he added. 

## An AI-native platform for autonomous defense 

Kai built an AI-native platform to run the entire exposure management cycle. The platform autonomously pulls from scanners, logs, asset inventories, and threat feeds, and multiple investigative agents correlate that data, separating true exposures from noise. Kai then scores severity in the context of the environment, assessing network reachability, vulnerability chaining, and real-world exploitability so the issues that matter surface first. Validated exposures get remediation plans routed to the responsible owner, with ticketing and verification built into the pipeline. 

At the core of the architecture is a harness: a layer of deterministic algorithms that ingests, cleanses, deduplicates, validates, and chunks raw security data before any of it reaches the model. Claude then analyzes inconsistent findings and extracts insights from unstructured data. Kai routes that work across Claude Sonnet and Opus models, applying the one best suited to each task. "We implemented Claude, and LLMs in general, as a fully autonomous system rather than as a chatbot," Bolzoni said. "That allowed us to use LLMs in sensitive and complex workflows while keeping control, auditability, and reliability."  

"Amazon Bedrock gave us the access controls, monitoring, and compliance framework."

Damiano Bolzoni

Co-founder and CTO, Kai


## The outcome

## Preemptive exposure management 

For one Global 1000 company, the numbers were straightforward: Kai processed 2.5 million Software Composition Analysis (SCA) findings from 5,000 images in under an hour with 99.5% eliminated as false positives. The triage work Kai absorbed saved roughly 3 million engineering and security hours annually. When threat intelligence identified a new supply chain attack, Kai delivered a remediation solution within minutes.

The remediation side is where Kai’s ability to preempt attacks becomes concrete for engineers. For validated findings, Kai generates least-invasive auto-remediation, resolving dependencies upstream and downstream so a fix would not introduce a breaking change. "Engineers do not receive a vulnerability report and a problem to solve," Bolzoni said. "For AppSec findings, they receive commit-ready fixes with the dependency analysis already done. What remained was the work that actually requires human judgment." 

## Looking ahead 

Kai's architecture is designed so that as frontier models advance, its capabilities advance with them. “Kai's roadmap expands autonomous defense beyond the CTEM cycle, into domains where the intelligence Kai has already built creates a direct path to deeper, more specialized coverage,” said Galina Antova, co-founder and CEO. "Frontier model advances are accelerating what is possible faster than we anticipated when we started building."

"What stood out about Claude was its consistency. The combination of analysis, depth, and instruction-following held up."

Damiano Bolzoni

Co-founder and CTO, Kai

## Related stories

[How Artemis helps security teams cut incident resolution time by 96%](/customers/artemis)

How Artemis helps security teams cut incident resolution time by 96%

How Artemis helps security teams cut incident resolution time by 96%

Customer story

[Customer story](/customers/artemis)

Customer story

[Cogent resolves security threats 97% faster with Claude](/customers/cogent)

Cogent resolves security threats 97% faster with Claude

Cogent resolves security threats 97% faster with Claude

Customer story

[Customer story](/customers/cogent)

Customer story

[How eSentire runs expert-level threat investigations at scale with Claude](/customers/esentire)

How eSentire runs expert-level threat investigations at scale with Claude

How eSentire runs expert-level threat investigations at scale with Claude

Customer story

[Customer story](/customers/esentire)

Customer story

[Vanta streamlines compliance remediation with Claude](/customers/vanta)

Vanta streamlines compliance remediation with Claude

Vanta streamlines compliance remediation with Claude

Customer story

[Customer story](/customers/vanta)

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
