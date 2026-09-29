---
title: "Reducing latency - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency"
category: "04-API-Reference/Test-Evaluate"
fetched_at: "2026-09-26T06:39:59Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Ftest-and-evaluate%2Fstrengthen-guardrails%2Freduce-latency)





SearchCtrlK

Use cases

[Overview](/docs/en/about-claude/use-case-guides/overview)[Ticket routing](/docs/en/about-claude/use-case-guides/ticket-routing)[Customer support agent](/docs/en/about-claude/use-case-guides/customer-support-chat)[Content moderation](/docs/en/about-claude/use-case-guides/content-moderation)[Legal summarization](/docs/en/about-claude/use-case-guides/legal-summarization)[Commerce agent](/docs/en/about-claude/use-case-guides/commerce-agents)

Prompt engineering

[Overview](/docs/en/build-with-claude/prompt-engineering/overview)[Prompting best practices](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)[Prompting Claude Fable 5.1](/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)[Prompting Claude Fable 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)[Prompting Claude Opus 5.5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5)[Prompting Claude Opus 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)[Prompting Claude Opus 4.8](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8)[Prompting Claude Sonnet 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5)

Test and evaluate

[Define success and build evaluations](/docs/en/test-and-evaluate/develop-tests)[Reducing latency](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)

Strengthen guardrails

[Reduce hallucinations](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)[Increase output consistency](/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)[Mitigate jailbreaks](/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks)[Reduce prompt leak](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-prompt-leak)

Reference

[Glossary](/docs/en/about-claude/glossary)[Additional resources](/docs/en/about-claude/additional-resources)

[Console](/)

[Best practices](/docs/en/about-claude/use-case-guides/overview)Test and evaluate

# Reducing latency

Copy page



Reduce Claude's response latency by choosing a faster model like Claude Haiku 4.5, trimming prompt and output tokens, and streaming responses.

Copy page



Latency refers to the time it takes for the model to process a prompt and generate an output. Latency can be influenced by various factors, such as the size of the model, the complexity of the prompt, and the underlying infrastructure supporting the model and point of interaction.



It's always better to first engineer a prompt that works well without model or prompt constraints, and then try latency reduction strategies afterward. Trying to reduce latency prematurely might prevent you from discovering what top performance looks like.

------------------------------------------------------------------------

## How to measure latency

When discussing latency, you might come across several terms and measurements:

- **Baseline latency:** This is the time taken by the model to process the prompt and generate the response, without considering the input and output tokens per second. It provides a general idea of the model's speed.
- **Time to first token (TTFT):** This metric measures the time it takes for the model to generate the first token of the response, from when the prompt was sent. It's particularly relevant when you're using streaming (more on that later) and want to provide a responsive experience to your users.

For a more in-depth understanding of these terms, check out the [glossary](/docs/en/about-claude/glossary).

------------------------------------------------------------------------

## How to reduce latency

### 1. Choose the right model

One of the most direct ways to reduce latency is to select the appropriate model for your use case. Anthropic offers a [range of models](/docs/en/models/overview) with different capabilities and performance characteristics. Consider your specific requirements and choose the model that best fits your needs in terms of speed and output quality.

For speed-critical applications, **Claude Haiku 4.5** offers the fastest response times while maintaining high intelligence:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

# For time-sensitive applications, use Claude Haiku 4.5
message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Summarize this customer feedback in 2 sentences: [feedback text]",
        }
    ],
)
print(message.content[0].text)
```

For more details about model metrics, see the [models overview](/docs/en/models/overview) page.

### 2. Optimize prompt and output length

Minimize the number of tokens in both your input prompt and the expected output, while still maintaining high performance. The fewer tokens the model has to process and generate, the faster the response will be.

Here are some tips to help you optimize your prompts and outputs:

- **Be clear but concise:** Aim to convey your intent clearly and concisely in the prompt. Avoid unnecessary details or redundant information, while keeping in mind that [Claude lacks context](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct) on your use case and might not make the intended leaps of logic if instructions are unclear.
- **Ask for shorter responses:** Ask Claude directly to be concise. If Claude is outputting unwanted length, ask Claude to [curb its chattiness](/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#be-clear-and-direct).
  
  Because of how LLMs count [tokens](/docs/en/about-claude/glossary#tokens) instead of words, asking for an exact word count or a word count limit is not as effective a strategy as asking for paragraph or sentence count limits.
- **Set appropriate output limits:** Use the `max_tokens` parameter to set a hard limit on the maximum length of the generated response. This prevents Claude from generating overly long outputs.
  
  When the response reaches `max_tokens` tokens, the response will be cut off, perhaps mid-sentence or mid-word, so this is a blunt technique that might require post-processing and is usually most appropriate for multiple choice or short answer responses where the answer comes right at the beginning.
- **Experiment with temperature:** The `temperature` [parameter](/docs/en/api/messages/create) controls the randomness of the output. Lower values (for example, 0.2) can sometimes lead to more focused and shorter responses, while higher values (for example, 0.8) might result in more diverse but potentially longer outputs.

Finding the right balance among prompt clarity, output quality, and token count might require some experimentation.

### 3. Stream responses

Streaming is a feature that allows the model to start sending back its response before the full output is complete. This can significantly improve the perceived responsiveness of your application, as users can see the model's output in real time.

With streaming enabled, you can process the model's output as it arrives, updating your user interface or performing other tasks in parallel.

Visit [Streaming messages](/docs/en/build-with-claude/streaming) to learn about how you can implement streaming for your use case.

------------------------------------------------------------------------

## Next steps



[Reduce hallucinations](/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)

Minimize hallucinations in Claude's outputs by allowing uncertainty, grounding responses in direct quotes, and verifying claims with citations.



[Streaming messages](/docs/en/build-with-claude/streaming)

Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.
