---
title: "Pricing - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/about-claude/pricing"
category: "17-Billing-Plans"
fetched_at: "2026-11-13T06:35:11Z"
tags: ["agents", "billing"]
---

# Pricing

Copy page



Learn about Anthropic’s pricing structure for models and features

Copy page



This page provides detailed pricing information for Anthropic’s models and features. All prices are in USD.

For the most current pricing information, see the [Claude pricing](pricing.md) page.

## Model pricing

The following table shows pricing for all Claude models:

[TABLE]



Additional notes

All other models use the standard 0.1x multiplier.

Claude 4.7 and later models and Claude Mythos Preview use a newer tokenizer that contributes to their improved performance on a wide range of tasks. This tokenizer produces approximately 30% more tokens for the same text. The exact increase depends on the content and workload shape. Claude Sonnet 4.6 and earlier models use the previous tokenizer.

## Cloud platform pricing

This section covers partner-operated cloud platforms, where the cloud provider invoices you. For Anthropic-operated cloud platforms billed through a marketplace, see [Claude Platform on AWS pricing](#claude-platform-on-aws-pricing), [Claude Models on Google Cloud (Anthropic managed) billing](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#billing), and [Claude in Microsoft Foundry pricing](#claude-in-microsoft-foundry-pricing).

For official pricing on [Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md) and [Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), visit:

- [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
- [Google Cloud pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing#claude-models)



**Regional and multi-region endpoint pricing for Claude 4.5 models and beyond**

Starting with Claude Sonnet 4.5, Haiku 4.5, and Opus 4.5:

- **Bedrock** offers two endpoint types: global endpoints (dynamic routing for maximum availability) and regional endpoints (guaranteed data routing through specific geographic regions).
- **Claude Models on Google Cloud (Google managed)** offers global endpoints and multi-region endpoints (dynamic routing within a geographic area) for these models, and regional endpoints for Claude Sonnet 4.6 and earlier models.

Regional and multi-region endpoints include a 10 percent premium over global endpoints. The Claude API (first-party) is global by default; for first-party data residency options and pricing, see [Data residency pricing](#data-residency-pricing).

**Scope:** This pricing structure applies to Claude Sonnet 4.5 (deprecated), Haiku 4.5, Opus 4.5, and later models. It doesn’t apply to earlier models (Claude Opus 4.1 and prior releases).

For implementation details and code examples:

- Amazon Bedrock global versus regional endpoints: [Claude in Amazon Bedrock (`bedrock-mantle`)](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md#regions) or [Claude on Amazon Bedrock (`bedrock-runtime`)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md#global-vs-regional-endpoints), depending on whether you call `bedrock-mantle` or `bedrock-runtime`
- Google Cloud global, multi-region, and regional endpoints: [Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md#global-multi-region-and-regional-endpoints)

## Claude Platform on AWS pricing

[Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md) bills through AWS Marketplace using Claude Consumption Units (CCUs). Anthropic rates your token usage in USD at standard per-model, per-feature rates, applies any negotiated discount, converts the result to CCUs at \$0.01 USD per CCU, and reports the CCU quantity to AWS Marketplace hourly. Your AWS bill shows a single CCU line item.

[TABLE]

### Inference geography

For Claude 4.6 and later models, using `inference_geo: "us"` applies a 1.1x pricing multiplier. `inference_geo: "global"` (default) uses standard pricing. See [Data residency](../04-API-Reference/Other/manage-claude-data-residency.md) for details.

### Private offers

When you sign up on the AWS Console **Claude Platform on AWS** service page, the AWS Console looks up any private offer associated with your account and prompts you to accept it in AWS Marketplace. Contact your Anthropic account representative for private offer terms.



If you have an existing Amazon Bedrock private offer, contact your Anthropic or AWS account representative before getting started with Claude Platform on AWS to ensure your discounts are applied correctly. Discounts cannot be applied retroactively to usage incurred before your private offer is accepted.

## Claude in Microsoft Foundry pricing

[Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md) bills through the Azure Marketplace using Claude Consumption Units (CCUs). Anthropic rates your token usage in USD at standard per-model, per-feature rates, applies any negotiated discount, converts the result to CCUs at \$0.01 USD per CCU, and reports the CCU quantity to the Azure Marketplace hourly. Your Azure bill shows a single CCU line item.

[TABLE]

### Inference geography

Deployments hosted on Azure can use the US Data Zone Standard deployment type, which keeps inference within the United States. This is equivalent to `inference_geo: "us"` on the Claude API and applies the same 1.1x pricing multiplier. See [Data residency](../04-API-Reference/Other/manage-claude-data-residency.md) for details.

## Feature-specific pricing

### Prompt caching

Prompt caching reduces costs and latency by reusing previously processed portions of your prompt across API calls. Instead of reprocessing the same large system prompt, document, or conversation history on every request, the API reads from cache at a fraction of the standard input price.

There are two ways to enable prompt caching:

- **Automatic caching:** Add a single `cache_control` field at the top level of your request. The system automatically manages cache breakpoints as conversations grow. This is the recommended starting point for most use cases.
- **Explicit cache breakpoints:** Place `cache_control` directly on individual content blocks for fine-grained control over exactly what gets cached.

Prompt caching uses the following pricing multipliers relative to base input token rates:

| Cache operation | Multiplier | Duration |
|:---|:---|:---|
| 5-minute cache write | 1.25x base input price | Cache valid for 5 minutes |
| 1-hour cache write | 2x base input price | Cache valid for 1 hour |
| Cache read (hit) | 0.1x base input price on most models | Same duration as the preceding write |

Cache write tokens are charged when content is first stored. Cache read tokens are charged when a subsequent request retrieves the cached content.

Caching saves money after a small number of cache reads:

- **5-minute duration (1.25x write):** after one cache read
- **1-hour duration (2x write):** after two cache reads

What a cache hit costs depends on the model:

| Model | Cache hit multiplier | Cache hit price per million tokens |
|:---|:---|:---|
| Claude Fable 5.2 and Claude Mythos 5.2 | 0.025x | \$0.20 USD |
| Claude Fable 5.1 and Claude Mythos 5.1 | 0.025x | \$0.25 USD |
| Claude Opus 5.5 | 0.05x | \$0.20 USD |
| Claude Sonnet 5.5 | 0.05x | \$0.10 USD |
| All other models | 0.1x | See [Model pricing](#model-pricing) |

These multipliers stack with other pricing modifiers, including the Batch API discount and data residency.

For implementation details, supported models, and code examples, see [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md).

### Data residency pricing

For Claude 4.6 and later models, specifying US-only inference through the `inference_geo` parameter incurs a 1.1x multiplier on all token pricing categories, including input tokens, output tokens, cache writes, and cache reads. On Claude Haiku 5.5, the multiplier also applies to the higher prices for prompts over 100,000 tokens (see [Long context pricing](#long-context-pricing)). Global routing (the default) uses standard pricing.

This applies to the Claude API (first-party), Claude Platform on AWS, and Claude Models on Google Cloud (Anthropic managed). On Claude in Microsoft Foundry, the same 1.1x multiplier applies to deployments that use the US Data Zone Standard deployment type (see [Inference geography](#foundry-inference-geography)). Partner-operated platforms, Claude Models on Google Cloud (Google managed) and Amazon Bedrock, have independent regional pricing. See [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) and [Google Cloud pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing#claude-models) for details. Earlier models do not support the `inference_geo` parameter and always use standard pricing; requests that include the parameter on these models return a 400 error.

For more information, see [Data residency](../04-API-Reference/Other/manage-claude-data-residency.md).

### Fast mode pricing

[Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) provides up to 2.5x higher output tokens per second at premium pricing. It is available for Claude Fable 5.2, Claude Opus 5.5, Claude Opus 5, and Claude Opus 4.8. Fast mode is in research preview for Claude Opus 5 and deprecated for Claude Opus 4.8.

Fast mode pricing applies across the full context window, including requests over 200k input tokens.

Fast mode is available on the Claude API (first-party). For Claude Opus 5.5, it is also available on [Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#billing) and on [Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md) for deployments hosted on Azure.

Fast mode for Claude Fable 5.2 is also available on [Claude Models on Google Cloud (Anthropic managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md#billing).

Fast mode for Claude Fable 5.2 is also available on [Claude Models on Google Cloud (Google managed)](../04-API-Reference/Guides/build-with-claude-claude-models-on-google-cloud-google-managed.md). Google Cloud sets its prices there. See [Cloud platform pricing](#cloud-platform-pricing).

Fast mode for Claude Fable 5.2 is also available on Claude in Microsoft Foundry for deployments hosted on Anthropic. See [Claude in Microsoft Foundry pricing](#claude-in-microsoft-foundry-pricing).

Fast mode is also available for Claude Mythos 5.2 on the Claude API. [Availability of fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md#feature-availability) lists every platform where Claude Mythos 5.2 has fast mode.

| Model                           | Input           | Output          |
|---------------------------------|-----------------|-----------------|
| Claude Fable 5.2                | \$16 USD / MTok | \$80 USD / MTok |
| Claude Mythos 5.2               | \$16 USD / MTok | \$80 USD / MTok |
| Claude Opus 5.5                 | \$8 USD / MTok  | \$40 USD / MTok |
| Claude Opus 5 / Claude Opus 4.8 | \$10 USD / MTok | \$50 USD / MTok |

Fast mode pricing stacks with other pricing modifiers:

- [Prompt caching multipliers](#prompt-caching) apply on top of fast mode pricing.
- [Data residency](../04-API-Reference/Other/manage-claude-data-residency.md) multipliers apply on top of fast mode pricing.

Fast mode is not available with the [Batch API](#batch-processing).

For more information, see [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md).

### Batch processing

The Batch API allows asynchronous processing of large volumes of requests with a 50 percent discount on both input and output tokens.

[TABLE]

For more information about batch processing, see [Batch processing](../04-API-Reference/Guides/build-with-claude-batch-processing.md).

### Long context pricing

Claude 4.6 and later models (except Claude Haiku 5.5) and [Claude Mythos Preview](../22-Safety-Policy/glasswing.md) include the full [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) at standard pricing. (A 900k-token request is billed at the same per-token rate as a 9k-token request.) Prompt caching and batch processing discounts apply at standard rates across the full context window.

Claude Haiku 5.5 is priced by prompt length: a request whose prompt is over 100,000 tokens pays higher prices. A request’s prompt length counts all of its input tokens, including cache reads and cache writes. Each request is priced on its own: a request over the threshold pays the higher prices even when part of its prompt is a cache hit, and earlier requests keep the prices they were billed at. The [model pricing](#model-pricing) and [batch processing pricing](#batch-processing) sections list both sets of prices.

### Tool use pricing

Tool use requests are priced based on:

1.  The total number of input tokens sent to the model (including in the `tools` parameter).
2.  The number of output tokens generated.
3.  For server-side tools, additional usage-based pricing (for example, web search charges per search performed).

Client-side tools are priced the same as any other Claude API request, although server-side tools can incur additional charges based on their specific usage.

The additional tokens from tool use come from:

- The `tools` parameter in API requests (tool names, descriptions, and schemas)
- `tool_use` content blocks in API requests and responses
- `tool_result` content blocks in API requests

When you use `tools`, the API also automatically includes a special system prompt for the model that enables tool use. The following table lists the number of tool use tokens that each model requires (excluding the additional tokens listed earlier). The table assumes that you provide at least one tool. If you provide no `tools`, a tool choice of `none` uses 0 additional system prompt tokens.

[TABLE]

These token counts are added to your normal input and output tokens to calculate the total cost of a request.

For current per-model prices, refer to the [model pricing](#model-pricing) section.

For more information about tool use implementation and best practices, see [Tool use with Claude](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md).

### Specific tool pricing

#### Bash tool

The bash tool definition adds the following input tokens to your request. This is in addition to the per-model [tool use system prompt](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md#pricing) that applies whenever any tool is present.

| Model | Additional input tokens |
|----|----|
| Claude 4.7 and later models and Claude Mythos Preview | 325 tokens |
| Claude 4.6 and earlier models | 244 tokens |

Additional tokens are consumed by:

- Command outputs (stdout/stderr)
- Error messages
- Large file contents

See [tool use pricing](#tool-use-pricing) for complete pricing details.

#### Code execution tool

**Code execution is free when used with web search or web fetch.** When `web_search_20260209` (or later) or `web_fetch_20260209` (or later) is included in your API request, there are no additional charges for code execution tool calls beyond the standard input and output token costs.

When used without these tools, code execution is billed by execution time, tracked separately from token usage:

- Execution time has a minimum of 5 minutes.
- Each organization receives **1,550 free hours** of usage per month.
- Additional usage beyond 1,550 hours is billed at **\$0.05 USD per hour, per container**.
- If files are included in the request, execution time is billed even if the tool is not called, because files are preloaded onto the container.

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

The text editor tool uses the same pricing structure as other tools used with Claude. It follows the standard input and output token pricing based on the Claude model you’re using.

In addition to the base tokens, the following additional input tokens are needed for the text editor tool:

| Tool | Additional input tokens |
|----|----|
| `text_editor_20250728` (Claude 4.7 and later models and Claude Mythos Preview) | 974 tokens |
| `text_editor_20250728` (Claude 4.6 and earlier models) | 745 tokens |

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

Web search is available on the Claude API for **\$10 USD per 1,000 searches**, plus standard token costs for search-generated content. Web search results retrieved throughout a conversation are counted as input tokens, in search iterations run during a single turn and in subsequent conversation turns.

Each web search counts as one use, regardless of the number of results returned. A web search that fails with an error is not billed.

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

- Average webpage (10 kB): ~2,500 tokens
- Large documentation page (100 kB): ~25,000 tokens
- Research paper PDF (500 kB): ~125,000 tokens

#### Computer use tool

Computer use follows the standard [tool use pricing in the tool use overview](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md#pricing). When using the computer use tool:

**Toolset definition overhead:** Declaring `computer_toolset_20260801` with its default members adds about 4,500 input tokens to a request: about 4,590 on Claude Sonnet 5 and about 4,520 on the other supported models. These tokens cover the member tool definitions and the tool use system prompt. Disabling `zoom` with `configs` removes about 410 of those tokens. The response `usage` reports the exact count for a request, and you can estimate it in advance with the [token counting endpoint](../04-API-Reference/Guides/build-with-claude-token-counting.md).

**Earlier tool versions:** The following figures apply to the `computer_20251124` and `computer_20250124` tool versions, not to `computer_toolset_20260801`:

- System prompt overhead: 466–499 tokens added to the system prompt
- Tool definition: about 735 input tokens for each tool definition (measured with `computer_20250124`)

**Additional token consumption:**

- Screenshot and zoom images returned in tool results, billed as image input (see [Resolution and token cost](../04-API-Reference/Guides/build-with-claude-vision.md#evaluate-image-size))
- Tool execution results returned to Claude



If you’re also using bash or text editor tools alongside computer use, those tools have their own token costs as documented in their respective pages.

#### Browser use tool

Browser use follows the standard [tool use pricing in the tool use overview](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-overview.md#pricing). When using the browser use tool:

**Toolset definition overhead:** Declaring `browser_toolset_20260801` with its default members adds about 6,600 input tokens to a request: about 6,670 on Claude Sonnet 5 and about 6,610 on the other supported models. These tokens cover the member tool definitions and the tool use system prompt. Enabling all four optional members adds about 880 tokens, and disabling members with `configs` reduces the count. The response `usage` reports the exact count for a request, and you can estimate it in advance with the [token counting endpoint](../04-API-Reference/Guides/build-with-claude-token-counting.md).

**Additional token consumption:**

- Screenshot and zoom images returned in tool results, billed as image input (see [Resolution and token cost](../04-API-Reference/Guides/build-with-claude-vision.md#evaluate-image-size))
- Text tool results returned to Claude, such as accessibility trees, page text, and console or network entries



If you also use the computer use tool, bash tool, text editor tool, or your own tools alongside browser use, those tools have their own token costs as documented on their respective pages.

## Claude Managed Agents pricing

[Claude Managed Agents](../04-API-Reference/Other/managed-agents-overview.md) is billed on two dimensions: tokens and session runtime.

For pricing of [self-hosted Claude Managed Agents](../04-API-Reference/Other/managed-agents-self-hosted.md), contact your Anthropic account team.

### Tokens

All tokens consumed by a Claude Managed Agents session are billed at the rates shown in [Model pricing](#model-pricing). [Prompt caching multipliers](#prompt-caching) apply identically. Web search triggered inside a session incurs the standard \$10 USD per 1,000 searches. On Claude Platform on AWS, session token and runtime charges convert to Claude Consumption Units at the standard rate (see [Claude Platform on AWS pricing](#claude-platform-on-aws-pricing)). [Fast mode premium pricing](#fast-mode-pricing) applies when an agent’s `model.speed` is set to `"fast"`.

The [data residency multiplier](#data-residency-pricing) also applies: when an agent’s `model.inference_geo` is pinned to `"us"`, tokens consumed by sessions running that agent are billed at 1.1x the standard rates, the same multiplier that applies to US-only inference on the Messages API.

The following Messages API modifiers do **not** apply to Claude Managed Agents sessions:

| Modifier | Why it doesn’t apply |
|----|----|
| [Batch API discount](#batch-processing) | Sessions are stateful and interactive. There is no batch mode. |
| [Cloud platform pricing](#cloud-platform-pricing) | Not available on partner-operated cloud platforms. |

### Session runtime

| SKU             | Rate                        | Metering                  |
|-----------------|-----------------------------|---------------------------|
| Session runtime | \$0.08 USD per session-hour | `running` status duration |

Runtime is measured to the millisecond and accrues only while the session’s status is `running`. Time spent `idle` (waiting for your next message or a tool confirmation), `rescheduling`, or `terminated` does not count toward runtime.



Session runtime replaces the [code execution](#code-execution-tool) container-hour billing model when using Claude Managed Agents. You are not separately billed for container hours on top of session runtime.

### Worked example

A 1-hour coding session using Claude Opus 5.5 that consumes 50,000 input tokens and 15,000 output tokens:

| Line item       | Calculation               | Cost           |
|-----------------|---------------------------|----------------|
| Input tokens    | 50,000 × \$4 / 1,000,000  | \$0.20 USD     |
| Output tokens   | 15,000 × \$20 / 1,000,000 | \$0.30 USD     |
| Session runtime | 1.0 hour × \$0.08         | \$0.08 USD     |
| **Total**       |                           | **\$0.58 USD** |

If prompt caching is active and 40,000 of the input tokens are cache reads:

| Line item             | Calculation                     | Cost            |
|-----------------------|---------------------------------|-----------------|
| Uncached input tokens | 10,000 × \$4 / 1,000,000        | \$0.04 USD      |
| Cache read tokens     | 40,000 × \$4 × 0.05 / 1,000,000 | \$0.008 USD     |
| Output tokens         | 15,000 × \$20 / 1,000,000       | \$0.30 USD      |
| Session runtime       | 1.0 hour × \$0.08               | \$0.08 USD      |
| **Total**             |                                 | **\$0.428 USD** |

## Additional pricing considerations

### Cost optimization strategies

When building agents with Claude:

1.  **Use appropriate models:** Choose Haiku for simple tasks, Sonnet for most production workloads, and Opus for the most complex reasoning.
2.  **Implement prompt caching:** Reduce costs for repeated context.
3.  **Batch operations:** Use the Batch API for non-time-sensitive tasks.
4.  **Monitor usage patterns:** Track token consumption to identify optimization opportunities.



For high-volume agent applications, contact the [enterprise sales team](https://claude.com/contact-sales) for custom pricing arrangements.

### Rate limits

Rate limits vary by usage tier and affect how many requests you can make:

- **Start tier:** Entry-level limits for getting started
- **Build tier:** Increased limits for growing applications
- **Scale tier:** Highest standard limits for production workloads

For detailed rate limit information, see [Rate limits](../04-API-Reference/Endpoints/rate-limits.md).

For limits beyond the Scale tier or custom pricing arrangements, [contact the sales team](https://claude.com/contact-sales).

### Volume discounts

Volume discounts might be available for high-volume users. These are negotiated on a case-by-case basis.

- Standard usage tiers use the pricing shown in [Model pricing](#model-pricing).
- Enterprise customers can [email sales](mailto:sales@anthropic.com) for custom pricing.
- Academic and research discounts might be available.

### Enterprise pricing

For enterprise customers with specific needs:

- Custom rate limits
- Volume discounts
- Dedicated support
- Custom terms

To discuss enterprise pricing options, email <sales@anthropic.com> or [contact sales from the Claude Console](../04-API-Reference/Other/playground.md).

## Billing and payment

- Billing is based on actual monthly usage.
- All payments are in USD.
- Credit card and invoicing options are available.
- Usage tracking is available in the [Claude Console](../04-API-Reference/Other/playground.md).

## Frequently asked questions

### How is token usage calculated?

Tokens are pieces of text that models process. How many tokens the same text produces depends on the model’s tokenizer, the language, and the type of content. Claude 4.7 and later models and Claude Mythos Preview (`claude-mythos-preview`) use a newer tokenizer that produces approximately 30 percent more tokens for the same text than earlier models. To see how many tokens a request uses on a specific model, count it with [Token counting](../04-API-Reference/Guides/build-with-claude-token-counting.md) and that model’s ID.

### Are there free tiers or trials?

New users receive free credits to test the API. [Email sales](mailto:sales@anthropic.com) for information about extended trials for enterprise evaluation.

### How do discounts stack?

Batch API and prompt caching discounts can be combined. For example, using both features together provides significant cost savings compared to standard API calls. See [prompt caching pricing](#prompt-caching) for how the multipliers interact.

### What payment methods are accepted?

Major credit cards are accepted for standard accounts. To buy credits or manage your payment methods, go to the [Billing](../04-API-Reference/Other/playground.md) page (`platform.claude.com/settings/billing`) in the Claude Console. Enterprise customers can arrange invoicing and other payment methods.

For additional questions about pricing, contact <support@anthropic.com>.
