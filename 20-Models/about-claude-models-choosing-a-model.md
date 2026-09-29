---
title: "Choosing the right model - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/about-claude/models/choosing-a-model"
category: "20-Models"
fetched_at: "2026-09-26T06:38:13Z"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fabout-claude%2Fmodels%2Fchoosing-a-model)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

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

[Models & pricing](about-claude-models-overview.md)Guides

# Choosing the right model

Copy page



Choosing a Claude model means balancing capabilities, speed, and cost. This guide covers the questions to ask, two ways to pick a starting model, and how to test the choice.

Copy page



## Establish key criteria

When choosing a Claude model, consider first evaluating these factors:

- **Capabilities:** What specific features or capabilities will you need the model to have to meet your needs?
- **Speed:** How quickly does the model need to respond in your application? Claude Opus 5.5, Claude Opus 5, and Claude Opus 4.8 support [fast mode](../04-API-Reference/Guides/build-with-claude-fast-mode.md) (research preview), which delivers up to 2.5x higher output speed at premium pricing.
- **Cost:** What's your budget for both development and production usage?
- **Effort:** Several Claude models support an [effort parameter](../04-API-Reference/Guides/build-with-claude-effort.md) that trades intelligence for latency and cost within a single model. Tuning effort is often a better lever than switching models. On Claude Fable 5.1 and Claude Opus 5, start with the default (`high`) and adjust up or down based on your evals. On Claude Opus 5.5 the default is `medium`; start there and adjust the same way. On Claude Opus 4.8 and Claude Opus 4.7, the `xhigh` effort level, between `high` and `max`, is the best setting for most coding and agentic use cases.

------------------------------------------------------------------------

## Choose the best model to start with

There are two general approaches you can use to start testing which Claude model best works for your needs.

### Option 1: Start efficiency-first

For many applications, starting with a faster, more cost-effective model like Claude Haiku 4.5 can be the optimal approach:

1.  Begin implementation with Claude Haiku 4.5.
2.  Test your use case thoroughly.
3.  Evaluate if performance meets your requirements.
4.  Upgrade only if necessary for specific capability gaps.

This approach allows for quick iteration, lower development costs, and is often sufficient for many common applications. This approach is best for:

- Initial prototyping and development
- Applications with tight latency requirements
- Cost-sensitive implementations
- High-volume, straightforward tasks

### Option 2: Start capability-first

For complex tasks where intelligence and advanced capabilities are paramount, you may want to start capability-first: implement with the strongest starting point for your task, then optimize to more efficient models down the line:

1.  Implement with Claude Opus 5.5.
2.  [Optimize your prompts](../10-Prompting-Guides/build-with-claude-prompt-engineering-prompting-claude-opus-5-5.md) for this model.
3.  Evaluate if performance meets your requirements.
4.  Consider increasing efficiency by lowering [effort](../04-API-Reference/Guides/build-with-claude-effort.md) or downgrading models over time with greater workflow optimization.
5.  If your evals at `xhigh` or `max` effort still fall short on demanding reasoning or long-horizon agentic work, move to [Claude Fable 5.1](models-fable-5-1-whats-new-fable-5-1.md).

This approach is best for:

- Complex reasoning tasks
- Scientific or mathematical applications
- Tasks requiring nuanced understanding
- Applications where accuracy outweighs cost considerations
- Advanced coding and high-autonomy agentic work

**Claude Opus 5.5** (`claude-opus-5-5`) is built for long-running agentic coding and knowledge work, with [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) always on. If your integration forces tool use (`tool_choice` of type `any` or `tool`), turns thinking off, or uses the `computer_20251124` computer use tool, see [Breaking changes](models-opus-5-5-whats-new-opus-5-5.md#breaking-changes) before switching.

**Claude Fable 5.1** (`claude-fable-5-1`) is Anthropic's most capable model open to all customers. It extends Claude Fable 5 with stronger long-running agentic coding, knowledge work, and research at the same input and output prices, with cache reads at a quarter of the cost. **Claude Mythos 5.1** (`claude-mythos-5-1`) offers the same capabilities to [Project Glasswing](../22-Safety-Policy/glasswing.md) participants only. Both models use always-on [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md). See [What's new in Claude Fable 5.1](models-fable-5-1-whats-new-fable-5-1.md) for details.

For context windows, output limits, and prices, see the [model comparison table](about-claude-models-overview.md#latest-models-comparison).

## Model selection matrix

Most workloads start with Claude Opus 5.5.

| When you need...                                                          | Consider starting with... | Example use cases                                                                                                                 |
|---------------------------------------------------------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| The highest available capability                                          | Claude Fable 5.1          | Agent sessions that run for hours, multistep deep research, analysis carried through to a finished document, spreadsheet, or deck |
| Complex agentic coding and enterprise work                                | Claude Opus 5.5           | Multihour autonomous coding agents, large-scale refactoring, complex systems engineering, vision-heavy workflows, computer use    |
| Speed and capability for everyday coding, agent, and enterprise workloads | Claude Sonnet 5           | Code generation, data analysis, content creation, visual understanding, agentic tool use                                          |
| The lowest latency and price, with extended thinking                      | Claude Haiku 4.5          | Real-time applications, high-volume intelligent processing, cost-sensitive deployments needing strong reasoning, sub-agent tasks  |

------------------------------------------------------------------------

## Decide whether to upgrade or change models

To determine if you need to upgrade or change models, you should:

1.  [Create benchmark tests](../04-API-Reference/Test-Evaluate/test-and-evaluate-develop-tests.md) specific to your use case - having a good evaluation set is the most important step in the process.
2.  Test with your actual prompts and data.
3.  Compare performance across models for:
    - Accuracy of responses
    - Response quality
    - Handling of edge cases
4.  Weigh performance and cost tradeoffs.

## Combine models

Multi-model strategies pair a lower-cost model with a frontier model so that most tokens are billed at the lower rate. The two common patterns are an executor that escalates hard decisions to an advisor, and an orchestrator that delegates bulk work to lower-cost workers. See [Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md) for both strategies, measured examples, and implementation options.

## Next steps



[Model comparison chart](about-claude-models-overview.md)

See detailed specifications and pricing for the latest Claude models

[What's new in Claude Fable 5.1](models-fable-5-1-whats-new-fable-5-1.md)

Built for demanding reasoning and long-horizon agentic work

[What's new in Claude Opus 5.5](models-opus-5-5-whats-new-opus-5-5.md)

The latest Opus model: breaking changes, new features, and behavior differences

[What's new in Claude Sonnet 5](models-sonnet-5-whats-new-sonnet-5.md)

For everyday workloads that balance speed and capability



[Start building](../01-Getting-Started/get-started.md)

Get started with your first API call
