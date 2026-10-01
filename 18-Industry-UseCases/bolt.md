---
title: "Bolt Claude Agent SDK case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/bolt"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:40Z"
tags: ["agents", "case-studies", "enterprise", "rag", "sdk", "security"]
---

# Bolt builds autonomous design system agent on the Claude Agent SDK

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
Claude Agent SDK

Location:  
North America

~53-minute average autonomous agent workflow

powered by Claude Opus 4.7, resolving conflicts and mapping tokens across thousands of components

~90% cache efficiency on the Agent SDK

reducing inference costs across high-traffic workflows

[Bolt](https://bolt.new) is a vibe coding tool that lets users build full applications in natural language, with built-in integrations for databases, payments, and deployment. Built by StackBlitz and powered by the Claude Agent SDK, Bolt's newest capability is a design system agent that lets PMs and designers generate production-ready, on-brand prototypes without writing code.

## With Claude, StackBlitz achieved:

- 10,000+ users uploading their own design systems to Bolt
- ~53-minute design system generation, then unlimited on-brand prototypes in ~5 minutes each, with minimal engineer rework needed to ship
- Autonomous design system generation that consolidates Storybook, GitHub repos, npm packages, Figma tokens, and documentation into a unified system
- ~90% cache efficiency on the Agent SDK, reducing inference costs across high-traffic workflows

## The challenge

## The problem with fragmented design systems

Most companies don't have their design system in one place. Typography lives in a Google Doc. Components are scattered across Figma files, Storybook instances, and GitHub repositories. Spacing and layout guidelines might be in a wiki, or just in an engineer's head.

That gap has become a major barrier to enterprise adoption of AI development tools. PMs and designers can prototype ideas in tools like Bolt, but without access to the company's actual design language, the result looks generic. "Oftentimes if you just use Bolt, it doesn't have any idea about your company's design system," said Dominic Elm, Founding Engineer at StackBlitz. "And a design system is a somewhat complex system. It has guidelines, typography, spacing, layout, all these things."

The tools can generate code quickly, but the output doesn't match a company's internal standards. Prototypes end up as throwaways: a PM builds something to communicate an idea, but an engineer rewrites it entirely before it can ship. That distance between prototype and production code keeps non-engineers on the sidelines of the development lifecycle.

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

## The solution

## Why StackBlitz built on the Claude Agent SDK

StackBlitz had built its own internal agent to power Bolt, but as the team planned a major overhaul, the Claude Agent SDK arrived at the right moment. "We were looking at making a ton of improvements to our agent, looking at a v2," Elm explained. "But then the Agent SDK came and it just made a lot of sense to go with something that is already used by so many people."

The decision shifted the team's focus from building and maintaining agent infrastructure to product innovation. StackBlitz's AI team is small. "We have a couple people, but it's probably still nowhere near the people that are working on Claude Code," Elm added. Claude Code's established user base was part of the appeal: the Agent SDK meant StackBlitz didn't need to match that investment to get the same underlying capabilities. The Agent SDK is built on the same harness that powers Claude Code, so StackBlitz could inherit those capabilities without having to match that investment.

## Building a design system agent with Claude

StackBlitz was one of the earliest teams to go all in on the Agent SDK, and the extended experience building on it has shown Elm how flexible the platform is. "The way it's currently shaped just allows you to build almost any workflow," he said.

The design system agent is a case in point. It starts by taking in everything a company has: Storybook sites, GitHub repositories, npm packages, Figma tokens, documentation files. Users point the agent at all their sources and it does a thorough pass across each one, resolving conflicts, mapping design tokens, and understanding component variants. What comes out is a consolidated intermediate representation of the full design system. The agent uses Claude Opus 4.7, which Elm said "showed the best results overall" for the sustained reasoning this research phase demands.

This research phase can run for 40 minutes to an hour and a half depending on how many sources are connected, averaging around 53 minutes. That's a different kind of task than a typical five-minute prototype build. The SDK's hooks made that feasible. With the stop hook, the team can keep an agent running across a long workflow, pass feedback back in, and change the agent's trajectory mid-run. Custom sub-agents handle parallel tasks while keeping the main agent's context clean. "It helps with overall speed because you can parallelize things," Elm noted. "Also, what the sub-agent does isn't polluting the main context window."

The result lives inside Bolt as a browsable library of all the company's components, sections, and pages in one place. StackBlitz was deliberate about not making Bolt the source of truth for a company's design system. Instead, when a team updates their design system on their end, they can come back to Bolt and reindex, and the agent does an incremental update. Once the design system is in place, a user selects it, prompts Bolt to build something, say a car configurator or a comparison page, and the output follows the company's actual components, typography, and spacing. The agent then checks its own work in a review loop. "You build something and then you check again: does this match what it's supposed to look like?" Elm said, comparing the process to how a developer would verify output against a Figma file.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](../15-Claude-AI-Features/claude-com-product-claude-code.md)

## The outcome

## From throwaway prototypes to production code

The design system agent changes what PMs and designers can deliver. The design system is generated once in an autonomous run averaging 53 minutes. From that point on, any team member can prompt Bolt to produce on-brand prototypes in roughly five minutes, generating code that can go to production with minimal rework. "The idea is that Bolt can generate a prototype that is not just a throwaway," Elm said. "You can take it and hand it to an engineer and they can ship that code almost as-is to production and just connect the business logic to the components."

StackBlitz sees roughly 90% cache efficiency on the Agent SDK, keeping inference costs manageable across these long-running workflows. More than 10,000 users have already uploaded their own design systems to Bolt.

## Looking ahead

StackBlitz is focused on broader adoption among companies shipping production code through Bolt. "The goal is to get PMs and designers actually integrated into the development lifecycle and able to contribute to production code," Elm said. "That's the holy grail for almost everyone."

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
