---
title: "Claude Code on Microsoft Foundry - Claude Code Docs"
source_url: "https://code.claude.com/docs/en/microsoft-foundry"
category: "02-Claude-Code-CLI"
fetched_at: "2026-09-16T06:24:08Z"
tags: ["claude-code"]
---

## On this page

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [1. Provision Microsoft Foundry resource](#1-provision-microsoft-foundry-resource)
  - [2. Configure Azure credentials](#2-configure-azure-credentials)
  - [3. Configure Claude Code](#3-configure-claude-code)
  - [4. Pin model versions](#4-pin-model-versions)
  - [5. Run Claude Code](#5-run-claude-code)
- [Azure RBAC configuration](#azure-rbac-configuration)
- [Troubleshooting](#troubleshooting)
- [Additional resources](#additional-resources)

Deployment

# Claude Code on Microsoft Foundry

Copy pageCopy page

Learn about configuring Claude Code through Microsoft Foundry, including setup, configuration, and troubleshooting.

Copy pageCopy page


[​](#prerequisites)

Prerequisites

Before configuring Claude Code with Microsoft Foundry, ensure you have:

- An Azure subscription with access to Microsoft Foundry
- RBAC permissions to create Microsoft Foundry resources and deployments
- Azure CLI installed and configured (optional - only needed if you don’t have another mechanism for getting credentials)

If you are deploying Claude Code to multiple users, [pin your model versions](#4-pin-model-versions) before rolling out.


[​](#setup)

Setup


[​](#1-provision-microsoft-foundry-resource)

1. Provision Microsoft Foundry resource

First, create a Claude resource in Azure:

1.  Go to the [Microsoft Foundry portal](https://ai.azure.com/)
2.  Create a new resource, noting your resource name
3.  Create deployments for the Claude models, noting the deployment name you give each; you’ll set these names as the model variables in step 4:
    - Claude Opus
    - Claude Sonnet
    - Claude Haiku

    When you configure a deployment, you also choose its [hosting option](../04-API-Reference/Guides/build-with-claude-claude-in-microsoft-foundry.md#hosting-options), which determines whether inference runs on Azure or on Anthropic infrastructure.


[​](#2-configure-azure-credentials)

2. Configure Azure credentials

Claude Code supports three authentication methods for Microsoft Foundry. Choose the method that best fits your security requirements. **Option A: API key authentication**

1.  Navigate to your resource in the Microsoft Foundry portal
2.  Go to the **Endpoints and keys** section
3.  Copy **API Key**
4.  Set the environment variable, replacing `your-azure-api-key` with the key you copied:

```python
export ANTHROPIC_FOUNDRY_API_KEY=your-azure-api-key
```

**Option B: Microsoft Entra ID authentication** When neither `ANTHROPIC_FOUNDRY_API_KEY` nor `ANTHROPIC_FOUNDRY_AUTH_TOKEN` is set, Claude Code automatically uses the Azure SDK [default credential chain](https://learn.microsoft.com/en-us/azure/developer/javascript/sdk/authentication/credential-chains#defaultazurecredential-overview). This supports a variety of methods for authenticating local and remote workloads. On local environments, you commonly may use the Azure CLI:

```python
az login
```

**Option C: Bearer token authentication** Claude Code sends the value of `ANTHROPIC_FOUNDRY_AUTH_TOKEN` on every request as the `Authorization: Bearer` header. Use this option when another process, such as a host application or a sign-in script, has already obtained an access token for you. Requires Claude Code v2.1.203 or later. Set the variable to a bearer token that Microsoft Entra ID issued for your resource:

```python
export ANTHROPIC_FOUNDRY_AUTH_TOKEN=your-entra-access-token
```

`ANTHROPIC_FOUNDRY_AUTH_TOKEN` takes precedence over `ANTHROPIC_FOUNDRY_API_KEY` and over the default credential chain.

When using Microsoft Foundry, the `/logout` command is unavailable since authentication is handled through Azure credentials.


[​](#3-configure-claude-code)

3. Configure Claude Code

Set the following environment variables to enable Microsoft Foundry:

```python
# Enable Microsoft Foundry integration
export CLAUDE_CODE_USE_FOUNDRY=1

# Azure resource name (replace {resource} with your resource name)
export ANTHROPIC_FOUNDRY_RESOURCE={resource}
# Or provide the full base URL:
# export ANTHROPIC_FOUNDRY_BASE_URL=https://{resource}.services.ai.azure.com/anthropic
```


[​](#4-pin-model-versions)

4. Pin model versions

Pin specific model versions for every deployment. Without pinning, model aliases such as `sonnet` and `opus` resolve to Claude Code’s built-in default for Microsoft Foundry, which can lag the newest release and may not yet be available in your account. Microsoft Foundry has no startup model check, so requests fail when the default is unavailable. When you create Azure deployments, select a specific model version rather than “auto-update to latest.”

Set the model variables to match the deployment names you created in step 1. Without `ANTHROPIC_DEFAULT_OPUS_MODEL`, the `opus` alias on Microsoft Foundry resolves to Opus 4.6. Set it to the ID of a newer Opus model, such as Opus 4.8:

```python
export ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-8'
export ANTHROPIC_DEFAULT_SONNET_MODEL='claude-sonnet-5'
export ANTHROPIC_DEFAULT_HAIKU_MODEL='claude-haiku-4-5'
```

Background tasks such as session title generation use the small/fast model, normally a Haiku-class model. On Microsoft Foundry, Claude Code defaults this to the primary model because not every account has a Haiku deployment. To use Haiku for background tasks, set `ANTHROPIC_DEFAULT_HAIKU_MODEL` to a Haiku deployment that is available in your account, as shown above. For current and legacy model IDs, see [Models overview](../20-Models/about-claude-models-overview.md). See [Model configuration](model-config.md#pin-models-for-third-party-deployments) for the full list of environment variables. [Prompt caching](prompt-caching.md) is enabled automatically. To request a 1-hour cache TTL instead of the 5-minute default, set the following variable; cache writes with a 1-hour TTL are billed at a higher rate:

```python
export ENABLE_PROMPT_CACHING_1H=1
```

To set different TTLs for your main conversation and for the requests Claude Code makes outside it, [choose the TTL yourself](prompt-caching.md#choose-the-ttl-yourself).


[​](#5-run-claude-code)

5. Run Claude Code

With the environment variables set, start Claude Code from your project directory:

```python
claude
```

Claude Code reads `CLAUDE_CODE_USE_FOUNDRY` and the other Microsoft Foundry variables from the environment and connects to your Azure resource on the first prompt. Unlike Amazon Bedrock and Google Cloud’s Agent Platform, Microsoft Foundry has no interactive setup wizard, so the environment variables in steps 3 and 4 are the only configuration path. To verify your setup, run `/status` inside Claude Code. The API provider line shows `Microsoft Foundry`, along with the resource name or base URL you configured.


[​](#azure-rbac-configuration)

Azure RBAC configuration

The `Azure AI User` and `Cognitive Services User` default roles include all required permissions for invoking Claude models. For more restrictive permissions, create a custom role with the following:

```python
{
  "permissions": [
    {
      "dataActions": [
        "Microsoft.CognitiveServices/accounts/providers/*"
      ]
    }
  ]
}
```

For details, see [Microsoft Foundry RBAC documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/rbac-azure-ai-foundry).


[​](#troubleshooting)

Troubleshooting

If you receive an error “Failed to get token from azureADTokenProvider: ChainedTokenCredential authentication failed”:

- Configure Entra ID on the environment, or set `ANTHROPIC_FOUNDRY_API_KEY`.

If requests fail with repeated connection errors on the first prompt:

- Check that `ANTHROPIC_FOUNDRY_RESOURCE` is set to your actual resource name rather than a placeholder. Claude Code builds the endpoint URL from this value, so an incorrect name points at a host that doesn’t exist.


[​](#additional-resources)

Additional resources

- [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry)
- [Microsoft Foundry models](https://ai.azure.com/explore/models)
- [Microsoft Foundry pricing](https://azure.microsoft.com/en-us/pricing/details/ai-foundry/)
