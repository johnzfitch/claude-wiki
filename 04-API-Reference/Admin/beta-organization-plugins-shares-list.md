---
title: "List Plugin Shares - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugins/shares/list"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-02T06:26:36Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins)
5.  [Shares](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares)

# List Plugin Shares

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/plugins/{plugin_id}/shares

List the shares the owner of a member-owned Plugin has given — to every member of the organization, to an RBAC Group, or to one member — most recently granted first.

Shares are read-only in this API: members give and withdraw them in claude.ai, and who gave a share is recorded on the Compliance API activity feed rather than on the share. An organization-owned Plugin has installation settings instead, so this path returns 404 for one.

**Accepted credentials:** an Admin API key with the `read:plugins` or `read:org_audit` scope, or a Compliance Access Key with the `read:compliance_org_data` scope.

Every request must include the beta header `anthropic-beta: ce-plugins-2026-09-01`. A request without it returns `404`, exactly as if the endpoint did not exist. The Plugins API is in beta and is available to Claude Enterprise organizations only. It is not available to Claude Platform (Claude Console) organizations, or to organizations with HIPAA readiness enabled.

##### Path parameters

plugin_id: string



ID of the Plugin (prefixed `plugin_`).

##### Query parameters



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `100`.

default20

minimum1

maximum100

organization_id: optional string



For a `read:org_audit` or `read:compliance_org_data` key created for all of a parent organization's linked organizations: a child organization of that parent to read instead of the organization the key was created in, given as the organization's UUID or its `org_`-prefixed ID. A value that is neither returns a 400; an organization that is not a child of the key's parent, or where the Plugins API is not available, returns a 404. Any other key may pass only its own organization's ID here; another organization returns a 404.



page: optional string



Optionally set to the `next_page` token from the previous response.

maxLength2048



target_type: optional "organization" or "organization_member" or "rbac_group"



Only shares with this kind of target: `organization` (every member), `rbac_group` (one RBAC Group), or `organization_member` (one member).

One of the following:

"organization"



"organization_member"



"rbac_group"



##### Headers



"anthropic-beta": optional array of [AnthropicBeta](../Endpoints/platform-claude-com-http-beta.md#anthropic_beta)



This endpoint is in beta: requests must send `ce-plugins-2026-09-01` in this header.

One of the following:

string



"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"cache-diagnosis-2026-04-07"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"ce-user-management-2026-07-13"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"



"ce-plugins-2026-09-01"



"spend-limit-reads-2026-09-26"



"telemetry-destinations-2026-08-11"



"webhooks-2026-10-07"



"message-threads-2026-08-12"



"analytics-usage-cost-2026-08-24"



"experimental-claude-tag-2026-10-21"



##### Returns



data: array of [BetaPluginShare](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares#beta_plugin_share) { type: "plugin_share", granted_at, plugin_id, target }





type: "plugin_share"



Always `plugin_share`.

defaultplugin_share



granted_at: string



When the share was given; a share whose role is later changed in claude.ai is re-granted and carries the time of that change.

formatdate-time

plugin_id: string



The Plugin's ID.



target: [BetaPluginTargetOrganization](https://platform.claude.com/docs/en/api/http/beta/organization/plugins#beta_plugin_target_organization) or [BetaPluginTargetRBACGroup](https://platform.claude.com/docs/en/api/http/beta/organization/plugins#beta_plugin_target_rbac_group) or [BetaPluginTargetOrganizationMember](https://platform.claude.com/docs/en/api/http/beta/organization/plugins#beta_plugin_target_organization_member)



Who the Plugin is shared with: `organization` (every member), `rbac_group` (one RBAC Group), or `organization_member` (one member).

One of the following:



BetaPluginTargetOrganization object{ type: "organization" }





type: "organization"



Every member of the organization.

defaultorganization



BetaPluginTargetRBACGroup object{ type: "rbac_group", rbac_group_id }





type: "rbac_group"



An RBAC Group.

defaultrbac_group

rbac_group_id: string



The RBAC Group's ID.



BetaPluginTargetOrganizationMember object{ type: "organization_member", user_id }





type: "organization_member"



One member of the organization.

defaultorganization_member

user_id: string



The member's User ID.

next_page: string or null



Token to provide in as `page` in the subsequent request to retrieve the next page of data.

List Plugin Shares

cURL



```python
curl https://api.anthropic.com/v1/organizations/plugins/$PLUGIN_ID/shares \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: ce-plugins-2026-09-01' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "granted_at": "2026-03-14T09:26:53.589793Z",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "target": {
        "type": "organization"
      },
      "type": "plugin_share"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "granted_at": "2026-03-14T09:26:53.589793Z",
      "plugin_id": "plugin_01JyHfbRkZvD1gW7oTqXc3Ne",
      "target": {
        "type": "organization"
      },
      "type": "plugin_share"
    }
  ],
  "next_page": "page_MjAyNi0wOS0xNlQxNDowNTowOVo"
