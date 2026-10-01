---
title: "Compaction in the background - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-background"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-30T06:30:57Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcompaction-background)

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

# Compaction in the background

Copy page



Request an on-demand compaction summary while the conversation continues on its full history, then swap the block in when it arrives.

Copy page



Compaction in the background

[Beta](build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

compact-2026-09-04

Background compaction, often called async compaction, changes two things in the [compaction loop](build-with-claude-compaction-on-demand.md#compact-in-a-loop): the compaction request runs while the conversation continues on its full history, and the swap waits until the block arrives. [Continue from the summary](build-with-claude-compaction-on-demand.md#continue-from-the-summary) and [Handle a missing summary or an error](build-with-claude-compaction-on-demand.md#when-no-summary-comes-back) apply unchanged.

## How the swap works while work continues

The compaction request and the block it returns are the same as in the loop. Your history grows between sending the request and using its result, and the swap must leave that growth in place.

1.  Send the [compaction request](build-with-claude-compaction-on-demand.md#request-a-summary) with your history as it stands, and record how many messages it held.
2.  While that request runs, keep the conversation going on the full history. Append each new turn, don't edit anything already in the history, and don't start another compaction request until this one is swapped in or has failed.
3.  When the response arrives with `stop_reason` `"compaction"`, drop exactly the messages you sent from the front of your history and put the returned message in their place. Every turn appended since step 1 stays after it.
4.  Send the swapped history on the first request after the block arrives, so that thinking produced while the summary was being written stays valid.

For example, if the compaction request held messages 1 to 5 and the conversation gained messages 6 to 8 while it ran, after the swap your history is the block followed by messages 6 to 8.

If the response has any other `stop_reason`, no summary was produced, which counts as a failure in step 2. Keep the full history; [Handle a missing summary or an error](build-with-claude-compaction-on-demand.md#when-no-summary-comes-back) lists the causes and what to do for each.

## Request the summary in the background

The compaction request counts against your rate limits like any other request, and while it runs your application has two requests open at once. The conversation keeps growing on its full history until the swap, so start the compaction request while the context window still has room for the turns that arrive meanwhile.

The following program is the loop from [Compact in a loop](build-with-claude-compaction-on-demand.md#compact-in-a-loop) with the compaction request taken off the conversation's path. It has no PHP version, because the example depends on running two requests at once. The highlighted lines show where it differs from the loop, and the following list takes them in the order the program runs them.

Python

TypeScript

C#

Go

Java

Ruby



```python
from concurrent.futures import Future, ThreadPoolExecutor

import anthropic
from anthropic.types.beta import BetaMessage, BetaMessageParam

client = anthropic.Anthropic()
executor = ThreadPoolExecutor(max_workers=1)

# Set this near your real input budget. It is low here so a short conversation compacts.
COMPACT_AT_TOKENS = 2500
SYSTEM = "You help design a recipe app's data model. Keep answers short."

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


def swap_in(history: list[BetaMessageParam], summary: BetaMessage, sent: int) -> None:
    if summary.stop_reason == "compaction":
        # Replace exactly the messages the compaction request held.
        # Later turns stay after the block.
        history[:sent] = [{"role": "assistant", "content": summary.content}]
        print(f"Swapped {sent} messages")


history: list[BetaMessageParam] = []
pending: Future[BetaMessage] | None = None
sent = 0
for turn, question in enumerate(QUESTIONS, start=1):
    if pending is not None and pending.done():
        swap_in(history, pending.result(), sent)
        pending = None

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
    if (
        conversation_tokens > COMPACT_AT_TOKENS
        and turn < len(QUESTIONS)
        and pending is None
    ):
        sent = len(history)
        pending = executor.submit(
            client.beta.messages.create,
            model="claude-opus-5-5",
            max_tokens=4096,
            system=SYSTEM,
            betas=["compact-2026-09-04"],
            messages=history.copy(),
            compaction={"type": "summarize"},
        )

# Swap in a summary that is still on its way before you save
# or continue the conversation.
if pending is not None:
    swap_in(history, pending.result(), sent)
executor.shutdown()
```

- **Deciding when to compact:** The size check also requires that no compaction request is pending.
- **Starting the request:** Where the loop waits for the compaction response, this version records how many messages the history holds, starts the request on a copy of the history with each language's own concurrency tool, and goes on to the next turn without waiting.
- **Checking for the result:** At the top of each turn, the program checks whether the pending request has finished. If it has, the program makes the swap before it sends that turn's request.
- **Making the swap:** Where the loop replaces the whole history with the returned message, this version's swap function replaces only the messages the request held, counted from the front, and keeps everything appended since.
- **Ending the loop:** If the compaction request is still pending when the loop ends, the program waits for it and makes the swap, so a summary that is still on its way isn't lost before you save or continue the conversation.

The `stop_reason` check is unchanged from the loop: a response without a block leaves the history as it was. Because nothing is pending any more, the program can then start a new compaction request.

## Keep thinking valid while the summary is built

Turns that arrive while the summary is being written are kept turns. If you send thinking blocks back on a model with [preserved thinking](build-with-claude-preserved-thinking.md), the thinking in those turns stays valid only while the [conditions for kept thinking](build-with-claude-compaction-thinking-blocks.md#conditions-for-kept-thinking-to-stay-valid) hold.

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
