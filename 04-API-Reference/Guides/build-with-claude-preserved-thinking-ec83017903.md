---
title: "Preserved thinking - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/preserved-thinking"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:24Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fpreserved-thinking)





SearchCtrlK

First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)[Authentication](/docs/en/manage-claude/authentication)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

[Thinking](/docs/en/build-with-claude/thinking)

[Overview](/docs/en/build-with-claude/thinking)[Steering and cost control](/docs/en/build-with-claude/thinking-steering-and-cost)[Tool and multi-turn workflows](/docs/en/build-with-claude/thinking-tool-workflows)[Preserved thinking](/docs/en/build-with-claude/preserved-thinking)[Troubleshooting](/docs/en/build-with-claude/thinking-troubleshooting)[Extended thinking (legacy)](/docs/en/build-with-claude/extended-thinking)

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[Console](/)

[Messages](/docs/en/intro)Thinking

# Preserved thinking

Copy page



Preserved thinking lets a model use a thinking block from an earlier turn only if that model or an earlier one produced it and nothing before the block has changed.

Copy page



Preserved thinking is a property of newer Claude models that guards against distillation. It decides whether the model can use a thinking block that you send back from an earlier turn. Starting with Claude Fable 5.1, when a `thinking` or `redacted_thinking` block comes back in a request, the API checks the block's `signature` for two things:

