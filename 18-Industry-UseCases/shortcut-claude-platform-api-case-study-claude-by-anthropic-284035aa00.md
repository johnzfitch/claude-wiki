---
title: "Shortcut Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/shortcut"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:31:49Z"
tags: ["agents", "api", "enterprise", "search", "security"]
---

# How Shortcut uses Opus 4.6 to tackle complex spreadsheet work for enterprises

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Small

Product:  
Claude Platform

Location:  
North America

100,000+ users

Shortcut scaled from a consumer app to supporting more than 1,000 companies

Benchmark accuracy from 7.29 to 8.08

out of 10 after swapping to Opus 4.6 with no prompt changes

Introducing Claude Opus 4.6

We’re upgrading our smartest model. The new Claude Opus 4.6 improves on its predecessor’s coding skills. It plans more carefully, sustains agentic tasks for longer, and features a 1M token context window.

[Fundamental Research Labs](https://fundamentalresearchlabs.com/) is a two-year-old research lab focused on building more human-like AI. Their first commercial product, Shortcut, is an AI-powered spreadsheet tool that works across Excel, Google Sheets, and a standalone web and desktop app.

## With Claude, Fundamental Research Labs achieved:

- Benchmark accuracy from 7.29 to 8.08 out of 10 after swapping to Opus 4.6 with no prompt changes
- Almost half a trillion tokens processed through the platform in January 2026
- 100,000+ users at 1,000+ companies, spanning consumers, ad agencies, hedge funds, and management consulting firms
- Users report saving multiple hours per day on tasks like financial model buildouts, data extraction, and formula auditing
- Multi-agent architecture running 10+ Claude sub-agents simultaneously to analyze complex multi-sheet workbooks

## The challenge: Making AI work for spreadsheets

Spreadsheet tasks are deceptively complex for AI agents. A single financial model can contain hundreds of thousands of related cells across multiple sheets, and lacks the typical scaffolding afforded to coding agents to do the job. Nico Christie, who leads Shortcut at Fundamental Research Labs, previously worked in financial consulting where a team could spend weeks iterating on a single model before getting client sign-off. “AI is coming for spreadsheets now the same way it did for coding,” Christie said.

The work involves data extraction from documents, formula creation across interconnected cells, error detection, and model auditing. Tasks that involve finishing or auditing these models require both accuracy and an understanding of how sheets relate to each other.

Fundamental Research Labs built a benchmarking infrastructure to measure AI performance on these tasks: realistic, difficult Excel problems with verifiably correct answers. When they first launched their product Shortcut, the best models they tested scored in the 4-to-5.5 range out of 10. With other model providers, Christie reported that tasks failed roughly 70% of the time.

## Selecting Claude for spreadsheet complexity

After testing multiple model providers against its benchmark pipeline, Claude became the only model in production for Shortcut.

A key factor in the selection was how little adaptation Claude required. Other models required rounds of prompt engineering and benchmarking to work around model-specific behavior. Swapping in Opus required none. “There's very little Claude-specific prompting we have to do," Christie said.

Each subsequent Claude release has reinforced that decision. When Anthropic released Opus 4.6 in February, the score went from 7.29 to 8.08 out of 10.

“It was a step change in improvement,” Christie said. “Hard tasks that were impossible became doable. Medium tasks became easy. Easy tasks were just completely saturated. It was a total change, in the same way it was for coding."

## The results: Multi-agent architecture for complex tasks

Shortcut's architecture uses Claude in a multi-agent pattern. When a user asks Shortcut to audit a complex workbook, the system spins off multiple Claude sub-agents to explore each sheet in parallel, similar to how Claude Code operates. For a ten-sheet financial model, that might mean six to ten agents running simultaneously, each analyzing a different tab for errors, structural issues, and missing data. These agents gather context and feed findings back to a main agent.

Before executing changes, the system enters planning mode where Claude reviews the workbook, identifies issues, and asks clarifying questions. Once the plan is approved, Shortcut hands execution to a fresh Claude agent, which keeps the execution context clean and focused.

## Looking to the future

Each Claude model upgrade has delivered measurable gains for Shortcut without requiring engineering work. For Christie, that pattern shapes how the team thinks about its roadmap: as Claude's capabilities improve, so does what Shortcut can offer its users.

“Excel is used by a billion or so people, spreadsheets by two billion,” Christie said. “Shortcut’s mission is to give the feeling we get when using Claude to a billion Spreadsheet users around the world."


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
