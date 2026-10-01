---
title: "Greptile Claude Platform (API) case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/greptile"
category: "18-Industry-UseCases"
fetched_at: "2026-09-30T06:32:19Z"
tags: ["agents", "api", "case-studies", "enterprise", "sdk", "security"]
---

# Greptile builds truly agentic code review with Claude Agent SDK

[Get started](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)

Industry:  
Software

Company size:  
Small

Product:  
Claude Agent SDK[Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)

Location:  
North America

~90% cache hit rates

Prompt caching through the Agent SDK dramatically reduces costs and increases compute efficiency

1 million

Issues caught per month

[**Greptile**](https://greptile.com) builds AI agents that review pull requests with full codebase context. The company serves more than 2,000 organizations, from startups to enterprises like NVIDIA, Brex, and Coinbase, helping engineering teams catch bugs and anti-patterns before they ship to production.

## With Claude Agent SDK, Greptile:

- Achieves ~90% cache hit rates, dramatically reducing costs for both Greptile and self-hosting customers
- Enables multi-hop code investigation that follows leads across git history, similar functions, and pull request context
- Ships new capabilities faster by focusing engineering time on specialized tooling rather than harness infrastructure
- Powers autonomous code review that iteratively investigates issues rather than following rigid workflows
- Provides enterprise customers with cost-effective self-hosting options through efficient compute usage

## The problem

In the AI code review space, most tools follow predetermined paths. They scan a pull request, run through a fixed checklist, and surface findings in a predictable sequence. But Greptile sees code review as an investigation, not a checklist. When a skilled engineer spots something unusual, they don't follow a script. They dig deeper, examine context, trace history, and connect dots across the codebase.

Greptile's team recognized this gap. They had built specialized tools for the investigative work: utilities for grabbing codebase context, finding semantically similar functions, retrieving git history, and more. But their orchestration layer forced these tools into a rigid flowchart. Each step revealed new information, but the system couldn't act on those discoveries because it was locked into a predetermined sequence.

"We wanted to build a system where Greptile could be truly multi-hop and autonomous—where every step reveals new information, and the next step can be based on that information instead of following a rigid flowchart," says Daksh Gupta, Co-founder and CEO, at Greptile.

The team needed an orchestration layer as intelligent as their tooling—one that would let their code review agent think like a skilled engineer.

## Building an agentic code review system with the Agent SDK

The Greptile team considered building their own agent harness but quickly realized where their time would be better spent. "It became clear to us that the value was to spend all of our time building better tools for code review," Gupta says. For a team of 10 engineers, that focus matters.

The Claude Agent SDK offered a powerful orchestration layer that would let them focus on their domain expertise rather than infrastructure. The decision also reflected a technical intuition: agent harnesses and models are tightly coupled. "It was clear to us that models and harnesses would be coupled, and the models were the best," Gupta explains. "That was a really big advantage for the Anthropic SDK."

## Greptile uses Claude for multi-hop code investigation

Claude now powers Greptile's investigative approach to code review. When the agent spots a calculation that looks unusual or a function that differs from similar ones across the codebase, it can autonomously decide what to investigate next. It might examine git history to understand why something changed, trace a commit back to its original pull request to read the context, or compare the code against patterns elsewhere in the repository. "It's acting like an investigative reporter or detective," Gupta explains. "We have all the tooling for the detective, and what we wanted was a really powerful orchestrator for it."

Greptile runs on Opus 4.5. “We believe it to be the best coding model for everything we're trying to achieve with detecting bugs and anti-patterns in code,” Gupta said. “The prompt caching works well for our use case, and the integration with MCP has been valuable."

Greptile also makes heavy use of the SDK's sub-agent capabilities. One sub-agent handles memory retrieval, pulling from a bank of information that includes coding standards the team has expressed, idiosyncrasies Greptile has learned about the codebase, and context from documentation, claude.md files, and cursor rules. This accumulated knowledge informs every review.

The team also uses hooks to inject determinism where it matters. For code review, this means ensuring that every file in a pull request gets examined—a guarantee that's essential for enterprise customers who need thorough, consistent coverage.

## The outcome


The shift to the Agent SDK delivered immediate efficiency gains. Greptile now achieves cache hit rates close to 90%, which translates to meaningful cost savings across their operation. For customers who self-host Greptile using their own Anthropic instances, this efficiency means they can roll out AI code review at larger scale without proportional cost increases. "Now with the Agent SDK, we have true autonomy—every step creates new information, and the next step can be based on that information," Gupta says. "This has fundamentally changed how our code review agent operates."

The deeper impact is in what Greptile can now build. "The Agent SDK has allowed us to ship faster with far more cost effectiveness and allows us to focus deeply on building specialized tooling," Gupta says."We can focus all our energy on building highly specialized tools for the specific types of things we want to achieve."

Rather than maintaining harness infrastructure, the team invests that engineering time in the tools that make code review genuinely useful: better codebase understanding, smarter similarity detection, richer git history analysis.

The results show up in production. In one example from an NVIDIA open-source repository, Greptile flagged an issue that the reviewing engineer initially disputed. The agent responded with additional evidence—comparisons to similar functions across the codebase, relevant git history—and the engineer acknowledged the catch was correct. That kind of multi-step investigation, where the agent can defend its findings with evidence, is exactly what the agentic architecture enables.  
  
Customers have noticed the difference. "Despite having a tech stack that has repeatedly proven difficult for AI to grasp, Greptile has delivered consistent review insights with a good signal-to-noise ratio that has won over even our most discerning engineers," says Jarrod Ruhdland, Principal Engineer at Brex.

Greptile continues to expand what's possible with the Agent SDK, building new capabilities that would have been far more difficult to develop and maintain without it. For a company reviewing over a billion lines of code each month, the ability to focus on domain expertise rather than infrastructure has become a strategic advantage.

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
