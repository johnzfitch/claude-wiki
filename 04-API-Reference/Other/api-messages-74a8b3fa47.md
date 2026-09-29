---
title: "Messages - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/messages"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:15Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fmessages)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL



A beta version of this API exists and may have additional functionality. [View the beta version](/docs/en/api/http/beta/messages).

1.  [API reference](/docs/en/api/http)

# Messages

##### [Create a Message](/docs/en/api/http/messages/create)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

##### [Count tokens in a Message](/docs/en/api/http/messages/count_tokens)

POST/v1/messages/count_tokens

Count the number of tokens in a Message.

##### Models



Base64ImageSource object{ type: "base64", data, media_type }



type: "base64"





data: string



formatbyte



media_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"



One of the following:

"image/jpeg"



"image/png"



"image/gif"



"image/webp"





Base64PDFSource object{ type: "base64", data, media_type }



type: "base64"





data: string



formatbyte

media_type: "application/pdf"





BashCodeExecutionOutputBlock object{ type: "bash_code_execution_output", file_id }





type: "bash_code_execution_output"



defaultbash_code_execution_output

file_id: string





BashCodeExecutionOutputBlockParam object{ type: "bash_code_execution_output", file_id }



type: "bash_code_execution_output"



file_id: string





BashCodeExecutionResultBlock object{ type: "bash_code_execution_result", content, return_code, 2 more }





type: "bash_code_execution_result"



defaultbash_code_execution_result



