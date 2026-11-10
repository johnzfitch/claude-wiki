---
title: "Installation Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugins/installation_settings"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-02T06:26:54Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins)

# Installation Settings

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Plugin Installation Settings](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/list)

GET/v1/organizations/plugins/{plugin_id}/installation_settings

List an organization-owned Plugin's installation settings, which say which members it is for, most recently created first.

##### [Set Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/set)

POST/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Set or change an organization-owned Plugin's installation setting for the whole organization or for one RBAC Group.

##### [Remove Plugin Installation Setting](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/installation_settings/remove)

DELETE/v1/organizations/plugins/{plugin_id}/installation_settings/{target}

Remove an organization-owned Plugin's own installation setting for the whole organization or for one RBAC Group.

##### Models



BetaDeletedPluginInstallationSetting object{ type: "plugin_installation_setting_deleted", plugin_id, target }



Confirmation that one target's installation setting was removed, naming the Plugin and the target in place of an ID.



BetaPluginInstallationSetting object{ type: "plugin_installation_setting", created_at, installation_preference, 3 more }



The installation setting an organization-owned Plugin holds for one target. It has no ID of its own: it is addressed by the Plugin's ID and the target.
