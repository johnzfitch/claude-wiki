---
title: "Update Service Account - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/service_accounts/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:26Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/update).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Service Accounts](https://platform.claude.com/docs/en/api/http/organization/service_accounts)

# Update Service Account

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/service_accounts/{service_account_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be changed. Archived service accounts cannot be updated; this returns 400. Setting `organization_role` to `admin` (even when unchanged) requires an interactive credential (a user OAuth token or a Console session).

##### Path parameters

service_account_id: string



ID of the service account to update.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Body



description: optional string or null



Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

maxLength2000



organization_role: optional "admin" or "developer" or null



Replaces the org-level role. Omit or send `null` to leave unchanged.

One of the following:

"admin"



"developer"



##### Returns



ServiceAccount object{ type: "service_account", id, archived_at, 8 more }



Named non-human identity within the caller's organization.

A service account is a pure identity: name + org. Authorization lives on whatever references it (federation rules).

Update Service Account

cURL



```python
curl https://api.anthropic.com/v1/organizations/service_accounts/$SERVICE_ACCOUNT_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
```

Response 200



```python
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
