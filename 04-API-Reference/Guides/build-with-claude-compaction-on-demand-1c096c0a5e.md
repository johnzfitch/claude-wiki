---
title: "Compaction on demand - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/compaction-on-demand"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-22T06:29:53Z"
tags: ["api", "prompting"]
---

### Cookie settings

We use cookies to deliver and improve our services, analyze site usage, and if you agree, to customize or personalize your experience and market our services to you. You can read our Cookie Policy [here](https://www.anthropic.com/legal/cookies).

CustomizeCustomize Cookie Settings

RejectReject All Cookies

AcceptAccept All Cookies


Claude Platform Docs

- [Messages](/docs/en/intro)

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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fcompaction-on-demand)

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

# Compaction on demand

Copy page



Ask Claude to summarize a conversation when your application chooses, then continue from the summary.

Copy page



Compaction on demand

[Beta](/docs/en/build-with-claude/overview#feature-availability)

[Beta header](/docs/en/api/beta-headers)

compact-2026-09-04

With on-demand compaction, your application decides when a conversation is summarized: you send one request with the `compaction` parameter, and Claude returns a summary in place of a reply.

## How on-demand compaction works

A compaction request is separate from your conversation turns. You send the conversation as it stands with the `compaction` parameter, and the response contains a single `compaction` block. The block holds the summary as text you can read, and a signature. Send it in future requests exactly as it came.

From then on the block takes the place of the messages it summarizes. It goes first in `messages`, the summarized messages are removed, and your next turn follows it. Claude sees the summary where those messages were.

## Request a summary

Send the `compact-2026-09-04` beta header on the request that asks for the summary and on every later request that carries the signed block. To check whether a model supports on-demand compaction, call the [Models API](/docs/en/api/beta/models/list) with the beta header and read each model's `capabilities.compaction`. You can't combine `compaction` with `context_management` on one request.

Send the conversation as it stands with `"compaction": {"type": "summarize"}`. The API summarizes every message in the request once, generates no reply after it, and returns the block alone with `stop_reason` `"compaction"`. Send the same `system` prompt and `tools` that you use for the rest of the conversation. The summarizer reads them, and if you keep turns after the block on a model with [preserved thinking](/docs/en/build-with-claude/preserved-thinking), the thinking in those turns stays valid only if `system` and `tools` match. The conversation in this example has no `system` prompt or tools, so the request sends neither:

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
from anthropic.types.beta import BetaMessageParam

client = anthropic.Anthropic()

history: list[BetaMessageParam] = [
    {
        "role": "user",
        "content": "I am building a recipe app. Help me name the main entities in the data model.",
    },
    {
        "role": "assistant",
        "content": "Start with Recipe, Ingredient, and Step. Add a RecipeIngredient entry that holds the quantity and unit for each ingredient in a recipe.",
    },
    {"role": "user", "content": "Good. Now suggest field names for Recipe."},
]

response = client.beta.messages.create(
    model="claude-opus-5",
    # max_tokens caps the whole call, including any thinking, so allow several thousand tokens.
    max_tokens=4096,
    betas=["compact-2026-09-04"],
    messages=history,
    compaction={"type": "summarize"},
)
print(f"Stop reason: {response.stop_reason}")
```

Response



```python
{
  "id": "msg_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message",
  "role": "assistant",
  "model": "claude-opus-5",
  "content": [
    {
      "type": "compaction",
      "content": "Summary of the conversation: the user is designing the data model for a recipe app. The entities agreed so far are Recipe, Ingredient, Step, and RecipeIngredient, which holds the quantity and unit. The user then asked for field names for Recipe.",
      "signature": "EuYBCkQY..."
    }
  ],
  "stop_reason": "compaction",
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "iterations": [{ "type": "compaction", "input_tokens": 144, "output_tokens": 276 }]
  }
}
```

The summarization call uses the request's model, `system`, `tools`, thinking settings, and `max_tokens`. The summarizer reads the tool definitions but never runs a tool, and the response carries no thinking. `max_tokens` caps the whole call, including any thinking the model does before it writes the summary, so allow several thousand tokens. [Count compaction usage](#understanding-usage) shows how the call is billed.

If the last `assistant` turn ends in a tool call with no result yet, the API rejects the request. Send that turn's tool results first. Also leave out `stop_sequences`, structured-output `output_config.format`, and a `tool_choice` of type `any` or `tool`. They would do nothing on a summarization call, and the API rejects them. The conversation must still fit the model's context window, so compact before you outgrow it, not after.

When you stream the response, the block arrives whole. You get one `content_block_start` event carrying the complete block, then `content_block_stop`, with no `content_block_delta` events. `ping` events can arrive before or between them.

## Continue from the summary

In your history, replace the messages you sent with the returned assistant message. Keep the `compaction` block exactly as the API returned it, including its `signature`. Any turns taken after you sent the compaction request follow the block unchanged, which is what [Compaction in the background](/docs/en/build-with-claude/compaction-background) builds on. Send the block first on every later request, with the beta header:

```python
{
  "model": "claude-opus-5",
  "max_tokens": 2048,
  "messages": [
    {
      "role": "assistant",
      "content": [
        {
          "type": "compaction",
          "content": "Summary of the conversation: the user is designing the data model for a recipe app. The entities agreed so far are Recipe, Ingredient, Step, and RecipeIngredient, which holds the quantity and unit. The user then asked for field names for Recipe.",
          "signature": "EuYBCkQY..."
        }
      ]
    },
    {
      "role": "assistant",
      "content": "For Recipe, use title, description, servings, prep_minutes, and cook_minutes. Add created_at and updated_at timestamps."
    },
    { "role": "user", "content": "Now do the same for Ingredient." }
  ]
}
```



This example continues the request sample, which ended on a `user` turn; the diagram shows the simpler case, where no turn is taken while the summary is written. Here the second `assistant` message is the reply to the last summarized `user` turn. It arrived while the summary was being written, so it was not among the messages summarized. Two `assistant` messages in a row are fine here, because the block still comes first.

The API puts the summary where the block stands and passes every later message to Claude unchanged. Follow these rules:

- Put the block first in `messages`, either as an `assistant` message of its own or as the first content block of the first message, whether that is a `user` or `assistant` message.
- Remove the summarized messages. If any remain in front of the block, the request returns a 400 error (`compaction_block_misplaced`).
- Send exactly one `compaction` block per request, on every later request.



Two mistakes in the swap raise no error. If summarized messages remain after the block, the API sends them to Claude again. If a later request leaves the block out, Claude gets no summary.

Threshold compaction works the other way around: its block follows the messages it summarizes, and the API drops them for you. See [Passing compaction blocks back](/docs/en/build-with-claude/compaction-threshold#passing-compaction-blocks-back).

In Python, use `client.beta.messages`, as the samples on this page do. If you call `client.messages` and serialize blocks yourself, use `to_dict()` or `model_dump(exclude_none=True)`: a plain `model_dump()` adds `citations: null` and `text: null` to the block, and the API rejects it.

If you keep turns after the block and send their thinking blocks back, the conditions that keep that thinking valid are on [Compaction and preserved thinking](/docs/en/build-with-claude/compaction-thinking-blocks).

### Compact again

To compact a conversation that already starts with a block, send `compaction` again. The new block summarizes the old summary and everything after it. From then on, send only the newest block.

## Compact in a loop

After each turn, the loop adds the last response's input and output tokens, because the next request sends the reply too. When that total passes a limit and another turn is still to come, it sends a compaction request with the same model and `system` prompt, checks `stop_reason`, replaces its history with the returned message, and prints the turn it compacted before. The sample's limit of 2,500 tokens is deliberately low, so that a short conversation compacts. Set yours near your real input budget.

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
    if conversation_tokens > COMPACT_AT_TOKENS and turn < len(QUESTIONS):
        summary = client.beta.messages.create(
            model="claude-opus-5",
            max_tokens=4096,
            system=SYSTEM,
            betas=["compact-2026-09-04"],
            messages=history,
            compaction={"type": "summarize"},
        )
        if summary.stop_reason == "compaction":
            history = [{"role": "assistant", "content": summary.content}]
            print(f"Compacted before turn {turn + 1}")
```

