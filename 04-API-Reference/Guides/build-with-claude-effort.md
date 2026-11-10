---
title: "Effort - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/effort"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-05T06:36:01Z"
tags: ["api"]
---

# Effort

Copy page



Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency.

Copy page



Effort

[APIs](#feature-availability)  
Messages APIAlways onManaged AgentsAlways on

[Cloud platforms](#availability-feature-support)  
All platforms

[Data handling](#feature-data-handling)  
ZDR eligibleHIPAA eligible

Usage differs by product

Messages API

Set `output_config.effort` on the request. With no value, the model’s default level applies.

Managed Agents

Set `effort` on the agent’s model object, or in a session’s model override. With no value, Managed Agents fills in the model’s default.

The effort parameter lets you control how many tokens Claude spends when responding to requests. You can trade off between response thoroughness and token efficiency with a single model. The top-level effort parameter is available on all supported models with no beta header required. [Per-message effort](#change-effort-mid-conversation-beta) is in beta.



To learn how effort interacts with thinking and which control to reach for, see [Thinking and effort](build-with-claude-thinking.md#thinking-and-effort). Where adaptive thinking is available, effort is the recommended way to control thinking depth.

## Set the effort level

Set `output_config.effort` on the request. The following example runs one request at `medium` effort.

cURL

CLI

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
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "Analyze the trade-offs between microservices and monolithic architectures",
        }
    ],
    output_config={"effort": "medium"},
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

## How effort works

Most Claude models default to high effort, spending as many tokens as needed for excellent results; Claude Opus 5.5 and Claude Haiku 5.5 default to medium. You can raise the effort level to `max` for the absolute highest capability, or lower it to be more conservative with token usage, optimizing for speed and cost while accepting some reduction in capability.



Setting `effort` to the model’s default (`"medium"` on Claude Opus 5.5 and Claude Haiku 5.5, `"high"` on other models) produces exactly the same behavior as omitting the `effort` parameter entirely.

The effort parameter affects **all tokens** in the response, including:

- Text responses and explanations
- Tool calls and function arguments
- Thinking (when active)

Because effort applies to every output token, it works with or without thinking. Lower effort also means fewer and terser tool calls.

### Effort levels

| Level | Description | Typical use case |
|----|----|----|
| `max` | Absolute maximum capability with no constraints on token spending. Available on Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, and Claude Haiku 5.5. | Tasks requiring the deepest possible reasoning and most thorough analysis |
| `xhigh` | Extended capability for long-horizon work. Available on Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, Claude Mythos 5, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 5.5, Claude Sonnet 5, and Claude Haiku 5.5. | Long-running agentic and coding tasks (over 30 minutes) with token budgets in the millions |
| `high` | Spends as many tokens as the task needs for excellent results. The default on every model that supports effort except Claude Opus 5.5 and Claude Haiku 5.5. | Complex reasoning, difficult coding problems, agentic tasks |
| `medium` | Balanced approach with moderate token savings. The default on Claude Opus 5.5 and Claude Haiku 5.5. | Agentic tasks that require a balance of speed, cost, and performance |
| `low` | Most efficient. Significant token savings with some capability reduction. | Simpler tasks that need the best speed and lowest costs, such as subagents |

Not every model that supports `max` supports `xhigh`.



Effort is a behavioral signal, not a strict token budget. At lower effort levels, Claude still thinks on sufficiently difficult problems, but thinks less than it would at higher effort levels for the same problem.

The per-model recommendations that follow override this table where they differ.

## Recommended effort levels

Differs by model

Featured models

Claude Fable 5.1

Claude Opus 5.5

Claude Sonnet 5.5

Claude Haiku 5.5

Additional models

Claude Fable 5

Claude Opus 5

Claude Opus 4.8

Claude Opus 4.7

Claude Sonnet 5

Claude Sonnet 4.6

Claude Fable 5.1

[Claude Fable 5.1](../../20-Models/models-fable-5-1-overview.md) & [Claude Mythos 5.1](../../20-Models/models-mythos-5-1-overview.md)For demanding reasoning and long-horizon agentic work

Claude Fable 5.1 supports all five effort levels. **Start with `high`, the default.** Step up to `xhigh` or `max` for the most capability-sensitive agentic and coding work, and step down to `medium` or `low` for routine or latency-sensitive work once your evals show quality holds. At `high` and above, set a large `max_tokens`. It’s a hard limit on total output (thinking plus response text).

Claude Fable 5.1 also supports [changing effort mid-conversation](#change-effort-mid-conversation-beta) with a per-message `output_config`, which preserves the prompt cache.

See also: [Prompting Claude Fable 5.1](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md#consider-all-effort-levels)

[Claude Opus 5.5](../../20-Models/models-opus-5-5-overview.md)For long-running agentic coding and knowledge work

Claude Opus 5.5 supports all five effort levels, and `medium` is the default (Claude Opus 5 and earlier Opus models default to `high`, so a request that omits `effort` runs one level lower than it did on Claude Opus 5). Adaptive thinking is always on and can’t be turned off, so effort is the primary control for how much the model reasons and what a request costs. Run an effort sweep on your own evals rather than carrying settings over from an earlier model, and set a large `max_tokens` at the higher levels: it’s a hard limit on total output (thinking plus response text). Requests that set `thinking: {"type": "disabled"}` return a 400 error at every effort level. Claude Opus 5.5 also supports [changing effort mid-conversation](#change-effort-mid-conversation-beta) with a per-message `output_config`, which preserves the prompt cache.

See also: [Prompting Claude Opus 5.5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md)

[Claude Sonnet 5.5](../../20-Models/models-sonnet-5-5-overview.md)The best combination of speed and intelligence

Claude Sonnet 5.5 supports all five effort levels, and `high` is the default on the Claude API. Its levels are recalibrated, so a level doesn’t produce the same amount of thinking as the same level on Claude Sonnet 5. Run a fresh effort sweep on your evals rather than carrying over the setting you used on Claude Sonnet 5. Start with `high` unless your workload is agentic or latency-sensitive. For agentic coding and multistep tool use, start with `medium` for well-specified tasks and move to `high` for harder or longer ones. For chat and other latency-sensitive work, start with `medium` or `low`. Use `xhigh` or `max` only where your evals show a quality gain. Set `max_tokens` with room for thinking and the reply. Thinking counts toward `max_tokens` even when the thinking content isn’t returned. For agentic coding, set `max_tokens` to 128,000, the model’s maximum, and [stream](build-with-claude-streaming.md) the response.

To turn off up-front thinking, send `thinking: {"type": "between_tools"}` instead of `"disabled"`. It’s the lowest thinking setting on Claude Sonnet 5.5, and it works at `low`, `medium`, and `high` effort. At `xhigh` or `max`, a request with it returns a 400 error, so use adaptive thinking at those levels: omit the `thinking` field or send `thinking: {"type": "adaptive"}`. See [Running without up-front thinking](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-sonnet-5-5.md#running-without-up-front-thinking).

Claude Sonnet 5.5 also supports [changing effort mid-conversation](#change-effort-mid-conversation-beta) with a per-message `output_config`, which preserves the prompt cache. With `between_tools`, effort can’t change mid-conversation: a per-message `output_config.effort` that differs from the level in effect returns a 400 error. To vary effort for each turn, use adaptive thinking.

See also: [Prompting Claude Sonnet 5.5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-sonnet-5-5.md#calibrate-effort)

[Claude Haiku 5.5](../../20-Models/models-haiku-5-5-overview.md)For high-volume, latency-sensitive tasks such as classification, extraction, and routing

Claude Haiku 5.5 supports all five effort levels, and `medium` is the default. Effort is the main control for how much the model thinks, and with it quality, latency, and cost. **Start with `medium`** for most work, including agentic coding. Use `low`, the cheapest and fastest level, for chat, short tool tasks, and simple, high-volume requests. In long agent prompts, the model is more likely to skip a search, stop early, or skip a check at `low`. Use `high` for knowledge work, longer agent tasks, and strict instruction following. Use `xhigh` or `max` only where your evals show a quality gain, and compare them with Claude Sonnet 5.5 on performance, cost, and speed. Thinking is on by default and counts toward `max_tokens`, so leave room for it.

To get less thinking, lower the effort level. You can also send `thinking: {"type": "disabled"}` at `high` effort or below. At `xhigh` or `max`, it returns a 400 error, so use adaptive thinking there: omit the `thinking` field or send `thinking: {"type": "adaptive"}`.

Where your platform supports it, Claude Haiku 5.5 also lets you [change effort mid-conversation](#change-effort-mid-conversation-beta) with a per-message `output_config`, which preserves the prompt cache. With `thinking: {"type": "disabled"}`, effort can’t change mid-conversation: a per-message `output_config.effort` that differs from the level in effect returns a 400 error. To vary effort for each turn, use adaptive thinking.

See also: [Prompting Claude Haiku 5.5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-haiku-5-5.md#use-effort-to-control-thinking)

[Claude Fable 5](../../20-Models/models-fable-5-overview.md) & [Claude Mythos 5](../../20-Models/models-mythos-5-overview.md)

Effort is the primary control for trading off intelligence, latency, and cost on Claude Fable 5. **Start with `high`, the default, for most tasks**, use `xhigh` for the most capability-sensitive workloads, and step down to `medium` or `low` for routine work. Lower effort settings on Claude Fable 5 still perform well and often exceed `xhigh` performance on prior models. At `high` and `xhigh`, set a large `max_tokens`. It’s a hard limit on total output (thinking plus response text). See [Cost control](build-with-claude-thinking-steering-and-cost.md#cost-control).

Reduce effort if a task completes but takes longer than necessary, or if you want a faster, more interactive working style.

See also: [Prompting Claude Fable 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5.md)

[Claude Opus 5](../../20-Models/models-opus-5-overview.md)

Claude Opus 5 supports all five effort levels. **Start with `high`, the default**, and adjust based on your evals: step up to `xhigh` for demanding coding and agentic work, or to `max` when a task justifies unconstrained token spending. Use `low` and `medium` liberally as your primary control for token cost and response time wherever your evals show quality holds. If you carried effort settings over from an earlier model, run a fresh effort sweep on your evals rather than reusing them.

Effort controls thinking volume, not visible response length: on Claude Opus 5, changing effort does not reliably shorten responses, so [prompt for length](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#response-length-and-verbosity) instead.

The API default is `high`. Set `effort` explicitly to use a different level. The value you pass overrides the default.

On Claude Opus 5, thinking cannot be disabled at `xhigh` or `max` effort: requests that set `thinking: {"type": "disabled"}` at those levels return a 400 error. See [Effort with thinking](#effort-with-thinking).

When running Claude Opus 5 at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act across subagents and tool calls. Starting at 64k tokens and tuning from there is a reasonable default.

Claude Opus 5 also supports [changing effort mid-conversation](#change-effort-mid-conversation-beta) with a per-message `output_config`, which preserves the prompt cache. Per-message effort isn’t available for Claude Opus 5 on Amazon Bedrock.

See also: [Prompting Claude Opus 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md)

[Claude Opus 4.8](../../20-Models/models-opus-4-8-overview.md)

The guidance for Claude Opus 4.7 also applies to Claude Opus 4.8. **Start with `xhigh` for coding and agentic use cases**, use `high` for most other intelligence-sensitive workloads, and step down to `medium` or `low` only when you’ve measured that the lower level holds quality on your evals.

The API default is `high`. Set `effort` explicitly to use a different level. The value you pass overrides the default.

When running Claude Opus 4.8 at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act across subagents and tool calls. Starting at 64k tokens and tuning from there is a reasonable default.

See also: [Prompting Claude Opus 4.8](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-4-8.md)

[Claude Opus 4.7](../../20-Models/models-opus-4-7-overview.md)

**Start with `xhigh` for coding and agentic use cases**, and use `high` as the minimum for most intelligence-sensitive workloads. Step down to `medium` for cost-sensitive workloads, or up to `max` only when your evals show measurable headroom at `xhigh`.

The API default is `high`. To use `xhigh`, set `effort` explicitly. The value you pass overrides the default.

- **Low effort:** Efficient, but best for short, scoped tasks. Pair `low` with explicit checklists if your task has multiple sections.
- **Medium effort:** The setting for the average workflow where you want good results while reducing costs.
- **High effort:** Advanced use cases that still need a balance of intelligence and token consumption. This is often the best balance of quality and token efficiency.
- **Xhigh effort:** The recommended starting point for coding and agentic work, and for exploratory tasks such as repeated tool calling, detailed web search, and knowledge-base search. Expect meaningfully higher token usage than `high`.
- **Max effort:** Reserve for frontier problems. On most workloads `max` adds significant cost for relatively small quality gains, and on some structured-output or less intelligence-sensitive tasks it can lead to overthinking.

Claude Opus 4.7 also respects effort levels more strictly than Claude Opus 4.6, especially at `low` and `medium`. At lower effort levels, the model scopes its work to what was asked rather than doing more than requested. If you observe shallow reasoning on complex problems with Claude Opus 4.7, raise effort rather than prompting around it. If you must keep effort low for latency, add targeted guidance such as “This task involves multistep reasoning. Think carefully before responding.”

When running Claude Opus 4.7 at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act across subagents and tool calls. Starting at 64k tokens and tuning from there is a reasonable default.

See also: [Prompting best practices](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md)

[Claude Sonnet 5](../../20-Models/models-sonnet-5-overview.md)

Claude Sonnet 5 defaults to `high` effort on the Claude API and Claude Code.

- **High effort (default):** Suitable for complex reasoning, coding, and agentic tasks where quality matters more than speed or cost.
- **Xhigh effort:** For the hardest coding and agentic tasks.
- **Medium effort:** Cost-saving step-down from the default. Comparable to Claude Sonnet 4.6 at high effort.
- **Low effort:** For high-volume or latency-sensitive workloads. Suitable for chat and non-coding use cases where faster turnaround is prioritized.
- **Max effort:** For tasks requiring the absolute highest capability with no constraints on token spending.

See also: [Prompting Claude Sonnet 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-sonnet-5.md#calibrating-effort-and-thinking-depth)

[Claude Sonnet 4.6](../../20-Models/models-sonnet-4-6-overview.md)

Sonnet 4.6 defaults to `high` effort. Explicitly set effort when using Sonnet 4.6 to avoid unexpected latency:

- **Medium effort (recommended default):** Best balance of speed, cost, and performance for most applications. Suitable for agentic coding, tool-heavy workflows, and code generation.
- **Low effort:** For high-volume or latency-sensitive workloads. Suitable for chat and non-coding use cases where faster turnaround is prioritized.
- **High effort:** For complex reasoning and tasks where quality matters more than speed or cost.
- **Max effort:** For tasks requiring the absolute highest capability with no constraints on token spending.

See also: [Prompting best practices](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md)

## Effort with tool use

When using tools, the effort parameter affects both the explanations around tool calls and the tool calls themselves. Lower effort levels tend to:

- Combine multiple operations into fewer tool calls
- Make fewer tool calls
- Proceed directly to action without preamble
- Use terse confirmation messages after completion

Higher effort levels might:

- Make more tool calls
- Explain the plan before taking action
- Provide detailed summaries of changes
- Include more comprehensive code comments

## Effort with thinking

The `thinking` parameter controls whether Claude thinks in [thinking blocks](build-with-claude-thinking.md) before answering; the `effort` parameter controls how much work Claude puts into the whole response, which in adaptive mode includes how often and how deeply it thinks. Don’t pass `adaptive` as an `effort` value: `adaptive` is a thinking mode, not an effort level.

At higher effort levels, Claude thinks more readily and at greater length. In a tool-use loop, follow-up requests that only process tool results can still skip thinking at any level. At lower levels, Claude can skip thinking entirely for simpler problems. See [Thinking and effort](build-with-claude-thinking.md#thinking-and-effort) for full guidance on how the two controls work together.

On Claude Opus 4.5, the only extended-thinking-only model that supports effort, it works alongside [`budget_tokens`](build-with-claude-extended-thinking.md): set the effort level for your task, then set the thinking token budget based on how much reasoning depth the task needs.

For per-model thinking availability, see the [per-model configuration table](build-with-claude-thinking-troubleshooting.md#supported-models). Effort works with or without thinking. See [How effort works](#how-effort-works).

## Change effort mid-conversation

You can run later turns of a conversation at a different effort level in two ways. On Claude Fable 5.1, Claude Mythos 5.1, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, and Claude Haiku 5.5, use a per-message effort change, which keeps the prompt cache. On other models, set a new top-level value on the next request, which starts the cache over.

### Per-message effort (beta)

Per-message effort is in beta. On the Claude API and [Claude Models on Google Cloud (Google managed)](build-with-claude-claude-models-on-google-cloud-google-managed.md), it’s available on Claude Fable 5.1, Claude Mythos 5.1, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, and Claude Haiku 5.5. On [Claude Models on Google Cloud (Anthropic managed)](build-with-claude-claude-models-on-google-cloud-anthropic-managed.md) and [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md), it’s available on Claude Fable 5.1, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, and Claude Haiku 5.5. On [Amazon Bedrock](build-with-claude-claude-in-amazon-bedrock.md), it’s available on Claude Fable 5.1, Claude Mythos 5.1, and Claude Opus 5.5. It requires the [beta header](../Endpoints/beta-headers.md) `mid-conversation-output-config-2026-07-01`. With the Amazon Bedrock [InvokeModel API](build-with-claude-claude-on-amazon-bedrock-legacy.md), it’s available on Claude Fable 5.1 and Claude Opus 5.5, and you send that value in the `anthropic_beta` array of the request body instead.

Without the beta value, a per-message `output_config` returns a 400 error: `messages.N.output_config: Extra inputs are not permitted`, where `N` is the index of the `system` message in `messages`. With the beta value, models without per-message effort, including Claude Fable 5, return a 400 error: `output_config.effort requires a model that supports per-turn effort; this model does not`. On Amazon Bedrock, those models and Claude Opus 5 return the `Extra inputs are not permitted` error instead. On Claude Sonnet 5.5 with `thinking: {"type": "between_tools"}` and on Claude Haiku 5.5 with `thinking: {"type": "disabled"}`, effort can’t change mid-conversation: a per-message `output_config.effort` that differs from the level in effect returns a 400 error. To vary effort for each turn, use adaptive thinking.

Add a `role: "system"` message with empty `content` and the new level in `output_config.effort`. Placed directly after a `user` turn with new input, it sets the level for Claude’s reply to that turn. Placed anywhere else, such as between an `assistant` turn and the next `user` turn as in the following example, it takes effect from the next `user` turn with new input. A `user` turn that holds only `tool_result` blocks doesn’t count as new input, so a change placed after one in a tool-use loop waits for the next `user` turn with new input. The new level then holds until a later message changes it. Everything before that message is unchanged, so the cached prefix still matches.

The following example starts at `high`, then drops to `low` for a routine follow-up:

cURL

CLI

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
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-fable-5-1",
    max_tokens=4096,
    output_config={"effort": "high"},
    messages=[
        {
            "role": "user",
            "content": "Plan a migration from SQLite to PostgreSQL in three short steps.",
        },
        {
            "role": "assistant",
            "content": "1. Export the SQLite data. 2. Create the PostgreSQL schema. 3. Import the data and verify row counts.",
        },
        # Effort-only system message: the new level takes effect from the next user turn.
        {"role": "system", "content": [], "output_config": {"effort": "low"}},
        {"role": "user", "content": "Summarize the plan in one sentence."},
    ],
    betas=["mid-conversation-output-config-2026-07-01"],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

An effort-only system message carries no text, so the [placement rules for mid-conversation system messages](build-with-claude-mid-conversation-system-messages.md#limitations) don’t apply. It can appear anywhere in `messages`, including as the first entry or between an `assistant` turn and the next `user` turn. Values are the level names (`low`, `medium`, `high`, `xhigh`, and `max`).

Prefer this form over changing the top-level value between requests. A top-level change restarts the cache and, on Claude Fable 5.1, also steers the model less reliably: its earlier replies were written at the previous level, and it tends to stay consistent with them.

### Top-level effort on the next request

The top-level `output_config.effort` applies to the whole request. To run a later part of a conversation at a different level, set the new value on the next request. Because top-level effort shapes the rendered prompt, changing it between requests doesn’t preserve cached prefixes from earlier turns. If you rely on [prompt caching](build-with-claude-prompt-caching.md) across a long session and your model doesn’t support per-message effort, pick an effort level at the start and keep it constant.

## Best practices

1.  **Set effort explicitly:** The API defaults to `high` (`medium` on Claude Opus 5.5 and Claude Haiku 5.5), but the right starting point depends on your model and workload.
2.  **Use low for speed-sensitive or simple tasks:** When latency matters or tasks are straightforward, low effort can significantly reduce response times and costs.
3.  **Test your use case:** The impact of effort levels varies by task type. Evaluate performance on your specific use cases before deploying.
4.  **Consider dynamic effort:** Adjust effort based on task complexity. Simple queries might warrant low effort, whereas agentic coding and complex reasoning benefit from high effort. See the next item before varying it within one conversation.
5.  **Hold top-level effort constant within cached conversations:** Changing the top-level effort value between requests invalidates [prompt caching](build-with-claude-prompt-caching.md), so vary it across workloads rather than within a conversation that relies on cache hits. On models that support it, use a [per-message effort change](#change-effort-mid-conversation-beta) instead, which preserves the cache. See [Thinking and prompt caching](build-with-claude-thinking.md#thinking-and-prompt-caching).

## Next steps



[Task budgets](build-with-claude-task-budgets.md)

Give Claude an advisory token budget for the full agentic loop to help the model self-regulate on long agentic tasks.

[Steering thinking](build-with-claude-thinking-steering-and-cost.md)

Understand adaptive thinking, where Claude determines when and how much to think, and steer it with effort and prompting.



[Thinking](build-with-claude-thinking.md)

Understand how thinking works, when Claude thinks by default, and how thinking interacts with effort.

## Availability

Effort is available on select models and eligible for zero data retention and HIPAA readiness.

### API support

[Messages API](build-with-claude-working-with-messages.md)

Usage

Always on

Set `output_config.effort` on the request. With no value, the model’s default level applies.

StatusAvailable

Cloud platforms

- All supported platforms

Models

- [Claude Haiku 4.5](../../20-Models/models-haiku-4-5-overview.md)Not supported
- [Claude Sonnet 4.5](../../20-Models/models-sonnet-4-5-overview.md)Not supported
- All other models

[Managed Agents](../Other/managed-agents-overview.md)

Usage

Always on

Set `effort` on the agent’s model object, or in a session’s model override. With no value, Managed Agents fills in the model’s default.

StatusAvailable

Cloud platforms

- Claude API
- [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)

Models

- [Claude Haiku 4.5](../../20-Models/models-haiku-4-5-overview.md)Not supported
- [Claude Sonnet 4.5](../../20-Models/models-sonnet-4-5-overview.md)Not supported
- All other models

### Data handling

[Data handling overview](../Other/manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/messages` with `effort`

Zero data retentionEligible

Excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

HIPAAEligible
