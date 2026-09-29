---
title: "eSentire Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/esentire"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:02Z"
tags: ["agents", "api", "enterprise", "security"]
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

[](/)

© 2026 Anthropic PBC

## Products

- [Claude](/product/overview)
- [Claude Code](/product/claude-code)
- [Claude Cowork](/product/cowork)
- [@Claude](/product/tag)
- [Claude Science](/product/claude-science)
- [Claude Security](/product/claude-security)
- [Download app](/download)
- [Pricing](/pricing)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](/features/artifacts)
- [Design](/product/design)
- [Connectors](/marketplace/connectors-plugins)
- [Plugins](/marketplace/plugins)
- [Skills](/skills)

## Extensions

- [Claude in Chrome](/claude-in-chrome)
- [Claude for Microsoft 365](/claude-for-microsoft-365)

## Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

## Enterprise

- [Overview](/solutions/enterprise)
- [Claude Code for Enterprise](/product/claude-code/enterprise)

## Departments

- [Customer support](/solutions/customer-support)
- [Cybersecurity](/solutions/cybersecurity)
- [Legal](/solutions/legal)
- [Sales](/solutions/sales)

## Industries

- [Financial services](/solutions/financial-services)
- [Government](/solutions/government)
- [Healthcare](/solutions/healthcare)
- [Higher education](/solutions/education)
- [K-12 teachers](/solutions/teachers)
- [Life sciences](/solutions/life-sciences)
- [Nonprofits](/solutions/nonprofits)
- [Small business](/solutions/small-business)

## Programs

- [Startups](/programs/startups)
- [Scientists](/programs/team-plan-for-scientists)

## Developers

- [Developer docs](https://code.claude.com/docs/en/overview)
- [Developer blog](https://claude.dev)
- [Community](/community)
- [Console](https://platform.claude.com/docs/en/home)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](/platform/api)
- [Marketplace](/marketplace)
- [Claude on AWS](/partners/claude-on-aws)
- [Google Cloud](/partners/google-cloud)
- [Microsoft Foundry](/partners/microsoft-foundry)

## Resources

- [Blog](/blog)
- [Claude partner network](/partners)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](/customers)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](/partners/powered-by-claude)
- [Service partners](/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](/check-files)
- [Regional compliance](/regional-compliance)
- [Report abuse](/form/anthropic-content-reporting)
- [Security and compliance](https://trust.anthropic.com/)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

## Company

- [Anthropic](https://www.anthropic.com/)
- [Careers](https://www.anthropic.com/careers)
- [Policy](https://www.anthropic.com/policy)
- [Research](https://www.anthropic.com/research)
- [Anthropic news](https://www.anthropic.com/news)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
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

- [Claude](/product/overview)
- [Claude Code](/product/claude-code)
- [Claude Cowork](/product/cowork)
- [@Claude](/product/tag)
- [Claude Science](/product/claude-science)
- [Claude Security](/product/claude-security)
- [Download app](/download)
- [Pricing](/pricing)
- [Log in](https://claude.ai/login)

## Capabilities

- [Artifacts](/features/artifacts)
- [Design](/product/design)
- [Connectors](/marketplace/connectors-plugins)
- [Plugins](/marketplace/plugins)
- [Skills](/skills)

## Extensions

- [Claude in Chrome](/claude-in-chrome)
- [Claude for Microsoft 365](/claude-for-microsoft-365)

## Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

## Enterprise

- [Overview](/solutions/enterprise)
- [Claude Code for Enterprise](/product/claude-code/enterprise)

## Departments

- [Customer support](/solutions/customer-support)
- [Cybersecurity](/solutions/cybersecurity)
- [Legal](/solutions/legal)
- [Sales](/solutions/sales)

## Industries

- [Financial services](/solutions/financial-services)
- [Government](/solutions/government)
- [Healthcare](/solutions/healthcare)
- [Higher education](/solutions/education)
- [K-12 teachers](/solutions/teachers)
- [Life sciences](/solutions/life-sciences)
- [Nonprofits](/solutions/nonprofits)
- [Small business](/solutions/small-business)

## Programs

- [Startups](/programs/startups)
- [Scientists](/programs/team-plan-for-scientists)

## Developers

- [Developer docs](https://code.claude.com/docs/en/overview)
- [Developer blog](https://claude.dev)
- [Community](/community)
- [Console](https://platform.claude.com/docs/en/home)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)

## Platform

- [Overview](/platform/api)
- [Marketplace](/marketplace)
- [Claude on AWS](/partners/claude-on-aws)
- [Google Cloud](/partners/google-cloud)
- [Microsoft Foundry](/partners/microsoft-foundry)

## Resources

- [Blog](/blog)
- [Claude partner network](/partners)
- [Claude Academy](https://academy.claude.com/)
- [Customer stories](/customers)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](/partners/powered-by-claude)
- [Service partners](/marketplace/service-partners)

## Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Check files](/check-files)
- [Regional compliance](/regional-compliance)
- [Report abuse](/form/anthropic-content-reporting)
