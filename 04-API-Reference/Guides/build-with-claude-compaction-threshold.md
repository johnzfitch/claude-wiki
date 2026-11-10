---
title: "Compaction at a token threshold - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-threshold"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-08T06:24:41Z"
tags: ["api"]
---

# Compaction at a token threshold

Copy page



Have the API summarize older context automatically, inside an ordinary request, when the conversation reaches a token threshold you set.

Copy page



Threshold compaction

[Status](#availability-feature-support)  
Beta

[APIs](#feature-availability)  
Messages APIAvailableManaged AgentsAlways on

[Cloud platforms](#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableAmazon BedrockAvailableAmazon BedrockInvokeModelAvailableClaude Models on Google CloudGoogle managedAvailableMicrosoft FoundryAvailable

[Beta header](#feature-beta-headers)  
Messages API
- `compact-2026-01-12`
  

[Data handling](#feature-data-handling)  
ZDR eligibleNot HIPAA eligible

Usage differs by product

Messages API

Opt in with a `compact_20260112` edit; compaction starts at 150,000 input tokens by default.

Managed Agents

Always onIt compacts the session’s conversation history to fit the context window.

Threshold compaction is the automatic kind of compaction: you set a token threshold on your ordinary requests, and the API summarizes older context partway through a request once the threshold is reached. It is supported alongside on-demand compaction, where you decide when the summary is written (see [Compaction on demand](build-with-claude-compaction-on-demand.md)). To choose between them, see [Choose how to compact](build-with-claude-compaction.md#choose-how-to-compact).

Compaction extends the effective context length for long-running conversations and tasks by automatically summarizing older context when approaching the context window limit. It also keeps the active context small: as a conversation grows, response quality degrades, so compaction replaces older content with a concise summary.



For a deeper look at why long contexts degrade and how compaction helps, see [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents).

This is ideal for:

- Chat-based, multi-turn conversations where you want users to use one chat for a long period of time
- Task-oriented prompts that require a lot of follow-up work (often tool use) that might exceed the context window

## How compaction works

When compaction is enabled, Claude automatically summarizes your conversation when it reaches the configured token threshold. The API:

1.  Detects when input tokens reach your specified trigger threshold.
2.  Generates a summary of the current conversation.
3.  Creates a `compaction` block containing the summary.
4.  Continues the response with the compacted context.

On subsequent requests, append the response to your messages. The API automatically drops all content blocks prior to the `compaction` block, continuing the conversation from the summary.

## Basic usage

Enable compaction by adding the `compact_20260112` strategy to `context_management.edits` in your Messages API request.

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

messages = [{"role": "user", "content": "Help me build a website"}]

response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)

# Append the response (including any compaction block) to continue the conversation
messages.append({"role": "assistant", "content": response.content})
```

## Parameters

| Parameter | Type | Default | Description |
|:---|:---|:---|:---|
| `type` | string | Required | Must be `"compact_20260112"` |
| `trigger` | object | `{"type": "input_tokens", "value": 150000}` | When to trigger compaction. `input_tokens` is the only supported trigger type. `value` must be at least 50,000 tokens. |
| `pause_after_compaction` | boolean | `false` | Whether to pause after generating the compaction summary |
| `instructions` | string | `null` | Custom summarization prompt. Completely replaces the default prompt when provided. |

### Trigger configuration

Configure when compaction triggers using the `trigger` parameter:

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
messages = [{"role": "user", "content": "Hello, Claude"}]
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [
            {
                "type": "compact_20260112",
                "trigger": {"type": "input_tokens", "value": 150000},
            }
        ]
    },
)
```

### Custom summarization instructions

The default summarization prompt varies by model. Each default instructs Claude to write a summary inside `<summary></summary>` tags with the information needed to continue the task in a future context window. For example, some models use the following prompt:

``` block
You have written a partial transcript for the initial task above. Please write a summary of the transcript. The purpose of this summary is to provide continuity so you can continue to make progress towards solving the task in a future context, where the raw history above may not be accessible and will be replaced with this summary. Write down anything that would be helpful, including the state, next steps, learnings etc. You must wrap your summary in a <summary></summary> block.
```



You can provide custom instructions through the `instructions` parameter. Custom instructions don’t supplement the default prompt. They replace it completely:

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
messages = [{"role": "user", "content": "Hello, Claude"}]
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [
            {
                "type": "compact_20260112",
                "instructions": "Focus on preserving code snippets, variable names, and technical decisions.",
            }
        ]
    },
)
```

On Claude 5.1 and later models, a request with custom `instructions` summarizes from the visible conversation only: earlier thinking blocks are not part of the summarizer’s input.

### Pausing after compaction

Use `pause_after_compaction` to pause the API after generating the compaction summary. This allows you to add additional content blocks (such as preserving recent messages or specific instruction-oriented messages) before the API continues with the response.

When enabled, the API returns a message with the `compaction` stop reason after generating the compaction block:

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
messages = [{"role": "user", "content": "Hello, Claude"}]
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [{"type": "compact_20260112", "pause_after_compaction": True}]
    },
)

# Check if compaction triggered a pause
if response.stop_reason == "compaction":
    # Response contains only the compaction block
    messages.append({"role": "assistant", "content": response.content})

    # Continue the request
    response = client.beta.messages.create(
        betas=["compact-2026-01-12"],
        model="claude-opus-5-5",
        max_tokens=4096,
        messages=messages,
        context_management={"edits": [{"type": "compact_20260112"}]},
    )
```

The API pauses even if no summary is generated. The `compaction` block’s `content` is then `null`, so keep the original messages when you continue. If safeguards block the summary, `content` is also `null` and the stop reason is `refusal` instead of `compaction`. [`stop_details`](build-with-claude-handling-stop-reasons.md#refusal) gives the policy category, if there is one. Continue the same way in both cases: look for the `compaction` block instead of testing `stop_reason`, as the [example that preserves recent messages](#examples) does.

#### Enforcing a total token budget

When a model works on long tasks with many tool-use iterations, total token consumption can grow significantly. You can combine `pause_after_compaction` with a compaction counter to estimate cumulative usage and gracefully conclude the task once a budget is reached.

This example appears in the SDK languages only: its value is the budget-tracking logic around the request. The raw request combines the `trigger` from [Trigger configuration](#trigger-configuration) with `pause_after_compaction` from [Pausing after compaction](#pausing-after-compaction).

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
messages = [{"role": "user", "content": "Hello, Claude"}]
TRIGGER_THRESHOLD = 100_000
TOTAL_TOKEN_BUDGET = 3_000_000
n_compactions = 0

response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [
            {
                "type": "compact_20260112",
                "trigger": {"type": "input_tokens", "value": TRIGGER_THRESHOLD},
                "pause_after_compaction": True,
            }
        ]
    },
)

if response.stop_reason == "compaction":
    n_compactions += 1
    messages.append({"role": "assistant", "content": response.content})

    # Estimate total tokens consumed; prompt wrap-up if over budget
    if n_compactions * TRIGGER_THRESHOLD >= TOTAL_TOKEN_BUDGET:
        messages.append(
            {
                "role": "user",
                "content": "Please wrap up your current work and summarize the final state.",
            }
        )
```

## Working with compaction blocks

When compaction is triggered, the API returns a `compaction` block at the start of the assistant response.

A long-running conversation might result in multiple compactions. The last compaction block reflects the final state of the prompt, replacing content prior to it with the generated summary.

Output



```python
{
  "content": [
    {
      "type": "compaction",
      "content": "Summary of the conversation: The user requested help building a web scraper..."
    },
    {
      "type": "text",
      "text": "Based on our conversation so far..."
    }
  ]
}
```

### Passing compaction blocks back

You must pass the `compaction` block back to the API on subsequent requests to continue the conversation with the shortened prompt. The simplest approach is to append the entire response content to your messages:

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
messages = [{"role": "user", "content": "Hello, Claude"}]
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)
# After receiving a response with a compaction block
messages.append({"role": "assistant", "content": response.content})

# Continue the conversation
messages.append({"role": "user", "content": "Now add error handling"})

response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)
```

In Python, use `client.beta.messages`, as the samples on this page do. If you call `client.messages` and serialize blocks yourself, a plain `model_dump()` adds `text: null` and `citations: null` to the `compaction` block. The API then rejects the request with a 400 error (`Extra inputs are not permitted`). Use `to_dict()` or `model_dump(exclude_none=True)` instead. [Continue from the summary](build-with-claude-compaction-on-demand.md#continue-from-the-summary) gives the same advice for on-demand compaction.

When the API receives a `compaction` block, all content blocks before it are ignored. You can either:

- Keep the original messages in your list and let the API handle removing the compacted content
- Manually drop the compacted messages and only include the compaction block onward

If no summary is generated, the block’s `content` is `null` and the API ignores the block. Nothing is compacted, so keep the original messages.

On Claude 5.1 and later models, thinking blocks from before a `compaction` block aren’t carried forward, so the summary is all the model has of that earlier work. If you write your own `instructions`, tell the model what the summary must retain; see [Tell the model what to preserve in compaction summaries](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md#tell-the-model-what-to-preserve-in-compaction-summaries).

### Streaming

The compaction block streams differently from text blocks. You receive a `content_block_start` event, followed by a single `content_block_delta` with the complete summary content (no intermediate streaming), and then a `content_block_stop` event.

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
messages = [{"role": "user", "content": "Hello, Claude"}]

with client.beta.messages.stream(
    betas=["compact-2026-01-12"],
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
) as stream:
    for event in stream:
        match event.type:
            case "content_block_start":
                block = event.content_block
                match block.type:
                    case "compaction":
                        print("Compaction started...")
                    case "text":
                        print("Text response started...")

            case "content_block_delta":
                delta = event.delta
                match delta.type:
                    case "compaction_delta":
                        print(f"Compaction complete: {len(delta.content or '')} chars")
                    case "text_delta":
                        print(delta.text, end="", flush=True)

    # Get the final accumulated message
    message = stream.get_final_message()
    messages.append({"role": "assistant", "content": message.content})
```

### Prompt caching

Compaction works well with [prompt caching](build-with-claude-prompt-caching.md). You can add a `cache_control` breakpoint on compaction blocks to cache the summarized content.

```python
{
  "role": "assistant",
  "content": [
    {
      "type": "compaction",
      "content": "[summary text]",
      "cache_control": { "type": "ephemeral" }
    },
    {
      "type": "text",
      "text": "Based on our conversation..."
    }
  ]
}
```



#### Maximizing cache hits with system prompts

When compaction occurs, the summary becomes new content that needs to be written to the cache. Without additional cache breakpoints, this would also invalidate any cached system prompt, requiring it to be re-cached along with the compaction summary.

To maximize cache hit rates, add a `cache_control` breakpoint at the end of your system prompt. This keeps the system prompt cached separately from the conversation, so when compaction occurs:

- The system prompt cache remains valid and is read from cache
- Only the compaction summary needs to be written as a new cache entry

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
messages = [{"role": "user", "content": "Hello, Claude"}]
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-5-5",
    max_tokens=4096,
    system=[
        {
            "type": "text",
            "text": "You are a helpful coding assistant...",
            "cache_control": {
                "type": "ephemeral"
            },  # Cache the system prompt separately
        }
    ],
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)
```

This keeps long system prompts cached across multiple compaction events throughout a conversation.

## Understanding usage

Compaction requires an additional sampling step, which contributes to rate limits and billing. The API returns detailed usage information in the response:

Output



```python
{
  "usage": {
    "input_tokens": 23000,
    "output_tokens": 1000,
    "iterations": [
      {
        "type": "compaction",
        "input_tokens": 180000,
        "output_tokens": 3500
      },
      {
        "type": "message",
        "input_tokens": 23000,
        "output_tokens": 1000
      }
    ]
  }
}
```

The `iterations` array shows usage for each sampling iteration. When compaction occurs, you’ll see a `compaction` iteration followed by the main `message` iteration. The top-level `input_tokens` and `output_tokens` match the `message` iteration exactly in this example because there is only one non-compaction iteration. The final iteration’s token counts reflect the effective context size after compaction.



The top-level `input_tokens` and `output_tokens` do not include compaction iteration usage. They reflect the sum of all non-compaction iterations. To calculate total tokens consumed and billed for a request, sum across all entries in the `usage.iterations` array.

If you previously relied on `usage.input_tokens` and `usage.output_tokens` for cost tracking or auditing, you’ll need to update your tracking logic to aggregate across `usage.iterations` when compaction is enabled. With the compaction beta enabled, every response includes `usage.iterations`, even if no compaction occurred. A `compaction` entry appears only when a new compaction is triggered during the request. Re-applying a previous `compaction` block incurs no additional compaction cost, and the top-level usage fields remain accurate in that case.

## Combining with other features

### Server tools

When using server tools (such as web search), the compaction trigger is checked at the start of each sampling iteration. Compaction might occur multiple times within a single request depending on your trigger threshold and the amount of output generated.

### Token counting

The token counting endpoint (`/v1/messages/count_tokens`) applies existing `compaction` blocks in your prompt but does not trigger new compactions. Use it to check your effective token count after previous compactions:

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
messages = [{"role": "user", "content": "Hello, Claude"}]
count_response = client.beta.messages.count_tokens(
    betas=["compact-2026-01-12"],
    model="claude-opus-5-5",
    messages=messages,
    context_management={"edits": [{"type": "compact_20260112"}]},
)

print(f"Current tokens: {count_response.input_tokens}")
print(f"Original tokens: {count_response.context_management.original_input_tokens}")
```

## Examples

Here’s a complete example of a long-running conversation with compaction:

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

messages: list[dict] = []


def chat(user_message: str) -> str:
    messages.append({"role": "user", "content": user_message})

    response = client.beta.messages.create(
        betas=["compact-2026-01-12"],
        model="claude-opus-5-5",
        max_tokens=4096,
        messages=messages,
        context_management={
            "edits": [
                {
                    "type": "compact_20260112",
                    "trigger": {"type": "input_tokens", "value": 100000},
                }
            ]
        },
    )

    # Append response (compaction blocks are automatically included)
    messages.append({"role": "assistant", "content": response.content})

    # Return the text content
    return next((block.text for block in response.content if block.type == "text"), "")


# Run a long conversation
print(chat("Briefly, help me build a Python web scraper"))
print(chat("Briefly, add support for JavaScript-rendered pages"))
print(chat("Briefly, add rate limiting and error handling"))
# Continue calling chat() for as long as the conversation needs
```

On Claude 5.1 and later models, thinking blocks in any assistant turn you reinsert after the compaction block fail the [prefix check](build-with-claude-thinking.md#preserved-in-conversation), because they were produced when the full history was present. Strip the `thinking` and `redacted_thinking` blocks from those turns. Alternatively, send `thinking.block_binding.prefix_mismatch_behavior: "drop_block"` with the `thinking-binding-controls-2026-08-01` [beta header](../Endpoints/beta-headers.md). The preserved text and tool blocks can stay as they are. Letting the API summarize everything, without reinserting earlier turns, avoids this. On Claude Sonnet 5.5 and Claude Haiku 5.5, `block_binding` works only with `thinking: {"type": "adaptive"}`. With any other thinking setting on those models, strip the blocks.

Here’s an example that uses `pause_after_compaction` to preserve the prior exchange and the current user message (three messages total) instead of summarizing them. It keeps their text and tool blocks unchanged, removes the `thinking` and `redacted_thinking` blocks from the preserved assistant turn, and drops that turn if nothing else is left:

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
from typing import Any

client = anthropic.Anthropic()

messages: list[dict[str, Any]] = []


def chat(user_message: str) -> str:
    messages.append({"role": "user", "content": user_message})

    response = client.beta.messages.create(
        betas=["compact-2026-01-12"],
        model="claude-opus-5-5",
        max_tokens=4096,
        messages=messages,
        context_management={
            "edits": [
                {
                    "type": "compact_20260112",
                    "trigger": {"type": "input_tokens", "value": 100000},
                    "pause_after_compaction": True,
                }
            ]
        },
    )

    # Look for the compaction block, not the stop reason:
    # stop_reason is "refusal", not "compaction", if the summary was blocked
    compaction_block = next(
        (block for block in response.content if block.type == "compaction"), None
    )

    # Replace the history only if a summary was generated
    if compaction_block is not None and compaction_block.content is not None:
        # Preserve the prior exchange + current user message (3 messages)
        # by including them after the compaction block, without thinking
        # blocks; an assistant turn left with no content is dropped
        preserved_messages = [
            {
                **message,
                "content": [
                    block
                    for block in message["content"]
                    if block.type not in ("thinking", "redacted_thinking")
                ],
            }
            if message["role"] == "assistant"
            else message
            for message in messages[-3:]
        ]
        preserved_messages = [m for m in preserved_messages if m["content"]]

        # Build new message list: compaction + preserved messages
        new_assistant_content = [compaction_block]
        messages_after_compaction = [
            {"role": "assistant", "content": new_assistant_content}
        ] + preserved_messages

        # Update the message list to reflect the compaction
        messages.clear()
        messages.extend(messages_after_compaction)

    if compaction_block is not None:
        # Continue the request, with the full history if there is no summary
        response = client.beta.messages.create(
            betas=["compact-2026-01-12"],
            model="claude-opus-5-5",
            max_tokens=4096,
            messages=messages,
            context_management={"edits": [{"type": "compact_20260112"}]},
        )

    # Append the final response
    messages.append({"role": "assistant", "content": response.content})

    # Return the text content
    return next((block.text for block in response.content if block.type == "text"), "")


# Run a long conversation
print(chat("Briefly, help me build a Python web scraper"))
print(chat("Briefly, add support for JavaScript-rendered pages"))
print(chat("Briefly, add rate limiting and error handling"))
# Continue calling chat() for as long as the conversation needs
```

## Current limitations

- **Same model for summarization:** The model specified in your request is used for summarization. There is no option to use a different (for example, cheaper) model for the summary.

- **Compaction might fail when tools are defined:** When your request includes `tools`, the model occasionally calls a tool during the internal summarization step instead of writing a summary. When this occurs, the response contains a `compaction` block with `content: null`. To prevent this, set [`instructions`](#custom-summarization-instructions) to a prompt that explicitly tells the model not to call tools, for example:

  ``` block
  Summarize the transcript inside <summary></summary> tags. Include relevant information in the summary for continuing the task in the next context window. Do not call any tools while writing this summary; respond with text only.
  ```

  

## Next steps



[Context editing](build-with-claude-context-editing.md)

Automatically manage conversation context as it grows with context editing.

[Context windows](build-with-claude-context-windows.md)

Learn about context window sizes and management strategies.



[Session memory compaction recipe (Claude Cookbook)](https://platform.claude.com/cookbook/misc-session-memory-compaction)

Explore a practical implementation that manages long-running conversations with instant session memory compaction using background threading and prompt caching.

## Availability

Threshold compaction is in beta on select models and eligible for zero data retention.

### API support

[Messages API](build-with-claude-working-with-messages.md)

Usage

Opt in with a `compact_20260112` edit in `context_management.edits`. Compaction starts when input tokens reach the trigger, 150,000 by default and at least 50,000.

StatusBeta

Cloud platforms

- Claude API
- [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)
- [Amazon Bedrock](build-with-claude-claude-in-amazon-bedrock.md)
- [Amazon Bedrock](build-with-claude-claude-on-amazon-bedrock-legacy.md)InvokeModel
- [Claude Models on Google Cloud](build-with-claude-claude-models-on-google-cloud-google-managed.md)Google managed
- [Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

Models

- [Claude Haiku 4.5](../../20-Models/models-haiku-4-5-overview.md)Not supported
- [Claude Opus 4.5](../../20-Models/models-opus-4-5-overview.md)Not supported
- [Claude Sonnet 4.5](../../20-Models/models-sonnet-4-5-overview.md)Not supported
- All other models

[Managed Agents](../Other/managed-agents-overview.md)

Usage

Always on

It compacts the session’s conversation history to fit the context window, and each compaction emits an `agent.thread_context_compacted` event.

StatusBeta

Cloud platforms

- Claude API
- [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)

Models

- [Claude Haiku 4.5](../../20-Models/models-haiku-4-5-overview.md)Not supported
- [Claude Opus 4.5](../../20-Models/models-opus-4-5-overview.md)Not supported
- [Claude Sonnet 4.5](../../20-Models/models-sonnet-4-5-overview.md)Not supported
- All other models

### Required beta headers

[Beta headers overview](../Endpoints/beta-headers.md)

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

Header

- `compact-2026-01-12`
  

APIs

- [Messages API](build-with-claude-working-with-messages.md)

### Data handling

[Data handling overview](../Other/manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/messages` with `context_management`

Zero data retentionEligible

Excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

Server-side compaction results are returned and round-tripped statelessly through the API response.

HIPAANot eligible
