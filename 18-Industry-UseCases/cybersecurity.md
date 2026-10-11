---
title: "Claude for Cybersecurity | Claude by Anthropic"
source_url: "https://www.claude.com/solutions/cybersecurity"
category: "18-Industry-UseCases"
fetched_at: "2026-10-10T06:26:08Z"
tags: ["case-studies", "enterprise", "security"]
---

# Defense at the pace threats now demand

Frontier AI models have surpassed all but the most skilled humans at finding and exploiting software vulnerabilities. Within months, we expect these capabilities will proliferate across AI models and become widely accessible to everyone, including attackers.

Defenders across industries, research, open source, and government must act to find and fix what’s exposed today, and build a durable advantage that drives vulnerabilities ever closer to zero in the future.

01

### State of cybersecurity

Insights on model capabilities today, including Claude Mythos.

[Skip to](#state-of-cybersecurity)

02

### Products and technology

Security-tuned models and tools you can deploy today.

[Skip to](#products-and-technology)

03

### Commitments

Open-source support, critical-systems defense, and policy advocacy.

[Skip to](#commitments)

04

### Resources

Cybersecurity resources, including research, guides, and field insights.

[Skip to](#resources)

The state of cybersecurity

## Where frontier capability stands today

Models can build working exploits, defeat security walls, or help defenders ship fixes at scale. The outcome depends on how they’re used.

Capability

Remediation

Interactive demo — open this page on a larger screen to try it

### From finding flaws to full system control

A year ago, the most capable AI models could spot security flaws but couldn't reliably exploit them. Today, in the wrong hands, they can — and not just in simple software. Mythos Preview is the first model to consistently break through the sandbox protections modern browsers and operating systems rely on; other frontier models still stop at the wall. Defenses built on last year's assumptions are already behind.

[Read Red Team research (opens in new tab)](https://red.anthropic.com/2026/exploit-evals/)

Reading the chart

Capability trends downward as tasks get harder. T5 is "the model reaches vulnerable code." Only Mythos Preview passed T1: "the model fully controls the system."

### Tipping the scales to defenders

In March 2026, Mozilla shipped fixes for vulnerabilities found by Claude Opus 4.6, the model that found hundreds of bugs in open source software that survived decades of human review. With Mythos Preview, Mozilla shipped an additional 271 fixes in the April release, more than 20 times their monthly average. Says Bobby Holley, CTO of Firefox, “Defenders finally have a chance to win, decisively.”

[Read Mozilla research (opens in new tab)](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

Inside Mozilla's review process

The model expands what gets reviewed, and humans decide what gets patched.

Safeguards

### Our approach to dual-use frontier capabilities

Claude Opus and Mythos-class models have significantly stronger cybersecurity capabilities than previous generations, especially in exploit reasoning. As capabilities across all model classes continue to advance, we make our frontier models available under responsible safeguards that give defenders an advantage while limiting the potential for misuse.

- ### Securing critical software

  Through the Anthropic Cyber Mission, we’re partnering with organizations that maintain critical infrastructure and widely used software, so the systems the world depends on are hardened first.

  [Learn more (opens in new tab)](../19-Reference/anthropic-cyber-mission.md)

- ### Verification program

  Cybersecurity practitioners whose legitimate work overlaps with dual use categories can apply for the Cyber Verification Program for adjusted safeguards.

  [Apply now](https://portal.anthropic.com/programs)

- ### Mythos-powered defense

  Security teams can put frontier reasoning to work on their defense today through Claude Security alongside products and services delivered through trusted partners.

  [Learn more](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)

Project Glasswing

## Our approach to dual-use with Claude Mythos models

Claude Mythos Preview, and now Claude Mythos 5, are models with significantly stronger cybersecurity capabilities, especially in exploit reasoning. As this capability carries the greatest potential for misuse in security, we are limiting initial access to a small number of partners through Project Glasswing. Claude Fable 5 is our Mythos-class model safe for general use through additional safeguards. [Read the latest (opens in new tab)](../19-Reference/claude-fable-5-mythos-5.md)

## Securing critical software

Glasswing partners maintain critical infrastructure or software the world depends on, where a successful attack would be catastrophic.

## Expanding through trusted access

We are working toward steadily expanding access to Claude Mythos 5 through a trusted access program, and will share more soon.

## Providing tools for defenders today

[Claude Security (opens in new tab)](../15-Claude-AI-Features/product-claude-security.md), the open-source reference tools, and the practices emerging from Project Glasswing are available to all security teams.

## Backing defenders with resources

## 50+

12 founding members and 40+ organizations joined us in stewarding open-source infrastructure

## \$100M

In usage credits from Anthropic to Glasswing partners defending critical infrastructure

## \$4M

In direct donations to OpenSSF, Alpha-Omega, and the Apache Software Foundation

## Organizations defending critical software with Claude Mythos

## How security teams put Claude to work for defense

Across enterprise security programs and inside Anthropic, teams use Claude to improve risk posture.

[Learn more](../15-Claude-AI-Features/product-claude-security.md)

Claude Security

Claude Code

Claude Developer Platform

### Find and fix vulnerabilities with Claude Security

Claude Security reasons about your code like a security researcher: scanning for vulnerabilities, validating findings, and proposing targeted patches.

[Start defending](../15-Claude-AI-Features/product-claude-security.md)

### Ship secure code in your CI/CD workflow

Use the Code Review skill to set up automated PR reviews to catch logic errors, security vulnerabilities, and regressions across your full codebase.

[Start reviewing](../15-Claude-AI-Features/product-claude-code-fad1ab4b.md)

### Deploy security agents with the Claude Developer Platform

Ship defender tools and custom security agents with sandboxed execution, credential isolation, and audit logging built in via the Agent SDK, MCP, and Claude API.

[Start building](https://www.claude.com/platform/api)

"Anthropic prioritized safety and security a lot more than other LLMs... As the largest cybersecurity company, that's a big deal for us." - Gunjan Patel, Director of Engineering

“Claude consistently performed best on complex, agentic workflows, especially multi-step investigations requiring policy adherence and sustained reasoning across multiple tools.” - Anirudh Ravula, Head of AI

“The industry has always moved too slowly compared to attackers. AI is like giving defenders a jetpack when they've been limited to walking.” - Martin Holste, CTO of Cloud & AI

1 of 3

### Build threat context

Give scanning and response a map to work from. Claude derives a threat model from your codebase and past vulnerabilities, then enriches raw indicators with infrastructure links, attribution, and ATT&CK mapping, so analysts start with context.

- [Open source: Threat Intel Enrichment agent](https://platform.claude.com/cookbook/tool-use-threat-intel-enrichment-agent)

  (opens in new tab)
- [Open source: Threat Model skill](https://github.com/anthropics/defending-code-reference-harness/tree/main/.claude/skills/threat-model#threat-model)

  (opens in new tab)

### Vulnerability detection

Claude reads source code the way a researcher does, reasoning about reachability and exploitability, catching vulnerabilities that static tools often miss. A separate triage pass re-verifies every finding to help reduce false positives.

- [In Claude Security](../15-Claude-AI-Features/product-claude-security.md)

  (opens in new tab)
- [Open source: Vulnerability detection agent](https://platform.claude.com/cookbook/claude-agent-sdk-06-the-vulnerability-detection-agent)

  (opens in new tab)

### Patching

Findings now arrive faster than teams can fix them. Claude traces each one to its root cause, locates sibling call sites with the same flaw, and writes a minimal diff with a regression test for your team to review.

- [In Claude Security](../15-Claude-AI-Features/product-claude-security.md)

  (opens in new tab)
- [Open source: Patching skill](https://github.com/anthropics/defending-code-reference-harness/blob/main/.claude/skills/patch/SKILL.md#patch)

  (opens in new tab)

### Triage and verify findings

Hand Claude raw findings from any scanner and get back insights. Claude reads the surrounding code to confirm exploitability, deduplicates by root cause, and ranks by precondition and impact, so engineers can focus and work on real issues first.

- [In Claude Security](../15-Claude-AI-Features/product-claude-security.md)

  (opens in new tab)
- [Open source: Triage skill](https://github.com/anthropics/defending-code-reference-harness/tree/main/.claude/skills/triage)

  (opens in new tab)

### Security review across the dev loop

Review code for security at every stage of development. Claude checks its own edits as it writes and fixes issues in the same session, then specialized agents re-examine pull requests against your codebase, posting verified findings inline without blocking your review gates.

- [Security guidance in Claude Code](../02-Claude-Code-CLI/security-guidance.md)

  (opens in new tab)
- [Code Review in Claude Code](../02-Claude-Code-CLI/code-review.md)

  (opens in new tab)

### Secure source code, end to end

As offensive capability accelerates, the find-and-fix loop has to close faster. Claude runs threat modeling, discovery, verification, triage, and patching as one continuous loop on your codebase, carrying context across every stage so each finding arrives at the fix with its full history.

- [Using LLMs to secure source code](https://www.claude.com/resources/articles/using-llms-to-secure-source-code)

  (opens in new tab)

Customer story

Cogent resolves security threats 97% faster with Claude

[Read story (opens in new tab)](cogent.md)

Claude Opus

500+

high-severity vulnerabilities found that survived decades of scrutiny and automated analysis

## Cyber defense powered by Claude, available through our partners

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

- 

Frontier capabilities

### Leverage powerful models for defense

Claude reads code carefully, understands real risks, and sustains the long workflows that continuous defense requires. Verified practitioners can request [adjusted safeguards](https://support.claude.com/en/articles/14604842) for dual-use work.

[Learn more (opens in new tab)](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)

## Anthropic’s commitment to cyberdefense

Frontier AI capabilities are advancing faster than any single team can respond to. Through the Anthropic Cyber Mission, we work with the maintainers, vendors, operators, and public-sector defenders who protect the systems everyone shares.

### Supporting open-source security

The internet runs on critical software maintained by people with limited resources. We scan important projects with Claude, fund the organizations helping maintainers fix what's found, and disclose vulnerabilities responsibly when Claude finds them.

- [Enroll your project in OSS Scanner](http://red.anthropic.com/oss-scanner)

  (opens in new tab)
- [Apply for a free Claude Max account for maintainers](https://claude.com/contact-sales/claude-for-oss)

  (opens in new tab)
- [Read our CVD policy](https://www.anthropic.com/coordinated-vulnerability-disclosure)

  (opens in new tab)

### Defending critical infrastructure

Power grids, water systems, and factories run on technology that often can't be taken offline to patch. Our Critical Infrastructure Defense Program brings frontier Claude models to the consulting firms, security companies, and equipment makers operators already rely on, alongside our research with Pacific Northwest National Laboratory (PNNL) on defending cyber-physical systems.

- [Read about the Critical Infrastructure Defense Program](http://anthropic.com/news/cyber-resilience-initiative)

  (opens in new tab)
- [Read about Anthropic and PNNL](../19-Reference/2026-critical-infrastructure-defense.md)

### Advocating for policy that backs defenders

Our Advanced AI Framework proposes policies for binding obligations on frontier labs, Anthropic included, and government authority to block dangerous deployments, alongside investment in open-source hardening and the safeguards that would let frontier cyber capability reach more defenders safely.

- [Read the Advanced AI Framework](https://www.anthropic.com/policy-on-the-ai-exponential/aaif)

  (opens in new tab)

## Go deeper on cyberdefense

Everything you need to strengthen your defense posture, from research to implementation guides.

Research

Guides

In the field

TitleDate

- [GLM-5.3 and the spread of advanced cyber capabilitiesDateSeptember 29, 2026](../19-Reference/glm-5-3-and-the-spread-of-advanced-cyber-capabilities.md)
- [Countering misuse of AI: September 2026DateSeptember 10, 2026](https://www.anthropic.com/threat-intelligence-report-september-2026)
- [Discovering cryptographic weaknesses with ClaudeDateJuly 28, 2026](../19-Reference/discovering-cryptographic-weaknesses.md)
- [Measuring LLMs’ impact on N-day exploitsDateJune 8, 2026](https://red.anthropic.com/2026/n-days/)
- [Mapping AI-enabled cyber threats: Insights from the LLM ATT&CK NavigatorDateJune 3, 2026](../19-Reference/attack-navigator.md)
- [Expanding Project GlasswingDateJune 2, 2026](../19-Reference/expanding-project-glasswing.md)
- [Project Glasswing: An initial updateDateMay 22, 2026](../19-Reference/glasswing-initial-update.md)
- [Measuring LLMs’ ability to develop exploitsDateMay 22, 2026](https://red.anthropic.com/2026/exploit-evals/)
- [Anthropic's coordinated vulnerabilty disclosure dashboardDateMay 22, 2026](https://red.anthropic.com/2026/cvd/)
- [Assessing Claude Mythos Preview’s cybersecurity capabilitiesDateApril 7, 2026](../19-Reference/2026-mythos-preview.md)
- [Reverse engineering Claude's CVE-2026-2796 exploitDateMarch 6, 2026](https://red.anthropic.com/2026/exploit/)
- [LLM-discovered 0-daysDateFebruary 5, 2026](https://red.anthropic.com/2026/zero-days/)
- [AI models on realistic cyber rangesDateJanuary 16, 2026](../19-Reference/2026-cyber-toolkits-update.md)
- [Finding Bugs with Claude and Property-based TestingDateJanuary 14, 2026](https://red.anthropic.com/2026/property-based-testing/)
- [Experimenting with AI to Defend Critical InfrastructureDateJanuary 8, 2026](../19-Reference/2026-critical-infrastructure-defense.md)

Titlecontent typeDate

- [Developing Enterprise Frontier Safeguards with our customerscontent typeGuideDateSeptember 1, 2026](../19-Reference/enterprise-frontier-safeguards.md)
- [Getting started with Claude Securitycontent typeTutorialDateOctober 7, 2026](https://academy.claude.com/tutorials/getting-started-with-claude-security)
- [Using LLMs to secure source codecontent typeBlogDateMay 27, 2026](https://www.claude.com/resources/articles/using-llms-to-secure-source-code)
- [Zero Trust for AI Agentscontent typeeBookDateMay 27, 2026](https://www.claude.com/resources/articles/zero-trust-for-ai-agents)
- [Secure the Advantage: A CISO's Guide to Agentic AIcontent typeBlogDateMay 12, 2026](https://claude.com/resources/webinars/secure-the-advantage-a-cisos-guide-to-agentic-ai)
- [Vulnerability Detection Agentcontent typeCookbookDateApril 22, 2026](https://platform.claude.com/cookbook/claude-agent-sdk-06-the-vulnerability-detection-agent)
- [Preparing Your Security Program for AI-Accelerated Offensecontent typeBlogDateApril 10, 2026](https://www.claude.com/resources/articles/preparing-your-security-program-for-ai-accelerated-offense)
- [Threat Intelligence Enrichment Agentcontent typeCookbookDateApril 7, 2026](https://platform.claude.com/cookbook/tool-use-threat-intel-enrichment-agent)

Titlecontent typeDate

- [Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenderscontent typeBlogDateAugust 21, 2026](https://claude.com/resources/articles/bringing-claude-mythos-5-to-more-defenders)
- [Claude Security: Putting Claude to Work for Defenderscontent typeWebinarDateMay 28, 2026](https://claude.com/resources/webinars/claude-security-putting-claude-to-work-for-defenders)
- [How our partners are putting Opus to work for cybersecuritycontent typeBlogDateMay 21, 2026](https://www.claude.com/resources/articles/how-our-partners-are-putting-opus-to-work-for-cybersecurity)
- [How Anthropic's cybersecurity team built a threat detection platform with Claude Codecontent typeBlogDateMay 12, 2026](https://www.claude.com/resources/articles/how-anthropic-uses-claude-cybersecurity)
- [Long Running Agents: How Outtake built a Cyber investigator on Claudecontent typeWebinarDateApril 28, 2026](https://claude.com/resources/webinars/outtake-built-cyber-investigator-claude)
- [Partnering with Mozilla to improve Firefox's securitycontent typeBlogDateMarch 6, 2026](../19-Reference/2026-firefox.md)

## Give defenders an edge with Claude

[Contact sales](https://www.claude.com/contact-sales)[Start building](../04-API-Reference/Other/usage-limits.md)

[](https://www.claude.com/)

© 2026 Anthropic PBC

## Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/product-claude-code-fad1ab4b.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../15-Claude-AI-Features/product-tag.md)
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

- [Overview](../17-Billing-Plans/pricing-enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial advisors](financial-advisors.md)
- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Campus](../15-Claude-AI-Features/programs-campus.md)
- [Frontier Academy](../15-Claude-AI-Features/programs-frontier-academy.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)
- [Startups](../15-Claude-AI-Features/programs-startups.md)

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

- [Overview](https://www.claude.com/resources)
- [Articles](https://www.claude.com/resources/articles)
- [Webinars](https://www.claude.com/resources/webinars)
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
- [Claude Code](../15-Claude-AI-Features/product-claude-code-fad1ab4b.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../15-Claude-AI-Features/product-tag.md)
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

- [Overview](../17-Billing-Plans/pricing-enterprise.md)
- [Claude Code for Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)

## Departments

- [Customer support](customer-support.md)
- [Cybersecurity](cybersecurity.md)
- [Legal](legal.md)
- [Sales](sales.md)

## Industries

- [Financial advisors](financial-advisors.md)
- [Financial services](finance.md)
- [Government](government.md)
- [Healthcare](healthcare.md)
- [Higher education](education.md)
- [K-12 teachers](teachers.md)
- [Life sciences](life-sciences.md)
- [Nonprofits](nonprofits.md)
- [Small business](small-business.md)

## Programs

- [Campus](../15-Claude-AI-Features/programs-campus.md)
- [Frontier Academy](../15-Claude-AI-Features/programs-frontier-academy.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)
- [Startups](../15-Claude-AI-Features/programs-startups.md)

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

- [Overview](https://www.claude.com/resources)
- [Articles](https://www.claude.com/resources/articles)
- [Webinars](https://www.claude.com/resources/webinars)
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
