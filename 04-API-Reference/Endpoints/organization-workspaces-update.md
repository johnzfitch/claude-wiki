---
title: "Update Workspace - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/workspaces/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-02T06:26:53Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/workspaces/update).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/workspaces)

# Update Workspace

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/workspaces/{workspace_id}

Update Workspace

##### Path parameters

workspace_id: string



##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Body



data_residency: optional [DataResidencyUpdateConfig](https://platform.claude.com/docs/en/api/http/organization/workspaces#data_residency_update_config) { allowed_inference_geos, default_inference_geo } or null



Data residency configuration for the workspace.



allowed_inference_geos: optional array of [AllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/organization/workspaces#allowed_inference_geo) or "unrestricted" or null



Permitted inference geo values. Use 'unrestricted' to allow all geos, or a list of specific geos.

One of the following:



Geos = array of [AllowedInferenceGeo](https://platform.claude.com/docs/en/api/http/organization/workspaces#allowed_inference_geo)



One of the following:

"global"



"us"



"unrestricted"





default_inference_geo: optional "global" or "us" or null



Default inference geo applied when requests omit the parameter. Must be a member of `allowed_inference_geos` unless `allowed_inference_geos` is `"unrestricted"`.

One of the following:

"global"



"us"





display_color: optional string



Hex color code representing the Workspace in the Anthropic Console.

maxLength7

pattern^#\[0-9A-Fa-f\]{6}\$

external_key_id: optional string



ID of the customer-managed encryption key (CMEK) configuration to use for this Workspace. Setting this field requires CMEK to be enabled for your organization. When set, data stored for this Workspace is encrypted with the referenced key. Create key configurations with the External Keys API. On Claude Platform on AWS the value for an AWS KMS key is the key's ARN, and your organization's own key must be a single-Region key in the same AWS account and Region as the Workspace. On that platform the key is validated against this Workspace when it is attached, so a key-policy problem is reported as an error on this request. This field is write-once: once a key is attached to a Workspace it cannot be detached or replaced. To rotate key material, rotate the underlying key on your cloud KMS; the `external_key_id` stays the same.



name: optional string



Name of the Workspace.

minLength1

maxLength255

tags: optional map\[string\] or null



User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

user_profile_id: optional string



ID of a user profile to attach to the Workspace. Every inference request through the Workspace must then name this user profile; the API rejects a request that names none or a different one. Once set, it can't be replaced or removed (sending the same ID again changes nothing); only deleting the user profile clears it. The default Workspace can't have a user profile.

##### Returns



Workspace object{ type: "workspace", id, archived_at, 8 more }



Update Workspace

cURL



```python
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
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
