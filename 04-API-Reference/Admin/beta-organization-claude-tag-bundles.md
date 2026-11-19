---
title: "Bundles - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/claude_tag/bundles"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-16T06:24:38Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Claude Tag](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag)

# Bundles

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Bundles](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/list)

GET/v1/organizations/claude_tag/bundles

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

List the organization's Bundles, newest first by `created_at`. A Bundle that Claude Tag manages for itself is not listed.

##### [Get Bundle](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/retrieve)

GET/v1/organizations/claude_tag/bundles/{bundle_id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Get one Bundle. What the Bundle grants (connectors, repositories and credentials) is never returned.

##### Models



BetaClaudeTagBundle object{ type: "bundle", id, created_at, 3 more }



A named set of access that Claude can use in a Slack channel or a Slack workspace: connectors, repositories and credentials. Created and edited in claude.ai.

type: "bundle"



id: string



The Bundle's identifier. Starts with `capp_`.



created_at: string



Time the Bundle was created.

formatdate-time

description: string or null



What the Bundle is for. Null when it has none. Read-only.

display_name: string



The Bundle's name. Always set. Read-only.



updated_at: string



Time of the last change to the Bundle.

formatdate-time

#### Bundles[Targets](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets)

##### [List Bundle Targets](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/list)

GET/v1/organizations/claude_tag/bundles/{bundle_id}/targets

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

List the Slack channels and Slack workspaces a Bundle is attached to, newest first by `created_at`. Only channels and workspaces the organization owns are listed; a Bundle that is attached to anything else has no Bundle Target for it.

##### [Attach Bundle](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/create)

POST/v1/organizations/claude_tag/bundles/{bundle_id}/targets

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Attach a Bundle to a Slack channel or a Slack workspace. A Bundle attached to a workspace can be used in the workspace and in every channel in it. Attaching a Bundle to a channel or workspace it is already attached to returns the existing Bundle Target. The channel or workspace must be set up: attaching never sets a channel up. A group direct message takes no Bundle and returns 400.

##### [Get Bundle Target](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/retrieve)

GET/v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Get one Bundle Target. Returns 404 when `target_id` is the identifier of another Bundle's Bundle Target, or the Bundle Target was detached.

##### [Detach Bundle](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/delete)

DELETE/v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Detach a Bundle from a Slack channel or a Slack workspace. A repeated detach returns 404.
