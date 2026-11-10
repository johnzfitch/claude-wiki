---
title: "Fast mode - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/fast-mode"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-05T06:36:02Z"
tags: ["api"]
---

# Fast mode

Copy page



Get up to 2.5x higher output tokens per second from supported Claude models.

Copy page



Fast mode

[APIs](#feature-availability)  
Messages APIAvailableManaged AgentsAvailable

[Cloud platforms](#availability-feature-support)  
Claude APIAvailableClaude Models on Google CloudAnthropic managedAvailableMicrosoft FoundryHosted on AzureAvailable

[Beta header](#feature-beta-headers)  
Varies; see details

[Data handling](#feature-data-handling)  
ZDR eligibleHIPAA eligible

Usage differs by product

Messages API

Set `speed: "fast"` on the request.

Managed Agents

Set `speed` on the agent’s model object, for example `{"id": "claude-opus-5-5", "speed": "fast"}`.

Fast mode delivers up to 2.5x higher output tokens per second at premium pricing. Set `speed: "fast"` on your request to opt in. Fast mode is available on Claude Opus 5.5 and in research preview on Claude Opus 5 and Claude Opus 4.8.

## How fast mode works

Fast mode runs the same model with a faster inference configuration. There is no change to intelligence or capabilities.

- Up to 2.5x higher output tokens per second compared to standard speed
- Speed benefits are focused on output tokens per second (OTPS), not time to first token (TTFT)
- Compatible with [streaming](build-with-claude-streaming.md), where the OTPS gain is most visible

## Basic usage

Fast mode works only on supported models. See [Availability](#feature-availability) for details, including which models need a beta header.

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

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    speed="fast",
    messages=[
        {"role": "user", "content": "Refactor this module to use dependency injection"}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

## Rate limits

Fast mode has a dedicated rate limit that is separate from standard Opus rate limits. When your fast mode rate limit is exceeded, the API returns a `429` error with a `retry-after` header indicating when capacity will be available.

Claude Opus 5.5 has a default fast mode rate limit in the Start, Build, and Scale [usage tiers](../Endpoints/rate-limits.md), so you don’t need to request access to use fast mode with it. Organizations in the Evaluation tier can use fast mode with Claude Opus 5.5 once they move to the Start, Build, or Scale tier.

The response includes headers that indicate your fast mode rate limit status:

| Header | Description |
|:---|:---|
| `anthropic-fast-input-tokens-limit` | Maximum fast mode input tokens per minute |
| `anthropic-fast-input-tokens-remaining` | Remaining fast mode input tokens |
| `anthropic-fast-input-tokens-reset` | Time when the fast mode input token limit resets |
| `anthropic-fast-output-tokens-limit` | Maximum fast mode output tokens per minute |
| `anthropic-fast-output-tokens-remaining` | Remaining fast mode output tokens |
| `anthropic-fast-output-tokens-reset` | Time when the fast mode output token limit resets |

To see your fast mode rate limits, go to the [Rate limits](../Other/playground.md) page in the Claude Console.

## Checking which speed was used

The response `usage` object includes a `speed` field that indicates which speed was used, either `"fast"` or `"standard"`. Requesting `speed: "fast"` on a [model that doesn’t support fast mode](#availability-feature-support) returns an error, and so does exceeding fast mode’s rate limits or capacity (a `429` or `529`). When a request with `speed: "fast"` succeeds, `usage.speed` is `"fast"`. Claude Opus 4.6 is an exception: instead of returning an error, a request with `speed: "fast"` and the `fast-mode-2026-02-01` beta header succeeds, but runs at standard speed. This behavior is correctly reflected in `usage.speed`, which shows `"standard"` in this situation. On Claude Models on Google Cloud (Anthropic managed), a Claude Opus 4.6 request with `speed: "fast"` returns a `400` error even with the header.

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

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    speed="fast",
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.usage.speed)  # "fast" or "standard"
```

Output



```python
{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
// ...
  "usage": {
    "input_tokens": 8,
    "output_tokens": 12,
    "speed": "fast"
  }
}
```

To track fast mode usage and costs across your organization, see the [Usage and Cost Analytics API](../Other/manage-claude-usage-cost-analytics-api.md).

## Retries and fallbacks

### Automatic retries

The SDK automatically retries fast mode `429` errors up to 2 times by default (configurable with `max_retries`), waiting for the delay in the `retry-after` header before each retry. Because fast mode uses continuous token replenishment, the `retry-after` delay is typically short and requests succeed once capacity is available.

### Falling back to standard speed

If you’d prefer to fall back to standard speed rather than wait for fast mode capacity, catch the rate limit error and retry without `speed: "fast"`. Set `max_retries` to `0` on the initial fast request to skip automatic retries and fail immediately on rate limit errors.



Falling back from fast to standard speed results in a [prompt cache](build-with-claude-prompt-caching.md) miss. Requests at different speeds do not share cached prefixes.

Because setting `max_retries` to `0` also disables retries for other transient errors (overloaded, internal server errors), the following examples reissue the original request with default retries for those cases.

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


def create_message_with_fast_fallback(max_retries=0, max_attempts=3, **params):
    try:
        return client.with_options(max_retries=max_retries).messages.create(**params)
    except anthropic.RateLimitError:
        if params.get("speed") == "fast":
            del params["speed"]
            return create_message_with_fast_fallback(max_retries=max_retries, **params)
        raise
    except (
        anthropic.APIStatusError,
        anthropic.APIConnectionError,
    ) as error:
        if isinstance(error, anthropic.APIStatusError) and error.status_code < 500:
            raise
        if max_attempts > 1:
            return create_message_with_fast_fallback(
                max_retries=max_retries, max_attempts=max_attempts - 1, **params
            )
        raise


message = create_message_with_fast_fallback(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    speed="fast",
    max_retries=0,
)
```

## Considerations

- **Batch API:** Fast mode is not available with the [Batch API](build-with-claude-batch-processing.md).
- **Priority Tier:** Fast mode is not available with a [Priority Tier](../Endpoints/service-tiers.md) commitment.

## Pricing

Fast mode is priced at a multiplier on standard rates across the full context window, including requests over 200k input tokens.

| Model                           | Input           | Output          |
|:--------------------------------|:----------------|:----------------|
| Claude Opus 5.5                 | \$8 USD / MTok  | \$40 USD / MTok |
| Claude Opus 5 / Claude Opus 4.8 | \$10 USD / MTok | \$50 USD / MTok |

Fast mode pricing stacks with other pricing modifiers:

- [Prompt caching multipliers](../../17-Billing-Plans/about-claude-pricing.md#prompt-caching) apply on top of fast mode pricing.
- [Data residency](../Other/manage-claude-data-residency.md) multipliers apply on top of fast mode pricing.

For complete pricing details, see the [Pricing](../../17-Billing-Plans/about-claude-pricing.md#fast-mode-pricing) page.

## Availability

Fast mode is available or in research preview on select models and eligible for zero data retention and HIPAA readiness.

### API support

Fast mode is available only on the following models. If you were using fast mode on an earlier model, [migrate to a model that supports fast mode](../../20-Models/models-opus-5-5-migration-guide.md).

To access fast mode on Claude Opus 5, contact your account manager or [join the waitlist](https://claude.com/fast-mode).



Fast mode on Claude Opus 4.8 is deprecated and will be removed on November 30, 2026. After removal, requests to `claude-opus-4-8` with `speed: "fast"` will return an error. To continue using fast mode, migrate to Claude Opus 5.5. See [Migrating to Claude Opus 5.5 from Claude Opus 4.8](../../20-Models/models-opus-5-5-migration-guide.md#migrating-from-claude-opus-4-8).

[Messages API](build-with-claude-working-with-messages.md)

Usage

Set `speed: "fast"` on the request.

StatusAvailable

Cloud platforms

- Claude API
- [Claude Models on Google Cloud](build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)Anthropic managed
- [Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)Hosted on Azure

Models

- [Claude Opus 5.5](../../20-Models/models-opus-5-5-overview.md)

StatusResearch preview

Cloud platforms

- Claude API

Models

- [Claude Opus 5](../../20-Models/models-opus-5-overview.md)
- [Claude Opus 4.8](../../20-Models/models-opus-4-8-overview.md)

[Managed Agents](../Other/managed-agents-overview.md)

Usage

Set `speed` on the agent’s model object, for example `{"id": "claude-opus-5-5", "speed": "fast"}`.

StatusAvailable

Cloud platforms

- Claude API

Models

- [Claude Opus 5.5](../../20-Models/models-opus-5-5-overview.md)

StatusResearch preview

Cloud platforms

- Claude API

Models

- [Claude Opus 5](../../20-Models/models-opus-5-overview.md)
- [Claude Opus 4.8](../../20-Models/models-opus-4-8-overview.md)

### Required beta headers

[Beta headers overview](../Endpoints/beta-headers.md)

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

Header

- `fast-mode-2026-02-01`
  

Models

- [Claude Opus 5](../../20-Models/models-opus-5-overview.md)
- [Claude Opus 4.8](../../20-Models/models-opus-4-8-overview.md)

### Data handling

[Data handling overview](../Other/manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/messages` with `speed: "fast"`

Zero data retentionEligible

Excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

Same Messages API endpoint with faster inference. ZDR applies regardless of speed setting.

HIPAAEligible

## Next steps



[Structured outputs](build-with-claude-structured-outputs.md)

Get validated JSON results from agent workflows.

[Pricing](../../17-Billing-Plans/about-claude-pricing.md#fast-mode-pricing)

Learn about Anthropic’s pricing structure for models and features.



[Effort](build-with-claude-effort.md)

Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency.



[Streaming messages](build-with-claude-streaming.md)

Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.
