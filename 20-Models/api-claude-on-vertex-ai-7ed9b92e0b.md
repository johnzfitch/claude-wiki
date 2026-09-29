---
title: "Claude on Google Cloud - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/api/claude-on-vertex-ai"
category: "20-Models"
fetched_at: "2026-09-26T06:38:59Z"
tags: ["agents", "sdk"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fclaude-on-vertex-ai)





SearchCtrlK

First steps

[Intro to Claude](/docs/en/intro)[Get your API key](/docs/en/get-api-key)[Quickstart](/docs/en/get-started)[Authentication](/docs/en/manage-claude/authentication)

Building with Claude

[Features overview](/docs/en/build-with-claude/overview)[Using the Messages API](/docs/en/build-with-claude/working-with-messages)[Stop reasons and fallback](/docs/en/build-with-claude/handling-stop-reasons)[Refusals and fallback](/docs/en/build-with-claude/refusals-and-fallback)[Fallback credit](/docs/en/build-with-claude/fallback-credit)

Model capabilities

[Effort](/docs/en/build-with-claude/effort)[Task budgets (beta)](/docs/en/build-with-claude/task-budgets)[Fast mode (research preview)](/docs/en/build-with-claude/fast-mode)[Structured outputs](/docs/en/build-with-claude/structured-outputs)[Citations](/docs/en/build-with-claude/citations)[Streaming Messages](/docs/en/build-with-claude/streaming)[Batch processing](/docs/en/build-with-claude/batch-processing)[Search results](/docs/en/build-with-claude/search-results)[Streaming refusals](/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)[Multilingual support](/docs/en/build-with-claude/multilingual-support)[Embeddings](/docs/en/build-with-claude/embeddings)

[Thinking](/docs/en/build-with-claude/thinking)

Tools

[Overview](/docs/en/agents-and-tools/tool-use/overview)[How tool use works](/docs/en/agents-and-tools/tool-use/how-tool-use-works)[Tutorial: Build a tool-using agent](/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)[Define tools](/docs/en/agents-and-tools/tool-use/define-tools)[Handle tool calls](/docs/en/agents-and-tools/tool-use/handle-tool-calls)[Parallel tool use](/docs/en/agents-and-tools/tool-use/parallel-tool-use)[Tool Runner (SDK)](/docs/en/agents-and-tools/tool-use/tool-runner)[Strict tool use](/docs/en/agents-and-tools/tool-use/strict-tool-use)[Server tools](/docs/en/agents-and-tools/tool-use/server-tools)[Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)[Web fetch tool](/docs/en/agents-and-tools/tool-use/web-fetch-tool)[Code execution tool](/docs/en/agents-and-tools/tool-use/code-execution-tool)[Advisor tool](/docs/en/agents-and-tools/tool-use/advisor-tool)[Tool search tool](/docs/en/agents-and-tools/tool-use/tool-search-tool)[Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool)[Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool)[Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)[Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool)[Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool)[Troubleshooting](/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)

Tool infrastructure

[Tool reference](/docs/en/agents-and-tools/tool-use/tool-reference)[Manage tool context](/docs/en/agents-and-tools/tool-use/manage-tool-context)[Tool combinations](/docs/en/agents-and-tools/tool-use/tool-combinations)[Tool use with prompt caching](/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)[Programmatic tool calling](/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)[Fine-grained tool streaming](/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)

Context management

[Context windows](/docs/en/build-with-claude/context-windows)[Context editing](/docs/en/build-with-claude/context-editing)[Prompt caching](/docs/en/build-with-claude/prompt-caching)[Mid-conversation system messages and tool changes](/docs/en/build-with-claude/mid-conversation-system-messages)[Build an orchestration mode](/docs/en/build-with-claude/mid-conversation-effort-example)[Cache diagnostics](/docs/en/build-with-claude/cache-diagnostics)[Token counting](/docs/en/build-with-claude/token-counting)

