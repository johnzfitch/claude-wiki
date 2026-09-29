---
title: "Compaction in the background - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-background"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-22T06:30:27Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcompaction-background)

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

# Compaction in the background

Copy page



Request an on-demand compaction summary while the conversation continues on its full history, then swap the block in when it arrives.

Copy page



Compaction in the background

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

compact-2026-09-04

Background compaction, often called async compaction, changes two things in the [compaction loop](/docs/en/build-with-claude/compaction-on-demand#compact-in-a-loop): the compaction request runs while the conversation continues on its full history, and the swap waits until the block arrives. [Continue from the summary](/docs/en/build-with-claude/compaction-on-demand#continue-from-the-summary) and [Handle a missing summary or an error](/docs/en/build-with-claude/compaction-on-demand#when-no-summary-comes-back) apply unchanged.

## How the swap works while work continues

The compaction request and the block it returns are the same as in the loop. Your history grows between sending the request and using its result, and the swap must leave that growth in place.

1.  Send the [compaction request](/docs/en/build-with-claude/compaction-on-demand#request-a-summary) with your history as it stands, and record how many messages it held.
2.  While that request runs, keep the conversation going on the full history. Append each new turn, don't edit anything already in the history, and don't start another compaction request until this one is swapped in or has failed.
3.  When the response arrives with `stop_reason` `"compaction"`, drop exactly the messages you sent from the front of your history and put the returned message in their place. Every turn appended since step 1 stays after it.
4.  Send the swapped history on the first request after the block arrives, so that thinking produced while the summary was being written stays valid.

For example, if the compaction request held messages 1 to 5 and the conversation gained messages 6 to 8 while it ran, after the swap your history is the block followed by messages 6 to 8.

If the response has any other `stop_reason`, no summary was produced, which counts as a failure in step 2. Keep the full history; [Handle a missing summary or an error](/docs/en/build-with-claude/compaction-on-demand#when-no-summary-comes-back) lists the causes and what to do for each.

## Request the summary in the background

The compaction request counts against your rate limits like any other request, and while it runs your application has two requests open at once. The conversation keeps growing on its full history until the swap, so start the compaction request while the context window still has room for the turns that arrive meanwhile.

The following program is the loop from [Compact in a loop](/docs/en/build-with-claude/compaction-on-demand#compact-in-a-loop) with the compaction request taken off the conversation's path. It has no PHP version, because the example depends on running two requests at once. The highlighted lines show where it differs from the loop, and the following list takes them in the order the program runs them.

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
        model="claude-opus-5",
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
            model="claude-opus-5",
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

Turns that arrive while the summary is being written are kept turns. If you send thinking blocks back on a model with [preserved thinking](/docs/en/build-with-claude/preserved-thinking), the thinking in those turns stays valid only while the [conditions for kept thinking](/docs/en/build-with-claude/compaction-thinking-blocks#conditions-for-kept-thinking-to-stay-valid) hold.

## Compatibility

[TABLE]
