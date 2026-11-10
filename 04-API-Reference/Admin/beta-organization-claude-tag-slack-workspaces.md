---
title: "Slack Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/claude_tag/slack_workspaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-08T06:25:17Z"
tags: ["api", "slack"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Claude Tag](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag)

# Slack Workspaces

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Slack Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_workspaces/list)

GET/v1/organizations/claude_tag/slack_workspaces

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

List the set-up Slack workspaces the organization owns, newest first by `created_at`. Pass `slack_workspace_id` to look one workspace up by its Slack identifier: `data` then holds that workspace, or is empty when it is not set up. A workspace of a Slack Enterprise Grid the organization has connected returns 404 until it is set up. With `include_inherited=true` each workspace's `settings` holds what applies in it, and the request fails with 503 rather than resolve against a settings level that could not be read. A `page` cursor resumes only a request with the same `include_inherited`.

##### [Get Slack Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_workspaces/retrieve)

GET/v1/organizations/claude_tag/slack_workspaces/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Get one Slack workspace and its settings. By default `settings` holds what the workspace itself stores: a setting that is null there is not set on the workspace and is inherited. With `include_inherited=true`, `settings` holds what applies in the workspace once the organization's Slack defaults are taken into account, and the request fails with 503 rather than resolve against a settings level that could not be read. Either way `sources` names the settings level each value comes from.

##### [Update Slack Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_workspaces/update)

POST/v1/organizations/claude_tag/slack_workspaces/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Change the settings a Slack workspace stores. The update is partial: a setting left out is unchanged, and a setting sent as null is cleared, so the workspace inherits it. If any value is refused, no setting in the request is stored.

##### Models



BetaClaudeTagSlackWorkspace object{ type: "slack_workspace", id, created_at, 4 more }



A Slack workspace the organization has connected, itself or through its Slack Enterprise Grid, with the settings it stores or, with `include_inherited`, the settings that apply in it.
