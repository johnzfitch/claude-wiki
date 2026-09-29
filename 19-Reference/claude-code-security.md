---
title: "Making frontier cybersecurity capabilities available to defenders \\ Anthropic"
source_url: "https://www.anthropic.com/news/claude-code-security"
category: "19-Reference"
fetched_at: "2026-08-02T05:41:40Z"
tags: ["claude-code", "news-research", "security"]
---

# Making frontier cybersecurity capabilities available to defenders

Feb 20, 2026

**Claude Code Security**, a new capability built into Claude Code on the web, is now available in a limited research preview. It scans codebases for security vulnerabilities and suggests targeted software patches for human review, allowing teams to find and fix security issues that traditional methods often miss.  
  
Security teams face a common challenge: too many software vulnerabilities and not enough people to address them. Existing analysis tools help, but only to a point, as they usually look for known patterns. Finding the subtle, context-dependent vulnerabilities that are often exploited by attackers requires skilled human researchers, who are dealing with ever-expanding backlogs.

AI is beginning to change that calculus. We’ve recently shown that [Claude can detect novel, high-severity vulnerabilities](https://red.anthropic.com/2026/zero-days/). But the same capabilities that help defenders find and fix vulnerabilities could help attackers exploit them.

Claude Code Security is intended to put this power squarely in the hands of defenders and protect code against this new category of AI-enabled attack. We’re releasing it as a limited research preview to Enterprise and Team customers, with expedited access for maintainers of open-source repositories, so we can work together to refine its capabilities and ensure it is deployed responsibly.

## **How Claude Code Security works**

Static analysis—a widely deployed form of automated security testing—is typically rule-based, meaning it matches code against known vulnerability patterns. That catches common issues, like exposed passwords or outdated encryption, but often misses more complex vulnerabilities, like flaws in business logic or broken access control.

Rather than scanning for known patterns, Claude Code Security reads and reasons about your code the way a human security researcher would: understanding how components interact, tracing how data moves through your application, and catching complex vulnerabilities that rule-based tools miss.

Every finding goes through a multi-stage verification process before it reaches an analyst. Claude re-examines each result, attempting to prove or disprove its own findings and filter out false positives. Findings are also assigned severity ratings so teams can focus on the most important fixes first.

Validated findings appear in the Claude Code Security dashboard, where teams can review them, inspect the suggested patches, and approve fixes. Because these issues often involve nuances that are difficult to assess from source code alone, Claude also provides a confidence rating for each finding. Nothing is applied without human approval: Claude Code Security identifies problems and suggests solutions, but developers always make the call.

## **Using Claude for cybersecurity**

Claude Code Security builds on more than a year of research into Claude’s cybersecurity capabilities. Our Frontier Red Team has been stress-testing these abilities systematically: entering Claude in [competitive Capture-the-Flag events](https://red.anthropic.com/2025/ai-for-cyber-defenders/), partnering with Pacific Northwest National Laboratory to [experiment with using AI to defend critical infrastructure](2026-critical-infrastructure-defense.md), and refining Claude’s ability to find and patch real vulnerabilities in code.

Claude’s cyberdefensive abilities have improved substantially as a result. Using [Claude Opus 4.6](claude-opus-4-6.md), released earlier this month, our team [found over 500 vulnerabilities](https://red.anthropic.com/2026/zero-days/) in production open-source codebases—bugs that had gone undetected for decades, despite years of expert review. We’re working through triage and responsible disclosure with maintainers now, and we plan to expand our security work with the open-source community.

We also use Claude to review our own code, and we’ve found it to be extremely effective at securing Anthropic’s systems. We built Claude Code Security to make those same defensive capabilities more widely available. And since it’s built on Claude Code, teams can review findings and iterate on fixes within the tools they already use.

## **The road ahead**

This is a pivotal time for cybersecurity. We expect that a significant share of the world’s code will be scanned by AI in the near future, given how effective models have become at finding long-hidden bugs and security issues.

Attackers will use AI to find exploitable weaknesses faster than ever. But defenders who move quickly can find those same weaknesses, patch them, and reduce the risk of an attack. Claude Code Security is one step towards our goal of more secure codebases and a higher security baseline across the industry.

## **Getting started**

We’re opening a limited research preview of Claude Code Security to Enterprise and Team customers today. Participants will get early access and collaborate directly with our team to hone the tool’s capabilities. We also encourage open-source maintainers to apply for free, expedited access.

[Apply for access here](https://claude.com/contact-sales/security).

To learn more, visit [claude.com/solutions/claude-code-security](../18-Industry-UseCases/claude-code-security.md).


## Related content

### Investigating three real-world incidents in our cybersecurity evaluations

[Read more](investigating-incidents-cybersecurity-evals.md)

### Our position on open-weights models

[Read more](position-open-weights-models.md)

### Cognizant and Anthropic expand their partnership to bring Claude to enterprise clients

[Read more](cognizant-anthropic.md)

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
- [Claude for Chrome](https://claude.com/chrome)
- [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365)
- [Skills](https://www.claude.com/skills)
- [Download app](https://claude.ai/download)
- [Pricing](../17-Billing-Plans/pricing.md)
- [Log in to Claude](https://claude.ai/)

### Models

- [Mythos](../15-Claude-AI-Features/claude-mythos.md)
- [Fable](../15-Claude-AI-Features/claude-fable.md)
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
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
- [Courses](https://www.anthropic.com/learn)
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
- [Research Labs](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.anthropic.com/)
- [Support center](https://support.claude.com/en/)

### Company

- [Anthropic](company.md)
- [Careers](https://www.anthropic.com/careers)
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