- **The model can read the block.** Each model reads its own thinking blocks and those of a fixed set of other models. Claude Fable 5.1 reads blocks from Claude Opus 5 and, on the Claude API, from Claude Opus 5.5; neither Claude Opus 5 nor Claude Opus 5.5 reads blocks from Claude Fable 5.1. If the current model can't read a block, the API drops it from that request without an error. See [Switching models mid-conversation](#switching-models).
- **Nothing before the thinking block has changed.** The top-level `system` prompt, `tools`, and `messages` before the block are its prefix. If the prefix differs from what you sent when the block was produced, that block and every later thinking block are invalid, and the API rejects the request with a 400 error or drops the invalid blocks, whichever you choose. See [Keeping the prefix unchanged](#prefix-check).

The model check applies to every account. The API enforces the prefix check by default for accounts created on or after August 31, 2026, 00:00 UTC. On older accounts, it enforces the prefix check only on requests that set `thinking.block_binding.prefix_mismatch_behavior`. **Make your integration append-only regardless of your account's age**, so the same code works on every account, including newer accounts enforced by default.

## Who needs to change anything

Nothing changes for you if Claude Code, claude.ai, Claude Managed Agents, or the Claude Agent SDK builds your requests, or if your code keeps `system` and `tools` fixed for a session and only ever appends to `messages`. Claude Mythos 5.1 and models before Claude Fable 5.1 don't run the prefix check. If you never send thinking blocks back, the prefix check has nothing to reject, and the model gets none of its earlier reasoning.

Check your integration if, between two requests in one conversation, it does any of the following. Each item links to what to do instead:

- [Rebuilds the `system` prompt](#new-instructions): the date, a mode flag, re-read project instructions, or a plugin or MCP server that connects after the first turn
- [Re-renders the context in the first user message](#changing-context)
- [Clears or shortens old tool results, or re-encodes old images](#server-side-trimming)
- [Summarizes or drops old turns on the client](#custom-compaction-on-the-client) and keeps recent turns with their thinking
- [Adds, removes, or edits entries in `tools`](#tool-changes)
- [Adds a reminder to a user turn](#per-turn-reminders) and removes or rewrites it later
- [Drops some `thinking` blocks and keeps later ones](#append-assistant-turns-exactly-as-returned), or removes them and [later puts them back](#prefix-check)
- [Rebuilds a saved session from templates](#faq) instead of replaying what it sent

On an older account, none of these produces an error unless the request sets `prefix_mismatch_behavior`, so a run with no errors on your own key doesn't show whether your code is affected. If people run your tool with their own API keys, those on newer accounts get the 400 error before you do. To see what they see without changing how your requests behave, send the `thinking-binding-controls-2026-08-01` beta header. On an older account, each response then flags blocks that fail the check, and the model still reads them (see [Set the mismatch behavior and read `input_transformations`](#preserved-thinking-controls)).

## Switching models mid-conversation

Claude Fable 5.1 and Claude Mythos 5.1 read thinking blocks produced by each other and by earlier Claude models. No earlier model reads thinking blocks from Claude Fable 5.1 or Claude Mythos 5.1.

Claude Opus 5.5 reads thinking blocks from Claude Opus 5 and earlier Opus, Sonnet, and Haiku models, but not from Claude Fable or Claude Mythos models. On the Claude API, Claude Fable 5.1 and Claude Mythos 5.1 read thinking blocks from Claude Opus 5.5; no other model does. So a conversation that moves from Claude Opus 5 onto Claude Opus 5.5 keeps its reasoning, and so does one that moves from Claude Opus 5.5 up to Claude Fable 5.1 or Claude Mythos 5.1 on the Claude API. One that moves from Claude Fable 5.1 or Claude Mythos 5.1 to Claude Opus 5.5, or from Claude Opus 5.5 to any model other than those two, runs the turns after the switch without the previous model's reasoning. The blocks are dropped, not rejected, as described below.

- **A conversation that moves to Claude Fable 5.1 from an earlier model, or from Claude Opus 5.5 on the Claude API, keeps its reasoning.** The earlier model's thinking blocks stay readable, so the model thinks as usual from the first turn after the switch.
- **A conversation that moves down to an earlier model loses Claude Fable 5.1's reasoning for that request.** This happens when a router sends a turn to a cheaper model, after a [classifier refusal fallback](/docs/en/build-with-claude/refusals-and-fallback), or during a [server-side fallback](/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback). The API removes the unreadable blocks before the prompt reaches the model. They aren't billed and don't count toward `input_tokens`.

Keep sending the full history on every request, thinking blocks included, and let the API drop what the current model can't read. The API never edits your `messages` array, so the dropped blocks stay in your history. When the same history goes back to Claude Fable 5.1, its blocks are readable again, along with the earlier model's thinking. The reasoning is lost for good only if your client removes the blocks itself, for example a harness that strips thinking on a model switch or rebuilds the history from what each model used.

With the `thinking-binding-controls-2026-08-01` [beta header](/docs/en/api/beta-headers), the response lists each dropped block in a top-level `input_transformations` array with `reason: "model_binding_mismatch"`:

```python
{
  "input_transformations": [
    {
      "type": "thinking_dropped",
      "path": "messages.3.content.0",
      "reason": "model_binding_mismatch"
    }
  ]
}
```



Without the header, the drop is silent. This entry isn't a bug in your integration, and `prefix_mismatch_behavior` has no effect on it: a block the current model can't read is always dropped.

## Keeping the prefix unchanged

On Claude Fable 5.1 and Claude Opus 5.5, a thinking block stays valid only while everything you sent before it is unchanged on later requests. The checked prefix has three parts:

- The top-level `system` prompt
- The set of `tools`
- Every `message` before the block

Note: With server-side [compaction](/docs/en/build-with-claude/compaction), the checked prefix starts at the most recent compaction block.

Request parameters outside those three fields, such as `effort`, `max_tokens`, `output_config`, `tool_choice`, and `metadata`, aren't part of the prefix check, and neither are `cache_control` markers. [What counts as an edit](#what-counts-as-an-edit) has the full list.

Earlier thinking blocks aren't in the prefix, but each thinking block records which thinking block came before it, across turns. You can remove thinking blocks from the start of the history (oldest first), from the end, or all of them. What fails is a gap: the thinking blocks you keep must be an unbroken run of the original sequence, so removing one from the middle invalidates the thinking blocks after it. Once you remove a block, leave it out. Putting it back invalidates the thinking blocks produced while it was gone.

Keep `system` and `tools` fixed for the session and treat `messages` as append-only. The same discipline keeps the prefix stable for [prompt caching](/docs/en/build-with-claude/prompt-caching): the edits that invalidate thinking are the edits that restart the cache.

### What the API does with an invalid block

You choose with `thinking.block_binding.prefix_mismatch_behavior`:

- **`"error"` (the default):** the API rejects the request with a 400 `invalid_request_error` that names the first failing block.
- **`"drop_block"`:** the API drops each failing block and every thinking block after it, and the request succeeds. Dropped blocks aren't billed. The model answers that turn without using reasoning from dropped blocks, and the prompt cache restarts at the edit. The response lists each dropped block in `input_transformations` (on the `message_start` event when streaming) with `reason: "prefix_binding_mismatch"`.



`"drop_block"` hides the error but doesn't fix the edit that caused it. Dropped blocks aren't billed, but a session's token usage might still increase because Claude can sometimes think more to re-create the dropped thinking. The increase tends to be larger when more thinking blocks are dropped, or when blocks are dropped on more turns of a long session.

Count the responses in each session whose `input_transformations` has a `prefix_binding_mismatch` entry, alert on them, and replace each edit with the matching pattern in [Make changes without editing the prefix](#replace-prefix-edits). In the Message Batches API, an item that leaves the field unset doesn't fail. Where the API enforces the check by default, it drops the failing blocks instead. Set `"error"` explicitly there if you want batch items to fail.

Both the field and the `input_transformations` array require the `thinking-binding-controls-2026-08-01` [beta header](/docs/en/api/beta-headers). [Set the mismatch behavior and read `input_transformations`](#preserved-thinking-controls) shows the request in each SDK.

The 400 message begins:

``` block
messages.1.content.0: Invalid `signature` in `thinking` block. The block is bound to a different conversation. Remove the block, or set `thinking.block_binding.prefix_mismatch_behavior` to "drop_block".
```



If the request didn't send the beta header, the message continues:

```python
That setting requires the `thinking-binding-controls-2026-08-01` value in the `anthropic-beta` header.
```



It usually ends with a sentence naming what changed, for example that the `system` prompt or the `tools` list differs from when the block was created. [Troubleshooting thinking](/docs/en/build-with-claude/thinking-troubleshooting#error-thinking-block-signature) describes what that sentence can name.

A tampered or undecryptable signature is a different failure. It always returns a 400 (`` Invalid `signature` in `thinking` block `` with no sentence about the conversation), and `prefix_mismatch_behavior` doesn't apply to it.

#### Handle the error in code

This is the 400 `invalid_request_error` shown earlier in this section. Don't resend the same body: it fails the same way every time. Retry once with the beta header and `prefix_mismatch_behavior: "drop_block"`, and store that choice with the session so every later request sends it too, including after a restart. If you can't send the beta header, remove every `thinking` and `redacted_thinking` block from the history once, leave them out, and continue. Then fix the edit that caused the mismatch.

### Set the mismatch behavior and read `input_transformations`

The `thinking-binding-controls-2026-08-01` [beta header](/docs/en/api/beta-headers) adds:

- A top-level `input_transformations` array on every response
- A `block_binding` object on the `thinking` configuration, whose one field is `prefix_mismatch_behavior`

`block_binding` is accepted alongside `thinking.type: "adaptive"` and `thinking.type: "enabled"`. Sending it without the beta header returns a 400 error whose message ends `block_binding: Extra inputs are not permitted`. Models that don't run the prefix check accept the object and report only model-check drops, so one request body works across models. The API reference calls the prefix check the conversation check.

The following request opts into dropping rather than rejecting. On a first turn there's nothing to replay, so `input_transformations` comes back empty:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-fable-5-1",
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

Output



``` block
The greatest common divisor of 1071 and 462 is 21.
Input transformations: 0
```

Under the beta header, every response from a thinking-capable model carries `input_transformations`. Each entry names one thinking block by its `path` (for example `messages.1.content.0`) and gives a `reason`. There are two entry types:

- **`thinking_dropped`:** the API drops the block before the model reads it, and the block isn't billed. The `reason` is `prefix_binding_mismatch` or `model_binding_mismatch` (see [Switching models mid-conversation](#switching-models)).
- **`thinking_mismatch_allowed`:** the block fails the prefix check, but the API doesn't enforce that check for this request, so the block reaches the model unchanged and is billed. The `reason` is always `prefix_binding_mismatch`. This entry appears only on requests where the API doesn't enforce the check by default, such as those from an older account (see [When the API enforces the check](#enforcement)). Setting `prefix_mismatch_behavior` to either value opts the request into enforcement, so a request that sets it never gets this entry.

The array is empty when no block was dropped and none failed the prefix check. Ignore entries whose `type` or `reason` you don't recognize, because later checks add values.

When [streaming](/docs/en/build-with-claude/streaming), the array arrives on the `message` object in the `message_start` event. After a mid-stream server-side fallback, the final `message_delta` event carries it again with the serving model's entries. In a [message batch](/docs/en/build-with-claude/batch-processing), an item whose block fails the prefix check under an explicit `"error"` resolves as `errored`. An item that leaves the field unset doesn't fail. Where the API enforces the check by default, it drops the failing blocks instead. The [token counting](/docs/en/build-with-claude/token-counting) endpoint runs the same prefix check and returns the same 400.

### When the API enforces the check

The API enforces the prefix check on Claude Fable 5.1 and Claude Opus 5.5 for new accounts.

- **Accounts created on or after August 31, 2026, 00:00 UTC:** the API checks Claude Fable 5.1 and Claude Opus 5.5 requests and applies `"error"` unless you set `"drop_block"`. The same definition of a new account applies to the Claude API and to cloud platforms.
- **Older accounts:** the API enforces the check only on requests that set `prefix_mismatch_behavior`. Setting the field opts a request in, so you can see what a new account sees without creating one. On requests that leave it unset, the API still runs the check but lets failing blocks through to the model. With the beta header, the response lists each one in `input_transformations` as `thinking_mismatch_allowed`, so you can find prefix edits without changing what the model receives.

To find out which group your account is in, take a Claude Fable 5.1 conversation that contains a thinking block, change something before that block, and send it to Claude Fable 5.1 without the beta header or the `block_binding` field. A 400 response that names the header means your account is enforced by default. A 200 response means it isn't. To confirm, send the same request again with the beta header, still without `block_binding`: the response lists every thinking block after your edit in `input_transformations` as `thinking_mismatch_allowed`.

### What counts as an edit

Each row compares two consecutive requests:

| Change between requests                                                                                                                                                    | Later thinking blocks                                                                                                                                                                                                                                                                              |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Append messages at the end                                                                                                                                                 | Valid                                                                                                                                                                                                                                                                                              |
| Add a tool with `defer_loading: true` that nothing has referenced yet                                                                                                      | Valid                                                                                                                                                                                                                                                                                              |
| Remove `thinking` blocks from the start of the history, from the end, or all of them                                                                                       | Valid (the model loses that reasoning)                                                                                                                                                                                                                                                             |
| Change any request parameter outside `system`, `tools`, and `messages` (`effort`, `max_tokens`, `output_config`, `tool_choice`, `metadata`, `thinking.display`, and so on) | Valid                                                                                                                                                                                                                                                                                              |
| Add, move, or remove `cache_control` markers                                                                                                                               | Valid                                                                                                                                                                                                                                                                                              |
| A rotating signed URL that returns the same bytes                                                                                                                          | Valid                                                                                                                                                                                                                                                                                              |
| Server-side compaction or context editing removes or replaces content                                                                                                      | Valid (the check compares what you sent, not the server's edited copy)                                                                                                                                                                                                                             |
| A cleared [turn-scoped system message](#per-turn-reminders) left in place                                                                                                  | Valid                                                                                                                                                                                                                                                                                              |
| Edit, reorder, or delete any earlier `user`, `assistant`, or `system` message                                                                                              | Invalid, except when the signed block from [on-demand compaction](/docs/en/build-with-claude/compaction-on-demand) replaces the messages it summarizes, under the [conditions for kept thinking](/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid) |
| Re-render the context you put in the first user message with a changed value                                                                                               | Invalid for every thinking block                                                                                                                                                                                                                                                                   |
| Clear or shorten an earlier `tool_result`, re-encode an earlier image, or change an earlier `tool_use` input                                                               | Invalid for every later thinking block                                                                                                                                                                                                                                                             |
| Add a text block to an earlier user turn, or remove one you added last time                                                                                                | Invalid                                                                                                                                                                                                                                                                                            |
| Change the top-level `system` string or blocks                                                                                                                             | Invalid                                                                                                                                                                                                                                                                                            |
| Add, remove, rename, or edit a tool in `tools`                                                                                                                             | Invalid                                                                                                                                                                                                                                                                                            |
| Remove a `thinking` block from the middle of the history and keep later ones                                                                                               | Invalid for every later thinking block                                                                                                                                                                                                                                                             |
| Put back a `thinking` block you removed on an earlier request                                                                                                              | Invalid for thinking blocks produced while it was gone                                                                                                                                                                                                                                             |
| An image or document URL that returns different bytes on the next request                                                                                                  | Invalid                                                                                                                                                                                                                                                                                            |
| The same turn-scoped message deleted or reworded on a later request                                                                                                        | Invalid                                                                                                                                                                                                                                                                                            |

### Check whether your code edits the prefix

First, diff what you send. Capture the request bodies your integration sends over a few normal turns, including a compaction or a tool change. For each pair of consecutive requests, compare `system`, `tools`, and the `messages` they share. They should be identical up to the newly appended turns.

Then confirm against the API. Add the `thinking-binding-controls-2026-08-01` beta header, set `prefix_mismatch_behavior` to `"drop_block"`, and run a normal multi-turn session through your integration on claude-fable-5-1. The following example runs two turns the way your integration should: `messages` only grows, each assistant turn goes back exactly as the API returned it, `thinking` blocks included, and `block_binding` is set on every request. After each turn it prints the number of `thinking` blocks in the response and the number of dropped blocks:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

user_turns = [
    "How many positive integers below 500 have exactly 6 positive divisors?",
    "How many of those are odd?",
]

# messages grows across turns: each assistant turn goes back exactly as returned
messages = []
for user_turn in user_turns:
    messages.append({"role": "user", "content": user_turn})
    response = client.beta.messages.create(
        model="claude-fable-5-1",
        max_tokens=16000,
        thinking={
            "type": "adaptive",
            "block_binding": {"prefix_mismatch_behavior": "drop_block"},
        },
        messages=messages,
        betas=["thinking-binding-controls-2026-08-01"],
    )
    messages.append({"role": "assistant", "content": response.content})
    thinking_blocks = sum(block.type == "thinking" for block in response.content)
    dropped = len(response.input_transformations or [])
    print(f"thinking blocks: {thinking_blocks}, dropped: {dropped}")
```

Output



``` block
thinking blocks: 1, dropped: 0
thinking blocks: 1, dropped: 0
```

Neither turn drops a block because nothing earlier changed. Check that the first response contains a `thinking` block. With adaptive thinking, some responses have none. If no response in the session has one, there is nothing to check and the dropped count is 0 whatever you change, so run the example again.

Log `input_transformations` on every turn of your own integration. When the API drops a block, the entry looks like the following:

```python
{
  "input_transformations": [
    {
      "type": "thinking_dropped",
      "path": "messages.1.content.0",
      "reason": "prefix_binding_mismatch"
    }
  ]
}
```



- **Empty on every turn of a session that contains `thinking` blocks:** your integration keeps the prefix intact.
- **`reason: "prefix_binding_mismatch"`:** something before the block at `path` changed since the previous request. Diff `system`, `tools`, and `messages` up to that turn to find it, or resend the request with `"error"`: the 400 usually ends with a sentence naming what changed. Then find the matching replacement in [Make changes without editing the prefix](#replace-prefix-edits).
- **`reason: "model_binding_mismatch"`:** the conversation moved to a model that can't read the earlier model's blocks. This isn't a prefix edit. See [Switching models mid-conversation](#switching-models).

To see a failure on purpose, send a third turn from the earlier example and add a `system` prompt to that request only, so that it differs from the first two requests, which had none. With `"drop_block"`, the dropped count is no longer 0: the response has one entry for each thinking block in the history, each with `reason: "prefix_binding_mismatch"`. With `"error"`, the request returns the 400 described in [What the API does with an invalid block](#mismatch-behavior), and its last sentence names the `system` prompt. In the cURL and CLI tabs, remove the `jq` filter to see the error body. If the count is still 0, there was nothing to check: confirm that the model is claude-fable-5-1, that the request sets `block_binding`, that the history you sent contains `thinking` blocks, and that the first two requests had no `system` prompt.

Two plain turns rarely show the problem. Run a session through each of the following, with `"error"` set so that a regression fails your CI:

- The first client-side compaction or trim
- A tool, plugin, or MCP server that connects after the first turn
- A mode or instruction change
- A long tool loop, if you add reminders or shorten old tool results
- A switch to another model and back
- A save, a restart, and a resume on a later date

On an older account, you can also watch production traffic without opting into enforcement: send the beta header, leave `block_binding` out, and log `input_transformations`. Sending the header alone doesn't change what the model receives. Every thinking block that comes after the content you edited fails the check and gets its own `thinking_mismatch_allowed` entry, with the same `path` and `reason` fields as a `thinking_dropped` entry. Blocks before the edit still pass. An edit to `system` or `tools` comes before every block, so it fails every thinking block in the request. One entry looks like this:

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

Run the following example from an [older account](#enforcement), because a newer account rejects its third request with the 400. It sends the header without `block_binding` and extends the earlier session with a third request that adds a system prompt, which changes the prefix on purpose. After each turn it prints the number of `thinking` blocks and flagged blocks:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

user_turns = [
    "How many positive integers below 500 have exactly 6 positive divisors?",
    "How many of those are odd?",
    "And how many of the odd ones are below 100?",
]

# messages grows across turns: each assistant turn goes back exactly as returned
messages = []
for turn, user_turn in enumerate(user_turns, start=1):
    messages.append({"role": "user", "content": user_turn})
    response = client.beta.messages.create(
        model="claude-fable-5-1",
        max_tokens=16000,
        thinking={"type": "adaptive"},
        # Only the last request adds a system prompt, which changes the prefix on purpose
        system="Answer briefly." if turn == len(user_turns) else anthropic.omit,
        messages=messages,
        betas=["thinking-binding-controls-2026-08-01"],
    )
    messages.append({"role": "assistant", "content": response.content})
    thinking_blocks = sum(block.type == "thinking" for block in response.content)
    flagged = sum(
        transformation.type == "thinking_mismatch_allowed"
        for transformation in response.input_transformations or []
    )
    print(f"thinking blocks: {thinking_blocks}, flagged: {flagged}")
```

Output



``` block
thinking blocks: 1, flagged: 0
thinking blocks: 1, flagged: 0
thinking blocks: 1, flagged: 2
```

The third response flags every thinking block from the earlier turns, one per turn in this run, because the new system prompt comes before all of them. The model still read them.

Handle these entries as you would `prefix_binding_mismatch` drops. The edit is before the first block listed: diff `system`, `tools`, and `messages` up to that block's `path` against the previous request to find it, then replace it with the matching pattern in [Make changes without editing the prefix](#replace-prefix-edits). On a new account, or on any request that sets `prefix_mismatch_behavior`, the API instead rejects the request or drops the failing blocks. The entries are a lower bound on what enforcement would remove: with `"drop_block"`, a failing block also takes the rest of that turn's thinking blocks with it, and removing one block can make the next one fail too. When the API only records the check, it judges each block on its own and lists a block only if that block fails.

## Make changes without editing the prefix

Each common prefix edit has a replacement that gives the model the same information and leaves earlier bytes unchanged, so later thinking stays valid. Find the edit your code makes today in the first column:

| Instead of                                                                                                            | Use                                                                                                                                                                                                                                                                                        | Beta header                                                                                                                                                                                                                                                  |
|:----------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rebuilding the top-level `system` prompt                                                                              | A [mid-conversation system message](#new-instructions)                                                                                                                                                                                                                                     | None                                                                                                                                                                                                                                                         |
| Re-rendering the context in your first user message (environment, date, memory, project instructions) on each request | Render it once and resend it unchanged. When something changes, [put the new version in the newest turn](#changing-context)                                                                                                                                                                | None                                                                                                                                                                                                                                                         |
| Clearing or shortening old `tool_result` content, or re-encoding old images, in place                                 | Shorten a tool result or downscale an image before the first time you send it, not after. To clear old results later, [trim context on the server](#server-side-trimming) with `clear_tool_uses_20250919`                                                                                  | `context-management-2025-06-27`                                                                                                                                                                                                                              |
| Injecting a reminder and deleting it on the next request                                                              | A [turn-scoped system message](#per-turn-reminders) (`clear_at: "next_user_message"`)                                                                                                                                                                                                      | `mid-conversation-system-clear-at-2026-08-21`                                                                                                                                                                                                                |
| Adding or removing entries in `tools`                                                                                 | [`tool_addition` and `tool_removal` blocks](#tool-changes)                                                                                                                                                                                                                                 | `inline-tools-2026-09-15` (add `mcp-client-2026-09-15` when the tool comes from an MCP server connected through the MCP connector), or the older `mid-conversation-tool-changes-2026-07-01`, which works on the Claude API, Amazon Bedrock, and Google Cloud |
| Changing top-level `output_config.effort` (restarts the cache, doesn't affect thinking)                               | A [per-message `output_config`](#effort-changes)                                                                                                                                                                                                                                           | `mid-conversation-output-config-2026-07-01`                                                                                                                                                                                                                  |
| Dropping or summarizing old turns on the client                                                                       | [On-demand compaction](/docs/en/build-with-claude/compaction-on-demand) to keep the recent turns with their thinking, other server-side [compaction or context editing](#server-side-trimming), or [client-side compaction](#custom-compaction-on-the-client) that keeps no stale thinking | `compact-2026-09-04`                                                                                                                                                                                                                                         |
| An image or document URL whose bytes change between requests                                                          | A [`file_id` from the Files API](#files-by-id), or base64                                                                                                                                                                                                                                  | None                                                                                                                                                                                                                                                         |

All of these assume you [send assistant turns back exactly as returned](#append-assistant-turns-exactly-as-returned). Mid-conversation system messages, turn-scoped system messages, and tool changes aren't available on every model: [Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages) lists the models that accept them. If your code serves several models, keep editing the top-level `system` prompt for the models that don't accept them.

To use several betas in one request, combine the values in one `anthropic-beta` header. Beta names are the same on Amazon Bedrock and Google Cloud wherever the beta is available there (see [Beta headers](/docs/en/api/beta-headers)):

``` block
anthropic-beta: thinking-binding-controls-2026-08-01,mid-conversation-system-clear-at-2026-08-21,inline-tools-2026-09-15
```



### Send assistant turns back exactly as returned

Store the `content` array from each response and send it back unchanged as the assistant turn: every block type, in the order received, including `thinking` blocks whose `thinking` field is empty. A serializer that drops unknown block types, drops empty fields, or reorders blocks edits the prefix for every later turn.

On Claude Fable 5.1, the `thinking` field is empty by default and the `signature` carries the reasoning, so a serializer that skips empty blocks removes thinking. If it removes all of them, nothing fails and the model loses its earlier reasoning on every turn. If you parse the stream yourself, keep the block even when no thinking text arrives: it opens, receives its `signature` in a `signature_delta` event, and closes. A block sent back with an empty `signature` fails.

### Add instructions with a mid-conversation system message

Some harnesses rebuild the top-level `system` prompt on each request to carry the current time, a token budget, a mode flag, or newly discovered project context. That invalidates every thinking block in the conversation. Instead, freeze `system` at session start. When something changes, append a [`role: "system"` message](/docs/en/build-with-claude/mid-conversation-system-messages) at the point in `messages` where the change becomes true:

```python
{
  "role": "system",
  "content": "The user switched the workspace to read-only mode. Do not write files until told otherwise."
}
```



The model treats this message with system-prompt authority, and everything before it stays unchanged. In a tool loop, place the message after the `tool_result` user message, never between an assistant `tool_use` and its `tool_result` (see [Limitations](/docs/en/build-with-claude/mid-conversation-system-messages#limitations)). Once sent, the message is part of the prefix for later thinking: leave it in place on later requests.

### Put changing context in the newest turn

Some harnesses put an environment block in the first user message (working directory, branch, date, memory, project instructions) and render it again on every request. When any value changes, `messages[0]` changes, and every thinking block in the conversation is invalid. Render that block once and resend it as it was. When a value changes, say so in the newest turn: add a text block to the user message you are about to send, or append a [mid-conversation system message](#new-instructions) if the change comes from you as the operator.

```python
{
  "role": "user",
  "content": [
    {
      "type": "text",
      "text": "Environment update: the current branch is now release-2."
    },
    { "type": "text", "text": "Run the tests again." }
  ]
}
```



Once sent, that text block is part of the prefix for later thinking: leave it in place on later requests.

### Send per-turn reminders as turn-scoped system messages

A common prefix edit is the per-turn nudge: a line such as "request independent reads together" or "you haven't updated the user in a while" that your code appends after each batch of tool results. To keep reminders from piling up, send each nudge as a [mid-conversation system message](/docs/en/build-with-claude/mid-conversation-system-messages) with `clear_at: "next_user_message"`, placed after the `tool_result` user message. `clear_at` requires the beta header `mid-conversation-system-clear-at-2026-08-21`. The following `messages` array is the request after two tool calls and their results. `messages[3]` is the previous request's nudge, left in place, and `messages[6]` is this request's copy:

```python
[
  { "role": "user", "content": "Fix the failing test." },
  {
    "role": "assistant",
    "content": [
      { "type": "thinking", "thinking": "", "signature": "..." },
      {
        "type": "tool_use",
        "id": "toolu_01",
        "name": "read_file",
        "input": { "path": "tests/test_auth.py" }
      }
    ]
  },
  {
    "role": "user",
    "content": [{ "type": "tool_result", "tool_use_id": "toolu_01", "content": "..." }]
  },
  {
    "role": "system",
    "clear_at": "next_user_message",
    "content": "Request every independent read in one turn."
  },
  {
    "role": "assistant",
    "content": [
      { "type": "thinking", "thinking": "", "signature": "..." },
      {
        "type": "tool_use",
        "id": "toolu_02",
        "name": "read_file",
        "input": { "path": "src/auth.py" }
      }
    ]
  },
  {
    "role": "user",
    "content": [{ "type": "tool_result", "tool_use_id": "toolu_02", "content": "..." }]
  },
  {
    "role": "system",
    "clear_at": "next_user_message",
    "content": "Request every independent read in one turn."
  }
]
```



A user message that contains only `tool_result` blocks counts as the "next user message", so `messages[3]` is already cleared. It adds nothing to what the model sees and costs no input tokens, but because it's still in the array, the thinking in `messages[4]` stays valid. `messages[6]` is the copy the model sees this turn. On later requests, keep both where they are and append a fresh copy after the next `tool_result` message.

### Add or remove tools with `tool_addition` and `tool_removal`

Editing the `tools` array mid-session invalidates preserved thinking blocks. Leave the array as you first sent it, and change which tools the model can use by appending a `role: "system"` message that carries `tool_addition` or `tool_removal` blocks. These are [mid-conversation tool changes](/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes) and need the beta header `inline-tools-2026-09-15`, which is available on the Claude API. The older `mid-conversation-tool-changes-2026-07-01` header still works for changes that name a tool by reference, on the Claude API, Amazon Bedrock, and Google Cloud.

You have two ways to use these blocks:

- **Declare every tool up front.** Put every tool the session might need in `tools` on the first request, with `defer_loading: true` on any the model shouldn't see yet. Then turn tools on and off with `tool_addition` and `tool_removal` blocks that name them.
- **Start with a snapshot and add tools as you go.** Put the tools you know about in `tools` on the first request. When a new tool comes along, define it inside a `tool_addition` block instead of editing `tools`.

Either way, `tools` never changes, so earlier thinking stays valid and the prompt cache still hits, with the one exception noted below.

For example, to withdraw a dangerous tool after a mode switch:

```python
{
  "role": "system",
  "content": [
    { "type": "tool_removal", "tool": { "type": "tool_reference", "name": "delete_branch" } },
    { "type": "text", "text": "Branch deletion is disabled for the rest of this session." }
  ]
}
```



To turn on a tool you declared with `defer_loading: true`, append a `tool_addition` block that names it:

```python
{
  "role": "system",
  "content": [
    { "type": "tool_addition", "tool": { "type": "tool_reference", "name": "deploy" } },
    { "type": "text", "text": "Authentication succeeded. Deployment is now available." }
  ]
}
```



Sometimes you can't declare a tool up front because you don't know its schema yet: a tool your application discovers at runtime, or an MCP server that connects after the first turn. Define it inside the `tool_addition` block instead of touching `tools`. With `inline-tools-2026-09-15`, the block's `tool` can be `{"type": "tool_definition", "definition": {...}}`, carrying the same entry you would have put in `tools`:

```python
{
  "role": "system",
  "content": [
    {
      "type": "tool_addition",
      "tool": {
        "type": "tool_definition",
        "definition": {
          "name": "db_query",
          "description": "Run a read-only SQL query against the analytics database.",
          "input_schema": {
            "type": "object",
            "properties": { "sql": { "type": "string" } },
            "required": ["sql"]
          }
        }
      }
    }
  ]
}
```



The new tool arrives in `messages`, `tools` never changes, and earlier thinking stays valid. Keep at least one tool without `defer_loading: true` in `tools`: if every tool there is deferred, the first tool you define this way costs one full prompt cache miss.

If the API connects to the MCP server for you through the [MCP connector](/docs/en/agents-and-tools/mcp-connector), also send `mcp-client-2026-09-15`. It covers everything `mcp-client-2025-11-20` does, so send it instead of that one. The block's `definition` can then be an `mcp_toolset` for a server listed in `mcp_servers`. When the API has to fetch a server's tool list, the response starts with an `mcp_tool_listing` block for that server. Send it back unchanged with the rest of the assistant turn, and keep sending `mcp-client-2026-09-15` on every later request that carries it. The block pins the toolset to that list, so the API doesn't contact the server again for it. These MCP connector features are available on the Claude API.

With only the older header, you can still append a tool you learn about mid-session to `tools` with `defer_loading: true`, then offer it with a `tool_addition` block. That's safe because the prefix check ignores a deferred tool until a `tool_addition` block references it. Adding a tool without `defer_loading: true` changes the prefix and invalidates earlier thinking.

The `role: "system"` messages that carry these blocks join the prefix for later thinking. Leave them in place on later requests.

### Change effort with a per-message `output_config`

Changing top-level `output_config.effort` between requests doesn't invalidate thinking, because effort isn't part of the prefix. Changing top-level effort does restart the prompt cache. On Claude Fable 5.1, use [per-message effort](/docs/en/build-with-claude/effort#change-effort-mid-conversation-beta) instead: append a `role: "system"` message with empty `content` and the new level. It needs the beta header `mid-conversation-output-config-2026-07-01`.

```python
{ "role": "system", "content": [], "output_config": { "effort": "low" } }
```



The new level takes effect from the next `user` turn. Once sent, the message is part of `messages` and therefore part of the prefix for later thinking: leave it in place on later requests, and append another one to change effort again.

### Trim context on the server

Another common prefix edit is client-side trimming: dropping or summarizing the oldest turns and keeping the recent ones verbatim. The kept turns' thinking blocks were produced while the removed history was still in place, so they fail the check. The server-side equivalents don't count as edits, because the check compares the conversation as you sent it:

- [On-demand compaction](/docs/en/build-with-claude/compaction-on-demand) (beta) returns the summary from a separate request, which can [run in the background](/docs/en/build-with-claude/compaction-background), and you send the returned block in place of the messages it summarizes. The check accepts that swap, so the turns you keep can stay valid with their thinking, under the [conditions for kept thinking](/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid). [Request a summary](/docs/en/build-with-claude/compaction-on-demand#request-a-summary) shows the request and names the beta header it needs.
- [Compaction at a token threshold](/docs/en/build-with-claude/compaction-threshold) summarizes older turns into a compaction block when the context approaches a threshold you set, and the checked prefix restarts from that block. Its [`instructions` parameter](/docs/en/build-with-claude/compaction-threshold#custom-summarization-instructions) takes your own summarization prompt, such as "preserve every ticker, position size, and stated assumption".
- [Context editing](/docs/en/build-with-claude/context-editing) clears old tool results or old thinking blocks by rule, oldest first. The strategies are `clear_tool_uses_20250919` and `clear_thinking_20251015`.

### Compact on the client

You can still compact on the client. If you write the summary yourself, don't send back a thinking block that was produced before the rewrite. If the API writes it with on-demand compaction, [Conditions for kept thinking to stay valid](/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid) lists when kept thinking stays valid.

#### Simple compaction (recommended)

When the conversation grows too long, summarize the whole session into one user message and send only that message plus the next instruction. Nothing earlier is replayed, so there's no thinking left to fail the check, and the model reasons afresh from the summary.

```python
[
  {
    "role": "user",
    "content": "<summary of the session so far>\n\n<the next instruction>"
  }
]
```



Claude models are trained on long-horizon tasks with this scheme and for most workloads it performs well.

#### Keep-tail compaction

Keep-tail compaction summarizes the older turns and keeps the most recent turns verbatim, so the model still sees the last few exchanges word for word. If you write the summary yourself, it breaks the rule: the kept assistant turns still carry thinking blocks that were produced when the original turns, not the summary, came before them. Those blocks fail.

To keep that thinking, have the API write the summary with on-demand compaction. [Compaction that keeps recent turns](/docs/en/build-with-claude/compaction-keep-recent-turns) shows how, and [Conditions for kept thinking to stay valid](/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid) lists when the kept thinking stays valid.

The rest of this section covers a summary you write yourself.

Fix: keep the turns exactly as they are and send `prefix_mismatch_behavior: "drop_block"`. The API drops the stale thinking blocks, the model reads the kept turns' `text` and `tool_use` blocks, and the request succeeds.

Pass the compacted history as `messages` and set `block_binding` on the `thinking` configuration. In the following example, `compacted_messages` is the array your compaction step produced: the summary message followed by the kept turns exactly as the API returned them, `thinking` blocks included:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
client = anthropic.Anthropic()

# compacted_messages: the summary message, then the kept turns as returned
response = client.beta.messages.create(
    model="claude-fable-5-1",
    max_tokens=16000,
    thinking={
        "type": "adaptive",
        "block_binding": {"prefix_mismatch_behavior": "drop_block"},
    },
    messages=compacted_messages,
    betas=["thinking-binding-controls-2026-08-01"],
)

print(response.input_transformations)
```

The response carries the new assistant turn as usual, plus one `input_transformations` entry per dropped block. For the history in the diagram, that's the thinking on assistant turns 3 and 4:

```python
{
  "input_transformations": [
    {
      "type": "thinking_dropped",
      "path": "messages.2.content.0",
      "reason": "prefix_binding_mismatch"
    },
    {
      "type": "thinking_dropped",
      "path": "messages.4.content.0",
      "reason": "prefix_binding_mismatch"
    }
  ]
}
```



Keep sending `"drop_block"` on later requests for as long as those two turns stay in the history. Thinking the model produces from this request onward follows the summary and stays valid. If you'd rather not depend on the beta header, the alternative is to strip the `thinking` and `redacted_thinking` blocks from the kept assistant turns yourself when you build the compacted history.

#### Background (async) compaction

Background compaction builds the summary off the critical path while the conversation continues, then swaps it in a few requests later. To keep the thinking produced in the meantime, have the API write the summary with on-demand compaction: [Compaction in the background](/docs/en/build-with-claude/compaction-background) has the steps, and that thinking stays valid under the same [conditions for kept thinking](/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid) as kept recent turns.

A summary you build yourself breaks the rule the same way keep-tail does, with a delay: every assistant turn produced while the summary was being built carries thinking that predates the swap, and it all fails the moment the summary lands. If you use one, treat the swap like keep-tail and send `"drop_block"` from the swap onward, or compact synchronously.

#### Patterns that don't work with preserved thinking

- **Cutting turns out of the middle.** Removing individual turns invalidates every thinking block after them, and no compaction scheme avoids that. If you were cutting a turn to change an instruction, append a [mid-conversation system message](#new-instructions) instead. To remove old tool results or old thinking selectively, use server-side [context editing](/docs/en/build-with-claude/context-editing).
- **Compacting in the middle of a tool round.** Don't compact between an assistant turn's `tool_use` and the `tool_result` that answers it. Send that assistant turn back with its thinking intact so the model finishes the round with its reasoning. See [Preserving thinking blocks](/docs/en/build-with-claude/thinking#preserving-thinking-blocks).

### Reference files by ID, not by a URL whose content changes

For an `image` or `document` block with a `url` source, the check covers the fetched bytes, not the URL string. A URL whose content changes invalidates later thinking: a "latest screenshot" endpoint, or a document someone edits between turns. A rotating signed URL for the same file doesn't. For content you reference across turns, upload it once with the [Files API](/docs/en/build-with-claude/files) and use the `file_id`, or send base64.

### Libraries, proxies, and gateways

A library, proxy, or gateway sits between someone else's history and the API, so its own rewrites count as edits, and its users can't see or fix them.

- **Pass through what you don't recognize.** Forward the caller's `anthropic-beta` values and `thinking.block_binding` unchanged, and return `input_transformations` to them. An options schema that rejects unknown keys stops your users from choosing `"drop_block"`.
- **Leave a `role: "system"` message where the caller put it.** Moving it into the top-level `system` field changes `system` on that request and invalidates every thinking block in the conversation.
- **To turn tool use off for a request, send `tool_choice: {"type": "none"}`.** Don't remove `tools`.
- **Don't hide the 400.** If your code catches it, strips thinking, and retries on the caller's behalf, log that it did: their history is still edited, and the model loses its earlier reasoning on every later request.

## FAQ

### Do I need a new account to test preserved thinking?

No. Send the `thinking-binding-controls-2026-08-01` beta header and set `thinking.block_binding.prefix_mismatch_behavior`. Setting the field opts that request into enforcement regardless of account age. `"error"` rejects an edited history with the same 400 a new account gets, and `"drop_block"` lets the request through and lists what was dropped in `input_transformations`. To find prefix edits from an older account without enforcing the check, send the header and leave the field unset: failing blocks still reach the model, and `input_transformations` lists them as `thinking_mismatch_allowed`. See [Check whether your code edits the prefix](#how-to-tell-whether-your-integration-is-impacted).

### If anything before a thinking block changes, even one tool description, is the conversation unusable?

No. What fails is the thinking already in the history after the point you changed, and you choose what happens to it. With `prefix_mismatch_behavior: "drop_block"`, the API drops those blocks and the request succeeds: the model answers that turn without that reasoning, and the prompt cache restarts at the edit. With the default `"error"`, the API rejects the request with a 400 until you undo the edit or resend with `"drop_block"`. See [What the API does with an invalid block](#mismatch-behavior). [What counts as an edit](#what-counts-as-an-edit) lists which changes matter.

### Does changing effort or other thinking settings between requests invalidate earlier thinking?

No. `output_config.effort`, `max_tokens`, and the `thinking` configuration aren't part of the checked prefix, which covers only `system`, `tools`, and `messages`. A top-level effort change invalidates most of the prompt cache. On Claude Fable 5.1, a [per-message effort](#effort-changes) change keeps the prompt cache and is used as the new effort level until changed again.

### My tool list changes mid-session. How do I avoid invalidating the conversation?

Don't edit `tools`. Declare the full set at session start, mark tools that aren't available yet with `defer_loading: true`, and offer or withdraw them with `tool_addition` and `tool_removal` blocks. If you learn a tool's schema only mid-session, define it inside the `tool_addition` block (`inline-tools-2026-09-15`, plus `mcp-client-2026-09-15` for a server the API's MCP connector reaches) and leave `tools` unchanged. The `role: "system"` messages that carry these blocks join the prefix for later thinking, so don't move, reword, or delete them afterward. See [Add or remove tools with `tool_addition` and `tool_removal`](#tool-changes).

### I compact by summarizing older turns and keeping recent turns verbatim. Does that still work?

Yes, if the API writes the summary. [On-demand compaction](/docs/en/build-with-claude/compaction-on-demand) (beta header `compact-2026-09-04`) summarizes the older turns into a signed block that you send in place of them. The recent turns keep their thinking under the [conditions for kept thinking](/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid).

If you write the summary yourself, the kept turns' thinking fails the check, because those blocks were produced against the history you replaced. Strip `thinking` and `redacted_thinking` blocks from the turns you carry across and keep their `text` and `tool_use` blocks, or send `prefix_mismatch_behavior: "drop_block"` and let the API drop them. Simple compaction leaves no thinking behind to fail and is the recommended approach: one summary message plus the next user turn, with no earlier turns replayed. Server-side [compaction](/docs/en/build-with-claude/compaction) and [context editing](/docs/en/build-with-claude/context-editing) don't count as edits. See [Compact on the client](#custom-compaction-on-the-client).

### How do I handle instruction files such as AGENTS.md or CLAUDE.md that change mid-session?

Load them once at session start and keep the top-level `system` prompt and `tools` fixed. When a file changes, append the new version at that point in `messages` instead of editing the original. Use a [mid-conversation system message](/docs/en/build-with-claude/mid-conversation-system-messages) for instructions that come from you as the operator. For file text you treat as untrusted, which shouldn't carry system-prompt authority, put the content in the next `user` turn instead. See [Add instructions with a mid-conversation system message](#new-instructions) and [Limitations](/docs/en/build-with-claude/mid-conversation-system-messages#limitations).

### Can I resume a saved session later, after a restart or the next day?

Yes. A resumed session is an ordinary follow-up request: `system`, `tools`, and the earlier `messages` must have the same content as what you last sent. JSON formatting and key order don't matter; the values do. Persist exactly what you sent and received, and replay that: the rendered system prompt, the tool definitions, and each assistant turn as returned. Don't re-render from inputs that might have changed since, such as the date, an updated instruction file, or a new tool version. Anything new goes in an appended message. See [Send assistant turns back exactly as returned](#append-assistant-turns-exactly-as-returned).

### A saved session now fails on every request. How do I get it working again?

The stored history has an edit in it, so replaying it can't succeed. Send that session with `prefix_mismatch_behavior: "drop_block"` from now on, or remove its `thinking` and `redacted_thinking` blocks once and continue. Thinking the model produces from that point on stays valid as long as nothing before it changes again. Then find the edit so that new sessions don't hit it. See [Handle the error in code](#handle-the-error-in-code).

### My harness can route a turn to a non-Claude model. Do those turns invalidate Claude's earlier thinking?

No, provided they're appended after the existing history and nothing earlier changes: an assistant message without thinking blocks is an appended message like any other. Send the other model's output as `text` and `tool_use` content.

### Can I carry a conversation's reasoning into a new conversation?

Not into a different conversation. A thinking block is usable only when it follows the exact `system`, `tools`, and `messages` it was produced from. A branch that replays that history unchanged up to the fork point keeps its thinking. A conversation that starts from anything else can't use it, so start that conversation from a summary of the task state, as in [simple compaction](#custom-compaction-on-the-client): the goal, decisions made, files and results so far, and the next step.

## Next steps



[Troubleshooting thinking](/docs/en/build-with-claude/thinking-troubleshooting)

Diagnose and fix the most common thinking failures: configuration 400 errors, empty or missing thinking blocks, max_tokens stops, and cache misses.



[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)

Change system instructions or tool availability partway through a conversation without invalidating the cached prefix that came before them.



[Compaction](/docs/en/build-with-claude/compaction)

Server-side context compaction for managing long conversations that approach context window limits.



[Prompt caching](/docs/en/build-with-claude/prompt-caching)

Cache prompt prefixes with `cache_control` to cut costs and latency, using automatic caching or explicit breakpoints with 5-minute or 1-hour TTLs.
