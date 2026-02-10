---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:08:19Z"
source_url: "https://platform.claude.com/docs/en/api/java/completions"
title: "Completions - Claude API Reference"
---

Copy page

Java

# Completions

##### [Create a Text Completion](/docs/en/api/completions/create)

[Completion](/docs/en/api/completions#completion) completions().create(CompletionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

post/v1/complete

##### ModelsExpand Collapse 

class Completion:

String id

Unique object identifier.

The format and length of IDs may change over time.

String completion

The resulting completion up to and excluding the stop sequences.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE_OPUS_4_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE_OPUS_4_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE_3_7_SONNET_LATEST("claude-3-7-sonnet-latest")

High-performance model with early extended thinking

CLAUDE_3_7_SONNET_20250219("claude-3-7-sonnet-20250219")

High-performance model with early extended thinking

CLAUDE_3_5_HAIKU_LATEST("claude-3-5-haiku-latest")

Fastest and most compact model for near-instant responsiveness

CLAUDE_3_5_HAIKU_20241022("claude-3-5-haiku-20241022")

Our fastest model

CLAUDE_HAIKU_4_5("claude-haiku-4-5")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")

Hybrid model, capable of near-instant responses and extended thinking

CLAUDE_SONNET_4_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE_SONNET_4_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE_4_SONNET_20250514("claude-4-sonnet-20250514")

High-performance model with extended thinking

CLAUDE_SONNET_4_5("claude-sonnet-4-5")

Our best model for real-world agents and coding

CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")

Our best model for real-world agents and coding

CLAUDE_OPUS_4_0("claude-opus-4-0")

Our most capable model

CLAUDE_OPUS_4_20250514("claude-opus-4-20250514")

Our most capable model

CLAUDE_4_OPUS_20250514("claude-4-opus-20250514")

Our most capable model

CLAUDE_OPUS_4_1_20250805("claude-opus-4-1-20250805")

Our most capable model

CLAUDE_3_OPUS_LATEST("claude-3-opus-latest")

Excels at writing and complex tasks

CLAUDE_3_OPUS_20240229("claude-3-opus-20240229")

Excels at writing and complex tasks

CLAUDE_3_HAIKU_20240307("claude-3-haiku-20240307")

Our previous most fast and cost-effective

Optional\<String\> stopReason

The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

JsonValue; type "completion"constant"completion"constant

Object type.

For Text Completions, this is always `"completion"`.

Accepts one of the following:

COMPLETION("completion")

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
