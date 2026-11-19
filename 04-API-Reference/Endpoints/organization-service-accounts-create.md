---
title: "Create Service Account - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/service_accounts/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:23Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/service_accounts/create).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Service Accounts](https://platform.claude.com/docs/en/api/http/organization/service_accounts)

# Create Service Account

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/service_accounts

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Create a service account.

A service account is a named workload identity that federation rules target. `organization_role` is `developer` (default) or `admin`; a rule may only be created or retargeted to grant `org:admin` scope when the target's `organization_role` is `admin`. Creating an `admin`-role service account requires an interactive credential (a user OAuth token or a Console session) — a workload may only create `developer`-role service accounts.

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

Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

minLength1

maxLength255



description: optional string or null



Optional free-text description.

maxLength2000



organization_role: optional "admin" or "developer"



Org-level role. Defaults to `developer`.

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

Create Service Account

cURL



```python
curl https://api.anthropic.com/v1/organizations/service_accounts \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "name": "ci-deploy-bot"
        }'
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
