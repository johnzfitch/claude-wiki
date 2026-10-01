---
title: "Introducing Claude 3.5 Sonnet \\ Anthropic"
source_url: "https://www.anthropic.com/news/claude-3-5-sonnet"
category: "19-Reference"
fetched_at: "2026-08-02T05:41:39Z"
tags: ["news-research"]
---

# Claude 3.5 Sonnet

Jun 21, 2024

[Try on Claude.ai](https://claude.ai/)

- Update
  Consumer Terms and Privacy Policy

  Aug 28, 2025

Today, we’re launching Claude 3.5 Sonnet—our first release in the forthcoming Claude 3.5 model family. Claude 3.5 Sonnet raises the industry bar for intelligence, outperforming competitor models and Claude 3 Opus on a wide range of evaluations, with the speed and cost of our mid-tier model, Claude 3 Sonnet.

Claude 3.5 Sonnet is now available for free on Claude.ai and the Claude iOS app, while Claude Pro and Team plan subscribers can access it with significantly higher rate limits. It is also available via the Anthropic [API](https://docs.anthropic.com/en/home), [Amazon Bedrock](https://aws.amazon.com/blogs/aws/anthropics-claude-3-5-sonnet-model-now-available-in-amazon-bedrock-the-most-intelligent-claude-model-yet/), and [Google Cloud’s Vertex AI](https://cloud.google.com/blog/products/ai-machine-learning/announcing-anthropics-claude-3-5-sonnet-on-vertex-ai-providing-more-choice-for-enterprises). The model costs \$3 per million input tokens and \$15 per million output tokens, with a 200K token context window.

## Frontier intelligence at 2x the speed

Claude 3.5 Sonnet sets new industry benchmarks for graduate-level reasoning (GPQA), undergraduate-level knowledge (MMLU), and coding proficiency (HumanEval). It shows marked improvement in grasping nuance, humor, and complex instructions, and is exceptional at writing high-quality content with a natural, relatable tone.

Claude 3.5 Sonnet operates at twice the speed of Claude 3 Opus. This performance boost, combined with cost-effective pricing, makes Claude 3.5 Sonnet ideal for complex tasks such as context-sensitive customer support and orchestrating multi-step workflows.

In an [internal agentic coding evaluation](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf), Claude 3.5 Sonnet solved 64% of problems, outperforming Claude 3 Opus which solved 38%. Our evaluation tests the model’s ability to fix a bug or add functionality to an open source codebase, given a natural language description of the desired improvement. When instructed and [provided with the relevant tools](tool-use-ga.md), Claude 3.5 Sonnet can independently write, edit, and execute code with sophisticated reasoning and troubleshooting capabilities. It handles code translations with ease, making it particularly effective for updating legacy applications and migrating codebases.

## State-of-the-art vision

Claude 3.5 Sonnet is our strongest vision model yet, surpassing Claude 3 Opus on standard vision benchmarks. These step-change improvements are most noticeable for tasks that require visual reasoning, like interpreting charts and graphs. Claude 3.5 Sonnet can also accurately transcribe text from imperfect images—a core capability for retail, logistics, and financial services, where AI may glean more insights from an image, graphic or illustration than from text alone.

## Artifacts—a new way to use Claude

Today, we’re also introducing Artifacts on Claude.ai, a new feature that expands how users can interact with Claude. When a user asks Claude to generate content like code snippets, text documents, or website designs, these Artifacts appear in a dedicated window alongside their conversation. This creates a dynamic workspace where they can see, edit, and build upon Claude’s creations in real-time, seamlessly integrating AI-generated content into their projects and workflows.

This preview feature marks Claude’s evolution from a conversational AI to a collaborative work environment. It’s just the beginning of a broader vision for Claude.ai, which will soon expand to support team collaboration. In the near future, teams—and eventually entire organizations—will be able to securely centralize their knowledge, documents, and ongoing work in one shared space, with Claude serving as an on-demand teammate.

## Commitment to safety and privacy

Our models are subjected to rigorous testing and have been trained to reduce misuse. Despite Claude 3.5 Sonnet’s leap in intelligence, our red teaming assessments have concluded that Claude 3.5 Sonnet remains at [ASL-2](anthropics-responsible-scaling-policy.md). More details can be found in the [model card addendum](https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/Model_Card_Claude_3_Addendum.pdf).

As part of our commitment to safety and transparency, we’ve engaged with external experts to test and refine the safety mechanisms within this latest model. We recently provided Claude 3.5 Sonnet to the UK’s Artificial Intelligence Safety Institute (UK AISI) for pre-deployment safety evaluation. The UK AISI completed tests of 3.5 Sonnet and shared their results with the US AI Safety Institute (US AISI) as part of a Memorandum of Understanding, made possible by the partnership between the US and UK AISIs [announced earlier this year](https://www.commerce.gov/news/press-releases/2024/04/us-and-uk-announce-partnership-science-ai-safety).

We have integrated policy feedback from outside subject matter experts to ensure that our evaluations are robust and take into account new trends in abuse. This engagement has helped our teams scale up our ability to evaluate 3.5 Sonnet against various types of misuse. For example, we used feedback from child safety experts at [Thorn](https://www.thorn.org/) to update our classifiers and fine-tune our models.

One of the core constitutional principles that guides our AI model development is privacy. We do not train our generative models on user-submitted data unless a user gives us explicit permission to do so.

## Coming soon

Our aim is to substantially improve the tradeoff curve between intelligence, speed, and cost every few months. To complete the Claude 3.5 model family, we’ll be releasing Claude 3.5 Haiku and Claude 3.5 Opus later this year.

In addition to working on our next-generation model family, we are developing new modalities and features to support more use cases for businesses, including integrations with enterprise applications. Our team is also exploring features like Memory, which will enable Claude to remember a user’s preferences and interaction history as specified, making their experience even more personalized and efficient.

We’re constantly working to improve Claude and love hearing from our users. You can submit feedback on Claude 3.5 Sonnet directly in-product to inform our development roadmap and help our teams to improve your experience. As always, we look forward to seeing what you build, create, and discover with Claude.


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
