---
title: "Claude Models on Google Cloud (Google managed) - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-08T06:24:57Z"
tags: ["api", "billing"]
---

# Claude Models on Google Cloud (Google managed)

Copy page



Google operates Claude Models on Google Cloud (Google managed) as part of Google Cloud’s Agent Platform. You can call Claude with Anthropic’s client SDKs.

Copy page



[Claude Models on Google Cloud](build-with-claude-claude-models-on-google-cloud-overview.md) compares the two Google Cloud offerings. It also shows how to tell which one you use.

## Before making API calls

To use Claude Models on Google Cloud (Google managed), you need:

1.  A Google Cloud project that can use Agent Platform. For setup steps, see Google Cloud’s [Anthropic Claude models on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude) page.
2.  The [gcloud CLI](https://cloud.google.com/sdk/docs/install) installed, for local development.
3.  For the identity making the calls, an IAM role that includes the `aiplatform.endpoints.predict` permission, such as Agent Platform User (`roles/aiplatform.user`). For details, see Google Cloud’s [Agent Platform partner models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models) page.
4.  Google Cloud credentials for that identity. For the SDK examples, you might need to run `gcloud auth application-default login` to authenticate with Google Cloud. The cURL examples for Claude Models on Google Cloud (Google managed) get their token with `gcloud auth print-access-token`. That command uses the gcloud CLI’s own login, not Application Default Credentials. For those examples, run `gcloud auth login` or `gcloud init` first.

### Install an SDK

Anthropic’s [client SDKs](../Other/cli-sdks-libraries-overview.md) support Claude Models on Google Cloud (Google managed) through `AnthropicVertex`. Install the package that provides it:

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

```python
pip install -U "anthropic[vertex]"
```



The `ant` CLI doesn’t support Claude Models on Google Cloud (Google managed).

## Making requests

Requests to Claude Models on Google Cloud (Google managed) go to an Agent Platform endpoint URL that ends in `:rawPredict`. Streaming requests use `:streamRawPredict` instead.

A request is nearly identical to a [Messages API](../Endpoints/messages-create.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. request. It differs in two main ways:

- **Model:** The endpoint URL names the model. In a cURL request, leave `model` out of the body.
- **Version:** In a cURL request, pass `anthropic_version` in the body, not as a header. Set it to `vertex-2023-10-16`, or to [API version `2026-10-21`](../Endpoints/migration-2026-10-21.md).

The following examples use the global endpoint. For the other endpoint types, see [Global, multi-region, and regional endpoints](#global-multi-region-and-regional-endpoints).

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

### API model IDs

| Model | Agent Platform API model ID |
|----|----|
| Claude Fable 5.1 | claude-fable-5-1 |
| Claude Mythos 5.1 ([limited availability(opens in new tab)](https://support.claude.com/en/articles/14604842)) | claude-mythos-5-1 |
| Claude Fable 5 | claude-fable-5 |
| Claude Mythos 5 ([limited availability(opens in new tab)](https://support.claude.com/en/articles/14604842)) | claude-mythos-5 |
| Claude Opus 5.5 | claude-opus-5-5 |
| Claude Opus 5 | claude-opus-5 |
| Claude Opus 4.8 | claude-opus-4-8 |
| Claude Opus 4.7 | claude-opus-4-7 |
| Claude Opus 4.6 | claude-opus-4-6 |
| Claude Opus 4.5 | claude-opus-4-5@20251101 |
| Claude Opus 4.1 ([deprecated](../../20-Models/about-claude-model-deprecations.md)) | claude-opus-4-1@20250805 |
| Claude Opus 4 ([deprecated](../../20-Models/about-claude-model-deprecations.md)) | claude-opus-4@20250514 |
| Claude Sonnet 5.5 | claude-sonnet-5-5 |
| Claude Sonnet 5 | claude-sonnet-5 |
| Claude Sonnet 4.6 | claude-sonnet-4-6 |
| Claude Sonnet 4.5 ([deprecated](../../20-Models/about-claude-model-deprecations.md)) | claude-sonnet-4-5@20250929 |
| Claude Sonnet 4 ([deprecated](../../20-Models/about-claude-model-deprecations.md)) | claude-sonnet-4@20250514 |
| Claude Haiku 5.5 | claude-haiku-5-5 |
| Claude Haiku 4.5 | claude-haiku-4-5@20251001 |

Claude Models on Google Cloud (Google managed) offers different Claude models in different regions. To check which models a region offers, search “Claude” in [Model Garden](https://cloud.google.com/model-garden) or see Google Cloud’s [Anthropic Claude models on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude) page.

Google sets the lifecycle dates for the models that Claude Models on Google Cloud (Google managed) serves. These dates can differ from the Claude API schedule. For a model’s current retirement date, see Google Cloud’s [Anthropic Claude models on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude) page. For what Deprecated and Retired mean, see [Model deprecations](../../20-Models/about-claude-model-deprecations.md).



Claude Mythos Preview is a research preview. Claude Models on Google Cloud (Google managed) offers it to invited customers. For more information, see [Project Glasswing](../../22-Safety-Policy/glasswing.md).

Claude Code

Let Claude Code migrate your code to a newer model

Run in

`❯``/claude-api`` migrate this project to the latest Claude Opus model`



## Global, multi-region, and regional endpoints

Claude Models on Google Cloud (Google managed) offers three endpoint types. You choose one with the region value you pass when you create the client. In a cURL request, the endpoint type sets the host and the `locations` segment of the URL.

[TABLE]

The endpoint types differ in where they send requests:

- **Global:** Requests go to any region with available capacity. Use it when you want maximum availability and data residency is flexible.
- **Multi-region:** Requests go to any region in the United States (`"us"`) or the European Union (`"eu"`). Use it when you need data residency within a broad geography and higher availability than a single region.
- **Regional:** Requests go only to the region you name, such as `"us-east5"` or `"europe-west1"`. Use it when you need single-region data residency or must meet strict compliance mandates.

Multi-region and regional endpoints cost 10 percent more than global endpoints. All three endpoint types take pay-as-you-go traffic, and provisioned throughput needs a regional endpoint.

Regional endpoints serve Claude Sonnet 4.6 and earlier models only. For newer models, use a global or multi-region endpoint.



The premium for multi-region and regional endpoints applies only to Claude Sonnet 4.5 (deprecated) and later models. For the models that keep their earlier pricing, see [Cloud platform pricing](../../17-Billing-Plans/about-claude-pricing.md#cloud-platform-pricing). For regional endpoints, the premium reflects infrastructure costs for dedicated regional capacity.

The following examples use the `us` multi-region endpoint. The highlighted lines set the region. For a full request on the global endpoint, see [Making requests](#accessing-vertex-ai).

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



```python
from anthropic import AnthropicVertex

project_id = "MY_PROJECT_ID"
region = "us"  # Multi-region identifier: "us" or "eu"

client = AnthropicVertex(project_id=project_id, region=region)
```

## Feature support

Features supported on Claude Models on Google Cloud (Google managed) include the following:

- [Messages API](../Endpoints/messages-create.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.
- [Prompt caching](build-with-claude-prompt-caching.md)
- [Thinking](build-with-claude-thinking.md)
- [Tool use](../Agents-Tools/agents-and-tools-tool-use-overview.md), including these tools:
  - [Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)
  - [Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)
  - [Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)
  - [Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)
  - [Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)
  - [Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)
- [Citations](build-with-claude-citations.md)
- [Structured outputs](build-with-claude-structured-outputs.md)

[Features overview](build-with-claude-overview.md) lists every feature. Each feature’s page shows whether Claude Models on Google Cloud (Google managed) supports it.

### Features not supported

Claude Models on Google Cloud (Google managed) doesn’t support the following:

- **Input sources:** URL sources for images and documents, and the Files API
- **Server-side tools:** Code execution, web fetch, and advisor
- **Agent infrastructure:** Agent Skills, MCP connector, and programmatic tool calling
- **API endpoints:** Message Batches API, Models API, Admin API, Compliance API, and Usage and Cost API
- **Claude Managed Agents**
- **Server-side fallback:** The [`fallbacks` parameter](build-with-claude-refusals-and-fallback.md#server-side-fallback)

Instead of server-side fallback, use the [client-side fallback pattern](build-with-claude-refusals-and-fallback.md#client-side-fallback).

### Context window

Claude Models on Google Cloud (Google managed) offers a [1M-token context window](build-with-claude-context-windows.md) for these models:

- Claude Fable 5.1
- Claude Fable 5
- Claude Opus 5.5
- Claude Opus 5
- Claude Opus 4.8
- Claude Opus 4.7
- Claude Opus 4.6
- Claude Sonnet 5.5
- Claude Sonnet 5
- Claude Sonnet 4.6
- Claude Haiku 5.5

Other Claude models have a 200k-token context window. These include Claude Sonnet 4.5 (deprecated) and Claude Sonnet 4 (deprecated).

Agent Platform limits request payloads to 30 MB. When you send large documents or many images, you might reach this limit before the token limit.

## Billing, rate limits, and logging

### Rate limits

Google Cloud manages rate limits and quotas for Claude Models on Google Cloud (Google managed). For details, including how to request a quota increase, see Google Cloud’s [Quotas for Anthropic Claude models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/quotas) page.

### Billing

Google Cloud invoices you for Claude Models on Google Cloud (Google managed). For prices, see Google Cloud’s [Generative AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing#claude-models) page. Prices also depend on the endpoint type. See [Global, multi-region, and regional endpoints](#global-multi-region-and-regional-endpoints).

### Data retention

Google Cloud governs data handling for Claude Models on Google Cloud (Google managed). For details, see [Agent Platform and zero data retention](https://cloud.google.com/vertex-ai/generative-ai/docs/data-governance).

### Monitoring and logging

To log prompts and completions for Claude Models on Google Cloud (Google managed), use Agent Platform’s [request-response logging service](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/request-response-logging).

Anthropic recommends that you keep at least the last 30 days of logs. The logs help you understand your activity and investigate possible misuse.



Turning on this service doesn’t give Google or Anthropic any access to your content.

## Migrating from Claude Models on Google Cloud (Anthropic managed)

For what changes when you move, see [How the two Google Cloud offerings differ](build-with-claude-claude-models-on-google-cloud-overview.md#how-the-two-google-cloud-offerings-differ). To move to Claude Models on Google Cloud (Google managed), follow these steps:

1.  1

    ### Set up access

    Check that your project and the identity that makes the calls meet the requirements in [Before making API calls](#before-making-api-calls).

2.  2

    ### Install the SDK package

    Install the package that provides the client for Claude Models on Google Cloud (Google managed). See [Install an SDK](#install-an-sdk-for-accessing-vertex-ai).

3.  3

    ### Replace the import and the client

    Change the code that imports and creates your client. Use `AnthropicVertex` in place of `AnthropicGoogleCloud`. A cURL request needs a new URL, new headers, and a new body. The following code creates the client for Claude Models on Google Cloud (Anthropic managed) that you use today:

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

    

    ``` shiki
    from anthropic import AnthropicGoogleCloud

    client = AnthropicGoogleCloud()
    ```

    The following code creates the client for Claude Models on Google Cloud (Google managed). It uses the global endpoint. For the other endpoint types, see [Global, multi-region, and regional endpoints](#global-multi-region-and-regional-endpoints).

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

    

    ``` shiki
    from anthropic import AnthropicVertex

    project_id = "MY_PROJECT_ID"
    region = "global"

    client = AnthropicVertex(project_id=project_id, region=region)
    ```

    This code passes your project ID and a region when it creates the client. Replace `MY_PROJECT_ID` with your project ID. The Messages API calls that you make with the client stay as they are. The exceptions are the model IDs and features in the next step.

4.  4

    ### Check model IDs and features

    - **Model IDs:** If you use a model earlier than Claude 4.6, replace the hyphen before the snapshot date in its ID with `@`. For example, `claude-haiku-4-5-20251001` becomes `claude-haiku-4-5@20251001`. For the models and their IDs, see [API model IDs](#api-model-ids).
    - **Features:** Check that the features your code uses aren’t listed in [Features not supported](#features-not-supported).

5.  5

    ### Run a test request

    Run the request in [Making requests](#accessing-vertex-ai) to check that your setup works. Then run your own code. Before you move production traffic, read about [rate limits for Claude Models on Google Cloud (Google managed)](#rate-limits).

## Next steps



[Features overview](build-with-claude-overview.md)

Explore Claude’s features.



[Anthropic Claude models on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude)

Check which Claude models each region offers, and their retirement dates.



[Agent Platform documentation](https://cloud.google.com/vertex-ai/docs)

Read Google Cloud’s Agent Platform documentation.



[Global endpoint for Claude models](https://cloud.google.com/blog/products/ai-machine-learning/global-endpoint-for-claude-models-generally-available-on-vertex-ai)

Read Google Cloud’s blog post about the global endpoint for Claude models.
