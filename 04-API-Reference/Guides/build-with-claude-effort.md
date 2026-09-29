---
title: "Effort - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/effort"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:21Z"
tags: ["api"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Feffort)

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

[Messages](../../01-Getting-Started/intro.md)Model capabilities

# Effort

Copy page



Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency.

Copy page



Effort

[ZDR](../Other/manage-claude-api-and-data-retention.md)

Eligible

excludes [Covered Models](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

The effort parameter lets you control how many tokens Claude spends when responding to requests. You can trade off between response thoroughness and token efficiency with a single model. The top-level effort parameter is available on all supported models with no beta header required. [Per-message effort](#change-effort-mid-conversation-beta) is in beta.



To learn how effort interacts with thinking and which control to reach for, see [Thinking and effort](build-with-claude-thinking.md#thinking-and-effort). Where adaptive thinking is available, effort is the recommended way to control thinking depth.

## Set the effort level

Set `output_config.effort` on the request. The following example runs one request at `medium` effort and prints the response text.

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

Most Claude models default to high effort, spending as many tokens as needed for excellent results; Claude Opus 5.5 defaults to medium. You can raise the effort level to `max` for the absolute highest capability, or lower it to be more conservative with token usage, optimizing for speed and cost while accepting some reduction in capability.



Setting `effort` to the model's default (`"medium"` on Claude Opus 5.5, `"high"` on other models) produces exactly the same behavior as omitting the `effort` parameter entirely.

The effort parameter affects **all tokens** in the response, including:

- Text responses and explanations
- Tool calls and function arguments
- Thinking (when active)

Because effort applies to every output token, it works whether or not thinking is enabled. Lower effort also means fewer and terser tool calls.

### Effort levels

| Level    | Description                                                                                                                                                                                                                                                                                             | Typical use case                                                                           |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| `max`    | Absolute maximum capability with no constraints on token spending. Available on Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, Claude Mythos 5, Claude Mythos Preview, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5, and Claude Sonnet 4.6. | Tasks requiring the deepest possible reasoning and most thorough analysis                  |
| `xhigh`  | Extended capability for long-horizon work. Available on Claude Fable 5.1, Claude Mythos 5.1, Claude Fable 5, Claude Mythos 5, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.8, Claude Opus 4.7, and Claude Sonnet 5.                                                                                    | Long-running agentic and coding tasks (over 30 minutes) with token budgets in the millions |
| `high`   | Spends as many tokens as the task needs for excellent results. The default on every model that supports effort except Claude Opus 5.5.                                                                                                                                                                  | Complex reasoning, difficult coding problems, agentic tasks                                |
| `medium` | Balanced approach with moderate token savings. The default on Claude Opus 5.5.                                                                                                                                                                                                                          | Agentic tasks that require a balance of speed, cost, and performance                       |
| `low`    | Most efficient. Significant token savings with some capability reduction.                                                                                                                                                                                                                               | Simpler tasks that need the best speed and lowest costs, such as subagents                 |

Not every model that supports `max` supports `xhigh`.



Effort is a behavioral signal, not a strict token budget. At lower effort levels, Claude still thinks on sufficiently difficult problems, but thinks less than it would at higher effort levels for the same problem.

The per-model recommendations that follow override this table where they differ.

### Recommended effort levels for Claude Fable 5.1

Claude Fable 5.1 supports all five effort levels. **Start with `high`, the default.** Step up to `xhigh` or `max` for the most capability-sensitive agentic and coding work, and step down to `medium` or `low` for routine or latency-sensitive work once your evals show quality holds. At `high` and above, set a large `max_tokens`. It's a hard limit on total output (thinking plus response text). The same recommendations apply to Claude Mythos 5.1. See [Prompting Claude Fable 5.1](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5-1.md#consider-all-effort-levels).

Claude Fable 5.1 also supports [changing effort mid-conversation](#change-effort-mid-conversation-beta) with a per-message `output_config`, which preserves the prompt cache.

### Recommended effort levels for Claude Fable 5

Effort is the primary control for trading off intelligence, latency, and cost on Claude Fable 5. **Start with `high`, the default, for most tasks**, use `xhigh` for the most capability-sensitive workloads, and step down to `medium` or `low` for routine work. Lower effort settings on Claude Fable 5 still perform well and often exceed `xhigh` performance on prior models. At `high` and `xhigh`, set a large `max_tokens`. It's a hard limit on total output (thinking plus response text). See [Cost control](build-with-claude-thinking-steering-and-cost.md#cost-control).

Reduce effort if a task completes but takes longer than necessary, or if you want a faster, more interactive working style. The same recommendations apply to Claude Mythos 5. For fuller guidance, see [Prompting Claude Fable 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5.md).

### Recommended effort levels for Claude Opus 5.5

Claude Opus 5.5 supports all five effort levels, and `medium` is the default (Claude Opus 5 and earlier Opus models default to `high`, so a request that omits `effort` runs one level lower than it did on Claude Opus 5). Adaptive thinking is always on and can't be turned off, so effort is the primary control for how much the model reasons and what a request costs. Run an effort sweep on your own evals rather than carrying settings over from an earlier model, and set a large `max_tokens` at the higher levels: it's a hard limit on total output (thinking plus response text). Requests that set `thinking: {"type": "disabled"}` return a 400 error at every effort level. Claude Opus 5.5 also supports [changing effort mid-conversation](#change-effort-mid-conversation-beta) with a per-message `output_config`, which preserves the prompt cache. See [Prompting Claude Opus 5.5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md).

### Recommended effort levels for Claude Opus 5

Claude Opus 5 supports all five effort levels. **Start with `high`, the default**, and adjust based on your evals: step up to `xhigh` for demanding coding and agentic work, or to `max` when a task justifies unconstrained token spending, and use `low` and `medium` liberally as your primary control for token cost and response time wherever your evals show quality holds. If you carried effort settings over from an earlier model, run a fresh effort sweep on your evals rather than reusing them.

Effort controls thinking volume, not visible response length: on Claude Opus 5, changing effort does not reliably shorten responses, so [prompt for length](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#response-length-and-verbosity) instead.

The API default is `high`. Set `effort` explicitly to use a different level. The value you pass overrides the default.

On Claude Opus 5, thinking cannot be disabled at `xhigh` or `max` effort: requests that set `thinking: {"type": "disabled"}` at those levels return a 400 error. See [Effort with thinking](#effort-with-thinking).

When running Claude Opus 5 at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act across subagents and tool calls. Starting at 64k tokens and tuning from there is a reasonable default.

Claude Opus 5 also supports [changing effort mid-conversation](#change-effort-mid-conversation-beta) with a per-message `output_config`, which preserves the prompt cache.

### Recommended effort levels for Claude Opus 4.8

The guidance for Claude Opus 4.7 also applies to Claude Opus 4.8. **Start with `xhigh` for coding and agentic use cases**, use `high` for most other intelligence-sensitive workloads, and step down to `medium` or `low` only when you've measured that the lower level holds quality on your evals.

The API default is `high`. Set `effort` explicitly to use a different level. The value you pass overrides the default.

When running Claude Opus 4.8 at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act across subagents and tool calls. Starting at 64k tokens and tuning from there is a reasonable default.

### Recommended effort levels for Claude Opus 4.7

**Start with `xhigh` for coding and agentic use cases**, and use `high` as the minimum for most intelligence-sensitive workloads. Step down to `medium` for cost-sensitive workloads, or up to `max` only when your evals show measurable headroom at `xhigh`.

The API default is `high`. To use `xhigh`, set `effort` explicitly. The value you pass overrides the default.

| Effort   | Guidance for Claude Opus 4.7                                                                                                                                                                                             |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `low`    | Efficient, but best for short, scoped tasks. Pair `low` with explicit checklists if your task has multiple sections.                                                                                                     |
| `medium` | The drop-in for the average workflow where you want good results while reducing costs.                                                                                                                                   |
| `high`   | Advanced use cases that still need a balance of intelligence and token consumption. This is often the best balance of quality and token efficiency.                                                                      |
| `xhigh`  | The recommended starting point for coding and agentic work, and for exploratory tasks such as repeated tool calling, detailed web search, and knowledge-base search. Expect meaningfully higher token usage than `high`. |
| `max`    | Reserve for frontier problems. On most workloads `max` adds significant cost for relatively small quality gains, and on some structured-output or less intelligence-sensitive tasks it can lead to overthinking.         |

Claude Opus 4.7 also respects effort levels more strictly than Claude Opus 4.6, especially at `low` and `medium`. At lower effort levels, the model scopes its work to what was asked rather than doing more than requested. If you observe shallow reasoning on complex problems with Claude Opus 4.7, raise effort rather than prompting around it. If you must keep effort low for latency, add targeted guidance like "This task involves multistep reasoning. Think carefully before responding."

When running Claude Opus 4.7 at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act across subagents and tool calls. Starting at 64k tokens and tuning from there is a reasonable default.

### Recommended effort levels for Claude Sonnet 5

Claude Sonnet 5 defaults to `high` effort on the Claude API and Claude Code.

- **High effort (default):** Suitable for complex reasoning, coding, and agentic tasks where quality matters more than speed or cost.
- **Xhigh effort:** For the hardest coding and agentic tasks. See [Prompting Claude Sonnet 5](../../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-sonnet-5.md#calibrating-effort-and-thinking-depth).
- **Medium effort:** Cost-saving step-down from the default. Comparable to Claude Sonnet 4.6 at high effort.
- **Low effort:** For high-volume or latency-sensitive workloads. Suitable for chat and non-coding use cases where faster turnaround is prioritized.
- **Max effort:** For tasks requiring the absolute highest capability with no constraints on token spending.

### Recommended effort levels for Claude Sonnet 4.6

Sonnet 4.6 defaults to `high` effort. Explicitly set effort when using Sonnet 4.6 to avoid unexpected latency:

- **Medium effort** (recommended default): Best balance of speed, cost, and performance for most applications. Suitable for agentic coding, tool-heavy workflows, and code generation.
- **Low effort:** For high-volume or latency-sensitive workloads. Suitable for chat and non-coding use cases where faster turnaround is prioritized.
- **High effort:** For complex reasoning and tasks where quality matters more than speed or cost.
- **Max effort:** For tasks requiring the absolute highest capability with no constraints on token spending.

## Effort with tool use

When using tools, the effort parameter affects both the explanations around tool calls and the tool calls themselves. Lower effort levels tend to:

- Combine multiple operations into fewer tool calls
- Make fewer tool calls
- Proceed directly to action without preamble
- Use terse confirmation messages after completion

Higher effort levels may:

- Make more tool calls
- Explain the plan before taking action
- Provide detailed summaries of changes
- Include more comprehensive code comments

## Effort with thinking

The `thinking` parameter controls whether Claude thinks in [thinking blocks](build-with-claude-thinking.md) before answering; the `effort` parameter controls how much work Claude puts into the whole response, which in adaptive mode includes how often and how deeply it thinks. Don't pass `adaptive` as an `effort` value: `adaptive` is a thinking mode, not an effort level.

At higher effort levels, Claude thinks more readily and at greater length. In a tool-use loop, follow-up requests that only process tool results can still skip thinking at any level. At lower levels, Claude can skip thinking entirely for simpler problems. See [Thinking and effort](build-with-claude-thinking.md#thinking-and-effort) for full guidance on how the two controls work together.

On Claude Opus 4.5, the only extended-thinking-only model that supports effort, it works alongside [`budget_tokens`](build-with-claude-extended-thinking.md): set the effort level for your task, then set the thinking token budget based on how much reasoning depth the task needs.

For per-model thinking availability, see the [per-model configuration table](build-with-claude-thinking-troubleshooting.md#supported-models). Effort works with or without thinking. See [How effort works](#how-effort-works).

## Change effort mid-conversation

You can run later turns of a conversation at a different effort level in two ways. On Claude Fable 5.1, Claude Mythos 5.1, Claude Opus 5.5, and Claude Opus 5, use a per-message effort change, which keeps the prompt cache. On other models, set a new top-level value on the next request, which starts the cache over.

### Per-message effort (beta)

Per-message effort is in beta and requires the [beta header](../Endpoints/beta-headers.md) `mid-conversation-output-config-2026-07-01`. Models without per-message effort, including Claude Fable 5, return a 400 error: `output_config.effort requires a model that supports per-turn effort; this model does not`.

Add a `role: "system"` message with empty `content` and the new level in `output_config.effort`. The new level takes effect from the next `user` turn and holds until a later message changes it. Everything before that message is unchanged, so the cached prefix still matches.

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

An effort-only system message carries no text, so the [placement rules for mid-conversation system messages](build-with-claude-mid-conversation-system-messages.md#limitations) don't apply. It can appear anywhere in `messages`, including as the first entry or between an `assistant` turn and the next `user` turn. Values are the level names (`low`, `medium`, `high`, `xhigh`, and `max`).

On Claude Fable 5.1, prefer this form over changing the top-level value between requests. A top-level change restarts the cache and also steers the model less reliably: its earlier replies were written at the previous level, and it tends to stay consistent with them.

### Top-level effort on the next request

The top-level `output_config.effort` applies to the whole request. To run a later part of a conversation at a different level, set the new value on the next request. Because top-level effort shapes the rendered prompt, changing it between requests doesn't preserve cached prefixes from earlier turns. If you rely on [prompt caching](build-with-claude-prompt-caching.md) across a long session and your model doesn't support per-message effort, pick an effort level at the start and keep it constant.

## Best practices

1.  **Set effort explicitly:** The API defaults to `high` (`medium` on Claude Opus 5.5), but the right starting point depends on your model and workload.
2.  **Use low for speed-sensitive or simple tasks:** When latency matters or tasks are straightforward, low effort can significantly reduce response times and costs.
3.  **Test your use case:** The impact of effort levels varies by task type. Evaluate performance on your specific use cases before deploying.
4.  **Consider dynamic effort:** Adjust effort based on task complexity. Simple queries may warrant low effort while agentic coding and complex reasoning benefit from high effort. See the next item before varying it within one conversation.
5.  **Hold top-level effort constant within cached conversations:** Changing the top-level effort value between requests invalidates [prompt caching](build-with-claude-prompt-caching.md), so vary it across workloads rather than within a conversation that relies on cache hits. On models that support it, use a [per-message effort change](#change-effort-mid-conversation-beta) instead, which preserves the cache. See [Thinking and prompt caching](build-with-claude-thinking.md#thinking-and-prompt-caching).

## Next steps



[Task budgets](build-with-claude-task-budgets.md)

Give Claude an advisory token budget for the full agentic loop to help the model self-regulate on long agentic tasks.

[Steering thinking](build-with-claude-thinking-steering-and-cost.md)

Understand adaptive thinking, where Claude decides when and how much to think, and steer it with effort and prompting.



[Thinking](build-with-claude-thinking.md)

Understand how thinking works, when Claude thinks by default, and how thinking interacts with effort.

## Compatibility

Supported models  
- Fable 5 and 5.1
- Mythos 5, 5.1, and Preview
- Opus 4.5, 4.6, 4.7, 4.8, 5, and 5.5
- Sonnet 4.6 and 5

Supported platforms  
- Claude API
- Claude Platform on AWS
- Amazon Bedrock
- Google Cloud
- Microsoft Foundry
