---
title: "Developing nuclear safeguards for AI \\ Anthropic"
source_url: "https://www.anthropic.com/research/nuclear-safeguards-for-ai"
category: "19-Reference"
fetched_at: "2026-09-11T06:29:21Z"
tags: ["news-research"]
---

# Developing nuclear safeguards for AI

Aug 21, 2025

Nuclear technology is inherently dual-use: the same physics principles that power nuclear reactors can be misused for weapons development. As AI models become more capable, we need to keep a close eye on whether they can provide users with dangerous technical knowledge in ways that could threaten national security.

Information relating to nuclear weapons is particularly sensitive, which makes evaluating these risks challenging for a private company acting alone. That’s why last April we [partnered](https://www.axios.com/2024/11/14/anthropic-claude-nuclear-information-safety) with the U.S. Department of Energy (DOE)’s National Nuclear Security Administration (NNSA) to assess our models for nuclear proliferation risks and continue to work with them on these evaluations.

Now, we’re going beyond assessing risk to build the tools needed to monitor for it. **Together with the NNSA and DOE national laboratories, we have co-developed a classifier**—an AI system that automatically categorizes content—**that distinguishes between concerning and benign nuclear-related conversations with 96% accuracy in preliminary testing** (see below for details).

We have already deployed this classifier on Claude traffic as part of our broader system for identifying misuse of our models. Early deployment data suggests the classifier works well with real Claude conversations.

**We will share our approach with the** **[Frontier Model Forum](https://www.frontiermodelforum.org/),** the industry body for frontier AI companies, **in hopes that this partnership can serve as a blueprint that any AI developer can use to implement similar safeguards in partnership with NNSA.**^([1](#footnote-1))

Along with the concrete importance of securing frontier AI models against nuclear misuse, this first-of-its-kind effort shows the power of public-private partnerships. These partnerships combine the complementary strengths of industry and government to address risks head-on, making AI models more reliable and trustworthy for all their users.

## What we built

In this partnership, we did not stop with identifying risks—we developed an approach for addressing them. After a year of NNSA staff red teaming Claude models in a secure environment, we began to co-develop risk mitigations.

Informed by their red teaming, NNSA shared with us a carefully curated set of nuclear risk indicators designed to distinguish potentially concerning conversations about nuclear weapons development from benign discussions about nuclear energy, medicine, or policy. Crucially, this list was developed at a classification level such that it could be shared with our team, allowing us to use it to build defenses.

Our Policy and [Safeguards](building-safeguards-for-claude.md) teams turned that list into a classifier that could identify concerning nuclear queries in real-time. Think of a classifier as a specialized labeller, like the one that underpins the spam filter in your email inbox. Instead of identifying junk mail, this classifier identifies conversations that are potentially harmful while allowing legitimate discussions.

To validate the system, we generated hundreds of synthetic test prompts—some concerning, some benign—ran them through the classifier, and shared the results with the NNSA. NNSA validated that the classifier scores aligned with the expected labels (i.e., harmful or benign). We then refined the approach based on their feedback, and repeated the cycle to improve precision. Figure 1 summarizes this process.

The most challenging aspect of this endeavor wasn’t technical—it was bridging the gap between a national security agency and a private AI company. Both sides had to operate under information sharing constraints: the NNSA needed to keep certain information classified, and Anthropic needed to protect user data. How, then, could we validate that our classifier actually worked? Synthetic data generation was our solution: we used example prompts from NNSA to generate hundreds of test cases, creating a robust evaluation set without compromising either party’s equities.

## Why does this matter?

If an AI system is too cautious, it might refuse legitimate nuclear engineering coursework. Too permissive, and it could inadvertently assist bad actors.

Our classifier appears to strike the right balance. In preliminary testing with synthetic data, we achieved a 94.8% detection rate for nuclear weapons queries and zero false positives (overall, 96.2% of the classifier’s labels in this test were accurate as shown in Figure 2), suggesting this system would not flag legitimate educational, medical, or research discussions as concerning. This precision matters because nuclear conversations in AI systems are rare but high-stakes—they bear directly on national security.

## Sharing with industry

We’re making these resources available so that other leading AI companies can implement similar safeguards if they choose. Beyond demonstrating how government expertise can enhance AI safety through voluntary public-private cooperation, we hope this sparks an exchange where we can learn from each other’s approaches to risk mitigation.

## What’s next?

As noted above, we have deployed the classifier as an experimental addition to our Safeguards framework, monitoring a percentage of Claude traffic. Its real-world performance has confirmed that the classifier works effectively beyond our testing environment. Whereas our synthetic test data provided clear examples of harmful and benign exchanges, the distribution of actual user traffic proved more complex and surprising, yet the classifier still performed well.

One example of how real-world deployment differs from testing is that the classifier flagged certain conversations about nuclear weapons that we ultimately determined to be benign. For example, recent events in the Middle East brought renewed attention to the issue of nuclear weapons. During this time, the nuclear classifier incorrectly flagged some conversations that were only related to these events, not actual misuse attempts. We found that when these exchanges went through [hierarchical summarization](https://alignment.anthropic.com/2025/summarization-for-monitoring/)—which reviews multiple flagged conversations together—they were correctly identified as harmless current events discussions because of the additional context provided by the summarization step.

This reveals two dynamics: first, that real-world conversations often fall into gray areas that are difficult to capture in synthetic data, and second, that combining multiple safety tools creates a more nuanced and precise system.

Ultimately, the classifier proved its value by successfully catching concerning content (i.e. true positives) when deployed. For example, Anthropic red teamers who were not aware the classifier had been deployed were conducting routine adversarial testing of our systems using deliberately concerning prompts. The classifier correctly identified these test queries as potentially harmful, demonstrating its effectiveness.

This work leveraged each party’s strengths (i.e., government domain expertise and industry technical capabilities) and early results show it is working in practice. This demonstrates a model of public-private partnerships that can be replicated in other national security domains. It also illustrates that there are steps that industry can take now to implement meaningful safety measures.

We are grateful to the team at NNSA and DOE national laboratories for their commitment to this collaboration, which demonstrates how industry and government can work together to enhance national security.

*For more on our safety initiatives, see our* *[Responsible Scaling Policy](https://www.anthropic.com/rsp-updates),* *[Frontier Red Team](strategic-warning-for-ai-risk-progress-and-insights-from-our-frontier-red-team.md), and* *[Safeguards](building-safeguards-for-claude.md) work.*

#### Footnotes

1.  We are able to share this kind of information because FMF member firms (i.e., Amazon, Anthropic, Google, Meta, Microsoft, and OpenAI) have signed a unique [agreement](https://www.frontiermodelforum.org/updates/fmf-announces-first-of-its-kind-information-sharing-agreement/) designed to facilitate information-sharing about threats, vulnerabilities, and capability advances unique to frontier AI.[](#footnote-ref-1)


## Related content

### Measuring tactical intelligence targeting and conventional weapons capabilities of AI models

Anthropic’s Frontier Red Team developed new evaluations to measure AI capabilities in tactical intelligence targeting and conventional weapons development.

[Read more](intelligence-targeting-conventional-weapons-capabilities.md)

### An alignment assessment of recent cybersecurity incidents

We present an alignment assessment of four incidents in which Claude models gained unauthorized access to real third-party systems.

[Read more](alignment-assessment-cybersecurity-incidents.md)

### Formalizing Fermat's Last Theorem

We are sharing the first complete computer-checked proof of Fermat’s Last Theorem. Claude worked largely autonomously over 11 days to write the proof in the Lean programming language.

[Read more](formalizing-fermats-last-theorem.md)

## Subscribe to the Frontier Red Team newsletter

Get updates on our latest red-teaming research and findings.

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
