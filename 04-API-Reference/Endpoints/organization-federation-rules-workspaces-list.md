---
title: "List Federation Rule Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/federation/rules/workspaces/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-02T06:26:42Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/federation/rules/workspaces/list).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Federation](https://platform.claude.com/docs/en/api/http/organization/federation)
4.  [Rules](https://platform.claude.com/docs/en/api/http/organization/federation/rules)
5.  [Workspaces](https://platform.claude.com/docs/en/api/http/organization/federation/rules/workspaces)

# List Federation Rule Workspaces

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/federation_rules/{federation_rule_id}/workspaces

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and `page` parameters are accepted but have no effect, and `next_page` is always `null`. Returns explicit per-workspace enablements only; for rules with `applies_to_all_workspaces` or a legacy single `workspace_id`, check those fields on the rule itself.

##### Path parameters

federation_rule_id: string



ID of the federation rule.

##### Query parameters



limit: optional number



Number of results per page.

default20

minimum1

maximum100

page: optional string



Opaque cursor from a previous response's `next_page`.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



data: array of [FederationRuleWorkspace](https://platform.claude.com/docs/en/api/http/organization/federation/rules#federation_rule_workspace) { type: "federation_rule_workspace", created_at, created_by_actor_id, 3 more }

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

next_page: string or null



Opaque cursor for the next page; null when there are no more results.

List Federation Rule Workspaces

cURL



```python
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
