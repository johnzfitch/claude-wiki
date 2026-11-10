---
title: "Using the Messages API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/working-with-messages"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-05T06:36:11Z"
tags: ["api"]
---

# Using the Messages API

Copy page



Practical patterns and examples for using the Messages API effectively

Copy page



Messages API

[Cloud platforms](#availability-feature-support)  
All platforms

[Data handling](#feature-data-handling)  
ZDR eligibleHIPAA eligible

Anthropic offers two ways to build with Claude, each suited to different use cases:

|  | Messages API | Claude Managed Agents |
|----|----|----|
| **What it is** | Direct model prompting access | Pre-built, configurable agent harness that runs in managed infrastructure |
| **Best for** | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work |

This guide covers common patterns for working with the Messages API, including basic requests, multi-turn conversations, prefill techniques, and vision capabilities. For complete API specifications, see the [Messages API reference](../Endpoints/messages-create.md). For the managed agent harness instead, see the [Claude Managed Agents overview](../Other/managed-agents-overview.md).

## Basic request and response



The `temperature`, `top_p`, and `top_k` sampling parameters are not supported on Claude 4.7 and later models and Claude Mythos Preview, or on any model starting with [API version `2026-10-21`](../Endpoints/migration-2026-10-21.md#sampling-parameters). Setting them to a non-default value returns a 400 error, and starting with `2026-10-21` any value does. Omit them from request payloads and use prompting to guide the model’s behavior instead. See the [breaking changes in the migration guide](../../20-Models/models-opus-5-5-migration-guide.md#opus-46-breaking-changes).

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
message = anthropic.Anthropic().messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message)
```

Output



```python
{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Hello!"
    }
  ],
  "model": "claude-opus-5-5",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 12,
    "output_tokens": 6
  }
}
```

Refusal responses (`stop_reason: "refusal"`) also include a `stop_details` object identifying the policy category that triggered the refusal, on every model. See [Handling stop reasons](build-with-claude-refusals-and-fallback.md#refusal-response) for the field reference and example handling code.

## Multiple conversational turns

The Messages API is stateless, which means that you always send the full conversational history to the API. You can use this pattern to build up a conversation over time. Earlier conversational turns don’t necessarily need to actually originate from Claude. You can use synthetic `assistant` messages.

With [message threads](build-with-claude-message-threads.md), in beta, the API can keep the conversation, so that each later request sends only the new messages. A thread expires 5 minutes after its last request and is deleted no more than 1 hour after its last use.

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
message = anthropic.Anthropic().messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"},
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Can you describe LLMs to me?"},
    ],
)
print(message)
```

Output



```python
{
  "id": "msg_018gCsTGsXkYJVqYPxTgDHBU",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "Sure, I'd be happy to provide..."
    }
  ],
  "model": "claude-opus-5-5",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 30,
    "output_tokens": 309
  }
}
```

### System role in messages

