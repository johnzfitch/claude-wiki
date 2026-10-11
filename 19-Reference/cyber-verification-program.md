---
title: "Expanding the Cyber Verification Program \\ Anthropic"
source_url: "https://www.anthropic.com/news/cyber-verification-program"
category: "19-Reference"
fetched_at: "2026-10-08T06:25:30Z"
tags: ["news-research"]
---

# Expanding the Cyber Verification Program

Oct 6, 2026

We’re launching a new, expanded version of our Cyber Verification Program (CVP), which makes advanced cyber capabilities and reduced blocking classifiers available to qualifying security professionals. The program now consists of three access tiers, which allow security teams to apply for the level of access that best suits their work. Each tier includes access to our most capable models, including Claude Opus 5.5, Claude Sonnet 5.5, Claude Mythos 5.1, and new models moving forward. Interested customers can [apply here](https://portal.anthropic.com/programs/cvp).

Cybersecurity is inherently dual use: the same capabilities that enable a security team to find and fix a vulnerability can also help a malicious actor exploit it. For this reason, our generally available models, such as [Claude Opus 5.5](../15-Claude-AI-Features/claude-opus-5-5.md), [Claude Fable 5.1](../15-Claude-AI-Features/claude-fable-and-mythos-5-1.md), and [Claude Sonnet 5.5](../15-Claude-AI-Features/claude-sonnet-5-5.md), have conservative cyber safeguards that block most cyber work. This is intended to limit the harmful activities malicious actors can carry out using our models, while we continue to work to reduce false positives for secure coding.

But defenders also need access to the best tools and most powerful capabilities to secure their systems. For the past six months, we’ve enabled trusted access through two programs: [Project Glasswing](../22-Safety-Policy/glasswing.md) and the [CVP](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet). The former gave a group of organizations securing the most critical software access to Claude Mythos; the latter gave vetted security teams access to reduced safeguards on Claude Opus and Claude Sonnet models.

Now, we’re integrating these programs into one expanded offering, designed to give more security organizations access to the capabilities they need to protect their systems.

###  New access tiers

The updated access tiers make specific model capabilities available to security professionals based on the scope of their cyber work. Each has different verification requirements and security controls.

**Defense Access** is for defensive work, including security operations center and incident response tasks, reverse-engineering malware, and analyzing and validating vulnerabilities. Examples of qualifying organizations include security teams at companies, nonprofits, universities, and government bodies who are defending systems they own or maintain; operators of critical infrastructure of any size, such as regional hospitals or municipal utilities; smaller security firms; open-source maintainers; and individual researchers with a track record of reported vulnerabilities.

We expect many organizations conducting defensive cybersecurity work to qualify for this tier. We aim to respond to applications within a few days.

**Red Team Access** adds authorized penetration testing and red-teaming to the defensive uses above. Examples of qualifying organizations include in-house red teams, government red teams, and security and penetration testing firms. Organizations in this tier can only perform adversarial testing against systems they are authorized to test, including IT systems in critical industries. Users will still experience real-time blocks on actions that could cause physical harm or mass disruption, such as deploying ransomware, damaging physical systems, or pen testing high-risk safety systems.

Given the increased eligibility requirements and security controls, we expect applications in this tier to take a few weeks to review. Qualifying organizations will be enrolled in the Defense Access tier while we review their Red Team Access applications. Currently, this tier is for organizations only; individual researchers are not eligible.

**Specialized Access**, which has the fewest cyber blocks, is reserved for a limited set of verified organizations that are authorized to test safety systems that could impact people’s lives or disrupt markets, such as flight operating systems, power grids, telecom networks, interbank transfer infrastructure, and government administrative networks.

For this tier, we currently review every organization in depth in collaboration with the US government. Existing members of Project Glasswing will transition to this tier and do not require reapproval for current models.

Our generally available models can continue to be used for tasks such as code review, patching known issues, vulnerability finding in owned source code, and triage of security alerts.

Data retention is required for organizations enrolled in the program so that we can monitor for cyber misuse. Once [Enterprise Frontier Safeguards](enterprise-frontier-safeguards.md) (EFS)—a new solution that combines the privacy of zero data retention with robust safeguards—is available later this fall, eligible organizations will be able to store data in cloud infrastructure they control. Until EFS is available, organizations with access to Claude Fable 5.1 or Claude Mythos 5.1 with zero data retention can also use CVP with zero data retention. To register interest in EFS, [fill out this form](https://claude.com/form/enterprise-frontier-safeguards).

Below, we share an overview of what’s available at each CVP access level, as well as requirements for security and privacy controls:

###  Testing the efficacy of our tiers

To assess the efficacy of our CVP protections, we ran Claude Opus 5.5 through CyScenarioBench—an evaluation that measures whether models can plan and execute multi-stage cyber operations under realistic constraints—with safeguards tuned for our different CVP tiers. Because this evaluation involves complex, interactive offensive scenarios, we would expect Claude to experience significant blocks both on the generally available model and in the Defense Access tier, while experiencing no blocks in the Red Team Access and Specialized Access tiers.

Across five attempts at each of the 10 CyScenarioBench challenges in each access tier, we found that:

- Without CVP access, every task was blocked on the first prompt;
- In the Defense Access tier, 46 of the 50 trials were blocked at some point in the challenge, while the remaining four tasks succeeded; and
- In the Red Team Access tier, no blocks occurred, and Claude Opus 5.5 successfully completed 34 of the 50 tasks—effectively equivalent to the model’s 67.6% success rate on this evaluation with no safeguards applied (representative of Specialized Access).

These evaluations give us confidence that we can make advanced cyber capabilities safely available to a broader set of defenders, expanding the defensive efforts we began with Project Glasswing. We will continue to refine our tier-based classifiers over time.

## Giving defenders the advantage

Through Project Glasswing, we found that Claude Mythos models significantly increased the rate at which organizations were able to identify vulnerabilities in their systems. Through the program, our partners uncovered at least 129,000 verified software vulnerabilities between April and July 2026. And through our own open-source scanning efforts, we found an additional 5,500 verified software vulnerabilities between April and October 2026. Of these verified vulnerabilities, more than 33,000 have so far been rated as critical- or high-severity. This is likely an undercount, as it is based on survey data from only a subset of Glasswing partners. As such, we expect the true impact to be at least five times higher.

When asked how long it would have taken them to find the same number of vulnerabilities without Claude Mythos models, several partners told us that the models had increased their rate of vulnerability finding by months or even years. Read more from our partners at [Booz Allen and Comcast](https://claude.com/blog/how-comcast-booz-allen-use-claude-mythos-to-secure-their-codebases) about their experience.

The changes we’re making to our Cyber Verification Program today are intended to extend the impact of Project Glasswing to a much larger number of cyber defenders. We’re also continuing our efforts to help secure open-source software and critical infrastructure. In the coming weeks, we’ll share more about this work and what we’ve learned as we continue to work to give defenders a permanent advantage.

## Apply for access

Interested organizations can [apply to CVP here](https://portal.anthropic.com/programs/cvp). As part of the application process, we will verify all applicants and request proof of the required security controls for the relevant access tier. Existing CVP members will keep their current settings for previous models and will be automatically evaluated for access to Claude Opus 5.5, Claude Sonnet 5.5, and Claude Mythos 5.1 through the updated program. Admins will need to assign access to specific workspaces by following [these steps](../21-Account-Support/assign-a-program-to-workspaces-in-claude-console.md).

CVP is available on the Claude Platform, Google Cloud’s Vertex AI, and Microsoft Foundry. CVP is only available on Amazon Bedrock for customers eligible for [Enterprise Frontier Safeguards](enterprise-frontier-safeguards.md).

If you’re blocked on work you think your tier should allow, you can [report it here](https://claude.com/form/cyber-block-false-positive-report-cvp-rejection-appeal). Full details on each tier can be found in our [Help Center](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet).


## Related content

### Anthropic invests \$100 million to train 10,000 engineers and tackle the enterprise AI talent gap

Anthropic is investing \$100 million in Claude Frontier Academy to train 10,000 Frontier Deployed Engineers by the end of 2027, with cohorts from Accenture, Bain, CBA, Deloitte, McKinsey, Morgan Stanley and Novo Nordisk already underway.

[Read more](claude-frontier-academy.md)

### Barclays scales Claude to upgrade operations and improve client experience

Barclays, the British universal bank, is expanding its strategic collaboration with Anthropic to integrate secure, enterprise-grade AI systems across its global operations.

[Read more](barclays-scales-claude.md)

### Claude discovers a novel enzyme system with CRISPR-like repeats

We’re announcing a new life sciences research group and laboratory at Anthropic. This post introduces the team behind this work and shares early results in which Claude discovered a novel enzyme system with properties reminiscent of CRISPR.

[Read more](claude-discovers-novel-enzyme-system.md)

[](https://www.anthropic.com/)

### Products

- [Claude](../15-Claude-AI-Features/product-overview.md)
- [Claude Code](../15-Claude-AI-Features/product-claude-code-fad1ab4b.md)
- [Claude Code Enterprise](../15-Claude-AI-Features/product-claude-code-enterprise.md)
- [Claude Cowork](../15-Claude-AI-Features/product-cowork.md)
- [@Claude](../15-Claude-AI-Features/product-tag.md)
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
- [Opus](../15-Claude-AI-Features/claude-opus.md)
- [Sonnet](../15-Claude-AI-Features/claude-sonnet.md)
- [Haiku](../15-Claude-AI-Features/claude-haiku.md)

### Solutions

- [AI agents](../18-Industry-UseCases/agents.md)
- [Code modernization](../18-Industry-UseCases/code-modernization.md)
- [Coding](../18-Industry-UseCases/coding.md)
- [Commerce](../18-Industry-UseCases/commerce.md)
- [Customer support](../18-Industry-UseCases/customer-support.md)
- [Cybersecurity](../18-Industry-UseCases/cybersecurity.md)
- [Enterprise](../17-Billing-Plans/pricing-enterprise.md)
- [Financial services](../18-Industry-UseCases/finance.md)
- [Government](../18-Industry-UseCases/government.md)
- [Healthcare](../18-Industry-UseCases/healthcare.md)
- [Higher education](../18-Industry-UseCases/education.md)
- [K-12 teachers](../18-Industry-UseCases/teachers.md)
- [Legal](../18-Industry-UseCases/legal.md)
- [Life sciences](../18-Industry-UseCases/life-sciences.md)
- [Nonprofits](../18-Industry-UseCases/nonprofits.md)
- [Sales](../18-Industry-UseCases/sales.md)
- [Small business](../18-Industry-UseCases/small-business.md)

### Claude Platform

- [Overview](https://claude.com/platform/api)
- [Developer docs](../04-API-Reference/Other/home.md)
- [Pricing](../17-Billing-Plans/pricing.md#api)
- [Ecosystem](https://claude.com/ecosystem)
- [Marketplace](https://claude.com/platform/marketplace)
- [Regional compliance](https://claude.com/regional-compliance)
- [Claude on AWS](../04-API-Reference/Other/partners-claude-on-aws.md)
- [Google Cloud](../04-API-Reference/Other/partners-google-cloud.md)
- [Microsoft Foundry](../04-API-Reference/Other/partners-microsoft-foundry.md)
- [Console login](../04-API-Reference/Other/usage-limits.md)

### Resources

- [Blog](https://claude.com/blog)
- [Claude partner network](../04-API-Reference/Other/partners.md)
- [Community](https://claude.com/community)
- [Connectors](../04-API-Reference/Other/partners-mcp.md)
- [Courses](https://academy.claude.com)
- [Customer stories](../18-Industry-UseCases/customers.md)
- [Developer blog](https://claude.dev)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Plugins](../08-Plugins-Skills/claude-com-plugins.md)
- [Powered by Claude](../04-API-Reference/Other/partners-powered-by-claude.md)
- [Service partners](../04-API-Reference/Other/partners-services.md)
- [Tutorials](https://claude.com/resources/tutorials)
- [Use cases](https://claude.com/resources/use-cases)

### Programs

- [Campus](../15-Claude-AI-Features/programs-campus.md)
- [Frontier Academy](../15-Claude-AI-Features/programs-frontier-academy.md)
- [Scientists](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)
- [Startups](../15-Claude-AI-Features/programs-startups.md)

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
