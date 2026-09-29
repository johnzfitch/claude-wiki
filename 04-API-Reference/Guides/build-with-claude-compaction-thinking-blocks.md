---
title: "Compaction and preserved thinking - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-thinking-blocks"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-22T06:31:44Z"
tags: ["api", "prompting"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcompaction-thinking-blocks)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](build-with-claude-overview.md)[Using the Messages API](build-with-claude-working-with-messages.md)[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)[Refusals and fallback](build-with-claude-refusals-and-fallback.md)[Fallback credit](build-with-claude-fallback-credit.md)

Model capabilities

[Effort](build-with-claude-effort.md)[Task budgets (beta)](build-with-claude-task-budgets.md)[Fast mode (research preview)](build-with-claude-fast-mode.md)[Structured outputs](build-with-claude-structured-outputs.md)[Citations](build-with-claude-citations.md)[Streaming Messages](build-with-claude-streaming.md)[Batch processing](build-with-claude-batch-processing.md)[Search results](build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](build-with-claude-multilingual-support.md)[Embeddings](build-with-claude-embeddings.md)

[Thinking](build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool Runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics (beta)](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

[Compaction](build-with-claude-compaction.md)

[Overview](build-with-claude-compaction.md)[Compact on demand](build-with-claude-compaction-on-demand.md)[Keep recent turns](build-with-claude-compaction-keep-recent-turns.md)[Compact in the background](build-with-claude-compaction-background.md)[Keep thinking blocks valid](build-with-claude-compaction-thinking-blocks.md)[Threshold compaction](build-with-claude-compaction-threshold.md)

Working with files

[Files API](build-with-claude-files.md)[PDF support](build-with-claude-pdf-support.md)

[Images and vision](build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)[Google Cloud](build-with-claude-claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

[Console](../Other/usage-limits.md)

[Messages](../../01-Getting-Started/intro.md)Compaction

# Compaction and preserved thinking

Copy page



When thinking blocks in turns kept after on-demand compaction stay valid on models with preserved thinking, and how to check.

Copy page



Compaction and preserved thinking

[Beta](build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

compact-2026-09-04

Skip this page unless you send thinking blocks back to a model with [preserved thinking](build-with-claude-preserved-thinking.md) and keep turns after the compaction block. Kept turns are the turns that follow the block: recent turns you left out of the compaction request, as in [Compaction that keeps recent turns](build-with-claude-compaction-keep-recent-turns.md), or turns that arrived while the summary was being written, as in [Compaction in the background](build-with-claude-compaction-background.md).

Models with preserved thinking check earlier thinking blocks against the conversation that produced them. A summary replaces part of that conversation, but the check accepts the swap when the API wrote the summary, so the thinking in kept turns can stay valid.

## Conditions for kept thinking to stay valid

The thinking blocks in kept turns stay valid while all of these hold:

- **The compaction request runs on a model with preserved thinking.** This condition covers every compaction request since a thinking block was produced, not only the most recent one. One way to meet it is to send every compaction request to the model the conversation uses.
- **The kept turns directly follow the summarized messages, and you send them unchanged.** Send each kept message exactly as it is in your history. Don't skip or add a message between the last summarized message and the first kept one. The first kept message must also have a different role from the last summarized message, and it can't be a mid-conversation `role: "system"` message. Otherwise, the API merges it into the last summarized message. One way to get the first kept message right is to compact exactly the `messages` of a request you already sent. The kept turns then start with Claude's reply to it.
- **`system` and the `tools` not marked `defer_loading: true` don't change.** They are the same on the compaction request as on the requests that produced the kept thinking, and they stay the same on the requests that follow. [Change the system prompt or tools](#change-the-system-prompt-or-tools) covers how to change them safely.

If a condition doesn't hold, nothing fails when you compact, and the API accepts the block on later requests either way. The failure comes on the first later request that sends the kept thinking where the API enforces the check: a 400 error by default, or dropped thinking blocks if the request sets `thinking.block_binding.prefix_mismatch_behavior` to `"drop_block"`. In the Message Batches API, an item that leaves the field unset doesn't fail. Where the check applies by default, the API drops the blocks instead. [What the API does with an invalid block](build-with-claude-preserved-thinking.md#mismatch-behavior) describes both outcomes, and [When the API enforces the check](build-with-claude-preserved-thinking.md#enforcement) says which requests are checked.

## Compact again without breaking older thinking

You can [compact again](build-with-claude-compaction-on-demand.md#compact-again) and keep turns: the new block covers the old summary and every message that follows it in the compaction request, and any turns you leave out of that request are kept turns of the new block.

The first of the [conditions for kept thinking](#conditions-for-kept-thinking-to-stay-valid) counts every compaction since a thinking block was produced, so a turn that you keep through two compactions needs both to have run on a model with preserved thinking.

Compactions from before a thinking block was produced don't count against it. Thinking produced after a block is in place is bound to that block, and it stays valid through later compactions that meet the conditions.

## Change the system prompt or tools

A later request can use a different `system`, different `tools`, or a different model than the compaction request, and the API still accepts the block. Such a change can invalidate the thinking in the kept turns, but it has no other effect.

To change `system` or `tools` without invalidating any kept thinking, compact the whole conversation first, so no turns are kept. Then change them on the next request.

To add an instruction or change the available tools without touching `system` or `tools`, append the change to `messages`, as described in [Make changes without editing the prefix](build-with-claude-preserved-thinking.md#replace-prefix-edits).

Mid-conversation system messages inside the summarized turns are summarized too, so their instructions and tool changes stop applying after the swap. To keep one in force, state it again in a `role: "system"` message directly after the first new `user` turn that follows the kept turns. A system message placed between the block and the kept turns breaks their thinking.

## Check that the kept thinking held

The compaction response doesn't say whether the kept thinking holds. The first request after the swap does. To check in your tests:

1.  Have a short conversation with thinking on. Use a model on which the API runs the check (see [When the API enforces the check](build-with-claude-preserved-thinking.md#enforcement)), and use it for every step, because a model that can't read a thinking block drops it with no error.
2.  Compact the older turns, and keep at least one turn that holds a thinking block.
3.  Send the next request, with the block first, then the kept turn, then a new `user` message, and with `thinking.block_binding.prefix_mismatch_behavior` set to `"error"`.
4.  Read the result. A 200 response whose `input_transformations` array is empty means no thinking block failed the check or was dropped. A 400 error that says the block is bound to a different conversation means one did. The message starts with the path of the first block that failed, and [What the API does with an invalid block](build-with-claude-preserved-thinking.md#mismatch-behavior) shows it in full.

The `prefix_mismatch_behavior` field needs the `thinking-binding-controls-2026-08-01` beta header in addition to [the `compact-2026-09-04` beta header](build-with-claude-compaction-on-demand.md#request-a-summary). Setting the field also opts the request into the check on accounts where the check isn't on by default.

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

In production, `"drop_block"` keeps requests succeeding when a condition doesn't hold, and reports each dropped block in `input_transformations` with `reason: "prefix_binding_mismatch"`. An entry whose `path` falls in a kept turn means that turn's thinking didn't hold. [What the API does with an invalid block](build-with-claude-preserved-thinking.md#mismatch-behavior) describes what is dropped and says how to alert on it.

## Compatibility

[TABLE]
