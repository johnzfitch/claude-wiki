---
title: "Migrating to Claude Haiku 4.5 - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/models/haiku-4-5/migration-guide"
category: "20-Models"
fetched_at: "2026-09-26T06:39:44Z"
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


[Console](../04-API-Reference/Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmodels%2Fhaiku-4-5%2Fmigration-guide)





SearchCtrlK

Models

[Models overview](about-claude-models-overview.md)

[Claude Fable 5.1](models-fable-5-1-overview.md)

[Claude Opus 5.5](models-opus-5-5-overview.md)

[Claude Sonnet 5](models-sonnet-5-overview.md)

[Claude Haiku 4.5](models-haiku-4-5-overview.md)

[Overview](models-haiku-4-5-overview.md)[Migration guide](models-haiku-4-5-migration-guide.md)

Specialized models

Legacy models

Guides

[Choosing a model](about-claude-models-choosing-a-model.md)[Optimizing for cost and intelligence](about-claude-models-optimizing-for-cost-and-intelligence.md)[Upgrade between model versions](about-claude-models-migration-guide.md)

Lifecycle and reference

[Model IDs and versioning](about-claude-models-model-ids-and-versions.md)[Model deprecations](about-claude-model-deprecations.md)[Model cards](../04-API-Reference/Other/resources-overview.md)[Pricing](../17-Billing-Plans/about-claude-pricing.md)

[System prompts](release-notes-system-prompts-overview.md)

[Console](../04-API-Reference/Other/usage-limits.md)

[Models & pricing](about-claude-models-overview.md)Claude Haiku 4.5

# Migrating to Claude Haiku 4.5

Copy page



Migrate to Claude Haiku 4.5 from earlier Haiku models: model IDs, breaking changes, and a migration checklist.

Copy page





This guide covers migrating [Messages API](../04-API-Reference/Guides/build-with-claude-working-with-messages.md) code. If you use [Claude Managed Agents](../04-API-Reference/Other/managed-agents-overview.md), no changes beyond updating the model name are required.



**Automate your migration with the Claude API skill.** In Claude Code, run `/claude-api migrate` to invoke the bundled [Claude API skill](../04-API-Reference/Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md#migrating-to-a-newer-claude-model). It works for any current Claude model as the target:

```python
/claude-api migrate this project to claude-haiku-4-5
```



The skill applies the model ID swap and, as needed, breaking parameter changes, prefill replacement, and effort calibration for your target model across your code base, then produces a checklist of items to verify manually. It asks you to confirm the migration scope (entire working directory, a subdirectory, or a specific file list) before editing any files. The skill also detects Amazon Bedrock and Claude Platform on AWS clients and adjusts model ID formats and feature changes for those platforms.

Claude Haiku 4.5 is the fastest and most intelligent Haiku model with near-frontier performance, delivering premium model quality for interactive applications and high-volume processing.

For a complete overview of capabilities, see the [models overview](about-claude-models-overview.md).



For Claude Haiku 4.5 pricing, see [Claude pricing](../17-Billing-Plans/about-claude-pricing.md).



For significant performance improvements on coding and reasoning tasks, consider enabling extended thinking with `thinking: {type: "enabled", budget_tokens: N}`.



Extended thinking impacts [prompt caching](../04-API-Reference/Guides/build-with-claude-prompt-caching.md#caching-with-thinking-blocks) efficiency.

Extended thinking is deprecated in Claude 4.6 models and removed in Claude Opus 4.7. If using newer models, use [adaptive thinking](../04-API-Reference/Guides/build-with-claude-thinking.md) instead.

## Migrating to Claude Haiku 4.5 from Claude Haiku 3.5 and earlier Haiku models

**Update your model name:**

```python
# From Haiku 3.5
model = "claude-3-5-haiku-20241022"  # Before
model = "claude-haiku-4-5-20251001"  # After
```



**Review new rate limits:** Haiku 4.5 has separate rate limits from Haiku 3.5. See [Rate limits](../04-API-Reference/Endpoints/rate-limits.md) documentation for details.

**Explore new capabilities:** See the [models overview](about-claude-models-overview.md) for details on context awareness, increased output capacity (64k tokens), higher intelligence, and improved speed.

### Breaking changes

These breaking changes apply when migrating from Claude 3.x Haiku models.

1.  **Update sampling parameters**

    

    This is a breaking change when migrating from Claude 3.x models.

    Use only `temperature` OR `top_p`, not both. Setting both returns a 400 error on Claude Haiku 4.5.

2.  **Update tool versions**

    

    This is a breaking change when migrating from Claude 3.x models.

    Update to the latest tool versions (`text_editor_20250728`, `code_execution_20250825`). Remove any code using the `undo_edit` command.

3.  **Handle the `refusal` stop reason**

    Update your application to [handle `refusal` stop reasons](../04-API-Reference/Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md).

4.  **Update your prompts for behavioral changes**

    Claude 4 models have a more concise, direct communication style. Review [prompting best practices](../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md) for optimization guidance.

### Haiku 4.5 migration checklist

- Update model ID to `claude-haiku-4-5-20251001`
- **BREAKING:** Update tool versions to latest (`text_editor_20250728`, `code_execution_20250825`); legacy versions are not supported
- **BREAKING:** Remove any code using the `undo_edit` command (if applicable)
- **BREAKING:** Update sampling parameters to use only `temperature` OR `top_p`, not both (setting both returns a 400 error)
- Handle new `refusal` stop reason in your application
- Review and adjust for new rate limits (separate from Haiku 3.5)
- Review and update prompts following [prompting best practices](../10-Prompting-Guides/build-with-claude-prompt-engineering-claude-prompting-best-practices.md)
- Consider enabling extended thinking for complex reasoning tasks
- Test in development environment before production deployment
