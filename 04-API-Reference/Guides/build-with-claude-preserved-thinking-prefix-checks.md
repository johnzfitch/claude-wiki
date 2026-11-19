---
title: "Prefix checks on thinking blocks - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/preserved-thinking/prefix-checks"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-13T06:36:27Z"
tags: ["api", "prompting"]
---

# Prefix checks on thinking blocks

Copy page



What the prefix check compares, which models run it, what happens when a request fails it, and how to handle the 400 error and the case with no error.

Copy page



[Preserved thinking](build-with-claude-preserved-thinking.md)

Safeguard of  
[Thinking](build-with-claude-thinking.md)

[Models](build-with-claude-preserved-thinking.md#feature-availability)  
- All latest models
- Limited support for other models; see details

[APIs](build-with-claude-preserved-thinking.md#feature-availability)  
- Messages API
- Managed Agents

[Cloud platforms](build-with-claude-preserved-thinking.md#feature-availability)  
- All platforms

Each request that sends thinking blocks back to a [model with preserved thinking](#outcomes) gets a prefix check. A prefix check fails if `system`, `tools`, or an earlier message changed after Claude produced a block. It also fails if a thinking block between others was left out or moved.

Failing the prefix check might or might not result in a 400 error, [depending on the model](#outcomes), so [handle both cases](#handle-either-outcome).

## Who the prefix check affects

You have nothing to change if one of these is true:

- Claude Code, claude.ai, or Claude Managed Agents manages your conversation history.
- The Claude Agent SDK manages the history, and the system prompt you give the SDK stays the same.
- Your code follows [the three habits of an append-only integration](#prefix-check), and nothing rewrites its requests on the way.
- You call no [model with preserved thinking](#outcomes).

If your requests pass through a library, proxy, or gateway, [compare what it sends with what you sent](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md#find-the-change-details). If you run one, see [Libraries, proxies, and gateways](build-with-claude-preserved-thinking-change-tools-or-instructions.md#libraries-proxies-gateways) for what to pass through.

## What must stay the same, and why

Make your integration append-only. Three habits do it:

1.  Send each assistant turn back exactly as the API returned it, including thinking blocks whose text is empty.
2.  Build `system` and `tools` once for each conversation, and send that copy every time.
3.  Put every update in a new message at the end, and leave it there.

Each thinking block’s reasoning is about exactly what came before it: `system`, `tools`, and every earlier message. That content is the block’s *prefix*, and it’s what the [prefix check](#prefix-check-details) compares.

The prefix check is similar to prompt caching, except that a change makes the thinking after it invalid instead of only missing the cache.

Take an app that puts today’s date in its system prompt. At midnight the date changes, and so does the prefix of the thinking already in the conversation. That thinking becomes invalid, and the next request can fail. An append-only app keeps the system prompt as it was, and states the new date in [a message at the end](build-with-claude-preserved-thinking-change-tools-or-instructions.md#changing-context).

A change makes only the thinking that already follows it invalid. The thinking before it and the thinking Claude produces afterward stay valid.

## If your code changes the system prompt, tools, or history

| If your code… | What to do |
|:---|:---|
| Rebuilds the system prompt with the date, a mode, or instruction files | Stop changing `system`. [Append your own instructions as a system message](build-with-claude-preserved-thinking-change-tools-or-instructions.md#new-instructions), a `role: "system"` entry in `messages`, and [state new values in the newest turn](build-with-claude-preserved-thinking-change-tools-or-instructions.md#changing-context). For text that other people can edit, see [Text that other people can edit](build-with-claude-preserved-thinking-change-tools-or-instructions.md#untrusted-text) instead. |
| Adds, removes, or rewords a tool, or gains tools when an MCP server connects | Stop changing `tools`, and [add or remove tools in a system message](build-with-claude-preserved-thinking-change-tools-or-instructions.md#tool-changes). |
| Trims, collapses, or summarizes older turns, and keeps the latest ones unchanged | [Let the API write the summary, or remove the kept turns’ thinking](build-with-claude-preserved-thinking-change-tools-or-instructions.md#server-side-trimming). |

Other causes, such as skipping thinking blocks whose text is empty or rebuilding a saved conversation, have fixes of their own: see [Change tools or instructions without failing the prefix check](build-with-claude-preserved-thinking-change-tools-or-instructions.md). To find yours, [have an agent check your code](build-with-claude-preserved-thinking.md#hand-to-an-agent).

## What each model does when the prefix check fails

On the Claude API and [some cloud platforms](build-with-claude-preserved-thinking.md#feature-availability), the result of failing the prefix check with [`prefix_mismatch_behavior`](#preserved-thinking-controls) unset depends on the model:

| Model with preserved thinking | Result                                    |
|:------------------------------|:------------------------------------------|
| Claude Fable 5.2              | 400 error                                 |
| Claude Mythos 5.2             | 400 error                                 |
| Claude Mythos 5.1             | 400 error                                 |
| Claude Fable 5.1              | [Possible 400 error](#possible-400-error) |
| Claude Opus 5.5               | [Possible 400 error](#possible-400-error) |
| Claude Sonnet 5.5             | [Possible 400 error](#possible-400-error) |
| Claude Haiku 5.5              | [Possible 400 error](#possible-400-error) |

Where the table says “Possible 400 error,” there are two cases: a request that fails the prefix check might get a 400 error or no error. When no error is returned, the failing blocks reach the model. Claude reads them like any other input, you’re billed for them, and Claude works from reasoning about content that has since changed.

On those models, you can [check which case a request gets](#check-which-case), but [handle both cases](#handle-either-outcome).



Code that follows [the three habits of an append-only integration](#prefix-check) doesn’t cause prefix check failures.

[Message Batches items](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md#batches) that leave `prefix_mismatch_behavior` unset get no error, and the API can drop the failing blocks.

## Handle both cases

For one result on every request, make your integration append-only or set `prefix_mismatch_behavior`. Otherwise, your code must handle both behaviors.

- **Append-only:** with [the three habits](#prefix-check), your code doesn’t make a request fail the prefix check.
- **The setting:** with `"error"` on every request, each failure is a 400 error, and you [catch it in code](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md#handle-the-error-in-code).
- **Both behaviors:** if you leave the setting unset, catch the 400 error, and [watch for failing thinking that reached Claude](#watch-production-traffic).

After a 400 error, send `"drop_block"` on that conversation’s later requests to recover. It has a cost: see [What dropping thinking costs](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md#drop-block-cost). Don’t send it on all your conversations to hide errors.

## Technical details

### How the prefix check works

The models with preserved thinking record a fingerprint of each thinking block’s prefix in its `signature`. The API reference calls the prefix check the conversation check, and the 400 error says that a failing block `is bound to a different conversation`.

### Which models run the prefix check

The prefix check runs on the Claude API and on [some cloud platforms](build-with-claude-preserved-thinking.md#feature-availability). It checks thinking blocks that a [model with preserved thinking](#outcomes) produced, on requests to one of those models. On the Claude API, other models, such as Claude Opus 5, don’t run it, and it doesn’t cover their blocks.

### What counts as a change

- **Each block is checked against its own record.** The API compares what’s before a block in this request with what its signature recorded when Claude produced it. Your last request plays no part. The prefix check looks only at content, not at sessions, IDs, or users. The same content in a new request or a fork passes it.
- **The prefix check compares what you sent, not what Claude read.** [Compaction at a token threshold](build-with-claude-compaction-threshold.md) and context editing change only what Claude reads, so they never count. After a threshold compaction block, the API compares only the messages from that block on, plus `system` and `tools`. On-demand compaction has its own conditions: see [Conditions for kept thinking to stay valid](build-with-claude-compaction-thinking-blocks.md#conditions-for-kept-thinking-to-stay-valid). For a file sent by URL and, on the Claude API, [an MCP tool list](../Agents-Tools/agents-and-tools-mcp-connector.md#pin-mcp-tool-list), the API compares what it fetched instead.
- **The thinking you send must be an unbroken run.** Thinking blocks aren’t compared as content. But each one you send, apart from the first, must have the same previous thinking block as when Claude produced it. So you can [leave out the oldest, the newest, or all of them](build-with-claude-preserved-thinking-change-tools-or-instructions.md#leave-out-thinking), but not one in between.

A change can be as small as one word of a tool description. Changing, inserting, moving, or deleting an earlier message counts, whatever its role. So does changing text before a thinking block in its own message.

### What doesn’t count

| This doesn’t count | Because |
|:---|:---|
| `model`, `effort`, `max_tokens`, `tool_choice`, `metadata`, `thinking.display`, and other parameters | Only `system`, `tools`, and messages are compared |
| JSON formatting or key order | The API compares parsed JSON, not its text |
| `cache_control` markers | They say where to cache, and aren’t content that Claude reads |
| A tool with `defer_loading: true` that nothing has referred to | It isn’t in Claude’s context until something refers to it |

### Set `prefix_mismatch_behavior`

The [beta header](../Endpoints/beta-headers.md#beta-features-on-other-platforms) `thinking-binding-controls-2026-08-01` adds the setting `thinking.block_binding.prefix_mismatch_behavior` and the response’s `input_transformations` array.

| Value | If a block fails the prefix check |
|:---|:---|
| `"error"` | The API rejects the request with a 400 error that names the first invalid block |
| `"drop_block"` | The API drops the invalid blocks, and the request succeeds. You aren’t billed for those blocks, but [dropping them can cost more](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md#drop-block-cost) |
| Not set, or `null` | [Depends on the model](#outcomes) |

Blocks that fail the prefix check stay invalid on every later request that sends them, while the change is in place. The setting acts on the one request that carries it. With thinking off (`"disabled"` or `"between_tools"`), sending it is a 400 error on every model.

The following request sets `prefix_mismatch_behavior` to `"drop_block"`. On a first turn there’s no thinking to send back, so `input_transformations` comes back empty:

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
    model="claude-opus-5-5",
    max_tokens=16000,
    thinking={
        "type": "adaptive",
        "block_binding": {"prefix_mismatch_behavior": "drop_block"},
    },
    messages=[
        {
            "role": "user",
            "content": "What is the greatest common divisor of 1071 and 462?",
        }
    ],
    betas=["thinking-binding-controls-2026-08-01"],
)

for block in response.content:
    if block.type == "text":
        print(block.text)

print(f"Input transformations: {len(response.input_transformations or [])}")
```

### Watch production traffic

With `prefix_mismatch_behavior` unset, a request that fails the prefix check might get no error on [some models](#outcomes). The thinking blocks that failed it then reach the model. To find those blocks in production traffic, send the `thinking-binding-controls-2026-08-01` beta header, leave the setting unset, and log each response’s `input_transformations` array. The header adds that array and doesn’t change what the model receives.

Each of those blocks gets its own `thinking_mismatch_allowed` entry in that array. One entry looks like this:

```python
{
  "input_transformations": [
    {
      "type": "thinking_mismatch_allowed",
      "path": "messages.1.content.0",
      "reason": "prefix_binding_mismatch"
    }
  ]
}
```



To find the change, see [Find what your code changed](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md#find-the-change).

### Check which case you get

On [some models](#outcomes), a request that fails the prefix check might get the 400 error or no error. This test shows which one a request gets:

1.  Take a conversation that holds a thinking block from one of those models. Change or add the system prompt (`system`). The block then fails the prefix check, because the system prompt changed after Claude produced the block.
2.  Send it to the same model with the `thinking-binding-controls-2026-08-01` beta header, and leave `prefix_mismatch_behavior` unset.

The response is one of these:

- **A [400 error](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md#prefix-mismatch-error) that says `bound to a different conversation`:** The request got the 400 error.
- **A 200 response whose `input_transformations` array has `thinking_mismatch_allowed` entries:** The request got no error. Each entry names a thinking block that failed the prefix check and reached Claude.
- **A 200 response whose `input_transformations` array is empty:** No block failed the prefix check, so the test shows nothing. Check that the conversation holds a thinking block from that model.

The result describes that one request and promises nothing about later ones, so write your code to [handle both cases](#handle-either-outcome).

## Next steps



[Change tools or instructions without failing the prefix check](build-with-claude-preserved-thinking-change-tools-or-instructions.md)

What to send instead of each change your code makes to a conversation.



[Fix a thinking block bound to a different conversation](build-with-claude-preserved-thinking-fix-bound-to-a-different-conversation.md)

Recover a failing conversation, find what your code changes, and test that it’s gone.



[Preserved thinking](build-with-claude-preserved-thinking.md)

What preserved thinking is, what a thinking block is tied to, and switching models or accounts.
