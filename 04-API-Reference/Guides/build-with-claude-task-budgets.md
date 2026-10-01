---
title: "Task budgets - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/task-budgets"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Ftask-budgets)

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

# Task budgets

Copy page



Give Claude an advisory token budget for the full agentic loop to help the model self-regulate on long agentic tasks.

Copy page



Task budgets

[Beta](build-with-claude-overview.md#feature-availability)

[Beta header](../Endpoints/beta-headers.md)

task-budgets-2026-03-13

Task budgets let you tell Claude how many tokens it has for a full agentic loop, including thinking, tool calls, tool results, and output. The model sees a running countdown and uses it to prioritize work and finish gracefully as the budget is consumed.

## When to use task budgets

Task budgets work best for agentic workflows where Claude makes multiple tool calls and decisions before finalizing its output to await the next human response. Use them when:

- You want Claude to self-regulate token spend on long-horizon tasks.
- You have a predictable per-task cost or latency ceiling to enforce.
- You want the model to finish gracefully (summarize findings, report progress) as it approaches the budget rather than cutting off mid-action.

Task budgets complement the [effort parameter](build-with-claude-effort.md): effort controls how thoroughly Claude reasons about each step, while task budgets cap the total work Claude can do across an agentic loop.

## Setting a task budget

Add `task_budget` to `output_config` and include the beta header:

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

with client.beta.messages.stream(
    model="claude-opus-5-5",
    max_tokens=128000,
    output_config={
        "effort": "high",
        "task_budget": {"type": "tokens", "total": 64000},
    },
    messages=[
        {"role": "user", "content": "Review the codebase and propose a refactor plan."}
    ],
    betas=["task-budgets-2026-03-13"],
) as stream:
    response = stream.get_final_message()

print(response.usage)
```

The `task_budget` object has three fields:

- `type`: always `"tokens"`.
- `total`: the number of tokens Claude can spend across the agentic loop, including thinking, tool calls, tool results, and output.
- `remaining` (optional): the budget remainder carried over from a prior request. Defaults to `total` when omitted.

## How the budget countdown works

Claude sees a budget-countdown marker injected server-side throughout the conversation. The marker shows how many tokens remain in the current agentic loop and updates as the model generates thinking, tool calls, and output, and as it processes tool results. Claude uses this signal to pace itself and finish gracefully as the budget is consumed.



**The countdown is visible only to the model.** API responses do not include a remaining-budget field: there is no `task_budget` information in the response `usage` object, and SDKs have no accessor for it. To track spend client-side, sum token usage across the requests in your loop as shown in [Measure your current usage](#measure-your-current-usage), or pass your own figure forward with `remaining` when [carrying a budget across compaction](#carrying-a-budget-across-compaction-with-remaining).



**The countdown reflects tokens Claude has processed in the current agentic loop, not tokens you resend between requests.** If your client sends the full conversation history on every follow-up request, your client-side token count might differ from the budget Claude is tracking. If you also decrement `remaining` while resending full history, the model sees an under-reported budget and the countdown drops faster than it should, causing Claude to wrap up earlier than the budget actually allows. Set a generous budget and let the model self-regulate against the countdown rather than trying to mirror it client-side.

### What counts as a turn

The budget covers one agentic turn, also called an agentic loop: everything Claude does in response to one user message that carries no tool results. A turn can span several requests.

A user message that carries no tool results starts a new turn with a fresh budget. Today, the countdown still counts earlier turns' history while it remains in the context. A common case is a follow-up after Claude has ended its turn, for example because the budget ran out:

```python
{ "role": "user", "content": "Continue." }
```



A user message that contains `tool_result` blocks continues the current turn, because your client is resolving tool calls that are part of that turn:

```python
{
  "role": "user",
  "content": [
    { "type": "tool_result", "tool_use_id": "toolu_01", "content": "<npm audit output>" }
  ]
}
```



That holds even when the message adds new content alongside the tool results:

```python
{
  "role": "user",
  "content": [
    { "type": "tool_result", "tool_use_id": "toolu_01", "content": "<npm audit output>" },
    { "type": "text", "text": "Also check the Dockerfile." }
  ]
}
```



Server-side [compaction](build-with-claude-compaction-threshold.md) during a turn does not reset the budget: tokens the turn consumed before the compaction still count against it. Tokens from before the turn began do not count, even when a compaction at the start of a turn summarizes them. Today, that exclusion applies only to the budget carried across a server-side compaction; earlier turns' history still counts while it remains in the context.

### Worked example: budget counting across requests

The task budget counts what Claude **sees** (thinking, tool calls and results, and text), not what's in your request payload. In an agentic loop your client resends the full conversation on every request, so the payload keeps growing, but the budget only decrements by what is new: the tokens Claude generates and the content it has not seen before. The following example is one [agentic turn](#what-counts-as-a-turn) made of three requests: the first carries the user message, and the next two each resend the history with a tool result appended.

Consider a loop with `task_budget: {type: "tokens", total: 100000}` and a single `bash` tool.

**Request 1.** You send the initial request:

```python
{
  "messages": [
    { "role": "user", "content": "Audit this repo for security issues and report findings." }
  ]
}
```



Claude thinks, then emits a tool call and stops with `stop_reason: "tool_use"`:

```python
{
  "role": "assistant",
  "content": [
    {
      "type": "thinking",
      "thinking": "I'll start by listing dependencies to look for known-vulnerable packages..."
    },
    {
      "type": "tool_use",
      "id": "toolu_01",
      "name": "bash",
      "input": { "command": "cat package.json && npm audit --json" }
    }
  ]
}
```



Suppose this assistant message (thinking plus the tool call) totals 5,000 generated tokens. The countdown Claude saw during generation ended near `remaining` ≈ 95,000.

**Request 2.** Your client runs the tool, then resends the full history with the tool result appended:

```python
{
  "messages": [
    { "role": "user", "content": "Audit this repo for security issues and report findings." },
    {
      "role": "assistant",
      "content": [
        { "type": "thinking", "thinking": "I'll start by listing dependencies..." },
        {
          "type": "tool_use",
          "id": "toolu_01",
          "name": "bash",
          "input": { "command": "cat package.json && npm audit --json" }
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "tool_result",
          "tool_use_id": "toolu_01",
          "content": "<2,800 tokens of npm audit output>"
        }
      ]
    }
  ]
}
```



The resent messages from request 1 are not counted again, but the 2,800-token tool result is new content and counts against the budget. Claude spends another 4,000 tokens on thinking and a second tool call (`grep -rn "eval(" src/`). The countdown ends near `remaining` ≈ 88,200.

**Request 3.** Full history resent again with the second tool result (1,200 tokens of grep output) appended. Claude writes a 6,000-token final findings report and stops with `stop_reason: "end_turn"`. `remaining` ≈ 81,000.

Putting the three requests side by side makes the distinction between payload size and budget spend explicit:

| Request   | Request payload (approx. input tokens you sent) | Tokens counted against budget this request                | Budget `remaining` after |
|-----------|-------------------------------------------------|-----------------------------------------------------------|--------------------------|
| 1         | ~20                                             | 5,000 (thinking + `tool_use`)                             | ~95,000                  |
| 2         | ~7,800 (messages from request 1 + tool result)  | 6,800 (2,800 tool result + 4,000 thinking and `tool_use`) | ~88,200                  |
| 3         | ~13,000 (full history + second tool result)     | 7,200 (1,200 tool result + 6,000 `text`)                  | ~81,000                  |
| **Total** | **~20,820 sent across requests**                | **19,000 counted against budget**                         | N/A                      |

Your client sent the original user message three times and the first assistant message twice, but each was counted once. The budget spent 19,000 of 100,000 tokens, even though the cumulative payload your client transmitted was larger and the prompt-cached input on requests 2 and 3 was larger still.

### Carrying a budget across compaction with `remaining`

If your own code compacts or rewrites the message history between requests (for example, by summarizing earlier messages), the server has no memory of how much budget was spent before compaction. Pass `remaining` on the next request so the countdown continues from where you left off rather than resetting to `total`:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
# Tokens spent before compaction, tracked client-side
tokens_spent_so_far = 45000

output_config = {
    "effort": "high",
    "task_budget": {
        "type": "tokens",
        "total": 128000,
        "remaining": 128000 - tokens_spent_so_far,
    },
}
```

In this example, the tokens spent before compaction are the usage of all the messages you have removed from the history so far, measured as in [Measure your current usage](#measure-your-current-usage). Leave out anything still present in the messages you send, including any summary you added, because the server counts those tokens itself. Update this figure only when you replace the history this way; don't decrement it per request. Pass the resulting `remaining` on every request, not only the one that compacts.

For loops that resend the full uncompacted history on every request, omit `remaining` and let the server track the countdown.

## Changing the budget mid-conversation

`task_budget` is a request-level setting. To change the budget partway through a task, for example to extend it when the user broadens the request, set a new `task_budget` in `output_config` on the next request. Keep the caching consequence in mind: the budget value participates in the rendered prompt, so a changed value does not match cache entries created under the old one (see [Feature support](#feature-support) below).

## Task budgets are advisory, not enforced

Task budgets are a **soft hint, not a hard cap**. Claude may occasionally exceed the budget if it is in the middle of an action that would be more disruptive to interrupt than to finish. The enforced limit on total output tokens is still `max_tokens`, which truncates the response with `stop_reason: "max_tokens"` when reached.

For a hard cap on cost or latency, combine task budgets with a reasonable `max_tokens` value:

- Use `task_budget` to give Claude a target to pace against.
- Use `max_tokens` as the absolute ceiling that prevents runaway generation.

Because `task_budget` spans the full agentic loop (potentially many requests) while `max_tokens` caps each individual request, the two values are independent; one is not required to be at or below the other.



**A budget that is too small for the task can cause refusal-like behavior.** When Claude sees a budget that is clearly insufficient for the work being asked (for example, a 20,000-token budget for a multihour agentic coding task), it may decline to attempt the task at all, scope it down aggressively, or stop early with a partial result rather than start work it cannot finish. If you observe unexpected refusals or premature stops after setting a budget, raise the budget before debugging other parameters. Size budgets against your actual task-length distribution rather than a fixed default; see [Choosing a budget](#choosing-a-budget).

## Choosing a budget

The right budget depends on how much work your agentic loop currently does. Rather than guessing, measure your existing token usage first and then tune from there.

### Measure your current usage

Run a representative sample of tasks **without** `task_budget` set and record the total tokens Claude spends per task. For an agentic loop, sum `usage.output_tokens` across every request in the loop, plus the tokens of the tool results you append between requests:

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
        {"role": "user", "content": "Review the codebase and propose a refactor plan."}
    ],
)

# Sum output_tokens (text + thinking + tool calls) across every request in your loop.
print(response.usage.output_tokens)
```

Run this across a representative set of tasks and record the distribution. Start with the p99 of your per-task token spend to understand how providing the model with a task budget might modify the model's behavior, then test up or down as needed.

The minimum accepted `task_budget.total` is **20,000 tokens** on every model that supports task budgets (see [Feature support](#feature-support)). Smaller values return a 400 error.

## Interaction with other parameters

- **`max_tokens`:** Orthogonal to task budgets. `max_tokens` is a hard per-request cap on generated tokens, while `task_budget` is an advisory cap across the full agentic loop (potentially spanning many requests). At `xhigh` or `max` effort, set `max_tokens` to at least 64k to give Claude room to think and act on each request.
- **[Effort](build-with-claude-effort.md):** Effort controls how deeply Claude reasons per step. Task budgets control how much total work Claude does across an agentic loop. The two are complementary: effort tunes depth, task budgets tune breadth.
- **[Adaptive thinking](build-with-claude-thinking.md):** Task budgets include thinking tokens in the count, so adaptive thinking scales down as the budget depletes.
- **[Prompt caching](build-with-claude-prompt-caching.md):** The budget-countdown marker is injected server-side on each request, so it does not match across requests. If your client decrements `task_budget.remaining` on each follow-up request, the changed value invalidates any cache prefix that contains it. To preserve caching, set the budget once on the initial request and let the model self-regulate against the server-side countdown rather than mutating the budget client-side.

## Feature support

| Model             | Support                                     |
|-------------------|---------------------------------------------|
| Claude Fable 5.1  | Beta (set `task-budgets-2026-03-13` header) |
| Claude Mythos 5.1 | Beta (set `task-budgets-2026-03-13` header) |
| Claude Opus 5.5   | Beta (set `task-budgets-2026-03-13` header) |
| Claude Opus 5     | Beta (set `task-budgets-2026-03-13` header) |
| Claude Fable 5    | Beta (set `task-budgets-2026-03-13` header) |
| Claude Mythos 5   | Beta (set `task-budgets-2026-03-13` header) |
| Claude Sonnet 5   | Not supported                               |
| Claude Opus 4.8   | Beta (set `task-budgets-2026-03-13` header) |
| Claude Opus 4.7   | Beta (set `task-budgets-2026-03-13` header) |
| Claude Opus 4.6   | Not supported                               |
| Claude Sonnet 4.6 | Not supported                               |
| Claude Haiku 4.5  | Not supported                               |

Task budgets are not supported on [Claude Code](https://platform.claude.com/docs/01-Getting-Started/overview.md) or Cowork surfaces. Use task budgets directly through the Messages API on a [supported model](#feature-support).

## Next steps



[Effort](build-with-claude-effort.md)

Control how thoroughly Claude reasons about each step of an agentic loop.



[Adaptive thinking](build-with-claude-thinking.md)

Let Claude decide when and how much to use extended thinking.



[Compaction](build-with-claude-compaction.md)

Manage context in long-running conversations with server-side compaction.



[Prompt caching](build-with-claude-prompt-caching.md)

Reduce cost and latency on repeated prompts by caching prompt prefixes.

## Compatibility

Supported models  
- Fable 5 and 5.1
- Mythos 5 and 5.1
- Opus 4.7, 4.8, 5, and 5.5
