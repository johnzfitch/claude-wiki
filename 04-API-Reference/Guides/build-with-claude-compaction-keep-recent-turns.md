---
title: "Compaction that keeps recent turns - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-keep-recent-turns"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-16T06:24:44Z"
tags: ["api"]
---

# Compaction that keeps recent turns

Copy page



Summarize the older turns of a conversation with on-demand compaction and send the most recent turns after the summary, word for word.

Copy page



Keep-tail compaction

Feature of  
[On-demand compaction](build-with-claude-compaction-on-demand.md)

[Status](#feature-availability)  
Beta

[Models](#feature-availability)  
- All latest models
- Limited support for other models; see details

[APIs](#feature-availability)  
- Messages API

[Cloud platforms](#feature-availability)  
- Claude API
- Amazon Bedrock
- Claude Platform on AWS
- Claude Models on Google CloudGoogle managed
- Microsoft Foundry

[Beta header](#feature-availability)  
- 
  Copy`compact-2026-09-04`

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

Python

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
- **The swap:** Where the loop replaces the whole history with the returned message, this version’s new history is the returned message followed by the kept turns.

The `stop_reason` check and every request after the swap are unchanged from the loop.

## Keep thinking valid in the kept turns

If you send thinking blocks back on a model with [preserved thinking](build-with-claude-preserved-thinking.md), the thinking in the kept turns stays valid only while the [conditions for kept thinking](build-with-claude-compaction-thinking-blocks.md#conditions-for-kept-thinking-to-stay-valid) hold, and one of them limits where the cut can fall.

The program’s cut, between a reply and the next `user` message, meets that condition. So does a cut at the end of a request you already made: compact exactly that request’s `messages`, and keep everything your history has gained since.

## Availability

Keep-tail compaction

Cloud platform

Cloud platform: Claude API

Claude API

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Mythos 5.2, Mythos 5.1, Mythos 5, Mythos Preview
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5

Amazon Bedrock

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Fable 5.1, Fable 5
- Claude Mythos 5.1, Mythos 5
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7
- Claude Sonnet 5.5, Sonnet 5
- Claude Haiku 5.5

Claude Platform on AWS

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5

Claude Models on Google Cloud (Google managed)

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Mythos 5.2, Mythos 5.1, Mythos 5
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5

Microsoft Foundry (hosted on Azure)

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Opus 5.5, Opus 5, Opus 4.8
- Claude Sonnet 5.5, Sonnet 5
- Claude Haiku 5.5

Microsoft Foundry (hosted on Anthropic)

Status  
Beta

API  
- Messages API

Beta header  
Requires

compact-2026-09-04

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Mythos 5.2, Mythos 5.1, Mythos 5
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5
