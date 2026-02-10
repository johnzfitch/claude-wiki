---
category: "04-API-Reference"
fetched_at: "2026-02-08T11:49:22Z"
source_url: "https://platform.claude.com/docs/en/build-with-claude/fast-mode"
title: "Fast mode (research preview) - Claude API Docs"
---

Capabilities

# Fast mode (research preview)

Copy page

Higher output speed for Claude Opus 4.6, delivering significantly faster token generation for latency-sensitive and agentic workflows.

Copy page

Fast mode provides significantly faster output token generation for Claude Opus 4.6. By setting `speed: "fast"` in your API request, you get up to 2.5x higher output tokens per second from the same model at premium pricing.

Fast mode is currently in research preview. [Join the waitlist](https://claude.com/fast-mode) to request access. Availability is limited while we gather feedback.

## 

Supported models

Fast mode is supported on the following models:

- Claude Opus 4.6 (`claude-opus-4-6`)

## 

How fast mode works

Fast mode runs the same model with a faster inference configuration. There is no change to intelligence or capabilities.

- Up to 2.5x higher output tokens per second compared to standard speed
- Speed benefits are focused on output tokens per second (OTPS), not time to first token (TTFT)
- Same model weights and behavior (not a different model)

## 

Basic usage

Shell

``` shiki
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: fast-mode-2026-02-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
        "max_tokens": 4096,
        "speed": "fast",
        "messages": [{
            "role": "user",
            "content": "Refactor this module to use dependency injection"
        }]
    }'
```

## 

Pricing

Fast mode is priced at 6x standard Opus rates for prompts \<= 200K tokens, and 12x standard Opus rates for prompts \> 200K tokens. The following table shows pricing for Claude Opus 4.6 with fast mode:

| Context window       | Input       | Output       |
|----------------------|-------------|--------------|
| ≤ 200K input tokens  | \$30 / MTok | \$150 / MTok |
| \> 200K input tokens | \$60 / MTok | \$225 / MTok |

Fast mode pricing stacks with other pricing modifiers:

- [Prompt caching multipliers](/docs/en/about-claude/pricing#model-pricing) apply on top of fast mode pricing
- [Data residency](/docs/en/build-with-claude/data-residency) multipliers apply on top of fast mode pricing

For complete pricing details, see the [pricing page](/docs/en/about-claude/pricing#fast-mode-pricing).

## 

Rate limits

Fast mode has a dedicated rate limit that is separate from standard Opus rate limits. Unlike standard speed, which has separate limits for ≤200K and \>200K input tokens, fast mode uses a single rate limit that covers the full context range. When your fast mode rate limit is exceeded, the API returns a `429` error with a `retry-after` header indicating when capacity will be available.

The response includes headers that indicate your fast mode rate limit status:

| Header | Description |
|----|----|
| `anthropic-fast-input-tokens-limit` | Maximum fast mode input tokens per minute |
| `anthropic-fast-input-tokens-remaining` | Remaining fast mode input tokens |
| `anthropic-fast-input-tokens-reset` | Time when the fast mode input token limit resets |
| `anthropic-fast-output-tokens-limit` | Maximum fast mode output tokens per minute |
| `anthropic-fast-output-tokens-remaining` | Remaining fast mode output tokens |
| `anthropic-fast-output-tokens-reset` | Time when the fast mode output token limit resets |

For tier-specific rate limits, see the [rate limits page](/docs/en/api/rate-limits).

## 

Checking which speed was used

The response `usage` object includes a `speed` field that indicates which speed was used, either `"fast"` or `"standard"`:

Shell

``` shiki
curl https://api.anthropic.com/v1/messages \
    --header "x-api-key: $ANTHROPIC_API_KEY" \
    --header "anthropic-version: 2023-06-01" \
    --header "anthropic-beta: fast-mode-2026-02-01" \
    --header "content-type: application/json" \
    --data '{
        "model": "claude-opus-4-6",
        "max_tokens": 1024,
        "speed": "fast",
        "messages": [{"role": "user", "content": "Hello"}]
    }'

{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  ...
  "usage": {
    "input_tokens": 523,
    "output_tokens": 1842,
    "speed": "fast"
  }
}
```

To track fast mode usage and costs across your organization, see the [Usage and Cost API](/docs/en/build-with-claude/usage-cost-api).

## 

Retries and fallback

### 

Automatic retries

When fast mode rate limits are exceeded, the API returns a `429` error with a `retry-after` header. The Anthropic SDKs automatically retry these requests up to 2 times by default (configurable via `max_retries`), waiting for the server-specified delay before each retry. Since fast mode uses continuous token replenishment, the `retry-after` delay is typically short and requests succeed once capacity is available.

### 

Falling back to standard speed

If you'd prefer to fall back to standard speed rather than wait for fast mode capacity, catch the rate limit error and retry without `speed: "fast"`. Set `max_retries` to `0` on the initial fast request to skip automatic retries and fail immediately on rate limit errors.

Falling back from fast to standard speed will result in a [prompt cache](/docs/en/build-with-claude/prompt-caching) miss. Requests at different speeds do not share cached prefixes.

Since setting `max_retries` to `0` also disables retries for other transient errors (overloaded, internal server errors), the examples below re-issue the original request with default retries for those cases.

Python

``` shiki
import anthropic

client = anthropic.Anthropic()

def create_message_with_fast_fallback(max_retries=None, max_attempts=3, **params):
    try:
        return client.beta.messages.create(**params, max_retries=max_retries)
    except anthropic.RateLimitError:
        if params.get("speed") == "fast":
            del params["speed"]
            return create_message_with_fast_fallback(**params)
        raise
    except (anthropic.InternalServerError, anthropic.OverloadedError, anthropic.APIConnectionError):
        if max_attempts > 1:
            return create_message_with_fast_fallback(max_attempts=max_attempts - 1, **params)
        raise

message = create_message_with_fast_fallback(
    model="claude-opus-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    betas=["fast-mode-2026-02-01"],
    speed="fast",
    max_retries=0,
)
```

## 

Considerations

- **Prompt caching**: Switching between fast and standard speed invalidates the prompt cache. Requests at different speeds do not share cached prefixes.
- **Supported models**: Fast mode is currently supported on Opus 4.6 only. Sending `speed: "fast"` with an unsupported model returns an error.
- **TTFT**: Fast mode's benefits are focused on output tokens per second (OTPS), not time to first token (TTFT).
- **Batch API**: Fast mode is not available with the [Batch API](/docs/en/build-with-claude/batch-processing).
- **Priority Tier**: Fast mode is not available with [Priority Tier](/docs/en/api/service-tiers).

## 

Next steps

[](/docs/en/about-claude/pricing#fast-mode-pricing)

Pricing

View detailed fast mode pricing information.

[](/docs/en/api/rate-limits)

Rate limits

Check rate limit tiers for fast mode.

[](/docs/en/build-with-claude/effort)

Effort parameter

Control token usage with the effort parameter.

Was this page helpful?

- 

- [Supported models](#supported-models)

- [How fast mode works](#how-fast-mode-works)

- [Basic usage](#basic-usage)

- [Pricing](#pricing)

- [Rate limits](#rate-limits)

- [Checking which speed was used](#checking-which-speed-was-used)

- [Retries and fallback](#retries-and-fallback)

- [Automatic retries](#automatic-retries)

- [Falling back to standard speed](#falling-back-to-standard-speed)

- [Considerations](#considerations)

- [Next steps](#next-steps)

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
