---
category: "10-Prompting-Guides"
fetched_at: "2026-02-07T10:04:53Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompt-improver"
title: "Use our prompt improver to optimize your prompts - Claude API Docs"
---

Prompt engineering

# Use our prompt improver to optimize your prompts

Copy page

Copy page

Our prompt improver is compatible with all Claude models, including those with extended thinking capabilities. For prompting tips specific to extended thinking models, see [here](/docs/en/build-with-claude/extended-thinking).

The prompt improver helps you quickly iterate and improve your prompts through automated analysis and enhancement. It excels at making prompts more robust for complex tasks that require high accuracy.

## 

Before you begin

You'll need:

- A [prompt template](/docs/en/build-with-claude/prompt-engineering/prompt-templates-and-variables) to improve
- Feedback on current issues with Claude's outputs (optional but recommended)
- Example inputs and ideal outputs (optional but recommended)

## 

How the prompt improver works

The prompt improver enhances your prompts in 4 steps:

1.  **Example identification**: Locates and extracts examples from your prompt template
2.  **Initial draft**: Creates a structured template with clear sections and XML tags
3.  **Chain of thought refinement**: Adds and refines detailed reasoning instructions
4.  **Example enhancement**: Updates examples to demonstrate the new reasoning process

You can watch these steps happen in real-time in the improvement modal.

## 

What you get

The prompt improver generates templates with:

- Detailed chain-of-thought instructions that guide Claude's reasoning process and typically improve its performance
- Clear organization using XML tags to separate different components
- Standardized example formatting that demonstrates step-by-step reasoning from input to output
- Strategic prefills that guide Claude's initial responses

While examples appear separately in the Workbench UI, they're included at the start of the first user message in the actual API call. View the raw format by clicking "**\</\> Get Code**" or insert examples as raw text via the Examples box.

## 

How to use the prompt improver

1.  Submit your prompt template
2.  Add any feedback about issues with Claude's current outputs (e.g., "summaries are too basic for expert audiences")
3.  Include example inputs and ideal outputs
4.  Review the improved prompt

## 

Generate test examples

Don't have examples yet? Use our [Test Case Generator](/docs/en/test-and-evaluate/eval-tool#creating-test-cases) to:

1.  Generate sample inputs
2.  Get Claude's responses
3.  Edit the responses to match your ideal outputs
4.  Add the polished examples to your prompt

## 

When to use the prompt improver

The prompt improver works best for:

- Complex tasks requiring detailed reasoning
- Situations where accuracy is more important than speed
- Problems where Claude's current outputs need significant improvement

For latency or cost-sensitive applications, consider using simpler prompts. The prompt improver creates templates that produce longer, more thorough, but slower responses.

## 

Example improvement

Here's how the prompt improver enhances a basic classification prompt:

### Original prompt

### Improved prompt

Notice how the improved prompt:

- Adds clear step-by-step reasoning instructions
- Uses XML tags to organize content
- Provides explicit output formatting requirements
- Guides Claude through the analysis process

## 

Troubleshooting

Common issues and solutions:

- **Examples not appearing in output**: Check that examples are properly formatted with XML tags and appear at the start of the first user message
- **Chain of thought too verbose**: Add specific instructions about desired output length and level of detail
- **Reasoning steps don't match your needs**: Modify the steps section to match your specific use case

------------------------------------------------------------------------

## 

Next steps

[](/docs/en/resources/prompt-library/library)

Prompt library

Get inspired by example prompts for various tasks.

[](https://github.com/anthropics/prompt-eng-interactive-tutorial)

GitHub prompting tutorial

Learn prompting best practices with our interactive tutorial.

[](/docs/en/test-and-evaluate/eval-tool)

Test your prompts

Use our evaluation tool to test your improved prompts.

Was this page helpful?

- 

- [Before you begin](#before-you-begin)

- [How the prompt improver works](#how-the-prompt-improver-works)

- [What you get](#what-you-get)

- [How to use the prompt improver](#how-to-use-the-prompt-improver)

- [Generate test examples](#generate-test-examples)

- [When to use the prompt improver](#when-to-use-the-prompt-improver)

- [Example improvement](#example-improvement)

- [Troubleshooting](#troubleshooting)

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
