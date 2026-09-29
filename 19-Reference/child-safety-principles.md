---
title: "Aligning on child safety principles \\ Anthropic"
source_url: "https://www.anthropic.com/news/child-safety-principles"
category: "19-Reference"
fetched_at: "2026-08-02T05:43:03Z"
tags: ["news-research"]
---

# Aligning on child safety principles

Apr 23, 2024

Alongside other leading AI companies, we are committed to implementing robust child safety measures in the development, deployment, and maintenance of generative AI technologies. This new initiative, led by [Thorn](https://thorn.org), a nonprofit dedicated to defending children from sexual abuse, and [All Tech Is Human](https://alltechishuman.org/), an organization dedicated to collectively tackling tech and society's complex problems, aims to mitigate the risks generative AI poses to children.

The commitment marks a significant step forward in preventing the misuse of AI technologies to create or spread child sexual abuse material (AIG-CSAM) and other forms of sexual harm against children.

As a safety-focused organization, we have made it a priority to implement rigorous policies, conduct extensive red teaming, and collaborate with external experts to make sure our models are safe. Anthropic’s [policies strictly prohibit content](https://www.anthropic.com/legal/aup) that describes, encourages, supports or distributes any form of child sexual exploitation or abuse. If we detect this material, we will report it to the National Center for Missing & Exploited Children (NCMEC). It’s important to note that at this time, our models do not have multimodal outputs, even though they are able to ingest images.

As part of this Safety by Design effort, Anthropic is [committed to the Safety by Design principles](https://www.thorn.org/blog/generative-ai-principles/). To ensure tangible action, Anthropic is also committing to the following mitigations, stemming from the principles. We are working towards the following:

## Develop

- Responsibly source our training data: avoid ingesting data into training that has a known risk - as identified by relevant experts in the space - of containing CSAM and CSEM.
- Detect, remove, and report CSAM and CSEM from our training data at ingestion.
- Conduct red teaming, incorporating structured, scalable, and consistent stress testing of our models for AIG-CSAM and CSEM.
- Define specific training data and model development policies.
- Prohibit customer use of our models to further sexual harms against children.

## Deploy

- Detect abusive content (CSAM, AIG-CSAM, and CSEM) in inputs and outputs.
- Include user reporting, feedback, or flagging options.
- Include an enforcement mechanism.
- Include prevention messaging for CSAM solicitation using available tools.
- Incorporate phased deployment, monitoring for abuse in early stages before launching broadly.
- Incorporate a child safety section into our model cards.

## Maintain

- When reporting to NCMEC, use the Generative AI File Annotation.
- Detect, report, remove, and prevent CSAM, AIG-CSAM and CSEM.
- Invest in tools to protect content from AI-generated manipulation.
- Maintain the quality of our mitigations.
- Disallow the use of generative AI to deceive others for the purpose of sexually harming children.
- Leverage Open Source Intelligence (OSINT) capabilities to understand how our platforms, products and models are potentially being abused by bad actors.

More detailed information about the principles which we and other organizations have signed up to can be found in the white paper: [Safety by Design for Generative AI: Preventing Child Sexual Abuse](https://info.thorn.org/hubfs/thorn-safety-by-design-for-generative-AI.pdf).


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
