---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/models"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:36:30Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-models.md).

1.  [API reference](http.md)

# Models

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Models](https://platform.claude.com/docs/en/api/http/models/list)

GET/v1/models

List available models.

##### [Get a Model](https://platform.claude.com/docs/en/api/http/models/retrieve)

GET/v1/models/{model_id}

Get a specific model.

##### Models



CapabilitySupport object{ supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.



ContextManagementCapability object{ clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management capability details.



clear_thinking_20251015: [CapabilitySupport](models.md#capability_support) { supported } or null



Whether the clear_thinking_20251015 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



clear_tool_uses_20250919: [CapabilitySupport](models.md#capability_support) { supported } or null



Whether the clear_tool_uses_20250919 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



compact_20260112: [CapabilitySupport](models.md#capability_support) { supported } or null



Whether the compact_20260112 strategy is supported.

supported: boolean



Whether this capability is supported by the model.

supported: boolean



Whether this capability is supported by the model.



EffortCapability object{ high, low, max, 3 more }



Effort (reasoning_effort) capability details.



ModelCapabilities object{ batch, citations, code_execution, 7 more }



Model capability information.



ModelInfo object{ type: "model", id, capabilities, 8 more }





ModelLine = "haiku" or "sonnet" or "opus" or 2 more



A Claude model line, such as `opus` or `sonnet`. More lines may be added as new values.

One of the following:

"haiku"



"sonnet"



"opus"



"fable"



"mythos"





ServerToolsCapability object{ code_execution, supported, web_search }



Web search and code execution tool support, with one entry per tool.



code_execution: [CapabilitySupport](models.md#capability_support) { supported }



Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

supported: boolean



Whether this capability is supported by the model.

supported: boolean



Whether this capability is supported by the model.



web_search: [CapabilitySupport](models.md#capability_support) { supported }



Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

supported: boolean



Whether this capability is supported by the model.



ThinkingCapability object{ supported, types }



Thinking capability details.

supported: boolean



Whether this capability is supported by the model.



types: [ThinkingTypes](models.md#thinking_types) { adaptive, between_tools, disabled, enabled }



Supported thinking type configurations.



ThinkingTypes object{ adaptive, between_tools, disabled, enabled }



Which `thinking.type` values the model accepts on requests. Read each key on its own: for example, `enabled` can be false while `disabled` is true.
