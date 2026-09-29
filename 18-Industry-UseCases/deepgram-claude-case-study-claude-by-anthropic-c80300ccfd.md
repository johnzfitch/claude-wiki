---
title: "Deepgram Claude case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/deepgram"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:30Z"
tags: ["agents", "enterprise", "security"]
---

# Deepgram ships 4–10x more durable code with Claude

[Try Claude](https://claude.ai)

Industry:  
Software

Company size:  
Startup

Product:  
[Claude Code](https://claude.com/product/claude-code)[Claude Enterprise](https://claude.com/solutions/enterprise)

Location:  
North America

4–10x durable code output

from regular and power Claude users vs. non-users in an internal cohort study

Minutes to triage customer incidents

compared to multi-day back-and-forths, with agents that verify their own diagnoses

[Deepgram](https://deepgram.com/) builds the speech models that let software hear and talk: real-time speech-to-text, text-to-speech, and a Voice Agent API with Claude built in. It also rebuilt its own engineering on Claude, end to end.

## With Claude, Deepgram:

- Produces 4–10x more durable code output among regular and power Claude users than non-users, per an internal cohort analysis
- Cut customer incident triage from multi-day back-and-forth to minutes
- Runs roughly 95% Claude-written code on its most productive engineering team
- Documented 3–5x gains on team projects, with individuals reporting more than 2x on routine work
- Migrated the entire company to Claude Enterprise with SSO, centrally managed compliance, and organization-scoped MCP allowlists
- Replaced roughly 80% of its legacy research stack with a new agent-native environment

## The challenge

## A product surface outgrowing human-speed workflows

Deepgram's engineering surface is enormous: inference, APIs, SDKs, billing, integrations, infrastructure, and apps. Traditional workflows couldn't cover it fast enough. "Our competitors and startups we haven't even heard of yet are building AI-native now, and the cost of code generation is approaching zero," said Kris Efland, Deepgram's VP of Engineering. "If we don't ship it, someone else does, and customers follow whoever ships."

Incident triage showed the cost most plainly. When a customer reported a spike in text-to-speech errors, a Deepgram engineer pulled logs and metrics by hand, pieced them together, and wrote a response, often over a multi-day back-and-forth. The data lived in five places, and the engineer fielding the report wasn't always the one who owned the affected service.

Claude adoption, meanwhile, was outrunning any official plan: engineers moved from personal API keys to out-of-pocket Claude Max subscriptions. "If your best people are paying out of pocket to get around your limits, you've already lost more than the license would've cost," Efland said.

Claude for Statrtups

Join the founders building on Claude. Access community and resources to accelerate your growth.

[Read more](https://claude.com/programs/startups)

## The solution

## A bake-off, a cohort study, and a hard cutover to Enterprise

The conclusion was to rebuild as an agentic company or get out-shipped, an effort Deepgram calls DG2. The rebuild started with data: a real-world bake-off of Claude Code against other coding agents. What mattered most was raw model quality on Deepgram's Rust, Python, and infrastructure-as-code codebases, fit with existing internal tools, ability to verify its own work, and zero-friction access for every engineer. “The model is just better, full stop," said one of Deepgram's power users after Claude Opus 4.6 arrived. “Everything else is moot.”

An internal analysis grouped developers by Claude usage and tracked how often code was later replaced; code that stayed in the codebase counted as durable. Regular and power Claude users produced durable code at roughly 4–10x the rate of non-users, while the heaviest use drove about 9x higher churn. So Deepgram set test-coverage standards for Claude-generated code higher, not lower.

Formalizing engineer access meant a hard cutover to Claude Enterprise in mid-2026. Deepgram handles customer data under HIPAA, SOC 2, GDPR, PCI-DSS, and CCPA, so it requires Enterprise licenses where training is off by default and not changeable by users. Retention, tool permissions, and MCP allowlists are centrally managed; new-hire accounts are auto-issued before day one.

The commitment outlasts any single release. "Claude is the only frontier model where the surrounding system is good enough that we've reshaped our own infrastructure around it," Efland said. Deepgram open-sourced a terminal API so agents could drive terminal I/O directly, changing its tooling to suit the agent rather than the reverse. Code review runs through Claude on rubrics that encode where each project sits in its lifecycle, with explicit instruction not to block on nits while staying alert to security issues. Claude also runs in Slack for ambient briefings and standup recall. "The differentiator is the ecosystem with Claude Code, Cowork, MCP, skills, and subagents,” Efland said. “These create so much more than value any single model's ceiling. That's a depth of integration we haven't reached with any other provider."

## Solve a problem once, ship it as a skill

The default engineering loop runs through Claude Code: start in plan mode, iterate until it's right, then let Claude execute and verify. Claude Code connects over the Model Context Protocol (MCP) to the systems engineers already live in, from Slack and Asana to GitHub and Grafana, and drives daily CLI work. All of it runs on a CLAUDE.md file and a few slash commands. "A tight setup beats elaborate configs all day long," Efland explained.

When a solution is reusable, it becomes a SKILL.md in the shared deepgram/agents repository for the whole company to use and improve. Non-coding work runs the same way: Slack messages become Asana tickets or incident investigations.

Underneath, Opus, better at tool use, handles heavy coding and reasoning, and Haiku covers high-volume automation. Claude shows up on the product side too: the Voice Agent API pairs Deepgram's own Nova, Flux, and Aura voice model with Sonnet on the Advanced tier and Haiku on Standard as its reasoning step, with end-to-end latency under about 700ms.

## Multi-agent support for customers

One engineer, Jake, built Deephive, an in-house multi-agent support system, using Claude Code. A central Opus-class agent reads a problem and spawns parallel, read-only Sonnet-class workers that pull context from Slack, DevRev, Notion, GitHub, and Asana, then synthesize a diagnosis and draft internal handoffs and customer replies. Anything sent or changed needs human approval. Deepgram supports its top accounts this way, Anthropic among them, moving from root cause to pull request in hours and to GPU-spec recommendations in minutes.

The clearest moment was a sustained text-to-speech degradation a customer reported. A Deepgram engineer pointed the incident-response skill, Claude Code with Loki and Prometheus access, at the problem. It came back with the correct diagnosis, a low-baseline server-side stream error, not an outage, and the exact client-side fix, reconnect-on-1011, correcting the engineer's earlier guess. The reply went out signed "Sent using Claude."

"Getting 'water through pipes' is easy now,” Efland said. “Getting all the bugs out still requires reading the code.” Every production change carries human sign-off; every deliverable has one responsible human.

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Read more](/product/claude-code)

## The outcome

## Shifting from writing to validating code

With Claude built into daily engineering, regular and power Claude users now produce 4–10x the durable code of non-users, and incident triage that once ran multi-day returns verified root causes in minutes.

Deepgram's restaurant and drive-thru team, its most productive group, runs roughly 95% Claude-written code; one new hire shipped 40+ substantial pull requests in six weeks. Company-wide, new hires onboard in hours and days, not weeks. The research team replaced roughly 80% of its legacy stack with an agent-native environment; porting models to new hardware is now routine. Non-engineers stand up tools too, from ops reconciliations to MVP apps in days, and recruiting uses Claude Code for its applicant surge. Together, these workflows run on the same skills and MCP infrastructure, expanding Deepgram's capacity to build and support its voice AI products across engineering, research, and customer support.

Cheap code generation moved the constraint to validation, so Deepgram writes more tests, not fewer, and engineering shifts from writing code to defining behavior and reviewing results. "The future is agents driving not just code authoring but infrastructure, deployment, testing, and support triage,” Efland said, “with humans in the loop to defend product integrity as non-negotiable.”

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
