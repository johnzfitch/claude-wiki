---
title: "Elections and AI in 2024: Anthropic observations and learnings \\ Anthropic"
source_url: "https://www.anthropic.com/news/elections-ai-2024"
category: "19-Reference"
fetched_at: "2026-08-02T05:43:08Z"
---

# Elections and AI in 2024: observations and learnings

Dec 12, 2024

2024 marked the first major election cycle with widespread access to generative AI and the first major election year that Claude has been available. With concerns about generative AI's impact on election outcomes, we implemented proactive safety measures and drew upon usage analysis from our new [Clio tool](https://anthropic.com/research/clio). Across our products (Claude.ai, first party and third party API), election-related activity constituted less than 0.5% of overall use, ticking up to just over 1% of total usage in the weeks leading up to the US election. Below are insights about our election safety work and lessons learned for future elections.

### Our safety approach

In February 2024 we [outlined](https://www.anthropic.com/news/preparing-for-global-elections-in-2024) three major components of our election work:

- First, we developed and enforced comprehensive policies around election issues. Our Usage Policy prohibits campaigning and election interference, including promoting candidates or parties, soliciting votes or contributions, and generating misinformation. In May 2024, we [expanded](https://www.anthropic.com/news/updating-our-usage-policy) these policies to address influence campaigns, voter targeting, impersonation, and election interference.
- Second, we [rigorously tested](https://www.anthropic.com/news/testing-and-mitigating-elections-related-risks) our models' performance against potential misuse. We conducted over a dozen rounds of policy vulnerability testing, a form of targeted red-teaming with external policy experts, to identify risks and guide Claude's responses. Our testing focused on detecting inaccurate information, evaluating parity across candidates and issues, and understanding refusal rates for harmful queries. We completed regular testing ahead of global elections in India, South Africa, Mexico, the United Kingdom, France, and the European Union Parliamentary elections, with daily testing of Claude's responses to misinformation narratives during the US election period.  
    
  Third, we directed users seeking voting information to authoritative, nonpartisan sources including TurboVote/Democracy Works in the US and relevant election authorities in other geographies, including the EU Parliament elections site, the UK Electoral Commission, and the France administrative elections website.

Over the past year we saw approximately 100 election-related enforcement actions globally, including warnings and in some cases account bans for repeat violators. Unlike social media platforms that elevate or reduce visible content within algorithmically-driven feeds, chatbots like Claude function primarily through one-on-one interactions between users, lowering the risk of amplification. Additionally, Claude currently outputs only text, eliminating the threat of deepfakes. While abuse vectors remain low, we maintain rigorous monitoring and cautious response protocols as these threats continue to evolve.

### Usage patterns and safety with Clio

Clio is an automated tool that enables analysis of real-world language model use and acts as a complement to our existing mitigation and enforcement strategies to provide insight into how people use or misuse our model. Clio takes raw conversations that people have with the language model and distills them into abstracted, understandable topic clusters. You can learn more about the tool in our [blog](https://anthropic.com/research/clio).

The first election-related application of Clio was analyzing usage patterns around the US election. During the week of the election (November 2 - 8) we saw a noticeable uptick in election related usage (Figure 1). Approximately two-thirds of election-related conversations asked Claude to analyze and explain political systems, policies, current events, and political issues, or to analyze political data such as voting patterns and political trends. Other less prevalent but still relevant use cases included asking Claude to translate election information, as well as requests to generate educational content around democracy and government.

Election-related interactions represent a very small percentage of overall Claude.ai usage with less than 1% of conversations touching on election-related topics. Within this, a small proportion violated our Usage Policy (with violations primarily related to political campaigning) and were addressed with the mitigations outlined above. In the leadup to the US election, we witnessed a spike in election-related conversations.

### Case study: incorporating knowledge cutoff dates

Our experience this year highlighted the importance of transparent communication about our systems' limitations. When France called snap elections during the summer, we faced a challenge: our model, trained only through April 2024, couldn't provide accurate information about the new timing of the elections. Understanding that users asking questions about an election the model has no knowledge of could lead to confusing Claude responses, we worked to implement clearer communications about Claude's knowledge cutoff date, both in the [model system prompt](https://docs.anthropic.com/en/release-notes/system-prompts#oct-22nd-2024) and user interface via our elections banner. This has helped users better understand model limitations and encouraged them to seek information from authoritative sources where appropriate.

### Looking forward

Protecting election integrity requires constant vigilance and adaptation as AI technology evolves. We remain committed to developing sophisticated testing systems, strengthening industry collaboration, and maintaining transparent communication about our findings as we work to protect democratic processes.


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
