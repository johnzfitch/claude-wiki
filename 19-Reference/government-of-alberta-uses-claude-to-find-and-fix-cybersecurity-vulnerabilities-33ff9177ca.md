---
title: "Government of Alberta uses Claude to find and fix cybersecurity vulnerabilities \\ Anthropic"
source_url: "https://www.anthropic.com/news/alberta-government-claude-cybersecurity"
category: "19-Reference"
fetched_at: "2026-08-02T05:41:25Z"
tags: ["security"]
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

**Run continuous security review.** Alberta’s cybersecurity team also built a set of specialized Claude review agents that run throughout the development process. A “red team” agent probes an application from the outside, the way an attacker might, and maps how a vulnerability might be exploited. A “blue team” agent then assesses the application’s defenses against an international security standard, and writes a remediation plan that points to the exact files to fix. Additional agents check code quality and the clarity of the writing the public sees. Every application is checked against roughly 95 security controls on each pass. These agents are built on top of the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) and run a robust series of checks and analysis for every application.

In addition to scanning, securing, and modernizing its own systems, Alberta is training both government workers and the public in the use of AI through the Alberta AI Academy. Thousands of government employees and more than 10,000 members of the public have used the platform to learn the essentials of effective AI use, from prompting through enterprise application delivery. Through the Academy, the Ministry of Technology and Innovation aims to extend its approach beyond a single team or project to every ministry that needs it.

## Looking ahead

Today, Claude helps the Ministry write, review, and deploy code that aids in its modernization efforts. Next, it plans to expand that work with AI agents that can build entirely new software and tools alongside engineers.

The Government of Alberta also plans to continue its modernization work. One ministry, for example, has 185 legacy applications running in production, which are expensive to maintain and difficult to update. The Government plans to use Claude Code to analyze these systems, understand what they do, and consolidate them into 16 reusable applications built on modern coding languages and conventions. The goal is to reduce complexity, lower maintenance costs, and speed up modernization work that would otherwise take years to complete.

## A case study for governments

The technical debt and security vulnerabilities the Government of Alberta is working to address are hardly unique. They exist in the systems of many provinces, states, and federal agencies across the world. The [technical white papers](https://thevelocitywhitepapers.com/) Alberta has released give other governments a blueprint for addressing these same issues.

In addition to the white papers, Alberta is hosting [an industry day](https://luma.com/yzd00tir) in Edmonton in July to share what it has learned. And this fall, it will begin a program to scale its approach across the provincial government. We’ll keep working with Alberta as it expands these efforts, and we hope the approach it has documented can help other governments secure their own systems.


## Related content

### Investigating three real-world incidents in our cybersecurity evaluations

[Read more](/news/investigating-incidents-cybersecurity-evals)

### Our position on open-weights models

[Read more](/news/position-open-weights-models)

### Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients

[Read more](/news/cognizant-anthropic)

[](/)

### Products

- [Claude](https://claude.com/product/overview)
- [Claude Code](https://claude.com/product/claude-code)
- [Claude Code Enterprise](https://claude.com/product/claude-code/enterprise)
- [Claude Cowork](https://claude.com/product/cowork)
- [@Claude](https://claude.com/product/tag)
- [Claude Design](https://claude.com/product/design)
- [Claude Science](https://claude.com/product/claude-science)
- [Claude Security](https://claude.com/product/claude-security)
- [Claude for Chrome](https://claude.com/chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](https://claude.com/pricing)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](https://www.anthropic.com/claude/mythos)
- [Fable](https://www.anthropic.com/claude/fable)
- [Opus](https://www.anthropic.com/claude/opus)
- [Sonnet](https://www.anthropic.com/claude/sonnet)
- [Haiku](https://www.anthropic.com/claude/haiku)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Cybersecurity](https://claude.com/solutions/cybersecurity)
- [Enterprise](https://claude.com/solutions/enterprise)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Healthcare](https://claude.com/solutions/healthcare)
- [Higher education](https://claude.com/solutions/education)
- [K-12 teachers](https://claude.com/solutions/teachers)
- [Legal](https://claude.com/solutions/legal)
- [Life sciences](https://claude.com/solutions/life-sciences)
- [Nonprofits](https://claude.com/solutions/nonprofits)
- [Small business](https://claude.com/solutions/small-business)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](https://platform.claude.com/docs)
- [Pricing](https://claude.com/pricing#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](https://claude.com/partners/claude-on-aws)
- [Google Cloud](https://claude.com/partners/google-cloud-vertex-ai)
- [Microsoft Foundry](https://claude.com/partners/microsoft-foundry)
- [Console login](https://platform.claude.com/)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](https://claude.com/partners)
- [Community](https://claude.com/community)
- [Connectors](https://claude.com/connectors)
- [Courses](/learn)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](/engineering)
- [Events](/events)
- [Plugins](https://claude.com/plugins)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Startups](https://claude.com/programs/startups)
- [Research Labs](https://claude.com/programs/claude-team-plan-for-research-labs)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](/company)
- [Careers](/careers)
- [Policy](/policy)
- [Economic Futures](/economic-futures)
- [Research](/research)
- [News](/news)
- [Claude’s Constitution](/constitution)
- [Claude Corps](/claude-corps)
- [Keep thinking](https://www.anthropic.com/path-to-hope)
- [Policy on the AI Exponential](/policy-on-the-ai-exponential)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com/)
- [Transparency](/transparency)
