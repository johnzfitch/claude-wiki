---
title: "Claude in Amazon Bedrock (Opus 4.7 and later) - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-26T06:39:19Z"
tags: ["api", "authentication", "bedrock", "sdk"]
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fclaude-in-amazon-bedrock)

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

# Claude in Amazon Bedrock (Opus 4.7 and later)

Copy page



Access Claude models through Amazon Bedrock with AWS-native authentication, billing, and security boundaries.

Copy page



This guide walks you through setting up and making API calls to Claude in Amazon Bedrock. Claude in Amazon Bedrock runs on AWS-managed infrastructure with zero operator access (Anthropic personnel have no access to the inference infrastructure), letting you build sensitive applications entirely inside the AWS security boundary while using the same Messages API shape you use with Anthropic's first-party API.



This page covers Claude in Amazon Bedrock, which serves Claude through the Messages API at `/anthropic/v1/messages` on AWS-managed infrastructure. The previous Amazon Bedrock integration (the `InvokeModel` and `Converse` APIs with ARN-versioned model identifiers) remains available and is documented at [Claude on Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md). For an Anthropic-operated alternative on AWS with AWS Marketplace billing and typically same-day feature access, see [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md).

## Access

Amazon Bedrock sets access criteria for each Claude model individually. Claude Fable 5.1, Claude Fable 5, Claude Opus 4.8, Claude Sonnet 5, Claude Opus 4.7, and Claude Haiku 4.5 are open to all Amazon Bedrock customers. For any other model's current criteria, check [Amazon Bedrock model access](https://console.aws.amazon.com/bedrock/home#/modelaccess) in the AWS console. Claude Mythos Preview requires an invitation through [Project Glasswing](../../22-Safety-Policy/glasswing.md). For region availability, see [Regions](#regions).

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

Anthropic's [client SDKs](../Other/cli-sdks-libraries-overview.md) support Claude in Amazon Bedrock through a Bedrock-specific package or module.

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

Model IDs in Claude in Amazon Bedrock carry an `anthropic.` provider prefix. Model capabilities and behaviors are documented on the [Models overview](../../20-Models/about-claude-models-overview.md) page.

| Model                                                                                             | Model ID                        | Access                |
|---------------------------------------------------------------------------------------------------|---------------------------------|:----------------------|
| Claude Fable 5.1                                                                                  | anthropic.claude-fable-5-1      | Open                  |
| Claude Mythos 5.1 ([limited availability(opens in new tab)](../../22-Safety-Policy/glasswing.md))     | anthropic.claude-mythos-5-1     | Invitation only       |
| Claude Fable 5                                                                                    | anthropic.claude-fable-5        | Open                  |
| Claude Mythos 5 ([limited availability(opens in new tab)](../../22-Safety-Policy/glasswing.md))       | anthropic.claude-mythos-5       | Invitation only       |
| Claude Mythos Preview ([limited availability(opens in new tab)](../../22-Safety-Policy/glasswing.md)) | anthropic.claude-mythos-preview | Invitation only       |
| Claude Opus 5.5                                                                                   | anthropic.claude-opus-5-5       | [See Access](#access) |
| Claude Opus 5                                                                                     | anthropic.claude-opus-5         | [See Access](#access) |
| Claude Opus 4.8                                                                                   | anthropic.claude-opus-4-8       | Open                  |
| Claude Opus 4.7                                                                                   | anthropic.claude-opus-4-7       | Open                  |
| Claude Sonnet 5                                                                                   | anthropic.claude-sonnet-5       | Open                  |
| Claude Haiku 4.5                                                                                  | anthropic.claude-haiku-4-5      | Open                  |

Use Claude Code 2.1.255 or later with Claude Fable 5.1 on Amazon Bedrock, and 2.1.280 or later with Claude Opus 5.5; run `claude update` to upgrade.



Upgrading to a newer Claude model? In Claude Code, run `/claude-api migrate` to apply model ID swaps and breaking parameter changes across your codebase. The skill detects which cloud platform your code targets and adjusts model ID formats and feature changes for that platform. See [Migrating to a newer Claude model](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md#migrating-to-a-newer-claude-model).

## Feature support

For the full feature list with Amazon Bedrock availability, see [Features overview](build-with-claude-overview.md).

### Supported feature highlights

- [Messages API](../Endpoints/messages-create.md) (`/anthropic/v1/messages`)
- [Prompt caching](build-with-claude-prompt-caching.md)
- [Thinking](build-with-claude-thinking.md)
- [Tool use](../Agents-Tools/agents-and-tools-tool-use-overview.md), including the [Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md), [Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md), [Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md), and [Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)
- [Citations](build-with-claude-citations.md)

### Features not supported

- [Structured outputs](build-with-claude-structured-outputs.md)
- Input sources (URL sources for images and documents, Files API)
- Server-side tools (code execution, web search, web fetch, advisor)
- Agent infrastructure (Agent Skills, MCP connector, programmatic tool calling)
- API endpoints (Message Batches, Models, Admin, Compliance, Usage and Cost)
- Claude Managed Agents
- Server-side fallback (the [`fallbacks` parameter](build-with-claude-refusals-and-fallback.md#server-side-fallback); use the [client-side fallback pattern](build-with-claude-refusals-and-fallback.md#client-side-fallback) instead)
- [Computer use](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) and [browser use](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md) toolsets (`computer_toolset_20260801` and `browser_toolset_20260801` are not currently available on Amazon Bedrock; the beta computer use tool versions remain available)

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

**Claude Mythos Preview** is a research preview model available to invited customers on Amazon Bedrock. For more information, see [Project Glasswing](../../22-Safety-Policy/glasswing.md).
