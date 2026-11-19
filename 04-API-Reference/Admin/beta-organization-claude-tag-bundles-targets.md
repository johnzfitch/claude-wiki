---
title: "Targets - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/claude_tag/bundles/targets"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-16T06:25:53Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Claude Tag](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag)
5.  [Bundles](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles)

# Targets

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

##### Models



BetaClaudeTagBundleTarget = [BetaClaudeTagSlackChannelBundleTarget](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets#beta_claude_tag_slack_channel_bundle_target) or [BetaClaudeTagSlackWorkspaceBundleTarget](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets#beta_claude_tag_slack_workspace_bundle_target)



One Bundle attached to one Slack channel or one Slack workspace. More types of target can be added.

One of the following:



BetaClaudeTagBundleTargetCreate = [BetaClaudeTagSlackChannelBundleTargetCreate](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets#beta_claude_tag_slack_channel_bundle_target_create) or [BetaClaudeTagSlackWorkspaceBundleTargetCreate](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets#beta_claude_tag_slack_workspace_bundle_target_create)



One of the following:



BetaClaudeTagSlackChannelBundleTargetCreate object{ type: "slack_channel", slack_channel_id }



Attach the Bundle to a Slack channel.

type: "slack_channel"





slack_channel_id: string



The identifier of the Slack channel to attach the Bundle to, starting with `slch_`. It is the channel object's `id`, not Slack's `channel_id`.

minLength8

maxLength64



BetaClaudeTagSlackWorkspaceBundleTargetCreate object{ type: "slack_workspace", slack_workspace_id }



Attach the Bundle to a Slack workspace.

type: "slack_workspace"





slack_workspace_id: string



The identifier of the Slack workspace to attach the Bundle to, starting with `slws_`.

minLength8

maxLength64



BetaClaudeTagDeletedBundleTarget object{ type: "bundle_target_deleted", id }



Confirms that a Bundle was detached.

type: "bundle_target_deleted"



id: string



The identifier the Bundle Target had.



BetaClaudeTagSlackChannelBundleTarget object{ type: "slack_channel", id, created_at, slack_channel_id }



One Bundle attached to one Slack channel. The Bundle can be used in that channel only.

type: "slack_channel"



id: string



The Bundle Target's identifier. Starts with `btgt_`. No two Bundle Targets have the same one, and the same Bundle and target always give the same one, also after a detach and a new attach. It is opaque.



created_at: string



Time the Bundle was attached.

formatdate-time

slack_channel_id: string



The identifier of the Slack channel the Bundle is attached to, starting with `slch_`. It is the channel object's `id`, not Slack's `channel_id`.



BetaClaudeTagSlackChannelBundleTargetCreate object{ type: "slack_channel", slack_channel_id }



Attach the Bundle to a Slack channel.

type: "slack_channel"





slack_channel_id: string



The identifier of the Slack channel to attach the Bundle to, starting with `slch_`. It is the channel object's `id`, not Slack's `channel_id`.

minLength8

maxLength64



BetaClaudeTagSlackWorkspaceBundleTarget object{ type: "slack_workspace", id, created_at, slack_workspace_id }



One Bundle attached to one Slack workspace. The Bundle can be used in the workspace and in every channel in it.

type: "slack_workspace"



id: string



The Bundle Target's identifier. Starts with `btgt_`. No two Bundle Targets have the same one, and the same Bundle and target always give the same one, also after a detach and a new attach. It is opaque.



created_at: string



Time the Bundle was attached.

formatdate-time

slack_workspace_id: string



The identifier of the Slack workspace the Bundle is attached to, starting with `slws_`.



BetaClaudeTagSlackWorkspaceBundleTargetCreate object{ type: "slack_workspace", slack_workspace_id }



Attach the Bundle to a Slack workspace.

type: "slack_workspace"





slack_workspace_id: string



The identifier of the Slack workspace to attach the Bundle to, starting with `slws_`.
