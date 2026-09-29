---
title: "Pricing - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/about-claude/pricing"
category: "17-Billing-Plans"
fetched_at: "2026-09-26T06:38:19Z"
tags: ["agents", "billing"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fabout-claude%2Fpricing)





SearchCtrlK

Models

[Models overview](/docs/en/models/overview)

[Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

[Claude Opus 5.5](/docs/en/models/opus-5-5/overview)

[Claude Sonnet 5](/docs/en/models/sonnet-5/overview)

[Claude Haiku 4.5](/docs/en/models/haiku-4-5/overview)

Specialized models

Legacy models

Guides

[Choosing a model](/docs/en/about-claude/models/choosing-a-model)[Optimizing for cost and intelligence](/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)[Upgrade between model versions](/docs/en/about-claude/models/migration-guide)

Lifecycle and reference

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)[Model deprecations](/docs/en/about-claude/model-deprecations)[Model cards](/docs/en/resources/overview)[Pricing](/docs/en/about-claude/pricing)

[System prompts](/docs/en/release-notes/system-prompts/overview)

[Console](/)

[Models & pricing](/docs/en/models/overview)Lifecycle and reference

# Pricing

Copy page



Learn about Anthropic's pricing structure for models and features

Copy page



This page provides detailed pricing information for Anthropic's models and features. All prices are in USD.

