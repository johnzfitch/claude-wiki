---
title: "Add Federation Rule Workspace - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/federation/rules/workspaces/add"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:21Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/add).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Federation](https://platform.claude.com/docs/en/api/http/organization/federation)
4.  [Rules](https://platform.claude.com/docs/en/api/http/organization/federation/rules)
5.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/federation/rules/workspaces)

# Add Federation Rule Workspace

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Enable a federation rule for a workspace.

Idempotent; re-enabling returns the existing enablement. The rule and workspace must both belong to your organization. Membership of the rule's target service account in this workspace is not checked at enablement: token exchange into this workspace is rejected unless the target is a member (it is implicitly a member of the default workspace). Archived rules are rejected with 400. OAuth callers may only manage rules whose `oauth_scope` is `workspace:developer` or `workspace:inference`; other scopes require a Console session.

##### Path parameters

federation_rule_id: string



ID of the federation rule.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Body

workspace_id: string



Tagged ID of the workspace to enable this rule for.

##### Returns



FederationRuleWorkspace object{ type: "federation_rule_workspace", created_at, created_by_actor_id, 3 more }





type: "federation_rule_workspace"



defaultfederation_rule_workspace



created_at: string



When this workspace was enabled for the rule.

formatdate-time

created_by_actor_id: string or null



Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

federation_rule_id: string



Tagged ID of the federation rule.

workspace_id: string



Tagged ID of the workspace this rule is enabled for.

workspace_name: string or null



Workspace display name. Populated when listing; null in the enable response.

Add Federation Rule Workspace

cURL



```python
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{
          "workspace_id": "workspace_id"
        }'
```

Response 200



```python
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace",
  "workspace_id": "workspace_id",
  "workspace_name": "workspace_name"
}
```

##### Returns Examples

Response 200



```python
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace",
  "workspace_id": "workspace_id",
  "workspace_name": "workspace_name"
