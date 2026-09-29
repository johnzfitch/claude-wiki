---
title: "Cogent Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/cogent"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:32Z"
tags: ["agents", "api", "enterprise", "security"]
---

# Cogent resolves security threats 97% faster with Claude

[Try Claude](https://claude.ai)

Industry:  
Cybersecurity

Company size:  
Startup

Product:  
Claude Platform

Location:  
North America

97% reduction in time critical vulnerabilities remain open

Exposure-to-remediation compressed from days or weeks to minutes

Response time to zero-day vulnerabilities reduced to 30 minutes

Down from days of manual investigation and coordination

Cogent is an applied AI lab building agents to automate critical security tasks for Fortune 1000 enterprises. Where many security tools focus on finding vulnerabilities, Cogent focuses on fixing them. Cogent automates investigation, prioritization, and remediation across the full vulnerability lifecycle.

## With Claude, Cogent achieved:

- 97% reduction in time that critical vulnerabilities remain open, compressing remediation cycles from days or weeks to minutes
- Response time to zero-day vulnerabilities reduced to 30 minutes, down from days of manual investigation and coordination
- 90% reduction in vulnerability noise requiring human review
- Reduced average investigation time from days to minutes
- 40+ hours per month reclaimed from manual reporting per enterprise customer

## The challenge

## The gap between finding and fixing

Security teams at large enterprises are generally effective at discovering vulnerabilities: scanners can surface thousands of findings daily. The hard part is the tedious, time consuming work that comes after that: determining which ones actually matter, who owns the fix, and what the exact remediation steps are. Those answers require pulling data across scanners, endpoint detection tools, asset inventories, threat intelligence feeds, and configuration databases, then synthesizing it manually.

The work is slow and often inconsistent. High-severity vulnerabilities can sit open for days or weeks. “AI has shifted the balance of power in cybersecurity,” said Geng Sng, Cogent's CTO. “Attackers now automate most of the attack lifecycle, compressing what once took weeks into hours. Meanwhile, defenders still rely on fragmented tools and manual coordination.” Cogent's founders wanted to build a system that could do this work continuously and at machine speed, across the full vulnerability lifecycle.

97%

Reduction in time that critical vulnerabilities remain open

## The solution

## Cogent selects Claude for agentic reliability

Cogent evaluated multiple model providers using internal security-focused benchmarks. The decisive factor was performance on complex, multi-step agentic workflows.

In vulnerability investigation, an agent needs to follow a chain of evidence across disparate systems without losing the thread: a vulnerability surfaces in a scanner, which points to a specific software version, which maps to a set of assets, which have varying levels of exposure depending on compensating controls. In workflows involving 10-15 sequential tool calls, Claude maintained coherence and instruction-following where alternatives lost context.

That reliability made Claude Opus and Haiku models the clear choice for production deployment in enterprise security environments, where incomplete reasoning has real consequences.

"Claude consistently performed best on complex, agentic workflows, especially multi-step investigations requiring policy adherence and sustained reasoning across multiple tools," said Anirudh Ravula, Cogent's Head of AI.

30 minutes

Response time to zero-day vulnerabilities

## The outcome

## How Cogent uses Claude across the vulnerability lifecycle

Fixing a vulnerability requires three things to go right in sequence: understanding what’s actually exploitable, deciding which issues deserve immediate attention, and actually resolving them. Most security teams do all three manually. Cogent automates the full chain by building the end-to-end remediation stack then embedding Claude as the reasoning layer at each step.

**Investigation:** Cogent's platform continuously pulls from scanners, logs, asset inventories, and threat feeds, building the environmental context that doesn't exist anywhere in a customer's environment ready-made. From there, Cogent's investigative agent works autonomously: tracing asset ownership across systems, synthesizing threat intelligence and business context into a risk score, and mapping the remediation processes that apply to each asset. For issues that warrant deeper analysis, security teams can ask questions in plain language and get back clear, explainable findings. Investigations that once took days now happen in minutes.

**Prioritization:** A large enterprise typically faces millions of vulnerability-asset combinations at any given time. Traditional risk scoring treats them uniformly, assigning severity based on the vulnerability itself rather than the environment it lives in. Cogent's agents assess real-world exploitability, how critical the affected asset is to the business, whether it's exposed to the internet, and what compensating controls are already in place. The result is a ranked list that reflects actual business risk, not a generic severity label. False positives drop; the issues that truly matter surface.

**Remediation:** Once vulnerabilities are prioritized, Cogent's agents generate action plans, identify the responsible owner, and draft implementation steps. Cogent is advancing toward fully autonomous remediation: agents that execute fixes directly within defined guardrails, with verification loops and policy controls at each step.

The results are measurable. Customers have reduced the time critical vulnerabilities remain open by 97%. Response time to zero-day vulnerabilities has dropped to 30 minutes. Vulnerability noise requiring human review has fallen by 90%, freeing security teams to focus on findings that genuinely require attention. Individual analysts have reclaimed more than 40 hours per month previously consumed by manual reporting.

One enterprise customer at a large hospitality brand put it simply: "In meetings, I used to say 'I'll get back to you on that' and spend hours in BI tools and Excel. Now I ask Cogent in plain language and generate charts in seconds. Executive questions get answered in real time, not days later."

Claude is also embedded in how Cogent builds its own product. The team developed an AI-driven software development lifecycle, integrating Claude into engineering workflows from specification through implementation and review. Smaller teams can now move faster and maintain the high security standards their enterprise customers require.

## Looking ahead: Fully autonomous systems

Cogent is working toward two capabilities next: fully autonomous remediation, where systems identify and fix vulnerabilities with minimal intervention, and offensive security simulation, where agents replicate attacker behavior.

“We are exploring Claude-powered agents that simulate sophisticated attackers, chaining misconfigurations and privilege escalations to uncover attack paths before adversaries do,” said CTO Geng Sng. “Our goal is fully autonomous systems, reducing millions of exploitable issues toward zero.”

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
