---
title: "What's new in Claude Opus 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5/whats-new-opus-5"
category: "20-Models"
fetched_at: "2026-09-18T06:35:53Z"
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fopus-5%2Fwhats-new-opus-5)





SearchCtrlK

Models

[Models overview](/docs/en/models/overview)

[Claude Fable 5.1](/docs/en/models/fable-5-1/overview)

[Claude Opus 5](/docs/en/models/opus-5/overview)

[Overview](/docs/en/models/opus-5/overview)[What's new](/docs/en/models/opus-5/whats-new-opus-5)[Migration guide](/docs/en/models/opus-5/migration-guide)

[Claude Sonnet 5](/docs/en/models/sonnet-5/overview)

[Claude Haiku 4.5](/docs/en/models/haiku-4-5/overview)

Specialized models

Legacy models

Guides

[Choosing a model](/docs/en/about-claude/models/choosing-a-model)[Optimizing for cost and intelligence](/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)[Upgrade between model versions](/docs/en/about-claude/models/migration-guide)

Lifecycle and reference

[Model IDs and versioning](/docs/en/about-claude/models/model-ids-and-versions)[Model deprecations](/docs/en/about-claude/model-deprecations)[Model cards](/docs/en/resources/overview)[Pricing](/docs/en/about-claude/pricing)

[System prompts](/docs/en/release-notes/system-prompts/overview)

[Console](/)

[Models & pricing](/docs/en/models/overview)Claude Opus 5

# What's new in Claude Opus 5

Copy page



Overview of new features and behavior changes in Claude Opus 5.

Copy page



Claude Opus 5 is a step-change improvement over Claude Opus 4.8, with the largest gains in deep reasoning, agentic and long-horizon tasks, and test-time compute scaling. This page summarizes everything new in Claude Opus 5, including mid-conversation tool changes and two breaking changes for code running on Claude Opus 4.8: thinking is on by default, and thinking can be disabled only at effort `high` or below.

## New model

| Model         | API model ID    | Description                                    |
|:--------------|:----------------|:-----------------------------------------------|
| Claude Opus 5 | `claude-opus-5` | For complex agentic coding and enterprise work |

Claude Opus 5 has a [1M token context window](/docs/en/build-with-claude/context-windows) (1M tokens is both the default and the maximum; there is no smaller context variant), 128k max output tokens, and [thinking](/docs/en/build-with-claude/thinking) on by default. [Priority Tier](/docs/en/api/service-tiers#supported-models) is not supported on Claude Opus 5.

For complete pricing and specs, see the [models overview](/docs/en/models/overview).

## New features

### Mid-conversation tool changes (beta)

You can add or remove tools between turns of a conversation while preserving the prompt cache, instead of resending a fixed tool list for the life of a session. Mid-conversation tool changes are in beta: include the `mid-conversation-tool-changes-2026-07-01` beta header in your requests. See [Mid-conversation tool changes](/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes) for usage.

### Default fallbacks mode

The `fallbacks` parameter supports a new `"default"` mode, which applies Anthropic's recommended fallback models by refusal category instead of a model list you maintain yourself. The entire `fallbacks` parameter is in beta. Use the `server-side-fallback-2026-07-01` beta header, which supports both the `"default"` mode and explicit model lists (the earlier `server-side-fallback-2026-06-01` header accepts only explicit lists). See [Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback).

### Lower prompt cache minimum

The minimum cacheable prompt length on Claude Opus 5 is 512 tokens, down from 1,024 tokens on Claude Opus 4.8. Prompts that were too short to cache on Claude Opus 4.8 can now create cache entries with no code changes. See [Prompt caching](/docs/en/build-with-claude/prompt-caching#cache-limitations) for per-model minimums.

### Fast mode

[Fast mode](/docs/en/build-with-claude/fast-mode) (research preview) is available for Claude Opus 5 on the Claude API only; it is not currently available on Amazon Bedrock, Claude Platform on AWS, Google Cloud, or Microsoft Foundry. Fast mode for Claude Opus 5 is priced at \$10 USD per million input tokens and \$50 USD per million output tokens. See [Fast mode](/docs/en/build-with-claude/fast-mode) for access, supported models, and pricing.

## Behavior changes

### Thinking on by default

On Claude Opus 4.8, requests run without thinking unless you set `thinking: {"type": "adaptive"}`. On Claude Opus 5, the same requests run with [adaptive thinking](/docs/en/build-with-claude/thinking) on by default: the model decides when and how much to think on each turn, and the [effort parameter](/docs/en/build-with-claude/effort) is the control for thinking depth. The wire value is unchanged; `thinking: {"type": "adaptive"}` remains valid and equivalent to the default.

This is a breaking change for code that ran without thinking on Claude Opus 4.8. A response can begin with one or more `thinking` blocks before the first `text` block, returned with an empty `thinking` field at the default `display: "omitted"`, so code that reads `content[0].text` or treats the first streamed content block as text must select content blocks by their `type` field instead. Tool-use loops must pass `thinking` blocks back complete and unmodified with their tool results; see [Preserving thinking blocks](/docs/en/build-with-claude/thinking#preserving-thinking-blocks).

Thinking tokens are billed as output tokens and count toward `max_tokens`, a hard limit on total output (thinking plus response text), so revisit `max_tokens` and re-baseline cost for workloads that ran without thinking on Claude Opus 4.8.

The API keeps the option to disable thinking, subject to the [effort restriction](#disabling-thinking-requires-effort-high-or-below) on disabling it.

### Effort matters more

Claude Opus 5 converts additional [effort](/docs/en/build-with-claude/effort) into better results more reliably than any earlier Opus model, so the effort level you choose carries more weight. The full ladder is available: `low`, `medium`, `high`, `xhigh`, and `max`, with `max` as the top tier for the deepest possible reasoning. Start at the default, `high`, and adjust in either direction based on your evals: step down where quality holds to save tokens and latency, or step up for the most demanding work. When running at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act across subagents and tool calls.

This request turns effort all the way up to `max`:

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

with client.messages.stream(
    model="claude-opus-5",
    max_tokens=64000,
    output_config={"effort": "max"},
    messages=[
        {
            "role": "user",
            "content": "Explain why the sum of two even numbers is always even.",
        }
    ],
) as stream:
    response = stream.get_final_message()

print(response)
```

Thinking is [on by default](#thinking-on-by-default) on Claude Opus 5, so no `thinking` field is needed.

### Disabling thinking requires effort `high` or below

On Claude Opus 5, `thinking: {"type": "disabled"}` is accepted only when the effort level is `high` or below. Setting `thinking: {"type": "disabled"}` with effort `xhigh` or `max` returns a 400 error. This rule is enforced on every request to Claude Opus 5 and later models. It is a breaking change from Claude Opus 4.8, where disabling thinking was independent of the effort level. If your Claude Opus 4.8 requests disable thinking at effort `xhigh` or `max`, either keep thinking disabled and set effort to `high` or below, or keep the effort level and remove the `thinking` field.

With thinking disabled, Claude Opus 5 can occasionally write a tool call into its text output instead of emitting a `tool_use` block, or include internal XML tags in its visible response. Where possible, keep thinking enabled and control token cost with lower effort levels; for integrations that must keep thinking disabled, see [Running with thinking disabled](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5#running-with-thinking-disabled) for prompting mitigations.

### Model behavior differences

Beyond these API changes, Claude Opus 5 behaves differently from Claude Opus 4.8 in ways you may notice without changing any code. Default user-facing responses and written deliverables run longer. In agentic sessions, the model narrates its progress to the user more often. In multi-agent frameworks, it delegates to subagents more readily. It also verifies its own work without being told to, so remove verification instructions carried over from earlier models ("include a final verification step," "use a subagent to verify"); they cause over-verification on Claude Opus 5. For prompting patterns that tune each of these behaviors, see [Prompting Claude Opus 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5).

## Capability improvements

Compared with Claude Opus 4.8, Claude Opus 5 is a step-change improvement rather than an incremental one, and it delivers frontier intelligence at half the cost of [Claude Fable 5](/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5). The largest gains are in:

- **Deep reasoning**, sustaining multistep analysis across long problem chains.
- **Agentic coding and long-horizon tasks**, staying on task across extended tool-use loops and completing multi-file features, larger refactors, and end-to-end feature work without leaving stubs or placeholders.
- **Test-time compute scaling**, converting additional effort (up to the `max` level) into better results.
- **Efficiency at lower effort levels**, with `low` and `medium` [effort](/docs/en/build-with-claude/effort) producing strong quality at a fraction of the tokens and latency of higher settings.
- **Code review and bug-finding**, surfacing real bugs at a high rate per pass with few false positives, and staying accurate at lower effort levels.
- **Vision**, understanding charts, documents, and diagrams and replicating UI and frontend visuals, strongest when given tools to iteratively analyze, crop, and verify its work.
- **Long-context work**, with a [1M token context window](/docs/en/build-with-claude/context-windows) as both the default and the maximum, and consistent instruction following, tool calling, and reasoning throughout the window.
- **Office and document tasks**, generating and editing complex multi-sheet spreadsheets with non-trivial formulas, and producing well-structured slide decks.
- **Multi-agent coordination**, running teams of subagents with effective writer-verifier patterns and few cases of agents overwriting each other's work.

For the prompting patterns that get the most out of these capabilities, see [Prompting Claude Opus 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5#capability-improvements).

## Pricing

Claude Opus 5 is priced at \$5 USD per million input tokens and \$25 USD per million output tokens, unchanged from Claude Opus 4.8. Because thinking is on by default and thinking tokens are billed as output tokens, a workload that ran without thinking on Claude Opus 4.8 can produce more output tokens per request at the same per-token rates; see [Cost control](/docs/en/build-with-claude/thinking-steering-and-cost#cost-control).

See [Pricing](/docs/en/about-claude/pricing) for complete pricing, including batch processing, prompt caching, and fast mode rates.

## Availability

Claude Opus 5 is available on:

- **Claude API:** available to all customers, as `claude-opus-5`.
- **AWS:** available through [Claude in Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock), as `anthropic.claude-opus-5`, and through [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws). On Amazon Bedrock, Claude Opus 5 is also reachable through the `InvokeModel` API on `bedrock-runtime`, served by the same infrastructure; the [Claude on Amazon Bedrock (legacy)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy) integration does not include it in its ARN-versioned model ID table.
- **Google Cloud:** available through [Claude on Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai), as `claude-opus-5`.
- **Microsoft Foundry:** available through [Claude in Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry).

Claude Opus 4.8 remains available on all of these platforms.

## Migration guide

To migrate from Claude Opus 4.8, update your model ID:

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
model = "claude-opus-4-8"  # Before
model = "claude-opus-5"  # After
```

Then review the two breaking changes under [Behavior changes](#behavior-changes): thinking is on by default (responses can begin with `thinking` blocks, so select content blocks by `type`), and disabling thinking with effort `xhigh` or `max` returns a 400 error. See the [migration guide](/docs/en/models/opus-5/migration-guide#migrating-from-claude-opus-4-8-to-claude-opus-5) for step-by-step instructions and the full checklist.

## Next steps



[Models overview](/docs/en/models/overview)

Complete specs and pricing for all current Claude models.



[Prompting Claude Opus 5](/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5)

Behavioral differences and prompting patterns specific to Claude Opus 5.



[Effort](/docs/en/build-with-claude/effort)

Control how many tokens Claude uses when responding, from low to max.



[Thinking](/docs/en/build-with-claude/thinking)

How thinking works when it's on by default, and when it can be disabled.



[Task budgets](/docs/en/build-with-claude/task-budgets)

Give Claude an advisory token budget to pace its work against.



[Migration guide](/docs/en/about-claude/models/migration-guide)

Guide for migrating to the latest Claude models from previous Claude versions.



[Fast mode](/docs/en/build-with-claude/fast-mode)

Get higher output tokens per second from Claude Opus models at premium pricing.
