---
title: "Features overview - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/overview"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:23Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Foverview)

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

[Messages](../../01-Getting-Started/intro.md)Building with Claude

# Features overview

Copy page



Explore Claude's advanced features and capabilities.

Copy page



Claude's API surface is organized into five areas:

- **Model capabilities:** Control how Claude reasons and formats responses.
- **Tools:** Let Claude take actions on the web or in your environment.
- **Tool infrastructure:** Handles discovery and orchestration at scale.
- **Context management:** Keeps long-running sessions efficient.
- **Files and assets:** Manage the documents and data you provide to Claude.

If you're new, start with [model capabilities](#model-capabilities) and [tools](#tools). Return to the other sections when you're ready to optimize cost, latency, or scale.

For administration and governance, see the [Admin API](../Other/manage-claude-admin-api.md), the [Usage and Cost API](../Other/manage-claude-usage-cost-api.md), and the [Compliance API](../Other/manage-claude-compliance-api.md).

## Feature availability

The Availability column in each of the following tables lists the platforms that offer a feature. A platform listed without a label offers the feature as stable, fully supported, and recommended for production use, with no beta header and with standard API [versioning](../Endpoints/versioning.md) guarantees. A label after a platform name marks one of the following classifications on that platform. Not all features pass through every stage, and a feature may enter at any stage or skip stages.

[TABLE]

**Platform labels:** Claude API (Anthropic first-party) · [Bedrock](build-with-claude-claude-in-amazon-bedrock.md) (AWS-operated) · [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md) (Anthropic-operated on AWS) · [Google Cloud](build-with-claude-claude-on-vertex-ai.md) (Google-operated) · [Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md) (Anthropic-operated on Azure)

## Model capabilities

Ways to steer Claude and Claude's direct outputs, including response format, reasoning depth, and input modalities.



You can discover which capabilities a model supports programmatically. The [Models API](../Endpoints/models-list.md) returns `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.

The ZDR column indicates whether a feature is available under a Zero Data Retention arrangement. For most features this depends only on what the feature mechanism retains; for features tied to specific models, model-level ZDR availability also applies. See [Model-specific data retention requirements](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements).

[TABLE]

## Tools

Built-in tools that Claude invokes through `tool_use`. Server-side tools are run by the platform; client-side tools are implemented and executed by you.

### Server-side tools

[TABLE]

### Client-side tools

[TABLE]

## Tool infrastructure

Infrastructure that supports discovering, orchestrating, and scaling tool use.

[TABLE]

## Context management

Infrastructure for controlling and optimizing Claude's context window.

[TABLE]

## Files and assets

Manage files and assets for use with Claude.

[TABLE]

\* **Structured outputs:** Your prompts and Claude's outputs are not stored. Only JSON schemas are cached, for up to 24 hours since last use. **Web search and web fetch:** ZDR-eligible except when [dynamic filtering](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md#dynamic-filtering) is enabled. **Fallback credit and server-side fallback:** The features retain no message content, but they handle refusals from the Claude Fable models, which [are not available under ZDR](../Other/manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements). See [ZDR details](../Other/manage-claude-api-and-data-retention.md#feature-eligibility).

† On Microsoft Foundry, feature availability differs by [hosting option](build-with-claude-claude-in-microsoft-foundry.md#hosting-options). These features are available on Hosted on Anthropic deployments, and not on Hosted on Azure deployments.

‡ On Microsoft Foundry, the [Skill version download endpoint](../Endpoints/beta-skills-versions-download.md) (`GET /v1/skills/{skill_id}/versions/{version}/content`) is not supported.
