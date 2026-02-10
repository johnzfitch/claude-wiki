---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:04:15Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/multilingual-support"
title: "Multilingual support - Claude API Docs"
---

Capabilities

# Multilingual support

Copy page

Claude excels at tasks across multiple languages, maintaining strong cross-lingual performance relative to English.

Copy page

## 

Overview

Claude demonstrates robust multilingual capabilities, with particularly strong performance in zero-shot tasks across languages. The model maintains consistent relative performance across both widely-spoken and lower-resource languages, making it a reliable choice for multilingual applications.

Note that Claude is capable in many languages beyond those benchmarked below. We encourage testing with any languages relevant to your specific use cases.

## 

Performance data

Below are the zero-shot chain-of-thought evaluation scores for Claude models across different languages, shown as a percent relative to English performance (100%):

| Language | Claude Opus 4.1¹ | Claude Opus 4¹ | Claude Sonnet 4.5¹ | Claude Sonnet 4¹ | Claude Haiku 4.5¹ |
|----|----|----|----|----|----|
| English (baseline, fixed to 100%) | 100% | 100% | 100% | 100% | 100% |
| Spanish | 98.1% | 98.0% | 98.2% | 97.5% | 96.4% |
| Portuguese (Brazil) | 97.8% | 97.3% | 97.8% | 97.2% | 96.1% |
| Italian | 97.7% | 97.5% | 97.9% | 97.3% | 96.0% |
| French | 97.9% | 97.7% | 97.5% | 97.1% | 95.7% |
| Indonesian | 97.3% | 97.2% | 97.3% | 96.2% | 94.2% |
| German | 97.7% | 97.1% | 97.0% | 94.7% | 94.3% |
| Arabic | 97.1% | 96.9% | 97.2% | 96.1% | 92.5% |
| Chinese (Simplified) | 97.1% | 96.7% | 96.9% | 95.9% | 94.2% |
| Korean | 96.6% | 96.4% | 96.7% | 95.9% | 93.3% |
| Japanese | 96.9% | 96.2% | 96.8% | 95.6% | 93.5% |
| Hindi | 96.8% | 96.7% | 96.7% | 95.8% | 92.4% |
| Bengali | 95.7% | 95.2% | 95.4% | 94.4% | 90.4% |
| Swahili | 89.8% | 89.5% | 91.1% | 87.1% | 78.3% |
| Yoruba | 80.3% | 78.9% | 79.7% | 76.4% | 52.7% |

¹ With [extended thinking](/docs/en/build-with-claude/extended-thinking).

These metrics are based on [MMLU (Massive Multitask Language Understanding)](https://en.wikipedia.org/wiki/MMLU) English test sets that were translated into 14 additional languages by professional human translators, as documented in [OpenAI's simple-evals repository](https://github.com/openai/simple-evals/blob/main/multilingual_mmlu_benchmark_results.md). The use of human translators for this evaluation ensures high-quality translations, particularly important for languages with fewer digital resources.

------------------------------------------------------------------------

## 

Best practices

When working with multilingual content:

1.  **Provide clear language context**: While Claude can detect the target language automatically, explicitly stating the desired input/output language improves reliability. For enhanced fluency, you can prompt Claude to use "idiomatic speech as if it were a native speaker."
2.  **Use native scripts**: Submit text in its native script rather than transliteration for optimal results
3.  **Consider cultural context**: Effective communication often requires cultural and regional awareness beyond pure translation

We also suggest following our general [prompt engineering guidelines](/docs/en/build-with-claude/prompt-engineering/overview) to better improve Claude's performance.

------------------------------------------------------------------------

## 

Language support considerations

- Claude processes input and generates output in most world languages that use standard Unicode characters
- Performance varies by language, with particularly strong capabilities in widely-spoken languages
- Even in languages with fewer digital resources, Claude maintains meaningful capabilities

[](/docs/en/build-with-claude/prompt-engineering/overview)

Prompt Engineering Guide

Master the art of prompt crafting to get the most out of Claude.

[](/docs/en/resources/prompt-library)

Prompt Library

Find a wide range of pre-crafted prompts for various tasks and industries. Perfect for inspiration or quick starts.

Was this page helpful?

- 

- [Overview](#overview)

- [Performance data](#performance-data)

- [Best practices](#best-practices)

- [Language support considerations](#language-support-considerations)

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
