---
title: "Caylent Claude Agent SDK case study | Claude by Anthropic"
source_url: "https://www.claude.com/customers/caylent"
category: "18-Industry-UseCases"
fetched_at: "2026-09-29T06:32:27Z"
tags: ["agents", "case-studies", "enterprise", "sdk", "security"]
---

# Caylent turns months of migration work into days with Claude Agent SDK

[Try Claude](https://claude.ai)

Industry:  
Professional services

Company size:  
Medium

Product:  
Claude Platform

Partner:  
AWS

Location:  
North America

90% reduction in engineering hours

on a 2,500-procedure database migration

\$600,000 in annual licensing eliminated

alongside a 58% faster migration

One database migration can cost more than 10,000 hours of engineering work before a single workload is validated. For years, that math priced modernization out of reach. Caylent, a cloud consultancy that helps more than 1,200 customers build and run their systems on Amazon Web Services, built Caylent Accelerate™ to break that math: an agentic delivery system that runs hundreds of Claude instances in parallel, finishing migrations in days instead of months.

## With Claude, Caylent:

- Cut engineering hours by 90% on a 2,500-procedure database migration
- Eliminated \$600,000 in annual licensing for a global enterprise SaaS customer
- Completed database migrations 58% to 82% faster across four additional customer engagements
- Compressed pre-sales environment analysis from weeks to hours
- Expedited 70% of cloud operations remediation work and cut mean time to resolution by 40%
- Reached more than 85% daily Claude use across its 900-plus-person team, with Claude Code as the primary development environment

## The challenge

## Migration math that priced out modernization

Caylent's work centers on getting customer systems onto AWS and modernizing what already runs there, and database migration was the sharpest pain. When a customer moves from a legacy commercial database to a modern open-source one on AWS, thousands of stored procedures have to be translated one by one — roughly four hours each, by engineers fluent in both platforms. That expertise is rare, and many customers deferred entirely, letting technical debt compound.

Cloud migration assessments had a parallel problem: mapping application and server dependencies for a mid-sized environment consumed months of analysis before a single server moved. "Human bandwidth set a hard ceiling on how many engagements we could accurately scope," the team explained.

Building agents with the Claude Agent SDK

The Claude Agent SDK is a collection of tools that helps developers build powerful agents on top of Claude Code.

[Read more](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

## The solution

## Proven on Caylent first

The route to Accelerate started inside Caylent. "We became our own first customer before we built anything for anyone else," the team said. More than 85% of the 900-plus-person company uses Claude daily, and DevBench, an internal harness for large engineering backlogs, compresses hundreds of hours of effort into 10 to 20.

"Caylent runs on Claude," said Randall Hunt, Chief Technology Officer at Caylent. "We’ve deployed Claude Enterprise company-wide and made Claude Code our engineers’ primary development tooling. We’ve already instrumented Claude Tag in several workstreams across departments and we built our global context management and autonomous backlog development systems entirely on Claude models. This daily operating experience, combined with Anthropic’s pace of innovation, has convinced us that we’re building on a compounding technology stack. Through Caylent Accelerate and ACE, our Anthropic consulting division, we put these same patterns to work for our customers."

Model selection for customer deployments started from one constraint: as an AWS Premier Tier Services Partner, Caylent runs Accelerate inside customers' own AWS environments through Amazon Bedrock, so models unavailable on Bedrock were excluded from the start. Caylent then tested frontier and fine-tuned open-source models on security, enterprise suitability, and task performance. Claude stood out on instruction-following, code generation across database dialects, and reasoning over the long contexts migrations produce. "In production, inconsistent outputs are expensive, and Claude's reliability was the deciding factor," the team noted.

## How it works: Specialized agents inside a customer's own AWS account

With the model chosen, the question became orchestration. The first version of Accelerate, Caylent's agentic delivery system, ran on a homegrown harness. It proved the concept but was brittle: custom orchestration code, hard to maintain, and slow to extend.

The team rebuilt Accelerate on the Claude Agent SDK, adopting the same agent loop and tool infrastructure that powers Claude Code. Heavier orchestration frameworks added abstraction the pipelines didn't need, while the Claude Agent SDK let the team define agent behavior directly in markdown, keeping orchestration logic in prompts rather than application code. That made Accelerate, in the team's words, "faster to build, easier to iterate, and simpler to debug."

Each workflow Accelerate runs for a customer is now a pipeline of stages assigned to specialized Claude agents, each scoped to only the tools it needs: an inventory parser, a dialect translator, a guardrail validator, a summary generator. An orchestrator routes work between them and selects the right model for each task, Haiku for high-volume parsing, Sonnet for synthesis and executive output. In database modernization, the pipeline parses the full inventory, classifies every object by complexity, and retires dead code before translation begins. Claude translates the active objects into the target dialect and tests them, the guardrail agent validates each translation before it commits, and a summary agent turns the results into a business-ready assessment with time and cost projections. The division of labor is deliberate. "Deterministic scripts handle precision tasks," the team explained. "Claude handles everything requiring reasoning, judgment, or language, which is most of the work." Engineers validate edge cases and final output.

Everything stays inside the customer's AWS account: no data transit to external systems, no customer data used for model training, and an AWS CloudTrail audit log capturing every AI-assisted action. Accelerate also runs before a contract is signed. In hours rather than weeks, it produces a complexity breakdown, a time estimate, and projected savings, so the first sales conversation starts from evidence.

Claude on Amazon Bedrock

Build innovative AI applications with safer systems from Anthropic, supported by secure infrastructure from AWS.

## The outcome

## 90% fewer hours and a cleaner database

The flagship engagement, one of Accelerate's earliest, cut migration hours by 90% for Arborgold. The software company had carried its SQL Server estate for more than a decade: 2,500 stored procedures across five database clusters, the kind of technical debt a founder-owned software business keeps deferring because the bill never pencils out. The target was Amazon Aurora PostgreSQL, and translated by hand, the work ran to roughly 2,600 hours.

Accelerate started by reading the whole estate, and the first finding changed the project: 1,850 of the 2,500 procedures were dead code no workload had touched in years, objects a manual team would have translated anyway. Claude classified every object, retired the dead ones, translated the active procedures, and validated each through the guardrail agent. The migration finished in about 220 hours instead of 2,600, with active procedures translated 66% faster than the general-purpose AI tools tried without Accelerate. With projected database costs down 77%, Arborgold ended with a cleaner database than it started with and a modernization path that had been priced out the week before.

A software asset management company brought a smaller version of the same problem: 257 Oracle objects scoped at roughly 1,486 hours. Accelerate finished in about 268 hours, an 82% cut worth \$202,000 in savings. "The economics hold whether the migration is large or small," the team said. The pattern repeats: migrations 73% faster at a healthcare IT provider, 75.7% faster at a data services firm that saved 2,374 engineering hours, and 58% faster at a global enterprise SaaS company that also eliminated \$600,000 in annual licensing.

## Looking ahead: A practice built on Claude from day one

The architecture reaches past migration too: in Accelerate for Agentic Cloud Operations, Caylent's new managed services offering, Claude on Amazon Bedrock AgentCore expedites 70% of remediation work and has cut mean time to resolution by 40%, while Caylent's engineers focus on the work that moves the business forward.

Caylent's newest practice is Claude-powered from day one: in April 2026, the company launched ACE, its Anthropic Consulting and Engineering practice, advancing its role as a Preferred Services Partner in the Claude Partner Network. Forward-deployed teams embed inside customer organizations to build the integrations and internal capabilities that make AI adoption stick. Every stage of the engagement runs on Claude Code, and DevBench is now available to ACE customers. Demand for that work is concentrating among software-intensive enterprises, and the team sees the question changing: "They have stopped asking whether AI belongs in the software development lifecycle and started asking how to operationalize it."

## Related stories


### How can a two-person fabrication studio make room for problems it’s never solved before?


### LG CNS modernizes 20-year-old enterprise systems with Claude


### How Blank Metal, a lean professional services firm, runs on Claude Cowork


### Quantium scales Claude across Australia's largest enterprises

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
