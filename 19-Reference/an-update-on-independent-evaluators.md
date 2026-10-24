---
title: "Anthropic update on independent evaluators \\ Anthropic"
source_url: "https://www.anthropic.com/news/an-update-on-independent-evaluators"
category: "19-Reference"
fetched_at: "2026-10-20T06:41:18Z"
tags: ["news-research"]
---

# An update on independent evaluators

Oct 15, 2026

Last month, we committed to [stronger independent, third-party assessment](https://darioamodei.com/post/we-must-pace-the-frontier) of our models and safety practices. We also signed the White House Accord on Super Intelligence, in which companies pledged to partner with independent external auditors or evaluators. Today, we’re announcing that we’ve started to give employee-like access to a team from [METR](https://metr.org/), a nonprofit that evaluates frontier AI models.

METR will publish the results of its risk assessments. Over the past year, we’ve worked with METR on [several reviews of our Risk Reports](https://metr.org/risk-assessment/). We’re also working with [SecureBio](https://securebio.org/) and [Accenture](accenture-embedded-evaluation.md) as evaluators, and are in early discussions with several other organizations, including [Hugging Face](https://huggingface.co/).

Here, we explain our approach to working with evaluators.

## Why we work with independent evaluators

As models have become more powerful, they’ve required stronger safeguards and more challenging risk assessments. We want to be publicly accountable for the decisions we’re making. But we can’t publicly share all the information relevant to our safety work. Some of it could be useful to malicious actors, or is commercially sensitive, like compute or training information. Instead, we’re giving third-party evaluators deep access to our information, and are having them share evidence and reasoned conclusions about the risks involved in building our models. We aim to close the gap between what evaluators understand about a frontier AI company’s systems and what the company itself understands.

To evaluate frontier models, evaluators need the following:

- *Expertise* in assessing the capabilities of frontier models, including understanding the way evaluations can go wrong, such as [alignment faking](alignment-faking.md).
- *Independence*: they shouldn’t hold equity in the company they’re evaluating, or be financially or operationally dependent on it.
- Enough *access* to meaningfully evaluate risks. Beyond access to the latest models, evaluators also need visibility into how those models were trained, into how our safeguards function, and more.
- *Freedom to publish* observations and assessments of a model or a process.

Although the analogy isn’t exact, bank supervision operates on similar logic. Banks know more about their own risk positions than outsiders do, so regulators assign resident examiners to work inside the largest banks. If a bank’s risk-taking could threaten the public, third parties try to see that in advance.

For the AI industry, this is a step toward [robust safety oversight](https://www-cdn.anthropic.com/files/4zrzovbb/website/0a58d567024a8b448ff15158ebc3625328dfcc1f.pdf). We’re moving quickly with multiple evaluators and learning actively about what kinds of partnership work. We’re committed to sharing updates as we go.

## What we mean by “employee-like access”

We’ve onboarded six METR employees with company hardware, office space, and access to internal tools and systems that are roughly on par with what our own risk assessment teams have access to. Outside a small number of clearly defined categories (e.g., data about customers, attorney-client privileged information, or information about our model architectures), Anthropic employees are encouraged to share information with them just as they would with a fellow employee working on alignment risk.^([1](#footnote-1))

METR will publish its analysis of our risk levels, incidents, or practices. Anthropic can’t veto publication, but we can require them to redact information if it falls into predefined categories such as reproducing confidential IP. (Anthropic ultimately decides what information does and does not fall into these categories, although METR reserves the right to make certain statements about the level of access and information it received.)^([2](#footnote-2))

Our engagement with METR is limited to a small team operating under enforceable agreements. Other METR employees are siloed from that team’s work, including researchers who work with us on other projects. Embedded evaluation gives a few qualified people working under Anthropic’s security standards a close view of how we operate. It’s not a way for other organizations to obtain our information, or that of our customers and partners.

## Our other evaluator partnerships

We’re working on several other partnerships. Because these other partnerships are still in early stages, we’re providing these evaluators with more limited information, and they have more limited publication rights. Our goal with these early engagements is to make sure that our partners protect confidential information and have the requisite resources and expertise to evaluate our models. As partnerships progress and we build trust, we hope to fully embed more independent evaluators.

We’re developing three tiers of access for evaluators. Over time, we hope to have several evaluators at the third tier, with each team publishing their own analysis of our risk posture and key decisions.

**In the first tier,** evaluators conduct narrowly scoped risk investigations. We decide what access to provide a first-tier evaluator, and evaluators can publish their findings with our approval.

**In the second tier,** evaluators can publish without our approval, and they have access to more information. We can still require removal of specific categories of information, though evaluators can publish their views on whether our redactions were justified.

**The third tier** is the arrangement we’ve described with METR, with employee-like access and publication rights similar to those of the second tier.

**SecureBio** is in the process of reviewing the chemical and biological weapons chapter of our [August Risk Report](https://www-cdn.anthropic.com/f61d49fa5596956a5dec75fea0e973bf6a6a8378/Redacted%20Risk%20Report%20August%202026%20.pdf), after completing and [publishing a pilot review](https://securebio.org/resources/anthropic_feb_2026_risk_review.pdf) of our previous risk report. After this review is complete, we will consider moving to projects with increased access.^([3](#footnote-3))

**With Accenture** and Faculty, we're working [toward an ambitious partnership](accenture-embedded-evaluation.md) that includes evaluating and red-teaming models, conducting alignment assessments, testing model safeguards, and building capabilities across our organizations.

We’re embedding evaluators voluntarily, and we believe every frontier AI company should do the same.

#### Footnotes

1.  Because these evaluators (like bank examiners) may also work with other companies, we exercise caution around the possibility of inadvertent leaks. Information about architectures presents a high risk of inadvertent leaks, and its relevance to risk assessment is typically low. When it is highly relevant, we will generally seek to share it, though this will require explicit internal approvals.[](#footnote-ref-1)
2.  Updated on October 16 to clarify METR's current project terms with Anthropic.[](#footnote-ref-2)
3.  Updated on October 15 to clarify SecureBio's current project terms with Anthropic.[](#footnote-ref-3)


## Related content

### Investing in the public benefit

We’re committing a portion of Anthropic’s shares to the Anthropic Public Benefit Fund, a new entity with a structure that increases the stake as the company grows.

[Read more](public-benefit-fund.md)

### Preparing for the 2026 US midterms

Earlier this year, we shared an update on our election safeguards. Here, we outline how we’ve continued to strengthen these safeguards ahead of this year’s US midterms.

[Read more](2026-us-midterms.md)

### Anthropic opens Singapore office and signs MOU with the Government of Singapore

Anthropic has opened an office in Singapore and signed an MOU with the country’s government to advance safe, responsible AI adoption.

[Read more](singapore-office-opening.md)

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
- [Claude for Google Workspace](https://claude.com/claude-for-google-workspace)
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
- [Financial advisors](../18-Industry-UseCases/financial-advisors.md)
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
- [Console login](../04-API-Reference/Other/playground.md)

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
- [Scientists](../15-Claude-AI-Features/programs-team-plan-for-scientists.md)
- [Startups](../15-Claude-AI-Features/programs-startups.md)

### Help and security

- [Availability](https://www.anthropic.com/legal/supported-regions)
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
