---
title: "OpenAI SDK compatibility - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk"
category: "04-API-Reference/Other"
fetched_at: "2026-11-05T06:36:56Z"
tags: ["api", "sdk"]
---

# OpenAI SDK compatibility

Copy page



Anthropic provides a compatibility layer that lets you use the OpenAI SDK to test the Claude API. With a few code changes, you can evaluate Anthropic model capabilities.

Copy page



OpenAI SDK compatibility

Feature of  
[Messages API](../Guides/build-with-claude-working-with-messages.md)

[Cloud platforms](#availability-feature-support)  
Claude APIAvailable



This compatibility layer is primarily intended to test and compare model capabilities, and is not considered a long-term or production-ready solution for most use cases. Although it is intended to remain fully functional and not have breaking changes, the priority is the reliability and effectiveness of the [Claude API](../Endpoints/overview.md).

For more information on known compatibility limitations, see [Important OpenAI compatibility limitations](#important-openai-compatibility-limitations).

If you encounter any issues with the OpenAI SDK compatibility feature, share your feedback through this [compatibility feedback form](https://forms.gle/oQV4McQNiuuNbz9n8).



For the best experience and access to the full Claude API feature set ([PDF processing](../Guides/build-with-claude-pdf-support.md), [citations](../Guides/build-with-claude-citations.md), [thinking](../Guides/build-with-claude-thinking.md), and [prompt caching](../Guides/build-with-claude-prompt-caching.md)), use the native [Claude API](../Endpoints/overview.md).

## Getting started with the OpenAI SDK

To use the OpenAI SDK compatibility feature, you need to:

1.  Use an official OpenAI SDK.
2.  Change the following:
    - Update your base URL to point to the Claude API.
    - Replace your API key with a [Claude API key](playground.md) from the Claude Console.
    - If your key is a [personal or service account key](manage-claude-authentication.md#key-types) that isn’t scoped to a workspace, also send the `anthropic-workspace-id` header on every request (for example, `default_headers` in the Python SDK or `defaultHeaders` in TypeScript); see [Select a workspace](manage-claude-authentication.md#select-a-workspace).
    - Update your model name to use a [Claude model](../../20-Models/about-claude-models-overview.md).
3.  Review the following sections for what features are supported.

### Quick start example

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
import os

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # Your Claude API key
    base_url="https://api.anthropic.com/v1/",  # the Claude API endpoint
)

response = client.chat.completions.create(
    model="claude-opus-5-5",  # Claude model name
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who are you?"},
    ],
)

print(response.choices[0].message.content)
```

## Important OpenAI compatibility limitations

### API behavior

Here are the most substantial differences from using OpenAI:

- The `strict` parameter for function calling is ignored, which means the tool use JSON is not guaranteed to follow the supplied schema. For guaranteed schema conformance, use the native [Claude API with structured outputs](../Guides/build-with-claude-structured-outputs.md).
- `response_format` accepts only `json_schema` with `strict: true`. A request that sets `json_object` or `text` returns a 400 error.
- Audio and file inputs are not supported. A request that includes an `input_audio` or `file` content part returns a 400 error.
- Prompt caching is not supported, but it is supported in the [Anthropic SDKs](cli-sdks-libraries-overview.md).
- System/developer messages are hoisted and concatenated into the top-level `system` field, wherever they appear in the conversation. To add system instructions partway through a conversation, use [mid-conversation system messages](../Guides/build-with-claude-mid-conversation-system-messages.md) in the native Claude API.
- Depending on the model, text generated for a request that sets `temperature` or `top_p` to a value other than the Claude API’s default might not carry the [text watermark](../Guides/build-with-claude-text-watermark.md#sampling-settings). If you rely on the watermark, omit both parameters.

Most unsupported fields are silently ignored rather than producing errors. These are all documented in the following sections.

### Output quality considerations

If you’ve adjusted your prompt extensively, it’s likely to be well-tuned to OpenAI specifically. Consider reworking it for Claude using the [prompting best practices](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md) guide.

### System / developer message hoisting

Most of the inputs to the OpenAI SDK clearly map directly to Claude API parameters, but one distinct difference is the handling of system / developer prompts. These two prompts can be put throughout a chat conversation in the OpenAI API. The compatibility layer takes all system/developer messages and concatenates them together with a single newline (`\n`) in between them. This full string is then supplied as the top-level `system` field, ahead of every message.

### Thinking support

On Claude 5 models and Claude Mythos Preview, [thinking](../Guides/build-with-claude-thinking.md) is on by default, so you can omit the `thinking` field. To use thinking on other models through the compatibility layer, set the `thinking` field of the request body to `{"type": "enabled", "budget_tokens": N}`. `N` must be at least 1,024 and less than `max_tokens` or `max_completion_tokens`, whichever you set.

The compatibility layer differs from the native Claude API in the following ways:

- The response doesn’t include Claude’s thinking. The native Claude API can return [summarized thinking](../Guides/build-with-claude-thinking.md#summarized-thinking).
- Setting `thinking` to `{"type": "adaptive"}` returns a 400 error.
- On [models that reject `enabled`](../Guides/build-with-claude-thinking-troubleshooting.md#rejected-configurations) in the native Claude API, the compatibility layer converts `enabled` to adaptive thinking. On those models, `budget_tokens` is required but has no effect.

The OpenAI SDK has no `thinking` parameter, so the following example sends it as an extra field in the request body.

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
response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Who are you?"}],
    extra_body={"thinking": {"type": "enabled", "budget_tokens": 2000}},
)
```

## Rate limits

Rate limits follow Anthropic’s [standard limits](../Endpoints/rate-limits.md) for the `/v1/messages` endpoint.

## Detailed OpenAI compatible API support

### Request fields

#### Simple fields

| Field | Support status |
|----|----|
| `model` | Use Claude model names |
| `max_tokens` | Fully supported |
| `max_completion_tokens` | Fully supported |
| `stream` | Fully supported |
| `stream_options` | Fully supported |
| `top_p` | Passed through to the model. Claude 4.7 and later models and Claude Mythos Preview return a 400 error for any value other than `0.99`, the default, so omit it. A request that sets both `temperature` and `top_p` also returns a 400 error. See [Using the Messages API](../Guides/build-with-claude-working-with-messages.md). |
| `parallel_tool_calls` | Fully supported |
| `tool_choice` | Supported with limits. `"required"` and a named function force a tool call. Claude Opus 5.5, Claude Sonnet 5.5, Claude Fable 5.1, and Claude Mythos 5.1 don’t support forced tool use and return a 400 error, so use `"auto"` on those models. See [Forcing tool use](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md#forcing-tool-use). |
| `stop` | All non-whitespace stop sequences work |
| `temperature` | Between 0 and 1 (inclusive). Values greater than 1 are capped at 1. On Claude 4.7 and later models and Claude Mythos Preview, any value below 1 returns a 400 error, so omit it. See [Using the Messages API](../Guides/build-with-claude-working-with-messages.md). |
| `n` | Must be exactly 1. Any other value returns a 400 error. |
| `response_format` | Supported with limits. Only `json_schema` with `strict: true` is accepted, and the structured outputs [JSON Schema limitations](../Guides/build-with-claude-structured-outputs.md#json-schema-limitations) apply. Any other value, including `json_object` and `text`, returns a 400 error. |
| `logprobs` | Ignored |
| `metadata` | Ignored |
| `prediction` | Ignored |
| `presence_penalty` | Ignored |
| `frequency_penalty` | Ignored |
| `seed` | Ignored |
| `service_tier` | Ignored |
| `audio` | Ignored |
| `logit_bias` | Ignored |
| `store` | Ignored |
| `user` | Ignored |
| `modalities` | Ignored |
| `top_logprobs` | Ignored |
| `reasoning_effort` | Ignored |

#### `tools` / `functions` fields

### Show fields

Tools

Functions

Tools

`tools[n].function` fields

| Field | Support status |
|----|----|
| `name` | Fully supported |
| `description` | Fully supported |
| `parameters` | Fully supported |
| `strict` | Ignored. Use [structured outputs](../Guides/build-with-claude-structured-outputs.md) with the native Claude API for strict schema validation. |

Functions

`functions[n]` fields



OpenAI has deprecated the `functions` field and recommends using `tools` instead.

| Field | Support status |
|----|----|
| `name` | Fully supported |
| `description` | Fully supported |
| `parameters` | Fully supported |
| `strict` | Ignored. Use [structured outputs](../Guides/build-with-claude-structured-outputs.md) with the native Claude API for strict schema validation. |

#### `messages` array fields

### Show fields

Developer role

System role

User role

Assistant role

Tool role

Function role

Developer role

Fields for `messages[n].role == "developer"`



Developer messages are hoisted to the beginning of the conversation as part of the initial system message.

| Field     | Support status               |
|-----------|------------------------------|
| `content` | Fully supported, but hoisted |
| `name`    | Ignored                      |

System role

Fields for `messages[n].role == "system"`



System messages are hoisted to the beginning of the conversation as part of the initial system message.

| Field     | Support status               |
|-----------|------------------------------|
| `content` | Fully supported, but hoisted |
| `name`    | Ignored                      |

User role

Fields for `messages[n].role == "user"`

| Field     | Variant                          | Sub-field | Support status      |
|-----------|----------------------------------|-----------|---------------------|
| `content` | `string`                         |           | Fully supported     |
|           | `array`, `type == "text"`        |           | Fully supported     |
|           | `array`, `type == "image_url"`   | `url`     | Fully supported     |
|           |                                  | `detail`  | Ignored             |
|           | `array`, `type == "input_audio"` |           | Returns a 400 error |
|           | `array`, `type == "file"`        |           | Returns a 400 error |
| `name`    |                                  |           | Ignored             |

Assistant role

Fields for `messages[n].role == "assistant"`

| Field           | Variant                      | Support status  |
|-----------------|------------------------------|-----------------|
| `content`       | `string`                     | Fully supported |
|                 | `array`, `type == "text"`    | Fully supported |
|                 | `array`, `type == "refusal"` | Ignored         |
| `tool_calls`    |                              | Fully supported |
| `function_call` |                              | Fully supported |
| `audio`         |                              | Ignored         |
| `refusal`       |                              | Ignored         |

Tool role

Fields for `messages[n].role == "tool"`

| Field          | Variant                   | Support status  |
|----------------|---------------------------|-----------------|
| `content`      | `string`                  | Fully supported |
|                | `array`, `type == "text"` | Fully supported |
| `tool_call_id` |                           | Fully supported |
| `name`         |                           | Ignored         |

Function role

Fields for `messages[n].role == "function"`

| Field     | Variant  | Support status                     |
|-----------|----------|------------------------------------|
| `content` | `string` | Fully supported                    |
| `name`    |          | Required, but the value is ignored |

### Response fields

| Field                             | Support status           |
|-----------------------------------|--------------------------|
| `id`                              | Fully supported          |
| `choices[]`                       | Always has a length of 1 |
| `choices[].finish_reason`         | Fully supported          |
| `choices[].index`                 | Fully supported          |
| `choices[].message.role`          | Fully supported          |
| `choices[].message.content`       | Fully supported          |
| `choices[].message.tool_calls`    | Fully supported          |
| `object`                          | Fully supported          |
| `created`                         | Fully supported          |
| `model`                           | Fully supported          |
| `usage.completion_tokens`         | Fully supported          |
| `usage.prompt_tokens`             | Fully supported          |
| `usage.total_tokens`              | Fully supported          |
| `usage.completion_tokens_details` | Always empty             |
| `usage.prompt_tokens_details`     | Always empty             |
| `choices[].message.refusal`       | Always empty             |
| `choices[].message.audio`         | Always empty             |
| `logprobs`                        | Always empty             |
| `service_tier`                    | Always empty             |
| `system_fingerprint`              | Always empty             |

### Error message compatibility

The compatibility layer maintains consistent error formats with the OpenAI API. However, the detailed error messages are not equivalent. Only use the error messages for logging and debugging.

### Header compatibility

If your code reads or sets headers directly, the following table shows how the Claude API handles OpenAI’s headers.

| Header | Support status |
|----|----|
| `x-ratelimit-limit-requests` | Not returned. The request limit is in `x-ratelimit-requests`. |
| `x-ratelimit-limit-tokens` | Not returned. The token limit is in `x-ratelimit-tokens`. |
| `x-ratelimit-remaining-requests` | Fully supported |
| `x-ratelimit-remaining-tokens` | Fully supported |
| `x-ratelimit-reset-requests` | Fully supported |
| `x-ratelimit-reset-tokens` | Fully supported |
| `retry-after` | Fully supported |
| `x-request-id` | Fully supported. Carries the Claude API [request ID](../Endpoints/errors.md#request-id) in place of the `request-id` header. |
| `openai-version` | Not returned |
| `openai-processing-ms` | Not returned |
| `authorization` | Fully supported |

## Availability

OpenAI SDK compatibility is available on every model.

### API support

StatusAvailable

Cloud platforms

- Claude API