content: array of [BashCodeExecutionOutputBlock](/docs/en/api/http/messages#bash_code_execution_output_block) { type: "bash_code_execution_output", file_id }





type: "bash_code_execution_output"



defaultbash_code_execution_output

file_id: string



return_code: number



stderr: string



stdout: string





BashCodeExecutionResultBlockParam object{ type: "bash_code_execution_result", content, return_code, 2 more }



type: "bash_code_execution_result"





content: array of [BashCodeExecutionOutputBlockParam](/docs/en/api/http/messages#bash_code_execution_output_block_param) { type: "bash_code_execution_output", file_id }



type: "bash_code_execution_output"



file_id: string



return_code: number



stderr: string



stdout: string





BashCodeExecutionToolResultBlock object{ type: "bash_code_execution_tool_result", content, tool_use_id }





BashCodeExecutionToolResultBlockParam object{ type: "bash_code_execution_tool_result", content, tool_use_id, cache_control }





BashCodeExecutionToolResultError object{ type: "bash_code_execution_tool_result_error", error_code }





type: "bash_code_execution_tool_result_error"



defaultbash_code_execution_tool_result_error



error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/http/messages#bash_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"



"output_file_too_large"





BashCodeExecutionToolResultErrorCode = "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"



"output_file_too_large"





BashCodeExecutionToolResultErrorParam object{ type: "bash_code_execution_tool_result_error", error_code }



type: "bash_code_execution_tool_result_error"





error_code: [BashCodeExecutionToolResultErrorCode](/docs/en/api/http/messages#bash_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"



"output_file_too_large"





BrowserCloseTabConfig object{ defer_loading, enabled }



`close_tab`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserDoubleClickConfig object{ defer_loading, enabled }



`double_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserFileUploadConfig object{ defer_loading, enabled }



`file_upload`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserFindConfig object{ defer_loading, enabled }



`find`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserFormInputConfig object{ defer_loading, enabled }



`form_input`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserGetPageTextConfig object{ defer_loading, enabled }



`get_page_text`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserHoldKeyConfig object{ defer_loading, enabled }



`hold_key`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserHoverConfig object{ defer_loading, enabled }



`hover`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserJavascriptExecConfig object{ defer_loading, enabled }



`javascript_exec`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserKeyConfig object{ defer_loading, enabled }



`key`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserLeftClickConfig object{ defer_loading, enabled }



`left_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserLeftClickDragConfig object{ defer_loading, enabled }



`left_click_drag`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserLeftMouseDownConfig object{ defer_loading, enabled }



`left_mouse_down`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserLeftMouseUpConfig object{ defer_loading, enabled }



`left_mouse_up`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserListTabsConfig object{ defer_loading, enabled }



`list_tabs`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserMiddleClickConfig object{ defer_loading, enabled }



`middle_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserMouseMoveConfig object{ defer_loading, enabled }



`mouse_move`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserNavigateConfig object{ defer_loading, enabled }



`navigate`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserNewTabConfig object{ defer_loading, enabled }



`new_tab`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserReadConsoleConfig object{ defer_loading, enabled }



`read_console`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserReadNetworkConfig object{ defer_loading, enabled }



`read_network`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserReadPageConfig object{ defer_loading, enabled }



`read_page`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserRightClickConfig object{ defer_loading, enabled }



`right_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserScreenshotConfig object{ defer_loading, enabled }



`screenshot`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserScrollConfig object{ defer_loading, enabled }



`scroll`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserScrollToConfig object{ defer_loading, enabled }



`scroll_to`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserStateBlockParam object{ type: "browser_state", tabs, cache_control, state_changes }



The caller's browser state after a browser toolset member call — the full inventory of open tabs, which tab is active, and any side effects (tabs opened, download state changes) the call produced.

At most one per `tool_result`, only on a non-error result answering a browser toolset member `tool_use`. The server renders the model-visible text from it; the model never sees the raw fields.



BrowserStateChange = [BrowserStateChangeTabOpened](/docs/en/api/http/messages#browser_state_change_tab_opened) or [BrowserStateChangeDownloadStarted](/docs/en/api/http/messages#browser_state_change_download_started) or [BrowserStateChangeDownloadCompleted](/docs/en/api/http/messages#browser_state_change_download_completed) or [BrowserStateChangeDownloadFailed](/docs/en/api/http/messages#browser_state_change_download_failed)



One of the following:



BrowserStateChangeDownloadCompleted object{ type: "download_completed", download_id, url, 2 more }



A file download that finished during this call, reported with the same `download_id` as its `download_started` — or without a prior `download_started`, when the download finished during the call that started it (at most one state change per `download_id` per result).

type: "download_completed"





download_id: string



The caller-assigned identifier for this download, stable across the state changes reporting it.

minLength1

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



url: string



The final post-redirect URL the download was served from.

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



path: optional string or null



Where the executor saved the file, on the executor's filesystem. Only included when another tool in the same environment can read the file at that path.

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



size_bytes: optional number or null



The completed download's size.

minimum0



BrowserStateChangeDownloadFailed object{ type: "download_failed", download_id, url, error }



A file download that failed — or was cancelled — during this call.

type: "download_failed"





download_id: string



The caller-assigned identifier for this download, stable across the state changes reporting it.

minLength1

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



url: string



The final post-redirect URL the download was served from.

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



error: optional string or null



The failure or cancellation detail, when known.

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



BrowserStateChangeDownloadStarted object{ type: "download_started", download_id, url }



A file download that started during this call.

type: "download_started"





download_id: string



The caller-assigned identifier for this download, stable across the state changes reporting it.

minLength1

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



url: string



The final post-redirect URL the download was served from.

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



BrowserStateChangeTabOpened object{ type: "tab_opened", tab_id }



A tab this call's execution opened that remains open at its end — the creation delta of the `tabs` inventory, not an event log.

Carries only the `tab_id`; the tab's `title` and `url` live on its `tabs` entry, which must include the same `tab_id`. A tab opened during a failed call gets no deferred `tab_opened`; it simply appears in the next result's `tabs` inventory.

type: "tab_opened"





tab_id: string



The `tab_id` of the opened tab, present in `tabs`.

minLength1

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



BrowserStateTabEntry object{ tab_id, title, url, active }



One open browser tab reported in a `browser_state` block's `tabs` inventory.

`tab_id` is the caller-assigned identifier for the tab; `title` and `url` describe the page the tab is currently showing and may be empty strings (a blank tab legitimately has both empty). `active` marks the tab that is active after this call; whenever `tabs` is non-empty, exactly one entry is marked.



tab_id: string



The caller-assigned identifier for this tab, unique within the inventory.

minLength1

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



title: string



The title of the page the tab is showing. May be empty.

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$



url: string



The URL of the page the tab is showing. May be empty.

maxLength4096

pattern^\[^\x00-\x1f\x7f-\x9f\u2028\u2029\]\*\$

active: optional boolean



Whether this tab is the active tab after this call. Whenever `tabs` is non-empty, exactly one entry is marked `active: true`.



BrowserSwitchTabConfig object{ defer_loading, enabled }



`switch_tab`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserToolset20260801 object{ type: "browser_toolset_20260801", cache_control, configs }



The browser toolset: a single `tools[]` entry (carrying no `name`) that declares the browser tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema.



BrowserToolsetConfigs object{ type, close_tab, double_click, 28 more }



Per-member configuration for `browser_toolset_20260801`: one optional field per member tool, keyed by the member name — the same name the member's `tool_use` blocks carry. Every member is an accepted key, and a member's defaults apply wherever its key is absent. Unknown keys are rejected: the field set is this toolset version's complete member set.



BrowserTripleClickConfig object{ defer_loading, enabled }



`triple_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserTypeConfig object{ defer_loading, enabled }



`type`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserWaitConfig object{ defer_loading, enabled }



`wait`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BrowserZoomConfig object{ defer_loading, enabled }



`zoom`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



CacheControlEphemeral object{ type: "ephemeral", ttl }



type: "ephemeral"





ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



"1h"





CacheCreation object{ ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }





ephemeral_1h_input_tokens: number



The number of input tokens used to create the 1 hour cache entry.

default0

minimum0



ephemeral_5m_input_tokens: number



The number of input tokens used to create the 5 minute cache entry.

default0

minimum0



CacheMissMessagesChanged object{ type: "messages_changed", cache_missed_input_tokens }





type: "messages_changed"



defaultmessages_changed

cache_missed_input_tokens: number



Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



CacheMissModelChanged object{ type: "model_changed", cache_missed_input_tokens }





type: "model_changed"



defaultmodel_changed

cache_missed_input_tokens: number



Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



CacheMissPreviousMessageNotFound object{ type: "previous_message_not_found" }





type: "previous_message_not_found"



defaultprevious_message_not_found



CacheMissReason = [CacheMissModelChanged](/docs/en/api/http/messages#cache_miss_model_changed) or [CacheMissSystemChanged](/docs/en/api/http/messages#cache_miss_system_changed) or [CacheMissToolsChanged](/docs/en/api/http/messages#cache_miss_tools_changed) or 3 more



One of the following:



CacheMissSystemChanged object{ type: "system_changed", cache_missed_input_tokens }





type: "system_changed"



defaultsystem_changed

cache_missed_input_tokens: number



Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



CacheMissToolsChanged object{ type: "tools_changed", cache_missed_input_tokens }





type: "tools_changed"



defaulttools_changed

cache_missed_input_tokens: number



Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



CacheMissUnavailable object{ type: "unavailable" }





type: "unavailable"



defaultunavailable



CitationCharLocation object{ type: "char_location", cited_text, document_index, 4 more }





type: "char_location"



defaultchar_location

cited_text: string





document_index: number



minimum0

document_title: string or null



end_char_index: number



file_id: string or null





start_char_index: number



minimum0



CitationCharLocationParam object{ type: "char_location", cited_text, document_index, 3 more }



type: "char_location"



cited_text: string





document_index: number



minimum0



document_title: string or null



minLength1

maxLength500

end_char_index: number





start_char_index: number



minimum0



CitationContentBlockLocation object{ type: "content_block_location", cited_text, document_index, 4 more }





type: "content_block_location"



defaultcontent_block_location



cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



document_index: number



minimum0

document_title: string or null





end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file_id: string or null





start_block_index: number



0-based index of the first cited block in the source's `content` array.

minimum0



CitationContentBlockLocationParam object{ type: "content_block_location", cited_text, document_index, 3 more }



type: "content_block_location"





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



document_index: number



minimum0



document_title: string or null



minLength1

maxLength500



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



start_block_index: number



0-based index of the first cited block in the source's `content` array.

minimum0



CitationPageLocation object{ type: "page_location", cited_text, document_index, 4 more }





type: "page_location"



defaultpage_location

cited_text: string





document_index: number



minimum0

document_title: string or null



end_page_number: number



file_id: string or null





start_page_number: number



minimum1



CitationPageLocationParam object{ type: "page_location", cited_text, document_index, 3 more }



type: "page_location"



cited_text: string





document_index: number



minimum0



document_title: string or null



minLength1

maxLength500

end_page_number: number





start_page_number: number



minimum1



CitationSearchResultLocationParam object{ type: "search_result_location", cited_text, end_block_index, 4 more }



type: "search_result_location"





cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string





start_block_index: number



0-based index of the first cited block in the source's `content` array.

minimum0

title: string or null





CitationWebSearchResultLocationParam object{ type: "web_search_result_location", cited_text, encrypted_index, 2 more }



type: "web_search_result_location"



cited_text: string



encrypted_index: string





title: string or null



minLength1

maxLength512



url: string



minLength1



CitationsConfig object{ enabled }





enabled: boolean



defaultfalse



CitationsConfigParam object{ enabled }



enabled: optional boolean





CitationsDelta object{ type: "citations_delta", citation }





CitationsSearchResultLocation object{ type: "search_result_location", cited_text, end_block_index, 4 more }





type: "search_result_location"



defaultsearch_result_location



cited_text: string



The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end_block_index: number



Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search_result_index: number



0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: string





start_block_index: number



0-based index of the first cited block in the source's `content` array.

minimum0

title: string or null





CitationsWebSearchResultLocation object{ type: "web_search_result_location", cited_text, encrypted_index, 2 more }





type: "web_search_result_location"



defaultweb_search_result_location

cited_text: string



encrypted_index: string





title: string or null



maxLength512

url: string





CodeExecutionOutputBlock object{ type: "code_execution_output", file_id }





type: "code_execution_output"



defaultcode_execution_output

file_id: string





CodeExecutionOutputBlockParam object{ type: "code_execution_output", file_id }



type: "code_execution_output"



file_id: string





CodeExecutionResultBlock object{ type: "code_execution_result", content, return_code, 2 more }





type: "code_execution_result"



defaultcode_execution_result



content: array of [CodeExecutionOutputBlock](/docs/en/api/http/messages#code_execution_output_block) { type: "code_execution_output", file_id }





type: "code_execution_output"



defaultcode_execution_output

file_id: string



return_code: number



stderr: string



stdout: string





CodeExecutionResultBlockParam object{ type: "code_execution_result", content, return_code, 2 more }



type: "code_execution_result"





content: array of [CodeExecutionOutputBlockParam](/docs/en/api/http/messages#code_execution_output_block_param) { type: "code_execution_output", file_id }



type: "code_execution_output"



file_id: string



return_code: number



stderr: string



stdout: string





CodeExecutionTool20250522 object{ type: "code_execution_20250522", name, allowed_callers, 3 more }





CodeExecutionTool20250825 object{ type: "code_execution_20250825", name, allowed_callers, 3 more }





CodeExecutionTool20260120 object{ type: "code_execution_20260120", name, allowed_callers, 3 more }



Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



CodeExecutionTool20260521 object{ type: "code_execution_20260521", name, allowed_callers, 3 more }



Code execution tool with REPL state persistence.



CodeExecutionToolResultBlock object{ type: "code_execution_tool_result", content, tool_use_id }





type: "code_execution_tool_result"



defaultcode_execution_tool_result



content: [CodeExecutionToolResultBlockContent](/docs/en/api/http/messages#code_execution_tool_result_block_content)



One of the following:



tool_use_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



CodeExecutionToolResultBlockContent = [CodeExecutionToolResultError](/docs/en/api/http/messages#code_execution_tool_result_error) or [CodeExecutionResultBlock](/docs/en/api/http/messages#code_execution_result_block) or [EncryptedCodeExecutionResultBlock](/docs/en/api/http/messages#encrypted_code_execution_result_block)



One of the following:



CodeExecutionToolResultBlockParam object{ type: "code_execution_tool_result", content, tool_use_id, cache_control }



type: "code_execution_tool_result"





content: [CodeExecutionToolResultBlockParamContent](/docs/en/api/http/messages#code_execution_tool_result_block_param_content)



One of the following:



tool_use_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



cache_control: optional [CacheControlEphemeral](/docs/en/api/http/messages#cache_control_ephemeral) { type: "ephemeral", ttl } or null



Create a cache control breakpoint at this content block.

type: "ephemeral"





ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



"1h"





CodeExecutionToolResultBlockParamContent = [CodeExecutionToolResultErrorParam](/docs/en/api/http/messages#code_execution_tool_result_error_param) or [CodeExecutionResultBlockParam](/docs/en/api/http/messages#code_execution_result_block_param) or [EncryptedCodeExecutionResultBlockParam](/docs/en/api/http/messages#encrypted_code_execution_result_block_param)



One of the following:



CodeExecutionToolResultError object{ type: "code_execution_tool_result_error", error_code }





type: "code_execution_tool_result_error"



defaultcode_execution_tool_result_error



error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/http/messages#code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"





CodeExecutionToolResultErrorCode = "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"





CodeExecutionToolResultErrorParam object{ type: "code_execution_tool_result_error", error_code }



type: "code_execution_tool_result_error"





error_code: [CodeExecutionToolResultErrorCode](/docs/en/api/http/messages#code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"





ComputerCursorPositionConfig object{ defer_loading, enabled }



`cursor_position`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerDoubleClickConfig object{ defer_loading, enabled }



`double_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerHoldKeyConfig object{ defer_loading, enabled }



`hold_key`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerKeyConfig object{ defer_loading, enabled }



`key`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerLeftClickConfig object{ defer_loading, enabled }



`left_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerLeftClickDragConfig object{ defer_loading, enabled }



`left_click_drag`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerLeftMouseDownConfig object{ defer_loading, enabled }



`left_mouse_down`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerLeftMouseUpConfig object{ defer_loading, enabled }



`left_mouse_up`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerMiddleClickConfig object{ defer_loading, enabled }



`middle_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerMouseMoveConfig object{ defer_loading, enabled }



`mouse_move`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerRightClickConfig object{ defer_loading, enabled }



`right_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerScreenshotConfig object{ defer_loading, enabled }



`screenshot`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerScrollConfig object{ defer_loading, enabled }



`scroll`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerToolset20260801 object{ type: "computer_toolset_20260801", cache_control, configs }



The computer toolset: a single `tools[]` entry (carrying no `name`) that declares the computer tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema. Every member is enabled by default, zoom included. The single-tool options `display_number` and `enable_zoom` are not fields of a toolset entry — it carries only `type`, `configs`, and `cache_control`; zoom is controlled via `configs.zoom.enabled`.



ComputerToolsetConfigs object{ type, cursor_position, double_click, 14 more }



Per-member configuration for `computer_toolset_20260801`: one optional field per member tool, keyed by the member name — the same name the member's `tool_use` blocks carry. Every member is an accepted key, and a member's defaults apply wherever its key is absent. Unknown keys are rejected: the field set is this toolset version's complete member set.



ComputerTripleClickConfig object{ defer_loading, enabled }



`triple_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerTypeConfig object{ defer_loading, enabled }



`type`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerWaitConfig object{ defer_loading, enabled }



`wait`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



ComputerZoomConfig object{ defer_loading, enabled }



`zoom`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



Container object{ id, expires_at, skills }



Information about the container used in the request (for the code execution tool)

id: string



Identifier for the container used in this request



expires_at: string



The time at which the container will expire.

formatdate-time



skills: array of [ContainerSkill](/docs/en/api/http/messages#container_skill) { type, skill_id, version } or null



Skills loaded in the container



type: "anthropic" or "custom"



Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"



"custom"





skill_id: string



Skill ID

minLength1

maxLength64



version: string



The resolved version: a skill version ID for custom skills.

minLength1

maxLength64



ContainerParams object{ id, skills }



Container parameters with skills to be loaded.

id: optional string or null



Container id



skills: optional array of [SkillParams](/docs/en/api/http/messages#skill_params) { type, skill_id, version } or null



List of skills to load in the container

maxItems20



type: "anthropic" or "custom"



Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"



"custom"





skill_id: string



Skill ID

minLength1

maxLength64



version: optional string



Skill version or 'latest' for most recent version

minLength1

maxLength64



ContainerSkill object{ type, skill_id, version }



A skill that was loaded in a container (response model).



type: "anthropic" or "custom"



Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"



"custom"





skill_id: string



Skill ID

minLength1

maxLength64



version: string



The resolved version: a skill version ID for custom skills.

minLength1

maxLength64



ContainerUploadBlock object{ type: "container_upload", file_id }



Response model for a file uploaded to the container.



type: "container_upload"



defaultcontainer_upload

file_id: string





ContainerUploadBlockParam object{ type: "container_upload", file_id, cache_control }



A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

type: "container_upload"



file_id: string





cache_control: optional [CacheControlEphemeral](/docs/en/api/http/messages#cache_control_ephemeral) { type: "ephemeral", ttl } or null



Create a cache control breakpoint at this content block.

type: "ephemeral"





ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



"1h"





ContentBlock = [TextBlock](/docs/en/api/http/messages#text_block) or [ThinkingBlock](/docs/en/api/http/messages#thinking_block) or [RedactedThinkingBlock](/docs/en/api/http/messages#redacted_thinking_block) or 9 more



One of the following:



ContentBlockParam = [TextBlockParam](/docs/en/api/http/messages#text_block_param) or [ImageBlockParam](/docs/en/api/http/messages#image_block_param) or [DocumentBlockParam](/docs/en/api/http/messages#document_block_param) or 13 more



One of the following:



ContentBlockSource object{ type: "content", content }



type: "content"





content: string or array of [ContentBlockSourceContent](/docs/en/api/http/messages#content_block_source_content)



One of the following:

string





ContentBlockSourceContent = array of [ContentBlockSourceContent](/docs/en/api/http/messages#content_block_source_content)



One of the following:



TextBlockParam object{ type: "text", text, cache_control, citations }





ImageBlockParam object{ type: "image", source, cache_control, transformations }





ContentBlockSourceContent = [TextBlockParam](/docs/en/api/http/messages#text_block_param) or [ImageBlockParam](/docs/en/api/http/messages#image_block_param)



One of the following:



TextBlockParam object{ type: "text", text, cache_control, citations }





ImageBlockParam object{ type: "image", source, cache_control, transformations }





Diagnostics object{ cache_miss_reason }



Request-level diagnostics: why the prompt cache could not fully reuse the prefix of the request named by `diagnostics.previous_message_id`.



cache_miss_reason: [CacheMissReason](/docs/en/api/http/messages#cache_miss_reason) or null



Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



DiagnosticsParam object{ previous_message_id }



Request-level diagnostics. Currently carries the previous response id for prompt-cache divergence reporting.



previous_message_id: optional string or null



The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

maxLength256



DirectCaller object{ type: "direct" }



Tool invocation directly from the model.

type: "direct"





DocumentBlock object{ type: "document", citations, source, title }





DocumentBlockParam object{ type: "document", source, cache_control, 3 more }





EncryptedCodeExecutionResultBlock object{ type: "encrypted_code_execution_result", content, encrypted_stdout, 2 more }



Code execution result with encrypted stdout for PFC + web_search results.



type: "encrypted_code_execution_result"



defaultencrypted_code_execution_result



content: array of [CodeExecutionOutputBlock](/docs/en/api/http/messages#code_execution_output_block) { type: "code_execution_output", file_id }





type: "code_execution_output"



defaultcode_execution_output

file_id: string



encrypted_stdout: string



return_code: number



stderr: string





EncryptedCodeExecutionResultBlockParam object{ type: "encrypted_code_execution_result", content, encrypted_stdout, 2 more }



Code execution result with encrypted stdout for PFC + web_search results.

type: "encrypted_code_execution_result"





content: array of [CodeExecutionOutputBlockParam](/docs/en/api/http/messages#code_execution_output_block_param) { type: "code_execution_output", file_id }



type: "code_execution_output"



file_id: string



encrypted_stdout: string



return_code: number



stderr: string





FileDocumentSource object{ type: "file", file_id }



type: "file"



file_id: string





FileImageSource object{ type: "file", file_id }



type: "file"



file_id: string





ImageBlockParam object{ type: "image", source, cache_control, transformations }





ImageTransformationsParam object{ oversized_image }



Configures the transformations the server applies to this image before the model observes it. Each key names a condition the server transforms images for; its value selects the transformation applied. Omitted keys keep their default behavior, and an empty object is equivalent to omitting the field.



oversized_image: optional "downsize" or "error"



What the server does when this image exceeds the model's maximum image size. `"downsize"` (the default) scales the image down to fit, which changes the dimensions the model observes without telling you. `"error"` instead rejects the request with a 400 error naming the image's dimensions and the largest dimensions that fit, so you can scale the image deliberately — your image is never silently scaled down.

One of the following:

"downsize"



"error"





InputJSONDelta object{ type: "input_json_delta", partial_json }





type: "input_json_delta"



defaultinput_json_delta

partial_json: string





JSONOutputFormat object{ type: "json_schema", schema }



type: "json_schema"



schema: map\[unknown\]



The JSON schema of the format



MemoryTool20250818 object{ type: "memory_20250818", name, allowed_callers, 4 more }





Message object{ type: "message", id, container, 8 more }





MessageCountTokensTool = [Tool](/docs/en/api/http/messages#tool) or [ToolBash20250124](/docs/en/api/http/messages#tool_bash_20250124) or [CodeExecutionTool20250522](/docs/en/api/http/messages#code_execution_tool_20250522) or 18 more



One of the following:



MessageCreateParamsContainer = [ContainerParams](/docs/en/api/http/messages#container_params) or string



Container identifier for reuse across requests.

One of the following:



ContainerParams object{ id, skills }



Container parameters with skills to be loaded.

id: optional string or null



Container id



skills: optional array of [SkillParams](/docs/en/api/http/messages#skill_params) { type, skill_id, version } or null



List of skills to load in the container

maxItems20



type: "anthropic" or "custom"



Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"



"custom"





skill_id: string



Skill ID

minLength1

maxLength64



version: optional string



Skill version or 'latest' for most recent version

minLength1

maxLength64

string





MessageDeltaUsage object{ cache_creation_input_tokens, cache_read_input_tokens, input_tokens, 3 more }





MessageParam object{ content, role }





MessageTokensCount object{ input_tokens }



input_tokens: number



The total number of tokens across the provided list of messages, system prompt, and tools.



Metadata object{ user_id }





user_id: optional string or null



An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



Model = string or "claude-fable-5-1" or "claude-opus-5-5" or "claude-mythos-5-1" or 15 more



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



OutputConfig object{ effort, format }





effort: optional "low" or "medium" or "high" or 2 more or null



How much effort the model should put into its response. Higher effort levels may result in more thorough analysis but take longer.

Valid values are `low`, `medium`, `high`, `xhigh`, or `max`.

One of the following:

"low"



"medium"



"high"



"xhigh"



"max"





format: optional [JSONOutputFormat](/docs/en/api/http/messages#json_output_format) { type: "json_schema", schema } or null



A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

type: "json_schema"



schema: map\[unknown\]



The JSON schema of the format



OutputTokensDetails object{ thinking_tokens }





thinking_tokens: number



Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.

default0

minimum0



PlainTextSource object{ type: "text", data, media_type }



type: "text"



data: string



media_type: "text/plain"





RawContentBlockDelta = [TextDelta](/docs/en/api/http/messages#text_delta) or [InputJSONDelta](/docs/en/api/http/messages#input_json_delta) or [CitationsDelta](/docs/en/api/http/messages#citations_delta) or 2 more



One of the following:



RawContentBlockDeltaEvent object{ type: "content_block_delta", delta, index }





type: "content_block_delta"



defaultcontent_block_delta



delta: [RawContentBlockDelta](/docs/en/api/http/messages#raw_content_block_delta)



One of the following:

index: number





RawContentBlockStartEvent object{ type: "content_block_start", content_block, index }





RawContentBlockStopEvent object{ type: "content_block_stop", index }





type: "content_block_stop"



defaultcontent_block_stop

index: number





RawMessageDeltaEvent object{ type: "message_delta", delta, usage }





RawMessageStartEvent object{ type: "message_start", message }





type: "message_start"



defaultmessage_start



message: [Message](/docs/en/api/http/messages#message) { type: "message", id, container, 8 more }





RawMessageStopEvent object{ type: "message_stop" }





type: "message_stop"



defaultmessage_stop



RawMessageStreamEvent = [RawMessageStartEvent](/docs/en/api/http/messages#raw_message_start_event) or [RawMessageDeltaEvent](/docs/en/api/http/messages#raw_message_delta_event) or [RawMessageStopEvent](/docs/en/api/http/messages#raw_message_stop_event) or 3 more



One of the following:



RedactedThinkingBlock object{ type: "redacted_thinking", data }





type: "redacted_thinking"



defaultredacted_thinking



data: string



The contents of this redacted thinking block, returned when portions of the model's thinking were safety-redacted. This field is opaque and encrypted, with no readable content.

Pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#redacted-thinking-blocks) for details.



RedactedThinkingBlockParam object{ type: "redacted_thinking", data }



type: "redacted_thinking"



data: string



The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.



RefusalStopDetails object{ type: "refusal", category, explanation }



Structured information about a refusal.



type: "refusal"



defaultrefusal



category: "cyber" or "bio" or "frontier_llm" or 2 more or null



The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

One of the following:

"cyber"



The request could enable cyber harm, such as malware or exploit development. Benign cybersecurity work can also trigger this category.

"bio"



The request could enable biological harm, such as dangerous lab methods. Beneficial life sciences work can also trigger this category.

"frontier_llm"



The request could assist the development of competing AI models, which is restricted under [Anthropic's commercial terms](https://www.anthropic.com/legal/commercial-terms). Benign machine learning work can also trigger this category.

"reasoning_extraction"



The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking).

"general_harms"



The request could be related to an area that was determined as harmful. Benign work might sometimes trigger this category.



explanation: string or null



Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



SearchResultBlockParam object{ type: "search_result", content, source, 3 more }





ServerToolCaller object{ type: "code_execution_20250825", tool_id }



Tool invocation generated by a server-side tool.

type: "code_execution_20250825"





tool_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



ServerToolCaller20260120 object{ type: "code_execution_20260120", tool_id }



type: "code_execution_20260120"





tool_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



ServerToolUsage object{ web_fetch_requests, web_search_requests }





web_fetch_requests: number



The number of web fetch tool requests.

default0

minimum0



web_search_requests: number



The number of web search tool requests.

default0

minimum0



ServerToolUseBlock object{ type: "server_tool_use", id, caller, 2 more }





ServerToolUseBlockParam object{ type: "server_tool_use", id, input, 3 more }





SignatureDelta object{ type: "signature_delta", signature }





type: "signature_delta"



defaultsignature_delta

signature: string



The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.



SkillParams object{ type, skill_id, version }



Specification for a skill to be loaded in a container (request model).



type: "anthropic" or "custom"



Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"



"custom"





skill_id: string



Skill ID

minLength1

maxLength64



version: optional string



Skill version or 'latest' for most recent version

minLength1

maxLength64



StopReason = "end_turn" or "max_tokens" or "stop_sequence" or 4 more



One of the following:

"end_turn"



"max_tokens"



"stop_sequence"



"tool_use"



"pause_turn"



"refusal"



"model_context_window_exceeded"





TextBlock object{ type: "text", citations, text }





TextBlockParam object{ type: "text", text, cache_control, citations }





TextCitation = [CitationCharLocation](/docs/en/api/http/messages#citation_char_location) or [CitationPageLocation](/docs/en/api/http/messages#citation_page_location) or [CitationContentBlockLocation](/docs/en/api/http/messages#citation_content_block_location) or 2 more



One of the following:



TextCitationParam = [CitationCharLocationParam](/docs/en/api/http/messages#citation_char_location_param) or [CitationPageLocationParam](/docs/en/api/http/messages#citation_page_location_param) or [CitationContentBlockLocationParam](/docs/en/api/http/messages#citation_content_block_location_param) or 2 more



One of the following:



TextDelta object{ type: "text_delta", text }





type: "text_delta"



defaulttext_delta

text: string





TextEditorCodeExecutionCreateResultBlock object{ type: "text_editor_code_execution_create_result", is_file_update }





type: "text_editor_code_execution_create_result"



defaulttext_editor_code_execution_create_result

is_file_update: boolean





TextEditorCodeExecutionCreateResultBlockParam object{ type: "text_editor_code_execution_create_result", is_file_update }



type: "text_editor_code_execution_create_result"



is_file_update: boolean





TextEditorCodeExecutionStrReplaceResultBlock object{ type: "text_editor_code_execution_str_replace_result", lines, new_lines, 3 more }





type: "text_editor_code_execution_str_replace_result"



defaulttext_editor_code_execution_str_replace_result

lines: array of string or null



new_lines: number or null



new_start: number or null



old_lines: number or null



old_start: number or null





TextEditorCodeExecutionStrReplaceResultBlockParam object{ type: "text_editor_code_execution_str_replace_result", lines, new_lines, 3 more }



type: "text_editor_code_execution_str_replace_result"



lines: optional array of string or null



new_lines: optional number or null



new_start: optional number or null



old_lines: optional number or null



old_start: optional number or null





TextEditorCodeExecutionToolResultBlock object{ type: "text_editor_code_execution_tool_result", content, tool_use_id }





TextEditorCodeExecutionToolResultBlockParam object{ type: "text_editor_code_execution_tool_result", content, tool_use_id, cache_control }





TextEditorCodeExecutionToolResultError object{ type: "text_editor_code_execution_tool_result_error", error_code, error_message }





type: "text_editor_code_execution_tool_result_error"



defaulttext_editor_code_execution_tool_result_error



error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/http/messages#text_editor_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"



"file_not_found"



error_message: string or null





TextEditorCodeExecutionToolResultErrorCode = "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"



"file_not_found"





TextEditorCodeExecutionToolResultErrorParam object{ type: "text_editor_code_execution_tool_result_error", error_code, error_message }



type: "text_editor_code_execution_tool_result_error"





error_code: [TextEditorCodeExecutionToolResultErrorCode](/docs/en/api/http/messages#text_editor_code_execution_tool_result_error_code)



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"



"file_not_found"



error_message: optional string or null





TextEditorCodeExecutionViewResultBlock object{ type: "text_editor_code_execution_view_result", content, file_type, 3 more }





type: "text_editor_code_execution_view_result"



defaulttext_editor_code_execution_view_result

content: string





file_type: "text" or "image" or "pdf"



One of the following:

"text"



"image"



"pdf"



num_lines: number or null



start_line: number or null



total_lines: number or null





TextEditorCodeExecutionViewResultBlockParam object{ type: "text_editor_code_execution_view_result", content, file_type, 3 more }



type: "text_editor_code_execution_view_result"



content: string





file_type: "text" or "image" or "pdf"



One of the following:

"text"



"image"



"pdf"



num_lines: optional number or null



start_line: optional number or null



total_lines: optional number or null





ThinkingBlock object{ type: "thinking", signature, thinking }





type: "thinking"



defaultthinking



signature: string



A value used to verify that this thinking block was generated by Claude when it is passed back to the API.

This is an opaque field and should not be interpreted or parsed. When passing thinking blocks back to the API (required when using tools with extended thinking), pass them back exactly as received, with this field intact.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

thinking: string



The text of Claude's thinking process for this block.



ThinkingBlockParam object{ type: "thinking", signature, thinking }



type: "thinking"





signature: string



The `signature` value of this thinking block, exactly as returned by the API in a previous response. Used to verify that the block was generated by Claude.

Thinking blocks must be passed back unmodified and in their original order; a modified block results in a 400 `invalid_request_error`.

thinking: string



The `thinking` text of this block as returned by the API.



ThinkingConfigAdaptive object{ type: "adaptive", display }



type: "adaptive"





display: optional "summarized" or "omitted" or null



Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"



"omitted"





ThinkingConfigDisabled object{ type: "disabled" }



type: "disabled"





ThinkingConfigEnabled object{ type: "enabled", budget_tokens, display }



type: "enabled"





budget_tokens: number



Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

minimum1024



display: optional "summarized" or "omitted" or null



Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"



"omitted"





ThinkingConfigParam = [ThinkingConfigEnabled](/docs/en/api/http/messages#thinking_config_enabled) or [ThinkingConfigDisabled](/docs/en/api/http/messages#thinking_config_disabled) or [ThinkingConfigAdaptive](/docs/en/api/http/messages#thinking_config_adaptive)



Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

One of the following:



ThinkingDelta object{ type: "thinking_delta", thinking }





type: "thinking_delta"



defaultthinking_delta

thinking: string



The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.



Tool object{ type, input_schema, name, 7 more }





ToolBash20250124 object{ type: "bash_20250124", name, allowed_callers, 4 more }





ToolChoice = [ToolChoiceAuto](/docs/en/api/http/messages#tool_choice_auto) or [ToolChoiceAny](/docs/en/api/http/messages#tool_choice_any) or [ToolChoiceTool](/docs/en/api/http/messages#tool_choice_tool) or [ToolChoiceNone](/docs/en/api/http/messages#tool_choice_none)



How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



ToolChoiceAny object{ type: "any", disable_parallel_tool_use }



The model will use any available tools.

type: "any"





disable_parallel_tool_use: optional boolean



Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



ToolChoiceAuto object{ type: "auto", disable_parallel_tool_use }



The model will automatically decide whether to use tools.

type: "auto"





disable_parallel_tool_use: optional boolean



Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



ToolChoiceNone object{ type: "none" }



The model will not be allowed to use tools.

type: "none"





ToolChoiceTool object{ type: "tool", name, disable_parallel_tool_use }



The model will use the specified tool with `tool_choice.name`.

type: "tool"



name: string



The name of the tool to use.



disable_parallel_tool_use: optional boolean



Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



ToolReferenceBlock object{ type: "tool_reference", tool_name }





type: "tool_reference"



defaulttool_reference



tool_name: string



minLength1

maxLength256

pattern^\[a-zA-Z0-9\_-\]{1,256}\$



ToolReferenceBlockParam object{ type: "tool_reference", tool_name, cache_control }



Tool reference block that can be included in tool_result content.

type: "tool_reference"





tool_name: string



minLength1

maxLength256

pattern^\[a-zA-Z0-9\_-\]{1,256}\$



cache_control: optional [CacheControlEphemeral](/docs/en/api/http/messages#cache_control_ephemeral) { type: "ephemeral", ttl } or null



Create a cache control breakpoint at this content block.

type: "ephemeral"





ttl: optional "5m" or "1h"



The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for details.

One of the following:

"5m"



"1h"





ToolResultBlockParam object{ type: "tool_result", tool_use_id, cache_control, 3 more }





ToolSearchToolBm25_20251119 object{ type, name, allowed_callers, 3 more }





ToolSearchToolRegex20251119 object{ type, name, allowed_callers, 3 more }





ToolSearchToolResultBlock object{ type: "tool_search_tool_result", content, tool_use_id }





ToolSearchToolResultBlockParam object{ type: "tool_search_tool_result", content, tool_use_id, cache_control }





ToolSearchToolResultError object{ type: "tool_search_tool_result_error", error_code, error_message }





type: "tool_search_tool_result_error"



defaulttool_search_tool_result_error



error_code: [ToolSearchToolResultErrorCode](/docs/en/api/http/messages#tool_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"



error_message: string or null





ToolSearchToolResultErrorCode = "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"





ToolSearchToolResultErrorParam object{ type: "tool_search_tool_result_error", error_code, error_message }



type: "tool_search_tool_result_error"





error_code: [ToolSearchToolResultErrorCode](/docs/en/api/http/messages#tool_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



"unavailable"



"too_many_requests"



"execution_time_exceeded"



error_message: optional string or null





ToolSearchToolSearchResultBlock object{ type: "tool_search_tool_search_result", tool_references }





type: "tool_search_tool_search_result"



defaulttool_search_tool_search_result



tool_references: array of [ToolReferenceBlock](/docs/en/api/http/messages#tool_reference_block) { type: "tool_reference", tool_name }





type: "tool_reference"



defaulttool_reference



tool_name: string



minLength1

maxLength256

pattern^\[a-zA-Z0-9\_-\]{1,256}\$



ToolSearchToolSearchResultBlockParam object{ type: "tool_search_tool_search_result", tool_references }





ToolTextEditor20250124 object{ type: "text_editor_20250124", name, allowed_callers, 4 more }





ToolTextEditor20250429 object{ type: "text_editor_20250429", name, allowed_callers, 4 more }





ToolTextEditor20250728 object{ type: "text_editor_20250728", name, allowed_callers, 5 more }





ToolUnion = [Tool](/docs/en/api/http/messages#tool) or [ToolBash20250124](/docs/en/api/http/messages#tool_bash_20250124) or [CodeExecutionTool20250522](/docs/en/api/http/messages#code_execution_tool_20250522) or 18 more



One of the following:



ToolUseBlock object{ type: "tool_use", id, caller, 3 more }





ToolUseBlockParam object{ type: "tool_use", id, input, 4 more }





URLImageSource object{ type: "url", url }



type: "url"



url: string





URLPDFSource object{ type: "url", url }



type: "url"



url: string





Usage object{ cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 6 more }





UserLocation object{ type: "approximate", city, country, 2 more }



type: "approximate"





city: optional string or null



The city of the user.

minLength1

maxLength255



country: optional string or null



The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

minLength2

maxLength2



region: optional string or null



The region of the user.

minLength1

maxLength255



timezone: optional string or null



The [IANA timezone](https://nodatime.org/TimeZones) of the user.

minLength1

maxLength255



WebFetchBlock object{ type: "web_fetch_result", content, retrieved_at, url }





type: "web_fetch_result"



defaultweb_fetch_result



content: [DocumentBlock](/docs/en/api/http/messages#document_block) { type: "document", citations, source, title }



retrieved_at: string or null



ISO 8601 timestamp when the content was retrieved

url: string



Fetched content URL



WebFetchBlockParam object{ type: "web_fetch_result", content, url, retrieved_at }



type: "web_fetch_result"





content: [DocumentBlockParam](/docs/en/api/http/messages#document_block_param) { type: "document", source, cache_control, 3 more }



url: string



Fetched content URL

retrieved_at: optional string or null



ISO 8601 timestamp when the content was retrieved



WebFetchTool20250910 object{ type: "web_fetch_20250910", name, allowed_callers, 9 more }





WebFetchTool20260209 object{ type: "web_fetch_20260209", name, allowed_callers, 9 more }





WebFetchTool20260309 object{ type: "web_fetch_20260309", name, allowed_callers, 10 more }



Web fetch tool with use_cache parameter for bypassing cached content.



WebFetchTool20260318 object{ type: "web_fetch_20260318", name, allowed_callers, 11 more }





WebFetchToolResultBlock object{ type: "web_fetch_tool_result", caller, content, tool_use_id }





WebFetchToolResultBlockParam object{ type: "web_fetch_tool_result", content, tool_use_id, 2 more }





WebFetchToolResultErrorBlock object{ type: "web_fetch_tool_result_error", error_code }





type: "web_fetch_tool_result_error"



defaultweb_fetch_tool_result_error



error_code: [WebFetchToolResultErrorCode](/docs/en/api/http/messages#web_fetch_tool_result_error_code)



One of the following:

"invalid_tool_input"



"url_too_long"



"url_not_allowed"



"url_not_in_prior_context"



"url_not_accessible"



"unsupported_content_type"



"too_many_requests"



"max_uses_exceeded"



"unavailable"



"content_too_large"





WebFetchToolResultErrorBlockParam object{ type: "web_fetch_tool_result_error", error_code }



type: "web_fetch_tool_result_error"





error_code: [WebFetchToolResultErrorCode](/docs/en/api/http/messages#web_fetch_tool_result_error_code)



One of the following:

"invalid_tool_input"



"url_too_long"



"url_not_allowed"



"url_not_in_prior_context"



"url_not_accessible"



"unsupported_content_type"



"too_many_requests"



"max_uses_exceeded"



"unavailable"



"content_too_large"





WebFetchToolResultErrorCode = "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 7 more



One of the following:

"invalid_tool_input"



"url_too_long"



"url_not_allowed"



"url_not_in_prior_context"



"url_not_accessible"



"unsupported_content_type"



"too_many_requests"



"max_uses_exceeded"



"unavailable"



"content_too_large"





WebFetchURLSourceAll object{ type: "all" }



The `url_sources` variant under which a source contributes in full: every result of the tool filter's source, or all user input.

type: "all"





WebFetchURLSourceExcept object{ type: "except", tools }



The tool filter variant under which every result but the named tools' contributes.

type: "except"





tools: array of [WebFetchURLSourceToolReference](/docs/en/api/http/messages#web_fetch_url_source_tool_reference) { type: "tool_reference", name }



type: "tool_reference"



name: string





WebFetchURLSourceNone object{ type: "none" }



The `url_sources` variant under which a source contributes nothing: no result of the tool filter's source, or no user input.

type: "none"





WebFetchURLSourceOnly object{ type: "only", tools }



The tool filter variant under which only the named tools' results contribute.

type: "only"





tools: array of [WebFetchURLSourceToolReference](/docs/en/api/http/messages#web_fetch_url_source_tool_reference) { type: "tool_reference", name }



type: "tool_reference"



name: string





WebFetchURLSourceToolReference object{ type: "tool_reference", name }



One entry of a tool filter's `tools`: it must name a tool declared in this request's `tools[]`.

type: "tool_reference"



name: string





WebFetchURLSources object{ client_tool_results, server_tool_results, user_input }



Which sources contribute to the set of URLs web fetch may fetch.

Each key is a tagged variant: `user_input` is `all` or `none`; the two tool filters are `all`, `none`, `only` (only the named tools' results) or `except` (every result but the named tools'). A named tool must be declared in this request's `tools[]`.



WebSearchResultBlock object{ type: "web_search_result", encrypted_content, page_age, 2 more }





type: "web_search_result"



defaultweb_search_result

encrypted_content: string



page_age: string or null



title: string



url: string





WebSearchResultBlockParam object{ type: "web_search_result", encrypted_content, title, 2 more }



type: "web_search_result"



encrypted_content: string



title: string



url: string



page_age: optional string or null





WebSearchTool20250305 object{ type: "web_search_20250305", name, allowed_callers, 7 more }





WebSearchTool20260209 object{ type: "web_search_20260209", name, allowed_callers, 7 more }





WebSearchTool20260318 object{ type: "web_search_20260318", name, allowed_callers, 8 more }





WebSearchToolRequestError object{ type: "web_search_tool_result_error", error_code }



type: "web_search_tool_result_error"





error_code: [WebSearchToolResultErrorCode](/docs/en/api/http/messages#web_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



"unavailable"



"max_uses_exceeded"



"too_many_requests"



"query_too_long"



"request_too_large"





WebSearchToolResultBlock object{ type: "web_search_tool_result", caller, content, tool_use_id }





WebSearchToolResultBlockContent = [WebSearchToolResultError](/docs/en/api/http/messages#web_search_tool_result_error) or array of [WebSearchResultBlock](/docs/en/api/http/messages#web_search_result_block)



One of the following:



WebSearchToolResultBlockParam object{ type: "web_search_tool_result", content, tool_use_id, 2 more }





WebSearchToolResultBlockParamContent = array of [WebSearchResultBlockParam](/docs/en/api/http/messages#web_search_result_block_param) or [WebSearchToolRequestError](/docs/en/api/http/messages#web_search_tool_request_error)



One of the following:



WebSearchToolResultError object{ type: "web_search_tool_result_error", error_code }





type: "web_search_tool_result_error"



defaultweb_search_tool_result_error



error_code: [WebSearchToolResultErrorCode](/docs/en/api/http/messages#web_search_tool_result_error_code)



One of the following:

"invalid_tool_input"



"unavailable"



"max_uses_exceeded"



"too_many_requests"



"query_too_long"



"request_too_large"





WebSearchToolResultErrorCode = "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more



One of the following:

"invalid_tool_input"



"unavailable"



"max_uses_exceeded"



"too_many_requests"



"query_too_long"



"request_too_large"



#### Messages[Batches](/docs/en/api/http/messages/batches)

##### [Create a Message Batch](/docs/en/api/http/messages/batches/create)

POST/v1/messages/batches

Send a batch of Message creation requests.

##### [Retrieve a Message Batch](/docs/en/api/http/messages/batches/retrieve)

GET/v1/messages/batches/{message_batch_id}

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

##### [List Message Batches](/docs/en/api/http/messages/batches/list)

GET/v1/messages/batches

List all Message Batches within a Workspace. Most recently created batches are returned first.

##### [Cancel a Message Batch](/docs/en/api/http/messages/batches/cancel)

POST/v1/messages/batches/{message_batch_id}/cancel

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

##### [Delete a Message Batch](/docs/en/api/http/messages/batches/delete)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/http/messages/batches/results)

GET/v1/messages/batches/{message_batch_id}/results

Streams the results of a Message Batch as a `.jsonl` file.
