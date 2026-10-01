---
title: "Expanding Project Glasswing \\ Anthropic"
source_url: "https://www.anthropic.com/news/expanding-project-glasswing"
category: "19-Reference"
fetched_at: "2026-09-10T06:43:59Z"
tags: ["news-research"]
---

# Expanding Project Glasswing

Jun 2, 2026

[Project Glasswing](../22-Safety-Policy/glasswing.md) is our collaborative effort to secure the world’s most important software. In early April, we announced that roughly 50 initial partners had access to Claude Mythos Preview, and since then, they’ve been deploying the model to scan their codebases for vulnerabilities. We recently [described](glasswing-initial-update.md) how these partners have so far found more than 10,000 high- or critical-severity security flaws.

We’re now expanding Project Glasswing. Following several weeks of close collaboration with our Project Glasswing partners, the security industry, open-source software maintainers, and the US government, we’re extending the partnership to approximately 150 new organizations. Each one will need to meet our security requirements before they gain access.

The organizations in this new group are based in more than 15 countries, and most provide critical infrastructure to many more. (In the future, we intend to expand our geographical reach much further.) The group covers several industries that weren’t well represented in our initial cohort, such as power, water, healthcare, communications, and hardware. And many of the new partners are vendors—companies or nonprofits that maintain codebases that are relied upon by lots of other organizations around the world, including governments.

What each partner has in common is that a successful attack on their codebase could be catastrophic. For most partners, we estimate that a major attack could affect more than 100 million people, with important ramifications for both global and national security.

This expansion is the next step toward our long-term goals: for AI to make *all* software more secure, and for us to help the industry adjust to how AI could change many of the core assumptions of cybersecurity.

## The role of Project Glasswing

Project Glasswing and the capabilities of Claude Mythos Preview have sparked broad conversations—both within the software industry and with governments—about how AI is changing cybersecurity. These conversations have informed how we’ve expanded the program. They’ve also shaped our thinking about the very purpose of Project Glasswing.

Cheap, fast AI models with powerful cyber capabilities are around the corner. We want Project Glasswing to spur institutions toward operating norms that reflect this reality.

Mythos Preview continues a long-term trend that we’ve been warning about for some time: within 6 to 12 months, we expect that many other AI companies will have Mythos-class models, and they could release them without safeguards that prevent misuse. In that world, cyberattacks could occur much more often, and in much more unpredictable forms. It’s imperative that cyberdefenders [adapt to maintain pace](glasswing-initial-update.md).

We see our role as twofold. First, to help the software industry adapt by safely providing wide access to better models, tools, and common infrastructure. Second, to steadily shift the support we provide, from finding vulnerabilities to disclosing, fixing, and deploying patched software. We’ll now discuss each of these in turn.

### Supporting cyberdefenders

So far, companies, nonprofits, maintainers, and researchers have acted quickly. Within the first weeks of Project Glasswing, each member began using Mythos Preview at large scale, sharing information and best practices with other partners, and working with third parties to triage the model’s findings. These organizations’ methods for adapting to new tools can, and should, be replicated widely across the millions of organizations and developers who are vulnerable to cyberattacks.

To support this, we recently released [Claude Security](../15-Claude-AI-Features/product-claude-security.md), a product that uses our latest public frontier models, like Claude Opus 4.8, to scan codebases and suggest patches. We're also releasing—on request, to trusted security teams—[the tools](glasswing-initial-update.md) we developed to help Project Glasswing’s partners find vulnerabilities more quickly.

We intend to go much further: our longer-term aim is to support the industry in creating new initiatives, standards, and infrastructure for the era of powerful cyber models.

### Accelerating patching and the rest of security

As we’ve [previously discussed](glasswing-initial-update.md), the bottleneck in cybersecurity is now verifying, disclosing, and patching the large numbers of vulnerabilities that Mythos-class models can surface.

Mythos Preview itself can help. Many of Project Glasswing’s partners now use the model to write patches, as well as for pre-release checks that prevent vulnerabilities from appearing in the first place. Models like Mythos Preview can also be used for penetration testing (simulating a cyberattack to identify how vulnerabilities might be exploited), automating threat detection and response, and rebuilding legacy codebases in memory-safe languages, among many other defensive tasks.

We’re in discussions with third parties about how we might substantially scale up the reviewing and patching of vulnerabilities in open-source software. We’re also working on sharing ideas and best practices for disclosing vulnerabilities to open-source maintainers, with the intent of making these reports easier to triage and to act upon.

## The path ahead

To address the scale of this coming challenge, hundreds of thousands of organizations, researchers, and maintainers will likely need access to the most advanced cyber capabilities and tools available.

We’re working as quickly as we can to safely release Mythos-level capabilities in general access. To do so, we’ll need highly robust safeguards that prevent the model’s cyber capabilities from being misused—safeguards that we (and, to our knowledge, all other AI developers) have yet to develop. Because cybersecurity has both helpful and destructive uses, making safeguards that are both strong and precise enough is a major challenge.

In the meantime, we plan to expand Project Glasswing even further—prioritizing additional essential infrastructure providers, maintainers of critical open-source software, and safety testers. We intend for future expansions to cover organizations in the US and overseas, just as this one does. We also intend to scale up our Cyber Verification Program, which would grant Mythos-class capabilities to many more organizations for specific cyberdefense tasks.

In the future, frontier model releases will become increasingly high-stakes. Capabilities will continue to improve across all domains, including many that—like cybersecurity—can empower attackers and defenders alike. This will not be the last time we need to confront a challenge like this one. But Project Glasswing has taught us a great deal about how to respond when models cross important capability thresholds. If we’re successful, we hope to enable a permanent advantage for defenders.


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
