---
category: "15-Claude-AI-Features"
fetched_at: "2026-03-17T10:27:33Z"
last_modified: "Tue, 17 Mar 2026 04:11:45 GMT"
source_url: "https://www.claude.com/customers/semgrep"
title: "Customer story | Semgrep | Claude"
---

# How Semgrep delivers AI-powered code security with Claude in Amazon Bedrock


[Try Claude](https://claude.ai)


[Contact sales](/contact-sales)


Industry:

Cybersecurity

Company size:

Small

Product:

Claude Platform

Partner:

Location:

North America

20% reduction

in false positive security alerts

92% user agree

rate on safe-to-ignore labeling

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


Semgrep, a leading cyber security company, leverages Claude in Amazon Bedrock to power many of its AI-assisted features for customers, helping developers detect, filter, and fix code vulnerabilities more effectively—while minimizing false positives that waste engineering time.

With Claude, Semgrep:

- Confidently labels 20% of security findings as safe to ignore, with a 92% user agree rate and 96% security researcher agree rate
- Achieved 16% higher accuracy identifying false positives than a prior version powered by GPT-4o
- Delivered 17% better performance in component tagging (compared to their previous model, GPT-4o)
- Processes and analyzes thousands of security findings for customers daily

## How Semgrep is solving security's false positive problem

Software development teams face an overwhelming volume of security alerts, many of which are false positives that consume valuable time and resources. "Security tools are notorious for generating high volumes of alerts. This is a widespread problem across the industry," said Bence Nagy, Staff Engineer at Semgrep.

Semgrep recognized this pain point and saw an opportunity to apply AI to dramatically reduce alert noise.

Semgrep's fast, deterministic code analysis engine and LLM-friendly rule syntax made it the perfect foundation for AI-powered AppSec—retaining the benefits of precise pattern matching while taking advantage of AI’s ability to understand code context.

Nagy explained their first breakthrough with a practical example: "We tested if an AI model could distinguish between actual leaked passwords in code versus harmless placeholders like 'password=REPLACE_PASSWORD_HERE'.”

Traditional security tools blindly flag both as vulnerabilities, but we discovered that AI could accurately determine which alerts represented genuine security risks and which were false alarms. This initial success proved AI could solve a fundamental problem in security scanning—distinguishing real threats from noise—prompting Semgrep to explore how AI could transform their entire security platform to help teams focus exclusively on legitimate security issues.

## Choosing the best model for every task

Semgrep’s AI features rely on a variety of prompt chains and evaluation loops that reference both project-specific inputs (dependencies, prior fixes, dataflow traces) and inputs from Semgrep’s non-AI analyses.

To compare how different models perform on these prompt chains, Semgrep relies on a rigorous evaluation process that ensures they are always using the best LLM across a multitude of security tasks—from filtering false positives to generating accurate remediation guidance.

“Our goal is to make sure developers only see the security issues that matter. We benchmark models against real-world data, constantly monitor performance across over 1000+ customers and let the results guide us,” said Bence Nagy, Staff Engineer at Semgrep.

Claude was unique in that it was a top performing model (top 3) across every single one of Semgrep’s unique, task-specific evals.

"Claude 3.7 Sonnet demonstrated remarkable code analysis capabilities with deeper contextual understanding," said Nagy. "It was the only model that recognized a vulnerability in an auto-generated file, advising developers to fix the generating source rather than editing the output file directly."

In two of the most important evals, false positive detection and component tagging, Claude outperformed GPT-4o, the previous top performing model, by 16% and 17% respectively.

“Operating at the application layer, we see model benchmarking and selection as our responsibility—not the customer’s. While anyone can request the use of a specific model, customers generally trust us to optimize and choose for them on a per-task basis,” said Chushi Li, Product Marketing Manager at Semgrep.

## Claude enhances Semgrep’s security capabilities

Semgrep uses a variety of large language models—including Claude—to power features that help security teams cut noise, automate routine tasks, and generate fixes:

- **Noise filtering:** Analyze security alerts to separate true issues from false positives, reducing alert volume by 20% out of the box, and up to 40% over time.
- **Memories:** Learns and stores critical, security-relevant context about an environment as users triage findings and fix issues, eliminating future false positives.
- **Autofix + Remediation guidance:** Suggest one-click code fixes to remediate vulnerabilities, and give developers the context they need to understand and feel confident merging the changes.
- **Breaking change analysis:** Analyze dependency upgrades for breaking changes, and automatically create upgrade PRs that tell developers if the version bump is safe or if they need to refactor.
- **File sensitivity classification:** Assess the criticality of files, elevating issues in high-risk components like auth or payments over low-risk ones.
- **Rule-writing:** Write deterministic Semgrep rules based on instructions in natural language

## One of the security tools that developers don’t mind

Semgrep's AI-powered features have improved productivity for security and development teams, and extend beyond noise reduction. Claude's contextual understanding also helps developers implement more comprehensive fixes. "Claude provides additional detail on what developers need to check after implementing a fix and how to adapt other parts of their project," said Nagy. This approach prevents the common problem where fixing a vulnerability breaks existing functionality.

Semgrep's benchmarking approach ensures optimal AI performance for each security task. Nagy explained, "For our noise filtering feature, we've built evaluation suites containing thousands of pre-classified security findings to measure accuracy precisely."

This testing revealed important insights about model configuration, including a counterintuitive discovery: "We found that giving Claude more tokens for 'thinking' actually made it overly cautious about security issues, becoming too conservative in its assessments." These insights allow Semgrep to fine-tune Claude's parameters for security tasks, maximizing its effectiveness for real-world operations.

## Claude in Amazon Bedrock: Enterprise security, privacy, and performance

Semgrep frequently works with customers in industries with strict data governance requirements. [Amazon Bedrock](https://aws.amazon.com/bedrock/) provides a secure way to access powerful foundation models like Claude within private environments, such as an organization’s Amazon Virtual Private Cloud (VPC).

“Security and privacy are non-negotiable for us and our customers,” said Drew Dennison, Semgrep co-founder. “The ability to access Claude through Amazon Bedrock—within a secure, compliant setup—gives us the flexibility we need without compromising on performance.”

This availability makes Claude a compelling choice—not just for its technical excellence, but for how seamlessly it fits into real-world enterprise environments.

## MCP and the future of AI-powered development

Semgrep envisions a future where AI both creates and secures software. "As software development becomes more accessible, less experienced engineers will generate more AI-written code. How do we keep that code secure?" asked Dennison. "We need security tools embedded directly in the AI's generation process, plus verification systems to audit code in the chain of thought."

This vision drove Semgrep to develop an open-source Model Context Protocol (MCP) tool that enables AI assistants like Claude to scan their generated code for vulnerabilities before delivering it. Since Semgrep’s core SAST engine is fast, transparent, and source-based, an MCP server makes it possible for LLMs to dynamically call Semgrep as a tool. Nagy said, "We want to create a world where you can build an entire project with AI and be confident it's secure and functional."

The company is also developing organizational memory features to enhance contextual security. "We're building systems that learn from developer comments and decisions to understand non-obvious facts about a codebase," explained Nagy. By capturing this institutional knowledge, security assessments become more intelligent over time.

Through these innovations, Semgrep aims to ensure AI accelerates development while maintaining security—benefiting the entire software industry with both speed and safety.


Video caption


[Prev](#)

Prev


## Related stories

[eSentire scales elite cybersecurity expertise with Claude in Amazon Bedrock](/customers/esentire)

eSentire scales elite cybersecurity expertise with Claude in Amazon Bedrock

eSentire scales elite cybersecurity expertise with Claude in Amazon Bedrock

Customer story

[Customer story](/customers/esentire)

Customer story

[Vanta streamlines compliance remediation with Claude](/customers/vanta)

Vanta streamlines compliance remediation with Claude

Vanta streamlines compliance remediation with Claude

Customer story

[Customer story](/customers/vanta)

Customer story

[Trellix deploys autonomous security agents with Claude in Amazon Bedrock](/customers/trellix)

Trellix deploys autonomous security agents with Claude in Amazon Bedrock

Trellix deploys autonomous security agents with Claude in Amazon Bedrock

Customer story

[Customer story](/customers/trellix)

Customer story

[Panther launches AI security teams can trust, powered by Claude in Amazon Bedrock](/customers/panther)

Panther launches AI security teams can trust, powered by Claude in Amazon Bedrock

Panther launches AI security teams can trust, powered by Claude in Amazon Bedrock

Customer story

[Customer story](/customers/panther)

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
