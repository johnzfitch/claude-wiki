---
title: "Emergent Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/emergent"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:02Z"
tags: ["api", "enterprise", "security"]
---

# Emergent builds autonomous coding agents with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Small

Product:  
Claude Platform

Location:  
North America

\$25M ARR

Achieved in 4.5 months of commercial launch

2 million

Users enabled to build applications without coding knowledge

Customer story: Brex

94%

compliance rate vs 70% industry standard

[Emergent](https://emergent.sh) is an AI platform that makes building software as simple as having a conversation. The company has created autonomous coding agents that run in cloud-based development environments, where they write code, manage databases, handle deployment, and debug issues without human intervention.

## With Claude, Emergent has:

- Achieved \$25M ARR in 4.5 months of commercial launch
- Enabled more than 2 million users to build applications without coding knowledge
- Generated complete full-stack applications averaging 5,000+ lines of code
- Built multi-agent systems where specialized Claude instances handle frontend, backend, testing, and deployment

## The problem

Emergent set out to democratize software creation by removing coding as a barrier. The company's customers—founders building MVPs, product managers creating internal tools, domain experts developing industry solutions, and small businesses automating operations—typically pay \$25-50 monthly to build applications that would traditionally cost \$50,000+ in development fees.

"We've had three lives," said Mukund Jha, CEO and co-founder at Emergent. The company initially built an AI-powered QA testing product, with agents that could navigate web applications, understand interfaces, and verify functionality. Then on day one of Y Combinator, they had a revelation: if their AI could understand applications well enough to test them, why not build them?

They pivoted immediately. Version two was an enterprise coding agent that topped SWE benchmarks. But enterprise sales cycles slowed feedback to months. In January, they pivoted again—this time to consumers, packaging their agent into a web platform where anyone could start building immediately.

However, they faced three critical technical challenges. Models would forget instructions within the same session, specifying formatting requirements only to ignore them minutes later. They would write partial code with comments like "rest remains the same," making output unusable for actual development. Most problematically, agents needed to execute hundreds of terminal commands, but models consistently failed at maintaining correct syntax and parameter ordering.

## Claude enables complete autonomous development workflows

Emergent tested everything—leading proprietary models, open source options, all of it. Claude proved substantially better across the dimensions that mattered most.

Instructions given once remained consistent throughout entire projects. Command execution showed high accuracy in tool-calling syntax and multi-step workflows. The model consistently generated full code files spanning 500+ lines without truncation.

"The API integration was straightforward—we had it running in production within two days," said Jha.

## Emergent deploys Claude across development lifecycle

Claude powers five core functions in Emergent's platform. For code generation, it produces complete applications averaging 5,000+ lines across Python backends, JavaScript frontends, and database schemas. Different Claude instances handle specialized tasks in multi-agent orchestration—one manages frontend work, another handles backend logic, a third focuses on testing, and a fourth manages deployment.

For autonomous debugging, Claude analyzes stack traces, identifies root causes, and implements fixes without human intervention. It uses vision capabilities to verify UI functionality through visual testing. Claude also makes architecture decisions, selecting appropriate tech stacks and implementing design patterns.

"The bigger challenge was learning to trust it," Jha explained. "We kept wanting to constrain Claude, add guardrails, limit its capabilities. Then we realized: Claude performs better with more freedom, not less. So we gave it full access to virtual machines. That's when the magic happened."

The approach unlocked capabilities that weren't possible before. Projects can now complete 100+ step workflows successfully, compared to 10-15 steps previously. Agents generate 5,000+ line codebases without human intervention and build full-stack applications with separate frontend and backend architectures. They handle complex features like WebSockets, real-time updates, and payment processing, while automatically recovering from errors by fixing their own mistakes.

## The outcome

The final pivot to consumers, powered by Claude's capabilities, changed everything. Emergent went commercial at the start of June. Four months later, the company reached \$25M ARR with 2 million+ users and thousands of real businesses launched through the platform.

Projects that would traditionally take a freelancer two weeks get built in two hours. The technical integration took two days for initial setup, one week to fully optimize prompts, and two weeks to restructure the entire agent architecture around Claude's capabilities.

Looking ahead, Emergent is developing mobile and desktop application capabilities in the near term. Medium-term projects include voice coding, where users can describe applications verbally while Emergent builds them in real-time, and screen sharing functionality that lets users point at problems for the agent to fix.

The company is collaborating with Anthropic on production performance benchmarking, multi-agent orchestration patterns, long-context optimization, and real-world reliability metrics. Emergent's testing and evaluation data helps Anthropic understand production applications, while model improvements directly enhance the platform's capabilities.

"Our shared goal is making software development accessible to anyone who can describe what they need, regardless of technical background," said Jha.


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
