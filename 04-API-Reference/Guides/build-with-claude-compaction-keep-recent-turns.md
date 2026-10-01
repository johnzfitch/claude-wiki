---
title: "Compaction that keeps recent turns - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-keep-recent-turns"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-30T06:32:04Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcompaction-keep-recent-turns)

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

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

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

# Compaction that keeps recent turns

Copy page



Summarize the older turns of a conversation with on-demand compaction and send the most recent turns after the summary, word for word.

Copy page



Compaction that keeps recent turns

[Beta](build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

compact-2026-09-04

Keep-tail compaction keeps the last few turns of a conversation word for word after the summary. It changes two things in the [compaction loop](build-with-claude-compaction-on-demand.md#compact-in-a-loop): which messages go into the compaction request, and what you send after the block. Everything in [Continue from the summary](build-with-claude-compaction-on-demand.md#continue-from-the-summary) applies unchanged.

## Choose which turns to keep

No parameter sets which turns are kept. You pick a cut point in your history: the messages before it go into the compaction request, and the messages from it on are kept.

Kept turns go back to Claude at full length, so the more you keep, the less room the compaction frees.

Put the cut where no tool call is left open, with each tool call and its result on the same side. If the messages you send end in an `assistant` turn whose tool call has no result yet, the API rejects the compaction request.

## Compact the older turns and send the rest after the block

To keep a tail of recent turns word for word, leave those turns out of the compaction request. The API summarizes every message it is sent, so send only the older turns, then put the block in front of the turns you kept.

Send the kept turns exactly as they are in your history, thinking blocks included. Both requests carry the beta header, as in [Request a summary](build-with-claude-compaction-on-demand.md#request-a-summary).

In the following example, the history holds two turns, and the cut keeps the second. The compaction request carries the first turn:

```python
{
  "model": "claude-opus-5-5",
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

The next request sends the returned block first, then the kept turn exactly as it was, then the new `user` message. [Continue from the summary](build-with-claude-compaction-on-demand.md#continue-from-the-summary) shows a request that starts with a block.

The following program is the loop from [Compact in a loop](build-with-claude-compaction-on-demand.md#compact-in-a-loop), changed to keep the last two turns. The highlighted lines show where it differs from the loop.

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
        model="claude-opus-5-5",
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
            model="claude-opus-5-5",
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

If you send thinking blocks back on a model with [preserved thinking](build-with-claude-preserved-thinking.md), the thinking in the kept turns stays valid only while the [conditions for kept thinking](build-with-claude-compaction-thinking-blocks.md#conditions-for-kept-thinking-to-stay-valid) hold, and one of them limits where the cut can fall.

The program's cut, between a reply and the next `user` message, meets that condition. So does a cut at the end of a request you already made: compact exactly that request's `messages`, and keep everything your history has gained since.

## Compatibility

Supported models  
- Fable 5 and 5.1
- Mythos 5, 5.1, and Preview
- Opus 4.6, 4.7, 4.8, 5, and 5.5
- Sonnet 4.6, 5, and 5.5

Supported platforms  
- Claude APIBeta
- Claude Platform on AWSBeta
- Google CloudBeta
- Microsoft FoundryBeta
