---
category: "20-Models"
fetched_at: "2026-02-07T10:04:03Z"
source_url: "https://platform.claude.com/docs/en/about-claude/models/choosing-a-model"
title: "Choosing the right model - Claude API Docs"
---

Models & pricing

# Choosing the right model

Copy page

Selecting the optimal Claude model for your application involves balancing three key considerations: capabilities, speed, and cost. This guide helps you make an informed decision based on your specific requirements.

Copy page

## 

Establish key criteria

When choosing a Claude model, we recommend first evaluating these factors:

- **Capabilities:** What specific features or capabilities will you need the model to have in order to meet your needs?
- **Speed:** How quickly does the model need to respond in your application?
- **Cost:** What's your budget for both development and production usage?

Knowing these answers in advance will make narrowing down and deciding which model to use much easier.

------------------------------------------------------------------------

## 

Choose the best model to start with

There are two general approaches you can use to start testing which Claude model best works for your needs.

### 

Option 1: Start with a fast, cost-effective model

For many applications, starting with a faster, more cost-effective model like Claude Haiku 4.5 can be the optimal approach:

1.  Begin implementation with Claude Haiku 4.5
2.  Test your use case thoroughly
3.  Evaluate if performance meets your requirements
4.  Upgrade only if necessary for specific capability gaps

This approach allows for quick iteration, lower development costs, and is often sufficient for many common applications. This approach is best for:

- Initial prototyping and development
- Applications with tight latency requirements
- Cost-sensitive implementations
- High-volume, straightforward tasks

### 

Option 2: Start with the most capable model

For complex tasks where intelligence and advanced capabilities are paramount, you may want to start with the most capable model and then consider optimizing to more efficient models down the line:

1.  Implement with Claude Opus 4.6
2.  Optimize your prompts for these models
3.  Evaluate if performance meets your requirements
4.  Consider increasing efficiency by downgrading intelligence over time with greater workflow optimization

This approach is best for:

- Complex reasoning tasks
- Scientific or mathematical applications
- Tasks requiring nuanced understanding
- Applications where accuracy outweighs cost considerations
- Advanced coding

## 

Model selection matrix

| When you need... | We recommend starting with... | Example use cases |
|----|----|----|
| Claude Opus 4.6 is the latest version of our most intelligent model, and the world’s best model for coding, enterprise agents, and professional work. | Claude Opus 4.6 | Professional software engineering, advanced agents for office tasks, computer and browser use at scale, multi-hour research tasks, step-change vision applications |
| The best combination of speed and intelligence for everyday tasks | Claude Sonnet 4.5 | Code generation, data analysis, content creation, visual understanding, agentic tool use |
| Near-frontier performance with lightning-fast speed and extended thinking at the most economical price point | Claude Haiku 4.5 | Real-time applications, high-volume intelligent processing, cost-sensitive deployments needing strong reasoning, sub-agent tasks |

------------------------------------------------------------------------

## 

Decide whether to upgrade or change models

To determine if you need to upgrade or change models, you should:

1.  [Create benchmark tests](/docs/en/test-and-evaluate/develop-tests) specific to your use case - having a good evaluation set is the most important step in the process
2.  Test with your actual prompts and data
3.  Compare performance across models for:
    - Accuracy of responses
    - Response quality
    - Handling of edge cases
4.  Weigh performance and cost tradeoffs

## 

Next steps

[](/docs/en/about-claude/models/overview)

Model comparison chart

See detailed specifications and pricing for the latest Claude models

[](/docs/en/about-claude/models/whats-new-claude-4-6)

What's new in Claude 4.6

Explore the latest improvements in Claude 4.6 models

[](/docs/en/get-started)

Start building

Get started with your first API call

Was this page helpful?

- 

- [Establish key criteria](#establish-key-criteria)

- [Choose the best model to start with](#choose-the-best-model-to-start-with)

- [Option 1: Start with a fast, cost-effective model](#option-1-start-with-a-fast-cost-effective-model)

- [Option 2: Start with the most capable model](#option-2-start-with-the-most-capable-model)

- [Model selection matrix](#model-selection-matrix)

- [Decide whether to upgrade or change models](#decide-whether-to-upgrade-or-change-models)

- [Next steps](#next-steps)

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
