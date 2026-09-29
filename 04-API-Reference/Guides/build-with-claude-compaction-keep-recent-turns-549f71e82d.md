---
title: "Compaction that keeps recent turns - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-keep-recent-turns"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-22T06:30:30Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcompaction-keep-recent-turns)

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

# Compaction that keeps recent turns

Copy page



Summarize the older turns of a conversation with on-demand compaction and send the most recent turns after the summary, word for word.

Copy page



Compaction that keeps recent turns

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

compact-2026-09-04

Keep-tail compaction keeps the last few turns of a conversation word for word after the summary. It changes two things in the [compaction loop](/docs/en/build-with-claude/compaction-on-demand#compact-in-a-loop): which messages go into the compaction request, and what you send after the block. Everything in [Continue from the summary](/docs/en/build-with-claude/compaction-on-demand#continue-from-the-summary) applies unchanged.

## Choose which turns to keep

No parameter sets which turns are kept. You pick a cut point in your history: the messages before it go into the compaction request, and the messages from it on are kept.

Kept turns go back to Claude at full length, so the more you keep, the less room the compaction frees.

Put the cut where no tool call is left open, with each tool call and its result on the same side. If the messages you send end in an `assistant` turn whose tool call has no result yet, the API rejects the compaction request.

## Compact the older turns and send the rest after the block

To keep a tail of recent turns word for word, leave those turns out of the compaction request. The API summarizes every message it is sent, so send only the older turns, then put the block in front of the turns you kept.

Send the kept turns exactly as they are in your history, thinking blocks included. Both requests carry the beta header, as in [Request a summary](/docs/en/build-with-claude/compaction-on-demand#request-a-summary).

In the following example, the history holds two turns, and the cut keeps the second. The compaction request carries the first turn:

```python
{
  "model": "claude-opus-5",
  "max_tokens": 4096,
  "messages": [
    {
      "role": "user",
      "content": "I am building a recipe app. Help me name the main entities in the data model."
    },
    {
      "role": "assistant",
      "content": "Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe."
    }
  ],
  "compaction": { "type": "summarize" }
}
```



The next request sends the returned block first, then the kept turn exactly as it was, then the new `user` message. [Continue from the summary](/docs/en/build-with-claude/compaction-on-demand#continue-from-the-summary) shows a request that starts with a block.

The following program is the loop from [Compact in a loop](/docs/en/build-with-claude/compaction-on-demand#compact-in-a-loop), changed to keep the last two turns. The highlighted lines show where it differs from the loop.

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
from anthropic.types.beta import BetaMessageParam

client = anthropic.Anthropic()

# Set this near your real input budget. It is low here so a short conversation compacts.
COMPACT_AT_TOKENS = 2500
SYSTEM = "You help design a recipe app's data model. Keep answers short."
KEEP_TURNS = 2

QUESTIONS = [
    "What are the main entities in the data model?",
    "Which fields should Recipe have?",
    "Which fields should Ingredient have?",
    "Which fields should RecipeIngredient have?",
    "Which fields should Step have?",
    "Which indexes should these tables have?",
    "Which fields should be required?",
    "Which fields should have default values?",
]

history: list[BetaMessageParam] = []
for turn, question in enumerate(QUESTIONS, start=1):
    history.append({"role": "user", "content": question})
    response = client.beta.messages.create(
        model="claude-opus-5",
        max_tokens=8192,
        system=SYSTEM,
        betas=["compact-2026-09-04"],
        messages=history,
    )
    history.append({"role": "assistant", "content": response.content})

    # The next request sends this reply too, so count it.
    conversation_tokens = response.usage.input_tokens + response.usage.output_tokens
    if conversation_tokens > COMPACT_AT_TOKENS and KEEP_TURNS < turn < len(QUESTIONS):
        # A turn is one user message and one assistant reply,
        # so the kept turns start with a user message.
        split = -2 * KEEP_TURNS
        older, recent = history[:split], history[split:]
        summary = client.beta.messages.create(
            model="claude-opus-5",
            max_tokens=4096,
            system=SYSTEM,
            betas=["compact-2026-09-04"],
            messages=older,
            compaction={"type": "summarize"},
        )
        if summary.stop_reason == "compaction":
            history = [{"role": "assistant", "content": summary.content}, *recent]
            print(f"Kept {len(recent) // 2} turns after the block")
```

- **Picking the cut:** The program keeps the last two turns, where a turn is one `user` message and the reply to it. It splits the history four messages from the end, so the kept turns start with a `user` message.
- **Deciding when to compact:** The size check also requires that the conversation has more turns than the program keeps, so the older part is never empty.
- **The compaction request:** Where the loop sends the whole history, this version sends only the older messages.
- **The swap:** Where the loop replaces the whole history with the returned message, this version's new history is the returned message followed by the kept turns.

The `stop_reason` check and every request after the swap are unchanged from the loop.

## Keep thinking valid in the kept turns

If you send thinking blocks back on a model with [preserved thinking](/docs/en/build-with-claude/preserved-thinking), the thinking in the kept turns stays valid only while the [conditions for kept thinking](/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid) hold, and one of them limits where the cut can fall.

The program's cut, between a reply and the next `user` message, meets that condition. So does a cut at the end of a request you already made: compact exactly that request's `messages`, and keep everything your history has gained since.

## Compatibility

[TABLE]
