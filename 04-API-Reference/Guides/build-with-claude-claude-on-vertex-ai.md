---
title: "Claude on Google Cloud - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:19Z"
tags: ["agents", "api", "sdk"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fclaude-on-vertex-ai)

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

[Messages](../../01-Getting-Started/intro.md)Claude on cloud platforms

# Claude on Google Cloud

Copy page



Anthropic's Claude models are available through [Google Cloud's Agent Platform](https://cloud.google.com/vertex-ai).

Copy page



The API for accessing Claude on Google Cloud's Agent Platform is nearly identical to the [Messages API](../Endpoints/messages-create.md), with two key differences in request format:

- On Agent Platform, `model` is not passed in the request body. Instead, it is specified in the Google Cloud endpoint URL.
- On Agent Platform, `anthropic_version` is passed in the request body (rather than as a header), and must be set to the value `vertex-2023-10-16`.

Agent Platform is also supported by Anthropic's official [client SDKs](../Other/cli-sdks-libraries-overview.md). This guide walks you through making a request to Claude on Agent Platform using one of Anthropic's client SDKs.

Note that this guide assumes you already have a Google Cloud project that is able to use Agent Platform. See [Anthropic Claude models on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude) for more information on the setup required and a full walkthrough.

## Install an SDK for accessing Agent Platform

First, install Anthropic's [client SDK](../Other/cli-sdks-libraries-overview.md) for your language of choice.

Python

TypeScript

C#

Go

Java

PHP

Ruby

```python
pip install -U "anthropic[vertex]"
```



## Accessing Agent Platform

### Model availability

Note that Anthropic model availability varies by region. Search for "Claude" in the [Model Garden](https://cloud.google.com/model-garden) or go to [Anthropic Claude models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude) for the latest information.

#### API model IDs

Lifecycle terms (Deprecated, Retired) are defined in [Model deprecations](../../20-Models/about-claude-model-deprecations.md). Lifecycle dates on partner-operated platforms are set by the partner and can differ from the Claude API schedule. For the current retirement date of any model on Agent Platform, see [Google Cloud's documentation for Claude models on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude).

| Model                                                                                         | Agent Platform API model ID |
|-----------------------------------------------------------------------------------------------|-----------------------------|
| Claude Fable 5.1                                                                              | claude-fable-5-1            |
| Claude Mythos 5.1 ([limited availability(opens in new tab)](../../22-Safety-Policy/glasswing.md)) | claude-mythos-5-1           |
| Claude Fable 5                                                                                | claude-fable-5              |
| Claude Mythos 5 ([limited availability(opens in new tab)](../../22-Safety-Policy/glasswing.md))   | claude-mythos-5             |
| Claude Opus 5.5                                                                               | claude-opus-5-5             |
| Claude Opus 5                                                                                 | claude-opus-5               |
| Claude Opus 4.8                                                                               | claude-opus-4-8             |
| Claude Opus 4.7                                                                               | claude-opus-4-7             |
| Claude Opus 4.6                                                                               | claude-opus-4-6             |
| Claude Opus 4.5                                                                               | claude-opus-4-5@20251101    |
| Claude Opus 4.1 ([deprecated](../../20-Models/about-claude-model-deprecations.md))                      | claude-opus-4-1@20250805    |
| Claude Opus 4 ([deprecated](../../20-Models/about-claude-model-deprecations.md))                        | claude-opus-4@20250514      |
| Claude Sonnet 5                                                                               | claude-sonnet-5             |
| Claude Sonnet 4.6                                                                             | claude-sonnet-4-6           |
| Claude Sonnet 4.5                                                                             | claude-sonnet-4-5@20250929  |
| Claude Sonnet 4 ([deprecated](../../20-Models/about-claude-model-deprecations.md))                      | claude-sonnet-4@20250514    |
| Claude Haiku 4.5                                                                              | claude-haiku-4-5@20251001   |
| Claude Haiku 3.5 ([deprecated](../../20-Models/about-claude-model-deprecations.md))                     | claude-3-5-haiku@20241022   |



Upgrading to a newer Claude model? In Claude Code, run `/claude-api migrate` to apply model ID swaps and breaking parameter changes across your codebase. The skill detects which cloud platform your code targets and adjusts model ID formats and feature changes for that platform. See [Migrating to a newer Claude model](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md#migrating-to-a-newer-claude-model).

### Making requests

Before running requests you might need to run `gcloud auth application-default login` to authenticate with Google Cloud.

The following examples show how to generate text from Claude on Agent Platform:

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
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "global"

client = AnthropicVertex(project_id=project_id, region=region)

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
print(message)
```

See the [client SDKs](../Other/cli-sdks-libraries-overview.md) and the official [Agent Platform docs](https://cloud.google.com/vertex-ai/docs) for more details.

Claude is also available through [Amazon Bedrock](build-with-claude-claude-in-amazon-bedrock.md), [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md), and [Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md).

## Data retention

Data handling for this offering is governed by Google Cloud. For details, see [Agent Platform and zero data retention](https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance).

## Activity logging

Agent Platform provides a [request-response logging service](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/request-response-logging) that allows you to log the prompts and completions associated with your usage.

Anthropic recommends that you log your activity on at least a 30-day rolling basis to understand your activity and investigate any potential misuse.



Turning on this service does not give Google or Anthropic any access to your content.

## Feature support

For the full feature list with Google Cloud availability, see [Features overview](build-with-claude-overview.md).

### Supported feature highlights

- [Messages API](../Endpoints/messages-create.md)
- [Prompt caching](build-with-claude-prompt-caching.md)
- [Thinking](build-with-claude-thinking.md)
- [Tool use](../Agents-Tools/agents-and-tools-tool-use-overview.md), including the [Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md), [Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md), [Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md), [Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md), and [Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)
- [Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)
- [Citations](build-with-claude-citations.md)
- [Structured outputs](build-with-claude-structured-outputs.md)

### Features not supported

- Input sources (URL sources for images and documents, Files API)
- Server-side tools (code execution, web fetch, advisor)
- Agent infrastructure (Agent Skills, MCP connector, programmatic tool calling)
- API endpoints (Message Batches, Models, Admin, Compliance, Usage and Cost)
- Claude Managed Agents
- Server-side fallback (the [`fallbacks` parameter](build-with-claude-refusals-and-fallback.md#server-side-fallback); use the [client-side fallback pattern](build-with-claude-refusals-and-fallback.md#client-side-fallback) instead)

### Context window

Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5, and Claude Sonnet 4.6 have a [1M-token context window](build-with-claude-context-windows.md) on Agent Platform. Other Claude models, including Sonnet 4.5 and Sonnet 4 (deprecated), have a 200k-token context window.

Agent Platform limits request payloads to 30 MB. When sending large documents or many images, you might reach this limit before the token limit.

## Global, multi-region, and regional endpoints

Agent Platform offers three endpoint types:

- **Global endpoints:** Dynamic routing for maximum availability
- **Multi-region endpoints:** Dynamic routing within a geographic area (for example, the United States or the European Union) for data residency with high availability
- **Regional endpoints:** Guaranteed data routing through specific geographic regions

Regional and multi-region endpoints include a 10% pricing premium over global endpoints.



This applies to Claude Sonnet 4.5 and future models only. Older models (Claude Sonnet 4 (deprecated), Opus 4 (deprecated), and earlier) maintain their existing pricing structures.

### When to use each option

**Global endpoints (recommended):**

- Provide maximum availability and uptime
- Dynamically route requests to regions with available capacity
- No pricing premium
- Best for applications where data residency is flexible
- Only supports pay-as-you-go traffic (provisioned throughput requires regional endpoints)

**Multi-region endpoints:**

- Dynamically route requests across regions within a geographic area (currently `us` and `eu`)
- Useful when you need data residency within a broad geography but want higher availability than a single region
- 10% pricing premium over global endpoints
- Only supports pay-as-you-go traffic (provisioned throughput requires regional endpoints)

**Regional endpoints:**

- Route traffic through specific geographic regions
- Required for single-region data residency, strict compliance mandates, or provisioned throughput
- Support both pay-as-you-go and provisioned throughput
- 10% pricing premium reflects infrastructure costs for dedicated regional capacity

### Implementation

**Using global endpoints (recommended):**

Set the `region` parameter to `"global"` when initializing the client:

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
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "global"

client = AnthropicVertex(project_id=project_id, region=region)

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
print(message)
```

**Using multi-region endpoints:**

Set the `region` parameter to a multi-region identifier: `"us"` for the United States or `"eu"` for the European Union. The SDK routes requests to the corresponding multi-region endpoint (`https://aiplatform.us.rep.googleapis.com` or `https://aiplatform.eu.rep.googleapis.com`), which dynamically balances traffic across regions within that geography.

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
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "us"  # Multi-region identifier: "us" or "eu"

client = AnthropicVertex(project_id=project_id, region=region)

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
print(message)
```

**Using regional endpoints:**

Specify a specific region such as `"us-east5"` or `"europe-west1"`:

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
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "us-east5"  # Specify a specific region

client = AnthropicVertex(project_id=project_id, region=region)

message = client.messages.create(
    # Specific regional endpoints support Claude Sonnet 4.6 and earlier; newer models use the global or multi-region endpoints
    model="claude-sonnet-4-6",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hey Claude!",
        }
    ],
)
print(message)
```



Claude Mythos Preview is a research preview available to invited customers on Agent Platform. For more information, see [Project Glasswing](../../22-Safety-Policy/glasswing.md).

## Additional resources

- **Agent Platform pricing:** [Generative AI pricing on cloud.google.com](https://cloud.google.com/vertex-ai/generative-ai/pricing)
- **Claude models documentation:** [Claude on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude)
- **Google blog post:** [Global endpoint for Claude models](https://cloud.google.com/blog/products/ai-machine-learning/global-endpoint-for-claude-models-generally-available-on-vertex-ai)
- **Anthropic pricing details:** [Cloud platform pricing](../../17-Billing-Plans/about-claude-pricing.md#cloud-platform-pricing)
