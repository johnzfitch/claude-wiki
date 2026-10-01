---
title: "Tasklet Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/tasklet"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:50Z"
tags: ["agents", "api", "case-studies", "enterprise", "security"]
---

# How Tasklet built 24/7 business automation with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
Claude Platform

Location:  
North America

450,000 agent actions per day

executed across thousands of customer agents

160% revenue growth

month-over-month

Most workflow automation tools require users to think like programmers: map every branch, handle every edge case, start over when something unexpected happens. Productivity startup Tasklet takes a different approach. Users describe what they want an agent to do and the agent reasons through how to get it done. And because everything runs in the cloud, the agents keep working 24x7 even when you close your laptop.

## With Claude, Tasklet achieved:

- 160% month-over-month revenue growth, reaching over \$2.5M ARR within five months of launch
- 450,000 agent actions executed per day across all customer agents
- 2,000 new agents created daily by users automating everything from email triage to revenue reconciliation
- The ability to connect to any SaaS product or API via 3,000+ pre-built integrations, MCP, browser use, and an AI-powered feature that dynamically creates API connectors to new services
- A five-engineer team shipping production code 4+ times per day, supported by Claude Code

## The challenge

## From email triggers to a general-purpose agent

[Tasklet](https://tasklet.ai/) grew out of Shortwave, an AI-powered email client the same team started building in 2022. Shortwave users kept asking for one thing: "Can the AI just run automatically?" They wanted their inbox to trigger a HubSpot update, a Notion edit, or a Slack message, without having to open a chat window every time.

The team started building that, then realized the idea was bigger than email. If an agent could trigger on inbox events, it could trigger on anything: webhooks, schedules, RSS feeds, form submissions. And if it was running unattended in the cloud, it didn't need to live inside an email client at all. In June 2025 the team started writing Tasklet from scratch. By July they had their first paying customers, and by October they launched publicly.

By the time the team started on Tasklet, they had years of production experience with every major model family. What they found was that most models handle single-turn questions well. The gap shows up when the task requires iteration.

450,000

agent actions executed per day

## The solution

## Selecting Claude for multi-step reasoning

When the team started building Tasklet, they made a deliberate architectural choice: let the model reason through the workflow rather than constraining it with predefined logic. "What if the workflow goes away and you just let the agent reason about what to do?" said Andrew Lee, Tasklet's CEO and a co-founder of Firebase. "The argument in the past was that this approach isn’t reliable enough because the models aren't smart enough. But the models are smart enough now.”

"For tasks where it's not just one question and one response, but where you need to call a tool, think, and iterate, the other models get off track after a few iterations," Lee said. "Claude can just iterate a lot longer at a high quality level."

That difference compounds in practice. A Tasklet agent might make dozens or hundreds of tool calls to complete a single task: reading an email, looking up a contact in a CRM, drafting a reply, checking a calendar, updating a spreadsheet. A small reliability gap at each step becomes a large success-rate gap over a full workflow.

Every LLM call in Tasklet's product goes to a Claude model. Users working on standard business workflows use Claude Sonnet 4.6; those tackling complex, multi-step reasoning can step up to Claude Opus 4.6 with extended thinking. The team found Claude particularly reliable in unattended operation: taking careful, considered actions when uncertain. "Safety and reliability matter a lot when agents are running autonomously without human oversight," Lee noted.

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

## The outcome

## The outcome: Connected agents that run overnight

Every Tasklet agent is a long-lived Claude conversation built around three core capabilities. Connections give it reach: 3,000+ pre-built integrations, plus the ability to have Claude read API documentation on the fly and construct a working connector for any HTTP service. Triggers give it autonomy: the agent fires automatically on a schedule or in response to events like a new email, a webhook, or a calendar entry. And computer use gives it a fallback: when no API exists, Claude spins up a browser in a cloud VM and navigates the web interface directly.

That last capability, along with the recently launched Instant Apps feature, is where Lee sees Claude's latest models pulling furthest ahead. Instant Apps lets agents generate live, interactive web applications on the fly, connected to the user's real data. A user can ask for a marketing dashboard and get one built in minutes, wired directly to their real accounts. The feature relies on Claude's code generation capabilities to produce functional UI rather than static output, something Lee says wasn't possible with earlier models.

The Tasklet team also uses Claude Code for all internal development. With five engineers, the team has shipped major architectural releases roughly every three weeks since launch. "It's amazing what we can do with five engineers and Claude Code," Lee said.

Five months in, Tasklet is growing revenue 160% month over month. Customer agents are executing 450,000 tool calls per day, and users are creating roughly 2,000 new agents daily. Use cases include intelligent email triage, revenue reconciliation across tools like Stripe and Ramp, multi-source research, deal desk pipelines, and competitor monitoring. One customer built an entire multi-agent venture capital firm back-office system in under a week.

What stands out in customer feedback is speed to value. Users report working automations in minutes, not the days or weeks a traditional workflow build would take.

Tasklet's roadmap is shaped by the same bet that started the company: every model improvement from Anthropic makes the product better without a rewrite. Near-term work includes team workspaces, shared agents, and faster & cheaper computer use. The longer-term vision is what Lee calls the "Cloud Agent OS": a primary workspace where business users consume other software through agents rather than switching between interfaces.

“2025 was the year of coding agents,” Lee said. “We think 2026 will be the year of general purpose knowledge work agents.”

Claude Platform

Use the Claude API to create new user experiences, products, and ways to work with the most advanced AI models on the market.

[Read more](https://www.claude.com/platform/api)

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
