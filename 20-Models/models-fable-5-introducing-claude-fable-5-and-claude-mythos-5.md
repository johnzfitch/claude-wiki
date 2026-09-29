---
title: "Introducing Claude Fable 5 and Claude Mythos 5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/fable-5/introducing-claude-fable-5-and-claude-mythos-5"
category: "20-Models"
fetched_at: "2026-09-26T06:39:52Z"
tags: ["api", "billing", "models", "prompting"]
---

- [Managed Agents](../04-API-Reference/Other/managed-agents-overview.md)

- [Admin](../04-API-Reference/Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../04-API-Reference/About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../04-API-Reference/Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](release-notes-overview.md)

[API reference](../04-API-Reference/Endpoints/overview.md)




[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Ffable-5%2Fintroducing-claude-fable-5-and-claude-mythos-5)





SearchCtrlK

[Console](../04-API-Reference/Other/usage-limits.md)

Documentation

# Introducing Claude Fable 5 and Claude Mythos 5

Copy page



Claude Fable 5 and Claude Mythos 5 capabilities, API changes, and availability.

Copy page





Claude Fable 5.1 and Claude Mythos 5.1 build on these models. See [What's new in Claude Fable 5.1](models-fable-5-1-whats-new-fable-5-1.md).



Access to Claude Fable 5 and Claude Mythos 5 has been restored. See [our statement](../19-Reference/redeploying-fable-5.md) for more information.

Claude Fable 5 is built for demanding reasoning and long-horizon agentic work. Claude Mythos 5 shares the same capabilities and is available only in limited release through [Project Glasswing](../22-Safety-Policy/glasswing.md).

The headline change for integrations: Claude Fable 5 includes safety classifiers that can decline requests. Claude Mythos 5 does not include these classifiers. If your integration calls Claude Fable 5, plan for three changes: new response handling for refusals, fallback options for retrying on another Claude model, and new billing rules. [Refusals, fallback, and billing on Claude Fable 5](#refusals-fallback-and-billing-on-claude-fable-5) summarizes all three.

## Models

| Model           | API model ID      | Description                                                                                                                                   |
|:----------------|:------------------|:----------------------------------------------------------------------------------------------------------------------------------------------|
| Claude Fable 5  | `claude-fable-5`  | Built for demanding reasoning and long-horizon agentic work                                                                                   |
| Claude Mythos 5 | `claude-mythos-5` | Shares Claude Fable 5's capabilities without the safety classifiers. Available through Project Glasswing. Successor to Claude Mythos Preview. |

Claude Fable 5 and Claude Mythos 5 share the same specs and pricing:

- **Context window and output:** a [1M token context window](../04-API-Reference/Guides/build-with-claude-context-windows.md) by default, and up to 128k output tokens per request.
- **Pricing:** \$10 USD per million input tokens and \$50 USD per million output tokens.

For specs across all current models, see the [models overview](about-claude-models-overview.md).

## Refusals, fallback, and billing on Claude Fable 5

Claude Fable 5 includes safety classifiers that can decline certain requests. Claude Mythos 5 does not include these classifiers, so this section applies to Claude Fable 5 only. The following sections summarize what refusals mean for your integration. Each links to the full guide.

### Refusals

When Claude Fable 5 declines a request, the Messages API returns `stop_reason: "refusal"` as a successful HTTP 200 response, not an error. The response also reports which classifier declined the request. See [Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md) for response shapes and handling guidance.

### Fallback

A request that Claude Fable 5 refuses can usually be served by another Claude model. There are three ways to retry:

- **Server-side:** Pass the `fallbacks` parameter to have the API retry for you, using its `"default"` mode for Anthropic's recommended models or naming your own (in beta on the Claude API). See [Server-side fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#server-side-fallback).
- **Client-side:** Use the [SDK middleware](../04-API-Reference/Other/cli-sdks-libraries-middleware.md) to retry from the client on any platform. See [Client-side fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#client-side-fallback).
- **Manual:** Build the retry yourself, on any platform and in any language. See [Fallback credit](../04-API-Reference/Guides/build-with-claude-fallback-credit.md).

### Billing

A refusal that arrives before any output is billed when it is in a category with low volumes of false positives, to disrupt attempts to circumvent Anthropic's safeguards at scale. Before September 24, 2026, these refusals were not billed. A mid-stream refusal bills the input tokens and the output already streamed at normal rates. For the billed categories, see [How refusals are billed](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md#how-refusals-are-billed). When you retry on another model, [fallback credit](../04-API-Reference/Guides/build-with-claude-fallback-credit.md) refunds the prompt-cache cost of switching, so you avoid paying that cost twice.

## Availability

- **Claude Fable 5** is available on the Claude API, [Amazon Bedrock](../04-API-Reference/Guides/build-with-claude-claude-in-amazon-bedrock.md), [Claude Platform on AWS](../04-API-Reference/Guides/build-with-claude-claude-platform-on-aws.md), [Google Cloud](../04-API-Reference/Guides/build-with-claude-claude-on-vertex-ai.md), and [Microsoft Foundry](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md).
- **Claude Mythos 5** is offered only to approved customers in [Project Glasswing](../22-Safety-Policy/glasswing.md). For access, contact your Anthropic, AWS, or Google Cloud account team. Customers without access to Claude Mythos 5 can use Claude Fable 5, which does not require access approval and offers the same capabilities.

Claude Fable 5 and Claude Mythos 5 carry 30-day data retention and are not available under zero data retention unless expressly authorized by Anthropic. Both are designated [Covered Models](covered-models.md). See [Model-specific data retention requirements](../04-API-Reference/Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements).

## Prompting

Claude Fable 5 responds to the same prompting techniques as other Claude models, with a few differences in how to structure long-context prompts and reasoning instructions. See [Prompting Claude Fable 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5.md).

## Messages API on Claude Fable 5 and Claude Mythos 5

### Adaptive thinking is always on

Claude Fable 5 and Claude Mythos 5 always have thinking enabled. Passing `thinking: {"type": "disabled"}` is not supported. To reduce or otherwise control thinking depth, use the [effort](../04-API-Reference/Guides/build-with-claude-effort.md) parameter.

### Raw thinking content is never returned

The raw chain of thought is never returned on Claude Fable 5 and Claude Mythos 5. The `thinking.display` setting controls what thinking blocks contain instead:

- `"summarized"` returns thinking blocks with a readable summary of the reasoning.
- `"omitted"` (the default) returns thinking blocks with an empty `thinking` field.

Pass thinking blocks back unchanged in multi-turn conversations on the same model. See [thinking output on Claude Fable 5 and Claude Mythos 5](../04-API-Reference/Guides/build-with-claude-thinking.md#thinking-output-on-claude-fable-5-and-claude-mythos-5) for cross-model handling.

## Supported features

Claude Fable 5 and Claude Mythos 5 support:

- [Effort](../04-API-Reference/Guides/build-with-claude-effort.md)
- [Task budgets](../04-API-Reference/Guides/build-with-claude-task-budgets.md) (beta: set the `task-budgets-2026-03-13` header)
- The [memory tool](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-memory-tool.md)
- [Code execution](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)
- [Programmatic tool calling](../04-API-Reference/Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)
- Tool result clearing through [context editing](../04-API-Reference/Guides/build-with-claude-context-editing.md) (beta: set the `context-management-2025-06-27` header)
- [Compaction](../04-API-Reference/Guides/build-with-claude-compaction.md)
- [Vision](../04-API-Reference/Guides/build-with-claude-vision.md)

## Migrating from earlier models

Step-by-step instructions live in the migration guide:

- From Claude Mythos Preview: see [Migrating from Claude Mythos Preview to Claude Mythos 5](models-fable-5-migration-guide.md#migrating-from-claude-mythos-preview).
- From Claude Opus 4.8: see [Migrating from Claude Opus 4.8 to Claude Fable 5](models-fable-5-migration-guide.md#migrating-from-claude-opus-48).

## Next steps



[Models overview](about-claude-models-overview.md)

Specs and comparison for all current Claude models.



[Adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md)

The only thinking mode on Claude Fable 5 and Claude Mythos 5.



[Refusals and fallback](../04-API-Reference/Guides/build-with-claude-refusals-and-fallback.md)

How Claude Fable 5 declines requests, and how to retry on another model.

[Fallback credit](../04-API-Reference/Guides/build-with-claude-fallback-credit.md)

Avoid paying the prompt-cache cost twice on a retry.



[Fallback and billing cookbook](https://platform.claude.com/cookbook/fable-5-fallback-billing-guide)

A worked end-to-end example of refusal handling, fallback, and billing.



[Effort](../04-API-Reference/Guides/build-with-claude-effort.md)

Control thinking depth and cost on Claude Fable 5 and Claude Mythos 5.



[Prompting Claude Fable 5](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-fable-5.md)

Fable-specific prompting techniques.
