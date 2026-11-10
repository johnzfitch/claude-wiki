---
title: "Claude Tag - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/claude_tag"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-08T06:24:51Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Claude Tag

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### Models



BetaClaudeTagDefaultSettingSource object{ type: "default" }



No settings level sets a value, and the built-in default applies.

type: "default"





BetaClaudeTagGuestPolicy = [BetaClaudeTagGuestPolicyAllow](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag#beta_claude_tag_guest_policy_allow) or [BetaClaudeTagGuestPolicyRestrict](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag#beta_claude_tag_guest_policy_restrict) or [BetaClaudeTagGuestPolicyChannelOnly](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag#beta_claude_tag_guest_policy_channel_only)



What Claude does in a channel while a Slack guest is in it, for everyone in the channel. It changes nothing in a channel without Slack guests. More types can be added.

One of the following:



BetaClaudeTagGuestPolicyAllow object{ type: "allow" }



Claude answers in the channel.

type: "allow"





BetaClaudeTagGuestPolicyRestrict object{ type: "restrict" }



Claude does not answer in the channel.

type: "restrict"





BetaClaudeTagGuestPolicyChannelOnly object{ type: "channel_only" }



Claude answers with only the Bundles attached to the channel itself.

type: "channel_only"





BetaClaudeTagGuestPolicyAllow object{ type: "allow" }



Claude answers in the channel.

type: "allow"





BetaClaudeTagGuestPolicyChannelOnly object{ type: "channel_only" }



Claude answers with only the Bundles attached to the channel itself.

type: "channel_only"





BetaClaudeTagGuestPolicyRestrict object{ type: "restrict" }



Claude does not answer in the channel.

type: "restrict"





BetaClaudeTagSettingSource = [BetaClaudeTagSlackChannelSettingSource](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag#beta_claude_tag_slack_channel_setting_source) or [BetaClaudeTagSlackWorkspaceSettingSource](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag#beta_claude_tag_slack_workspace_setting_source) or [BetaClaudeTagSlackParentChannelSettingSource](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag#beta_claude_tag_slack_parent_channel_setting_source) or 3 more



The settings level a value comes from. More types can be added.

One of the following:



BetaClaudeTagSettingSources object{ enabled, environment_id, guest_policy, 2 more }



For each setting, the settings level its value in `settings` comes from. Without `include_inherited`, a setting the channel or workspace stores has a source that names the channel or workspace itself, and one it does not store has null, or an empty list for `instructions`. With `include_inherited=true` no member is null: a value that no settings level sets has the source `default`.



BetaClaudeTagSettings object{ enabled, environment_id, guest_policy, 2 more }



Claude Tag settings. Without `include_inherited`, a setting that is null is not set on the settings level and is inherited. With it, `enabled` and `guest_policy` are never null, and `instructions`, `model` and `environment_id` are null when no settings level sets them.



BetaClaudeTagSettingsCreate object{ enabled, environment_id, guest_policy, 2 more }



The settings in a request that sets a Slack channel up. A setting left out is not set. A setting sent as null is cleared.



BetaClaudeTagSettingsUpdate object{ enabled, environment_id, guest_policy, 2 more }



The settings to change. A setting left out is unchanged. A setting sent as null is cleared, so it is inherited.



BetaClaudeTagSlackChannelIdentifiers object{ channel_id, workspace_id }



The identifiers Slack shows for a channel. They are Slack's own, not identifiers of this API.



channel_id: string



Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

minLength2

maxLength32



workspace_id: string



Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

minLength2

maxLength32



BetaClaudeTagSlackChannelSettingSource object{ type: "slack_channel", slack_channel_id }



The value comes from the addressed Slack channel itself.

type: "slack_channel"



slack_channel_id: string



The channel's identifier, starting with `slch_`.



BetaClaudeTagSlackDefaultSettingSource object{ type: "slack_default" }



The value comes from the organization's Slack defaults, which have no identifier.

type: "slack_default"





BetaClaudeTagSlackGridChannelSettingSource object{ type: "slack_grid_channel", slack }



The value comes from the addressed channel as it is set up under another workspace of its Enterprise Grid: a channel shared across the Grid keeps one Slack channel identifier in every workspace that sees it.

type: "slack_grid_channel"





slack: [BetaClaudeTagSlackChannelIdentifiers](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag#beta_claude_tag_slack_channel_identifiers) { channel_id, workspace_id }



Slack's own identifiers for the channel under that other workspace.



channel_id: string



Slack's identifier for the channel, starting with `C` or `G`, such as `C0456EFGH`.

minLength2

maxLength32



workspace_id: string



Slack's identifier for the workspace the channel is in, starting with `T`, such as `T0123ABCD`.

minLength2

maxLength32



BetaClaudeTagSlackParentChannelSettingSource object{ type: "slack_parent_channel", slack_channel_id }



The value comes from the channel that a code channel was started from. A parent channel contributes `instructions` and `environment_id` only.

type: "slack_parent_channel"



slack_channel_id: string



The parent channel's identifier, starting with `slch_`.



BetaClaudeTagSlackWorkspaceIdentifiers object{ workspace_id }



The identifier Slack shows for a workspace. It is Slack's own, not an identifier of this API.

workspace_id: string



Slack's identifier for the workspace, starting with `T`, such as `T0123ABCD`.



BetaClaudeTagSlackWorkspaceSettingSource object{ type: "slack_workspace", slack_workspace_id }



The value comes from a Slack workspace of the organization.

type: "slack_workspace"



slack_workspace_id: string



The workspace's identifier, starting with `slws_`.

#### Claude Tag[Slack Channels](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels)

##### [Set Up Slack Channel](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels/create)

POST/v1/organizations/claude_tag/slack_channels

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Set a Slack channel up for Claude Tag and return it with its identifier. If the channel is already set up, whether in claude.ai, by Claude's first use in it or by an earlier request, the existing channel is returned, so the request can be repeated. `settings`, when sent, is applied as an update applies it. Before a channel is set up, Claude's Slack app confirms with Slack that the channel is in the workspace, is not archived and is visible to the app; a channel that fails the confirmation returns 404. Setting the channel up and applying `settings` are two steps: when the second is refused, the response is the refusal, the channel stays set up with every setting unset, and the error's `details.slack_channel_id` holds the channel's identifier.

##### [List Slack Channels](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels/list)

GET/v1/organizations/claude_tag/slack_channels

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

List the set-up Slack channels of one Slack workspace, newest first by `created_at`. A channel that is not set up is not listed: Slack holds the full list of a workspace's channels. Pass `slack_channel_id` as well to look one channel up by its Slack identifiers: `data` then holds that channel, or is empty when it is not set up, and `limit` and `page` are ignored. A workspace that the organization owns only through a Slack Enterprise Grid returns 404 until it is set up. With `include_inherited=true` each channel's `settings` holds what applies in it, and the request fails with 503 rather than resolve against a settings level that could not be read. A `page` cursor resumes only a request with the same `include_inherited`.

##### [Get Slack Channel](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels/retrieve)

GET/v1/organizations/claude_tag/slack_channels/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Get one Slack channel and its settings. By default `settings` holds what the channel itself stores: a setting that is null there is not set on the channel and is inherited. With `include_inherited=true`, `settings` holds what applies in the channel once the settings levels above it are taken into account, and the request fails with 503 rather than resolve against a settings level that could not be read. Either way `sources` names the settings level each value comes from, so a caller tells the channel's own value from an inherited one by its source, not by whether it is null.

##### [Update Slack Channel](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels/update)

POST/v1/organizations/claude_tag/slack_channels/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Change the settings a Slack channel stores. The update is partial: a setting left out is unchanged, and a setting sent as null is cleared, so the channel inherits it. If any value is refused, no setting in the request is stored. A group direct message takes no settings and returns 400.

##### [Remove Slack Channel](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_channels/delete)

DELETE/v1/organizations/claude_tag/slack_channels/{id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Remove a Slack channel from Claude Tag. This deletes the channel's stored settings and its Bundle Targets at once, and then, in the background, the channel's sessions and their transcripts, its memory, its routines and the artifacts published from it. None of it can be restored. The channel in Slack and its messages are unchanged. The request is refused with 400 and `error.details.error_code` `slack_channel_enabled` while `enabled` resolves to `true` for the channel, as a read with `include_inherited=true` returns it: set `enabled` to `false` on the channel first. This guards against removing a channel in use by mistake; it is not a way to keep Claude out, because the removal deletes the channel's own `enabled: false` with its other settings, after which the channel inherits again and Claude's next use of it can set it up anew with a new identifier. The identifier returns 404 as soon as the request returns, so a repeated removal returns 404. A group direct message returns 400, and so does a channel that holds configuration this API does not manage.

#### Claude Tag[Slack Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/slack_workspaces)

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

#### Claude Tag[Bundles](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles)

##### [List Bundles](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/list)

GET/v1/organizations/claude_tag/bundles

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

List the organization's Bundles, newest first by `created_at`. A Bundle that Claude Tag manages for itself is not listed.

##### [Get Bundle](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/retrieve)

GET/v1/organizations/claude_tag/bundles/{bundle_id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Get one Bundle. What the Bundle grants (connectors, repositories and credentials) is never returned.

#### Claude TagBundles[Targets](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets)

##### [List Bundle Targets](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/list)

GET/v1/organizations/claude_tag/bundles/{bundle_id}/targets

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

List the Slack channels and Slack workspaces a Bundle is attached to, newest first by `created_at`. Only channels and workspaces the organization owns are listed; a Bundle that is attached to anything else has no Bundle Target for it.

##### [Attach Bundle](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/create)

POST/v1/organizations/claude_tag/bundles/{bundle_id}/targets

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Attach a Bundle to a Slack channel or a Slack workspace. A Bundle attached to a workspace can be used in the workspace and in every channel in it. Attaching a Bundle to a channel or workspace it is already attached to returns the existing Bundle Target. The channel or workspace must be set up: attaching never sets a channel up. A group direct message takes no Bundle and returns 400.

##### [Get Bundle Target](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/retrieve)

GET/v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Get one Bundle Target. Returns 404 when `target_id` is the identifier of another Bundle's Bundle Target, or the Bundle Target was detached.

##### [Detach Bundle](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets/delete)

DELETE/v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Detach a Bundle from a Slack channel or a Slack workspace. A repeated detach returns 404.
