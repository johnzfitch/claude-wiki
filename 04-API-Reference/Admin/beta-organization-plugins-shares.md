---
title: "Shares - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugins/shares"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-18T06:27:14Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins)

# Shares

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Plugin Shares](https://platform.claude.com/docs/en/api/http/beta/organization/plugins/shares/list)

GET/v1/organizations/plugins/{plugin_id}/shares

Requires `anthropic-beta: ``ce-plugins-2026-09-01`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

List the shares the owner of a member-owned Plugin has given — to every member of the organization, to an RBAC Group, or to one member — most recently granted first.

##### Models



BetaPluginShare object{ type: "plugin_share", granted_at, plugin_id, target }



One share the owner of a member-owned Plugin has given. Shares are read-only in this API and have no ID of their own; who gave a share is recorded on the Compliance API activity feed, not here.
