---
title: "Understanding and addressing AI harms \\ Anthropic"
source_url: "https://www.anthropic.com/news/our-approach-to-understanding-and-addressing-ai-harms"
category: "19-Reference"
fetched_at: "2026-08-27T09:26:18Z"
tags: ["news-research"]
---

# Our approach to understanding and addressing AI harms

Apr 21, 2025

As AI capabilities rapidly advance, understanding and addressing the full spectrum of potential impacts becomes increasingly important. Today, we're sharing insights into our evolving approach to assessing and mitigating various harms that could result from our systems, ranging from catastrophic scenarios like biological threats to critical concerns like child safety, disinformation and fraud.

Why is this approach important? As models continue to evolve, we need more comprehensive ways to think about and manage their potential impacts. We believe that considering different types of harms in a structured way helps us better understand the challenges ahead and informs our thinking about responsible AI development.

Our approach complements our [Responsible Scaling Policy (RSP)](https://www-cdn.anthropic.com/17310f6d70ae5627f55313ed067afc1a762a4068.pdf), which focuses specifically on catastrophic risks. Identifying and addressing the full range of potential impacts requires a broader perspective. That's why we've built out a more comprehensive framework to assess harm that we can then proportionately manage and mitigate.

*  
**\*Important note**: This approach is still evolving. We're sharing our current thinking while acknowledging it will continue to develop as we learn more. We welcome collaboration from across the AI ecosystem as we work to make these systems benefit humanity.*

### **Breaking down our approach:**

We've developed an approach that helps our teams communicate clearly, make well-reasoned decisions, and develop targeted solutions for both known and emergent harms. This approach is designed to be both principled and adaptable to keep up with the evolving AI landscape. We examine potential AI impacts across multiple baseline dimensions, with room to grow and expand over time:

- **Physical impacts:** Effects on bodily health and well-being
- **Psychological impacts:** Effects on mental health and cognitive functioning
- **Economic impacts:** Financial consequences and property considerations
- **Societal impacts:** Effects on communities, institutions, and shared systems
- **Individual autonomy impacts:** Effects on personal decision-making and freedoms

For each dimension, we consider factors like likelihood, scale, affected populations, duration, causality, technology contribution, and mitigation feasibility. This helps us understand the real-world significance of different potential impacts.

Depending on harm type and severity, we address and manage risks through a variety of policies and practices including developing and maintaining a comprehensive [Usage Policy](https://www.anthropic.com/legal/aup), conducting [evaluations](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf) (including red teaming and adversarial testing) before and after launch, sophisticated [detection](clio.md) [techniques](https://alignment.anthropic.com/2025/summarization-for-monitoring/) to spot misuse and abuse, and [robust enforcement](https://www.anthropic.com/transparency/voluntary-commitments) ranging from prompt modifications to account blocking. This perspective helps us balance multiple considerations: addressing harms with proportionate safeguards while maintaining the helpfulness and functionality of our systems in everyday use cases. We’re excited to share more about this work in the near future.

### **Some examples of how we’ve used our framework to inform our understanding of harm **

When exploring new capabilities or features, we examine how they might introduce additional considerations across different harm dimensions. For example:  
  
**Computer Use:** As our models develop the ability to interact with computer interfaces, we consider factors like the types of software AI systems might interact with and the contexts in which these interactions occur, which helps us identify where additional safeguards might be beneficial. For computer use, we specifically examine a multitude of risks including those related to financial software and banking platforms where unauthorized automation could potentially facilitate fraud or manipulation, and communication tools where AI systems could be used for targeted influence operations or phishing campaigns. This analysis helps us develop approaches that maintain the utility of these capabilities while incorporating appropriate monitoring and enforcement to prevent misuse. For example, our initial work on computer use functionality led us to design more stringent enforcement thresholds and employ novel approaches to enforcement such as [hierarchical summarization](https://alignment.anthropic.com/2025/summarization-for-monitoring/) that allows us to detect harms while maintaining our privacy standards.

**Model Response Boundaries:** When considering how models should respond to different types of user requests, we've found value in examining tradeoffs between helpfulness and appropriate limitations. Models that are trained to be more helpful and responsive to user requests may also lean towards harmful behaviors (e.g., sharing information that violates our AUP or could be used in dangerous ways). Conversely, models that over-index on harmlessness can tend towards not sharing any information with users, even when requests are harmless. By thinking about both individual and societal impacts, we can better understand where to focus our safety evaluations and training. For example, with Claude 3.7 Sonnet, we evaluated different types of requests along this spectrum and improved how our model handles ambiguous prompts by encouraging safe, helpful responses rather than simply refusing to engage. This resulted in a 45% reduction in unnecessary refusals while maintaining strong safeguards against truly harmful content. This approach helps us make more nuanced decisions about model behavior, particularly in scenarios where certain vulnerable populations—such as children, marginalized communities, or individuals in crisis—might be at heightened risk.

### **Looking ahead**

There's still a lot to do. Our approach to understanding and addressing harms is just one input into our overall safety strategy, but we think it represents a useful step toward more systematic thinking about AI impacts.

As AI systems become more capable, we expect new challenges will emerge that we haven't yet anticipated. We're committed to evolving our approach alongside these developments, including adapting our frameworks, refining our assessment methods, and learning from both successes and failures along the way.

We know we can't do this work alone. We invite researchers, policy experts, and industry partners to collaborate with us as we continue exploring these important questions. You can connect with us on these issues via <usersafety@anthropic.com>.

  
## Related content

### Funding better evaluations of AI’s impact on wellbeing

We’re launching a \$5 million grant program to fund independent research into how AI impacts users’ wellbeing.

[Read more](wellbeing-research-grants.md)

### How Claude’s text watermark works

In this article, we share answers to some of the questions we’ve received about how our chosen watermarking method works, whether it affects Claude’s outputs, and why we’re making this change.

[Read more](claude-text-watermark.md)

### Improving Fable 5's biology safeguards

We’re making updates to Claude Fable 5’s biology safeguards in a way that substantially reduces false positives. Fable 5 users will now experience many fewer “fallbacks”—where the system switches to a less capable model after they make a biology-related query.

[Read more](improving-fable-5-s-biology-safeguards.md)

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
- [Research Labs](../15-Claude-AI-Features/programs-claude-team-plan-for-research-labs.md)

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
