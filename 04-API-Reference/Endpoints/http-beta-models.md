---
title: "Models - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/models"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:35:38Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)

# Models

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Models](platform-claude-com-http-beta-models-list.md)

GET/v1/models

List available models.

##### [Get a Model](platform-claude-com-http-beta-models-retrieve.md)

GET/v1/models/{model_id}

Get a specific model.

##### Models



BetaCapabilitySupport object{ supported }



Indicates whether a capability is supported.

supported: boolean



Whether this capability is supported by the model.



BetaCompactionCapability object{ summarize, supported }



Compaction capability details: whether the model accepts the top-level `compaction` request parameter, with one entry per supported `compaction.type` value.



summarize: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported }



Whether the summarize compaction type is supported.

supported: boolean



Whether this capability is supported by the model.

supported: boolean



Whether this capability is supported by the model.



BetaContextManagementCapability object{ clear_thinking_20251015, clear_tool_uses_20250919, compact_20260112, supported }



Context management capability details.



clear_thinking_20251015: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported } or null



Whether the clear_thinking_20251015 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



clear_tool_uses_20250919: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported } or null



Whether the clear_tool_uses_20250919 strategy is supported.

supported: boolean



Whether this capability is supported by the model.



compact_20260112: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported } or null



Whether the compact_20260112 strategy is supported.

supported: boolean



Whether this capability is supported by the model.

supported: boolean



Whether this capability is supported by the model.



BetaEffortCapability object{ high, low, max, 3 more }



Effort (reasoning_effort) capability details.



BetaModelCapabilities object{ batch, citations, code_execution, 8 more }



Model capability information.



BetaModelInfo object{ type: "model", id, allowed_fallback_models, 9 more }





BetaModelLine = "haiku" or "sonnet" or "opus" or 2 more

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

BetaServerToolsCapability object{ code_execution, supported, web_search }



Web search and code execution tool support, with one entry per tool.



code_execution: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported }



Whether the model supports the code execution tool: true when the model supports at least one version of the tool, not necessarily every version.

supported: boolean



Whether this capability is supported by the model.

supported: boolean



Whether this capability is supported by the model.



web_search: [BetaCapabilitySupport](platform-claude-com-http-beta-models.md#beta_capability_support) { supported }



Whether the model supports the web search tool: true when the model supports at least one version of the tool, not necessarily every version.

supported: boolean



Whether this capability is supported by the model.



BetaThinkingCapability object{ supported, types }



Thinking capability details.

supported: boolean



Whether this capability is supported by the model.



types: [BetaThinkingTypes](platform-claude-com-http-beta-models.md#beta_thinking_types) { adaptive, between_tools, disabled, enabled }



Supported thinking type configurations.



BetaThinkingTypes object{ adaptive, between_tools, disabled, enabled }



Which `thinking.type` values the model accepts on requests. Read each key on its own: for example, `enabled` can be false while `disabled` is true.
