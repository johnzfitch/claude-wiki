---
title: "Fast mode - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/fast-mode"
category: "04-API-Reference/Guides"
fetched_at: "2026-10-20T06:37:43Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Ffast-mode)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](build-with-claude-overview.md)[Using the Messages API](build-with-claude-working-with-messages.md)[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)[Refusals and fallback](build-with-claude-refusals-and-fallback.md)[Fallback credit](build-with-claude-fallback-credit.md)

Model capabilities

[Effort](build-with-claude-effort.md)[Task budgets (beta)](build-with-claude-task-budgets.md)[Fast mode](build-with-claude-fast-mode.md)[Structured outputs](build-with-claude-structured-outputs.md)[Citations](build-with-claude-citations.md)[Streaming Messages](build-with-claude-streaming.md)[Batch processing](build-with-claude-batch-processing.md)[Search results](build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](build-with-claude-multilingual-support.md)[Embeddings](build-with-claude-embeddings.md)

[Thinking](build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Browser and computer use (SDK)](../Agents-Tools/agents-and-tools-tool-use-browser-use-sdk.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

[Compaction](build-with-claude-compaction.md)

Working with files

[Files API](build-with-claude-files.md)[PDF support](build-with-claude-pdf-support.md)

[Images and vision](build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)[Google Cloud](build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/playground.md)

[Messages](../../01-Getting-Started/intro.md)Model capabilities

Fast mode

[ZDR](../Other/manage-claude-api-and-data-retention.md)

Eligible

excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

# Fast mode

Copy page



Get up to 2.5x higher output tokens per second from supported Claude models.

Copy page



Fast mode delivers up to 2.5x higher output tokens per second at premium pricing. Set `speed: "fast"` on your request to opt in. Fast mode is available on Claude Opus 5.5 and in research preview on Claude Opus 5 and Claude Opus 4.8.

## How fast mode works

Fast mode runs the same model with a faster inference configuration. There is no change to intelligence or capabilities.

- Up to 2.5x higher output tokens per second compared to standard speed
- Speed benefits are focused on output tokens per second (OTPS), not time to first token (TTFT)
- Compatible with [streaming](build-with-claude-streaming.md), where the OTPS gain is most visible

## Basic usage

Fast mode works only on supported models. See [Model availability](#supported-models) for details, including which models need a beta header.

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

## Supported platforms

Fast mode is available on the Claude API, including [Claude Managed Agents](../Other/managed-agents-overview.md).

Fast mode on Claude Opus 5.5 is also available on [Claude in Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md) for deployments hosted on Azure. It is not available for deployments [hosted on Anthropic](build-with-claude-claude-in-microsoft-foundry.md#hosting-options).

## Model availability

Fast mode is available only on the following models. If you were using fast mode on an earlier model, [migrate to a model that supports fast mode](../../20-Models/models-opus-5-5-migration-guide.md).

### Claude Opus 5.5

Fast mode is available on Claude Opus 5.5. It doesn't need a beta header or an access request.

### Claude Opus 5 and Claude Opus 4.8

Fast mode on Claude Opus 5 and Claude Opus 4.8 is in research preview. Requests that set `speed` must send the `fast-mode-2026-02-01` [beta header](../Endpoints/beta-headers.md); without it, they return a `400` error. To access fast mode on Claude Opus 5 or Claude Opus 4.8, contact your account manager or [join the waitlist](https://claude.com/fast-mode).

## Pricing

Fast mode is priced at a multiplier on standard rates across the full context window, including requests over 200k input tokens.

| Model                           | Input           | Output          |
|:--------------------------------|:----------------|:----------------|
| Claude Opus 5.5                 | \$8 USD / MTok  | \$40 USD / MTok |
| Claude Opus 5 / Claude Opus 4.8 | \$10 USD / MTok | \$50 USD / MTok |

Fast mode pricing stacks with other pricing modifiers:

- [Prompt caching multipliers](../../17-Billing-Plans/about-claude-pricing.md#prompt-caching) apply on top of fast mode pricing
- [Data residency](../Other/manage-claude-data-residency.md) multipliers apply on top of fast mode pricing

For complete pricing details, see the [Pricing](../../17-Billing-Plans/about-claude-pricing.md#fast-mode-pricing) page.

## Rate limits

Fast mode has a dedicated rate limit that is separate from standard Opus rate limits. When your fast mode rate limit is exceeded, the API returns a `429` error with a `retry-after` header indicating when capacity will be available.

Claude Opus 5.5 has a default fast mode rate limit in the Start, Build, and Scale [usage tiers](../Endpoints/rate-limits.md), so you don't need to request access to use fast mode with it. Organizations in the Evaluation tier can use fast mode with Claude Opus 5.5 once they move to the Start, Build, or Scale tier.

The response includes headers that indicate your fast mode rate limit status:

| Header                                   | Description                                       |
|:-----------------------------------------|:--------------------------------------------------|
| `anthropic-fast-input-tokens-limit`      | Maximum fast mode input tokens per minute         |
| `anthropic-fast-input-tokens-remaining`  | Remaining fast mode input tokens                  |
| `anthropic-fast-input-tokens-reset`      | Time when the fast mode input token limit resets  |
| `anthropic-fast-output-tokens-limit`     | Maximum fast mode output tokens per minute        |
| `anthropic-fast-output-tokens-remaining` | Remaining fast mode output tokens                 |
| `anthropic-fast-output-tokens-reset`     | Time when the fast mode output token limit resets |

To see your fast mode rate limits, go to the [Rate limits](../Other/playground.md) page in the Claude Console.

## Checking which speed was used

The response `usage` object includes a `speed` field that indicates which speed was used, either `"fast"` or `"standard"`. Requesting `speed: "fast"` on a [model that doesn't support fast mode](#supported-models) returns an error, and so does exceeding fast mode's rate limits or capacity (a `429` or `529`). When a request with `speed: "fast"` succeeds, `usage.speed` is `"fast"`. Claude Opus 4.6 is an exception: instead of returning an error, a request with `speed: "fast"` and the `fast-mode-2026-02-01` beta header succeeds, but runs at standard speed. This behavior is correctly reflected in `usage.speed`, which shows `"standard"` in this situation.

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

To track fast mode usage and costs across your organization, see the [Usage and Cost API](../Other/manage-claude-usage-cost-api.md).

## Retries and fallbacks

### Automatic retries

The SDK automatically retries fast mode `429` errors up to 2 times by default (configurable with `max_retries`), waiting for the delay in the `retry-after` header before each retry. Because fast mode uses continuous token replenishment, the `retry-after` delay is typically short and requests succeed once capacity is available.

### Falling back to standard speed

If you'd prefer to fall back to standard speed rather than wait for fast mode capacity, catch the rate limit error and retry without `speed: "fast"`. Set `max_retries` to `0` on the initial fast request to skip automatic retries and fail immediately on rate limit errors.



Falling back from fast to standard speed will result in a [prompt cache](build-with-claude-prompt-caching.md) miss. Requests at different speeds do not share cached prefixes.

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

## Next steps



[Structured outputs](build-with-claude-structured-outputs.md)

Get validated JSON results from agent workflows.

[Pricing](../../17-Billing-Plans/about-claude-pricing.md#fast-mode-pricing)

Learn about Anthropic's pricing structure for models and features.



[Effort](build-with-claude-effort.md)

Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency.



[Streaming messages](build-with-claude-streaming.md)

Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.

## Compatibility

Supported models  
- Opus 4.8, 5, and 5.5

Supported platforms  
- Claude API^([1](#compat-fn-1))
- Microsoft Foundry^([2](#compat-fn-2))

1.  Includes [Claude Managed Agents](../Other/managed-agents-overview.md). [↩](#compat-fnref-1)
2.  Available for Claude Opus 5.5 on deployments hosted on Azure, not on deployments [hosted on Anthropic](build-with-claude-claude-in-microsoft-foundry.md#hosting-options). [↩](#compat-fnref-2)

- Fast mode on Claude Opus 5 and Claude Opus 4.8 is in research preview and needs the `fast-mode-2026-02-01` beta header.
