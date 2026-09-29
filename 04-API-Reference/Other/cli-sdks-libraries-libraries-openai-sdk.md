---
title: "OpenAI SDK compatibility - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/cli-sdks-libraries/libraries/openai-sdk"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:30Z"
tags: ["api", "sdk"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fcli-sdks-libraries%2Flibraries%2Fopenai-sdk)





SearchCtrlK

CLI, SDKs, and libraries

[Overview](cli-sdks-libraries-overview.md)

ant CLI

[Quickstart](cli-sdks-libraries-cli-quickstart.md)[Authentication options](cli-sdks-libraries-cli-authentication.md)[Using the CLI](cli-sdks-libraries-cli-using.md)[Scripting and automation](cli-sdks-libraries-cli-scripting.md)[Manage resources as code](cli-sdks-libraries-cli-apply.md)[Connect to a Managed Agents session](cli-sdks-libraries-cli-sessions-connect.md)

Client SDKs

[Middleware](cli-sdks-libraries-middleware.md)[Python](cli-sdks-libraries-sdks-python.md)[TypeScript](cli-sdks-libraries-sdks-typescript.md)[C#](cli-sdks-libraries-sdks-csharp.md)[Go](cli-sdks-libraries-sdks-go.md)[Java](cli-sdks-libraries-sdks-java.md)[PHP](cli-sdks-libraries-sdks-php.md)[Ruby](cli-sdks-libraries-sdks-ruby.md)

Libraries and integrations

[Apple Foundation Models](cli-sdks-libraries-libraries-apple-foundation-models.md)[OpenAI SDK compatibility](cli-sdks-libraries-libraries-openai-sdk.md)

[Console](usage-limits.md)

[CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)Libraries and integrations

# OpenAI SDK compatibility

Copy page



Anthropic provides a compatibility layer that enables you to use the OpenAI SDK to test the Claude API. With a few code changes, you can quickly evaluate Anthropic model capabilities.

Copy page





This compatibility layer is primarily intended to test and compare model capabilities, and is not considered a long-term or production-ready solution for most use cases. While it is intended to remain fully functional and not have breaking changes, the priority is the reliability and effectiveness of the [Claude API](../Endpoints/overview.md).

For more information on known compatibility limitations, see [Important OpenAI compatibility limitations](#important-openai-compatibility-limitations).

If you encounter any issues with the OpenAI SDK compatibility feature, please share your feedback via this [compatibility feedback form](https://forms.gle/oQV4McQNiuuNbz9n8).



For the best experience and access to Claude API full feature set ([PDF processing](../Guides/build-with-claude-pdf-support.md), [citations](../Guides/build-with-claude-citations.md), [thinking](../Guides/build-with-claude-thinking.md), and [prompt caching](../Guides/build-with-claude-prompt-caching.md)), use the native [Claude API](../Endpoints/overview.md).

## Getting started with the OpenAI SDK

To use the OpenAI SDK compatibility feature, you'll need to:

1.  Use an official OpenAI SDK
2.  Change the following
    - Update your base URL to point to the Claude API
    - Replace your API key with a [Claude API key](usage-limits.md)
    - If your key is a [personal or service account key](manage-claude-authentication.md#key-types) with access to multiple workspaces, also send the `anthropic-workspace-id` header on every request (for example, `default_headers` in the Python SDK or `defaultHeaders` in TypeScript); see [Select a workspace](manage-claude-authentication.md#select-a-workspace)
    - Update your model name to use a [Claude model](../../20-Models/about-claude-models-overview.md)
3.  Review the following sections for what features are supported

### Quick start example

Python

TypeScript

C#

Go

Java

PHP

Ruby

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

- The `strict` parameter for function calling is ignored, which means the tool use JSON is not guaranteed to follow the supplied schema. For guaranteed schema conformance, use the native [Claude API with Structured Outputs](../Guides/build-with-claude-structured-outputs.md).
- Audio input is not supported; it will be ignored and stripped from input
- Prompt caching is not supported, but it is supported in the [Anthropic SDKs](cli-sdks-libraries-overview.md)
- System/developer messages are hoisted and concatenated to the beginning of the conversation, as Anthropic only supports a single initial system message.

Most unsupported fields are silently ignored rather than producing errors. These are all documented in the following sections.

### Output quality considerations

If you’ve done lots of tweaking to your prompt, it’s likely to be well-tuned to OpenAI specifically. Consider reworking it for Claude using the [prompting best practices guide](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md).

### System / developer message hoisting

Most of the inputs to the OpenAI SDK clearly map directly to Anthropic’s API parameters, but one distinct difference is the handling of system / developer prompts. These two prompts can be put throughout a chat conversation via OpenAI. Since Anthropic only supports an initial system message, the API takes all system/developer messages and concatenates them together with a single newline (`\n`) in between them. This full string is then supplied as a single system message at the start of the messages.

### Thinking support

You can enable [thinking](../Guides/build-with-claude-thinking.md) by adding the `thinking` parameter. On current models thinking is adaptive, with Claude deciding when and how deeply to think, and on Claude 5 models it is on by default; manually configured extended thinking is a legacy mode. Although thinking improves Claude's reasoning for complex tasks, the OpenAI SDK doesn't return Claude's detailed thought process. For full thinking features, including access to Claude's step-by-step reasoning output, use the native Claude API.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Who are you?"}],
    extra_body={"thinking": {"type": "enabled", "budget_tokens": 2000}},
)
```

## Rate limits

Rate limits follow Anthropic's [standard limits](../Endpoints/rate-limits.md) for the `/v1/messages` endpoint.

## Detailed OpenAI compatible API support

### Request fields

#### Simple fields

| Field                   | Support status                                                                                                               |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
| `model`                 | Use Claude model names                                                                                                       |
| `max_tokens`            | Fully supported                                                                                                              |
| `max_completion_tokens` | Fully supported                                                                                                              |
| `stream`                | Fully supported                                                                                                              |
| `stream_options`        | Fully supported                                                                                                              |
| `top_p`                 | Fully supported                                                                                                              |
| `parallel_tool_calls`   | Fully supported                                                                                                              |
| `stop`                  | All non-whitespace stop sequences work                                                                                       |
| `temperature`           | Between 0 and 1 (inclusive). Values greater than 1 are capped at 1.                                                          |
| `n`                     | Must be exactly 1                                                                                                            |
| `logprobs`              | Ignored                                                                                                                      |
| `metadata`              | Ignored                                                                                                                      |
| `response_format`       | Ignored. For JSON output, use [Structured Outputs](../Guides/build-with-claude-structured-outputs.md) with the native Claude API |
| `prediction`            | Ignored                                                                                                                      |
| `presence_penalty`      | Ignored                                                                                                                      |
| `frequency_penalty`     | Ignored                                                                                                                      |
| `seed`                  | Ignored                                                                                                                      |
| `service_tier`          | Ignored                                                                                                                      |
| `audio`                 | Ignored                                                                                                                      |
| `logit_bias`            | Ignored                                                                                                                      |
| `store`                 | Ignored                                                                                                                      |
| `user`                  | Ignored                                                                                                                      |
| `modalities`            | Ignored                                                                                                                      |
| `top_logprobs`          | Ignored                                                                                                                      |
| `reasoning_effort`      | Ignored                                                                                                                      |

#### `tools` / `functions` fields

### Show fields

Tools

Functions

`tools[n].function` fields

| Field         | Support status                                                                                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `name`        | Fully supported                                                                                                                      |
| `description` | Fully supported                                                                                                                      |
| `parameters`  | Fully supported                                                                                                                      |
| `strict`      | Ignored. Use [Structured Outputs](../Guides/build-with-claude-structured-outputs.md) with native Claude API for strict schema validation |

#### `messages` array fields

### Show fields

Developer role

System role

User role

Assistant role

Tool role

Function role

Fields for `messages[n].role == "developer"`



Developer messages are hoisted to beginning of conversation as part of the initial system message

| Field     | Support status               |
|-----------|------------------------------|
| `content` | Fully supported, but hoisted |
| `name`    | Ignored                      |

### Response fields

| Field                             | Support status                 |
|-----------------------------------|--------------------------------|
| `id`                              | Fully supported                |
| `choices[]`                       | Will always have a length of 1 |
| `choices[].finish_reason`         | Fully supported                |
| `choices[].index`                 | Fully supported                |
| `choices[].message.role`          | Fully supported                |
| `choices[].message.content`       | Fully supported                |
| `choices[].message.tool_calls`    | Fully supported                |
| `object`                          | Fully supported                |
| `created`                         | Fully supported                |
| `model`                           | Fully supported                |
| `finish_reason`                   | Fully supported                |
| `content`                         | Fully supported                |
| `usage.completion_tokens`         | Fully supported                |
| `usage.prompt_tokens`             | Fully supported                |
| `usage.total_tokens`              | Fully supported                |
| `usage.completion_tokens_details` | Always empty                   |
| `usage.prompt_tokens_details`     | Always empty                   |
| `choices[].message.refusal`       | Always empty                   |
| `choices[].message.audio`         | Always empty                   |
| `logprobs`                        | Always empty                   |
| `service_tier`                    | Always empty                   |
| `system_fingerprint`              | Always empty                   |

### Error message compatibility

The compatibility layer maintains consistent error formats with the OpenAI API. However, the detailed error messages will not be equivalent. Only use the error messages for logging and debugging.

### Header compatibility

While the OpenAI SDK automatically manages headers, here is the complete list of headers supported by the Claude API for developers who need to work with them directly.

| Header                           | Support Status      |
|----------------------------------|---------------------|
| `x-ratelimit-limit-requests`     | Fully supported     |
| `x-ratelimit-limit-tokens`       | Fully supported     |
| `x-ratelimit-remaining-requests` | Fully supported     |
| `x-ratelimit-remaining-tokens`   | Fully supported     |
| `x-ratelimit-reset-requests`     | Fully supported     |
| `x-ratelimit-reset-tokens`       | Fully supported     |
| `retry-after`                    | Fully supported     |
| `request-id`                     | Fully supported     |
| `openai-version`                 | Always `2020-10-01` |
| `authorization`                  | Fully supported     |
| `openai-processing-ms`           | Always empty        |
