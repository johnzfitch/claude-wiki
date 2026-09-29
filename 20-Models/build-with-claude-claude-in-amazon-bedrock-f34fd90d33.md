---
title: "Claude in Amazon Bedrock (Opus 4.7 and later) - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock"
category: "20-Models"
fetched_at: "2026-09-26T06:39:19Z"
tags: ["authentication", "bedrock", "sdk"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fclaude-in-amazon-bedrock)

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

# Claude in Amazon Bedrock (Opus 4.7 and later)

Copy page



Access Claude models through Amazon Bedrock with AWS-native authentication, billing, and security boundaries.

Copy page



This guide walks you through setting up and making API calls to Claude in Amazon Bedrock. Claude in Amazon Bedrock runs on AWS-managed infrastructure with zero operator access (Anthropic personnel have no access to the inference infrastructure), letting you build sensitive applications entirely inside the AWS security boundary while using the same Messages API shape you use with Anthropic's first-party API.



This page covers Claude in Amazon Bedrock, which serves Claude through the Messages API at `/anthropic/v1/messages` on AWS-managed infrastructure. The previous Amazon Bedrock integration (the `InvokeModel` and `Converse` APIs with ARN-versioned model identifiers) remains available and is documented at [Claude on Amazon Bedrock (Opus 4.6 and earlier)](/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy). For an Anthropic-operated alternative on AWS with AWS Marketplace billing and typically same-day feature access, see [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws).

## Access

Amazon Bedrock sets access criteria for each Claude model individually. Claude Fable 5.1, Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, Claude Opus 4.7, and Claude Haiku 4.5 are open to all Amazon Bedrock customers. For any other model's current criteria, check [Amazon Bedrock model access](https://console.aws.amazon.com/bedrock/home#/modelaccess) in the AWS console. Claude Mythos Preview requires an invitation through [Project Glasswing](https://anthropic.com/glasswing). For region availability, see [Regions](#regions).

## Prerequisites

Before you begin, ensure you have:

