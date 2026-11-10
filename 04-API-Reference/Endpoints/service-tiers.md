---
title: "Service tiers - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/service-tiers"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:36:20Z"
tags: ["api"]
---

# Service tiers

Copy page



Different tiers of service allow you to balance availability, performance, and predictable costs based on your application’s needs.

Copy page



Service tiers

Feature of  
[Messages API](../Guides/build-with-claude-working-with-messages.md)

[Status](#availability-feature-support)  
Legacy

[APIs](#feature-availability)  
Messages APIAvailableManaged AgentsNot available

[Cloud platforms](#availability-feature-support)  
Claude APIAvailable

Service tiers are legacy



Priority Tier capacity commitments are no longer available for purchase. Organizations with an existing commitment can continue to use Priority Tier through their contract end date, and this page remains available as a reference for them. If you need guaranteed capacity, [contact sales](https://claude.com/contact-sales).

Anthropic offers three service tiers:

- **Priority Tier:** Available only to organizations with an existing capacity commitment
- **Standard:** Default tier for both piloting and scaling everyday use cases
- **Batch:** Best for asynchronous workflows that can wait or benefit from being outside your normal capacity

## Standard tier

The standard tier is the default service tier for all API requests. The API prioritizes these requests alongside all other requests with best-effort availability.

## Priority Tier

The API prioritizes requests in this tier over all other requests. This prioritization helps minimize [“server overloaded” errors](errors.md#http-errors), even during peak times.

For more information, see [Existing Priority Tier commitments](#existing-priority-tier-commitments).

## How requests get assigned tiers

When handling a request, Anthropic decides to assign a request to Priority Tier in the following scenarios:

- Your organization has sufficient Priority Tier capacity **input** tokens per minute
- Your organization has sufficient Priority Tier capacity **output** tokens per minute

Anthropic counts usage against Priority Tier capacity as follows:

**Input tokens**

- Cache reads as 0.1 tokens per token read from the cache
- Cache writes as 1.25 tokens per token written to the cache with a 5-minute TTL
- Cache writes as 2.00 tokens per token written to the cache with a 1-hour TTL
- For [US-only inference](../Other/manage-claude-data-residency.md) (`inference_geo: "us"`) requests on Claude 4.6 and later models, input tokens are 1.1 tokens per token
- All other input tokens are 1 token per token

**Output tokens**

- For [US-only inference](../Other/manage-claude-data-residency.md) (`inference_geo: "us"`) requests on Claude 4.6 and later models, output tokens are 1.1 tokens per token
- All other output tokens are 1 token per token

Otherwise, requests proceed at standard tier.



These burndown rates reflect the relative pricing of each token type. For example, US-only inference is priced at 1.1x on Claude 4.6 and later models, so each token consumed with `inference_geo: "us"` draws down 1.1 tokens from your Priority Tier capacity.



Requests assigned Priority Tier pull from both the Priority Tier capacity and the regular rate limits. If servicing the request would exceed the rate limits, the request is declined.

## Using service tiers

You can control which service tiers can be used for a request by setting the `service_tier` parameter:

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
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude!"}],
    service_tier="auto",  # Automatically use Priority Tier when available, fall back to standard
)
print(message.usage.service_tier)
```

The `service_tier` parameter accepts the following values:

- `"auto"` (default) - Uses the Priority Tier capacity if available, falling back to your other capacity if not
- `"standard_only"` - Uses only standard tier capacity, useful if you don’t want to use your Priority Tier capacity

The response `usage` object also includes the service tier assigned to the request:

```python
{
  "usage": {
    "input_tokens": 410,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "output_tokens": 585,
    "service_tier": "priority"
  }
}
```



This allows you to determine which service tier was assigned to the request.

When requesting `service_tier="auto"` with a model with a Priority Tier commitment, these response headers provide insights:

``` block
anthropic-priority-input-tokens-limit: 10000
anthropic-priority-input-tokens-remaining: 9618
anthropic-priority-input-tokens-reset: 2025-01-12T23:11:59Z
anthropic-priority-output-tokens-limit: 10000
anthropic-priority-output-tokens-remaining: 6000
anthropic-priority-output-tokens-reset: 2025-01-12T23:12:21Z
```



You can use the presence of these headers to detect if your request was eligible for Priority Tier, even if it was over the limit.

## Existing Priority Tier commitments

A Priority Tier commitment consists of:

- A number of input tokens per minute
- A number of output tokens per minute
- A commitment duration (1, 3, 6, or 12 months)
- A specific model version

Priority Tier targets 99.5 percent uptime with prioritized computational resources. Requests beyond your committed capacity automatically fall back to standard tier.

### Supported models

Priority Tier is supported on all available Claude models except Claude Fable 5.1, Claude Haiku 5.5, Claude Mythos 5.1, Claude Mythos 5, [Claude Mythos Preview](../../22-Safety-Policy/glasswing.md), Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, and Claude Sonnet 5.

Check the [Models overview](../../20-Models/about-claude-models-overview.md) for more details on available models.

## Availability

Service tiers are available on every model.

### API support

[Messages API](../Guides/build-with-claude-working-with-messages.md)

Usage

Needs a Priority Tier commitment, which is no longer sold. With one, requests use Priority Tier by default; set `service_tier` to `"standard_only"` to use only standard capacity.

StatusAvailable

Cloud platforms

- Claude API

[Managed Agents](../Other/managed-agents-overview.md)

StatusNot available
