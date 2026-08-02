---
title: "Making frontier cybersecurity capabilities available to defenders \\ Anthropic"
source_url: "https://www.anthropic.com/news/claude-code-security"
category: "19-Reference"
fetched_at: "2026-08-02T05:41:40Z"
tags: ["claude-code", "security"]
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

Claude Code Security builds on more than a year of research into Claude’s cybersecurity capabilities. Our Frontier Red Team has been stress-testing these abilities systematically: entering Claude in [competitive Capture-the-Flag events](https://red.anthropic.com/2025/ai-for-cyber-defenders/), partnering with Pacific Northwest National Laboratory to [experiment with using AI to defend critical infrastructure](https://red.anthropic.com/2026/critical-infrastructure-defense/), and refining Claude’s ability to find and patch real vulnerabilities in code.

Claude’s cyberdefensive abilities have improved substantially as a result. Using [Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6), released earlier this month, our team [found over 500 vulnerabilities](https://red.anthropic.com/2026/zero-days/) in production open-source codebases—bugs that had gone undetected for decades, despite years of expert review. We’re working through triage and responsible disclosure with maintainers now, and we plan to expand our security work with the open-source community.

We also use Claude to review our own code, and we’ve found it to be extremely effective at securing Anthropic’s systems. We built Claude Code Security to make those same defensive capabilities more widely available. And since it’s built on Claude Code, teams can review findings and iterate on fixes within the tools they already use.

## **The road ahead**

This is a pivotal time for cybersecurity. We expect that a significant share of the world’s code will be scanned by AI in the near future, given how effective models have become at finding long-hidden bugs and security issues.

Attackers will use AI to find exploitable weaknesses faster than ever. But defenders who move quickly can find those same weaknesses, patch them, and reduce the risk of an attack. Claude Code Security is one step towards our goal of more secure codebases and a higher security baseline across the industry.

## **Getting started**

We’re opening a limited research preview of Claude Code Security to Enterprise and Team customers today. Participants will get early access and collaborate directly with our team to hone the tool’s capabilities. We also encourage open-source maintainers to apply for free, expedited access.

[Apply for access here](https://claude.com/contact-sales/security).

To learn more, visit [claude.com/solutions/claude-code-security](http://claude.com/solutions/claude-code-security).


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
