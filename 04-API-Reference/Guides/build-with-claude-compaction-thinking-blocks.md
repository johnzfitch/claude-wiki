---
title: "Compaction and preserved thinking - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-15T06:24:20Z"
tags: ["api", "prompting"]
---

# Compaction and preserved thinking

Copy page



When thinking in turns kept after compaction, or after your own summary or cut, stays valid on models with preserved thinking, and how to check.

Copy page



Compaction and preserved thinking

Feature of  
[On-demand compaction](build-with-claude-compaction-on-demand.md)

[Status](#feature-availability)  
Beta

[Models](#feature-availability)  
- All latest models
- Limited support for other models; see details

[APIs](#feature-availability)  
- Messages API

[Cloud platforms](#feature-availability)  
- Claude API
- Claude Platform on AWS
- Claude Models on Google CloudGoogle managed
- Microsoft Foundry

[Beta header](#feature-availability)  
- 
  Copy`compact-2026-09-04`

Skip this page unless you send thinking blocks back to a model with [preserved thinking](build-with-claude-preserved-thinking.md) and keep turns after the compaction block, or after your own summary or cut. Kept turns are the turns that follow the block. They’re either recent turns you left out of the compaction request, as in [Compaction that keeps recent turns](build-with-claude-compaction-keep-recent-turns.md), or turns that arrived while the API was writing the summary, as in [Compaction in the background](build-with-claude-compaction-background.md).

Models with preserved thinking check earlier thinking blocks against the conversation that produced them. A summary replaces part of that conversation, but the [prefix check](build-with-claude-preserved-thinking-prefix-checks.md#prefix-check) accepts the swap when the API wrote the summary, so the thinking in kept turns can stay valid.

## Conditions for kept thinking to stay valid

The thinking blocks in kept turns stay valid while all of these hold:

- **The compaction request runs on a model with preserved thinking.** This condition covers every compaction request since a thinking block was produced, not only the latest. One way to meet it is to send every compaction request to the model the conversation uses.
- **The kept turns directly follow the summarized messages, and you send them unchanged.** Send each kept message exactly as it is in your history, and don’t send summarized messages again. Don’t skip or add a message between the last summarized message and the first kept one. The first kept message must also have a different role from the last summarized message, and it can’t be a mid-conversation `role: "system"` message. Otherwise, the API merges it into the last summarized message. One way to get the first kept message right is to compact exactly the `messages` of a request you already sent. The kept turns then start with Claude’s reply to it.
- **`system` and `tools` don’t change.** They are the same on the compaction request as on the requests that produced the kept thinking, and they stay the same on the requests that follow. The exception is a tool marked `defer_loading: true` that nothing has referenced. To change them safely, see [Change the system prompt or tools](#change-the-system-prompt-or-tools).

If a condition doesn’t hold, the API still accepts the compaction block on later requests. What fails is the kept thinking, on the first later request that sends it. The compaction request runs the prefix check on the thinking blocks it carries, so a changed `system` or `tools`, or an edited message, can fail that request too. For what happens then, see [Set `prefix_mismatch_behavior`](build-with-claude-preserved-thinking-prefix-checks.md#preserved-thinking-controls).

## Compact again without breaking older thinking

You can [compact again](build-with-claude-compaction-on-demand.md#compact-again) and keep turns: the new block covers the old summary and every message that follows it in the compaction request, and any turns you leave out of that request are kept turns of the new block.

For a turn’s thinking to stay valid through two compactions, both must have run on a model with preserved thinking.

Compactions from before a thinking block was produced don’t count against it. Thinking produced after a block is in place is bound to that block, and it stays valid through later compactions that meet the conditions.

## Change the system prompt or tools

A later request can use another `system`, `tools`, or model that supports on-demand compaction, and the API still accepts the block. The change can invalidate the kept thinking.

To change `system` or `tools` without invalidating any kept thinking, compact the whole conversation first, so no turns are kept. Then change them on the next request.

To add an instruction or change the available tools without touching `system` or `tools`, append the change to `messages`, as described in [Change tools or instructions without failing the prefix check](build-with-claude-preserved-thinking-change-tools-or-instructions.md).

The summarized turns can include mid-conversation system messages, which are `role: "system"` entries in `messages`. They’re summarized with the rest, so their text instructions and [per-message effort](build-with-claude-effort-per-message.md) levels stop applying (see [Limits and interactions with other features](build-with-claude-compaction-on-demand.md#how-it-fits-with-the-rest-of-the-api)). Their tool changes can carry over:

1.  Send the `inline-tools-2026-09-15` beta header on the compaction request. The returned block then records the changes in a `tool_changes` field.
2.  Send the block back unmodified. The API then applies the recorded changes on each request that includes the block. If the field is missing, the API accepts the block but applies nothing, so state the changes again.
3.  Send the same header on every request that includes the block.

You can state an instruction, an effort level, or a tool change again. Put it in a `role: "system"` message directly after the new `user` message of your next request. The request’s `messages` then run in this order:

1.  The compaction block.
2.  The kept turns, if any.
3.  Your `user` message.
4.  The `role: "system"` message.

On later requests, leave those entries as they are, and add new turns after the system message. Don’t put the system message before or between the kept turns, where it invalidates every kept thinking block after it.

## When your code writes the summary

This section applies wherever the [prefix check runs](build-with-claude-preserved-thinking-prefix-checks.md#enforcement), with or without on-demand compaction.

If your code writes the summary, the thinking in turns you keep after it fails the [prefix check](build-with-claude-preserved-thinking-prefix-checks.md#prefix-check), because your summary replaced the messages that thinking came after. To keep that thinking, have the API write the summary.

The same goes for turns you keep by [pausing after compaction](build-with-claude-compaction-threshold.md#pausing-after-compaction) at a token threshold, turns Claude produced while your code summarized in the background, and turns after a cut.

Remove those turns’ `thinking` and [`redacted_thinking`](build-with-claude-thinking.md#redacted-thinking-blocks) blocks and keep their other blocks, or send [`"drop_block"`](build-with-claude-preserved-thinking-prefix-checks.md#preserved-thinking-controls) on every request that includes them. Either way, Claude reads those turns without that thinking, and [output tokens can increase](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md#drop-block-cost).

If you send only your summary and the next instruction, as one user message, no earlier thinking is sent, and later thinking is valid.

## Check that the kept thinking held

The compaction response doesn’t say whether the kept thinking holds. The first request after the swap does. To check in your tests:

1.  Have a short conversation with thinking on. Use a [model that runs the prefix check](build-with-claude-preserved-thinking-prefix-checks.md#enforcement), and use it for every step, because a model that can’t read a thinking block drops it with no error.
2.  Compact the older turns, and keep at least one turn that holds a thinking block.
3.  Send the next request, with the block first, then the kept turn, then a new `user` message, and with `thinking.block_binding.prefix_mismatch_behavior` set to `"error"`.
4.  Read the result. A 200 response whose `input_transformations` array is empty means no thinking block failed the prefix check or was dropped. A [400 error](../Endpoints/errors.md#thinking-block-conversation-mismatch) that says the block is bound to a different conversation means one did. The message starts with the path of the first block that failed, as [Error: The block is bound to a different conversation](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md#prefix-mismatch-error) shows.

The `prefix_mismatch_behavior` setting needs the `thinking-binding-controls-2026-08-01` beta header in addition to the [`compact-2026-09-04` beta header](build-with-claude-compaction-on-demand.md#request-a-summary).

The following program runs the four steps. It prints how many thinking blocks the kept turn holds and how many entries `input_transformations` has; no entries means the kept thinking held:

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
from anthropic.types.beta import BetaMessageParam, BetaThinkingConfigParam

client = anthropic.Anthropic()

# Claude Fable 5.1 is the first model that checks sent-back thinking against the conversation.
MODEL = "claude-fable-5-1"
BETAS = ["compact-2026-09-04", "thinking-binding-controls-2026-08-01"]
SYSTEM = "You help plan a recipe app's release. Keep answers short."
# With "error", a thinking block that fails the prefix check makes the request fail with a 400.
THINKING: BetaThinkingConfigParam = {
    "type": "adaptive",
    "block_binding": {"prefix_mismatch_behavior": "error"},
}

# 1. Have a short conversation with thinking on.
history: list[BetaMessageParam] = [
    {"role": "user", "content": "What are the main entities in the app's data model?"}
]
first = client.beta.messages.create(
    model=MODEL,
    max_tokens=8192,
    system=SYSTEM,
    betas=BETAS,
    thinking=THINKING,
    messages=history,
)
history += [
    {"role": "assistant", "content": first.content},
    {
        "role": "user",
        "content": "Testing starts on Tuesday, March 3, 2026, takes 10 weekdays, and pauses on March 9 and March 16. On which date does it end?",
    },
]
second = client.beta.messages.create(
    model=MODEL,
    max_tokens=8192,
    system=SYSTEM,
    betas=BETAS,
    thinking=THINKING,
    messages=history,
)
history.append({"role": "assistant", "content": second.content})
thinking_blocks = sum(block.type == "thinking" for block in second.content)
print(f"Thinking blocks in the kept turn: {thinking_blocks}")

# 2. Summarize the first turn. The second turn stays out of the request.
summary = client.beta.messages.create(
    model=MODEL,
    max_tokens=4096,
    system=SYSTEM,
    betas=BETAS,
    thinking=THINKING,
    messages=history[:2],
    compaction={"type": "summarize"},
)
if summary.stop_reason != "compaction":
    raise SystemExit(f"No summary: {summary.stop_reason}")

# 3. Put the block in front of the kept turn and ask the next question.
history = [
    {"role": "assistant", "content": summary.content},
    *history[2:],
    {"role": "user", "content": "Which day should the release go out?"},
]
third = client.beta.messages.create(
    model=MODEL,
    max_tokens=8192,
    system=SYSTEM,
    betas=BETAS,
    thinking=THINKING,
    messages=history,
)

# 4. A 200 with no dropped blocks means the kept thinking held.
print(f"Dropped thinking blocks: {len(third.input_transformations or [])}")
```

Output



```
Thinking blocks in the kept turn: 1
Dropped thinking blocks: 0
```

In production, `"drop_block"` keeps requests succeeding when a condition doesn’t hold, and the response lists each dropped block in `input_transformations` with `reason: "prefix_binding_mismatch"`. An entry whose `path` falls in a kept turn means a condition didn’t hold for that turn’s thinking. For how to alert on those entries, see [Watch production, and find reasoning lost with no error](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md#monitor). On Claude Sonnet 5.5 and Claude Haiku 5.5, `block_binding` works only with `thinking: {"type": "adaptive"}`. With any other thinking setting on those models, make sure every condition holds, or remove the `thinking` and `redacted_thinking` blocks from the kept turns.

## Availability

Compaction and preserved thinking

Cloud platform

Cloud platform: Claude API

Claude API

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Mythos 5.2, Mythos 5.1, Mythos 5, Mythos Preview
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5

Claude Platform on AWS

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5

Claude Models on Google Cloud (Google managed)

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Mythos 5.2, Mythos 5.1, Mythos 5
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5

Microsoft Foundry (hosted on Azure)

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Opus 5.5, Opus 5, Opus 4.8
- Claude Sonnet 5.5, Sonnet 5
- Claude Haiku 5.5

Microsoft Foundry (hosted on Anthropic)

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Mythos 5.2, Mythos 5.1, Mythos 5
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5