The check on `stop_reason` comes before the code looks for the block; [Handle a missing summary or an error](#when-no-summary-comes-back) says why. The history is replaced, not appended to: the returned message replaces every message the request carried, under the rules in [Continue from the summary](#continue-from-the-summary). When no summary comes back, the loop keeps its history and asks again after the next turn.

The SDK [tool runner](/docs/en/agents-and-tools/tool-use/tool-runner) in Python, TypeScript, C#, Go, and Java can send the compaction request for you. When you decide to compact, call `compact_before_next_turn()` on the runner (`compactBeforeNextTurn()` in TypeScript and Java, `CompactBeforeNextTurn()` in C# and Go). Once the current turn and its tool calls finish, the runner sends the compaction request and replaces its history with the returned message. Create the runner with the `compact-2026-09-04` beta, because the runner doesn't add it. The runner builds the request from its own parameters and leaves `context_management` out. If those parameters include `stop_sequences`, a `tool_choice` of type `any` or `tool`, or a structured-output `output_config.format`, the API rejects the request with a 400 error. [Request a summary](#request-a-summary) explains why. The runner refuses to compact while its `context_management` has a compaction edit, so use one kind of compaction on a runner.

### When to compact

You can send a compaction request after any completed turn, so your code decides when.

To estimate how large the next request will be, add `input_tokens` and `output_tokens` from the last response's `usage`, as the loop does. With [prompt caching](/docs/en/build-with-claude/prompt-caching#tracking-cache-performance), `input_tokens` counts only the tokens after the last cache breakpoint, so add `cache_read_input_tokens` and `cache_creation_input_tokens` as well. You can also send the same messages to the [token counting](/docs/en/build-with-claude/token-counting) endpoint.

Compare that number with a limit you choose, below the model's [context window](/docs/en/build-with-claude/context-windows).

## Write your own summarization prompt

Without `instructions`, the API uses its own summarization prompt. A non-blank `instructions` string (up to 16,384 characters) replaces that prompt entirely. For example:

```python
{
  "compaction": {
    "type": "summarize",
    "instructions": "Summarize this recipe app design conversation. Preserve every entity and field name agreed so far, and the user's latest open request. Do not call tools; respond with the summary text only."
  }
}
```



The summarizer reads the whole conversation, earlier thinking included, with or without `instructions`. In your `instructions`, say what the summary must retain and tell the model not to call tools. The summarization call runs under the same safeguards as any other request.

## Handle a missing summary or an error

A summary is produced only when the summarization call ends normally with text and no tool call. Otherwise, the response is still a 200 with empty `content`, so check `stop_reason` before you look for the block. The call is still billed and reported in `usage.iterations`, with zero usage when no call could be made. The `stop_reason` is the one the summarization call ended with. In every case you can continue without a summary and compact later.

| `stop_reason`                     | Cause                                                   | What to do                                                        |
|:----------------------------------|:--------------------------------------------------------|:------------------------------------------------------------------|
| `"max_tokens"`                    | The summary was cut off.                                | Resend with a larger `max_tokens`.                                |
| `"model_context_window_exceeded"` | There was no room for the summarization prompt.         | Resend with shorter `instructions` or fewer messages.             |
| `"tool_use"`                      | The model called a tool instead of writing the summary. | Resend with `instructions` that tell the model not to call tools. |
| `"refusal"`                       | The request was declined.                               | Continue without a summary.                                       |
| `"end_turn"`                      | The call returned no text.                              | Continue without a summary.                                       |

The summarization call is subject to the same safeguards as your other requests. After a `"refusal"`, [`stop_details`](/docs/en/build-with-claude/handling-stop-reasons#refusal) identifies the policy category behind it.

### Errors

A compaction request, or a request that carries a block, can also fail outright. Most 400 errors have a message that says what to remove or resend. Some also carry an `error.details.error_code` that starts with `compaction_`. Parameter errors, such as a field that can't be combined with `compaction`, carry the message only.

| Error                                                                                                                                                                           | Cause                                                                                   | What to do                                                                                                |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| 529 `overloaded_error`, `error.details.error_code` `compaction_unavailable`                                                                                                     | A transient server problem while producing a block, or while reading one you sent back. | Retry the request.                                                                                        |
| 400 `compaction_block_misplaced`                                                                                                                                                | Summarized messages remain in front of the block.                                       | Remove them, so the block comes first in `messages`.                                                      |
| 400 `compaction_signature_invalid` or `compaction_content_mismatch`                                                                                                             | The block's `signature` or `content` was changed after the API returned it.             | Send the block exactly as returned, including its `signature`.                                            |
| 400                                                                                                                                                                             | The request carries more than one `compaction` block.                                   | Send exactly one, the newest.                                                                             |
| 400                                                                                                                                                                             | The last `assistant` turn ends in a tool call with no result yet.                       | Send that turn's tool results, then compact.                                                              |
| 400 `compaction_nothing_to_summarize`                                                                                                                                           | `messages` has no `user` or `assistant` content, for example an empty list.             | Send at least one `user` or `assistant` message.                                                          |
| 400 on the compaction request, with a message that says the `compaction` parameter `requires anthropic-beta: compact-2026-09-04`                                                | The compaction request left out the beta header.                                        | Add the beta header; see [Request a summary](#request-a-summary).                                         |
| 400 on a later request that carries the block: a validation error that says `compaction` is not one of the expected content block types. The message doesn't mention the header | That request left out the beta header.                                                  | Add the beta header to every request that carries the block; see [Request a summary](#request-a-summary). |
| 400 validation error, such as `messages.0.content.0.compaction.citations: Extra inputs are not permitted`                                                                       | A block was sent back with fields the API didn't return, such as `citations: null`.     | Send the block exactly as returned; see [Continue from the summary](#continue-from-the-summary).          |

## Count compaction usage

The summarization call is billed and rate-limited like any other request, and `usage.iterations` reports it as the `compaction` entry. The top-level `input_tokens` and `output_tokens` are zero because no reply was generated. To count what a conversation consumed, sum across `usage.iterations`, not the top-level fields. Sending a block back on later requests adds no compaction cost.

You have a working loop that compacts a conversation and handles a missing summary. Two pages change how it runs, and you can combine them: [Compaction that keeps recent turns](/docs/en/build-with-claude/compaction-keep-recent-turns) keeps the last turns word for word, and [Compaction in the background](/docs/en/build-with-claude/compaction-background) lets the conversation continue while the summary is written. [Compaction and preserved thinking](/docs/en/build-with-claude/compaction-thinking-blocks) applies if you send thinking blocks back and do either.

## Limits and interactions with other features

- **Threshold compaction and context editing.** You can't send `compaction` and `context_management` on the same request. Threshold compaction (`compact_20260112`) can't run on a request that carries a signed block.
- **Prompt caching.** `cache_control` on the block places a breakpoint after the summary.
- **Mid-conversation system messages and tool changes.** `role: "system"` messages inside the summarized range are summarized too, so their text instructions stop applying once the block replaces them. If an instruction still matters, state it again in a `role: "system"` message. Send that message right after your next new `user` turn, and leave it in your history from then on. For [tool changes](/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes), and for where that message goes when you keep turns after the block, see [Change the system prompt or tools](/docs/en/build-with-claude/compaction-thinking-blocks#change-the-system-prompt-or-tools).
- **Task budgets.** Don't send the `remaining` value of a [task budget](/docs/en/build-with-claude/task-budgets) (`output_config.task_budget.remaining`) with `compaction` or on requests that carry the block. Doing so returns a 400 error.
- **Token counting.** The [token counting](/docs/en/build-with-claude/token-counting) endpoint ignores the `compaction` parameter.
- **Content the summary can't carry.** Images, documents, `container_upload` blocks, and fetched URLs inside the summarized messages are gone once the block replaces them. Restate or re-upload anything a later turn still needs.

## Compatibility

[TABLE]
