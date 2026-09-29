---
title: "Vapi Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/vapi"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:17Z"
tags: ["agents", "api", "enterprise", "security"]
---

# Vapi turns natural language into production voice agents with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
[Claude Platform](https://claude.com/platform/api)Claude Agent SDK[Claude Code](https://claude.com/product/claude-code)

Partner:  
AWS

Location:  
North America

~3x higher deep activation rate

for users who build voice agents through Vapi's Claude-powered AI agent

3x recovery rate after a failed first call

for users guided by Vapi's AI-powered setup agent

[Vapi](https://vapi.ai/) is an enterprise platform for building, deploying, and managing voice agents. The platform is API-native and deeply configurable, from audio ingestion and endpointing to tool-call structure and fallback logic.

## With Claude, Vapi:

- Shipped Composer, Vapi’s intelligent assistant that helps build and configure voice AI agents through natural conversation, from prototype to general availability in 2.5 months with a team of five engineers
- Made users nearly 3x more likely to reach 100 call minutes, Vapi's milestone for sustained platform usage, when they build voice agents through Vapi's Claude-powered AI agent
- Tripled recovery rate for users who engage Claude-powered guidance after a failed first call
- Doubled initial activation, defined as 10 call minutes, for users onboarded through natural language
- Enabled natural-language debugging of live agents, compressing hours of engineering time into minutes

## The challenge

## Strong signups, soft activation

Vapi gives teams a platform to build AI-powered voice agents that handle real customer calls without a human on the line. The platform exposes more than a dozen configuration points because the use cases demand it: a healthcare company with strict data residency requirements handling 250,000 monthly patient calls and a labor marketplace screening 50,000 applicants a month have almost nothing in common architecturally, but both run on Vapi. That depth of configurability was also a double-edged sword. Technical users could reach a prototype in a day or two. Everyone else hit a wall.

"If you were technical enough to read our API reference and wire up a call, you could reach a prototype in a day or two," said Jordan Dearsley, CEO and Co-founder. "If you were not, you were either in a support channel, a sales conversation, or you logged out."

New customer activation depended on documentation, example code, and Vapi's field engineering team. That was expensive in both directions: lost self-serve revenue from users who never activated, and engineering time spent on basic setup instead of strategic customer work. The goal was concrete: get a non-technical user from signup to a working voice agent in under 30 minutes through natural language alone.

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

## The solution

## Selecting Claude for function-calling reliability

To close that gap, Vapi built Composer, a Claude-powered AI agent that lets anyone create voice agents through natural language conversation. The team ran production experiments across Claude Opus, Sonnet, and Haiku, alongside models from other providers. They used feature flags to split live traffic between models and measured tool success rate, error classes, and user-level outcomes.

For Composer, the criteria that mattered most were function-calling reliability, output consistency under tool orchestration, and latency. Cost mattered once the first three were satisfied.

"Claude's function-calling behavior under the kinds of agentic workloads Composer runs is meaningfully more reliable than alternatives we have tested," Dearsley explained. "When Composer needs to invoke a tool to update an assistant's prompt, add a new squad member, run a simulation, or pull a call log, Claude gets the schema right on the first try more consistently."

The Claude Agent SDK was the second factor. Dearsley built the original Composer prototype on the SDK, which reduced the amount of agent-loop and context-management code the team had to write. "That let us move faster, and it let us reach a level of agentic reliability earlier than we would have otherwise," he noted.

## Composer turns natural language into working voice agents

Dearsley built the first working Composer prototype in a single evening. From that overnight build to general availability took 2.5 months with a team of five engineers, led by Dev Seth, Manager, Product Engineering. A user types what they want ("build me an outbound agent that qualifies real estate leads, transfers hot ones to my sales team, and logs the call in HubSpot") and Composer takes over. Claude has access to a tool suite that mirrors the full Vapi API, selects and invokes the right tools, and streams results back with an approve/deny flow on any action that mutates state. The loop is multi-turn and persistent across sessions.

Scaling that to production meant solving a real architectural problem. "Our first version was a single giant system prompt with tools bolted on," said Seth. "The system prompt was consuming more than 50 percent of our context window before a single user message came in." The fix was a modular architecture with a runtime router, shared chat kernel, and pluggable UI shell. The result: adding Composer to a new product surface dropped from around 700 lines of frontend code to around 30. Claude provides the intelligence layer; the team built everything else, from the architecture to the observability to the fallback logic between the direct Anthropic API and Amazon Bedrock.

Composer now runs on more than 10 skills and a catalog of 100+ tools that reaches beyond agent setup. In a chat thread, Composer searches the web to fill in missing prompt details, provisions a new phone number, runs a simulation against a proposed change, analyzes a transcript, or computes fleet-wide metrics like p95 latency. Claude reaches the catalog through tool search rather than loading every definition upfront. Only the tools relevant to the current turn flow into context.

"The accuracy gap between Claude and the other models we tested widens with chain length and tool specialization," Seth said. "Composer often picks the right tool, chains a dozen of them in the right order, and tunes an assistant's settings across many interdependent configs. Claude gets the full chain right far more often."

Beyond Composer, customers building voice agents on Vapi can also select Claude Sonnet or Opus, via the direct Anthropic API or Amazon Bedrock, to power the intelligence layer of their agent. Claude is among the most heavily used models across Vapi's enterprise customer base.

Introducing Agent Skills

Claude can now use Skills—folders with instructions, scripts, and resources—to become a specialist at specific tasks when you need it.

[Read more](https://claude.com/blog/skills)

## The outcome

## 3x more likely to reach deep activation

Composer users are 2x more likely to reach 10 call minutes and nearly 3x more likely to reach 100 call minutes, compared to users who don't engage Composer. The recovery metric is especially telling: users who engage Composer after a failed first call are 3x more likely to reach deep activation rather than churning.

Vapi's solutions engineers now stand up customer-specific demo agents in real time during prospect calls. Composer can also read call transcripts, diagnose why a call went sideways, and suggest or apply a fix directly, compressing what used to be hours of debugging into minutes.

One moment captures the shift well: a customer flagged a configuration option that was exposed in Vapi's API but didn't yet have a UI surface. A team member asked Composer to make the change, and it worked, updating the configuration through the underlying API without anyone waiting for a UI to ship.

"We knew that if we could compress the time from 'I signed up' to 'I have a working voice agent,' we would materially change the trajectory of the business," Dearsley said.

## Related stories


### Supermetrics lets marketers manage ad campaigns from a conversation with Claude


### How Atlassian builds AI agents teams can trust with Claude and Google Cloud


### Rocket Money on building agents that fix their own code


### How Rocket Money built its personal finance agent with Claude

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
