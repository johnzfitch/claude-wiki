---
title: "Semgrep Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/semgrep"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:48Z"
tags: ["api", "bedrock", "case-studies", "enterprise", "mcp", "security"]
---

# How Semgrep delivers AI-powered code security with Claude in Amazon Bedrock

[Try Claude](https://claude.ai)

Industry:  
Cybersecurity

Company size:  
Small

Product:  
Claude Platform

Location:  
North America

20% reduction

in false positive security alerts

92% user agree

rate on safe-to-ignore labeling

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

## Related stories


### Vega's cyber defense platform returns 67% of analysts' time with Claude


### Cyera on making Claude Cowork the front door to 40 tools


### Cyera scales agentic AI across 1,500 employees with Claude Enterprise


### Kai delivers preemptive exposure management with Claude

[](https://www.claude.com/)

© 2026 Anthropic PBC

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
- [Security and compliance](https://trust.anthropic.com/)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

## Company

- [Anthropic](https://www.anthropic.com/)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Research](../19-Reference/anthropic-com-research.md)
- [Anthropic news](../19-Reference/news.md)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](../19-Reference/announcing-our-updated-responsible-scaling-policy.md)
- [Transparency](https://anthropic.com/transparency)

## Terms and policies

- Privacy choices
- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Terms of Service: US K-12](https://anthropic.com/legal/k12-terms)
- [Data Processing Agreement: US K-12](https://anthropic.com/legal/k12-dpa)
- [Usage Policy](https://www.anthropic.com/legal/aup)

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Download app](https://www.claude.com/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](https://www.claude.com/features/artifacts)
- [Design](../15-Claude-AI-Features/product-design.md)
- [Connectors](https://www.claude.com/marketplace/connectors-plugins)
- [Plugins](https://www.claude.com/marketplace/plugins)
- [Skills](https://www.claude.com/skills)

## Extensions

- [Claude in Chrome](https://www.claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://www.claude.com/claude-for-microsoft-365)

## Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

## Enterprise

- [Overview](enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

## Developers

- [Developer docs](../02-Claude-Code-CLI/code-home.md)
- [Developer blog](https://claude.dev)
- [Community](https://www.claude.com/community)
- [Console](../04-API-Reference/Other/home.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](https://www.claude.com/platform/api)
- [Marketplace](https://www.claude.com/marketplace)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)

## Resources

- [Blog](https://www.claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](customers.md)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](https://www.claude.com/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](https://www.claude.com/check-files)
- [Regional compliance](https://www.claude.com/regional-compliance)
- [Report abuse](https://www.claude.com/form/anthropic-content-reporting)
