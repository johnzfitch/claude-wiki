---
title: "Steering thinking - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:27Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fthinking-steering-and-cost)

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

[Overview](build-with-claude-thinking.md)[Steering and cost control](build-with-claude-thinking-steering-and-cost.md)[Tool and multi-turn workflows](build-with-claude-thinking-tool-workflows.md)[Preserved thinking](build-with-claude-preserved-thinking.md)[Troubleshooting](build-with-claude-thinking-troubleshooting.md)[Extended thinking (legacy)](build-with-claude-extended-thinking.md)

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

[Messages](../../01-Getting-Started/intro.md)Thinking

# Steering thinking

Copy page



Steer how often and how deeply Claude thinks with effort levels, system prompt guidance, and per-message steering, and understand thinking's cost and pricing.

Copy page





To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

Claude's thinking is adaptive: the model evaluates each request and decides for itself whether to think and how much. You set an intent, optionally specify the effort, and the model allocates reasoning where it judges reasoning will help.

This makes thinking a strong fit for workloads that mix trivial and complex requests, and for long-horizon agentic workflows where the right amount of reasoning varies from step to step.

To learn how to turn thinking on, how to read thinking output, and about [thinking output on Claude Fable 5 and Claude Mythos 5](build-with-claude-thinking.md#thinking-output-on-claude-fable-5-and-claude-mythos-5), see the [Thinking](build-with-claude-thinking.md) overview. This page covers how Claude decides when to think, how to steer that decision, and the caching, cost, and pricing mechanics that follow from it.

## How Claude decides when to think

Thinking is optional for the model. On each request, Claude weighs the complexity of the input and decides whether deeper reasoning would improve the answer. A simple factual question may get a direct response with no thinking block at all; a multistep math problem or a tricky debugging task triggers deeper reasoning.

The decision happens per request. The same conversation can contain turns with and without thinking, and a turn where Claude chose not to think contains no thinking block. Don't build application logic that assumes every assistant turn starts with one.

The primary control over this decision is the [effort](build-with-claude-effort.md) parameter, which acts as soft guidance for how willing Claude should be to think and how deeply; see [Effort levels](#effort-levels) on this page for what each level does.

If you want Claude to think less often, lower the effort level before reaching for prompt-based steering.

Thinking also interleaves with tool use automatically: Claude can think between tool calls, reflecting on each tool result before deciding what to do next ([interleaved thinking](build-with-claude-thinking.md#interleaved-thinking)). You don't need a beta header or any additional configuration for this.

For the full picture of how the thinking configuration and the effort parameter interact, see [Thinking and effort](build-with-claude-thinking.md#thinking-and-effort).

## Steering how often Claude thinks

Whether Claude thinks on a given turn is promptable. Effort sets the overall posture, but you can also shape the decision directly with natural-language guidance, either globally in the system prompt or per message from the user turn.

Use the two levers together in this order:

1.  Set the effort level that matches your workload's default balance of quality and latency.
2.  Add prompt guidance only if Claude's triggering still doesn't match your needs at that level.

For broader prompting guidance with thinking, see [leverage thinking and interleaved thinking capabilities](../../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md#leverage-thinking-and-interleaved-thinking-capabilities).

### Effort levels

Effort is the primary steering lever for thinking. Each level sets a different default for how often Claude thinks and how deeply:

| Effort level                          | Thinking behavior                                                                                |
|:--------------------------------------|:-------------------------------------------------------------------------------------------------|
| `max`                                 | Claude thinks the most readily and at the greatest depth, with no constraint on thinking length. |
| `xhigh`                               | Claude thinks more readily and at greater depth than at `high`, suited to extended exploration.  |
| `high` (default on most models)       | Claude thinks on most requests that benefit from it. Provides deep reasoning on complex tasks.   |
| `medium` (default on Claude Opus 5.5) | Claude uses moderate thinking. May skip thinking for simple queries.                             |
| `low`                                 | Claude minimizes thinking. Skips thinking for simple tasks where speed matters most.             |

At every level, Claude decides per request whether to think. In a tool-use loop, the first request after new user input typically carries most of the reasoning, and follow-up requests that only process tool results can skip thinking, including at `xhigh` and `max`. Thinking per request also tends to decrease as a conversation grows longer. No level guarantees a thinking block on every request.

This table describes how each level changes thinking behavior. For guidance on which level to choose for a given workload, including per-model recommendations, see [When to adjust the effort parameter](build-with-claude-effort.md#when-to-adjust-the-effort-parameter) on the effort page.

Effort is set at `output_config.effort`, not inside the `thinking` object; for full per-language examples, see [Effort](build-with-claude-effort.md#basic-usage).

```python
{
  "model": "claude-opus-5-5",
  "max_tokens": 4096,
  "output_config": { "effort": "medium" },
  "messages": [{ "role": "user", "content": "..." }]
}
```



Level availability varies by model; the [effort availability table](build-with-claude-effort.md#effort-levels) on the effort page is the authority for which levels each model supports.

### System prompt guidance

System prompt guidance shifts Claude's thinking threshold for every request in the conversation. If Claude is thinking more often than your workload needs, add guidance like this to your system prompt:

``` block
Extended thinking adds latency and should only be used when it
will meaningfully improve answer quality, typically for problems
that require multistep reasoning. When in doubt, respond directly.
```



To encourage thinking instead, use a phrase like:

``` block
This task involves multistep reasoning. Think carefully before responding.
```



Steering effectiveness can be sensitive to exact wording. If one phrasing doesn't produce the behavior you want, try a more direct variant.

### Per-message steering

You can also steer thinking on a per-message basis from the user turn, independently of the system prompt. Appending `"Please think hard before responding."` to a user message encourages Claude to think on that turn; `"Answer directly without deliberating."` suppresses it.

Per-message steering is useful when only some requests in a conversation warrant extended reasoning. An agent harness, for example, can append the encouraging phrase on planning steps and the suppressing phrase on routine confirmations, without touching the system prompt or changing any request parameters between turns.

### Verify steering on your workload

Prompt-based steering changes model behavior, so treat it like any other prompt change: measure before you ship. Run a representative sample of your traffic with and without the guidance, and compare how often thinking triggers (the presence of thinking blocks in responses), output token usage, latency, and answer quality on the cases that matter to you.



Steering Claude to think less often may reduce quality on tasks that benefit from reasoning. Lowering the [effort](build-with-claude-effort.md) level is usually the better first lever, since it is a calibrated control rather than a wording-sensitive instruction. Measure the impact on your specific workloads before deploying prompt-based tuning to production.

## Mechanics

Three mechanics follow from Claude managing its own thinking: turn validation, prompt caching, and how you bound cost.

### Turn validation

Assistant turns don't need to start with a thinking block. (Models using a legacy manual thinking budget enforce that the final assistant turn of a thinking-enabled request begins with one; see [Turn structure in manual mode](build-with-claude-extended-thinking.md#turn-structure-in-manual-mode).)

For multi-turn applications, this means you can pass back conversation history in whatever shape you have it:

- Assistant turns where Claude chose not to think are valid history as-is.
- You can resume a conversation that began without thinking, or that used a different thinking configuration, without rewriting its history.
- History assembled from mixed sources doesn't need thinking blocks reinserted at the start of each assistant turn to pass validation.

The relaxation is about validation, not about what you should send. When you have thinking blocks, pass them back unmodified, particularly during tool use, where they carry the reasoning behind Claude's tool calls. See the [Thinking](build-with-claude-thinking.md) overview for the full rules.

### Prompt caching

Consecutive requests that keep the same thinking configuration and effort level preserve prompt caching; see [Thinking and prompt caching](build-with-claude-thinking.md#thinking-and-prompt-caching) for the full rules. The resolved effort value is rendered into the prompt, so changing it between requests invalidates cache breakpoints, just as changing the legacy [`budget_tokens`](build-with-claude-extended-thinking.md#extended-thinking-with-prompt-caching) parameter does on models that use it. Setting `effort` explicitly to the model's default is equivalent to omitting it and does not break the cache.

The practical consequence: pick a thinking configuration and an effort level per conversation and keep them. If some turns need more or less thinking, steer with [per-message prompting](#tuning-thinking-behavior): guidance appended to the newest user message leaves earlier cache breakpoints intact, where a configuration or effort change does not.

The following example demonstrates the invalidation with a multi-turn script you can run yourself:

### Effort changes invalidate the prompt cache

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

```python
import requests

client = Anthropic()


def fetch_article_content(url):
    text = requests.get(url).text
    lines = (line.strip() for line in text.splitlines())
    return "\n".join(line for line in lines if line)


# Fetch the content of the article
book_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
book_content = fetch_article_content(book_url)
# Use just enough text for caching (first few chapters)
LARGE_TEXT = book_content[:10000]

# No system prompt - caching in messages instead
MESSAGES = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": LARGE_TEXT,
                "cache_control": {"type": "ephemeral"},
            },
            {"type": "text", "text": "Analyze the tone of this passage."},
        ],
    }
]

# First request - establish cache
print("First request - establishing cache")
response1 = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=MESSAGES,
)

print(f"First response usage: {response1.usage}")

MESSAGES.append({"role": "assistant", "content": response1.content})
MESSAGES.append({"role": "user", "content": "Analyze the characters in this passage."})

# Second request - same configuration (cache hit expected)
print("\nSecond request - same configuration (cache hit expected)")
response2 = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=MESSAGES,
)

print(f"Second response usage: {response2.usage}")

MESSAGES.append({"role": "assistant", "content": response2.content})
MESSAGES.append({"role": "user", "content": "Analyze the setting in this passage."})

# Third request - different effort level (cache miss expected)
print("\nThird request - different effort level (cache miss expected)")
response3 = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "low"},
    messages=MESSAGES,
)

print(f"Third response usage: {response3.usage}")
```



Here is the output of the script (you may see slightly different numbers):

Output



``` block
First request - establishing cache
First response usage: { cache_creation_input_tokens: 3546, cache_read_input_tokens: 0, input_tokens: 15, output_tokens: 1033 }

Second request - same configuration (cache hit expected)
Second response usage: { cache_creation_input_tokens: 0, cache_read_input_tokens: 3546, input_tokens: 1062, output_tokens: 1630 }

Third request - different effort level (cache miss expected)
Third response usage: { cache_creation_input_tokens: 3546, cache_read_input_tokens: 0, input_tokens: 2706, output_tokens: 1468 }
```

With the cache breakpoint in the messages array, changing effort from `medium`, the default on Claude Opus 5.5, to `low` invalidates it: the third request shows `cache_creation_input_tokens=3546` and `cache_read_input_tokens=0` where the second showed a full cache read.

### Cost control

You don't set a thinking token budget. Two controls bound cost:

- `max_tokens` is a hard cap on total output for the request, thinking and response text combined. Claude never generates past it. In a tool-use loop, each request in the turn has its own `max_tokens`, so it doesn't bound the whole turn's spend.
- `effort` is soft guidance on how much of that output Claude allocates to thinking. It shapes behavior but doesn't guarantee a token count.

Because thinking counts toward `max_tokens`, set it high enough to leave room for both the reasoning and the answer. A `max_tokens` sized for a response with no thinking is often too small once Claude starts thinking on hard requests.

At `high` effort and above, Claude may think extensively and is more likely to exhaust the budget. If you see [`stop_reason: "max_tokens"`](build-with-claude-thinking-troubleshooting.md#stopped-at-max-tokens) in responses, you have two remedies:

- Raise `max_tokens` to give the model more room for thinking plus the answer.
- Lower the effort level so Claude thinks less and leaves more of the budget for response text.

Which one is right depends on whether the truncated responses needed the reasoning. If quality on those requests matters, raise the cap; if they were over-thought, lower the effort.

## Pricing

Thinking incurs charges for:

- Tokens Claude uses while thinking (billed as output tokens)
- Thinking blocks from prior assistant turns that remain in context, per the [preservation default](build-with-claude-thinking.md#thinking-block-preservation-by-model): all turns by default on keep-all models, only the last turn elsewhere (billed as input tokens)
- Standard text output tokens



When thinking is active, a specialized system prompt is automatically included to support this feature.

What you're billed for is the same regardless of the `display` setting; only what you see changes:

|                             | `display: "summarized"`                              | `display: "omitted"`                                 |
|:----------------------------|:-----------------------------------------------------|:-----------------------------------------------------|
| **Input tokens**            | Tokens in your original request                      | Same as summarized                                   |
| **Output tokens (billed)**  | The full thinking tokens Claude generated internally | Same as summarized                                   |
| **Output tokens (visible)** | The summarized thinking text                         | Zero thinking tokens (the `thinking` field is empty) |
| **Summary generation**      | No charge                                            | Not applicable                                       |



The billed output token count does **not** match the visible token count in the response. You are billed for the full thinking process, not the thinking content visible in the response.

To see how many billed output tokens were spent on internal reasoning, read `usage.output_tokens_details.thinking_tokens` in the response. This value reflects the raw reasoning the model generated (not the summarized text returned in the body) and is always less than or equal to `output_tokens`. Subtract it from `output_tokens` to approximate the non-reasoning portion of the output. When streaming, this breakdown appears only on the final `message_delta` event.

```python
{
  "usage": {
    "input_tokens": 25,
    "output_tokens": 348,
    "output_tokens_details": {
      "thinking_tokens": 312
    }
  }
}
```



`output_tokens` remains the inclusive, authoritative total used for billing. `output_tokens_details` is a read-only breakdown for observability. For complete pricing information including base rates, cache writes, cache hits, and output tokens, see [Pricing](../../17-Billing-Plans/about-claude-pricing.md).

## Next steps



[Thinking](build-with-claude-thinking.md)

Turn thinking on, read thinking output, and check per-model support.



[Thinking in tool and multi-turn workflows](build-with-claude-thinking-tool-workflows.md)

Preserve thinking blocks across tool calls and manage thinking in multi-turn conversations.



[Effort](build-with-claude-effort.md)

Control how much thinking and output Claude allocates per request.
