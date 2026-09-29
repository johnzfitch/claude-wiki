---
title: "Compaction and preserved thinking - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-22T06:31:44Z"
tags: ["api", "prompting"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcompaction-thinking-blocks)

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

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics (beta)](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

[Overview](/docs/en/build-with-claude/compaction)[Compact on demand](/docs/en/build-with-claude/compaction-on-demand)[Keep recent turns](/docs/en/build-with-claude/compaction-keep-recent-turns)[Compact in the background](/docs/en/build-with-claude/compaction-background)[Keep thinking blocks valid](/docs/en/build-with-claude/compaction-thinking-blocks)[Threshold compaction](/docs/en/build-with-claude/compaction-threshold)

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

[Messages](/docs/en/intro)Compaction

# Compaction and preserved thinking

Copy page



When thinking blocks in turns kept after on-demand compaction stay valid on models with preserved thinking, and how to check.

Copy page



Compaction and preserved thinking

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

compact-2026-09-04

Skip this page unless you send thinking blocks back to a model with [preserved thinking](/docs/en/build-with-claude/preserved-thinking) and keep turns after the compaction block. Kept turns are the turns that follow the block: recent turns you left out of the compaction request, as in [Compaction that keeps recent turns](/docs/en/build-with-claude/compaction-keep-recent-turns), or turns that arrived while the summary was being written, as in [Compaction in the background](/docs/en/build-with-claude/compaction-background).

Models with preserved thinking check earlier thinking blocks against the conversation that produced them. A summary replaces part of that conversation, but the check accepts the swap when the API wrote the summary, so the thinking in kept turns can stay valid.

## Conditions for kept thinking to stay valid

The thinking blocks in kept turns stay valid while all of these hold:

- **The compaction request runs on a model with preserved thinking.** This condition covers every compaction request since a thinking block was produced, not only the most recent one. One way to meet it is to send every compaction request to the model the conversation uses.
- **The kept turns directly follow the summarized messages, and you send them unchanged.** Send each kept message exactly as it is in your history. Don't skip or add a message between the last summarized message and the first kept one. The first kept message must also have a different role from the last summarized message, and it can't be a mid-conversation `role: "system"` message. Otherwise, the API merges it into the last summarized message. One way to get the first kept message right is to compact exactly the `messages` of a request you already sent. The kept turns then start with Claude's reply to it.
- **`system` and the `tools` not marked `defer_loading: true` don't change.** They are the same on the compaction request as on the requests that produced the kept thinking, and they stay the same on the requests that follow. [Change the system prompt or tools](#change-the-system-prompt-or-tools) covers how to change them safely.

If a condition doesn't hold, nothing fails when you compact, and the API accepts the block on later requests either way. The failure comes on the first later request that sends the kept thinking where the API enforces the check: a 400 error by default, or dropped thinking blocks if the request sets `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`. In the Message Batches API, an item that leaves the field unset doesn't fail. Where the check applies by default, the API drops the blocks instead. [What the API does with an invalid block](/docs/en/build-with-claude/preserved-thinking#mismatch-behavior) describes both outcomes, and [When the API enforces the check](/docs/en/build-with-claude/preserved-thinking#enforcement) says which requests are checked.

## Compact again without breaking older thinking

You can [compact again](/docs/en/build-with-claude/compaction-on-demand#compact-again) and keep turns: the new block covers the old summary and every message that follows it in the compaction request, and any turns you leave out of that request are kept turns of the new block.

The first of the [conditions for kept thinking](#conditions-for-kept-thinking-to-stay-valid) counts every compaction since a thinking block was produced, so a turn that you keep through two compactions needs both to have run on a model with preserved thinking.

Compactions from before a thinking block was produced don't count against it. Thinking produced after a block is in place is bound to that block, and it stays valid through later compactions that meet the conditions.

## Change the system prompt or tools

A later request can use a different `system`, different `tools`, or a different model than the compaction request, and the API still accepts the block. Such a change can invalidate the thinking in the kept turns, but it has no other effect.

To change `system` or `tools` without invalidating any kept thinking, compact the whole conversation first, so no turns are kept. Then change them on the next request.

To add an instruction or change the available tools without touching `system` or `tools`, append the change to `messages`, as described in [Make changes without editing the prefix](/docs/en/build-with-claude/preserved-thinking#replace-prefix-edits).

Mid-conversation system messages inside the summarized turns are summarized too, so their instructions and tool changes stop applying after the swap. To keep one in force, state it again in a `role: "system"` message directly after the first new `user` turn that follows the kept turns. A system message placed between the block and the kept turns breaks their thinking.

## Check that the kept thinking held

The compaction response doesn't say whether the kept thinking holds. The first request after the swap does. To check in your tests:

1.  Have a short conversation with thinking on. Use a model on which the API runs the check (see [When the API enforces the check](/docs/en/build-with-claude/preserved-thinking#enforcement)), and use it for every step, because a model that can't read a thinking block drops it with no error.
2.  Compact the older turns, and keep at least one turn that holds a thinking block.
3.  Send the next request, with the block first, then the kept turn, then a new `user` message, and with `thinking.block_binding.prefix_mismatch_behavior` set to `"error"`.
4.  Read the result. A 200 response whose `input_transformations` array is empty means no thinking block failed the check or was dropped. A 400 error that says the block is bound to a different conversation means one did. The message starts with the path of the first block that failed, and [What the API does with an invalid block](/docs/en/build-with-claude/preserved-thinking#mismatch-behavior) shows it in full.

The `prefix_mismatch_behavior` field needs the `thinking-binding-controls-2026-08-01` beta header in addition to [the `compact-2026-09-04` beta header](/docs/en/build-with-claude/compaction-on-demand#request-a-summary). Setting the field also opts the request into the check on accounts where the check isn't on by default.

The following program runs the four steps. It prints how many thinking blocks the kept turn holds and how many entries `input_transformations` has; no entries means the kept thinking held:

Python

TypeScript

C#

Go

Java

PHP

Ruby

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

In production, `"drop_block"` keeps requests succeeding when a condition doesn't hold, and reports each dropped block in `input_transformations` with `reason: "prefix_binding_mismatch"`. An entry whose `path` falls in a kept turn means that turn's thinking didn't hold. [What the API does with an invalid block](/docs/en/build-with-claude/preserved-thinking#mismatch-behavior) describes what is dropped and says how to alert on it.

## Compatibility

[TABLE]
