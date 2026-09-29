---
title: "Messages - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/messages"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:36Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fmessages)

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

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)

# Messages

##### [Create a Message](/docs/en/api/http/beta/messages/create)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

##### [Count tokens in a Message](/docs/en/api/http/beta/messages/count_tokens)

POST/v1/messages/count_tokens

Count the number of tokens in a Message.

##### Models



BetaAdvisorMessageIterationUsage object{ type: "advisor_message", cache_creation, cache_creation_input_tokens, 4 more }



Token usage for an advisor sub-inference iteration.



BetaAdvisorRedactedResultBlock object{ type: "advisor_redacted_result", encrypted_content, stop_reason }





type: "advisor_redacted_result"



defaultadvisor_redacted_result

encrypted_content: string



Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop_reason: string or null



The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).



BetaAdvisorRedactedResultBlockParam object{ type: "advisor_redacted_result", encrypted_content, stop_reason }



type: "advisor_redacted_result"



encrypted_content: string



Opaque blob produced by a prior response; must be round-tripped verbatim.

stop_reason: optional string or null





BetaAdvisorResultBlock object{ type: "advisor_result", stop_reason, text }





type: "advisor_result"



defaultadvisor_result

stop_reason: string or null



The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string





BetaAdvisorResultBlockParam object{ type: "advisor_result", text, stop_reason }



type: "advisor_result"



text: string



stop_reason: optional string or null





BetaAdvisorTool20260301 object{ type: "advisor_20260301", model, name, 7 more }





BetaAdvisorToolResultBlock object{ type: "advisor_tool_result", content, tool_use_id }





BetaAdvisorToolResultBlockParam object{ type: "advisor_tool_result", content, tool_use_id, cache_control }





BetaAdvisorToolResultError object{ type: "advisor_tool_result_error", error_code }





type: "advisor_tool_result_error"



defaultadvisor_tool_result_error



error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more



One of the following:

"max_uses_exceeded"



"prompt_too_long"



"too_many_requests"



"overloaded"



"unavailable"



"execution_time_exceeded"



"model_not_found"





BetaAdvisorToolResultErrorParam object{ type: "advisor_tool_result_error", error_code }



type: "advisor_tool_result_error"





error_code: "max_uses_exceeded" or "prompt_too_long" or "too_many_requests" or 4 more



One of the following:

"max_uses_exceeded"



"prompt_too_long"



"too_many_requests"



"overloaded"



"unavailable"



"execution_time_exceeded"



"model_not_found"





BetaAllThinkingTurns object{ type: "all" }



type: "all"





BetaBase64ImageSource object{ type: "base64", data, media_type }

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

BetaBase64PDFSource object{ type: "base64", data, media_type }

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

BetaBashCodeExecutionOutputBlock object{ type: "bash_code_execution_output", file_id }





type: "bash_code_execution_output"



defaultbash_code_execution_output

file_id: string





BetaBashCodeExecutionOutputBlockParam object{ type: "bash_code_execution_output", file_id }



type: "bash_code_execution_output"



file_id: string





BetaBashCodeExecutionResultBlock object{ type: "bash_code_execution_result", content, return_code, 2 more }





type: "bash_code_execution_result"



defaultbash_code_execution_result