On Claude Fable 5.1, [Claude Mythos 5.1](../../20-Models/models-mythos-5-1-overview.md), Claude Fable 5, [Claude Mythos 5](../../20-Models/models-mythos-5-overview.md), Claude Opus 5.5, Claude Opus 4.8, Claude Opus 5, Claude Sonnet 5.5, and Claude Haiku 5.5, you can include messages with `"role": "system"` after a user turn (subject to [placement rules](build-with-claude-mid-conversation-system-messages.md#limitations)) to add a new system instruction partway through a conversation. A `system` message that carries content cannot be the first entry in `messages`. Use the top-level `system` field for instructions that apply from the start.

A mid-conversation system message has the same authority as the top-level `system` field, but because it is appended to the end of the message history, it does not invalidate any cached prefix that came before it. Use the top-level `system` field for instructions that should apply from the very first turn, and a mid-conversation system message for instructions that only become relevant later.

See [Mid-conversation system messages](build-with-claude-mid-conversation-system-messages.md) for the complete guide, including how to combine it with [prompt caching](build-with-claude-prompt-caching.md).

## Prefilling Claude’s response

You can prefill part of Claude’s response in the last position of the input messages list. Use this technique to shape Claude’s response. The following example uses `"max_tokens": 1` to get a single multiple choice answer from Claude.



Prefilling is not supported on Claude 4.6 and later models and [Claude Mythos Preview](../../22-Safety-Policy/glasswing.md). Requests using prefill with these models return a 400 error. Use [structured outputs](build-with-claude-structured-outputs.md) on models that support it, or system prompt instructions, instead. See the [migration guide](../../20-Models/about-claude-models-migration-guide.md) for migration patterns.

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
message = anthropic.Anthropic().messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1,
    messages=[
        {
            "role": "user",
            "content": "What is latin for Ant? (A) Apoidea, (B) Rhopalocera, (C) Formicidae",
        },
        {"role": "assistant", "content": "The answer is ("},
    ],
)
print(message)
```

Output



```python
{
  "id": "msg_01Q8Faay6S7QPTvEUUQARt7h",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "C"
    }
  ],
  "model": "claude-sonnet-4-5",
  "stop_reason": "max_tokens",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 42,
    "output_tokens": 1
  }
}
```

## Vision

Claude can read both text and images in requests. You can supply images using the `base64`, `url`, or `file` source types. The `file` source type references an image uploaded through the [Files API](build-with-claude-files.md). Supported media types are `image/jpeg`, `image/png`, `image/gif`, and `image/webp`. See the [Vision](build-with-claude-vision.md) guide for more details.

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
import base64
import httpx2

# Option 1: base64-encoded image
image_url = "https://platform.claude.com/docs/images/vision-example.jpg"
image_media_type = "image/jpeg"
image_data = base64.standard_b64encode(httpx2.get(image_url).content).decode("utf-8")

message = anthropic.Anthropic().messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                    },
                },
                {"type": "text", "text": "What is in the above image?"},
            ],
        }
    ],
)
print(message)

# Option 2: URL-referenced image
message_from_url = anthropic.Anthropic().messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "url",
                        "url": "https://platform.claude.com/docs/images/vision-example.jpg",
                    },
                },
                {"type": "text", "text": "What is in the above image?"},
            ],
        }
    ],
)
print(message_from_url)
```

Output



```python
{
  "id": "msg_011CdKmWtV3oFx1C5yUbf5CY",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "This image is a beautiful minimalist/flat-design illustration of a sunset landscape. Here's what it contains:\n\n**Sky & Sun:**\n- A warm gradient sky transitioning from golden-yellow at the top to deep orange toward the horizon\n- A large pale yellow sun positioned in the upper-right area\n\n**Birds:**\n- Three small silhouetted birds flying in the upper-left portion of the sky, depicted as simple \"M\" or \"v\" shapes\n\n**Mountains:**\n- Multiple layered mountain peaks in purple and maroon tones\n- The mountains overlap to create depth, with varying shades of dusty purple and deep burgundy\n\n**Water:**\n- A dark purple body of water at the bottom of the image\n- A reflection of the sun shown as horizontal cream/peach colored lines in the center-bottom area\n\nThe overall style is clean, geometric, and uses a warm sunset color palette (oranges, yellows, purples, and maroons), giving it a peaceful, serene aesthetic typical of modern vector/flat design artwork."
    }
  ],
  "model": "claude-opus-5-5",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 1030,
    "output_tokens": 350
  }
}
```

## Next steps



[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)

Handle each `stop_reason` value and decide what to do when a response ends.



[Tool use with Claude](../Agents-Tools/agents-and-tools-tool-use-overview.md)

Give Claude tools to call external services and APIs from within the Messages API.



[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)

Control desktop computer environments with the Messages API.

[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)

Let Claude navigate, read, and interact with webpages in a browser you run.



[Structured outputs](build-with-claude-structured-outputs.md)

Get guaranteed, schema-validated JSON output from Claude.



[Task budgets](build-with-claude-task-budgets.md)

Set an advisory token budget across a full agentic loop with `output_config.task_budget`.

## Availability

The Messages API is available on every model and eligible for zero data retention and HIPAA readiness.

### API support

StatusAvailable

### Data handling

[Data handling overview](../Other/manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/messages`

Zero data retentionEligible

Excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

Standard API calls for generating Claude responses.

HIPAAEligible
