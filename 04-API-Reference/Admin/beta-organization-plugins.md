---
title: "Plugins - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugins"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-18T06:27:12Z"
tags: ["api", "plugins"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Plugins

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/create)

POST/v1/organizations/plugins

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Create an organization-owned Plugin and its first version by uploading the version's files.

##### [Get Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/retrieve)

GET/v1/organizations/plugins/{plugin_id}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Retrieve a Plugin by ID.

##### [Update Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/update)

POST/v1/organizations/plugins/{plugin_id}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Change which stored version of an organization-owned Plugin is served to members, for example to roll back to an earlier one. This pins the served version: later uploads are stored but no longer change what is served, and pinning cannot currently be undone, here or in claude.ai.

##### [List Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/list)

GET/v1/organizations/plugins

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

List the Plugins created under the organization, newest first: those in the organization's own plugin marketplaces and those in members' personal plugin marketplaces.

##### [Delete Plugin](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/delete)

DELETE/v1/organizations/plugins/{plugin_id}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Permanently delete a Plugin and every version it holds, exactly as when an administrator deletes it in claude.ai. The Plugin may belong to the organization or to a member, including a member who has since left the organization. Do not delete a Plugin only because your pipeline did not create it: a member or an administrator might have added it in claude.ai.

##### Models



BetaDeletedPlugin object{ type: "plugin_deleted", id }





type: "plugin_deleted"



Always `plugin_deleted`.

defaultplugin_deleted

id: string



The deleted Plugin's ID.



BetaPlugin object{ type: "plugin", id, components, 16 more }





BetaPluginAPIActor object{ type: "api_actor", api_key_id }





type: "api_actor"



An Admin API key, in the same form the Compliance API activity feed uses for it.

defaultapi_actor

api_key_id: string



The key's ID.



BetaPluginComponent object{ type, description, name }





type: "agent" or "cli" or "command" or 3 more



The kind of component.

One of the following:

"agent"



"cli"



"command"



"hook"



"mcp_server"



"skill"



description: string or null



What the component declares about itself; always null for MCP servers, hooks, and CLIs.

name: string



The component's name: a skill's, command's or agent's name, an MCP server's key in the manifest, the event a hook runs on, or a CLI's executable.



BetaPluginContentScan object{ assessment, reason, status }





assessment: "fail" or "pass" or "unknown" or "warn" or null



The scan's verdict; set only when `status` is `completed`. A `warn` can mean a `fail` that was allowed in claude.ai.

One of the following:

"fail"



"pass"



"unknown"



"warn"



reason: string or null



The primary mechanism behind a `warn` or `fail`, such as `credential-exposure` or `guardrail-tampering`; a mechanism this API does not yet name reads as `other`. Read `status` first: on an `errored` scan it is not a finding but why there is no verdict: `scan-invalid-archive`, the scan refused the version's archive, or could not process it, before checking what its files say, and running it again will not help, so change the files and store a new version; `scan-did-not-finish`, the scan did not finish or its result is no longer available, so retry the scan in claude.ai if it offers a retry; `scan-unavailable`, the scan could not run or its result cannot be read right now, so read the version again later, then retry the scan in claude.ai if it offers a retry. If these steps do not help, contact support. Null on a `pass`, while a scan runs, and when no mechanism is reported for the verdict. On an errored scan, null means that a compliance configuration ruled out the scan.



status: "completed" or "errored" or "processing"



`processing` while a scan runs, `completed` when it ran to completion, `errored` when it could not run. Once a scan of the version has completed, `content_scan` describes the newest completed scan, even while a later scan runs. While the scan outcome cannot be read, `status` is `errored` instead.

One of the following:

"completed"



"errored"



"processing"





BetaPluginNameTakenErrorDetails object{ error_code, plugin_id }



The marketplace already holds this name. `plugin_id` is the Plugin that holds it, and can be absent.

error_code: "plugin_name_taken"



plugin_id: optional string or null





BetaPluginOwnerOrganization object{ type: "organization" }





type: "organization"



The Plugin lives in a plugin marketplace the organization owns.

defaultorganization



BetaPluginOwnerUser object{ type: "user", user_id }





type: "user"



The Plugin lives in one member's personal plugin marketplace.

defaultuser

user_id: string



The member's User ID.



BetaPluginTargetOrganization object{ type: "organization" }





type: "organization"



Every member of the organization.

defaultorganization

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

BetaPluginUserActor object{ type: "user_actor", email_address, user_id }





type: "user_actor"



A member of the organization.

defaultuser_actor

email_address: string or null



The member's email address; may be null, for example when they are no longer a member of the organization.

user_id: string



The member's User ID.



BetaRegistrationPendingErrorDetails object{ error_code, plugin_id, plugin_version_id }



The Plugin version was stored but is not yet usable in claude.ai. `plugin_id` and `plugin_version_id` identify what was stored.

error_code: "registration_pending"



plugin_id: string



plugin_version_id: string





BetaScanFailedErrorDetails object{ error_code, plugin_version_id }



The version in `plugin_version_id` did not pass its content scan, so it cannot be served.

error_code: "scan_failed"



plugin_version_id: string





BetaScanPendingErrorDetails object{ error_code, plugin_version_id }



The content scan of the version in `plugin_version_id` is still running. Retry once the scan finishes.

error_code: "scan_pending"



plugin_version_id: string





BetaSkillNameTakenErrorDetails object{ error_code, skill_name }



One of the Plugin's skills has the name of an organization skill. `skill_name` is that name.

error_code: "skill_name_taken"



skill_name: string



#### Plugins[Versions](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions)

##### [Create Plugin Version](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/create)

POST/v1/organizations/plugins/{plugin_id}/versions

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Add a version to an organization-owned Plugin by uploading the new version's files; it becomes the version served to members unless the Plugin's served version has been pinned.

##### [List Plugin Versions](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/list)

GET/v1/organizations/plugins/{plugin_id}/versions

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

List a Plugin's versions, newest first.

##### [Get Plugin Version](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/retrieve)

GET/v1/organizations/plugins/{plugin_id}/versions/{version}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Retrieve one version of a Plugin by its ID, or the Plugin's newest version.

##### [Download Plugin Version Archive](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/versions/download)

GET/v1/organizations/plugins/{plugin_id}/versions/{version}/content

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Download one version's `.zip` archive, exactly as stored. Each download of a Plugin from a member's personal plugin marketplace is recorded on the Compliance API activity feed.

#### Plugins[Installation Settings](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings)

##### [List Plugin Installation Settings](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/list)

GET/v1/organizations/plugins/{plugin_id}/installation_settings

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

List an organization-owned Plugin's installation settings, which say which members it is for, most recently created first.

##### [Set Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/set)

POST/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Set or change an organization-owned Plugin's installation setting for the whole organization or for one RBAC Group.

##### [Remove Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/remove)

DELETE/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Remove an organization-owned Plugin's own installation setting for the whole organization or for one RBAC Group.

#### Plugins[Shares](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares)

##### [List Plugin Shares](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares/list)

GET/v1/organizations/plugins/{plugin_id}/shares

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

List the shares the owner of a member-owned Plugin has given — to every member of the organization, to an RBAC Group, or to one member — most recently granted first.
