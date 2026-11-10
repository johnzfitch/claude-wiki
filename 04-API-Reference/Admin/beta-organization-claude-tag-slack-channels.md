---
title: "Slack Channels - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/claude_tag/slack_channels"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-08T06:24:32Z"
tags: ["api", "slack"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Claude Tag](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag)

# Slack Channels

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

##### Models



BetaClaudeTagDeletedSlackChannel object{ type: "slack_channel_deleted", id }



Confirms that a Slack channel was removed from Claude Tag.

type: "slack_channel_deleted"



id: string



The removed channel's identifier.



BetaClaudeTagSlackChannel object{ type: "slack_channel", id, created_at, 4 more }



A Slack channel set up for Claude Tag, with the settings it stores or, with `include_inherited`, the settings that apply in it.
