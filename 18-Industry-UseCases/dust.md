---
title: "Dust Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/dust"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:44Z"
tags: ["agents", "api", "case-studies", "enterprise", "prompting", "security"]
---

# Dust enables agents to go deeper at lower cost with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
[Claude Platform](https://claude.com/platform/api)[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)

Location:  
Europe

\$10k/day saved

on model spend after optimizing prompt caching

8+ tool-calling steps per agent run

up from 4–5, with no engineering changes needed

[Dust](https://dust.tt/) is a multiplayer AI platform for human-agent collaboration. It gives companies a shared workspace where teams can build, deploy, and manage model-agnostic AI agents connected to their company knowledge, tools, and workflows. The agents read from a company's stack and write back to it: updating the CRM, drafting the report, or kicking off the workflow, without writing code. Teams at companies like Datadog, Vanta, and 1Password use Dust and together have deployed more than 300,000 agents.

## With Claude, Dust achieved:

- An 18% reduction in overall model spend, roughly \$10K per day, after optimizing prompt caching
- Increased cache reads from 30% to 65% of input tokens, cutting input spend by 22%
- An increase in autonomous tool-calling depth from 4–5 to 8+ steps per agent run, with no engineering changes
- A redesigned execution loop supporting up to 24 tool calls per run
- Deep Research workflows, orchestrated by Claude, that run for 10+ minutes across data warehouses, the web, and internal sources
- A standard integration layer built on Model Context Protocol (MCP), with Dust operating as both client and server

## The challenge

## Agents enterprise teams trust with real work

Dust's premise is that the people who build the most useful AI agents are the ones closest to the work. That includes the RevOps lead automating deal prep, the chief of staff rebuilding onboarding, or the support manager who turns ticket routing into a system. Dust calls them AI operators. "They're not always engineers,” said Stanislas Polu, co-founder and CTO of Dust. “They're the people who understand the work deeply enough to build the systems that automate it."

For that premise to hold, the agents those operators build must be able to act reliably across a company's systems. What makes this possible is the model behind them. As Polu put it: "You can't save time with AI you don't trust. Our goal was to make AI agents accurate and capable enough that enterprise teams trust them to do real work, not just answer questions."

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/claude-com-product-claude-code.md)

## The solution

## Choosing the model agents could trust

Dust allows customers to pick the model behind any Dust agent from a dropdown menu, with no code changes required. In those comparisons, one pattern held, Paul said: “Claude consistently stood out on the criteria that matter most: instruction-following, nuanced writing, and reliable tool use.”

The difference showed up most clearly in autonomous research. As Claude's agentic capabilities improved, the number of sources it consulted for a single research task grew from five to fourteen. "The new Claude models didn't just answer the question; it proactively explored adjacent information and synthesized across sources," Polu noted. "That behavior is exactly what enterprise agents need."

## Complex workflows with optimized prompt caching

Dust provides the orchestration, trust, and enterprise infrastructure around models like Claude. This includes an LLM picker and soon an automatic router, a retrieval pipeline connecting more than 100 data sources, a framework for delegating work across sub-agents, and the no-code agent builder itself. It also includes robust governance to control how Dust agents operate across a company’s systems: permission-aware retrieval, role-based access, and audit logs keep each agent within the data and tools its user is cleared for. Each model, including Claude, gets its own prompting and context strategy beneath the interface, so more capable models never translate into added complexity for users.

Earlier models produced truncated or unreliable results past a handful of tool calls; once Claude could chain many steps accurately, Dust raised the limit. "Our existing defaults, three tools per run with a maximum of eight, were too restrictive,” Polu said. “The model would hit the tool limit and produce truncated results." Dust redesigned its execution loop to support up to 24 tool calls per run.

That autonomy opened up complex workflows that weren't practical before. Dust's Deep Research agents now orchestrate sub-agents across data warehouses, the web, and internal sources, running for ten minutes or more to produce a single synthesized report. But the trade-off to longer runtime was increased token consumption. To offset this, Dust worked with Anthropic's Applied AI team to optimize prompt caching, landing on a three-tier structure: globally shared instructions cached for an hour, with workspace and per-user context on shorter windows.

Dust also adopted Model Context Protocol (MCP), the open standard Anthropic created for connecting models to tools. As an MCP client, Dust's agents reach any compatible tool through one standard interface, creating an issue, updating a CRM record, or querying a database without a custom integration built for each; as a server, Dust exposes its own agents and context to other MCP-aware systems, the wiring that makes it the orchestration layer between Claude and a company's tools.

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## The outcome

## \$10K a day saved, and agents that run deeper

The caching work paid off first on the bill. Cache reads doubled from about 30% to 65% of input tokens, input spend fell 22%, and overall model spend fell 18–19%: roughly \$10K saved per day. That efficiency gives Dust more capacity to run agents deeper and longer, instead of spending it on repeated context.

Use cases like deep research and workflow orchestration have helped Dust spread across teams, driving an average of 70% weekly active usage across customer organizations. That same pattern is visible inside Dust’s own team, where engineers use their day-to-day work as a testing ground for what the platform can bring to customers. "The role of an engineer at Dust is evolving from writing code to directing, reviewing, and orchestrating AI-generated output," Polu said. More attention now goes to architecture, product judgment, and quality.

Claude Code is one of the tools driving that: a day-to-day coding partner, a GitHub Action reviewing pull requests, and a way to turn well-scoped tasks into ready-for-review PRs. One engineer built a skill that pulls company context from Dust mid-session. It is part of a broader move that took AI-written code at Dust from roughly 30% in early 2025 to between 60% and 90% today, depending on the engineer. The transition happened in weeks instead of months. “We're still figuring out what it means to be a great engineer in this paradigm," Polu said. "But we're pushing the envelope of what a small, focused team can ship when AI handles more of the mechanical work and humans focus on the decisions that actually matter."

## Related stories


### Supermetrics lets marketers manage ad campaigns from a conversation with Claude


### How Atlassian builds AI agents teams can trust with Claude and Google Cloud


### Rocket Money on building agents that fix their own code


### How Rocket Money built its personal finance agent with Claude

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
