---
title: "Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugins/versions"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-18T06:27:14Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Plugins](https://platform.claude.com/docs/en/api/http/beta/organization/plugins)

# Versions

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

##### Models



BetaPluginVersion object{ type: "plugin_version", id, components, 9 more }
