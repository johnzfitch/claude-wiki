---
title: "Remove Federation Rule Workspace - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/federation/rules/workspaces/remove"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:32Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/remove).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Federation](https://platform.claude.com/docs/en/api/http/organization/federation)
4.  [Rules](https://platform.claude.com/docs/en/api/http/organization/federation/rules)
5.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/federation/rules/workspaces)

# Remove Federation Rule Workspace

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth callers may only manage rules whose `oauth_scope` is `workspace:developer` or `workspace:inference`; other scopes require a Console session.

##### Path parameters

federation_rule_id: string



ID of the federation rule.

workspace_id: string



ID of the workspace to disable for.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



type: "federation_rule_workspace_deleted"



defaultfederation_rule_workspace_deleted

federation_rule_id: string



Tagged ID of the federation rule.

workspace_id: string



Tagged ID of the workspace named in the delete request. Removal is idempotent.

Remove Federation Rule Workspace

cURL



```python
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces/$WORKSPACE_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace_deleted",
  "workspace_id": "workspace_id"
}
```

##### Returns Examples

Response 200



```python
{
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace_deleted",
  "workspace_id": "workspace_id"
