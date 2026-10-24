---
title: "Messages - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/messages"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-10-20T06:40:04Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fmessages)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](overview.md)[Beta headers](beta-headers.md)[Errors](errors.md)


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


Organization


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

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles

Plugins

Plugin Marketplaces

Telemetry Destinations


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


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


Completions


Create a Text Completion Deprecated

OpenTelemetry

[Spans](opentelemetry-spans.md)

Support & configuration

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/playground.md)

Copy page



cURL



A beta version of this API exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-messages.md).

1.  [API reference](http.md)

# Messages

Copy page



cURL

##### [Create a Message](https://platform.claude.com/docs/en/api/http/messages/create)

POST/v1/messages

Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.

##### [Count tokens in a Message](https://platform.claude.com/docs/en/api/http/messages/count_tokens)

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

content: array of [BashCodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/http/messages#bash_code_execution_output_block) { type: "bash_code_execution_output", file_id }

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

content: array of [BashCodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/http/messages#bash_code_execution_output_block_param) { type: "bash_code_execution_output", file_id }

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

error_code: [BashCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#bash_code_execution_tool_result_error_code)

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

error_code: [BashCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#bash_code_execution_tool_result_error_code)

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

BrowserClickTarget = [BrowserCoordinateTarget](https://platform.claude.com/docs/en/api/http/messages#browser_coordinate_target) or [BrowserRefTarget](https://platform.claude.com/docs/en/api/http/messages#browser_ref_target)



Where to act: either a viewport coordinate or an element reference.

One of the following:



BrowserCoordinateTarget object{ type: "coordinate", x, y }



A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot).

type: "coordinate"





x: number



Pixels from the left edge of the viewport.

minimum0



y: number



Pixels from the top edge of the viewport.

minimum0



BrowserRefTarget object{ type: "ref", ref }



An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render.

type: "ref"



ref: string



An element reference (e.g. "ref_7") returned by a prior `read_page` or `find` result.

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

BrowserCloseTabInput object{ tab_id }



Close the tab with the given tab_id.

tab_id: string



The tab to close.



BrowserCloseTabToolUseBlock object{ type: "tool_use", id, caller, 3 more }





BrowserCoordinateTarget object{ type: "coordinate", x, y }



A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot).

type: "coordinate"





x: number



Pixels from the left edge of the viewport.

minimum0



y: number



Pixels from the top edge of the viewport.

minimum0

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

BrowserDoubleClickInput object{ target, modifiers, tab_id }



Double left-click at a viewport coordinate or on an element by reference.



BrowserDoubleClickToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserFileUploadInput object{ target, document_ids, paths, tab_id }



Set the value of a file-input element to one or more files. The target must be an element reference; at least one of paths or document_ids is required.



target: [BrowserRefTarget](https://platform.claude.com/docs/en/api/http/messages#browser_ref_target) { type: "ref", ref }



An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render.

type: "ref"



ref: string



An element reference (e.g. "ref_7") returned by a prior `read_page` or `find` result.



document_ids: optional array of string or null



References to files the harness has staged, for deployments where the browser executor cannot read the caller's filesystem.

minItems1



paths: optional array of string or null



File paths on the browser executor's filesystem.

minItems1

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserFileUploadToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserFindInput object{ query, tab_id }



Find elements matching a natural-language description (e.g. "search bar", "add to cart button") and return up to 20 matches with element references.

query: string



Natural-language description of the element(s) to find.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserFindToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserFormInputInput object{ target, value, tab_id }



Set the value of a form element (input, textarea, select, checkbox). Use a boolean for checkboxes, an option value or text for selects.



target: [BrowserRefTarget](https://platform.claude.com/docs/en/api/http/messages#browser_ref_target) { type: "ref", ref }



An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render.

type: "ref"



ref: string



An element reference (e.g. "ref_7") returned by a prior `read_page` or `find` result.



value: [BrowserFormInputValue](https://platform.claude.com/docs/en/api/http/messages#browser_form_input_value)



The value to set.

One of the following:

string



number



boolean



tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserFormInputToolUseBlock object{ type: "tool_use", id, caller, 3 more }





BrowserFormInputValue = string or number or boolean



One of the following:

string



number



boolean



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

BrowserGetPageTextInput object{ tab_id }



Return the page's visible text content as plain text, prioritizing article content. Suited to articles, documentation, and other text-heavy pages.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserGetPageTextToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserHoldKeyInput object{ duration, text, tab_id }



Hold a key or key chord down for a duration, then release it. Uses the same key names and "+" chord syntax as the key action.



duration: number



Seconds to hold the key down (maximum 30).

minimum0

maximum30

text: string



The key or chord to hold.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserHoldKeyToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserHoverInput object{ target, tab_id }



Move the cursor to a coordinate or element without clicking.



BrowserHoverToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserJavascriptExecInput object{ text, tab_id }



Execute JavaScript in the page context and return the value of the last expression. The code runs with access to the DOM, `window`, and page variables. Write the expression you want evaluated — do NOT use `return`.

text: string



JavaScript to execute in the page context.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserJavascriptExecToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserKeyInput object{ text, repeat, tab_id }



Press a key or key chord. Use "+" to combine modifiers with a key (e.g. "ctrl+a", "cmd+shift+p") and space to sequence presses (e.g. "Backspace Backspace Delete"). Common names like "Return", "Tab", "Escape", "BackSpace" are supported.

text: string



The key, chord, or space-separated sequence to press.



repeat: optional number or null



Number of times to repeat. Default 1.

minimum1

maximum100

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserKeyToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserLeftClickDragInput object{ from, target, tab_id }



Press at `from`, drag to `target`, release. Both must be coordinate targets.



BrowserLeftClickDragToolUseBlock object{ type: "tool_use", id, caller, 3 more }





BrowserLeftClickInput object{ target, modifiers, tab_id }



Left-click at a viewport coordinate or on an element by reference.



BrowserLeftClickToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserLeftMouseDownInput object{ target, tab_id }



Press and hold the left mouse button at a viewport coordinate. Pair with left_mouse_up to perform a custom drag.



target: [BrowserCoordinateTarget](https://platform.claude.com/docs/en/api/http/messages#browser_coordinate_target) { type: "coordinate", x, y }



A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot).

type: "coordinate"





x: number



Pixels from the left edge of the viewport.

minimum0



y: number



Pixels from the top edge of the viewport.

minimum0

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserLeftMouseDownToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserLeftMouseUpInput object{ target, tab_id }



Release the left mouse button at a viewport coordinate.



target: [BrowserCoordinateTarget](https://platform.claude.com/docs/en/api/http/messages#browser_coordinate_target) { type: "coordinate", x, y }



A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot).

type: "coordinate"





x: number



Pixels from the left edge of the viewport.

minimum0



y: number



Pixels from the top edge of the viewport.

minimum0

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserLeftMouseUpToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserListTabsInput object{  }



List all open tabs with each tab's tab_id, title, and URL.



BrowserListTabsToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserMiddleClickInput object{ target, modifiers, tab_id }



Middle-click at a viewport coordinate or on an element by reference.



BrowserMiddleClickToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserMouseMoveInput object{ target, tab_id }



Move the pointer to a viewport coordinate without clicking.



target: [BrowserCoordinateTarget](https://platform.claude.com/docs/en/api/http/messages#browser_coordinate_target) { type: "coordinate", x, y }



A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot).

type: "coordinate"





x: number



Pixels from the left edge of the viewport.

minimum0



y: number



Pixels from the top edge of the viewport.

minimum0

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserMouseMoveToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserNavigateInput object{ url, tab_id }



Navigate to a URL, or go back/forward/reload in history. The protocol may be omitted (defaults to https://).

url: string



The URL to navigate to, or "back" / "forward" / "reload" for history navigation.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserNavigateToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserNewTabInput object{  }



Open a new empty tab and return its tab_id.



BrowserNewTabToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserReadConsoleInput object{ tab_id }



Return console output (log entries, errors, warnings) accumulated since the driver attached to the tab and since the last read, one line per entry. An empty result does not mean no traffic for a tab that predates attach.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserReadConsoleToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserReadNetworkInput object{ tab_id }



Return the network requests (method, URL, status, MIME type, timing) recorded since the driver attached to the tab and since the last read, one line per entry. An empty result does not mean no traffic for a tab that predates attach.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserReadNetworkToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserReadPageFilter = "all" or "interactive"



One of the following:

"all"



"interactive"





BrowserReadPageInput object{ depth, filter, ref, tab_id }



Return a structured accessibility tree of the page (or the subtree rooted at `ref`), with element references like \[ref_7\] that can be used as targets on later actions. Output is capped at 50,000 characters — narrow with `ref` or a smaller `depth` when exceeded.



depth: optional number or null



Maximum tree depth. Default 15.

minimum1



filter: optional [BrowserReadPageFilter](https://platform.claude.com/docs/en/api/http/messages#browser_read_page_filter) or null



Which elements to include. Omitted: every visible element. "interactive": interactive elements only. "all": additionally includes off-viewport elements.

One of the following:

"all"



"interactive"



ref: optional string or null



Element reference to read a subtree from. Omit to read from the page root.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserReadPageToolUseBlock object{ type: "tool_use", id, caller, 3 more }





BrowserRefTarget object{ type: "ref", ref }



An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render.

type: "ref"



ref: string



An element reference (e.g. "ref_7") returned by a prior `read_page` or `find` result.

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

BrowserRightClickInput object{ target, modifiers, tab_id }



Right-click at a viewport coordinate or on an element by reference.



BrowserRightClickToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserScreenshotInput object{ tab_id }



Capture the current browser viewport.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserScreenshotToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserScrollDirection = "up" or "down" or "left" or "right"



One of the following:

"up"



"down"



"left"



"right"





BrowserScrollInput object{ scroll_direction, target, scroll_amount, tab_id }



Scroll at a viewport position. `target` must be a coordinate target.



scroll_direction: [BrowserScrollDirection](https://platform.claude.com/docs/en/api/http/messages#browser_scroll_direction)



One of the following:

"up"



"down"



"left"



"right"





target: [BrowserCoordinateTarget](https://platform.claude.com/docs/en/api/http/messages#browser_coordinate_target) { type: "coordinate", x, y }



A point in the browser viewport, in viewport pixels (the same frame as a full-viewport screenshot).

type: "coordinate"





x: number



Pixels from the left edge of the viewport.

minimum0



y: number



Pixels from the top edge of the viewport.

minimum0



scroll_amount: optional number or null



Scroll-wheel notches (1–10). Default 3.

minimum1

maximum10

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.

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

BrowserScrollToInput object{ target, tab_id }



Scroll an element into view.



target: [BrowserRefTarget](https://platform.claude.com/docs/en/api/http/messages#browser_ref_target) { type: "ref", ref }



An element on the page, identified by a reference from a prior `read_page` or `find` result. References are scoped to the tab that produced them and become stale after navigation or a major re-render.

type: "ref"



ref: string



An element reference (e.g. "ref_7") returned by a prior `read_page` or `find` result.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserScrollToToolUseBlock object{ type: "tool_use", id, caller, 3 more }





BrowserScrollToolUseBlock object{ type: "tool_use", id, caller, 3 more }





BrowserStateBlockParam object{ type: "browser_state", tabs, cache_control, state_changes }



The caller's browser state after a browser toolset member call — the full inventory of open tabs, which tab is active, and any side effects (tabs opened, download state changes) the call produced.

At most one per `tool_result`, only on a non-error result answering a browser toolset member `tool_use`. The server renders the model-visible text from it; the model never sees the raw fields.



BrowserStateChange = [BrowserStateChangeTabOpened](https://platform.claude.com/docs/en/api/http/messages#browser_state_change_tab_opened) or [BrowserStateChangeDownloadStarted](https://platform.claude.com/docs/en/api/http/messages#browser_state_change_download_started) or [BrowserStateChangeDownloadCompleted](https://platform.claude.com/docs/en/api/http/messages#browser_state_change_download_completed) or [BrowserStateChangeDownloadFailed](https://platform.claude.com/docs/en/api/http/messages#browser_state_change_download_failed)

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

BrowserSwitchTabInput object{ tab_id }



Make the tab with the given tab_id the active tab — the tab that actions without a tab_id apply to.

tab_id: string



The tab to switch to.



BrowserSwitchTabToolUseBlock object{ type: "tool_use", id, caller, 3 more }





BrowserToolUseBlock = [BrowserNavigateToolUseBlock](https://platform.claude.com/docs/en/api/http/messages#browser_navigate_tool_use_block) or [BrowserListTabsToolUseBlock](https://platform.claude.com/docs/en/api/http/messages#browser_list_tabs_tool_use_block) or [BrowserNewTabToolUseBlock](https://platform.claude.com/docs/en/api/http/messages#browser_new_tab_tool_use_block) or 28 more



One of the following:

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

BrowserTripleClickInput object{ target, modifiers, tab_id }



Triple left-click at a viewport coordinate or on an element by reference (typically selects a line or paragraph).



BrowserTripleClickToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserTypeInput object{ text, tab_id }



Type a literal string at the current focus.

text: string



The text to type.

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserTypeToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserWaitInput object{ duration, tab_id }



Pause for the given duration.



duration: number



Seconds to wait (maximum 30).

minimum0

maximum30

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserWaitToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

BrowserZoomInput object{ region, tab_id }



Return a cropped screenshot of the given viewport region, scaled up for closer inspection — useful for small icons, buttons, or text. Coordinates are in the same viewport-pixel space as a full screenshot.



region: array of number



\[x0, y0, x1, y1\] in viewport pixels.

minItems4

maxItems4

tab_id: optional string or null



Tab to act on. Defaults to the active tab when omitted.



BrowserZoomToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

Defaults to `5m`. See [prompt caching pricing](../Guides/build-with-claude-prompt-caching.md) for details.

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

CacheMissReason = [CacheMissModelChanged](https://platform.claude.com/docs/en/api/http/messages#cache_miss_model_changed) or [CacheMissSystemChanged](https://platform.claude.com/docs/en/api/http/messages#cache_miss_system_changed) or [CacheMissToolsChanged](https://platform.claude.com/docs/en/api/http/messages#cache_miss_tools_changed) or 3 more

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

content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/http/messages#code_execution_output_block) { type: "code_execution_output", file_id }

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

content: array of [CodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/http/messages#code_execution_output_block_param) { type: "code_execution_output", file_id }

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

content: [CodeExecutionToolResultBlockContent](https://platform.claude.com/docs/en/api/http/messages#code_execution_tool_result_block_content)



One of the following:



tool_use_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



CodeExecutionToolResultBlockContent = [CodeExecutionToolResultError](https://platform.claude.com/docs/en/api/http/messages#code_execution_tool_result_error) or [CodeExecutionResultBlock](https://platform.claude.com/docs/en/api/http/messages#code_execution_result_block) or [EncryptedCodeExecutionResultBlock](https://platform.claude.com/docs/en/api/http/messages#encrypted_code_execution_result_block)



One of the following:



CodeExecutionToolResultBlockParam object{ type: "code_execution_tool_result", content, tool_use_id, cache_control }



type: "code_execution_tool_result"





content: [CodeExecutionToolResultBlockParamContent](https://platform.claude.com/docs/en/api/http/messages#code_execution_tool_result_block_param_content)



One of the following:



tool_use_id: string



pattern^srvtoolu\_\[a-zA-Z0-9\_\]+\$



cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/http/messages#cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

Defaults to `5m`. See [prompt caching pricing](../Guides/build-with-claude-prompt-caching.md) for details.

One of the following:

"5m"



"1h"





CodeExecutionToolResultBlockParamContent = [CodeExecutionToolResultErrorParam](https://platform.claude.com/docs/en/api/http/messages#code_execution_tool_result_error_param) or [CodeExecutionResultBlockParam](https://platform.claude.com/docs/en/api/http/messages#code_execution_result_block_param) or [EncryptedCodeExecutionResultBlockParam](https://platform.claude.com/docs/en/api/http/messages#encrypted_code_execution_result_block_param)

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

error_code: [CodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#code_execution_tool_result_error_code)

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

error_code: [CodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#code_execution_tool_result_error_code)

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

ComputerCursorPositionInput object{  }



Get the current (x, y) pixel coordinate of the cursor.



ComputerCursorPositionToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerDoubleClickInput object{ coordinate, text }



Double-click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted.



coordinate: optional array of number or null



(x, y): x pixels from the left edge, y pixels from the top edge.

minItems2

maxItems2

text: optional string or null



Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift").



ComputerDoubleClickToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerHoldKeyInput object{ duration, text }



Hold down a key or key-combination for a specified duration. Uses the same key syntax as `key`.



duration: number



Duration to hold the key, in seconds.

maximum300

text: string



The key or key-combination to hold.



ComputerHoldKeyToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerKeyInput object{ text, repeat }



Press a key or key-combination on the keyboard. Use "+" to combine modifiers with a key (e.g. "ctrl+s", "alt+Tab", "ctrl+shift+Escape"). Key names are case-insensitive; common names like "Return", "Tab", "Escape", "Up", "Down", "Left", "Right", "Home", "End", "Page_Up", "Page_Down", "Delete", "BackSpace" are supported.

text: string



The key or key-combination to press.



repeat: optional number or null



Number of times to repeat the key press. Default is 1.

minimum1

maximum100



ComputerKeyToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerLeftClickDragInput object{ coordinate, start_coordinate, text }



Click and drag the cursor from `start_coordinate` to `coordinate`.



coordinate: array of number



(x, y): x pixels from the left edge, y pixels from the top edge.

minItems2

maxItems2



start_coordinate: array of number



(x, y): x pixels from the left edge, y pixels from the top edge.

minItems2

maxItems2

text: optional string or null



Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift").



ComputerLeftClickDragToolUseBlock object{ type: "tool_use", id, caller, 3 more }





ComputerLeftClickInput object{ coordinate, text }



Click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted.



coordinate: optional array of number or null



(x, y): x pixels from the left edge, y pixels from the top edge.

minItems2

maxItems2

text: optional string or null



Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift").



ComputerLeftClickToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerLeftMouseDownInput object{  }



Press and hold the left mouse button at the current cursor position.



ComputerLeftMouseDownToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerLeftMouseUpInput object{  }



Release the left mouse button.



ComputerLeftMouseUpToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerMiddleClickInput object{ coordinate, text }



Click the middle mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted.



coordinate: optional array of number or null



(x, y): x pixels from the left edge, y pixels from the top edge.

minItems2

maxItems2

text: optional string or null



Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift").



ComputerMiddleClickToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerMouseMoveInput object{ coordinate }



Move the cursor to a specified (x, y) pixel coordinate. Use this ONLY to hover without clicking; otherwise use a click action directly.



coordinate: array of number



(x, y): x pixels from the left edge, y pixels from the top edge.

minItems2

maxItems2



ComputerMouseMoveToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerRightClickInput object{ coordinate, text }



Click the right mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted.



coordinate: optional array of number or null



(x, y): x pixels from the left edge, y pixels from the top edge.

minItems2

maxItems2

text: optional string or null



Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift").



ComputerRightClickToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerScreenshotInput object{  }



Take a screenshot of the screen.



ComputerScreenshotToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerScrollDirection = "up" or "down" or "left" or "right"



One of the following:

"up"



"down"



"left"



"right"





ComputerScrollInput object{ scroll_amount, scroll_direction, coordinate, text }



Scroll the screen at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted. Do NOT use PageUp/PageDown to scroll.

scroll_amount: number



Number of 'clicks' of the scroll wheel.



scroll_direction: [ComputerScrollDirection](https://platform.claude.com/docs/en/api/http/messages#computer_scroll_direction)



One of the following:

"up"



"down"



"left"



"right"





coordinate: optional array of number or null



(x, y): x pixels from the left edge, y pixels from the top edge.

minItems2

maxItems2

text: optional string or null



Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift").



ComputerScrollToolUseBlock object{ type: "tool_use", id, caller, 3 more }





ComputerToolUseBlock = [ComputerKeyToolUseBlock](https://platform.claude.com/docs/en/api/http/messages#computer_key_tool_use_block) or [ComputerHoldKeyToolUseBlock](https://platform.claude.com/docs/en/api/http/messages#computer_hold_key_tool_use_block) or [ComputerTypeToolUseBlock](https://platform.claude.com/docs/en/api/http/messages#computer_type_tool_use_block) or 14 more



One of the following:

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

ComputerTripleClickInput object{ coordinate, text }



Triple-click the left mouse button at the specified (x, y) pixel coordinate, or the current cursor position if `coordinate` is omitted.



coordinate: optional array of number or null



(x, y): x pixels from the left edge, y pixels from the top edge.

minItems2

maxItems2

text: optional string or null



Optional key combination to hold down during this action (e.g. "ctrl", "shift", "ctrl+shift").



ComputerTripleClickToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerTypeInput object{ text }



Type a string of text on the keyboard.

text: string



The text to type.



ComputerTypeToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerWaitInput object{ duration }



Wait for a specified duration.



duration: number



Duration to wait, in seconds.

maximum300



ComputerWaitToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

ComputerZoomInput object{ region }



Take a screenshot of a rectangular region. Region coordinates are in the full-screenshot space (not physical display pixels). The crop is scaled up to fill the image budget so fine details become legible.



region: array of number



(x0, y0, x1, y1): The region to capture.

minItems4

maxItems4



ComputerZoomToolUseBlock object{ type: "tool_use", id, caller, 3 more }



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

skills: array of [ContainerSkill](https://platform.claude.com/docs/en/api/http/messages#container_skill) { type, skill_id, version } or null

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

skills: optional array of [SkillParams](https://platform.claude.com/docs/en/api/http/messages#skill_params) { type, skill_id, version } or null

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

cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/http/messages#cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

Defaults to `5m`. See [prompt caching pricing](../Guides/build-with-claude-prompt-caching.md) for details.

One of the following:

"5m"



"1h"





ContentBlock = [TextBlock](https://platform.claude.com/docs/en/api/http/messages#text_block) or [ThinkingBlock](https://platform.claude.com/docs/en/api/http/messages#thinking_block) or [RedactedThinkingBlock](https://platform.claude.com/docs/en/api/http/messages#redacted_thinking_block) or 9 more



One of the following:



ContentBlockParam = [TextBlockParam](https://platform.claude.com/docs/en/api/http/messages#text_block_param) or [ImageBlockParam](https://platform.claude.com/docs/en/api/http/messages#image_block_param) or [DocumentBlockParam](https://platform.claude.com/docs/en/api/http/messages#document_block_param) or 13 more



One of the following:



ContentBlockSource object{ type: "content", content }



type: "content"





content: string or array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/http/messages#content_block_source_content)



One of the following:

string





ContentBlockSourceContent = array of [ContentBlockSourceContent](https://platform.claude.com/docs/en/api/http/messages#content_block_source_content)



One of the following:



TextBlockParam object{ type: "text", text, cache_control, citations }





ImageBlockParam object{ type: "image", source, cache_control, transformations }





ContentBlockSourceContent = [TextBlockParam](https://platform.claude.com/docs/en/api/http/messages#text_block_param) or [ImageBlockParam](https://platform.claude.com/docs/en/api/http/messages#image_block_param)

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

cache_miss_reason: [CacheMissReason](https://platform.claude.com/docs/en/api/http/messages#cache_miss_reason) or null

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

content: array of [CodeExecutionOutputBlock](https://platform.claude.com/docs/en/api/http/messages#code_execution_output_block) { type: "code_execution_output", file_id }

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

content: array of [CodeExecutionOutputBlockParam](https://platform.claude.com/docs/en/api/http/messages#code_execution_output_block_param) { type: "code_execution_output", file_id }

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

MessageCountTokensTool = [Tool](https://platform.claude.com/docs/en/api/http/messages#tool) or [ToolBash20250124](https://platform.claude.com/docs/en/api/http/messages#tool_bash_20250124) or [CodeExecutionTool20250522](https://platform.claude.com/docs/en/api/http/messages#code_execution_tool_20250522) or 18 more



One of the following:



MessageCreateParamsContainer = [ContainerParams](https://platform.claude.com/docs/en/api/http/messages#container_params) or string

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

skills: optional array of [SkillParams](https://platform.claude.com/docs/en/api/http/messages#skill_params) { type, skill_id, version } or null

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

Model = "claude-haiku-5-5" or "claude-sonnet-5-5" or "claude-fable-5-1" or 17 more or string

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

format: optional [JSONOutputFormat](https://platform.claude.com/docs/en/api/http/messages#json_output_format) { type: "json_schema", schema } or null



A schema to specify Claude's output format in responses. See [structured outputs](../Guides/build-with-claude-structured-outputs.md)

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

RawContentBlockDelta = [TextDelta](https://platform.claude.com/docs/en/api/http/messages#text_delta) or [InputJSONDelta](https://platform.claude.com/docs/en/api/http/messages#input_json_delta) or [CitationsDelta](https://platform.claude.com/docs/en/api/http/messages#citations_delta) or 2 more

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

delta: [RawContentBlockDelta](https://platform.claude.com/docs/en/api/http/messages#raw_content_block_delta)

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

message: [Message](https://platform.claude.com/docs/en/api/http/messages#message) { type: "message", id, container, 8 more }





RawMessageStopEvent object{ type: "message_stop" }





type: "message_stop"



defaultmessage_stop



RawMessageStreamEvent = [RawMessageStartEvent](https://platform.claude.com/docs/en/api/http/messages#raw_message_start_event) or [RawMessageDeltaEvent](https://platform.claude.com/docs/en/api/http/messages#raw_message_delta_event) or [RawMessageStopEvent](https://platform.claude.com/docs/en/api/http/messages#raw_message_stop_event) or 3 more

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

See [extended thinking](../Guides/build-with-claude-extended-thinking.md#redacted-thinking-blocks) for details.

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

The request asks the model to reproduce its internal reasoning in the response text. To get reasoning in a structured form instead, use [adaptive thinking](../Guides/build-with-claude-thinking-steering-and-cost.md).

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

TextCitation = [CitationCharLocation](https://platform.claude.com/docs/en/api/http/messages#citation_char_location) or [CitationPageLocation](https://platform.claude.com/docs/en/api/http/messages#citation_page_location) or [CitationContentBlockLocation](https://platform.claude.com/docs/en/api/http/messages#citation_content_block_location) or 2 more



One of the following:



TextCitationParam = [CitationCharLocationParam](https://platform.claude.com/docs/en/api/http/messages#citation_char_location_param) or [CitationPageLocationParam](https://platform.claude.com/docs/en/api/http/messages#citation_page_location_param) or [CitationContentBlockLocationParam](https://platform.claude.com/docs/en/api/http/messages#citation_content_block_location_param) or 2 more

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

error_code: [TextEditorCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#text_editor_code_execution_tool_result_error_code)

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

error_code: [TextEditorCodeExecutionToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#text_editor_code_execution_tool_result_error_code)

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

See [extended thinking](../Guides/build-with-claude-extended-thinking.md) for details.

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

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. The default depends on the model; see [Controlling thinking display](../Guides/build-with-claude-thinking.md#controlling-thinking-display).

One of the following:

"summarized"



"omitted"





ThinkingConfigBetweenTools object{ type: "between_tools" }



type: "between_tools"

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

See [extended thinking](../Guides/build-with-claude-extended-thinking.md) for details.

minimum1024



display: optional "summarized" or "omitted" or null



Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. The default depends on the model; see [Controlling thinking display](../Guides/build-with-claude-thinking.md#controlling-thinking-display).

One of the following:

"summarized"



"omitted"





ThinkingConfigParam = [ThinkingConfigEnabled](https://platform.claude.com/docs/en/api/http/messages#thinking_config_enabled) or [ThinkingConfigDisabled](https://platform.claude.com/docs/en/api/http/messages#thinking_config_disabled) or [ThinkingConfigBetweenTools](https://platform.claude.com/docs/en/api/http/messages#thinking_config_between_tools) or [ThinkingConfigAdaptive](https://platform.claude.com/docs/en/api/http/messages#thinking_config_adaptive)



Configuration for Claude's thinking.

With `{"type": "adaptive"}`, Claude decides when and how much to think. With `{"type": "enabled"}` (manual extended thinking), you set a `budget_tokens` of at least 1,024. Thinking tokens count toward your `max_tokens` limit.

Which `type` values are accepted, and what happens when you omit `thinking`, depend on the model. See [thinking](../Guides/build-with-claude-thinking.md#configuring-thinking) for each model's behavior.

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

ToolChoice = [ToolChoiceAuto](https://platform.claude.com/docs/en/api/http/messages#tool_choice_auto) or [ToolChoiceAny](https://platform.claude.com/docs/en/api/http/messages#tool_choice_any) or [ToolChoiceTool](https://platform.claude.com/docs/en/api/http/messages#tool_choice_tool) or [ToolChoiceNone](https://platform.claude.com/docs/en/api/http/messages#tool_choice_none)

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

cache_control: optional [CacheControlEphemeral](https://platform.claude.com/docs/en/api/http/messages#cache_control_ephemeral) { type: "ephemeral", ttl } or null

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

Defaults to `5m`. See [prompt caching pricing](../Guides/build-with-claude-prompt-caching.md) for details.

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

error_code: [ToolSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#tool_search_tool_result_error_code)

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

error_code: [ToolSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#tool_search_tool_result_error_code)

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

tool_references: array of [ToolReferenceBlock](https://platform.claude.com/docs/en/api/http/messages#tool_reference_block) { type: "tool_reference", tool_name }

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

ToolUnion = [Tool](https://platform.claude.com/docs/en/api/http/messages#tool) or [ToolBash20250124](https://platform.claude.com/docs/en/api/http/messages#tool_bash_20250124) or [CodeExecutionTool20250522](https://platform.claude.com/docs/en/api/http/messages#code_execution_tool_20250522) or 18 more



One of the following:



ToolUseBlock object{ type: "tool_use", id, caller, 3 more }





ToolUseBlockParam object{ type: "tool_use", id, input, 4 more }





ToolUseCaller = [DirectCaller](https://platform.claude.com/docs/en/api/http/messages#direct_caller) or [ServerToolCaller](https://platform.claude.com/docs/en/api/http/messages#server_tool_caller) or [ServerToolCaller20260120](https://platform.claude.com/docs/en/api/http/messages#server_tool_caller_20260120)



Which party invoked the tool call: the model directly, or a server tool on its behalf.

One of the following:



DirectCaller object{ type: "direct" }



Tool invocation directly from the model.

type: "direct"

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

ToolsetToolUseBlock = [BrowserToolUseBlock](https://platform.claude.com/docs/en/api/http/messages#browser_tool_use_block) or [ComputerToolUseBlock](https://platform.claude.com/docs/en/api/http/messages#computer_tool_use_block) or [ToolUseBlock](https://platform.claude.com/docs/en/api/http/messages#tool_use_block)



One of the following:

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

Usage object{ cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 7 more }

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

content: [DocumentBlock](https://platform.claude.com/docs/en/api/http/messages#document_block) { type: "document", citations, source, title }

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

content: [DocumentBlockParam](https://platform.claude.com/docs/en/api/http/messages#document_block_param) { type: "document", source, cache_control, 3 more }

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

error_code: [WebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#web_fetch_tool_result_error_code)

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

error_code: [WebFetchToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#web_fetch_tool_result_error_code)

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

tools: array of [WebFetchURLSourceToolReference](https://platform.claude.com/docs/en/api/http/messages#web_fetch_url_source_tool_reference) { type: "tool_reference", name }

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

tools: array of [WebFetchURLSourceToolReference](https://platform.claude.com/docs/en/api/http/messages#web_fetch_url_source_tool_reference) { type: "tool_reference", name }

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

error_code: [WebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#web_search_tool_result_error_code)

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

WebSearchToolResultBlockContent = [WebSearchToolResultError](https://platform.claude.com/docs/en/api/http/messages#web_search_tool_result_error) or array of [WebSearchResultBlock](https://platform.claude.com/docs/en/api/http/messages#web_search_result_block)



One of the following:



WebSearchToolResultBlockParam object{ type: "web_search_tool_result", content, tool_use_id, 2 more }





WebSearchToolResultBlockParamContent = array of [WebSearchResultBlockParam](https://platform.claude.com/docs/en/api/http/messages#web_search_result_block_param) or [WebSearchToolRequestError](https://platform.claude.com/docs/en/api/http/messages#web_search_tool_request_error)

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

error_code: [WebSearchToolResultErrorCode](https://platform.claude.com/docs/en/api/http/messages#web_search_tool_result_error_code)

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

#### Messages[Batches](https://platform.claude.com/docs/en/api/http/messages/batches)

##### [Create a Message Batch](https://platform.claude.com/docs/en/api/http/messages/batches/create)

POST/v1/messages/batches

Send a batch of Message creation requests.

##### [Retrieve a Message Batch](https://platform.claude.com/docs/en/api/http/messages/batches/retrieve)

GET/v1/messages/batches/{message_batch_id}

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

##### [List Message Batches](https://platform.claude.com/docs/en/api/http/messages/batches/list)

GET/v1/messages/batches

List all Message Batches within a Workspace. Most recently created batches are returned first.

##### [Cancel a Message Batch](https://platform.claude.com/docs/en/api/http/messages/batches/cancel)

POST/v1/messages/batches/{message_batch_id}/cancel

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

##### [Delete a Message Batch](https://platform.claude.com/docs/en/api/http/messages/batches/delete)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](https://platform.claude.com/docs/en/api/http/messages/batches/results)

GET/v1/messages/batches/{message_batch_id}/results

Streams the results of a Message Batch as a `.jsonl` file.
