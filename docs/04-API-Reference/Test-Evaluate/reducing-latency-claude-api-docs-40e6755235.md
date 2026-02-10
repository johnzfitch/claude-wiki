---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:05:00Z"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency"
title: "Reducing latency - Claude API Docs"
---

Test & evaluate

# Reducing latency

Copy page

Copy page

Latency refers to the time it takes for the model to process a prompt and and generate an output. Latency can be influenced by various factors, such as the size of the model, the complexity of the prompt, and the underlying infrastructure supporting the model and point of interaction.

It's always better to first engineer a prompt that works well without model or prompt constraints, and then try latency reduction strategies afterward. Trying to reduce latency prematurely might prevent you from discovering what top performance looks like.

------------------------------------------------------------------------

## 

How to measure latency

When discussing latency, you may come across several terms and measurements:

- **Baseline latency**: This is the time taken by the model to process the prompt and generate the response, without considering the input and output tokens per second. It provides a general idea of the model's speed.
- **Time to first token (TTFT)**: This metric measures the time it takes for the model to generate the first token of the response, from when the prompt was sent. It's particularly relevant when you're using streaming (more on that later) and want to provide a responsive experience to your users.

For a more in-depth understanding of these terms, check out our [glossary](/docs/en/about-claude/glossary).

------------------------------------------------------------------------

## 

How to reduce latency

### 

1\. Choose the right model

One of the most straightforward ways to reduce latency is to select the appropriate model for your use case. Anthropic offers a [range of models](/docs/en/about-claude/models/overview) with different capabilities and performance characteristics. Consider your specific requirements and choose the model that best fits your needs in terms of speed and output quality.

For speed-critical applications, **Claude Haiku 4.5** offers the fastest response times while maintaining high intelligence:

``` shiki
import anthropic

client = anthropic.Anthropic()

# For time-sensitive applications, use Claude Haiku 4.5
message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=100,
    messages=[{
        "role": "user",
        "content": "Summarize this customer feedback in 2 sentences: [feedback text]"
    }]
)
```

For more details about model metrics, see our [models overview](/docs/en/about-claude/models/overview) page.

### 

2\. Optimize prompt and output length

Minimize the number of tokens in both your input prompt and the expected output, while still maintaining high performance. The fewer tokens the model has to process and generate, the faster the response will be.

Here are some tips to help you optimize your prompts and outputs:

- **Be clear but concise**: Aim to convey your intent clearly and concisely in the prompt. Avoid unnecessary details or redundant information, while keeping in mind that [claude lacks context](/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct) on your use case and may not make the intended leaps of logic if instructions are unclear.

- **Ask for shorter responses:**: Ask Claude directly to be concise. The Claude 3 family of models has improved steerability over previous generations. If Claude is outputting unwanted length, ask Claude to [curb its chattiness](/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct).

  Due to how LLMs count [tokens](/docs/en/about-claude/glossary#tokens) instead of words, asking for an exact word count or a word count limit is not as effective a strategy as asking for paragraph or sentence count limits.

- **Set appropriate output limits**: Use the `max_tokens` parameter to set a hard limit on the maximum length of the generated response. This prevents Claude from generating overly long outputs.

  > **Note**: When the response reaches `max_tokens` tokens, the response will be cut off, perhaps midsentence or mid-word, so this is a blunt technique that may require post-processing and is usually most appropriate for multiple choice or short answer responses where the answer comes right at the beginning.

- **Experiment with temperature**: The `temperature` [parameter](/docs/en/api/messages) controls the randomness of the output. Lower values (e.g., 0.2) can sometimes lead to more focused and shorter responses, while higher values (e.g., 0.8) may result in more diverse but potentially longer outputs.

Finding the right balance between prompt clarity, output quality, and token count may require some experimentation.

### 

3\. Leverage streaming

Streaming is a feature that allows the model to start sending back its response before the full output is complete. This can significantly improve the perceived responsiveness of your application, as users can see the model's output in real-time.

With streaming enabled, you can process the model's output as it arrives, updating your user interface or performing other tasks in parallel. This can greatly enhance the user experience and make your application feel more interactive and responsive.

Visit [streaming Messages](/docs/en/build-with-claude/streaming) to learn about how you can implement streaming for your use case.

Was this page helpful?

- 

- [How to measure latency](#how-to-measure-latency)

- [How to reduce latency](#how-to-reduce-latency)

- [1. Choose the right model](#1-choose-the-right-model)

- [2. Optimize prompt and output length](#2-optimize-prompt-and-output-length)

- [3. Leverage streaming](#3-leverage-streaming)

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
