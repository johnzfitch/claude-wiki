---
title: "Testing our safety defenses with a new bug bounty program \\ Anthropic"
source_url: "https://www.anthropic.com/news/testing-our-safety-defenses-with-a-new-bug-bounty-program"
category: "19-Reference"
fetched_at: "2026-08-02T07:10:50Z"
tags: ["news-research", "testing"]
---

# Testing our safety defenses with a new bug bounty program

May 14, 2025

Today, we're launching a new bug bounty program to stress-test our latest safety measures. Similar to the program we announced last [summer](model-safety-bug-bounty.md), we're challenging researchers to find universal jailbreaks in safety classifiers that we haven't yet deployed publicly. These safeguards are part of the advanced protections we’ve developed to help us meet the AI Safety Level-3 (ASL-3) Deployment Standard as part of our [Responsible Scaling Policy](announcing-our-updated-responsible-scaling-policy.md), the framework that governs how we develop and deploy increasingly capable AI models safely.

The bug bounty program, which is in partnership with [HackerOne](https://www.hackerone.com/), will test an updated version of our [Constitutional Classifiers](constitutional-classifiers.md) system. Constitutional Classifiers are a technique we built to guard against jailbreaks that could elicit information related to CBRN (chemical, biological, radiological, and nuclear) weapons. This system follows a list of principles that define what type of content should and shouldn’t be allowed when interacting with Claude, and focus narrowly on specific harms.

Participants will receive early access to test our classifiers on Claude 3.7 Sonnet. We’re offering bounty rewards up to \$25,000 for verified universal jailbreaks found on the unreleased system. A universal jailbreak is a vulnerability that consistently bypasses Claude’s safety measures across many topics. For this initiative, we're interested in universal jailbreaks that could be exploited to enable misuse on CBRN-related topics.

Our models are becoming increasingly capable, and as we’ve [shared before](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf), we believe some future models may require the advanced ASL-3 security and safety protections outlined in our Responsible Scaling Policy. This bug bounty initiative will help contribute to the work we’ve done over the last several months to iterate and stress-test our ASL-3 safeguards.

We’ve kicked off this new bug bounty initiative with participation from the researchers who joined our earlier program last year and are offering the opportunity for new researchers to participate. If you're an experienced red teamer or have demonstrated expertise in identifying jailbreaks in language models, we encourage you to apply for an invitation through our [application form](https://forms.gle/3ocTorSkkuvcGePn9). Detailed instructions and feedback will be shared with selected participants. Applications open today, and the program will run through Sunday, May 18. This initiative is invite-only so we can respond to submissions with timely feedback.

We're grateful to the security community for its partnership in helping us make AI systems safer.

## Update on May 22, 2025

The bug bounty program in this post has concluded. Participants will transition to a new bug bounty initiative we’re rolling out today that’s focused on stress-testing our [Constitutional Classifiers system](constitutional-classifiers.md) on the new Claude Opus 4 model and testing other safety systems we may develop. We’re still accepting applications to participate in this new invite-only program. You can apply for an invite through our [application form](https://forms.gle/3ocTorSkkuvcGePn9).

To further advance AI safety, we are also accepting reports of universal jailbreaks for ASL-3 uses of concern (meaning those which elicit information related to biological threats) found on public platforms or forums, such as social media. For more information, see [here](https://docs.google.com/forms/d/e/1FAIpQLSfJAE2lJC0uKkkrKemR2ef_Q0yFFqiwjzcSE4lzMTdDQDuPcQ/viewform).  


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
