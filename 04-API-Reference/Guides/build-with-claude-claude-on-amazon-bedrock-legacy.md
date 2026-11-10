---
title: "Claude on Amazon Bedrock (Opus 4.6 and earlier) - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-05T06:36:41Z"
tags: ["api", "bedrock", "cli", "sdk"]
---

# Claude on Amazon Bedrock (Opus 4.6 and earlier)

Copy page



The legacy Amazon Bedrock integration for Claude models, using InvokeModel and Converse APIs with ARN-versioned model identifiers.

Copy page





This page covers the legacy Amazon Bedrock integration: the `InvokeModel` and `Converse` APIs with ARN-versioned model identifiers and AWS event-stream encoding. For models available on the Messages-API Bedrock endpoint, see [Claude in Amazon Bedrock](build-with-claude-claude-in-amazon-bedrock.md), which uses the Messages API at `/anthropic/v1/messages` with SSE streaming. For an Anthropic-operated alternative with AWS Marketplace billing and typically same-day feature access, see [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md). Existing Bedrock users can follow the [migration guide](build-with-claude-claude-platform-on-aws.md#migrating-from-amazon-bedrock).



The latest version of the SDK sends API version `2026-10-21` by default, including through Amazon Bedrock. The ARN-versioned models in the model table on this page don’t support `2026-10-21` on Bedrock, and requests to them that send it can return a 400 error. If you call them through the SDK, keep the SDK on the version you use today, and pin that version where you install it so a later install doesn’t upgrade it. The Boto3 example sets `anthropic_version` in its request body and isn’t affected.

To install an SDK for these models, use the commands in [Install an SDK for accessing Bedrock](#install-an-sdk-for-accessing-bedrock), which install the last major version before API version `2026-10-21`.

Calling Claude through Bedrock slightly differs from how you would call Claude on the Claude API directly. This guide walks you through completing an API call to Claude on Bedrock using one of Anthropic’s [client SDKs](../Other/cli-sdks-libraries-overview.md).

Note that this guide assumes you have already signed up for an [AWS account](https://portal.aws.amazon.com/billing/signup) and configured programmatic access.

## Install and configure the AWS CLI

1.  [Install a version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) at or newer than version `2.13.23`.
2.  Configure your AWS credentials using the AWS configure command (see [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)) or find your credentials by navigating to **Command line or programmatic access** within your AWS dashboard and following the directions in the modal window.
3.  Verify that your credentials are working:

AWS CLI



```python
aws sts get-caller-identity
```

## Install an SDK for accessing Bedrock

Anthropic’s [client SDKs](../Other/cli-sdks-libraries-overview.md) support Bedrock. You can also use an AWS SDK such as `boto3` directly.

Python

TypeScript

C#

Go

Java

PHP

Ruby

Boto3 (Python)

Python

```python
pip install -U "anthropic[bedrock]<2"
```



## Accessing Bedrock

### Subscribe to Anthropic models

Go to the [AWS Console \> Bedrock \> Model Access](https://console.aws.amazon.com/bedrock/home?region=us-west-2#/modelaccess) and request access to Anthropic models. Note that Anthropic model availability varies by region. See the [AWS documentation on model availability by region](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html) for the latest information.

#### API model IDs



Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Haiku 5.5, Claude Opus 4.8, and Claude Opus 4.7 are reachable through `InvokeModel` on `bedrock-runtime`. These requests are served by the same infrastructure as the [Claude in Amazon Bedrock](build-with-claude-claude-in-amazon-bedrock.md) endpoint. For the native Messages API request shape and full feature parity, use that page. These models are omitted from the model table on this page because they do not have ARN-versioned model IDs.

Lifecycle terms (Deprecated, Retired) are defined in [Model deprecations](../../20-Models/about-claude-model-deprecations.md). Lifecycle dates on partner-operated platforms are set by the partner and can differ from the Claude API schedule. For the current retirement date of any model on Amazon Bedrock, see [Amazon Bedrock’s model lifecycle page](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html).

AWS offers newer Claude models through [cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) rather than on-demand throughput. For these models, a request that passes the base model ID fails with an HTTP 400 error like the following:

```python
Invocation of model ID anthropic.claude-sonnet-4-5-20250929-v1:0 with on-demand throughput isn't supported. Retry your request with the ID or ARN of an inference profile that contains this model.
```



To call these models, pass an inference profile instead of the base model ID. The inference profile ID is the base model ID with a prefix from a column marked “Yes” in the following table, for example us.anthropic.claude-sonnet-4-5-20250929-v1:0. You can also pass the full inference profile ARN, in the form `arn:aws:bedrock:{region}:{account-id}:inference-profile/{inference-profile-id}`. For AWS’s authoritative list of available inference profiles, see [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html). To learn how the prefixes affect routing and pricing, see the [Global versus regional endpoints](#global-vs-regional-endpoints) section.

| Model | Base Bedrock model ID | `global` | `us` | `eu` | `jp` | `apac` |
|----|----|:---|:---|:---|:---|:---|
| Claude Opus 4.6 | anthropic.claude-opus-4-6-v1 | Yes | Yes | Yes | Yes | Yes |
| Claude Opus 4.5 | anthropic.claude-opus-4-5-20251101-v1:0 | Yes | Yes | Yes | No | No |
| Claude Opus 4.1 ([deprecated](../../20-Models/about-claude-model-deprecations.md)) | anthropic.claude-opus-4-1-20250805-v1:0 | No | Yes | No | No | No |
| Claude Sonnet 4.6 | anthropic.claude-sonnet-4-6 | Yes | Yes | Yes | Yes | No |
| Claude Sonnet 4.5 ([deprecated](../../20-Models/about-claude-model-deprecations.md)) | anthropic.claude-sonnet-4-5-20250929-v1:0 | Yes | Yes | Yes | Yes | No |
| Claude Sonnet 4 ([deprecated](../../20-Models/about-claude-model-deprecations.md)) | anthropic.claude-sonnet-4-20250514-v1:0 | Yes | Yes | Yes | No | Yes |
| Claude Haiku 4.5 | anthropic.claude-haiku-4-5-20251001-v1:0 | Yes | Yes | Yes | No | No |

### List available models

The following examples show how to print a list of all the Claude models available through Bedrock:

AWS CLI

Boto3 (Python)

TypeScript

C#

Go

Java

PHP

Ruby

Boto3 (Python)



```python
import boto3

bedrock = boto3.client(service_name="bedrock")
response = bedrock.list_foundation_models(byProvider="anthropic")

for summary in response["modelSummaries"]:
    print(summary["modelId"])
```

### Making requests

The following examples show how to generate text from Claude on Bedrock:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Boto3 (Python)

Python

```python
from anthropic import AnthropicBedrock

client = AnthropicBedrock(
    # Authenticate by either providing the following keys or using the default AWS credential providers, such as
    # using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
    aws_access_key="<access key>",
    aws_secret_key="<secret key>",
    # Temporary credentials can be used with aws_session_token.
    # Read more at https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html.
    aws_session_token="<session_token>",
    # aws_region changes the AWS region to which the request is made. If it is not provided, the SDK reads
    # AWS_REGION / AWS_DEFAULT_REGION, then the region configured for your boto3 session or AWS profile
    # (including ~/.aws/config), and raises ValueError if no region can be resolved.
    aws_region="us-west-2",
)

message = client.messages.create(
    model="global.anthropic.claude-opus-4-6-v1",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}],
)
print(message.content)
```



See the [client SDKs](../Other/cli-sdks-libraries-overview.md) for more details, and the [official Bedrock documentation](https://docs.aws.amazon.com/bedrock/).

### Bearer token authentication

You can authenticate with Bedrock using bearer tokens instead of AWS credentials. This is useful in corporate environments where teams need access to Bedrock without managing AWS credentials, IAM roles, or account-level permissions.

The simplest approach is to set the `AWS_BEARER_TOKEN_BEDROCK` environment variable, which the SDK detects automatically when resolving credentials from the environment.

To provide a token programmatically:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

```python
from anthropic import AnthropicBedrock

client = AnthropicBedrock(
    api_key="your-bearer-token",
    aws_region="us-west-2",
)

message = client.messages.create(
    model="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
print(message.content)
```



## Activity logging

Bedrock provides an [invocation logging service](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) that allows you to log the prompts and completions associated with your usage.

Anthropic recommends that you log your activity on at least a 30-day rolling basis to understand your activity and investigate any potential misuse.



Turning on this service does not give AWS or Anthropic any access to your content.

## Feature support

For the full feature list with Amazon Bedrock availability, see [Features overview](build-with-claude-overview.md).

### Supported feature highlights

- [Messages API](../Endpoints/messages-create.md)
- [Prompt caching](build-with-claude-prompt-caching.md)
- [Thinking](build-with-claude-thinking.md)
- [Tool use](../Agents-Tools/agents-and-tools-tool-use-overview.md), including the [Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md), [Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md), [Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md), and [Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)
- [Citations](build-with-claude-citations.md)
- [Structured outputs](build-with-claude-structured-outputs.md)

### Features not supported

- Input sources (URL sources for images and documents, Files API)
- Server-side tools (code execution, web search, web fetch, advisor)
- Agent infrastructure (Agent Skills, MCP connector, programmatic tool calling)
- API endpoints (Message Batches, Models, Admin, Compliance, Usage and Cost)
- Claude Managed Agents
- Server-side fallback (the [`fallbacks` parameter](build-with-claude-refusals-and-fallback.md#server-side-fallback); use the [client-side fallback pattern](build-with-claude-refusals-and-fallback.md#client-side-fallback) instead)
- Automatic prompt caching (the [top-level `cache_control` field](build-with-claude-prompt-caching.md#automatic-caching); use [explicit cache breakpoints](build-with-claude-prompt-caching.md#explicit-cache-breakpoints) instead)

### Computer use and browser use toolsets on Bedrock

The [computer use](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md) and [browser use](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md) toolsets are available through the InvokeModel API for these models:

- Claude Fable 5.1
- Claude Fable 5
- Claude Opus 5.5
- Claude Opus 5
- Claude Opus 4.8
- Claude Sonnet 5.5
- Claude Sonnet 5
- Claude Haiku 5.5

To use one, add an entry of type `computer_toolset_20260801` or `browser_toolset_20260801` to the `tools` array. No beta header is required for either toolset.

### PDF support on Bedrock

[PDF support](build-with-claude-pdf-support.md) is available on Bedrock through both the Converse API and the InvokeModel API.

### Mid-conversation system messages on Bedrock

[Mid-conversation system messages](build-with-claude-mid-conversation-system-messages.md) are available through the InvokeModel API for Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.8, Claude Sonnet 5.5, and Claude Haiku 5.5. As described in the note under [API model IDs](#api-model-ids), these requests are served by the same infrastructure as the [Claude in Amazon Bedrock](build-with-claude-claude-in-amazon-bedrock.md) endpoint. No beta header is required for mid-conversation system messages. This feature is not available on Claude Sonnet 5. Use the top-level `system` field instead. It is not available for the ARN-versioned models in the model table on this page.

A `role: "system"` message can also set `output_config.effort` to [change effort mid-conversation](build-with-claude-effort.md#change-effort-mid-conversation-beta) on Claude Fable 5.1 and Claude Opus 5.5. This is in beta: add `mid-conversation-output-config-2026-07-01` to the `anthropic_beta` array in the request body. Without that value, or on Claude Fable 5, Claude Opus 5, or Claude Opus 4.8, the request returns a 400 error: `messages.N.output_config: Extra inputs are not permitted`. In the error, `N` is the index of the `system` message in `messages`.

**For Converse API users:** the Converse API accepts system instructions through its top-level [`system` parameter](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html). To add system instructions mid-conversation, use the InvokeModel API.

### Context window

Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, and Claude Haiku 5.5 have a [1M-token context window](build-with-claude-context-windows.md) on Amazon Bedrock. Other Claude models, including Sonnet 4.5 (deprecated) and Sonnet 4 (deprecated), have a 200k-token context window.

Bedrock limits request payloads to 20 MB. When sending large documents or many images, you might reach this limit before the token limit.

## Global versus regional endpoints

Starting with **Claude Sonnet 4.5 and all future models**, Bedrock offers two endpoint types:

- **Global endpoints:** Dynamic routing for maximum availability
- **Regional endpoints:** Guaranteed data routing through specific geographic regions

Regional endpoints include a 10 percent pricing premium over global endpoints.



This applies to Claude Sonnet 4.5 (deprecated) and future models only. Older models (Claude Sonnet 4 (deprecated) and earlier) maintain their existing pricing structures.

### When to use each option

**Global endpoints (recommended):**

- Provide maximum availability and uptime
- Dynamically route requests to regions with available capacity
- Carry no pricing premium
- Work best for applications where data residency is flexible

**Regional endpoints (CRIS):**

- Route traffic through specific geographic regions
- Are required for data residency and compliance requirements
- Are available for US, EU, Japan, and Asia-Pacific
- Carry a 10 percent pricing premium that reflects infrastructure costs for dedicated regional capacity

### Implementation

**Using global endpoints (default for Opus 4.6, Sonnet 4.6, and Sonnet 4.5 (deprecated)):**

The model IDs for Claude Opus 4.6, Sonnet 4.6, and Sonnet 4.5 (deprecated) already include the `global.` prefix:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

```python
from anthropic import AnthropicBedrock

client = AnthropicBedrock(aws_region="us-west-2")

message = client.messages.create(
    model="global.anthropic.claude-opus-4-6-v1",
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}],
)
```



**Using regional endpoints (CRIS):**

To use regional endpoints, replace the `global.` prefix with a regional prefix such as `us.`:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

```python
from anthropic import AnthropicBedrock

client = AnthropicBedrock(aws_region="us-west-2")

# Using US regional endpoint (CRIS)
message = client.messages.create(
    model="us.anthropic.claude-opus-4-6-v1",  # Regional prefix
    max_tokens=256,
    messages=[{"role": "user", "content": "Hello, world"}],
)
```



## Additional resources

- **Bedrock pricing:** [Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/)
- **AWS pricing documentation:** [Bedrock pricing guide](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-pricing.html)
- **AWS blog post:** [Introducing Claude Sonnet 4.5 in Amazon Bedrock](https://aws.amazon.com/blogs/aws/introducing-claude-sonnet-4-5-in-amazon-bedrock-anthropics-most-intelligent-model-best-for-coding-and-complex-agents/)
- **Anthropic pricing details:** [Cloud platform pricing](../../17-Billing-Plans/about-claude-pricing.md#cloud-platform-pricing)
