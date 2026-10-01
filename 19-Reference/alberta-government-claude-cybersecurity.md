---
title: "Alberta uses Claude to find and fix security vulnerabilities \\ Anthropic"
source_url: "https://www.anthropic.com/news/alberta-government-claude-cybersecurity"
category: "19-Reference"
fetched_at: "2026-09-10T06:43:57Z"
tags: ["news-research", "security"]
---

# Government of Alberta uses Claude to find and fix cybersecurity vulnerabilities across government systems

Jul 6, 2026

Since 2025, the Government of Alberta has been using Claude Code with both Opus and Sonnet models to review its systems, find vulnerabilities, and fix them. A team inside Alberta’s Ministry of Technology and Innovation scanned 466 million lines of code in 20 hours, remediated security gaps across its systems, and built new tools to make those systems safer.

We’re sharing details of their experience as an example of how government agencies can use Claude and Claude Code to secure their systems at a large scale. This is a critical challenge, as governments rely on these systems to deliver benefits and keep services running—yet the code is often old, insecure, and incompletely documented. Alberta has also published a collection of technical white papers documenting its efforts for other governments to learn from; [you can read them here.](https://thevelocitywhitepapers.com/)

“Albertans trust their government with some of the most sensitive information in their lives, and it is our responsibility to protect it,” said Nate Glubish, Alberta’s Minister of Technology and Innovation. “By using AI to find and fix vulnerabilities across our systems, we accomplished in hours what would have taken a traditional approach years to complete. This is what responsible government looks like in the AI era, and the best is still ahead of us.”

## Alberta’s approach

Alberta’s Ministry of Technology and Innovation maintains the systems of all 27 provincial ministries, from social services to public safety to wildfire response. That includes roughly 1,280 applications and 3,400 code repositories. Most of it has never undergone a systematic security review, and the accumulated technical debt—insecure code, unaddressed bugs, outdated software—runs into the billions of dollars.

The Ministry’s systems hold highly sensitive information, including tax records, government procurement data, and social services case files. So in 2025, the Ministry set up an internal team with a mandate to make these systems more secure and easier to maintain over time, working with Claude to do so.

Already, the Ministry has used Claude to:

**Assess 466 million lines of government code in 20 hours.** The team put Claude to work on the codebases it maintains, using Claude Code with Claude Opus and Sonnet models. Around 50 agents worked autonomously and in parallel to scan the systems for security vulnerabilities, weaknesses in underlying infrastructure and deployment processes, and gaps in technical documentation. Claude Code ran a two-stage routine, first scanning each repository with a rules engine to flag known patterns, then reviewing those flags and citing the exact file and line for each finding so developers could verify them. The scan covered every repository Alberta owns and identified issues that traditional automated scanning tools had missed. It took about 20 hours for Alberta’s implementation; the team estimates that that kind of review could otherwise have taken around 6.5 years.

**Fix the vulnerabilities the scan found.** Where the scan identified a vulnerability, Claude Code could often generate a fix, test it, and build it. In cases where a system lacked the automated tests needed to confirm that a patch was safe, Claude wrote the tests first. Where the code was too outdated or too complex to patch efficiently in its existing form, Claude rebuilt it in a more modern and maintainable language. In some scenarios, these systems could be rebuilt in as little as four to five days, including a subsidy program portal that was originally hand-coded in Java roughly 25 years ago and took five months to build the first time. All of this was done in partnership with the Ministry’s engineers: before any patch shipped, it was reviewed and approved by the team.

**Run continuous security review.** Alberta’s cybersecurity team also built a set of specialized Claude review agents that run throughout the development process. A “red team” agent probes an application from the outside, the way an attacker might, and maps how a vulnerability might be exploited. A “blue team” agent then assesses the application’s defenses against an international security standard, and writes a remediation plan that points to the exact files to fix. Additional agents check code quality and the clarity of the writing the public sees. Every application is checked against roughly 95 security controls on each pass. These agents are built on top of the [Claude Agent SDK](https://www.anthropic.com/09-Agents-Patterns/agent-sdk-overview-b27888bae2.md) and run a robust series of checks and analysis for every application.

In addition to scanning, securing, and modernizing its own systems, Alberta is training both government workers and the public in the use of AI through the Alberta AI Academy. Thousands of government employees and more than 10,000 members of the public have used the platform to learn the essentials of effective AI use, from prompting through enterprise application delivery. Through the Academy, the Ministry of Technology and Innovation aims to extend its approach beyond a single team or project to every ministry that needs it.

## Looking ahead

Today, Claude helps the Ministry write, review, and deploy code that aids in its modernization efforts. Next, it plans to expand that work with AI agents that can build entirely new software and tools alongside engineers.

The Government of Alberta also plans to continue its modernization work. One ministry, for example, has 185 legacy applications running in production, which are expensive to maintain and difficult to update. The Government plans to use Claude Code to analyze these systems, understand what they do, and consolidate them into 16 reusable applications built on modern coding languages and conventions. The goal is to reduce complexity, lower maintenance costs, and speed up modernization work that would otherwise take years to complete.

## A case study for governments

The technical debt and security vulnerabilities the Government of Alberta is working to address are hardly unique. They exist in the systems of many provinces, states, and federal agencies across the world. The [technical white papers](https://thevelocitywhitepapers.com/) Alberta has released give other governments a blueprint for addressing these same issues.

In addition to the white papers, Alberta is hosting [an industry day](https://luma.com/yzd00tir) in Edmonton in July to share what it has learned. And this fall, it will begin a program to scale its approach across the provincial government. We’ll keep working with Alberta as it expands these efforts, and we hope the approach it has documented can help other governments secure their own systems.


## Related content

### Developing Enterprise Frontier Safeguards with our customers

[Read more](enterprise-frontier-safeguards.md)

### Improving our alignment and security efforts

On July 30, we reported three incidents in which Claude models gained unauthorized access to real computer systems. We are conducting an in-depth analysis of both incidents, and planning to work with METR for an independent review. In the meantime, we’re sharing some of the changes we’ve made over the past month.

[Read more](improving-alignment-security-efforts.md)

### Previewing the Model Hardware Standard

We’re opening a research preview of the Model Hardware Standard (MHS), a shared specification for AI agents to safely operate physical devices, to a first group of scientific research labs and advanced manufacturers.

[Read more](model-hardware-standard-research-preview.md)

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/claude-com-product-claude-code.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../14-Connectors/claude-for-slack.md)
- [Claude Design](../15-Claude-AI-Features/product-design.md)
- [Claude Science](../15-Claude-AI-Features/product-claude-science.md)
- [Claude Security](../15-Claude-AI-Features/product-claude-security.md)
- [Claude in Chrome](https://claude.com/claude-in-chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](https://www.anthropic.com/15-Claude-AI-Features/claude-opus-4-6-anthropic.md)
- [Sonnet](https://www.anthropic.com/15-Claude-AI-Features/claude-sonnet-4-6-anthropic.md)
- [Haiku](https://www.anthropic.com/15-Claude-AI-Features/claude-haiku-4-5-anthropic.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Commerce](../18-Industry-UseCases/commerce.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../18-Industry-UseCases/enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud-vertex-ai.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://academy.claude.com)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](../15-Claude-AI-Features/programs-startups.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
- [Leadership](company-leadership.md)
- [Policy](https://www.anthropic.com/policy)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](anthropic-com-research.md)
- [News](news.md)
- [Claude’s Constitution](https://www.anthropic.com/constitution)
- [Claude Corps](../15-Claude-AI-Features/claude-corps.md)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](https://www.anthropic.com/transparency)
