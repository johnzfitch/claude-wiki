---
title: "Expanding our model safety bug bounty program \\ Anthropic"
source_url: "https://www.anthropic.com/news/model-safety-bug-bounty"
category: "19-Reference"
fetched_at: "2026-08-02T07:11:57Z"
tags: ["news-research"]
---

# Expanding our model safety bug bounty program

Aug 8, 2024

The rapid progression of AI model capabilities demands an equally swift advancement in safety protocols. As we work on developing the next generation of our AI safeguarding systems, we’re expanding our bug bounty program to introduce a new initiative focused on finding flaws in the mitigations we use to prevent misuse of our models.

Bug bounty programs play a crucial role in strengthening the security and safety of technology systems. Our new initiative is focused on identifying and mitigating universal jailbreak attacks. These are exploits that could allow consistent bypassing of AI safety guardrails across a wide range of areas. By targeting universal jailbreaks, we aim to address some of the most significant vulnerabilities in critical, high-risk domains such as [CBRN](frontier-threats-red-teaming-for-ai-safety.md) (chemical, biological, radiological, and nuclear) and cybersecurity.

We’re eager to work with the global community of security and safety researchers on this effort and invite interested applicants to apply to our program and assess our new safeguards.

## Our approach

To date, we’ve operated an invite-only bug bounty program in partnership with [HackerOne](https://www.hackerone.com/) that rewards researchers for identifying model safety issues in our publicly released AI models. The bug bounty initiative we’re announcing today will test our next-generation system we've developed for AI safety mitigations, which we haven’t deployed publicly yet. Here’s how it will work:

- **Early Access:** Participants will be given early access to test our latest safety mitigation system before its public deployment. As part of this, participants will be challenged to identify potential vulnerabilities or ways to circumvent our safety measures in a controlled environment.
- **Program Scope:** We're offering bounty rewards up to \$15,000 for novel, universal jailbreak attacks that could expose vulnerabilities in critical, high risk domains such as CBRN (chemical, biological, radiological, and nuclear) and cybersecurity. As we’ve [written](many-shot-jailbreaking.md) about previously, a jailbreak attack in AI refers to a method used to circumvent an AI system's built-in safety measures and ethical guidelines, allowing a user to elicit responses or behaviors from the AI that would typically be restricted or prohibited. A universal jailbreak is a type of vulnerability in AI systems that allows a user to consistently bypass the safety measures across a wide range of topics. Identifying and mitigating universal jailbreaks is the key focus of this bug bounty initiative. If exploited, these vulnerabilities could have far-reaching consequences across a variety of harmful, unethical or dangerous areas. The jailbreak will be defined as universal if it can get the model to answer a defined number of specific harmful questions. Detailed instructions and feedback will be shared with the participants of the program.

## Get involved

This model safety bug bounty initiative will begin as invite-only in partnership with HackerOne. While it will be invite-only to start, we plan to expand this initiative more broadly in the future. This initial phase will allow us to refine our processes and respond to submissions with timely and constructive feedback. If you're an experienced AI security researcher or have demonstrated expertise in identifying jailbreaks in language models, we encourage you to apply for an invitation through our **[application form](https://forms.gle/rSKrtJkXMcMCtWYcA) by Friday, August 16.** We will follow up with selected applicants in the fall.

In the meantime, we actively seek any reports on model safety concerns to continually improve our current systems. If you've identified a potential safety issue in our current systems, please report it to usersafety@anthropic.com with sufficient details for us to replicate the issue. For more information, please refer to our [Responsible Disclosure Policy.](https://www.anthropic.com/responsible-disclosure-policy)

This initiative aligns with commitments we’ve signed onto with other AI companies for developing responsible AI such as the [Voluntary AI Commitments](https://www.whitehouse.gov/wp-content/uploads/2023/09/Voluntary-AI-Commitments-September-2023.pdf) announced by the White House and the [Code of Conduct for Organizations Developing Advanced AI Systems](https://www.mofa.go.jp/files/100573473.pdf) developed through the G7 Hiroshima Process. Our goal is to help accelerate progress in mitigating universal jailbreaks and strengthen AI safety in high-risk areas. If you have expertise in this area, please join us in this crucial work. Your contributions could play a key role in ensuring that as AI capabilities advance, our safety measures keep pace.


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
