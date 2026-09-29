---
title: "Warp Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/warp"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:18Z"
tags: ["agents", "api", "case-studies", "enterprise", "security"]
---

# Warp rebuilds the terminal for AI coding with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
Claude Platform

Location:  
North America

800K monthly developers

build software using Warp

10M Claude Code sessions

run inside Warp's terminal to date, including 400K+ each week

[Warp](https://www.warp.dev/) is building an agentic development environment: a workbench for running, managing, and scaling agents. Grounded in an open-source terminal with over 60k GitHub stars, developers using Warp run coding agents like Claude Code and Warp Agent locally or in the cloud. Users can start agents from any surface via CLI, API, or SDK, and manage all agents in a central control plane. Warp defaults to Claude models for advanced coding and provides a modern environment for running Claude Code locally.

## With Claude, Warp:

- Serves 800K monthly developers through its agentic terminal
- Has logged 40M Warp Agent conversations, with 65% of tokens routed to Claude models
- Processes 55 billion Claude tokens per day on its platform
- 10M Claude Code sessions run to date in its terminal, including 400K+ each week
- Can spawn Claude Code as a sub-agent for parallel work across a codebase
- Defaults its "auto-genius" mode to Claude for coding tasks when users want top intelligence

## The challenge

## A 40-year-old developer tool meets agentic coding

When Warp launched in 2021, the terminal hadn't seen meaningful investment in three or four decades. The team started by trying to improve the fundamental UI of the terminal, and added AI capability as language models became readily available: natural-language-to-shell-command translation, a chat assistant panel, then "agent mode," one of the first command-line agents with direct terminal access for running commands and reading files.

As agentic coding accelerated, teams trying to deploy autonomous coding agents into production started finding new problems. The terminal was the natural home for local development work, but wasn't built for it. And running agents in the cloud required stitching together a complex infrastructure: environments for agents to run, visibility into agent actions, tools to steer agents, and ways to continue work locally.

“Warp's mission has always been to help developers use great tools to ship great software, and that mission hasn't changed,” said Olivia Johnston, Senior Product Marketer at Warp. “What's changed is what supporting developers actually looks like today.”

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/claude-com-product-claude-code.md)

## The solution

## A Claude-powered agent harness, then a cloud platform around it

In 2024, Warp began evolving its flagship product from a terminal to an agentic development environment, optimizing the Warp Agent for complex coding tasks, and adding support for multi-agent workflows and code editing directly into the terminal.

When Claude Sonnet 4 arrived, Warp's team saw a step-change in coding capability. Up to that point, Warp's terminal agent had been strong at what the team called "shallow but broad" tasks: translating natural language commands, navigating CLIs, and helping developers find the right syntax. But with Sonnet 4, the agent could take on full software development lifecycle work: writing code, running tests, reviewing diffs, debugging across a codebase.

"There was an immediate, noticeable difference in what the agent was capable of, even as we were internally dogfooding,’" said Zach Bai, an Head of Product Engineering at Warp. "With Sonnet 4, the thing we built began working in a way it never had before."

For coding tasks, Warp's "auto" mode defaults to Claude. Most users who don't manually configure a model end up on Claude Opus, Sonnet, or Haiku, depending on the complexity of their task. “Most of our users believe Claude models are at the frontier of coding intelligence and are the right fit for the development tasks at hand," said Suraj Gupta, the engineer leading Agent Quality at Warp.

Warp's recently launched cloud agent orchestration platform, Oz, lets users start cloud runs of popular coding agents—including the Warp Agent and Claude Code—directly from the terminal. Runs can also be triggered through first-party integrations with Slack, Linear, and GitHub, or programmatically via API or SDK. Teammates can jump into an active session to see what an agent is doing and steer it, with the right permissions. Customers can self-host the platform, run it on Warp's infrastructure, or mix both.

Warp allows users to choose their preferred models and coding agents for tasks. Customers can use the Oz platform to start and steer Claude Code agents or Warp Agents in the cloud, can use the Warp code review feature to send comments directly to Claude Code in the terminal, and can select the model that best meets their needs.

"We want to provide the best place to build with agents, and for a lot of our customers that means giving them the flexibility to choose their favorite coding agent," Johnston said. "They've invested in tooling and want help building automations, but they want to keep using what they already have."

Choosing the right Claude model

Learn when to use Haiku, Sonnet, or Opus to get better results and stay inside your rate limit. A practical guide to picking the right Claude model.

## The outcome

## 800K developers, a new audience for the terminal

Warp now serves 800K monthly developers. The terminal has run 10 million Claude Code sessions to date, with over 400,000 each week. Warp Agent has logged 40 million conversations total, with 65% of those tokens routed to Claude. Users at 56% of the Fortune 500 are now on Warp, including leading engineering teams like Ramp, Peloton, and Docker.

Warp is also picking up an audience no one expected. "People who didn’t know what a terminal was two years ago are now seeking Warp out and downloading it," Bai said. Marketers and analysts use the terminal as a way into internal CLIs and data tools they otherwise couldn't reach, with an agent handling the parts they don't know. Johnston, a marketer herself, uses Warp's agent with Claude to query internal data directly, getting answers in minutes that previously meant filing a request and waiting on the data team's queue. "It can create dashboards and charts for me, then push them up onto our dashboard system so I can share them with everyone else," she said.

Warp's next focus is expanding on its support for teams using multiple agent harnesses with cross-agent memory. The team plans to add a persistent memory layer to the cloud platform so agents don't start every task from scratch. "We want it to be multi-harness," Gupta said. "Whether you're using Claude Code, our own harness, or another agent platform, your memories carry forward."

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
