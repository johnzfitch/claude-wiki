---
title: "Reducing latency - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency"
category: "04-API-Reference/Test-Evaluate"
fetched_at: "2026-11-05T06:36:37Z"
tags: ["api"]
---

# Reducing latency

Copy page



Reduce Claude’s response latency by choosing a faster model such as Claude Haiku 5.5, trimming prompt and output tokens, and streaming responses.

Copy page



Latency refers to the time it takes for the model to process a prompt and generate an output. Latency can be influenced by various factors, such as the size of the model, the complexity of the prompt, and the underlying infrastructure supporting the model and point of interaction.



It’s always better to first engineer a prompt that works well without model or prompt constraints, and then try latency reduction strategies afterward. Trying to reduce latency prematurely might prevent you from discovering what top performance looks like.

------------------------------------------------------------------------

## How to measure latency

When discussing latency, you might come across several terms and measurements:

- **Baseline latency:** This is the time taken by the model to process the prompt and generate the response, without considering the input and output tokens per second. It provides a general idea of the model’s speed.
- **Time to first token (TTFT):** This metric measures the time it takes for the model to generate the first token of the response, from when the prompt was sent. It’s particularly relevant when you’re using streaming (more on that later) and want to provide a responsive experience to your users.

For a more in-depth understanding of these terms, see the [glossary](../About/about-claude-glossary.md).

------------------------------------------------------------------------

## How to reduce latency

### 1. Choose the right model

One of the most direct ways to reduce latency is to choose the appropriate model for your use case. Anthropic offers a [range of models](../../20-Models/about-claude-models-overview.md) with different capabilities and performance characteristics. Consider your specific requirements and choose the model that best fits your needs in terms of speed and output quality.

For speed-critical applications, **Claude Haiku 5.5** offers the fastest response times while maintaining high intelligence. [Effort](../Guides/build-with-claude-effort.md) is its main control for speed and cost. See [Use effort to control thinking](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-haiku-5-5.md#use-effort-to-control-thinking). The following example runs it at `low`, the cheapest and fastest level, and leaves room in `max_tokens` for thinking:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

# For time-sensitive applications, use Claude Haiku 5.5 at low effort
message = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=1024,
    output_config={"effort": "low"},
    messages=[
        {
            "role": "user",
            "content": "Summarize this customer feedback in 2 sentences: [feedback text]",
        }
    ],
)
print(next(block.text for block in message.content if block.type == "text"))
```

For more details about model metrics, see the [models overview](../../20-Models/about-claude-models-overview.md) page.

### 2. Optimize prompt and output length

Minimize the number of tokens in both your input prompt and the expected output, while still maintaining high performance. The fewer tokens the model has to process and generate, the faster the response will be.

Here are some tips to help you optimize your prompts and outputs:

- **Be clear but concise:** Aim to convey your intent clearly and concisely in the prompt. Avoid unnecessary details or redundant information, while keeping in mind that [Claude lacks context](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#be-clear-and-direct) on your use case and might not make the intended inferences if instructions are unclear.
- **Ask for shorter responses:** Ask Claude directly to be concise. If Claude is outputting unwanted length, ask Claude to [reduce its verbosity](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#be-clear-and-direct).
  
  Because of how LLMs count [tokens](../About/about-claude-glossary.md#tokens) instead of words, asking for an exact word count or a word count limit is not as effective a strategy as asking for paragraph or sentence count limits.
- **Set appropriate output limits:** Use the `max_tokens` parameter to set a hard limit on the maximum length of the generated response. This prevents Claude from generating overly long outputs.
  
  When the response reaches `max_tokens` tokens, the response will be cut off, perhaps mid-sentence or mid-word, so this is a blunt technique that might require post-processing and is usually most appropriate for multiple choice or short answer responses where the answer comes right at the beginning.

Finding the right balance among prompt clarity, output quality, and token count might require some experimentation.

### 3. Stream responses

Streaming is a feature that allows the model to start sending back its response before the full output is complete. This can significantly improve the perceived responsiveness of your application, as users can see the model’s output in real time.

With streaming enabled, you can process the model’s output as it arrives, updating your user interface or performing other tasks in parallel.

Visit [Streaming messages](../Guides/build-with-claude-streaming.md) to learn about how you can implement streaming for your use case.

------------------------------------------------------------------------

## Next steps



[Reduce hallucinations](test-and-evaluate-strengthen-guardrails-reduce-hallucinations.md)

Minimize hallucinations in Claude’s outputs by allowing uncertainty, grounding responses in direct quotes, and verifying claims with citations.



[Streaming messages](../Guides/build-with-claude-streaming.md)

Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.