For the most current pricing information, visit [claude.com/pricing](https://claude.com/pricing).

## Model pricing

The following table shows pricing for all Claude models:

[TABLE]



Additional notes

All other models use the standard 0.1x multiplier.

Claude 4.7 and later models and Claude Mythos Preview use a newer tokenizer that contributes to their improved performance on a wide range of tasks. This tokenizer produces approximately 30% more tokens for the same text. The exact increase depends on the content and workload shape. Claude Sonnet 4.6 and earlier models use the previous tokenizer.

## Cloud platform pricing

This section covers partner-operated cloud platforms, where the cloud provider invoices you. For Anthropic-operated cloud platforms billed through a marketplace, see [Claude Platform on AWS pricing](#claude-platform-on-aws-pricing) and [Claude in Microsoft Foundry pricing](#claude-in-microsoft-foundry-pricing).

Claude models are available on [Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock) and [Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai). For official pricing, visit:

- [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
- [Google Cloud pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing#claude-models)



**Regional and multi-region endpoint pricing for Claude 4.5 models and beyond**

Starting with Claude Sonnet 4.5, Haiku 4.5, and Opus 4.5:

- **Bedrock** offers two endpoint types: global endpoints (dynamic routing for maximum availability) and regional endpoints (guaranteed data routing through specific geographic regions).
- **Google Cloud** offers three endpoint types: global endpoints, multi-region endpoints (dynamic routing within a geographic area), and regional endpoints.

Regional and multi-region endpoints include a 10% premium over global endpoints. The Claude API (first-party) is global by default; for first-party data residency options and pricing, see [Data residency pricing](#data-residency-pricing).

**Scope:** This pricing structure applies to Claude Sonnet 4.5, Haiku 4.5, Opus 4.5, and all future models. Earlier models (Claude Opus 4.1 and prior releases) retain their existing pricing.

For implementation details and code examples:

- [Amazon Bedrock global vs regional endpoints](/docs/en/build-with-claude/claude-in-amazon-bedrock#regions) for Opus 4.7, Haiku 4.5, and later models, or [the legacy integration](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy#global-vs-regional-endpoints) for all other models on Bedrock
- [Google Cloud global, multi-region, and regional endpoints](/docs/en/build-with-claude/claude-on-vertex-ai#global-multi-region-and-regional-endpoints)

## Claude Platform on AWS pricing

[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws) bills through AWS Marketplace using Claude Consumption Units (CCUs). Anthropic rates your token usage in USD at standard per-model, per-feature rates, applies any negotiated discount, converts the result to CCUs at \$0.01 per CCU, and reports the CCU quantity to AWS Marketplace hourly. Your AWS bill shows a single CCU line item.

[TABLE]

### Inference geography

For Claude 4.6 and later models, using `inference_geo: "us"` applies a 1.1x pricing multiplier. `inference_geo: "global"` (default) uses standard pricing. See [Data residency](/docs/en/manage-claude/data-residency) for details.

### Private offers

When you sign up on the AWS Console **Claude Platform on AWS** service page, the AWS Console looks up any private offer associated with your account and prompts you to accept it in AWS Marketplace. Contact your Anthropic account representative for private offer terms.



If you have an existing Amazon Bedrock private offer, contact your Anthropic or AWS account representative before getting started with Claude Platform on AWS to ensure your discounts are applied correctly. Discounts cannot be applied retroactively to usage incurred before your private offer is accepted.

## Claude in Microsoft Foundry pricing

[Claude in Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry) bills through the Azure Marketplace using Claude Consumption Units (CCUs). Anthropic rates your token usage in USD at standard per-model, per-feature rates, applies any negotiated discount, converts the result to CCUs at \$0.01 per CCU, and reports the CCU quantity to the Azure Marketplace hourly. Your Azure bill shows a single CCU line item.

[TABLE]

### Inference geography

Deployments hosted on Azure can use the US Data Zone Standard deployment type, which keeps inference within the United States. This is equivalent to `inference_geo: "us"` on the Claude API and applies the same 1.1x pricing multiplier. See [Data residency](/docs/en/manage-claude/data-residency) for details.

## Feature-specific pricing

### Prompt caching

Prompt caching reduces costs and latency by reusing previously processed portions of your prompt across API calls. Instead of reprocessing the same large system prompt, document, or conversation history on every request, the API reads from cache at a fraction of the standard input price.

There are two ways to enable prompt caching:

- **Automatic caching:** Add a single `cache_control` field at the top level of your request. The system automatically manages cache breakpoints as conversations grow. This is the recommended starting point for most use cases.
- **Explicit cache breakpoints:** Place `cache_control` directly on individual content blocks for fine-grained control over exactly what gets cached.

Prompt caching uses the following pricing multipliers relative to base input token rates:

| Cache operation      | Multiplier                                                                                         | Duration                             |
|:---------------------|:---------------------------------------------------------------------------------------------------|:-------------------------------------|
| 5-minute cache write | 1.25x base input price                                                                             | Cache valid for 5 minutes            |
| 1-hour cache write   | 2x base input price                                                                                | Cache valid for 1 hour               |
| Cache read (hit)     | 0.1x base input price (0.025x on Claude Fable 5.1 and Claude Mythos 5.1; 0.05x on Claude Opus 5.5) | Same duration as the preceding write |

Cache write tokens are charged when content is first stored. Cache read tokens are charged when a subsequent request retrieves the cached content. A cache hit costs 10% of the standard input price, which means caching pays off after one cache read for the 5-minute duration (1.25x write), or after two cache reads for the 1-hour duration (2x write). On Claude Fable 5.1 and Claude Mythos 5.1, a cache hit costs 2.5% of the standard input price (\$0.25 USD per million tokens). On Claude Opus 5.5, a cache hit costs 5% of the standard input price (\$0.20 USD per million tokens).

These multipliers stack with other pricing modifiers, including the Batch API discount and data residency.

For implementation details, supported models, and code examples, see [Prompt caching](/docs/en/build-with-claude/prompt-caching).

### Data residency pricing

For Claude 4.6 and later models, specifying US-only inference through the `inference_geo` parameter incurs a 1.1x multiplier on all token pricing categories, including input tokens, output tokens, cache writes, and cache reads. Global routing (the default) uses standard pricing.

This applies to the Claude API (first-party) and Claude Platform on AWS. On Claude in Microsoft Foundry, the same 1.1x multiplier applies to deployments that use the US Data Zone Standard deployment type (see [Inference geography](#foundry-inference-geography)). Partner-operated platforms (Bedrock and Google Cloud) have independent regional pricing. See [Bedrock](https://aws.amazon.com/bedrock/pricing/) and [Google Cloud](https://cloud.google.com/vertex-ai/generative-ai/pricing#claude-models) for details. Earlier models do not support the `inference_geo` parameter and always use standard pricing; requests that include the parameter on these models return a 400 error.

For more information, see [Data residency](/docs/en/manage-claude/data-residency).

### Fast mode pricing

[Fast mode](/docs/en/build-with-claude/fast-mode), in research preview, provides significantly faster output for Claude Opus 5.5, Claude Opus 5, and Claude Opus 4.8 at premium pricing. Fast mode pricing applies across the full context window, including requests over 200k input tokens. Fast mode is available on the Claude API (first-party) only; it is not available on Claude Platform on AWS or partner-operated cloud platforms.

| Model                           | Input       | Output      |
|:--------------------------------|:------------|:------------|
| Claude Opus 5.5                 | \$8 / MTok  | \$40 / MTok |
| Claude Opus 5 / Claude Opus 4.8 | \$10 / MTok | \$50 / MTok |

Fast mode is not available on Claude Opus 4.7 (requests with `speed: "fast"` return an error) or Claude Opus 4.6 (requests run at standard speed and are billed at standard rates). See [Fast mode](/docs/en/build-with-claude/fast-mode#supported-models).

Fast mode pricing stacks with other pricing modifiers:

- [Prompt caching multipliers](#prompt-caching) apply on top of fast mode pricing
- [Data residency](/docs/en/manage-claude/data-residency) multipliers apply on top of fast mode pricing

Fast mode is not available with the [Batch API](#batch-processing).

For more information, see [Fast mode](/docs/en/build-with-claude/fast-mode).

### Batch processing

The Batch API allows asynchronous processing of large volumes of requests with a 50% discount on both input and output tokens.

[TABLE]

For more information about batch processing, see [Batch processing](/docs/en/build-with-claude/batch-processing).

### Long context pricing

Claude 4.6 and later models and [Claude Mythos Preview](https://anthropic.com/glasswing) include the full [1M token context window](/docs/en/build-with-claude/context-windows) at standard pricing. (A 900k-token request is billed at the same per-token rate as a 9k-token request.) Prompt caching and batch processing discounts apply at standard rates across the full context window.

### Tool use pricing

Tool use requests are priced based on:

1.  The total number of input tokens sent to the model (including in the `tools` parameter)
2.  The number of output tokens generated
3.  For server-side tools, additional usage-based pricing (for example, web search charges per search performed)

Client-side tools are priced the same as any other Claude API request, although server-side tools can incur additional charges based on their specific usage.

The additional tokens from tool use come from:

- The `tools` parameter in API requests (tool names, descriptions, and schemas)
- `tool_use` content blocks in API requests and responses
- `tool_result` content blocks in API requests

When you use `tools`, the API also automatically includes a special system prompt for the model that enables tool use. The number of tool use tokens required for each model is listed in the following table (excluding the additional tokens listed earlier). Note that the table assumes at least 1 tool is provided. If no `tools` are provided, then a tool choice of `none` uses 0 additional system prompt tokens.

[TABLE]

These token counts are added to your normal input and output tokens to calculate the total cost of a request.

For current per-model prices, refer to the [model pricing](#model-pricing) section.

For more information about tool use implementation and best practices, see [Tool use](/docs/en/agents-and-tools/tool-use/overview).

### Specific tool pricing

#### Bash tool

The bash tool definition adds the following input tokens to your request. This is in addition to the per-model [tool use system prompt](/docs/en/agents-and-tools/tool-use/overview#pricing) that applies whenever any tool is present.

| Model                                               | Additional input tokens |
|-----------------------------------------------------|-------------------------|
| Claude Opus 5, Claude Opus 4.8, and Claude Opus 4.7 | 325 tokens              |
| Claude Opus 4.6, Claude Sonnet 4.6, and earlier     | 244 tokens              |

Additional tokens are consumed by:

- Command outputs (stdout/stderr)
- Error messages
- Large file contents

See [tool use pricing](#tool-use-pricing) for complete pricing details.

#### Code execution tool

**Code execution is free when used with web search or web fetch.** When `web_search_20260209` (or later) or `web_fetch_20260209` (or later) is included in your API request, there are no additional charges for code execution tool calls beyond the standard input and output token costs.

When used without these tools, code execution is billed by execution time, tracked separately from token usage:

- Execution time has a minimum of 5 minutes
- Each organization receives **1,550 free hours** of usage per month
- Additional usage beyond 1,550 hours is billed at **\$0.05 USD per hour, per container**
- If files are included in the request, execution time is billed even if the tool is not called, because files are preloaded onto the container

Code execution usage is tracked in the response:

```python
{
  "usage": {
    "input_tokens": 105,
    "output_tokens": 239,
    "server_tool_use": {
      "code_execution_requests": 1
    }
  }
}
```



#### Text editor tool

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you're using.

In addition to the base tokens, the following additional input tokens are needed for the text editor tool:

| Tool                                | Additional input tokens |
|-------------------------------------|-------------------------|
| `text_editor_20250429` (Claude 4.x) | 700 tokens              |

See [tool use pricing](#tool-use-pricing) for complete pricing details.

#### Web search tool

Web search usage is charged in addition to token usage:

```python
{
  "usage": {
    "input_tokens": 105,
    "output_tokens": 6039,
    "cache_read_input_tokens": 7123,
    "cache_creation_input_tokens": 7345,
    "server_tool_use": {
      "web_search_requests": 1
    }
  }
}
```



Web search is available on the Claude API for **\$10 per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations executed during a single turn and in subsequent conversation turns.

Each web search counts as one use, regardless of the number of results returned. If an error occurs during web search, the web search will not be billed.

#### Web fetch tool

Web fetch usage has **no additional charges** beyond standard token costs:

```python
{
  "usage": {
    "input_tokens": 25039,
    "output_tokens": 931,
    "cache_read_input_tokens": 0,
    "cache_creation_input_tokens": 0,
    "server_tool_use": {
      "web_fetch_requests": 1
    }
  }
}
```



The web fetch tool is available on the Claude API at **no additional cost**. You only pay standard token costs for the fetched content that becomes part of your conversation context.

To protect against inadvertently fetching large content that would consume excessive tokens, use the `max_content_tokens` parameter to set appropriate limits based on your use case and budget considerations.

Example token usage for typical content:

- Average web page (10 kB): ~2,500 tokens
- Large documentation page (100 kB): ~25,000 tokens
- Research paper PDF (500 kB): ~125,000 tokens

#### Computer use tool

Computer use follows the standard [tool use pricing](/docs/en/agents-and-tools/tool-use/overview#pricing). When using the computer use tool:

**Toolset definition overhead:** Declaring `computer_toolset_20260801` with its default members adds about 4,500 input tokens to a request (about 4,520 on Claude Fable 5, Claude Mythos 5, Claude Opus 5, and Claude Opus 4.8, and about 4,590 on Claude Sonnet 5), which covers the member tool definitions and the tool use system prompt. Disabling `zoom` with `configs` removes about 410 of those tokens. The exact count for a request is reported in the response `usage`, and you can estimate it in advance with the [token counting endpoint](/docs/en/build-with-claude/token-counting).

**Earlier tool versions:** The following figures apply to the `computer_20251124` and `computer_20250124` tool versions, not to `computer_toolset_20260801`:

- System prompt overhead: 466–499 tokens added to the system prompt
- Tool definition: about 735 input tokens per tool definition (measured with `computer_20250124`)

**Additional token consumption:**

- Screenshot and zoom images returned in tool results, billed as image input (see [Vision pricing](/docs/en/build-with-claude/vision#evaluate-image-size))
- Tool execution results returned to Claude



If you're also using bash or text editor tools alongside computer use, those tools have their own token costs as documented in their respective pages.

#### Browser use tool

Browser use follows the standard [tool use pricing](/docs/en/agents-and-tools/tool-use/overview#pricing). When using the browser use tool:

**Toolset definition overhead:** Declaring `browser_toolset_20260801` with its default members adds about 6,600 input tokens to a request (about 6,610 on Claude Fable 5, Claude Mythos 5, Claude Opus 5, and Claude Opus 4.8, and about 6,670 on Claude Sonnet 5), which covers the member tool definitions and the tool use system prompt. Enabling all four optional members adds about 880 tokens, and disabling members with `configs` reduces the count. The exact count for a request is reported in the response `usage`, and you can estimate it in advance with the [token counting endpoint](/docs/en/build-with-claude/token-counting).

**Additional token consumption:**

- Screenshot and zoom images returned in tool results, billed as image input (see [Vision pricing](/docs/en/build-with-claude/vision#evaluate-image-size))
- Text tool results returned to Claude, such as accessibility trees, page text, and console or network entries



If you also use the computer use tool, bash tool, text editor tool, or your own tools alongside browser use, those tools have their own token costs as documented on their respective pages.

## Claude Managed Agents pricing

[Claude Managed Agents](/docs/en/managed-agents/overview) is billed on two dimensions: tokens and session runtime.

### Tokens

All tokens consumed by a Claude Managed Agents session are billed at the rates shown in [Model pricing](#model-pricing). [Prompt caching](#prompt-caching) multipliers apply identically. Web search triggered inside a session incurs the standard \$10 per 1,000 searches. On [Claude Platform on AWS](#claude-platform-on-aws-pricing), session token and runtime charges convert to Claude Consumption Units at the standard rate. [Fast mode](#fast-mode-pricing) premium pricing applies when an agent's `model.speed` is set to `"fast"`.

The [data residency multiplier](#data-residency-pricing) also applies: when an agent's `model.inference_geo` is pinned to `"us"`, tokens consumed by sessions running that agent are billed at 1.1x the standard rates, the same multiplier that applies to US-only inference on the Messages API.

The following Messages API modifiers do **not** apply to Claude Managed Agents sessions:

| Modifier                                          | Why it doesn't apply                                           |
|---------------------------------------------------|----------------------------------------------------------------|
| [Batch API discount](#batch-processing)           | Sessions are stateful and interactive. There is no batch mode. |
| [Cloud platform pricing](#cloud-platform-pricing) | Not available on partner-operated cloud platforms.             |

### Session runtime

| SKU             | Rate                    | Metering                  |
|-----------------|-------------------------|---------------------------|
| Session runtime | \$0.08 per session-hour | `running` status duration |

Runtime is measured to the millisecond and accrues only while the session's status is `running`. Time spent `idle` (waiting for your next message or a tool confirmation), `rescheduling`, or `terminated` does not count toward runtime.



Session runtime replaces the [code execution](#code-execution-tool) container-hour billing model when using Claude Managed Agents. You are not separately billed for container hours on top of session runtime.

### Worked example

A one-hour coding session using Claude Opus 5 that consumes 50,000 input tokens and 15,000 output tokens:

| Line item       | Calculation               | Cost        |
|-----------------|---------------------------|-------------|
| Input tokens    | 50,000 × \$5 / 1,000,000  | \$0.25      |
| Output tokens   | 15,000 × \$25 / 1,000,000 | \$0.375     |
| Session runtime | 1.0 hour × \$0.08         | \$0.08      |
| **Total**       |                           | **\$0.705** |

If prompt caching is active and 40,000 of the input tokens are cache reads:

| Line item             | Calculation                    | Cost        |
|-----------------------|--------------------------------|-------------|
| Uncached input tokens | 10,000 × \$5 / 1,000,000       | \$0.05      |
| Cache read tokens     | 40,000 × \$5 × 0.1 / 1,000,000 | \$0.02      |
| Output tokens         | 15,000 × \$25 / 1,000,000      | \$0.375     |
| Session runtime       | 1.0 hour × \$0.08              | \$0.08      |
| **Total**             |                                | **\$0.525** |



Example calculation for processing 10,000 support tickets:

- Average ~3,700 tokens per conversation
- Using Claude Haiku 4.5 at \$1/MTok input, \$5/MTok output
- Total cost: ~\$37.00 per 10,000 tickets

For a detailed walkthrough of this calculation, see the [customer support agent guide](/docs/en/about-claude/use-case-guides/customer-support-chat).

## Additional pricing considerations

### Cost optimization strategies

When building agents with Claude:

1.  **Use appropriate models:** Choose Haiku for simple tasks, Sonnet for most production workloads, and Opus for the most complex reasoning
2.  **Implement prompt caching:** Reduce costs for repeated context
3.  **Batch operations:** Use the Batch API for non-time-sensitive tasks
4.  **Monitor usage patterns:** Track token consumption to identify optimization opportunities



For high-volume agent applications, contact the [enterprise sales team](https://claude.com/contact-sales) for custom pricing arrangements.

### Rate limits

Rate limits vary by usage tier and affect how many requests you can make:

- **Start tier:** Entry-level limits for getting started
- **Build tier:** Increased limits for growing applications
- **Scale tier:** Highest standard limits for production workloads

For detailed rate limit information, see [Rate limits](/docs/en/api/rate-limits).

For limits beyond the Scale tier or custom pricing arrangements, [contact the sales team](https://claude.com/contact-sales).

### Volume discounts

Volume discounts may be available for high-volume users. These are negotiated on a case-by-case basis.

- Standard usage tiers use the pricing shown in [Model pricing](#model-pricing)
- Enterprise customers can [contact sales](mailto:sales@anthropic.com) for custom pricing
- Academic and research discounts may be available

### Enterprise pricing

For enterprise customers with specific needs:

- Custom rate limits
- Volume discounts
- Dedicated support
- Custom terms

Contact the sales team at <sales@anthropic.com> or through the [Claude Console](/settings/limits) to discuss enterprise pricing options.

## Billing and payment

- Billing is based on actual monthly usage
- All payments are in USD
- Credit card and invoicing options available
- Usage tracking available in the [Claude Console](/)

## Frequently asked questions

### How is token usage calculated?

Tokens are pieces of text that models process. As a rough estimate, 1 token is approximately 4 characters or 0.75 words in English. The exact count varies by language and content type.

### Are there free tiers or trials?

New users receive a small amount of free credits to test the API. [Contact sales](mailto:sales@anthropic.com) for information about extended trials for enterprise evaluation.

### How do discounts stack?

Batch API and prompt caching discounts can be combined. For example, using both features together provides significant cost savings compared to standard API calls. See [prompt caching pricing](#prompt-caching) for how the multipliers interact.

### What payment methods are accepted?

Major credit cards are accepted for standard accounts. Enterprise customers can arrange invoicing and other payment methods.

For additional questions about pricing, contact <support@anthropic.com>.
