---
title: "Data residency - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/data-residency"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:35Z"
tags: ["api"]
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fdata-residency)





SearchCtrlK

Organization

[Admin API](/docs/en/manage-claude/admin-api)[User management](/docs/en/manage-claude/user-management)[Workspaces](/docs/en/manage-claude/workspaces)

Authentication

[Overview](/docs/en/manage-claude/authentication)[Create an Admin API key](/docs/en/manage-claude/admin-api-keys)[App Attest](/docs/en/manage-claude/app-attest)[Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation)[Manage WIF via API](/docs/en/manage-claude/wif-admin-api)[WIF reference](/docs/en/manage-claude/wif-reference)

Identity providers

Monitoring

[Usage and Cost API](/docs/en/manage-claude/usage-cost-api)[Rate Limits API](/docs/en/manage-claude/rate-limits-api)[Analytics APIs](/docs/en/manage-claude/analytics-api)[Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api)[Spend Limits API](/docs/en/manage-claude/spend-limits-api)

Data & compliance

[Data residency](/docs/en/manage-claude/data-residency)[API and data retention](/docs/en/manage-claude/api-and-data-retention)[Access Transparency](/docs/en/manage-claude/access-transparency)

[Encryption keys](/docs/en/manage-claude/cmek)

[Inference hooks](/docs/en/manage-claude/inference-hooks)

Compliance API

[Overview](/docs/en/manage-claude/compliance-api)[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)[Activity Feed](/docs/en/manage-claude/compliance-activity-feed)[Chats, files, and projects](/docs/en/manage-claude/compliance-content-data)[Session transcripts](/docs/en/manage-claude/compliance-sessions)[Organizations, users, roles, groups, and settings](/docs/en/manage-claude/compliance-org-data)[Design your integration](/docs/en/manage-claude/compliance-integration-patterns)[Errors](/docs/en/manage-claude/compliance-errors)[FAQ](/docs/en/manage-claude/compliance-faq)

[Console](/)

[Admin](/docs/en/manage-claude/admin-api)Data & compliance

# Data residency

Copy page



Manage where model inference runs and where data is stored with geographic controls.

Copy page



Data residency controls let you manage where your data is processed and stored. Two independent settings govern this:

- **Inference geo:** Controls where model inference runs, on a per-request basis. Set through the `inference_geo` API parameter or as a workspace default.
- **Workspace geo:** Controls where data is stored at rest and where endpoint processing (such as image transcoding and code execution) happens. Configured at the workspace level in the [Claude Console](https://platform.claude.com).



[Claude Managed Agents](/docs/en/managed-agents/overview) supports geographic pinning at the agent level: `inference_geo` on an [agent's model configuration](/docs/en/managed-agents/agent-setup#pin-the-inference-geo) pins the geography that serves model requests for sessions running that agent, with [per-session overrides](/docs/en/managed-agents/sessions#pin-the-inference-geo-for-a-session) at session create. Agents without a pin follow the workspace's default inference geo on each request. Managed Agents also respects the Workspace geo configured in Console, and with [self-hosted sandboxes](/docs/en/managed-agents/self-hosted-sandboxes), tool execution and the sandbox filesystem stay on infrastructure you control; the contents of attached [memory stores](/docs/en/managed-agents/self-hosted-sandboxes#use-memory-stores) remain stored by Anthropic and are copied to your sandbox for the session.

## Inference geo



To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](/docs/en/manage-claude/api-and-data-retention).

The `inference_geo` parameter controls where model inference runs for a specific API request. Add it to any `POST /v1/messages` call.

| Value      | Description                                                                                     |
|:-----------|:------------------------------------------------------------------------------------------------|
| `"global"` | Default. Inference may run in any available geography for optimal performance and availability. |
| `"us"`     | Inference runs only in US-based infrastructure.                                                 |

### API usage

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
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    inference_geo="us",
    messages=[
        {"role": "user", "content": "Summarize the key points of this document."}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
# Check where inference actually ran
print(f"Inference geo: {response.usage.inference_geo}")
```

### Response

The response `usage` object includes an `inference_geo` field indicating where inference ran:

Output



```python
{
  "usage": {
    "input_tokens": 25,
    "output_tokens": 150,
    "inference_geo": "us"
  }
}
```

### Model availability

The `inference_geo` parameter is supported on Claude 4.6 and later models. Requests with `inference_geo` on Claude Opus 4.5, Claude Sonnet 4.5, Claude Haiku 4.5, or earlier models return a 400 error.



The `inference_geo` parameter is available on the Claude API (first-party) and [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws). On Amazon Bedrock and Google Cloud, the inference region is determined by the endpoint URL or inference profile, so `inference_geo` is not applicable. On [Claude in Microsoft Foundry](/docs/en/build-with-claude/claude-in-microsoft-foundry), `inference_geo` is likewise not applicable: deployments hosted on Azure can instead use the US Data Zone Standard deployment type, which keeps inference within the United States. The `inference_geo` parameter is also not available through the [OpenAI SDK compatibility endpoint](/docs/en/cli-sdks-libraries/libraries/openai-sdk).

### Workspace-level restrictions

Workspace settings also support restricting which inference geos are available:

- **`allowed_inference_geos`:** Restricts which geos a workspace can use. If a request specifies an `inference_geo` not in this list, the API returns an error.
- **`default_inference_geo`:** Sets the fallback geo when `inference_geo` is omitted from a request. Individual requests can override this by setting `inference_geo` explicitly.

These settings can be configured through the Console or the [Admin API](/docs/en/manage-claude/admin-api) under the `data_residency` field.

## Workspace geo

Workspace geo is set when you create a workspace and can't be changed afterward. Currently, `"us"` is the only available workspace geo.

To set workspace geo, create a new workspace in the [Console](https://platform.claude.com):

1.  Go to **Settings** \> **Workspaces**.
2.  Create a new workspace.
3.  Select the workspace geo.



**Claude Platform on AWS:** Workspace geo is not configurable. Claude Managed Agents sessions on this platform run with an effective Workspace geo of `"us"`, which is currently the only available workspace geo. See [Claude Platform on AWS](/docs/en/build-with-claude/claude-platform-on-aws) for data residency considerations specific to that platform.

## Pricing

Data residency pricing varies by model generation:

- **Claude 4.6 and later models:** US-only inference (`inference_geo: "us"`) is priced at 1.1x the standard rate across all token pricing categories (input tokens, output tokens, cache writes, and cache reads).
- **Global routing** (`inference_geo: "global"`): Standard pricing applies.
- **Older models:** Don't support `inference_geo` (see [Model availability](#model-availability)); standard pricing applies. Requests that include the parameter return a 400 error.

This pricing applies to the Claude API (first-party) and Claude Platform on AWS. On Claude in Microsoft Foundry, the same 1.1x multiplier applies to deployments hosted on Azure that use the US Data Zone Standard deployment type. Partner-operated platforms (Bedrock and Google Cloud) have their own regional pricing. See [Data residency pricing](/docs/en/about-claude/pricing#data-residency-pricing) for details.

The same multiplier applies to [Claude Managed Agents](/docs/en/managed-agents/overview): when an agent's [model configuration](/docs/en/managed-agents/agent-setup) pins `inference_geo` to `"us"`, model requests in sessions running that agent are priced at 1.1x the standard rate.



If you have a [Priority Tier](/docs/en/api/service-tiers) commitment, the 1.1x multiplier for US-only inference also affects how tokens are counted against your Priority Tier capacity. Each token consumed with `inference_geo: "us"` draws down 1.1 tokens from your committed TPM, consistent with how other pricing multipliers (such as prompt caching) affect burndown rates.

## Batch API support

The `inference_geo` parameter is supported on the [Batch API](/docs/en/build-with-claude/batch-processing). Each request in a batch can specify its own `inference_geo` value.

## Migration from legacy opt-outs

If your organization previously opted out of global routing to keep inference in the US, your workspace has been automatically configured with `allowed_inference_geos: ["us"]` and `default_inference_geo: "us"`. No code changes are required. Your existing data residency requirements continue to be enforced through the new geo controls.

### What changed

The legacy opt-out was an organization-level setting that restricted all requests to US-based infrastructure. The new data residency controls replace this with two mechanisms:

- **Per-request control:** The `inference_geo` parameter lets you specify `"us"` or `"global"` on each API call, giving you request-level flexibility.
- **Workspace controls:** The `default_inference_geo` and `allowed_inference_geos` settings in the Console let you enforce geo policies across all keys in a workspace.

### What happened to your workspace

Your workspace was migrated automatically:

| Legacy setting                   | New equivalent                                                  |
|:---------------------------------|:----------------------------------------------------------------|
| Global routing opt-out (US only) | `allowed_inference_geos: ["us"]`, `default_inference_geo: "us"` |

All API requests using keys from your workspace continue to run on US-based infrastructure. No action is needed to maintain your current behavior.

### If you want to use global routing

If your data residency requirements have changed and you want to take advantage of global routing for better performance and availability, update your workspace's inference geo settings to include `"global"` in the allowed geos and set `default_inference_geo` to `"global"`. See [Workspace-level restrictions](#workspace-level-restrictions) for details.

### Pricing impact

Legacy models are unaffected by this migration. For current pricing on newer models, see [Pricing](#pricing).

## Current limitations

- **Shared rate limits:** Rate limits are shared across all geos.
- **Inference geo:** Only `"us"` and `"global"` are available.
- **Workspace geo:** Only `"us"` is currently available. Workspace geo can't be changed after workspace creation.

## Next steps



[Pricing](/docs/en/about-claude/pricing#data-residency-pricing)

View data residency pricing details.



[Workspaces](/docs/en/manage-claude/workspaces)

Learn about workspace configuration.



[Usage and Cost API](/docs/en/manage-claude/usage-cost-api)

Track usage and costs by data residency.