[Compaction](/docs/en/build-with-claude/compaction)

Working with files

[Files API](/docs/en/build-with-claude/files)[PDF support](/docs/en/build-with-claude/pdf-support)

[Images and vision](/docs/en/build-with-claude/vision)

Skills

[Overview](/docs/en/agents-and-tools/agent-skills/overview)[Quickstart](/docs/en/agents-and-tools/agent-skills/quickstart)[Best practices](/docs/en/agents-and-tools/agent-skills/best-practices)[Skills for enterprise](/docs/en/agents-and-tools/agent-skills/enterprise)[Skills in the API](/docs/en/build-with-claude/skills-guide)

MCP

[Remote MCP servers](/docs/en/agents-and-tools/remote-mcp-servers)[MCP connector](/docs/en/agents-and-tools/mcp-connector)

[MCP tunnels](/docs/en/agents-and-tools/mcp-tunnels/overview)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](/docs/en/build-with-claude/claude-in-amazon-bedrock)[Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)[Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws)[Google Cloud](/docs/en/build-with-claude/claude-on-vertex-ai)[Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry)

[Console](/)

[Messages](/docs/en/intro)Claude on cloud platforms

# Claude on Google Cloud

Copy page



Anthropic's Claude models are available through [Google Cloud's Agent Platform](https://cloud.google.com/vertex-ai).

Copy page



The API for accessing Claude on Google Cloud's Agent Platform is nearly identical to the [Messages API](/docs/en/api/messages/create), with two key differences in request format:

- On Agent Platform, `model` is not passed in the request body. Instead, it is specified in the Google Cloud endpoint URL.
- On Agent Platform, `anthropic_version` is passed in the request body (rather than as a header), and must be set to the value `vertex-2023-10-16`.

Agent Platform is also supported by Anthropic's official [client SDKs](/docs/en/cli-sdks-libraries/overview). This guide walks you through making a request to Claude on Agent Platform using one of Anthropic's client SDKs.

Note that this guide assumes you already have a Google Cloud project that is able to use Agent Platform. See [Anthropic Claude models on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude) for more information on the setup required and a full walkthrough.

## Install an SDK for accessing Agent Platform

First, install Anthropic's [client SDK](/docs/en/cli-sdks-libraries/overview) for your language of choice.

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

Lifecycle terms (Deprecated, Retired) are defined in [Model deprecations](/docs/en/about-claude/model-deprecations). Lifecycle dates on partner-operated platforms are set by the partner and can differ from the Claude API schedule. For the current retirement date of any model on Agent Platform, see [Google Cloud's documentation for Claude models on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude).

| Model                                                                                         | Agent Platform API model ID |
|-----------------------------------------------------------------------------------------------|-----------------------------|
| Claude Fable 5.1                                                                              | claude-fable-5-1            |
| Claude Mythos 5.1 ([limited availability(opens in new tab)](https://anthropic.com/glasswing)) | claude-mythos-5-1           |
| Claude Fable 5                                                                                | claude-fable-5              |
| Claude Mythos 5 ([limited availability(opens in new tab)](https://anthropic.com/glasswing))   | claude-mythos-5             |
| Claude Opus 5.5                                                                               | claude-opus-5-5             |
| Claude Opus 5                                                                                 | claude-opus-5               |
| Claude Opus 4.8                                                                               | claude-opus-4-8             |
| Claude Opus 4.7                                                                               | claude-opus-4-7             |
| Claude Opus 4.6                                                                               | claude-opus-4-6             |
| Claude Opus 4.5                                                                               | claude-opus-4-5@20251101    |
| Claude Opus 4.1 ([deprecated](/docs/en/about-claude/model-deprecations))                      | claude-opus-4-1@20250805    |
| Claude Opus 4 ([deprecated](/docs/en/about-claude/model-deprecations))                        | claude-opus-4@20250514      |
| Claude Sonnet 5                                                                               | claude-sonnet-5             |
| Claude Sonnet 4.6                                                                             | claude-sonnet-4-6           |
| Claude Sonnet 4.5                                                                             | claude-sonnet-4-5@20250929  |
| Claude Sonnet 4 ([deprecated](/docs/en/about-claude/model-deprecations))                      | claude-sonnet-4@20250514    |
| Claude Haiku 4.5                                                                              | claude-haiku-4-5@20251001   |
| Claude Haiku 3.5 ([deprecated](/docs/en/about-claude/model-deprecations))                     | claude-3-5-haiku@20241022   |



Upgrading to a newer Claude model? In Claude Code, run `/claude-api migrate` to apply model ID swaps and breaking parameter changes across your codebase. The skill detects which cloud platform your code targets and adjusts model ID formats and feature changes for that platform. See [Migrating to a newer Claude model](/docs/en/agents-and-tools/agent-skills/claude-api-skill#migrating-to-a-newer-claude-model).

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

See the [client SDKs](/docs/en/cli-sdks-libraries/overview) and the official [Agent Platform docs](https://cloud.google.com/vertex-ai/docs) for more details.

Claude is also available through [Amazon Bedrock](/docs/en/build-with-claude/claude-in-amazon-bedrock), [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws), and [Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry).

## Data retention

Data handling for this offering is governed by Google Cloud. For details, see [Agent Platform and zero data retention](https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance).

## Activity logging

Agent Platform provides a [request-response logging service](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/request-response-logging) that allows you to log the prompts and completions associated with your usage.

Anthropic recommends that you log your activity on at least a 30-day rolling basis to understand your activity and investigate any potential misuse.



Turning on this service does not give Google or Anthropic any access to your content.

## Feature support

For the full feature list with Google Cloud availability, see [Features overview](/docs/en/build-with-claude/overview).

### Supported feature highlights

- [Messages API](/docs/en/api/messages/create)
- [Prompt caching](/docs/en/build-with-claude/prompt-caching)
- [Thinking](/docs/en/build-with-claude/thinking)
- [Tool use](/docs/en/agents-and-tools/tool-use/overview), including the [Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool), [Browser use tool](/docs/en/agents-and-tools/tool-use/browser-use-tool), [Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool), [Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool), and [Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)
- [Web search tool](/docs/en/agents-and-tools/tool-use/web-search-tool)
- [Citations](/docs/en/build-with-claude/citations)
- [Structured outputs](/docs/en/build-with-claude/structured-outputs)

### Features not supported

- Input sources (URL sources for images and documents, Files API)
- Server-side tools (code execution, web fetch, advisor)
- Agent infrastructure (Agent Skills, MCP connector, programmatic tool calling)
- API endpoints (Message Batches, Models, Admin, Compliance, Usage and Cost)
- Claude Managed Agents
- Server-side fallback (the [`fallbacks` parameter](/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback); use the [client-side fallback pattern](/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback) instead)

### Context window

Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5, and Claude Sonnet 4.6 have a [1M-token context window](/docs/en/build-with-claude/context-windows) on Agent Platform. Other Claude models, including Sonnet 4.5 and Sonnet 4 (deprecated), have a 200k-token context window.

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

Claude Mythos Preview is a research preview available to invited customers on Agent Platform. For more information, see [Project Glasswing](https://anthropic.com/glasswing).

## Additional resources

- **Agent Platform pricing:** [Generative AI pricing on cloud.google.com](https://cloud.google.com/vertex-ai/generative-ai/pricing)
- **Claude models documentation:** [Claude on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude)
- **Google blog post:** [Global endpoint for Claude models](https://cloud.google.com/blog/products/ai-machine-learning/global-endpoint-for-claude-models-generally-available-on-vertex-ai)
- **Anthropic pricing details:** [Cloud platform pricing](/docs/en/about-claude/pricing#cloud-platform-pricing)
