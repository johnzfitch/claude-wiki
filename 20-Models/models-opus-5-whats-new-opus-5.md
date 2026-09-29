---
title: "What's new in Claude Opus 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/opus-5/whats-new-opus-5"
category: "20-Models"
fetched_at: "2026-09-18T06:35:53Z"
tags: ["models"]
---

- [Managed Agents](../04-API-Reference/Other/managed-agents-overview.md)

- [Admin](../04-API-Reference/Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../04-API-Reference/About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../04-API-Reference/Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](release-notes-overview.md)

[API reference](../04-API-Reference/Endpoints/overview.md)




[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fopus-5%2Fwhats-new-opus-5)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5](models-opus-5-overview.md)

[Overview](models-opus-5-overview.md)[What's new](models-opus-5-whats-new-opus-5.md)[Migration guide](models-opus-5-migration-guide.md)

[Claude Sonnet 5](models-sonnet-5-overview.md)

[Claude Haiku 4.5](models-haiku-4-5-overview.md)

Specialized models

Legacy models

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)

[Models & pricing](about-claude-models-overview.md)Claude Opus 5

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

Claude Opus 5 has a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) (1M tokens is both the default and the maximum; there is no smaller context variant), 128k max output tokens, and [thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) on by default. [Priority Tier](../04-API-Reference/Endpoints/service-tiers.md#supported-models) is not supported on Claude Opus 5.

For complete pricing and specs, see the [models overview](about-claude-models-overview.md).

## New features

### Mid-conversation tool changes (beta)

You can add or remove tools between turns of a conversation while preserving the prompt cache, instead of resending a fixed tool list for the life of a session. Mid-conversation tool changes are in beta: include the `mid-conversation-tool-changes-2026-07-01` beta header in your requests. See [Mid-conversation tool changes](../04-API-Reference/Guides/build-with-claude-mid-conversation-system-messages.md#mid-conversation-tool-changes) for usage.

### Default fallbacks mode

The `fallbacks` parameter supports a new `"default"` mode, which applies Anthropic's recommended fallback models by refusal category instead of a model list you maintain yourself. The entire `fallbacks` parameter is in beta. Use the `server-side-fallback-2026-07-01` beta header, which supports both the `"default"` mode and explicit model lists (the earlier `server-side-fallback-2026-06-01` header accepts only explicit lists). See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md).

### Lower prompt cache minimum

The minimum cacheable prompt length on Claude Opus 5 is 512 tokens, down from 1,024 tokens on Claude Opus 4.8. Prompts that were too short to cache on Claude Opus 4.8 can now create cache entries with no code changes. See [Prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#cache-limitations) for per-model minimums.

### Fast mode

[Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) (research preview) is available for Claude Opus 5 on the Claude API only; it is not currently available on Amazon Bedrock, Claude Platform on AWS, Google Cloud, or Microsoft Foundry. Fast mode for Claude Opus 5 is priced at \$10 USD per million input tokens and \$50 USD per million output tokens. See [Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) for access, supported models, and pricing.

## Behavior changes

### Thinking on by default

On Claude Opus 4.8, requests run without thinking unless you set `thinking: {"type": "adaptive"}`. On Claude Opus 5, the same requests run with [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) on by default: the model decides when and how much to think on each turn, and the [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) is the control for thinking depth. The wire value is unchanged; `thinking: {"type": "adaptive"}` remains valid and equivalent to the default.

This is a breaking change for code that ran without thinking on Claude Opus 4.8. A response can begin with one or more `thinking` blocks before the first `text` block, returned with an empty `thinking` field at the default `display: "omitted"`, so code that reads `content[0].text` or treats the first streamed content block as text must select content blocks by their `type` field instead. Tool-use loops must pass `thinking` blocks back complete and unmodified with their tool results; see [Preserving thinking blocks](../04-API-Reference/Guides/build-with-claude-thinking.md#preserving-thinking-blocks).

Thinking tokens are billed as output tokens and count toward `max_tokens`, a hard limit on total output (thinking plus response text), so revisit `max_tokens` and re-baseline cost for workloads that ran without thinking on Claude Opus 4.8.

The API keeps the option to disable thinking, subject to the [effort restriction](#disabling-thinking-requires-effort-high-or-below) on disabling it.

### Effort matters more

Claude Opus 5 converts additional [effort](../04-API-Reference/Guides/build-with-claude-effort.md) into better results more reliably than any earlier Opus model, so the effort level you choose carries more weight. The full ladder is available: `low`, `medium`, `high`, `xhigh`, and `max`, with `max` as the top tier for the deepest possible reasoning. Start at the default, `high`, and adjust in either direction based on your evals: step down where quality holds to save tokens and latency, or step up for the most demanding work. When running at `xhigh` or `max` effort, set a large `max_tokens` so the model has room to think and act across subagents and tool calls.

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

With thinking disabled, Claude Opus 5 can occasionally write a tool call into its text output instead of emitting a `tool_use` block, or include internal XML tags in its visible response. Where possible, keep thinking enabled and control token cost with lower effort levels; for integrations that must keep thinking disabled, see [Running with thinking disabled](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#running-with-thinking-disabled) for prompting mitigations.

### Model behavior differences

Beyond these API changes, Claude Opus 5 behaves differently from Claude Opus 4.8 in ways you may notice without changing any code. Default user-facing responses and written deliverables run longer. In agentic sessions, the model narrates its progress to the user more often. In multi-agent frameworks, it delegates to subagents more readily. It also verifies its own work without being told to, so remove verification instructions carried over from earlier models ("include a final verification step," "use a subagent to verify"); they cause over-verification on Claude Opus 5. For prompting patterns that tune each of these behaviors, see [Prompting Claude Opus 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md).

## Capability improvements

Compared with Claude Opus 4.8, Claude Opus 5 is a step-change improvement rather than an incremental one, and it delivers frontier intelligence at half the cost of [Claude Fable 5](models-fable-5-introducing-claude-fable-5-and-claude-mythos-5.md). The largest gains are in:

- **Deep reasoning**, sustaining multistep analysis across long problem chains.
- **Agentic coding and long-horizon tasks**, staying on task across extended tool-use loops and completing multi-file features, larger refactors, and end-to-end feature work without leaving stubs or placeholders.
- **Test-time compute scaling**, converting additional effort (up to the `max` level) into better results.
- **Efficiency at lower effort levels**, with `low` and `medium` [effort](../04-API-Reference/Guides/build-with-claude-effort.md) producing strong quality at a fraction of the tokens and latency of higher settings.
- **Code review and bug-finding**, surfacing real bugs at a high rate per pass with few false positives, and staying accurate at lower effort levels.
- **Vision**, understanding charts, documents, and diagrams and replicating UI and frontend visuals, strongest when given tools to iteratively analyze, crop, and verify its work.
- **Long-context work**, with a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) as both the default and the maximum, and consistent instruction following, tool calling, and reasoning throughout the window.
- **Office and document tasks**, generating and editing complex multi-sheet spreadsheets with non-trivial formulas, and producing well-structured slide decks.
- **Multi-agent coordination**, running teams of subagents with effective writer-verifier patterns and few cases of agents overwriting each other's work.

For the prompting patterns that get the most out of these capabilities, see [Prompting Claude Opus 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md#capability-improvements).

## Pricing

Claude Opus 5 is priced at \$5 USD per million input tokens and \$25 USD per million output tokens, unchanged from Claude Opus 4.8. Because thinking is on by default and thinking tokens are billed as output tokens, a workload that ran without thinking on Claude Opus 4.8 can produce more output tokens per request at the same per-token rates; see [Cost control](../04-API-Reference/Guides/build-with-claude-thinking-steering-and-cost.md#cost-control).

See [Pricing](../17-Billing-Plans/about-claude-pricing.md) for complete pricing, including batch processing, prompt caching, and fast mode rates.

## Availability

Claude Opus 5 is available on:

- **Claude API:** available to all customers, as `claude-opus-5`.
- **AWS:** available through [Claude in Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), as `anthropic.claude-opus-5`, and through [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md). On Amazon Bedrock, Claude Opus 5 is also reachable through the `InvokeModel` API on `bedrock-runtime`, served by the same infrastructure; the [Claude on Amazon Bedrock (legacy)](../04-API-Reference/Guides/build-with-claude-claude-on-amazon-bedrock-legacy.md) integration does not include it in its ARN-versioned model ID table.
- **Google Cloud:** available through [Claude on Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md), as `claude-opus-5`.
- **Microsoft Foundry:** available through [Claude in Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md).

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

Then review the two breaking changes under [Behavior changes](#behavior-changes): thinking is on by default (responses can begin with `thinking` blocks, so select content blocks by `type`), and disabling thinking with effort `xhigh` or `max` returns a 400 error. See the [migration guide](models-opus-5-migration-guide.md#migrating-from-claude-opus-4-8-to-claude-opus-5) for step-by-step instructions and the full checklist.

## Next steps



[Models overview](about-claude-models-overview.md)

Complete specs and pricing for all current Claude models.



[Prompting Claude Opus 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5.md)

Behavioral differences and prompting patterns specific to Claude Opus 5.



[Effort](../04-API-Reference/Guides/build-with-claude-effort.md)

Control how many tokens Claude uses when responding, from low to max.



[Thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)

How thinking works when it's on by default, and when it can be disabled.



[Task budgets](../04-API-Reference/Guides/build-with-claude-task-budgets.md)

Give Claude an advisory token budget to pace its work against.



[Migration guide](about-claude-models-migration-guide.md)

Guide for migrating to the latest Claude models from previous Claude versions.



[Fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md)

Get higher output tokens per second from Claude Opus models at premium pricing.
