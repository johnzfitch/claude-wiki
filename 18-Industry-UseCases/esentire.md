---
title: "eSentire Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/esentire"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:45Z"
tags: ["agents", "api", "case-studies", "enterprise", "security"]
---

# How eSentire runs expert-level threat investigations at scale with Claude

[Try Claude](https://claude.ai)

Industry:  
Cybersecurity

Company size:  
Medium

Product:  
Claude Platform

Partner:  
AWS

Location:  
North America

99.96% ransomware containment before encryption

more than double the industry average of 44%

120,000+ autonomous investigations in 12 months

each averaging 44 tool calls across endpoint, identity, network, and cloud telemetry

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

eSentire is a managed detection and response (MDR) provider that protects millions of endpoints across thousands of customers worldwide. Its Atlas platform uses Claude to run autonomous threat investigations, analyzing signals across endpoint, identity, network, and cloud telemetry to catch and contain attacks in minutes.

## With Claude, eSentire achieved:

- 99.96% ransomware containment before any file encryption, more than double the industry average of 44%
- Over 120,000 autonomous investigations across its full customer base in 12 months, each averaging 44 tool calls across endpoint, identity, network, and cloud telemetry
- Above 90% alignment with top SOC experts in continuous production evaluation, matching or exceeding human analyst performance
- 6-minute average agentic investigation, where the industry median attacker dwell time is 11 days
- 41% more confirmed attacks detected per customer after deploying agentic investigations, with overall alert volume down 11%

## The challenge: Matching attacker speed without sacrificing depth

AI-powered attacks now run at thousands of requests per second, a pace no human SOC team can match. eSentire needed to investigate live threats across thousands of heterogeneous customer environments, correlating signals across endpoint, identity, network, and cloud layers, and reasoning about attacker intent with incomplete information. The challenge was doing this with the same depth a senior analyst would bring to every signal, not just the ones flagged as critical.

"When attackers can run AI agents that move faster than any human SOC, the only viable response is AI that defends at the same speed and depth," said Dustin Hillard, CPTO of eSentire. "That's what we built on Claude."

## The solution: Why eSentire chose Claude for security reasoning

Standard cybersecurity benchmarks had become saturated, with leading models scoring near-perfect, but those benchmarks present defined problems with verifiable answers. eSentire's production work is fundamentally different: the agent receives a detection event and telemetry sources, but no predefined answer, and has to decide what tools to call, how to interpret contradictory evidence, and what verdict to reach.

When eSentire evaluated multiple models across real-world security scenarios, Claude provided the highest performance for complex security reasoning. Its agentic capabilities excelled at orchestrating multi-tool workflows while maintaining investigative coherence, essential for MDR work, and each successive model generation has improved on that.

"Benchmarks measure whether a model can solve a known problem in a controlled environment," said Hillard. "We needed Claude to solve unknown problems in live customer environments, thousands of times a day, with expert-level depth on every single one. That's a fundamentally different challenge, and Opus 4.6 is meeting it."

## How eSentire runs agentic investigations with Claude

eSentire's Atlas platform runs Claude Opus 4.6 on Amazon Bedrock through Agent SDK in a multi-agent architecture that mirrors the workflow of a senior SOC analyst. Each investigation averages 44 autonomous tool calls: querying threat intelligence, correlating signals across SIEM and endpoint telemetry, analyzing identity activity, reconstructing attacker behavior across process and network data, and connecting findings across workflows. Over 12 months, the platform executed more than 5 million tool calls, representing 468,000 hours of equivalent expert effort, with each call averaging roughly 5 minutes of analyst work.

Each case follows a structured analytical workflow that would take a senior analyst hours to replicate manually, with multiple sub-agents collaborating on each case.

Where this shows up most clearly is in ambiguous cases. An identity compromise where the attacker's activity overlaps with a legitimate user's normal behavior requires the agent to weigh timing, geography, user agent strings, and email forwarding rules before making a judgment call. Opus 4.6 consistently handles these cases at a level that matches eSentire's best human investigators. And it has to reason effectively across 3,600+ distinct investigation workflows spanning every major EDR, SIEM, and identity platform.

After deploying agentic analysis, eSentire detected 41% more confirmed attacks per customer while reducing overall alert volume by 11%. More real threats caught, less noise. Senior analysts review and act on every critical finding, providing a trust layer that automation alone doesn't provide. The AI analyzes at depth on every signal, freeing the human team to focus on the judgment calls that matter most: customer engagement, containment decisions, and remediation strategy.

"Before agentic investigations, we had to choose between depth and speed," said Hillard. "Now every investigation gets the deep analytical rigor our best experts would apply. That's what changes outcomes."

## The outcome: Measurable containment at production scale

eSentire measures this rigor through continuous production evaluation: senior SOC experts independently review a sample of the same cases the agent has investigated, and alignment is measured across dimensions like whether compromise occurred, severity classification, and recommended response. Across more than 500 adjudicated outcomes, Claude consistently achieves above 90% alignment with senior experts on the final verdict. When compared against junior analysts using the same methodology, the agent outperforms them.

Across 12 months of production, the results are concrete. Of nearly 10,000 escalated incidents across more than 1,400 customers:

- 31% were blocked before execution,
- 18% were attempted attacks that failed,
- 36% were identity compromises detected and remediated before attackers accessed business data, and
- 14% were device compromises where the SOC detected activity, isolated the host, and drove remediation.

Across nearly two million protected endpoints, attackers achieved lateral movement to a second device in fewer than 0.5% of incidents. Ransomware encrypted files in less than 0.04%. Every one of those cases was detected. The question was never whether the attack was found, but how fast it could be stopped. For context, the global median attacker dwell time is 11 days, and only 44% of ransomware attacks industry-wide are stopped before encryption.

## Looking ahead

The platform is expanding to ingest and respond across any security technology a customer runs, regardless of vendor stack. Each new integration deepens both the investigative context and the response capabilities available to every investigation.

"We're building a platform where every security signal, regardless of vendor, gets the same depth of analysis and quality of outcome," Hillard said. As the threat landscape accelerates, eSentire's bet is that depth and speed aren't a tradeoff anymore.


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
