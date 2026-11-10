---
title: "Multilingual support - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/multilingual-support"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-05T06:36:59Z"
tags: ["api"]
---

# Multilingual support

Copy page



Claude excels at tasks across multiple languages, maintaining strong cross-lingual performance relative to English.

Copy page



Multilingual support

[APIs](#feature-availability)  
Messages APIAlways onManaged AgentsAlways on

[Cloud platforms](#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableAmazon BedrockAvailableAmazon BedrockInvokeModelAvailableClaude Models on Google CloudGoogle managedAvailableMicrosoft FoundryAvailable

## Overview

Claude demonstrates robust multilingual capabilities, with particularly strong performance in zero-shot tasks across languages.

Claude is capable in many languages beyond those benchmarked in the following table. Test with any languages relevant to your specific use cases.

## Performance data

The following table shows zero-shot scores for Claude models on [Global-MMLU](https://arxiv.org/abs/2412.03304), which extends the [MMLU (Massive Multitask Language Understanding)](https://en.wikipedia.org/wiki/MMLU) test set to 42 languages. Each score is a percentage of the same model’s English score:

| Language | Claude Fable 5.1 | Claude Opus 5.5 | Claude Sonnet 5.5 | Claude Haiku 5.5 |
|----|----|----|----|----|
| English | 100% | 100% | 100% | 100% |
| Spanish | 99.4% | 99.3% | 99.0% | 98.1% |
| Portuguese (Brazil) | 99.0% | 99.2% | 98.7% | 98.1% |
| Italian | 99.0% | 99.2% | 98.4% | 97.7% |
| French | 99.0% | 99.3% | 98.7% | 97.7% |
| Indonesian | 98.9% | 99.1% | 98.6% | 97.1% |
| German | 99.1% | 99.1% | 98.5% | 97.4% |
| Arabic | 98.7% | 99.3% | 98.3% | 96.6% |
| Chinese (Simplified) | 98.8% | 99.3% | 98.5% | 97.7% |
| Korean | 98.8% | 99.1% | 98.3% | 97.0% |
| Japanese | 98.7% | 99.2% | 98.4% | 97.4% |
| Hindi | 98.9% | 99.2% | 98.5% | 96.6% |
| Bengali | 98.3% | 98.6% | 97.2% | 95.4% |
| Swahili | 97.7% | 98.3% | 96.9% | 94.0% |
| Yoruba | 95.1% | 96.3% | 93.6% | 87.0% |

All scores use [adaptive thinking](build-with-claude-thinking.md) at the `max` [effort level](build-with-claude-effort.md). Scores exclude questions that safety classifiers blocked or that went unanswered. For each score in the table, at most 1.7 percent of the questions are excluded.



Use the table to compare languages within a model, not to rank models. Differences of less than about 1 percentage point are within measurement noise.

------------------------------------------------------------------------

## Set the response language

Claude infers the response language from the conversation, but for production applications you should state the target language explicitly. The most reliable place to do this is the system prompt, which keeps the instruction stable across every turn of a conversation.

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

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    system="Always respond in French, regardless of the language the user writes in.",
    messages=[{"role": "user", "content": "How do I reset my password?"}],
)

print(message.content)
```

If your application lets users pick a language at runtime, interpolate that choice into the system prompt rather than relying on Claude to infer it from the user’s message. To translate between two specific languages, name both: `Translate the user's message from German to Korean. Respond with only the translation.`

------------------------------------------------------------------------

## Best practices

When working with multilingual content:

1.  **Provide clear language context:** Although Claude can detect the target language automatically, explicitly stating the input and output languages you want improves reliability. For enhanced fluency, you can prompt Claude to use “idiomatic speech as if it were a native speaker.”
2.  **Use native scripts:** Submit text in its native script rather than transliteration for optimal results.
3.  **Consider cultural context:** Effective communication often requires cultural and regional awareness beyond pure translation.

Also follow the general guidance in [Prompt engineering overview](../../10-Prompting-Guides/build-with-claude-prompt-engineering-overview.md) to further improve output quality.

------------------------------------------------------------------------

## Language support considerations

- Claude processes input and generates output in most world languages that use standard Unicode characters.
- Performance varies by language, with particularly strong capabilities in widely spoken languages.
- Even in languages with fewer digital resources, Claude maintains meaningful capabilities.

## Next steps



[Prompt engineering overview](../../10-Prompting-Guides/build-with-claude-prompt-engineering-overview.md)

Apply general prompting techniques to improve multilingual output quality.

[Customer support agent](../About/about-claude-use-case-guides-customer-support-chat.md)

Build a customer support chatbot. One chatbot can serve customers in many languages.



[Models overview](../../20-Models/about-claude-models-overview.md)

Compare model tiers to balance multilingual quality against cost and latency.



[Define success criteria and build evaluations](../Test-Evaluate/test-and-evaluate-develop-tests.md)

Apply general evaluation methods to measure output quality in each language you support.

## Availability

Multilingual support is available on every model.

### API support

[Messages API](build-with-claude-working-with-messages.md)

Usage

Always on

StatusAvailable

Cloud platforms

- Claude API
- [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)
- [Amazon Bedrock](build-with-claude-claude-in-amazon-bedrock.md)
- [Amazon Bedrock](build-with-claude-claude-on-amazon-bedrock-legacy.md)InvokeModel
- [Claude Models on Google Cloud](build-with-claude-claude-models-on-google-cloud-google-managed.md)Google managed
- [Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

[Managed Agents](../Other/managed-agents-overview.md)

Usage

Always on

StatusAvailable

Cloud platforms

- Claude API
- [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)
