---
title: "Data residency - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/data-residency"
category: "04-API-Reference/Other"
fetched_at: "2026-11-13T06:36:39Z"
tags: ["api"]
---

# Data residency

Copy page



Manage where model inference runs and where data is stored with geographic controls.

Copy page



Data residency

[Models](#feature-availability)  
- All latest models
- Limited support for other models; see details

[APIs](#feature-availability)  
- Messages API
- Managed Agents

[Cloud platforms](#feature-availability)  
- Claude API
- Claude Platform on AWS
- Claude Models on Google CloudAnthropic managed

[Data handling](#feature-data-handling)  
ZDRZDR eligibleHIPAAHIPAA eligible

Usage differs by product

Messages API

Set `inference_geo` on each request, or set a default for the workspace.

Managed Agents

Pin `inference_geo` in the agent’s model configuration; override it at session creation.

Data residency controls let you manage where your data is processed and stored. Two independent settings govern this:

- **Inference geo:** Controls where model inference runs, on a per-request basis. Set through the `inference_geo` API parameter or as a workspace default.
- **Workspace geo:** Controls where data is stored at rest and where endpoint processing (such as image transcoding and code execution) occurs. Configured at the workspace level in the [Claude Console](playground.md).



[Claude Managed Agents](managed-agents-overview.md) supports geographic pinning at the agent level: `inference_geo` on an [agent’s model configuration](managed-agents-agent-setup.md#pin-the-inference-geo) pins the geography that serves model requests for sessions running that agent, with [per-session overrides](managed-agents-sessions.md#pin-the-inference-geo-for-a-session) at session create. Agents without a pin follow the workspace’s default inference geo on each request. Managed Agents also respects the Workspace geo configured in Console, and with [self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md), tool execution and the sandbox filesystem stay on infrastructure you control; the contents of attached [memory stores](managed-agents-self-hosted-sandboxes-memory.md) remain stored by Anthropic and are copied to your sandbox for the session.

## Inference geo

The `inference_geo` parameter controls where model inference runs for a specific API request. Add it to any `POST /v1/messages` call.

| Value | Description |
|:---|:---|
| `"global"` | Default. Inference may run in any available geography for optimal performance and availability. |
| `"us"` | Inference runs only in US-based infrastructure. |

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

Python

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

The `inference_geo` parameter is supported on Claude 4.6 and later models. Requests with `inference_geo` on Claude Opus 4.5, Claude Sonnet 4.5 (deprecated), Claude Haiku 4.5, or earlier models return a 400 error.



The `inference_geo` parameter is available on the Claude API (first-party), [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md), and [Claude Models on Google Cloud (Anthropic managed)](../Guides/build-with-claude-claude-models-on-google-cloud-anthropic-managed.md). On Claude Models on Google Cloud (Google managed) and Amazon Bedrock, the inference region is determined by the endpoint URL or inference profile, so `inference_geo` is not applicable. On [Claude in Microsoft Foundry](../Guides/build-with-claude-claude-in-microsoft-foundry.md), `inference_geo` is likewise not applicable: deployments hosted on Azure can instead use the US Data Zone Standard deployment type, which keeps inference within the United States. The `inference_geo` parameter is also not available through the [OpenAI SDK compatibility endpoint](cli-sdks-libraries-libraries-openai-sdk.md).

### Workspace-level restrictions

Workspace settings also support restricting which inference geos are available:

- **`allowed_inference_geos`:** Restricts which geos a workspace can use. If a request specifies an `inference_geo` not in this list, the API returns an error.
- **`default_inference_geo`:** Sets the fallback geo when `inference_geo` is omitted from a request. Individual requests can override this by setting `inference_geo` explicitly.

These settings can be configured through the Console or the [Admin API](manage-claude-admin-api.md) under the `data_residency` field.



**Claude Models on Google Cloud (Anthropic managed):** Every workspace allows all inference geos and uses `"global"` as its default inference geo. The Claude Console shows both settings as read-only. For US-only inference, set `inference_geo: "us"` on each request.

## Workspace geo

Workspace geo is set when you create a workspace and can’t be changed afterward. Currently, `"us"` is the only available workspace geo.

To set workspace geo, create a new workspace in the [Console](playground.md):

1.  Go to [Workspaces in the Claude Console](playground.md) (`platform.claude.com/settings/workspaces`).
2.  Click **Create workspace** to open the [Create workspace](https://platform.claude.com/settings/workspaces/new) page (`platform.claude.com/settings/workspaces/new`) in the Console.
3.  Enter a name, confirm the value in the **Workspace geo** field, and click **Create workspace**.



**Claude Platform on AWS:** Workspace geo is not configurable. Claude Managed Agents sessions on this platform run with an effective Workspace geo of `"us"`, which is currently the only available workspace geo. See [Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md) for data residency considerations specific to that platform.



**Claude Models on Google Cloud (Anthropic managed):** Workspace geo is not configurable. Every workspace uses `"us"` as its workspace geo, and the **Workspace geo** field doesn’t appear in the Claude Console.

## Pricing

Data residency pricing varies by model generation:

- **Claude 4.6 and later models:** US-only inference (`inference_geo: "us"`) is priced at 1.1x the standard rate across all token pricing categories (input tokens, output tokens, cache writes, and cache reads). On Claude Haiku 5.5, the multiplier also applies to the higher prices for prompts over 100,000 tokens (see [Long context pricing](../../17-Billing-Plans/about-claude-pricing.md#long-context-pricing)).
- **Global routing (`inference_geo: "global"`):** Standard pricing applies.
- **Older models:** Don’t support `inference_geo` (see [Model availability](#model-availability)). Standard pricing applies. Requests that include the parameter return a 400 error.

This pricing applies to the Claude API (first-party), Claude Platform on AWS, and Claude Models on Google Cloud (Anthropic managed). On Claude in Microsoft Foundry, the same 1.1x multiplier applies to deployments hosted on Azure that use the US Data Zone Standard deployment type. Partner-operated platforms, Claude Models on Google Cloud (Google managed) and Bedrock, have their own regional pricing. See [Data residency pricing](../../17-Billing-Plans/about-claude-pricing.md#data-residency-pricing) for details.

The same multiplier applies to [Claude Managed Agents](managed-agents-overview.md): when an agent’s [model configuration](managed-agents-agent-setup.md) pins `inference_geo` to `"us"`, model requests in sessions running that agent are priced at 1.1x the standard rate.



If you have a [Priority Tier](../Endpoints/service-tiers.md) commitment, the 1.1x multiplier for US-only inference also affects how tokens are counted against your Priority Tier capacity. Each token consumed with `inference_geo: "us"` draws down 1.1 tokens from your committed TPM, consistent with how other pricing multipliers (such as prompt caching) affect burndown rates.

## Batch API support

The `inference_geo` parameter is supported on the [Batch API](../Guides/build-with-claude-batch-processing.md). Each request in a batch can specify its own `inference_geo` value.

## Migration from legacy opt-outs

If your organization previously opted out of global routing to keep inference in the US, your workspace has been automatically configured with `allowed_inference_geos: ["us"]` and `default_inference_geo: "us"`. No code changes are needed. Your existing data residency requirements continue to be enforced through the new geo controls.

### What changed

The legacy opt-out was an organization-level setting that restricted all requests to US-based infrastructure. The new data residency controls replace this with two mechanisms:

- **Per-request control:** The `inference_geo` parameter lets you specify `"us"` or `"global"` on each API call, giving you request-level flexibility.
- **Workspace controls:** The `default_inference_geo` and `allowed_inference_geos` settings in the Console let you enforce geo policies across all keys in a workspace.

### What happened to your workspace

Your workspace was migrated automatically:

| Legacy setting | New equivalent |
|:---|:---|
| Global routing opt-out (US only) | `allowed_inference_geos: ["us"]`, `default_inference_geo: "us"` |

All API requests using keys from your workspace continue to run on US-based infrastructure. No action is needed to maintain your current behavior.

### If you want to use global routing

If your data residency requirements have changed and you want to take advantage of global routing for better performance and availability, update your workspace’s inference geo settings to include `"global"` in the allowed geos and set `default_inference_geo` to `"global"`. See [Workspace-level restrictions](#workspace-level-restrictions) for details.

### Pricing impact

Legacy models are unaffected by this migration. For current pricing on newer models, see [Pricing](#pricing).

## Current limitations

- **Shared rate limits:** Rate limits are shared across all geos.
- **Inference geo:** Only `"us"` and `"global"` are available.
- **Workspace geo:** Only `"us"` is currently available. Workspace geo can’t be changed after workspace creation.

## Next steps



[Data residency pricing](../../17-Billing-Plans/about-claude-pricing.md#data-residency-pricing)

View data residency pricing details.



[Workspaces](manage-claude-workspaces.md)

Learn about workspace configuration.



[Usage and Cost Analytics API](manage-claude-usage-cost-analytics-api.md)

Track usage and costs by inference geo.

## Availability

Data residency

Cloud platform

Cloud platform: Claude API

Claude API

APIs  
- Messages API
- Managed Agents

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Mythos 5.2, Mythos 5.1, Mythos 5, Mythos Preview
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5

Claude Platform on AWS

APIs  
- Messages API

Workspace geo is not configurable.

- Managed Agents

Workspace geo is not configurable; Managed Agents sessions there run with workspace geo “us”.

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5

Claude Models on Google Cloud (Anthropic managed)

API  
- Messages API

Models  
- Claude Fable 5.2, Fable 5.1, Fable 5
- Claude Mythos 5.2
- Claude Opus 5.5, Opus 5, Opus 4.8, Opus 4.7, Opus 4.6
- Claude Sonnet 5.5, Sonnet 5, Sonnet 4.6
- Claude Haiku 5.5

Note  
Workspace geo is not configurable.

### Data handling

[Data handling overview](manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/messages` with `inference_geo`

Zero data retentionEligible

Excludes [Covered Models](manage-claude-api-and-data-retention.md#model-specific-data-retention-requirements)

HIPAAEligible
