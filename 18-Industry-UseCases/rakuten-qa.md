---
title: "Rakuten Claude Managed Agents case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/rakuten-qa"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:57Z"
tags: ["agents", "case-studies", "claude-code", "enterprise", "security"]
---

# Inside Rakuten's plan to turn every employee into a builder with Claude Managed Agents

[Try Claude](https://claude.ai)

Industry:  
Ecommerce

Company size:  
Large

Product:  
Claude Managed Agents[Claude Platform](https://claude.com/platform/api)

Location:  
Asia Pacific

Major releases every two weeks

down from once a quarter

97% reduction

in initial critical errors

Claude Managed Agents: Get to production 10x faster

We're launching Claude Managed Agents, a suite of composable APIs for building and deploying cloud-hosted agents at scale.

[Read more](https://claude.com/blog/claude-managed-agents)

[Rakuten](https://www.rakuten.com/) is a global technology company with over 70 businesses spanning e-commerce, travel, fintech, digital content, and communications. As part of its company-wide "AI-nization" strategy, the company moved from using Claude Code to accelerate software development to building AI agents that work alongside employees in every business function. Yusuke Kaji, General Manager of AI for Business at Rakuten, spoke with Anthropic about why the team adopted Claude Managed Agents, what it took to go from experiment to production, and what changes when employees start delegating outcomes to agents instead of tasks. The following conversation has been edited for length and clarity.

## Your team invested early in building agentic infrastructure from scratch. What changed when you started using Claude Managed Agents?

**Yusuke Kaji, Rakuten:** When you are at the frontier, you are often solving problems that have no prior art. We had a strong hunch early on that agents would need persistent compute, memory, and storage to move beyond chat-based AI interaction. That turned out to be exactly the right bet. Our engineers invested significant effort into the infrastructure needed to make our agents reliable and scalable. That was the right call at the time, because no one else had done it before.

Now managing the agent execution layer is not our core objective. With Managed Agents now handling scalability and reliability, that same engineering talent can be redirected toward what actually differentiates us: the agentic experience itself, and the safe, governed integration of agents with corporate systems. We see value in accomplishing things in a week rather than a year. The world will not wait for us.

## Rakuten's company-wide AI strategy accelerated with Claude Code. What made agents across the whole company the next step?

**Kaji:** From day one, we clearly saw the potential of Claude Code as a new way to work beyond engineering. We understand that technical innovation starts with a small group of users and then quickly scales to change the world. We see the agent as the next wave of that pattern.

With Managed Agents, our power users become like Galileo, contributing across domains far beyond a single specialty or discipline. We deploy each specialist agent within a week, managing long-running tasks across engineering, product, sales, marketing, and finance, generating apps, proposal decks, and spreadsheets in sandboxed environments. As agents become more capable, Managed Agents lets us scale safely without building agentic infrastructure ourselves, so we can focus entirely on democratizing innovation across the company.

In practice, we integrate agents with Slack, Microsoft Teams, and our own Kanban-style task system, where users create and assign tasks to agents. The workspace and artifacts are shared with colleagues. Managed Agents' support for multiple environments lets us create separate workspaces for each of these use cases.

We learned we can get things done anywhere, particularly from our mobile devices. Information density tends to be sparse in written communication. By natively supporting mobile, we use voice to communicate with agents, capturing more detail about the problem we want to solve while assigning tasks on the go. We see this as especially encouraging because we have Rakuten Mobile as a mobile communications business. We democratized the telecom industry, and now, using this mobile network, we can democratize innovation with AI agents.

## Walk us through how the task system works in practice. What does a typical workflow look like?

**Kaji:** In one of our products, we collect user feedback through an agent. The agent chats with users to understand their needs and pain points, then creates tickets. Another agent or our human colleagues triage the tickets. If we decide to take it, we work with agents to finalize the PRD, wireframe, or prototype. We run the iteration quickly until we meet our success criteria.

Our colleagues showcased their leadership skills, managing teams of agents the way a strong leader guides a team. One of our colleagues regularly spawns multiple agents in parallel: one for market research, another for analyzing data, while reviewing outputs generated overnight by long-running agents, sharing concrete feedback in real time, and coordinating the results into a final deck.

## You've called these power users "Galileo": people who contribute across domains beyond a single specialty. Can you give a specific example?

**Kaji:** We have a product manager, Shoko Sakamoto, who now operates far beyond her primary role. She uses agents to build FinOps pipelines across multiple public clouds, fetching data from their APIs, building dashboards from scratch to monitor trends, and implementing customized views for various stakeholders. All by herself. She also sets up ambient agents with observability skills to track anomalies in products she manages. The agents notify her when something comes up.

Engineers like Tanapat Ratana made this possible. Leading the Applied AI Group, Tanapat designed an agent that investigates production exceptions, delivers root cause analysis to Slack, and self-improves from feedback. He distributed it across teams so that non-engineers like Shoko can set it up on their own products without depending on the engineering team.

Shoko now scales the products she manages at a speed we have never seen, overseeing major releases every two weeks when it used to take a quarter, while ensuring that growth is financially sustainable. We see her as our "Galileo."

## Some of your agents work for hours at a time. What becomes possible at that timescale, and how does it change what you delegate?

**Kaji:** Before, we had to break work into well-defined chunks for the agent to execute. Now that an agent can work for hours, we share the objective or end state we want to achieve, and the agent decides what tasks should be done. That's the biggest change: we delegate goals, not tasks. This allows us to validate more hypotheses without investing as much cost and time.

## Your agents also use memory to self-improve after each session. What have you observed about quality over time?

**Kaji:** Our agents with memory remember what went wrong in past sessions and avoid repeating those mistakes. In our pilot, initial critical errors dropped by 97%, with cost and latency down more than 30%, without any loss in output quality. Agents adapt, avoiding mistakes they have already seen.

When agents retain memory at scale, the organization itself learns. Today, institutional knowledge is fragmented across people, documents, and systems. With agent memory, every insight one agent gains becomes available to the entire system. Individual learning becomes organizational learning instantly. That is when we stop thinking about agents as tools that remember and start thinking about Rakuten as an entity that continuously evolves its own intelligence. The new categories of work that open up are not just harder tasks, they are tasks that require the full breadth of what the organization knows.

## What's the biggest lesson from this journey?

**Kaji:** Our biggest learning is this hypothesis we validated through our journey: you need to completely transform the way you work to maximize the "marginal returns to intelligence." AI-nization is tough, but it is a required step to fully realize the potential of agentic systems.

## What's the end state you're building towards?

**Kaji:** We do not see AI agents as future colleagues or competitors. They are systems around us. The modern corporation was invented to reduce the cost of coordination. We believe AI agents will do the same for innovation. Our end state is simple: Rakuten becomes an entity that lowers the cost of innovation so we can accelerate our contribution to society.

Case Study: Rakuten

Rakuten uses Claude Code to accelerate software development, achieving 7 hours of autonomous coding and reducing feature delivery time from 24 days to 5 with 99.9% accuracy.

[Read more](rakuten.md)

## Related stories


### Reversia translates e-commerce stores across 110+ languages with Claude


### Rakuten accelerates development with Claude Code


### How Shopify uses Anthropic’s Claude on Google Cloud to supercharge Sidekick


### L'Oréal advances conversational analytics with Claude

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
