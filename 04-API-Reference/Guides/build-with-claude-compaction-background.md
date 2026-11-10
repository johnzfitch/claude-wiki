---
title: "Compaction in the background - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-background"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-08T06:24:39Z"
tags: ["api"]
---

# Compaction in the background

Copy page



Request an on-demand compaction summary while the conversation continues on its full history, then swap the block in when it arrives.

Copy page



Background compaction

Feature of  
[On-demand compaction](build-with-claude-compaction-on-demand.md)

[Status](#availability-feature-support)  
Beta

[APIs](#feature-availability)  
Messages APIAvailable

[Cloud platforms](#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableAmazon BedrockAvailableClaude Models on Google CloudGoogle managedAvailableMicrosoft FoundryAvailable

[Beta header](#feature-beta-headers)  
- `compact-2026-09-04`
  

Background compaction, often called async compaction, changes two things in the [compaction loop](build-with-claude-compaction-on-demand.md#compact-in-a-loop): the compaction request runs while the conversation continues on its full history, and the swap waits until the block arrives. [Continue from the summary](build-with-claude-compaction-on-demand.md#continue-from-the-summary) and [Handle a missing summary or an error](build-with-claude-compaction-on-demand.md#when-no-summary-comes-back) apply unchanged.

## How the swap works while work continues

The compaction request and the block it returns are the same as in the loop. Your history grows between sending the request and using its result, and the swap must leave that growth in place.

1.  Send the [compaction request](build-with-claude-compaction-on-demand.md#request-a-summary) with your history as it stands, and record how many messages it held.
2.  While that request runs, keep the conversation going on the full history. Append each new turn, don’t edit anything already in the history, and don’t start another compaction request until this one is swapped in or has failed.
3.  When the response arrives with `stop_reason` `"compaction"`, drop exactly the messages you sent from the front of your history and put the returned message in their place. Every turn appended since step 1 stays after it.
4.  Send the swapped history on the first request after the block arrives, so that thinking produced while the summary was being written stays valid.

For example, if the compaction request held messages 1 to 5 and the conversation gained messages 6 to 8 while it ran, after the swap your history is the block followed by messages 6 to 8.

If the response has any other `stop_reason`, no summary was produced, which counts as a failure in step 2. Keep the full history; [Handle a missing summary or an error](build-with-claude-compaction-on-demand.md#when-no-summary-comes-back) lists the causes and what to do for each.

## Request the summary in the background

The compaction request counts against your rate limits like any other request, and while it runs your application has two requests open at once. The conversation keeps growing on its full history until the swap, so start the compaction request while the context window still has room for the turns that arrive meanwhile.

The following program is the loop from [Compact in a loop](build-with-claude-compaction-on-demand.md#compact-in-a-loop) with the compaction request taken off the conversation’s path. The highlighted lines show where it differs from the loop, and the following list takes them in the order the program runs them.

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
- **Starting the request:** Where the loop waits for the compaction response, this version records how many messages the history holds, starts the request on a copy of the history with the language’s own concurrency tool, and goes on to the next turn without waiting.
- **Checking for the result:** At the top of each turn, the program checks whether the pending request has completed. If it has, the program makes the swap before it sends that turn’s request.
- **Making the swap:** Where the loop replaces the whole history with the returned message, this version’s swap function replaces only the messages the request held, counted from the front, and keeps everything appended since.
- **Ending the loop:** If the compaction request is still pending when the loop ends, the program waits for it and makes the swap, so a summary that is still on its way isn’t lost before you save or continue the conversation.

The `stop_reason` check is unchanged from the loop: a response without a block leaves the history as it was. Because nothing is pending any more, the program can then start a new compaction request.

## Keep thinking valid while the summary is built

Turns that arrive while the summary is being written are kept turns. If you send thinking blocks back on a model with [preserved thinking](build-with-claude-preserved-thinking.md), the thinking in those turns stays valid only while the [conditions for kept thinking](build-with-claude-compaction-thinking-blocks.md#conditions-for-kept-thinking-to-stay-valid) hold.

## Availability

Background compaction is in beta on select models.

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

StatusBeta

Cloud platforms

- [Amazon Bedrock](build-with-claude-claude-in-amazon-bedrock.md)

Models

- [Claude Haiku 4.5](../../20-Models/models-haiku-4-5-overview.md)Not supported
- All other models

### Required beta headers

[Beta headers overview](../Endpoints/beta-headers.md)

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

Header

- `compact-2026-09-04`
  