content: array of [BetaBashCodeExecutionOutputBlock](/docs/en/api/http/beta/messages#beta_bash_code_execution_output_block) { type: "bash_code_execution_output", file_id }

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

BetaBashCodeExecutionResultBlockParam object{ type: "bash_code_execution_result", content, return_code, 2 more }



type: "bash_code_execution_result"





content: array of [BetaBashCodeExecutionOutputBlockParam](/docs/en/api/http/beta/messages#beta_bash_code_execution_output_block_param) { type: "bash_code_execution_output", file_id }

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

BetaBashCodeExecutionToolResultBlock object{ type: "bash_code_execution_tool_result", content, tool_use_id }





BetaBashCodeExecutionToolResultBlockParam object{ type: "bash_code_execution_tool_result", content, tool_use_id, cache_control }





BetaBashCodeExecutionToolResultError object{ type: "bash_code_execution_tool_result_error", error_code }





type: "bash_code_execution_tool_result_error"



defaultbash_code_execution_tool_result_error



error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

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

BetaBashCodeExecutionToolResultErrorParam object{ type: "bash_code_execution_tool_result_error", error_code }



type: "bash_code_execution_tool_result_error"





error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

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

BetaBrowserCloseTabConfig object{ defer_loading, enabled }



`close_tab`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserDoubleClickConfig object{ defer_loading, enabled }



`double_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserFileUploadConfig object{ defer_loading, enabled }



`file_upload`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserFindConfig object{ defer_loading, enabled }



`find`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserFormInputConfig object{ defer_loading, enabled }



`form_input`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserGetPageTextConfig object{ defer_loading, enabled }



`get_page_text`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserHoldKeyConfig object{ defer_loading, enabled }



`hold_key`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserHoverConfig object{ defer_loading, enabled }



`hover`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserJavascriptExecConfig object{ defer_loading, enabled }



`javascript_exec`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserKeyConfig object{ defer_loading, enabled }



`key`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserLeftClickConfig object{ defer_loading, enabled }



`left_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserLeftClickDragConfig object{ defer_loading, enabled }



`left_click_drag`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserLeftMouseDownConfig object{ defer_loading, enabled }



`left_mouse_down`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserLeftMouseUpConfig object{ defer_loading, enabled }



`left_mouse_up`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserListTabsConfig object{ defer_loading, enabled }



`list_tabs`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserMiddleClickConfig object{ defer_loading, enabled }



`middle_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserMouseMoveConfig object{ defer_loading, enabled }



`mouse_move`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserNavigateConfig object{ defer_loading, enabled }



`navigate`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserNewTabConfig object{ defer_loading, enabled }



`new_tab`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserReadConsoleConfig object{ defer_loading, enabled }



`read_console`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserReadNetworkConfig object{ defer_loading, enabled }



`read_network`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserReadPageConfig object{ defer_loading, enabled }



`read_page`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserRightClickConfig object{ defer_loading, enabled }



`right_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserScreenshotConfig object{ defer_loading, enabled }



`screenshot`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserScrollConfig object{ defer_loading, enabled }



`scroll`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserScrollToConfig object{ defer_loading, enabled }



`scroll_to`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserStateBlockParam object{ type: "browser_state", tabs, cache_control, state_changes }



The caller's browser state after a browser toolset member call — the full inventory of open tabs, which tab is active, and any side effects (tabs opened, download state changes) the call produced.

At most one per `tool_result`, only on a non-error result answering a browser toolset member `tool_use`. The server renders the model-visible text from it; the model never sees the raw fields.



BetaBrowserStateChange = [BetaBrowserStateChangeTabOpened](/docs/en/api/http/beta/messages#beta_browser_state_change_tab_opened) or [BetaBrowserStateChangeDownloadStarted](/docs/en/api/http/beta/messages#beta_browser_state_change_download_started) or [BetaBrowserStateChangeDownloadCompleted](/docs/en/api/http/beta/messages#beta_browser_state_change_download_completed) or [BetaBrowserStateChangeDownloadFailed](/docs/en/api/http/beta/messages#beta_browser_state_change_download_failed)



One of the following:



BetaBrowserStateChangeDownloadCompleted object{ type: "download_completed", download_id, url, 2 more }

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

BetaBrowserStateChangeDownloadFailed object{ type: "download_failed", download_id, url, error }

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

BetaBrowserStateChangeDownloadStarted object{ type: "download_started", download_id, url }

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

BetaBrowserStateChangeTabOpened object{ type: "tab_opened", tab_id }

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

BetaBrowserStateTabEntry object{ tab_id, title, url, active }

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

BetaBrowserSwitchTabConfig object{ defer_loading, enabled }



`switch_tab`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserToolset20260801 object{ type: "browser_toolset_20260801", cache_control, configs }



The browser toolset: a single `tools[]` entry (carrying no `name`) that declares the browser tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema.



BetaBrowserToolsetConfigs object{ type, close_tab, double_click, 28 more }



Per-member configuration for `browser_toolset_20260801`: one optional field per member tool, keyed by the member name — the same name the member's `tool_use` blocks carry. Every member is an accepted key, and a member's defaults apply wherever its key is absent. Unknown keys are rejected: the field set is this toolset version's complete member set.



BetaBrowserTripleClickConfig object{ defer_loading, enabled }



`triple_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserTypeConfig object{ defer_loading, enabled }



`type`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserWaitConfig object{ defer_loading, enabled }



`wait`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaBrowserZoomConfig object{ defer_loading, enabled }



`zoom`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaCacheControlEphemeral object{ type: "ephemeral", ttl }

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

BetaCacheCreation object{ ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

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

BetaCacheMissMessagesChanged object{ type: "messages_changed", cache_missed_input_tokens }





type: "messages_changed"



defaultmessages_changed

cache_missed_input_tokens: number



Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



BetaCacheMissModelChanged object{ type: "model_changed", cache_missed_input_tokens }





type: "model_changed"



defaultmodel_changed

cache_missed_input_tokens: number



Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



BetaCacheMissPreviousMessageNotFound object{ type: "previous_message_not_found" }





type: "previous_message_not_found"



defaultprevious_message_not_found



BetaCacheMissReason = [BetaCacheMissModelChanged](/docs/en/api/http/beta/messages#beta_cache_miss_model_changed) or [BetaCacheMissSystemChanged](/docs/en/api/http/beta/messages#beta_cache_miss_system_changed) or [BetaCacheMissToolsChanged](/docs/en/api/http/beta/messages#beta_cache_miss_tools_changed) or 3 more



One of the following:



BetaCacheMissSystemChanged object{ type: "system_changed", cache_missed_input_tokens }





type: "system_changed"



defaultsystem_changed

cache_missed_input_tokens: number



Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



BetaCacheMissToolsChanged object{ type: "tools_changed", cache_missed_input_tokens }





type: "tools_changed"



defaulttools_changed

cache_missed_input_tokens: number



Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.



BetaCacheMissUnavailable object{ type: "unavailable" }





type: "unavailable"



defaultunavailable



BetaCitationCharLocation object{ type: "char_location", cited_text, document_index, 4 more }

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

BetaCitationCharLocationParam object{ type: "char_location", cited_text, document_index, 3 more }

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

BetaCitationConfig object{ enabled }





enabled: boolean



defaultfalse



BetaCitationContentBlockLocation object{ type: "content_block_location", cited_text, document_index, 4 more }

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

BetaCitationContentBlockLocationParam object{ type: "content_block_location", cited_text, document_index, 3 more }

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

BetaCitationPageLocation object{ type: "page_location", cited_text, document_index, 4 more }

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

BetaCitationPageLocationParam object{ type: "page_location", cited_text, document_index, 3 more }

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

BetaCitationSearchResultLocation object{ type: "search_result_location", cited_text, end_block_index, 4 more }

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

BetaCitationSearchResultLocationParam object{ type: "search_result_location", cited_text, end_block_index, 4 more }

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

BetaCitationWebSearchResultLocationParam object{ type: "web_search_result_location", cited_text, encrypted_index, 2 more }

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

BetaCitationsConfigParam object{ enabled }



enabled: optional boolean





BetaCitationsDelta object{ type: "citations_delta", citation }





BetaCitationsWebSearchResultLocation object{ type: "web_search_result_location", cited_text, encrypted_index, 2 more }

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

BetaClearThinking20251015Edit object{ type: "clear_thinking_20251015", keep }



type: "clear_thinking_20251015"





keep: optional [BetaThinkingTurns](/docs/en/api/http/beta/messages#beta_thinking_turns) or [BetaAllThinkingTurns](/docs/en/api/http/beta/messages#beta_all_thinking_turns) or "all"



Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



BetaThinkingTurns object{ type: "thinking_turns", value }



type: "thinking_turns"





value: number



minimum1



BetaAllThinkingTurns object{ type: "all" }



type: "all"



"all"





BetaClearThinking20251015EditResponse object{ type: "clear_thinking_20251015", cleared_input_tokens, cleared_thinking_turns }





type: "clear_thinking_20251015"



The type of context management edit applied.

defaultclear_thinking_20251015



cleared_input_tokens: number



Number of input tokens cleared by this edit.

minimum0



cleared_thinking_turns: number



Number of thinking turns that were cleared.

minimum0



BetaClearToolUses20250919Edit object{ type: "clear_tool_uses_20250919", clear_at_least, clear_tool_inputs, 3 more }





BetaClearToolUses20250919EditResponse object{ type: "clear_tool_uses_20250919", cleared_input_tokens, cleared_tool_uses }





type: "clear_tool_uses_20250919"



The type of context management edit applied.

defaultclear_tool_uses_20250919



cleared_input_tokens: number



Number of input tokens cleared by this edit.

minimum0



cleared_tool_uses: number



Number of tool uses that were cleared.

minimum0



BetaCodeExecutionOutputBlock object{ type: "code_execution_output", file_id }





type: "code_execution_output"



defaultcode_execution_output

file_id: string





BetaCodeExecutionOutputBlockParam object{ type: "code_execution_output", file_id }



type: "code_execution_output"



file_id: string





BetaCodeExecutionResultBlock object{ type: "code_execution_result", content, return_code, 2 more }





type: "code_execution_result"



defaultcode_execution_result



content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/http/beta/messages#beta_code_execution_output_block) { type: "code_execution_output", file_id }

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

BetaCodeExecutionResultBlockParam object{ type: "code_execution_result", content, return_code, 2 more }



type: "code_execution_result"





content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/http/beta/messages#beta_code_execution_output_block_param) { type: "code_execution_output", file_id }

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

BetaCodeExecutionTool20250522 object{ type: "code_execution_20250522", name, allowed_callers, 3 more }





BetaCodeExecutionTool20250825 object{ type: "code_execution_20250825", name, allowed_callers, 3 more }





BetaCodeExecutionTool20260120 object{ type: "code_execution_20260120", name, allowed_callers, 3 more }



Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



BetaCodeExecutionTool20260521 object{ type: "code_execution_20260521", name, allowed_callers, 3 more }



Code execution tool with REPL state persistence.



BetaCodeExecutionToolResultBlock object{ type: "code_execution_tool_result", content, tool_use_id }





type: "code_execution_tool_result"



defaultcode_execution_tool_result



content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/http/beta/messages#beta_code_execution_tool_result_block_content)



One of the following:



tool_use_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



BetaCodeExecutionToolResultBlockContent = [BetaCodeExecutionToolResultError](/docs/en/api/http/beta/messages#beta_code_execution_tool_result_error) or [BetaCodeExecutionResultBlock](/docs/en/api/http/beta/messages#beta_code_execution_result_block) or [BetaEncryptedCodeExecutionResultBlock](/docs/en/api/http/beta/messages#beta_encrypted_code_execution_result_block)



One of the following:



BetaCodeExecutionToolResultBlockParam object{ type: "code_execution_tool_result", content, tool_use_id, cache_control }



type: "code_execution_tool_result"





content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/http/beta/messages#beta_code_execution_tool_result_block_param_content)



One of the following:



tool_use_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/http/beta/messages#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

BetaCodeExecutionToolResultBlockParamContent = [BetaCodeExecutionToolResultErrorParam](/docs/en/api/http/beta/messages#beta_code_execution_tool_result_error_param) or [BetaCodeExecutionResultBlockParam](/docs/en/api/http/beta/messages#beta_code_execution_result_block_param) or [BetaEncryptedCodeExecutionResultBlockParam](/docs/en/api/http/beta/messages#beta_encrypted_code_execution_result_block_param)



One of the following:



BetaCodeExecutionToolResultError object{ type: "code_execution_tool_result_error", error_code }





type: "code_execution_tool_result_error"



defaultcode_execution_tool_result_error



error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/http/beta/messages#beta_code_execution_tool_result_error_code)

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

BetaCodeExecutionToolResultErrorCode = "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

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

BetaCodeExecutionToolResultErrorParam object{ type: "code_execution_tool_result_error", error_code }



type: "code_execution_tool_result_error"





error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/http/beta/messages#beta_code_execution_tool_result_error_code)

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

BetaCompact20260112Edit object{ type: "compact_20260112", instructions, pause_after_compaction, trigger }



Automatically compact older context when reaching the configured trigger threshold.

type: "compact_20260112"



instructions: optional string or null



Additional instructions for summarization.

pause_after_compaction: optional boolean



Whether to pause after compaction and return the compaction block to the user.



trigger: optional [BetaInputTokensTrigger](/docs/en/api/http/beta/messages#beta_input_tokens_trigger) { type: "input_tokens", value } or null



When to trigger compaction. Defaults to 150000 input tokens.

type: "input_tokens"





value: number



minimum1



BetaCompactionBlock object{ type: "compaction", content, encrypted_content, 2 more }



A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.



BetaCompactionBlockParam object{ type: "compaction", cache_control, content, 3 more }



A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.



BetaCompactionConfig object{ type: "summarize", instructions }



Compact the whole conversation and return a signed `compaction` block, alone, that a later request sends back first in `messages`, in place of the messages it summarizes. There is no trigger and no pause flag: sending the parameter compacts, and nothing is sampled after the block.

The summarization prompt is the server's own unless `instructions` are given, which then replace it for this request; a value that is empty or only whitespace counts as absent.

type: "summarize"





instructions: optional string or null



Replaces the server's default summarization prompt for this request. An empty or whitespace-only value counts as absent.

maxLength16384



BetaCompactionContentBlockDelta object{ type: "compaction_delta", content, encrypted_content }





type: "compaction_delta"



defaultcompaction_delta

content: string or null



encrypted_content: string or null



Opaque metadata from prior compaction, to be round-tripped verbatim



BetaCompactionIterationUsage object{ type: "compaction", cache_creation, cache_creation_input_tokens, 3 more }



Token usage for a compaction iteration.



type: "compaction"



Usage for a compaction iteration

defaultcompaction



cache_creation: [BetaCacheCreation](/docs/en/api/http/beta/messages#beta_cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens } or null



Breakdown of cached tokens by TTL

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

cache_creation_input_tokens: number



The number of input tokens used to create the cache entry.

default0

minimum0



cache_read_input_tokens: number



The number of input tokens read from the cache.

default0

minimum0



input_tokens: number



The number of input tokens which were used.

minimum0



output_tokens: number



The number of output tokens which were used.

minimum0



BetaComputerCursorPositionConfig object{ defer_loading, enabled }



`cursor_position`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerDoubleClickConfig object{ defer_loading, enabled }



`double_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerHoldKeyConfig object{ defer_loading, enabled }



`hold_key`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerKeyConfig object{ defer_loading, enabled }



`key`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerLeftClickConfig object{ defer_loading, enabled }



`left_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerLeftClickDragConfig object{ defer_loading, enabled }



`left_click_drag`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerLeftMouseDownConfig object{ defer_loading, enabled }



`left_mouse_down`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerLeftMouseUpConfig object{ defer_loading, enabled }



`left_mouse_up`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerMiddleClickConfig object{ defer_loading, enabled }



`middle_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerMouseMoveConfig object{ defer_loading, enabled }



`mouse_move`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerRightClickConfig object{ defer_loading, enabled }



`right_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerScreenshotConfig object{ defer_loading, enabled }



`screenshot`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerScrollConfig object{ defer_loading, enabled }



`scroll`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerToolset20260801 object{ type: "computer_toolset_20260801", cache_control, configs }



The computer toolset: a single `tools[]` entry (carrying no `name`) that declares the computer tool family. The model is served the family's tool with any members disabled via `configs` removed from its schema. Every member is enabled by default, zoom included. The single-tool options `display_number` and `enable_zoom` are not fields of a toolset entry — it carries only `type`, `configs`, and `cache_control`; zoom is controlled via `configs.zoom.enabled`.



BetaComputerToolsetConfigs object{ type, cursor_position, double_click, 14 more }



Per-member configuration for `computer_toolset_20260801`: one optional field per member tool, keyed by the member name — the same name the member's `tool_use` blocks carry. Every member is an accepted key, and a member's defaults apply wherever its key is absent. Unknown keys are rejected: the field set is this toolset version's complete member set.



BetaComputerTripleClickConfig object{ defer_loading, enabled }



`triple_click`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerTypeConfig object{ defer_loading, enabled }



`type`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerWaitConfig object{ defer_loading, enabled }



`wait`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaComputerZoomConfig object{ defer_loading, enabled }



`zoom`'s config overrides.

defer_loading: optional boolean or null



Defer loading for this member. Must resolve to the same value on every enabled member of the toolset.

enabled: optional boolean or null



Whether this member is offered to the model. Default is per member, per the toolset's documentation. A member whose enabled resolves false is withheld from the served schema.



BetaContainer object{ id, expires_at, skills }

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

skills: array of [BetaContainerSkill](/docs/en/api/http/beta/messages#beta_container_skill) { type, skill_id, version } or null

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

BetaContainerParams object{ id, skills }



Container parameters with skills to be loaded.

id: optional string or null



Container id



skills: optional array of [BetaSkillParams](/docs/en/api/http/beta/messages#beta_skill_params) { type, skill_id, version } or null

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

BetaContainerSkill object{ type, skill_id, version }

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

BetaContainerUploadBlock object{ type: "container_upload", file_id }



Response model for a file uploaded to the container.



type: "container_upload"



defaultcontainer_upload

file_id: string





BetaContainerUploadBlockParam object{ type: "container_upload", file_id, cache_control }



A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

type: "container_upload"



file_id: string





cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/http/beta/messages#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

BetaContentBlock = [BetaTextBlock](/docs/en/api/http/beta/messages#beta_text_block) or [BetaThinkingBlock](/docs/en/api/http/beta/messages#beta_thinking_block) or [BetaRedactedThinkingBlock](/docs/en/api/http/beta/messages#beta_redacted_thinking_block) or 15 more



One of the following:



BetaContentBlockParam = [BetaTextBlockParam](/docs/en/api/http/beta/messages#beta_text_block_param) or [BetaImageBlockParam](/docs/en/api/http/beta/messages#beta_image_block_param) or [BetaRequestDocumentBlock](/docs/en/api/http/beta/messages#beta_request_document_block) or 21 more



One of the following:



BetaContentBlockSource object{ type: "content", content }



type: "content"





content: string or array of [BetaContentBlockSourceContent](/docs/en/api/http/beta/messages#beta_content_block_source_content)



One of the following:

string





BetaContentBlockSourceContent = array of [BetaContentBlockSourceContent](/docs/en/api/http/beta/messages#beta_content_block_source_content)



One of the following:



BetaTextBlockParam object{ type: "text", text, cache_control, citations }





BetaImageBlockParam object{ type: "image", source, cache_control, transformations }





BetaContentBlockSourceContent = [BetaTextBlockParam](/docs/en/api/http/beta/messages#beta_text_block_param) or [BetaImageBlockParam](/docs/en/api/http/beta/messages#beta_image_block_param)



One of the following:



BetaTextBlockParam object{ type: "text", text, cache_control, citations }





BetaImageBlockParam object{ type: "image", source, cache_control, transformations }





BetaContextManagementConfig object{ edits }





BetaContextManagementResponse object{ applied_edits }





BetaCountTokensContextManagementResponse object{ original_input_tokens }



original_input_tokens: number



The original token count before context management was applied



BetaDiagnostics object{ cache_miss_reason }



Request-level diagnostics: why the prompt cache could not fully reuse the prefix of the request named by `diagnostics.previous_message_id`.



cache_miss_reason: [BetaCacheMissReason](/docs/en/api/http/beta/messages#beta_cache_miss_reason) or null



Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



BetaDiagnosticsParam object{ previous_message_id }



Request-level diagnostics. Currently carries the previous response id for prompt-cache divergence reporting.



previous_message_id: optional string or null



The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.

maxLength256



BetaDirectCaller object{ type: "direct" }



Tool invocation directly from the model.

type: "direct"





BetaDocumentBlock object{ type: "document", citations, source, title }





BetaEncryptedCodeExecutionResultBlock object{ type: "encrypted_code_execution_result", content, encrypted_stdout, 2 more }



Code execution result with encrypted stdout for PFC + web_search results.



type: "encrypted_code_execution_result"



defaultencrypted_code_execution_result



content: array of [BetaCodeExecutionOutputBlock](/docs/en/api/http/beta/messages#beta_code_execution_output_block) { type: "code_execution_output", file_id }

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

BetaEncryptedCodeExecutionResultBlockParam object{ type: "encrypted_code_execution_result", content, encrypted_stdout, 2 more }



Code execution result with encrypted stdout for PFC + web_search results.

type: "encrypted_code_execution_result"





content: array of [BetaCodeExecutionOutputBlockParam](/docs/en/api/http/beta/messages#beta_code_execution_output_block_param) { type: "code_execution_output", file_id }

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

BetaFallbackBlock object{ type: "fallback", from, to, trigger }



Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and declined. A turn where no preceding model ran and declined has no such boundary and carries no block — the signal for whether a fallback model served the response is the presence of a `fallback_message` entry in `usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it arrives via the standard `content_block_start` / `content_block_stop` pair and carries no deltas.



BetaFallbackBlockParam object{ type: "fallback", from, to, trigger }



A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its original position. The block marks the boundary between content produced before and after a fallback hop, and the server relies on that boundary to validate the turn: when thinking runs flank the boundary, omitting the block merges them into one span the server cannot validate (the request is rejected), and moving it into the middle of a single run is likewise rejected; between non-thinking blocks the block's placement has no validation effect.

type: "fallback"





from: [BetaFallbackInfoParam](/docs/en/api/http/beta/messages#beta_fallback_info_param) { model }



Identifies one hop of a fallback transition.



model: [Model](/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



to: [BetaFallbackInfoParam](/docs/en/api/http/beta/messages#beta_fallback_info_param) { model }



Identifies one hop of a fallback transition.



model: [Model](/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

trigger: optional unknown



The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



BetaFallbackCreditNotApplied object{ type: "not_applied", reason, remove_to_redeem }



No reprice was applied; `reason` says why.



BetaFallbackCreditRedeemed object{ type: "redeemed" }



The reprice was applied: the retry is billed as if the conversation had been on the retry model all along.



type: "redeemed"



defaultredeemed



BetaFallbackCreditTokenParam object{ token, mode }



Object form of `fallback_credit_token`: the token plus a redemption mode.

Requires `anthropic-beta: fallback-credit-2026-07-01`; without that header the field accepts the bare string only. The bare string and the mode-less object are equivalent (both select `strict`), so wrapping an existing token changes nothing by itself.



token: string



The opaque `fallback_credit_token` from a prior refusal's `stop_details` — the same string the bare-string form carries.

minLength1

maxLength2048



mode: optional "strict" or "best_effort"



How a failing token affects the retry. `strict` (the default, and the bare-string behavior): a failing redemption is a 400 and the retry is not served. `best_effort`: the retry is served either way — a token-layer failure no longer rejects the request; the retry proceeds at normal price and the outcome is reported on the response's `usage.fallback_credit`. Two failures stay hard in both modes: a malformed token, and combining `fallback_credit_token` with `fallbacks`.

One of the following:

"strict"



"best_effort"





BetaFallbackCreditUsage object{ status }



Outcome of the `fallback_credit_token` presented on this request.



status: [BetaFallbackCreditRedeemed](/docs/en/api/http/beta/messages#beta_fallback_credit_redeemed) or [BetaFallbackCreditNotApplied](/docs/en/api/http/beta/messages#beta_fallback_credit_not_applied)



Whether the fallback-credit reprice was applied to this response's billing.

A union discriminated on `type`. `redeemed`: the retry is billed as if the conversation had been on the retry model all along — including when the resulting shift is zero because there was nothing to move. `not_applied`: no reprice was applied; the arm's `reason` says why.

One of the following:



BetaFallbackCreditRedeemed object{ type: "redeemed" }



The reprice was applied: the retry is billed as if the conversation had been on the retry model all along.



type: "redeemed"



defaultredeemed



BetaFallbackCreditNotApplied object{ type: "not_applied", reason, remove_to_redeem }



No reprice was applied; `reason` says why.



BetaFallbackInfo object{ model }



Identifies one hop of a fallback transition.



model: [Model](/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaFallbackInfoParam object{ model }



Identifies one hop of a fallback transition.



model: [Model](/docs/en/api/http/messages#model)



The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



BetaFallbackMessageIterationUsage object{ type: "fallback_message", cache_creation, cache_creation_input_tokens, 4 more }



Token usage for the fallback-model attempt of a server-side fallback request.

The terminal entry of a fallback-served turn: when a fallback hop's output is the returned message, the entry for the iteration that completed it carries this type in place of `message`. A declined hop and the serving hop's earlier tool-loop iterations produce `message` entries. Whether a fallback model served the response is signalled by the presence of this entry in `usage.iterations`.



BetaFallbackParam object{ model, max_tokens, output_config, 2 more }



One entry in the `fallbacks` chain on a `/v1/messages` request.

`model` is required. The override fields (`max_tokens`, `thinking`, `output_config`, and `speed`) set the corresponding parameter for this attempt only and are validated as if the request were made to `model`. Any other key is rejected at parse time.



BetaFallbackRefusalTrigger object{ type: "refusal", category }



The `from` model declined for policy reasons.



type: "refusal"



defaultrefusal



category: "cyber" or "bio" or "frontier_llm" or 2 more or null



The policy category that triggered the `from` model's refusal at this hop. `null` when the refusal doesn't map to a named category. Same vocabulary as `stop_details.category`.

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

BetaFallbacksParam = array of [BetaFallbackParam](/docs/en/api/http/beta/messages#beta_fallback_param) or "default"



Opt-in server-side retry on one or more substitute models when the requested model declines for policy reasons. Tried in order: if the first entry also declines, the second is tried, and so on. The string "default" requests the requested model's server-defined default fallback configuration.

One of the following:



BetaFileDocumentSource object{ type: "file", file_id }



type: "file"



file_id: string





BetaFileImageSource object{ type: "file", file_id }



type: "file"



file_id: string





BetaImageBlockParam object{ type: "image", source, cache_control, transformations }





BetaImageTransformationsParam object{ oversized_image }

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

BetaInputJSONDelta object{ type: "input_json_delta", partial_json }





type: "input_json_delta"



defaultinput_json_delta

partial_json: string





BetaInputTokensClearAtLeast object{ type: "input_tokens", value }



type: "input_tokens"





value: number



minimum0



BetaInputTokensTrigger object{ type: "input_tokens", value }



type: "input_tokens"





value: number



minimum1



BetaInputTransformation = [BetaThinkingDroppedInputTransformation](/docs/en/api/http/beta/messages#beta_thinking_dropped_input_transformation) or [BetaThinkingMismatchAllowedInputTransformation](/docs/en/api/http/beta/messages#beta_thinking_mismatch_allowed_input_transformation)



One entry of `input_transformations`: either a change the API made to the request's input before showing it to the model, or a block that failed a binding check and was still shown to the model unchanged. The `type` field says which.

One of the following:



BetaIterationsUsage = array of [BetaMessageIterationUsage](/docs/en/api/http/beta/messages#beta_message_iteration_usage) or [BetaCompactionIterationUsage](/docs/en/api/http/beta/messages#beta_compaction_iteration_usage) or [BetaAdvisorMessageIterationUsage](/docs/en/api/http/beta/messages#beta_advisor_message_iteration_usage) or [BetaFallbackMessageIterationUsage](/docs/en/api/http/beta/messages#beta_fallback_message_iteration_usage)



Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics, discriminated by `type`. For `message` entries (model sampling iterations, such as the turns of a server-side tool use loop), this allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the context window size from the last `message` entry
- Understand token accumulation across server-side tool use loops

A `compaction` entry reports the token usage of the compaction operation itself — the server-side request that summarizes the context being closed — NOT the size of the context that was compacted away, and its token counts can be much smaller than that closed context (for example, a compaction that closes a ~200k-token context can report only a few thousand tokens). Do not derive the context window size from a `compaction` entry, even when it is the last entry. A `compaction` entry's tokens are not included in the top-level `usage` fields. When an input-token trigger is in effect (the default — 150,000 tokens unless configured otherwise), each `compaction` entry closes a context that had reached at least that threshold, though the context can exceed it by the final iteration's output and tool results.

One of the following:



BetaJSONOutputFormat object{ type: "json_schema", schema }



type: "json_schema"



schema: map\[unknown\]



The JSON schema of the format



BetaMCPTool object{ input_schema, name, description }



A tool as an MCP server lists it: its name on that server, its description, and its input schema.

input_schema: map\[unknown\]



name: string



description: optional string





BetaMCPToolConfig object{ defer_loading, enabled }



Configuration for a specific tool in an MCP toolset.

defer_loading: optional boolean



enabled: optional boolean





BetaMCPToolDefaultConfig object{ defer_loading, enabled }



Default configuration for tools in an MCP toolset.

defer_loading: optional boolean



enabled: optional boolean





BetaMCPToolListingBlock object{ type: "mcp_tool_listing", mcp_server_name, tools }



The tool listing the server fetched from an MCP server while producing this response. Send the assistant message back unchanged, this block included, so later requests use this listing instead of asking the MCP server again.



type: "mcp_tool_listing"



defaultmcp_tool_listing

mcp_server_name: string





tools: array of [BetaMCPTool](/docs/en/api/http/beta/messages#beta_mcp_tool) { input_schema, name, description }



input_schema: map\[unknown\]



name: string



description: optional string





BetaMCPToolListingBlockParam object{ type: "mcp_tool_listing", mcp_server_name, tools }



The tool listing an MCP server returned while an earlier response was produced, as that response carried it. Send the assistant message back unchanged, this block included, and the server uses this listing for the matching `mcp_toolset` instead of asking the MCP server again.

type: "mcp_tool_listing"





mcp_server_name: string



The name of the MCP server this listing came from, as `mcp_servers` declares it.

minLength1

maxLength255



tools: array of [BetaMCPToolParam](/docs/en/api/http/beta/messages#beta_mcp_tool_param) { input_schema, name, description }



The server's tools, exactly as the response listed them.

input_schema: map\[unknown\]



The tool's input schema as the MCP server lists it, verbatim.



name: string



The tool's name as the MCP server lists it (not prefixed with the server name).

minLength1

description: optional string or null



The tool's description as the MCP server lists it.



BetaMCPToolParam object{ input_schema, name, description }



A tool as an MCP server lists it: its name on that server, its description, and its input schema.

input_schema: map\[unknown\]



The tool's input schema as the MCP server lists it, verbatim.



name: string



The tool's name as the MCP server lists it (not prefixed with the server name).

minLength1

description: optional string or null



The tool's description as the MCP server lists it.



BetaMCPToolResultBlock object{ type: "mcp_tool_result", content, is_error, tool_use_id }





BetaMCPToolUseBlock object{ type: "mcp_tool_use", id, input, 2 more }





type: "mcp_tool_use"



defaultmcp_tool_use



id: string



pattern^\[a-zA-Z0-9\_-\]+\$

input: map\[unknown\]



name: string



The name of the MCP tool

server_name: string



The name of the MCP server



BetaMCPToolUseBlockParam object{ type: "mcp_tool_use", id, input, 3 more }





BetaMCPToolset object{ type: "mcp_toolset", mcp_server_name, cache_control, 3 more }



Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.



BetaMemoryTool20250818 object{ type: "memory_20250818", name, allowed_callers, 4 more }





BetaMemoryTool20250818Command = [BetaMemoryTool20250818ViewCommand](/docs/en/api/http/beta/messages#beta_memory_tool_20250818_view_command) or [BetaMemoryTool20250818CreateCommand](/docs/en/api/http/beta/messages#beta_memory_tool_20250818_create_command) or [BetaMemoryTool20250818StrReplaceCommand](/docs/en/api/http/beta/messages#beta_memory_tool_20250818_str_replace_command) or 3 more



One of the following:



BetaMemoryTool20250818CreateCommand object{ command, file_text, path }





command: "create"



Command type identifier

defaultcreate

file_text: string



Content to write to the file

path: string



Path where the file should be created



BetaMemoryTool20250818DeleteCommand object{ command, path }





command: "delete"



Command type identifier

defaultdelete

path: string



Path to the file or directory to delete



BetaMemoryTool20250818InsertCommand object{ command, insert_line, insert_text, path }





command: "insert"



Command type identifier

defaultinsert



insert_line: number



Line number where text should be inserted

minimum1

insert_text: string



Text to insert at the specified line

path: string



Path to the file where text should be inserted



BetaMemoryTool20250818RenameCommand object{ command, new_path, old_path }





command: "rename"



Command type identifier

defaultrename

new_path: string



New path for the file or directory

old_path: string



Current path of the file or directory



BetaMemoryTool20250818StrReplaceCommand object{ command, new_str, old_str, path }





command: "str_replace"



Command type identifier

defaultstr_replace

new_str: string



Text to replace with

old_str: string



Text to search for and replace

path: string



Path to the file where text should be replaced



BetaMemoryTool20250818ViewCommand object{ command, path, view_range }





command: "view"



Command type identifier

defaultview

path: string



Path to directory or file to view



view_range: optional array of number



Optional line range for viewing specific lines

minItems2

maxItems2



BetaMessage object{ type: "message", id, container, 10 more }





BetaMessageDeltaUsage object{ cache_creation_input_tokens, cache_read_input_tokens, fallback_credit, 5 more }





BetaMessageIterationUsage object{ type: "message", cache_creation, cache_creation_input_tokens, 4 more }



Token usage for a sampling iteration.



BetaMessageParam object{ content, role, clear_at, output_config }





BetaMessageTokensCount object{ context_management, input_tokens }





context_management: [BetaCountTokensContextManagementResponse](/docs/en/api/http/beta/messages#beta_count_tokens_context_management_response) { original_input_tokens } or null



Information about context management applied to the message.

original_input_tokens: number



The original token count before context management was applied

input_tokens: number



The total number of tokens across the provided list of messages, system prompt, and tools.



BetaMetadata object{ user_id }





user_id: optional string or null



An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



BetaOutputConfig object{ effort, format, task_budget }





BetaOutputTokensDetails object{ thinking_tokens }





thinking_tokens: number



Number of output tokens the model generated as internal reasoning, including the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter) summarized thinking text returned in the response body. Computed by re-tokenizing the raw reasoning text, so it may differ from the model's exact generation count by a small number of tokens. Always ≤ `output_tokens`; `output_tokens - thinking_tokens` approximates the non-reasoning output.

default0

minimum0



BetaPlainTextSource object{ type: "text", data, media_type }



type: "text"



data: string



media_type: "text/plain"





BetaRawContentBlockDelta = [BetaTextDelta](/docs/en/api/http/beta/messages#beta_text_delta) or [BetaInputJSONDelta](/docs/en/api/http/beta/messages#beta_input_json_delta) or [BetaCitationsDelta](/docs/en/api/http/beta/messages#beta_citations_delta) or 3 more



One of the following:



BetaRawContentBlockDeltaEvent object{ type: "content_block_delta", delta, index }





type: "content_block_delta"



defaultcontent_block_delta



delta: [BetaRawContentBlockDelta](/docs/en/api/http/beta/messages#beta_raw_content_block_delta)



One of the following:

index: number





BetaRawContentBlockStartEvent object{ type: "content_block_start", content_block, index }





BetaRawContentBlockStopEvent object{ type: "content_block_stop", index }





type: "content_block_stop"



defaultcontent_block_stop

index: number





BetaRawMessageDeltaEvent object{ type: "message_delta", context_management, delta, 2 more }





BetaRawMessageStartEvent object{ type: "message_start", message }





type: "message_start"



defaultmessage_start



message: [BetaMessage](/docs/en/api/http/beta/messages#beta_message) { type: "message", id, container, 10 more }





BetaRawMessageStopEvent object{ type: "message_stop" }





type: "message_stop"



defaultmessage_stop



BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](/docs/en/api/http/beta/messages#beta_raw_message_start_event) or [BetaRawMessageDeltaEvent](/docs/en/api/http/beta/messages#beta_raw_message_delta_event) or [BetaRawMessageStopEvent](/docs/en/api/http/beta/messages#beta_raw_message_stop_event) or 3 more



One of the following:



BetaRedactedThinkingBlock object{ type: "redacted_thinking", data }

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

BetaRedactedThinkingBlockParam object{ type: "redacted_thinking", data }



type: "redacted_thinking"



data: string



The `data` value of this redacted thinking block, exactly as returned by the API in a previous response. Opaque and encrypted; pass it back unchanged.



BetaRefusalStopDetails object{ type: "refusal", category, explanation, 3 more }



Structured information about a refusal.



BetaRequestDocumentBlock object{ type: "document", source, cache_control, 3 more }





BetaRequestMCPServerToolConfiguration object{ allowed_tools, enabled }



allowed_tools: optional array of string or null



enabled: optional boolean or null





BetaRequestMCPServerURLDefinition object{ type: "url", name, url, 2 more }



type: "url"



name: string



url: string



authorization_token: optional string or null





tool_configuration: optional [BetaRequestMCPServerToolConfiguration](/docs/en/api/http/beta/messages#beta_request_mcp_server_tool_configuration) { allowed_tools, enabled } or null



allowed_tools: optional array of string or null



enabled: optional boolean or null





BetaRequestMCPToolResultBlockParam object{ type: "mcp_tool_result", tool_use_id, cache_control, 2 more }





BetaRequestToolAdditionBlock object{ type: "tool_addition", tool, cache_control }



Mid-conversation directive to make a tool available.

`tool` is a reference to a tool (or MCP toolset) declared in the request's `tools`. Under the `inline-tools-2026-09-15` beta it may instead be a reference to a tool defined earlier in `messages`, or a `tool_definition` object that carries an inline tool definition in `definition` (the same object a `tools` entry holds). An `mcp_toolset` definition also requires the `mcp-client-2026-09-15` beta. The tool is offered to the model from this point in the conversation onward.



BetaRequestToolRemovalBlock object{ type: "tool_removal", tool, cache_control }



Mid-conversation directive to withdraw a tool.

`tool` references a tool (or MCP toolset) by name: one declared in the request's `tools` or defined earlier in `messages`. It is no longer offered to the model from this point in the conversation onward.



BetaResponseTool object{ type, input_schema, name, 6 more }



A custom tool definition, as sent.



BetaResponseToolAdditionBlock object{ type: "tool_addition", tool }



An entry of a `compaction` block's `tool_changes`: a tool the compacted range made available, as a reference to a `tools` entry or MCP toolset, or as the tool definition in effect at the end of the range, by value. Send it back unchanged.



BetaResponseToolChangeMCPToolReference object{ type: "mcp_tool_reference", name, server_name }



Reference to a single MCP tool, by its server and its name on that server, as a `compaction` block's `tool_changes` entry reports it. Send it back unchanged with the block.



type: "mcp_tool_reference"



defaultmcp_tool_reference

name: string



server_name: string





BetaResponseToolChangeMCPToolsetReference object{ type: "mcp_toolset_reference", server_name }



Reference to every tool in the named MCP server's toolset, as a `compaction` block's `tool_changes` entry reports it. Send it back unchanged with the block.



type: "mcp_toolset_reference"



defaultmcp_toolset_reference

server_name: string





BetaResponseToolChangeToolReference object{ type: "tool_reference", name }



Reference to a single tool, by the name the model uses to call it, as a `compaction` block's `tool_changes` entry reports it: a tool declared in `tools` or defined by an earlier `tool_addition` block. Send it back unchanged with the block.



type: "tool_reference"



defaulttool_reference

name: string





BetaResponseToolInputSchema object{ type: "object", properties, required }



[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"



properties: optional map\[unknown\] or null



required: optional array of string or null





BetaResponseToolRemovalBlock object{ type: "tool_removal", tool }



An entry of a `compaction` block's `tool_changes`: a tool of the request's `tools` (or an MCP tool or toolset) that the compacted range withdrew. Send it back unchanged.



BetaResponseToolUnion = [BetaResponseTool](/docs/en/api/http/beta/messages#beta_response_tool) or [BetaToolBash20241022](/docs/en/api/http/beta/messages#beta_tool_bash_20241022) or [BetaToolBash20250124](/docs/en/api/http/beta/messages#beta_tool_bash_20250124) or 25 more



One of the following:



BetaSearchResultBlockParam object{ type: "search_result", content, source, 3 more }





BetaServerToolCaller object{ type: "code_execution_20250825", tool_id }



Tool invocation generated by a server-side tool.

type: "code_execution_20250825"





tool_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



BetaServerToolCaller20260120 object{ type: "code_execution_20260120", tool_id }



type: "code_execution_20260120"





tool_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



BetaServerToolUsage object{ web_fetch_requests, web_search_requests }

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

BetaServerToolUseBlock object{ type: "server_tool_use", id, input, 2 more }





BetaServerToolUseBlockParam object{ type: "server_tool_use", id, input, 3 more }





BetaSignatureDelta object{ type: "signature_delta", signature }





type: "signature_delta"



defaultsignature_delta

signature: string



The `signature` for this thinking block: an opaque value used to verify that the block was generated by Claude when it is passed back to the API. Delivered in a `signature_delta` event just before the block's `content_block_stop` event.



BetaSkillParams object{ type, skill_id, version }

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

BetaStopReason = "end_turn" or "max_tokens" or "stop_sequence" or 5 more

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

"compaction"



"refusal"



"model_context_window_exceeded"





BetaSummarizeCompaction object{ type: "summarize", instructions }



Compact the whole conversation and return a signed `compaction` block, alone, that a later request sends back first in `messages`, in place of the messages it summarizes. There is no trigger and no pause flag: sending the parameter compacts, and nothing is sampled after the block.

The summarization prompt is the server's own unless `instructions` are given, which then replace it for this request; a value that is empty or only whitespace counts as absent.

type: "summarize"





instructions: optional string or null



Replaces the server's default summarization prompt for this request. An empty or whitespace-only value counts as absent.

maxLength16384



BetaSystemMessageOutputConfig object{ effort }



Per-message output configuration on a role:"system" input message.

Fields here apply per-turn; `format` remains top-level only. An empty `{}` is accepted on a message that carries content; a message with neither content nor output_config fields is rejected.

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

BetaTextBlock object{ type: "text", citations, text }





BetaTextBlockParam object{ type: "text", text, cache_control, citations }





BetaTextCitation = [BetaCitationCharLocation](/docs/en/api/http/beta/messages#beta_citation_char_location) or [BetaCitationPageLocation](/docs/en/api/http/beta/messages#beta_citation_page_location) or [BetaCitationContentBlockLocation](/docs/en/api/http/beta/messages#beta_citation_content_block_location) or 2 more



One of the following:



BetaTextCitationParam = [BetaCitationCharLocationParam](/docs/en/api/http/beta/messages#beta_citation_char_location_param) or [BetaCitationPageLocationParam](/docs/en/api/http/beta/messages#beta_citation_page_location_param) or [BetaCitationContentBlockLocationParam](/docs/en/api/http/beta/messages#beta_citation_content_block_location_param) or 2 more



One of the following:



BetaTextDelta object{ type: "text_delta", text }





type: "text_delta"



defaulttext_delta

text: string





BetaTextEditorCodeExecutionCreateResultBlock object{ type: "text_editor_code_execution_create_result", is_file_update }





type: "text_editor_code_execution_create_result"



defaulttext_editor_code_execution_create_result

is_file_update: boolean





BetaTextEditorCodeExecutionCreateResultBlockParam object{ type: "text_editor_code_execution_create_result", is_file_update }



type: "text_editor_code_execution_create_result"



is_file_update: boolean





BetaTextEditorCodeExecutionStrReplaceResultBlock object{ type: "text_editor_code_execution_str_replace_result", lines, new_lines, 3 more }

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

BetaTextEditorCodeExecutionStrReplaceResultBlockParam object{ type: "text_editor_code_execution_str_replace_result", lines, new_lines, 3 more }

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

BetaTextEditorCodeExecutionToolResultBlock object{ type: "text_editor_code_execution_tool_result", content, tool_use_id }





BetaTextEditorCodeExecutionToolResultBlockParam object{ type: "text_editor_code_execution_tool_result", content, tool_use_id, cache_control }





BetaTextEditorCodeExecutionToolResultError object{ type: "text_editor_code_execution_tool_result_error", error_code, error_message }





type: "text_editor_code_execution_tool_result_error"



defaulttext_editor_code_execution_tool_result_error



error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

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

BetaTextEditorCodeExecutionToolResultErrorParam object{ type: "text_editor_code_execution_tool_result_error", error_code, error_message }



type: "text_editor_code_execution_tool_result_error"





error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or 2 more

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

BetaTextEditorCodeExecutionViewResultBlock object{ type: "text_editor_code_execution_view_result", content, file_type, 3 more }

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

BetaTextEditorCodeExecutionViewResultBlockParam object{ type: "text_editor_code_execution_view_result", content, file_type, 3 more }

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

BetaThinkingBlock object{ type: "thinking", signature, thinking }

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

BetaThinkingBlockBinding object{ prefix_mismatch_behavior }



Controls for block binding: what happens when a thinking block this request sends back fails the conversation check. Every field is optional; an empty object means every default.



prefix_mismatch_behavior: optional [BetaThinkingPrefixMismatchBehavior](/docs/en/api/http/beta/messages#beta_thinking_prefix_mismatch_behavior) or null



"error" (default) \| "drop_block". What happens when a thinking block in `messages` fails the conversation check (it was created in a different conversation, or the messages before it have changed since). "error" fails the request with a 400 error. "drop_block" removes the failing blocks and the request proceeds; each removal is reported in `input_transformations`.

One of the following:

"error"



"drop_block"





BetaThinkingBlockParam object{ type: "thinking", signature, thinking }

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

BetaThinkingConfigAdaptive object{ type: "adaptive", block_binding, display }



type: "adaptive"





block_binding: optional [BetaThinkingBlockBinding](/docs/en/api/http/beta/messages#beta_thinking_block_binding) { prefix_mismatch_behavior } or null



Controls for block binding: what happens when a thinking block this request sends back fails the conversation check. `null`, absent or an empty object means every default.



prefix_mismatch_behavior: optional [BetaThinkingPrefixMismatchBehavior](/docs/en/api/http/beta/messages#beta_thinking_prefix_mismatch_behavior) or null



"error" (default) \| "drop_block". What happens when a thinking block in `messages` fails the conversation check (it was created in a different conversation, or the messages before it have changed since). "error" fails the request with a 400 error. "drop_block" removes the failing blocks and the request proceeds; each removal is reported in `input_transformations`.

One of the following:

"error"



"drop_block"





display: optional "summarized" or "omitted" or "updates" or null



Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"



"omitted"



"updates"





BetaThinkingConfigDisabled object{ type: "disabled" }



type: "disabled"





BetaThinkingConfigEnabled object{ type: "enabled", budget_tokens, block_binding, display }





BetaThinkingConfigParam = [BetaThinkingConfigEnabled](/docs/en/api/http/beta/messages#beta_thinking_config_enabled) or [BetaThinkingConfigDisabled](/docs/en/api/http/beta/messages#beta_thinking_config_disabled) or [BetaThinkingConfigAdaptive](/docs/en/api/http/beta/messages#beta_thinking_config_adaptive)



Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) for details.

One of the following:



BetaThinkingDelta object{ type: "thinking_delta", estimated_tokens, thinking }





type: "thinking_delta"



defaultthinking_delta

estimated_tokens: number or null



Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: string



The incremental `thinking` text for this content block. Concatenate the `thinking` values of successive `thinking_delta` events to assemble the block's full `thinking` value.



BetaThinkingDroppedInputTransformation object{ type: "thinking_dropped", path, reason }





type: "thinking_dropped"



Always `thinking_dropped` for this entry type.

defaultthinking_dropped

path: string



Where the removed block was in your request, as `messages.{i}.content.{j}`: `i` indexes the `messages` array you sent and `j` that message's `content` array — the same form error messages use.



reason: "model_binding_mismatch" or "prefix_binding_mismatch" or "organization_binding_mismatch" or "end_user_binding_mismatch"



Which binding check removed the block: `model_binding_mismatch` — it was created by a model whose reasoning the requested model may not read; `prefix_binding_mismatch` — the conversation before it differs from the conversation it was created in (the rest of that turn's consecutive thinking blocks are removed with it, each with this reason); `organization_binding_mismatch` — it was created under a different organization (an Anthropic organization, AWS account or Google Cloud project) and this organization is not one of its additional organizations; `end_user_binding_mismatch` — it was created for a different end user, or was removed by the consumer-organization binding. A block that would fail several checks reports one reason, in this order of precedence: `organization_binding_mismatch`, `end_user_binding_mismatch`, `model_binding_mismatch`, `prefix_binding_mismatch`.

One of the following:

"model_binding_mismatch"



"prefix_binding_mismatch"



"organization_binding_mismatch"



"end_user_binding_mismatch"





BetaThinkingMismatchAllowedInputTransformation object{ type: "thinking_mismatch_allowed", path, reason }





type: "thinking_mismatch_allowed"



Always `thinking_mismatch_allowed` for this entry type.

defaultthinking_mismatch_allowed

path: string



Where the block is in your request, as `messages.{i}.content.{j}`: `i` indexes the `messages` array you sent and `j` that message's `content` array — the same form error messages use.



reason: "model_binding_mismatch" or "prefix_binding_mismatch" or "organization_binding_mismatch" or "end_user_binding_mismatch"



Which binding check the block failed; the block was shown to the model all the same. Always `prefix_binding_mismatch` today — the conversation before the block differs from the conversation it was created in, or the block carries no record of one on a model that requires it. Were the check enforced for this request, the block would have been removed or the request rejected (`thinking.block_binding.prefix_mismatch_behavior`). A removal also takes the rest of that turn's consecutive thinking blocks, whereas here each block is checked on its own, so `thinking_mismatch_allowed` entries are a lower bound on what enforcement would remove.

One of the following:

"model_binding_mismatch"



"prefix_binding_mismatch"



"organization_binding_mismatch"



"end_user_binding_mismatch"





BetaThinkingPrefixMismatchBehavior = "error" or "drop_block"



What happens when a thinking block in `messages` fails the conversation check: it was created in a different conversation, or the messages before it have changed since. `"error"` (the default) fails the request with a 400 error. `"drop_block"` removes the failing blocks and the request proceeds; the model no longer sees the dropped reasoning.

One of the following:

"error"



"drop_block"





BetaThinkingTurns object{ type: "thinking_turns", value }



type: "thinking_turns"





value: number



minimum1



BetaTokenTaskBudget object{ type: "tokens", total, remaining }



User-configurable total token budget across contexts.

type: "tokens"



The budget type. Currently only 'tokens' is supported.



total: number



Total token budget across all contexts in the session.

minimum1024



remaining: optional number or null



Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.

minimum0



BetaTool object{ type, input_schema, name, 7 more }





BetaToolBash20241022 object{ type: "bash_20241022", name, allowed_callers, 4 more }





BetaToolBash20250124 object{ type: "bash_20250124", name, allowed_callers, 4 more }





BetaToolChangeMCPToolReference object{ type: "mcp_tool_reference", name, server_name }



Reference to a single MCP tool by its server and remote name; the same `server_name`/`name` pair `mcp_tool_use` carries.

type: "mcp_tool_reference"



name: string



server_name: string





BetaToolChangeMCPToolsetReference object{ type: "mcp_toolset_reference", server_name }



Reference to every tool in the named MCP server's toolset.

type: "mcp_toolset_reference"



server_name: string





BetaToolChangeToolDefinition object{ type: "tool_definition", definition }



A tool defined by value, as a `compaction` block's `tool_changes` entry reports it: `definition` is the tool's definition as it was sent, in the form of a `tools` entry, without `cache_control`. Send it back unchanged with the block.



type: "tool_definition"



defaulttool_definition



definition: [BetaResponseToolUnion](/docs/en/api/http/beta/messages#beta_response_tool_union)



One of the following:



BetaToolChangeToolDefinitionParam object{ type: "tool_definition", definition }



A tool defined by value: `definition` is a `tools` entry (any kind `tools` accepts, an MCP toolset included). An `mcp_toolset` given here also requires the `mcp-client-2026-09-15` beta.

type: "tool_definition"





definition: [BetaToolUnion](/docs/en/api/http/beta/messages#beta_tool_union)



One of the following:



BetaToolChangeToolReference object{ type: "tool_reference", name }



Reference to a single tool, by the name the model uses to call it: a tool declared in `tools` or defined by an earlier `tool_addition` block. Does not accept the composed `{server}_{name}` form the server assigns to MCP-resolved tools; use `mcp_tool_reference` or `mcp_toolset_reference` for those.

type: "tool_reference"





name: string



pattern^\[a-zA-Z0-9\_-\]{1,128}\$



BetaToolChoice = [BetaToolChoiceAuto](/docs/en/api/http/beta/messages#beta_tool_choice_auto) or [BetaToolChoiceAny](/docs/en/api/http/beta/messages#beta_tool_choice_any) or [BetaToolChoiceTool](/docs/en/api/http/beta/messages#beta_tool_choice_tool) or [BetaToolChoiceNone](/docs/en/api/http/beta/messages#beta_tool_choice_none)



How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



BetaToolChoiceAny object{ type: "any", disable_parallel_tool_use }

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

BetaToolChoiceAuto object{ type: "auto", disable_parallel_tool_use }

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

BetaToolChoiceNone object{ type: "none" }



The model will not be allowed to use tools.

type: "none"





BetaToolChoiceTool object{ type: "tool", name, disable_parallel_tool_use }

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

BetaToolComputerUse20241022 object{ type: "computer_20241022", display_height_px, display_width_px, 7 more }





BetaToolComputerUse20250124 object{ type: "computer_20250124", display_height_px, display_width_px, 7 more }





BetaToolComputerUse20251124 object{ type: "computer_20251124", display_height_px, display_width_px, 8 more }





BetaToolReferenceBlock object{ type: "tool_reference", tool_name }

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

BetaToolReferenceBlockParam object{ type: "tool_reference", tool_name, cache_control }

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

cache_control: optional [BetaCacheControlEphemeral](/docs/en/api/http/beta/messages#beta_cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

BetaToolResultBlockParam object{ type: "tool_result", tool_use_id, cache_control, 3 more }





BetaToolSearchToolBm25_20251119 object{ type, name, allowed_callers, 3 more }





BetaToolSearchToolRegex20251119 object{ type, name, allowed_callers, 3 more }





BetaToolSearchToolResultBlock object{ type: "tool_search_tool_result", content, tool_use_id }





BetaToolSearchToolResultBlockParam object{ type: "tool_search_tool_result", content, tool_use_id, cache_control }





BetaToolSearchToolResultError object{ type: "tool_search_tool_result_error", error_code, error_message }





type: "tool_search_tool_result_error"



defaulttool_search_tool_result_error



error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

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

BetaToolSearchToolResultErrorParam object{ type: "tool_search_tool_result_error", error_code, error_message }



type: "tool_search_tool_result_error"





error_code: "invalid_tool_input" or "unavailable" or "too_many_requests" or "execution_time_exceeded"

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

BetaToolSearchToolSearchResultBlock object{ type: "tool_search_tool_search_result", tool_references }





type: "tool_search_tool_search_result"



defaulttool_search_tool_search_result



tool_references: array of [BetaToolReferenceBlock](/docs/en/api/http/beta/messages#beta_tool_reference_block) { type: "tool_reference", tool_name }

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

BetaToolSearchToolSearchResultBlockParam object{ type: "tool_search_tool_search_result", tool_references }





BetaToolTextEditor20241022 object{ type: "text_editor_20241022", name, allowed_callers, 4 more }





BetaToolTextEditor20250124 object{ type: "text_editor_20250124", name, allowed_callers, 4 more }





BetaToolTextEditor20250429 object{ type: "text_editor_20250429", name, allowed_callers, 4 more }





BetaToolTextEditor20250728 object{ type: "text_editor_20250728", name, allowed_callers, 5 more }





BetaToolUnion = [BetaTool](/docs/en/api/http/beta/messages#beta_tool) or [BetaToolBash20241022](/docs/en/api/http/beta/messages#beta_tool_bash_20241022) or [BetaToolBash20250124](/docs/en/api/http/beta/messages#beta_tool_bash_20250124) or 25 more



One of the following:



BetaToolUseBlock object{ type: "tool_use", id, input, 3 more }





BetaToolUseBlockParam object{ type: "tool_use", id, input, 4 more }





BetaToolUsesKeep object{ type: "tool_uses", value }



type: "tool_uses"





value: number



minimum0



BetaToolUsesTrigger object{ type: "tool_uses", value }



type: "tool_uses"





value: number



minimum1



BetaURLImageSource object{ type: "url", url }



type: "url"



url: string





BetaURLPDFSource object{ type: "url", url }



type: "url"



url: string





BetaUsage object{ cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 9 more }





BetaUserLocation object{ type: "approximate", city, country, 2 more }

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

BetaWebFetchBlock object{ type: "web_fetch_result", content, retrieved_at, url }





type: "web_fetch_result"



defaultweb_fetch_result



content: [BetaDocumentBlock](/docs/en/api/http/beta/messages#beta_document_block) { type: "document", citations, source, title }



retrieved_at: string or null



ISO 8601 timestamp when the content was retrieved

url: string



Fetched content URL



BetaWebFetchBlockParam object{ type: "web_fetch_result", content, url, retrieved_at }



type: "web_fetch_result"





content: [BetaRequestDocumentBlock](/docs/en/api/http/beta/messages#beta_request_document_block) { type: "document", source, cache_control, 3 more }



url: string



Fetched content URL

retrieved_at: optional string or null



ISO 8601 timestamp when the content was retrieved



BetaWebFetchTool20250910 object{ type: "web_fetch_20250910", name, allowed_callers, 9 more }





BetaWebFetchTool20260209 object{ type: "web_fetch_20260209", name, allowed_callers, 9 more }





BetaWebFetchTool20260309 object{ type: "web_fetch_20260309", name, allowed_callers, 10 more }



Web fetch tool with use_cache parameter for bypassing cached content.



BetaWebFetchTool20260318 object{ type: "web_fetch_20260318", name, allowed_callers, 11 more }





BetaWebFetchToolResultBlock object{ type: "web_fetch_tool_result", content, tool_use_id, caller }





BetaWebFetchToolResultBlockParam object{ type: "web_fetch_tool_result", content, tool_use_id, 2 more }





BetaWebFetchToolResultErrorBlock object{ type: "web_fetch_tool_result_error", error_code }





type: "web_fetch_tool_result_error"



defaultweb_fetch_tool_result_error



error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/http/beta/messages#beta_web_fetch_tool_result_error_code)

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

BetaWebFetchToolResultErrorBlockParam object{ type: "web_fetch_tool_result_error", error_code }



type: "web_fetch_tool_result_error"





error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/http/beta/messages#beta_web_fetch_tool_result_error_code)

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

BetaWebFetchToolResultErrorCode = "invalid_tool_input" or "url_too_long" or "url_not_allowed" or 7 more

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

BetaWebFetchURLSourceAll object{ type: "all" }



The `url_sources` variant under which a source contributes in full: every result of the tool filter's source, or all user input.

type: "all"





BetaWebFetchURLSourceExcept object{ type: "except", tools }



The tool filter variant under which every result but the named tools' contributes.

type: "except"





tools: array of [BetaWebFetchURLSourceToolReference](/docs/en/api/http/beta/messages#beta_web_fetch_url_source_tool_reference) { type: "tool_reference", name }



type: "tool_reference"



name: string





BetaWebFetchURLSourceNone object{ type: "none" }



The `url_sources` variant under which a source contributes nothing: no result of the tool filter's source, or no user input.

type: "none"





BetaWebFetchURLSourceOnly object{ type: "only", tools }



The tool filter variant under which only the named tools' results contribute.

type: "only"





tools: array of [BetaWebFetchURLSourceToolReference](/docs/en/api/http/beta/messages#beta_web_fetch_url_source_tool_reference) { type: "tool_reference", name }



type: "tool_reference"



name: string





BetaWebFetchURLSourceToolReference object{ type: "tool_reference", name }



One entry of a tool filter's `tools`: it must name a tool declared in this request's `tools[]`.

type: "tool_reference"



name: string





BetaWebFetchURLSources object{ client_tool_results, server_tool_results, user_input }



Which sources contribute to the set of URLs web fetch may fetch.

Each key is a tagged variant: `user_input` is `all` or `none`; the two tool filters are `all`, `none`, `only` (only the named tools' results) or `except` (every result but the named tools'). A named tool must be declared in this request's `tools[]`.



BetaWebSearchResultBlock object{ type: "web_search_result", encrypted_content, page_age, 2 more }

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

BetaWebSearchResultBlockParam object{ type: "web_search_result", encrypted_content, title, 2 more }

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

BetaWebSearchTool20250305 object{ type: "web_search_20250305", name, allowed_callers, 7 more }





BetaWebSearchTool20260209 object{ type: "web_search_20260209", name, allowed_callers, 7 more }





BetaWebSearchTool20260318 object{ type: "web_search_20260318", name, allowed_callers, 8 more }





BetaWebSearchToolRequestError object{ type: "web_search_tool_result_error", error_code }



type: "web_search_tool_result_error"





error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/http/beta/messages#beta_web_search_tool_result_error_code)

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

BetaWebSearchToolResultBlock object{ type: "web_search_tool_result", content, tool_use_id, caller }





BetaWebSearchToolResultBlockContent = [BetaWebSearchToolResultError](/docs/en/api/http/beta/messages#beta_web_search_tool_result_error) or array of [BetaWebSearchResultBlock](/docs/en/api/http/beta/messages#beta_web_search_result_block)



One of the following:



BetaWebSearchToolResultBlockParam object{ type: "web_search_tool_result", content, tool_use_id, 2 more }





BetaWebSearchToolResultBlockParamContent = array of [BetaWebSearchResultBlockParam](/docs/en/api/http/beta/messages#beta_web_search_result_block_param) or [BetaWebSearchToolRequestError](/docs/en/api/http/beta/messages#beta_web_search_tool_request_error)



One of the following:



BetaWebSearchToolResultError object{ type: "web_search_tool_result_error", error_code }





type: "web_search_tool_result_error"



defaultweb_search_tool_result_error



error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/http/beta/messages#beta_web_search_tool_result_error_code)

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

BetaWebSearchToolResultErrorCode = "invalid_tool_input" or "unavailable" or "max_uses_exceeded" or 3 more

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

#### Messages[Batches](/docs/en/api/http/beta/messages/batches)

##### [Create a Message Batch](/docs/en/api/http/beta/messages/batches/create)

POST/v1/messages/batches

Send a batch of Message creation requests.

##### [Retrieve a Message Batch](/docs/en/api/http/beta/messages/batches/retrieve)

GET/v1/messages/batches/{message_batch_id}

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

##### [List Message Batches](/docs/en/api/http/beta/messages/batches/list)

GET/v1/messages/batches

List all Message Batches within a Workspace. Most recently created batches are returned first.

##### [Cancel a Message Batch](/docs/en/api/http/beta/messages/batches/cancel)

POST/v1/messages/batches/{message_batch_id}/cancel

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

##### [Delete a Message Batch](/docs/en/api/http/beta/messages/batches/delete)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/http/beta/messages/batches/results)

GET/v1/messages/batches/{message_batch_id}/results

Streams the results of a Message Batch as a `.jsonl` file.