- An AWS account with [Amazon Bedrock model access](https://console.aws.amazon.com/bedrock/home#/modelaccess) enabled for the Claude models you intend to use.
- The [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed and configured (optional, for credential management).

Claude Mythos Preview additionally requires a dedicated AWS account that has been allowlisted by the Bedrock Marketplace team. Your Anthropic account executive can submit your account ID for allowlisting (typically processed within 24 hours), and AWS sends a welcome email once it's complete.

## Authentication

Claude in Amazon Bedrock supports three authentication paths. Choose the one that best fits your security requirements.

### Bedrock service role (recommended)

Use a Bedrock service role with AWS-managed keys for the most secure, long-lived access:

1.  1

    ### Admin: provision the service role

    An AWS administrator provisions a Bedrock service role and grants developers `iam:PassRole` permission on the service role ARN.

2.  2

    ### Developer: pass the role

    When calling the API, Bedrock assumes the service role on your behalf. See the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html) for how to associate the role with your requests.

### IAM assumed roles

For identity-federated access with a 12-hour maximum session:

1.  1

    ### Admin: configure the IAM role

    Create an IAM role scoped to your Claude models. The trust policy names your identity provider (SAML, OIDC, or AWS Identity Center). The permissions policy grants `bedrock-mantle:CreateInference` only on the allowed model ARNs.

2.  2

    ### Developer: authenticate and assume

    Authenticate through your corporate identity provider, then assume the IAM role. AWS STS issues temporary credentials that the SDK or CLI uses to sign requests.

### Bearer tokens

For short-term access without IAM roles (12-hour maximum, least preferred):

1.  1

    ### Admin: restrict token types

    Block long-term keys by attaching a policy that denies `bedrock:CallWithBearerToken` unless the `bedrock:BearerTokenType` condition matches a short-term token.

2.  2

    ### Developer: mint a token

    Use the `aws-bedrock-token-generator` CLI to mint a bearer token. Pass it in the `x-api-key` header on each request.

## Install an SDK

Anthropic's [client SDKs](/docs/en/cli-sdks-libraries/overview) support Claude in Amazon Bedrock through a Bedrock-specific package or module.

Python

TypeScript

C#

Go

Java

PHP

Ruby

```python
pip install -U "anthropic[bedrock]"
```



## Making your first request

The endpoint follows the pattern `https://bedrock-mantle.{region}.api.aws/anthropic/v1/messages`. Unlike the `InvokeModel`-based integration, this endpoint uses standard SSE streaming and the same request body shape as Anthropic's first-party API.

The SDK resolves credentials and region using the standard AWS precedence: constructor arguments, then environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`, `AWS_REGION`), then the AWS config file and credential chain (SSO, assumed roles, ECS task role, IMDS).

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
from anthropic import AnthropicBedrockMantle

client = AnthropicBedrockMantle(aws_region="us-east-1")

message = client.messages.create(
    model="anthropic.claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)

print(next(block.text for block in message.content if block.type == "text"))
```





You can also use the standard `Anthropic` client: set `base_url` to `https://bedrock-mantle.{region}.api.aws/anthropic` and pass your bearer token as `api_key`. This path supports bearer-token authentication only. SigV4 signing requires `AnthropicBedrockMantle`.

## Supported models

Model IDs in Claude in Amazon Bedrock carry an `anthropic.` provider prefix. Model capabilities and behaviors are documented on the [Models overview](/docs/en/models/overview) page.

| Model                                                                                             | Model ID                        | Access                |
|---------------------------------------------------------------------------------------------------|---------------------------------|:----------------------|
| Claude Fable 5.1                                                                                  | anthropic.claude-fable-5-1      | Open                  |
| Claude Mythos 5.1 ([limited availability(opens in new tab)](https://anthropic.com/glasswing))     | anthropic.claude-mythos-5-1     | Invitation only       |
| Claude Fable 5                                                                                    | anthropic.claude-fable-5        | Open                  |
| Claude Mythos 5 ([limited availability(opens in new tab)](https://anthropic.com/glasswing))       | anthropic.claude-mythos-5       | Invitation only       |
| Claude Mythos Preview ([limited availability(opens in new tab)](https://anthropic.com/glasswing)) | anthropic.claude-mythos-preview | Invitation only       |
| Claude Opus 5.5                                                                                   | anthropic.claude-opus-5-5       | [See Access](#access) |
| Claude Opus 5                                                                                     | anthropic.claude-opus-5         | [See Access](#access) |
| Claude Opus 4.8                                                                                   | anthropic.claude-opus-4-8       | Open                  |
| Claude Opus 4.7                                                                                   | anthropic.claude-opus-4-7       | Open                  |
| Claude Sonnet 5                                                                                   | anthropic.claude-sonnet-5       | Open                  |
| Claude Haiku 4.5                                                                                  | anthropic.claude-haiku-4-5      | Open                  |

Use Claude Code 2.1.255 or later with Claude Fable 5.1 on Amazon Bedrock, and 2.1.280 or later with Claude Opus 5.5; run `claude update` to upgrade.



Upgrading to a newer Claude model? In Claude Code, run `/claude-api migrate` to apply model ID swaps and breaking parameter changes across your codebase. The skill detects which cloud platform your code targets and adjusts model ID formats and feature changes for that platform. See [Migrating to a newer Claude model](/docs/en/agents-and-tools/agent-skills/claude-api-skill#migrating-to-a-newer-claude-model).

## Feature support

For the full feature list with Amazon Bedrock availability, see [Features overview](/docs/en/build-with-claude/overview).

### Supported feature highlights

- [Messages API](/docs/en/api/messages/create) (`/anthropic/v1/messages`)
- [Prompt caching](/docs/en/build-with-claude/prompt-caching)
- [Thinking](/docs/en/build-with-claude/thinking)
- [Tool use](/docs/en/agents-and-tools/tool-use/overview), including the [Bash tool](/docs/en/agents-and-tools/tool-use/bash-tool), [Computer use tool](/docs/en/agents-and-tools/tool-use/computer-use-tool), [Memory tool](/docs/en/agents-and-tools/tool-use/memory-tool), and [Text editor tool](/docs/en/agents-and-tools/tool-use/text-editor-tool)
- [Citations](/docs/en/build-with-claude/citations)

### Features not supported

- [Structured outputs](/docs/en/build-with-claude/structured-outputs)
- Input sources (URL sources for images and documents, Files API)
- Server-side tools (code execution, web search, web fetch, advisor)
- Agent infrastructure (Agent Skills, MCP connector, programmatic tool calling)
- API endpoints (Message Batches, Models, Admin, Compliance, Usage and Cost)
- Claude Managed Agents
- Server-side fallback (the [`fallbacks` parameter](/docs/en/build-with-claude/refusals-and-fallback#server-side-fallback); use the [client-side fallback pattern](/docs/en/build-with-claude/refusals-and-fallback#client-side-fallback) instead)
- [Computer use](/docs/en/agents-and-tools/tool-use/computer-use-tool) and [browser use](/docs/en/agents-and-tools/tool-use/browser-use-tool) toolsets (`computer_toolset_20260801` and `browser_toolset_20260801` are not currently available on Amazon Bedrock; the beta computer use tool versions remain available)

## Regions

Claude in Amazon Bedrock is available in the following AWS regions. Amazon Bedrock offers two endpoint types:

- **Global:** dynamic routing across all available regions for maximum availability. No pricing premium.
- **Regional:** the endpoint resolves to the single AWS region you specify, for data-residency requirements. Regional endpoints carry a 10% pricing premium over global endpoints. To route across multiple regions within a geography, use an [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) (US, EU, JP, or AU). Regions marked **In-region only** in the table support direct single-region routing without an inference profile.

The global endpoint is available for Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 5, and Claude Haiku 4.5. For Claude Fable 5.1, regional endpoints are currently available in `us-east-1` only. Claude Mythos Preview is regional only and is available in `us-east-1`.

| AWS region       | Location                  | Endpoint types             |
|------------------|---------------------------|----------------------------|
| `af-south-1`     | Africa (Cape Town)        | Global                     |
| `ap-northeast-1` | Asia Pacific (Tokyo)      | Global, JP, In-region only |
| `ap-northeast-2` | Asia Pacific (Seoul)      | Global                     |
| `ap-northeast-3` | Asia Pacific (Osaka)      | Global, JP                 |
| `ap-south-1`     | Asia Pacific (Mumbai)     | Global                     |
| `ap-south-2`     | Asia Pacific (Hyderabad)  | Global                     |
| `ap-southeast-1` | Asia Pacific (Singapore)  | Global                     |
| `ap-southeast-2` | Asia Pacific (Sydney)     | Global, AU                 |
| `ap-southeast-3` | Asia Pacific (Jakarta)    | Global                     |
| `ap-southeast-4` | Asia Pacific (Melbourne)  | Global, AU, In-region only |
| `ca-central-1`   | Canada (Central)          | Global, US                 |
| `ca-west-1`      | Canada West (Calgary)     | Global                     |
| `eu-central-1`   | Europe (Frankfurt)        | Global, EU                 |
| `eu-central-2`   | Europe (Zurich)           | Global, EU                 |
| `eu-north-1`     | Europe (Stockholm)        | Global, EU, In-region only |
| `eu-south-1`     | Europe (Milan)            | Global, EU                 |
| `eu-south-2`     | Europe (Spain)            | Global, EU                 |
| `eu-west-1`      | Europe (Ireland)          | Global, EU, In-region only |
| `eu-west-2`      | Europe (London)           | Global, EU                 |
| `eu-west-3`      | Europe (Paris)            | Global, EU                 |
| `il-central-1`   | Israel (Tel Aviv)         | Global                     |
| `me-central-1`   | Middle East (UAE)         | Global                     |
| `sa-east-1`      | South America (São Paulo) | Global                     |
| `us-east-1`      | US East (N. Virginia)     | Global, US, In-region only |
| `us-east-2`      | US East (Ohio)            | Global, US, In-region only |
| `us-west-1`      | US West (N. California)   | Global, US                 |
| `us-west-2`      | US West (Oregon)          | Global, US, In-region only |

## Quotas

Default quota is 2 million input tokens per minute (TPM). You can request up to 5 million input TPM and 500,000 output TPM without additional Anthropic approval. AWS enforces requests-per-minute (RPM) limits on the Bedrock side; contact AWS support for RPM adjustments.

## Data retention

Data handling for this offering is governed by Amazon Bedrock. For details, see [Data protection in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html).

## Monitoring and logging

Claude in Amazon Bedrock emits logs to both CloudWatch and CloudTrail. Anthropic recommends retaining activity logs on at least a 30-day rolling basis to understand usage patterns and investigate potential issues.

## Support

For support, contact **<bedrock-ant-eap@amazon.com>**. Include your AWS account ID and the `request-id` from any failed API responses.



**Claude Mythos Preview** is a research preview model available to invited customers on Amazon Bedrock. For more information, see [Project Glasswing](https://anthropic.com/glasswing).
