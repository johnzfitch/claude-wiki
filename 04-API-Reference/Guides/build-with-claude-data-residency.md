---
title: "Data residency - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/data-residency"
category: "04-API-Reference/Guides"
fetched_at: "2026-09-27T06:27:09Z"
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


[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fdata-residency)





SearchCtrlK

Organization

[Admin API](../Other/manage-claude-admin-api.md)[User management](../Other/manage-claude-user-management.md)[Workspaces](../Other/manage-claude-workspaces.md)

Authentication

[Overview](../Other/manage-claude-authentication.md)[Create an Admin API key](../Other/manage-claude-admin-api-keys.md)[App Attest](../Other/manage-claude-app-attest.md)[Workload Identity Federation](../Other/manage-claude-workload-identity-federation.md)[Manage WIF via API](../Other/manage-claude-wif-admin-api.md)[WIF reference](../Other/manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](../Other/manage-claude-usage-cost-api.md)[Rate Limits API](../Other/manage-claude-rate-limits-api.md)[Analytics APIs](../Other/manage-claude-analytics-api.md)[Claude Code Analytics API](../Other/manage-claude-claude-code-analytics-api.md)[Spend Limits API](../Other/manage-claude-spend-limits-api.md)

Data & compliance

[Data residency](build-with-claude-data-residency.md)[API and data retention](../Other/manage-claude-api-and-data-retention.md)[Access Transparency](../Other/manage-claude-access-transparency.md)

[Encryption keys](../Other/manage-claude-cmek.md)

[Inference hooks](../Other/manage-claude-inference-hooks.md)

Compliance API

[Overview](../Other/manage-claude-compliance-api.md)[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)[Activity Feed](../Other/manage-claude-compliance-activity-feed.md)[Chats, files, and projects](../Other/manage-claude-compliance-content-data.md)[Session transcripts](../Other/manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](../Other/manage-claude-compliance-org-data.md)[Design your integration](../Other/manage-claude-compliance-integration-patterns.md)[Errors](../Other/manage-claude-compliance-errors.md)[FAQ](../Other/manage-claude-compliance-faq.md)

[Console](../Other/usage-limits.md)

[Admin](../Other/manage-claude-admin-api.md)Data & compliance

# Data residency

Copy page



Manage where model inference runs and where data is stored with geographic controls.

Copy page



Data residency controls let you manage where your data is processed and stored. Two independent settings govern this:

- **Inference geo:** Controls where model inference runs, on a per-request basis. Set through the `inference_geo` API parameter or as a workspace default.
- **Workspace geo:** Controls where data is stored at rest and where endpoint processing (such as image transcoding and code execution) happens. Configured at the workspace level in the [Claude Console](../Other/usage-limits.md).



[Claude Managed Agents](../Other/managed-agents-overview.md) supports geographic pinning at the agent level: `inference_geo` on an [agent's model configuration](../Other/managed-agents-agent-setup.md#pin-the-inference-geo) pins the geography that serves model requests for sessions running that agent, with [per-session overrides](../Other/managed-agents-sessions.md#pin-the-inference-geo-for-a-session) at session create. Agents without a pin follow the workspace's default inference geo on each request. Managed Agents also respects the Workspace geo configured in Console, and with [self-hosted sandboxes](../Other/managed-agents-self-hosted-sandboxes.md), tool execution and the sandbox filesystem stay on infrastructure you control; the contents of attached [memory stores](../Other/managed-agents-self-hosted-sandboxes.md#use-memory-stores) remain stored by Anthropic and are copied to your sandbox for the session.

## Inference geo



To learn how zero data retention (ZDR) applies to this feature, see [API and data retention](../Other/manage-claude-api-and-data-retention.md).

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

The `inference_geo` parameter is available on the Claude API (first-party) and [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md). On Amazon Bedrock and Google Cloud, the inference region is determined by the endpoint URL or inference profile, so `inference_geo` is not applicable. On [Claude in Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md), `inference_geo` is likewise not applicable: deployments hosted on Azure can instead use the US Data Zone Standard deployment type, which keeps inference within the United States. The `inference_geo` parameter is also not available through the [OpenAI SDK compatibility endpoint](../Other/cli-sdks-libraries-libraries-openai-sdk.md).

### Workspace-level restrictions

Workspace settings also support restricting which inference geos are available:

- **`allowed_inference_geos`:** Restricts which geos a workspace can use. If a request specifies an `inference_geo` not in this list, the API returns an error.
- **`default_inference_geo`:** Sets the fallback geo when `inference_geo` is omitted from a request. Individual requests can override this by setting `inference_geo` explicitly.

These settings can be configured through the Console or the [Admin API](../Other/manage-claude-admin-api.md) under the `data_residency` field.

## Workspace geo

Workspace geo is set when you create a workspace and can't be changed afterward. Currently, `"us"` is the only available workspace geo.

To set workspace geo, create a new workspace in the [Console](../Other/usage-limits.md):

1.  Go to **Settings** \> **Workspaces**.
2.  Create a new workspace.
3.  Select the workspace geo.



**Claude Platform on AWS:** Workspace geo is not configurable. Claude Managed Agents sessions on this platform run with an effective Workspace geo of `"us"`, which is currently the only available workspace geo. See [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md) for data residency considerations specific to that platform.

## Pricing

Data residency pricing varies by model generation:

- **Claude 4.6 and later models:** US-only inference (`inference_geo: "us"`) is priced at 1.1x the standard rate across all token pricing categories (input tokens, output tokens, cache writes, and cache reads).
- **Global routing** (`inference_geo: "global"`): Standard pricing applies.
- **Older models:** Don't support `inference_geo` (see [Model availability](#model-availability)); standard pricing applies. Requests that include the parameter return a 400 error.

This pricing applies to the Claude API (first-party) and Claude Platform on AWS. On Claude in Microsoft Foundry, the same 1.1x multiplier applies to deployments hosted on Azure that use the US Data Zone Standard deployment type. Partner-operated platforms (Bedrock and Google Cloud) have their own regional pricing. See [Data residency pricing](../../17-Billing-Plans/about-claude-pricing.md#data-residency-pricing) for details.

The same multiplier applies to [Claude Managed Agents](../Other/managed-agents-overview.md): when an agent's [model configuration](../Other/managed-agents-agent-setup.md) pins `inference_geo` to `"us"`, model requests in sessions running that agent are priced at 1.1x the standard rate.



If you have a [Priority Tier](../Endpoints/service-tiers.md) commitment, the 1.1x multiplier for US-only inference also affects how tokens are counted against your Priority Tier capacity. Each token consumed with `inference_geo: "us"` draws down 1.1 tokens from your committed TPM, consistent with how other pricing multipliers (such as prompt caching) affect burndown rates.

## Batch API support

The `inference_geo` parameter is supported on the [Batch API](build-with-claude-batch-processing.md). Each request in a batch can specify its own `inference_geo` value.

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

[Pricing](../../17-Billing-Plans/about-claude-pricing.md#data-residency-pricing)

View data residency pricing details.



[Workspaces](../Other/manage-claude-workspaces.md)

Learn about workspace configuration.



[Usage and Cost API](../Other/manage-claude-usage-cost-api.md)

Track usage and costs by data residency.
