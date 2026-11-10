---
title: "Compaction and preserved thinking - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-07T06:23:44Z"
tags: ["api", "prompting"]
---

# Compaction and preserved thinking

Copy page



When thinking blocks in turns kept after on-demand compaction stay valid on models with preserved thinking, and how to check.

Copy page



Compaction and preserved thinking

Feature of  
[On-demand compaction](build-with-claude-compaction-on-demand.md)

[Status](#availability-feature-support)  
Beta

[APIs](#feature-availability)  
Messages APIAvailable

[Cloud platforms](#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableClaude Models on Google CloudGoogle managedAvailableMicrosoft FoundryAvailable

[Beta header](#feature-beta-headers)  
- `compact-2026-09-04`
  

Skip this page unless you send thinking blocks back to a model with [preserved thinking](build-with-claude-preserved-thinking.md) and keep turns after the compaction block. Kept turns are the turns that follow the block: recent turns you left out of the compaction request, as in [Compaction that keeps recent turns](build-with-claude-compaction-keep-recent-turns.md), or turns that arrived while the summary was being written, as in [Compaction in the background](build-with-claude-compaction-background.md).

Models with preserved thinking check earlier thinking blocks against the conversation that produced them. A summary replaces part of that conversation, but the check accepts the swap when the API wrote the summary, so the thinking in kept turns can stay valid.

## Conditions for kept thinking to stay valid

The thinking blocks in kept turns stay valid while all of these hold:

- **The compaction request runs on a model with preserved thinking.** This condition covers every compaction request since a thinking block was produced, not only the most recent one. One way to meet it is to send every compaction request to the model the conversation uses.
- **The kept turns directly follow the summarized messages, and you send them unchanged.** Send each kept message exactly as it is in your history. Don’t skip or add a message between the last summarized message and the first kept one. The first kept message must also have a different role from the last summarized message, and it can’t be a mid-conversation `role: "system"` message. Otherwise, the API merges it into the last summarized message. One way to get the first kept message right is to compact exactly the `messages` of a request you already sent. The kept turns then start with Claude’s reply to it.
- **`system` and the `tools` not marked `defer_loading: true` don’t change.** They are the same on the compaction request as on the requests that produced the kept thinking, and they stay the same on the requests that follow. [Change the system prompt or tools](#change-the-system-prompt-or-tools) covers how to change them safely.

If a condition doesn’t hold, nothing fails when you compact, and the API accepts the compaction block on later requests either way. What fails is the kept thinking, on the first later request that sends it. [What the API does with an invalid block](build-with-claude-preserved-thinking.md#mismatch-behavior) describes what happens then, and [When `prefix_mismatch_behavior` is unset](build-with-claude-preserved-thinking.md#enforcement) covers requests that don’t set the field, including Message Batches items.

## Compact again without breaking older thinking

You can [compact again](build-with-claude-compaction-on-demand.md#compact-again) and keep turns: the new block covers the old summary and every message that follows it in the compaction request, and any turns you leave out of that request are kept turns of the new block.

The first of the [conditions for kept thinking](#conditions-for-kept-thinking-to-stay-valid) counts every compaction since a thinking block was produced, so a turn that you keep through two compactions needs both to have run on a model with preserved thinking.

Compactions from before a thinking block was produced don’t count against it. Thinking produced after a block is in place is bound to that block, and it stays valid through later compactions that meet the conditions.

## Change the system prompt or tools

A later request can use a different `system`, different `tools`, or a different model from the compaction request, and the API still accepts the block. Such a change can invalidate the thinking in the kept turns, but it has no other effect.

To change `system` or `tools` without invalidating any kept thinking, compact the whole conversation first, so no turns are kept. Then change them on the next request.

To add an instruction or change the available tools without touching `system` or `tools`, append the change to `messages`, as described in [Make changes without editing the prefix](build-with-claude-preserved-thinking.md#replace-prefix-edits).

Mid-conversation system messages inside the summarized turns are summarized too, so their text instructions stop applying after the swap. A [per-message effort](build-with-claude-effort.md#change-effort-mid-conversation-beta) level they set isn’t carried over either: until a later message sets a level, turns run at the request’s top-level `output_config.effort`, or the model’s default if you don’t set one. To keep an instruction or effort level in force, state it again in a `role: "system"` message directly after the first new `user` turn that follows the kept turns. Tool changes inside those turns carry over on their own when the compaction request also carries `inline-tools-2026-09-15`: the returned block records their net effect in its `tool_changes` field, so send the block back unmodified. If the block has no `tool_changes` field, restate those tool changes the same way. A system message placed between the block and the kept turns breaks their thinking.

## Check that the kept thinking held

The compaction response doesn’t say whether the kept thinking holds. The first request after the swap does. To check in your tests:

1.  Have a short conversation with thinking on. Use a model that runs the prefix check (see [Keeping the prefix unchanged](build-with-claude-preserved-thinking.md#prefix-check)), and use it for every step, because a model that can’t read a thinking block drops it with no error.
2.  Compact the older turns, and keep at least one turn that holds a thinking block.
3.  Send the next request, with the block first, then the kept turn, then a new `user` message, and with `thinking.block_binding.prefix_mismatch_behavior` set to `"error"`.
4.  Read the result. A 200 response whose `input_transformations` array is empty means no thinking block failed the check or was dropped. A 400 error that says the block is bound to a different conversation means one did. The message starts with the path of the first block that failed, and [What the API does with an invalid block](build-with-claude-preserved-thinking.md#mismatch-behavior) shows it in full.

The `prefix_mismatch_behavior` field needs the `thinking-binding-controls-2026-08-01` beta header in addition to the [`compact-2026-09-04` beta header](build-with-claude-compaction-on-demand.md#request-a-summary). The value a request sets applies on any account.

The following program runs the four steps. It prints how many thinking blocks the kept turn holds and how many entries `input_transformations` has; no entries means the kept thinking held:

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
# With "error", a thinking block that fails the check makes the request fail with a 400.
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
print(f"Dropped thinking blocks: {len(third.input_transformations)}")
```

Output



``` block
Thinking blocks in the kept turn: 1
Dropped thinking blocks: 0
```

In production, `"drop_block"` keeps requests succeeding when a condition doesn’t hold. The response lists each dropped block in `input_transformations` with `reason: "prefix_binding_mismatch"`. An entry whose `path` falls in a kept turn means a condition didn’t hold for that turn’s thinking. [What the API does with an invalid block](build-with-claude-preserved-thinking.md#mismatch-behavior) describes what is dropped and says how to alert on it. On Claude Sonnet 5.5 and Claude Haiku 5.5, `block_binding` works only with `thinking: {"type": "adaptive"}`. With any other thinking setting on those models, you can’t send `block_binding`, so make sure every condition holds or strip the `thinking` and `redacted_thinking` blocks from the kept turns.

## Availability

Compaction and preserved thinking are in beta on select models.

### API support

[Messages API](build-with-claude-working-with-messages.md)

StatusBeta

Cloud platforms

- Claude API
- [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)
- [Claude Models on Google Cloud](build-with-claude-claude-models-on-google-cloud-google-managed.md)Google managed
- [Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

Models

- [Claude Haiku 4.5](../../20-Models/models-haiku-4-5-overview.md)Not supported
- [Claude Opus 4.5](../../20-Models/models-opus-4-5-overview.md)Not supported
- [Claude Sonnet 4.5](../../20-Models/models-sonnet-4-5-overview.md)Not supported
- All other models

### Required beta headers

[Beta headers overview](../Endpoints/beta-headers.md)

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

Header

- `compact-2026-09-04`
  
