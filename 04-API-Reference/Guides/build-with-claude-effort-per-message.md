---
title: "Per-message effort - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/effort-per-message"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-12T06:24:47Z"
tags: ["api"]
---

# Per-message effort

Copy page



Use a system message to change the effort level partway through a conversation and keep the prompt cache.

Copy page



Per-message effort

Beta

Feature of  
[Effort](build-with-claude-effort.md)

[Models](#feature-availability)  
- All latest models
- Limited support for other models; see details

[APIs](#feature-availability)  
- Messages API
- Managed Agents Not supported

[Cloud platforms](#feature-availability)  
- All platforms

[Beta header](#feature-availability)  
- 
  Copy`mid-conversation-output-config-2026-07-01`

A per-message effort change sets a new effort level for later turns of a conversation without changing the request’s top-level value, so the cached prefix still matches.

## Change the effort level

To change the level partway through a conversation:

1.  Add a `role: "system"` message to `messages`, with empty `content` and the new [effort](build-with-claude-effort.md) level in `output_config.effort`.
2.  Send the `mid-conversation-output-config-2026-07-01` [beta header](../Endpoints/beta-headers.md).
3.  Leave the top-level value unchanged.

The following example keeps the top-level value at `high` and drops to `low` for a routine follow-up:

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

response = client.beta.messages.create(
    model="claude-fable-5-1",
    max_tokens=4096,
    output_config={"effort": "high"},
    messages=[
        {
            "role": "user",
            "content": "Plan a migration from SQLite to PostgreSQL in three short steps.",
        },
        {
            "role": "assistant",
            "content": "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts.",
        },
        # Effort-only system message: the new level takes effect from the next user turn.
        {"role": "system", "content": [], "output_config": {"effort": "low"}},
        {"role": "user", "content": "Summarize the plan in one sentence."},
    ],
    betas=["mid-conversation-output-config-2026-07-01"],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

The message’s position decides when the new level starts:

- Directly after a `user` turn with new input: Claude’s reply to that turn uses the new level.
- In any other position, such as between an `assistant` turn and the next `user` turn as in the preceding example: the new level starts at the next `user` turn with new input.

A `user` turn that holds only `tool_result` blocks doesn’t count as new input.

The new level stays in effect until a later message changes it.

Put the message after everything you’ve already sent, and keep it in place on later requests. Don’t insert it before turns you’ve already sent, and don’t move or remove it later. On models with [preserved thinking](build-with-claude-preserved-thinking.md), any of those changes invalidates the thinking blocks in the `assistant` turns after the message. [What the API does with an invalid block](build-with-claude-preserved-thinking.md#mismatch-behavior) says what happens next.

If it sits next to a `system` message that has content, both messages must follow the [placement rules for mid-conversation system messages](build-with-claude-mid-conversation-system-messages.md#limitations).

With the Amazon Bedrock InvokeModel API, send the beta value in the `anthropic_beta` array of the request body instead of the header. For the models that support per-message effort there, see [Mid-conversation system messages on Bedrock](build-with-claude-claude-on-amazon-bedrock-legacy.md#mid-conversation-system-messages-on-bedrock).

## Errors

- Without the beta header, a per-message `output_config` returns a 400 error: `messages.N.output_config: Extra inputs are not permitted`, where `N` is the index of the `system` message in `messages`.
- With the beta header, models without per-message effort, such as Claude Fable 5, return a 400 error: `output_config.effort requires a model that supports per-turn effort; this model does not`. On Amazon Bedrock, those models and Claude Opus 5 return `Extra inputs are not permitted` instead.
- On Claude Sonnet 5.5 with `thinking: {"type": "between_tools"}`, and on Claude Haiku 5.5 with `thinking: {"type": "disabled"}`, you can’t change the effort level mid-conversation. There, a per-message `output_config.effort` with a new level returns a 400 error. To vary effort for each turn, use adaptive thinking.

## Per-message or top-level effort

Prefer per-message effort over [changing the top-level value](build-with-claude-effort.md#top-level-effort-on-the-next-request) between requests. A per-message change leaves everything before it unchanged, so the cached prefix still matches. A top-level change restarts the cache. On Claude Fable 5.1, a top-level change also steers the model less reliably. The model’s earlier replies were written at the previous level, and the model tends to stay consistent with them.

## Availability

Per-message effort

Cloud platform

Cloud platform: Claude API

Claude API

Status  
Beta

APIs  
- Messages API

- Managed Agents Not supported

Beta header  
Requires

mid-conversation-output-config-2026-07-01

Models  
- Claude Fable 5.2, Fable 5.1
- Claude Mythos 5.2, Mythos 5.1
- Claude Opus 5.5, Opus 5
- Claude Sonnet 5.5
- Claude Haiku 5.5

Amazon Bedrock

Status  
Beta

API  
- Messages API

Beta header  
Requires

mid-conversation-output-config-2026-07-01

Models  
- Claude Fable 5.1
- Claude Mythos 5.1
- Claude Opus 5.5

Amazon Bedrock (bedrock-runtime)

Status  
Beta

API  
- Messages API

Beta header  
Requires

mid-conversation-output-config-2026-07-01

Models  
- Claude Fable 5.2, Fable 5.1
- Claude Mythos 5.2
- Claude Opus 5.5

Note  
Send the beta value in the `anthropic_beta` array of the request body.

Claude Platform on AWS

Status  
Beta

APIs  
- Messages API

- Managed Agents Not supported

Beta header  
Requires

mid-conversation-output-config-2026-07-01

Models  
- Claude Fable 5.2, Fable 5.1
- Claude Opus 5.5, Opus 5
- Claude Sonnet 5.5
- Claude Haiku 5.5

Claude Models on Google Cloud (Anthropic managed)

Status  
Beta

APIs  
- Messages API

- Managed Agents Not supported

Beta header  
Requires

mid-conversation-output-config-2026-07-01

Models  
- Claude Fable 5.2, Fable 5.1
- Claude Mythos 5.2
- Claude Opus 5.5, Opus 5
- Claude Sonnet 5.5
- Claude Haiku 5.5

Claude Models on Google Cloud (Google managed)

Status  
Beta

API  
- Messages API

Beta header  
Requires

mid-conversation-output-config-2026-07-01

Models  
- Claude Fable 5.2, Fable 5.1
- Claude Mythos 5.2, Mythos 5.1
- Claude Opus 5.5, Opus 5
- Claude Sonnet 5.5
- Claude Haiku 5.5

Microsoft Foundry (hosted on Azure)

Status  
Beta

API  
- Messages API

Beta header  
Requires

mid-conversation-output-config-2026-07-01

Models  
- Claude Opus 5.5, Opus 5
- Claude Sonnet 5.5
- Claude Haiku 5.5

Microsoft Foundry (hosted on Anthropic)

Status  
Beta

API  
- Messages API

Beta header  
Requires

mid-conversation-output-config-2026-07-01

Models  
- Claude Fable 5.2, Fable 5.1
- Claude Mythos 5.2, Mythos 5.1
- Claude Opus 5.5, Opus 5
- Claude Sonnet 5.5
- Claude Haiku 5.5
