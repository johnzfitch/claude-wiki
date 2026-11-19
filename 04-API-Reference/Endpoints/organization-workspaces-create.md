---
title: "Create Workspace - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/workspaces/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:28Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/create).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces)

# Create Workspace

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/workspaces

Create Workspace

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Body



name: string



Name of the Workspace.

minLength1

maxLength255



data_residency: optional [DataResidencyCreateConfig](https://platform.claude.com/docs/en/api/http/organization/workspaces#data_residency_create_config) { allowed_inference_geos, default_inference_geo, workspace_geo } or null



Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.



display_color: optional string or null



Hex color code representing the Workspace in the Anthropic Console.

maxLength7

pattern^#\[0-9A-Fa-f\]{6}\$

external_key_id: optional string or null



ID of the customer-managed encryption key (CMEK) configuration to use for this Workspace. Setting this field requires CMEK to be enabled for your organization. When set, data stored for this Workspace is encrypted with the referenced key. Create key configurations with the External Keys API. On Claude Platform on AWS the value for an AWS KMS key is the key's ARN, and your organization's own key must be a single-Region key in the same AWS account and Region as the Workspace. On that platform the key is validated against this Workspace when it is attached, so a key-policy problem is reported as an error on this request. This field is write-once: once a key is attached to a Workspace it cannot be detached or replaced. To rotate key material, rotate the underlying key on your cloud KMS; the `external_key_id` stays the same.

tags: optional map\[string\] or null



User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

user_profile_id: optional string or null



ID of a user profile to attach to the Workspace. Every inference request through the Workspace must then name this user profile; the API rejects a request that names none or a different one. The user profile can't be replaced or removed later; only deleting the user profile clears it.

##### Returns



Workspace object{ type: "workspace", id, archived_at, 8 more }



Create Workspace

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "name": "Workspace Name",
          "display_color": "#6C5BB9",
          "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
          "tags": {
            "env": "prod",
            "team": "platform"
          },
          "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
        }'
```

Response 200



```python
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "global",
    "workspace_geo": "us"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "global",
    "workspace_geo": "us"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace",
  "user_profile_id": "uprof_01SDCCSbTxrXDpWc1phhtcfK"
