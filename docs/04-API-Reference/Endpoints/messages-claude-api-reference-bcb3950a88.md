---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:08:00Z"
source_url: "https://platform.claude.com/docs/en/api/python/beta/messages"
title: "Messages - Claude API Reference"
---

Copy page

Python

# Messages

##### [Create a Message](/docs/en/api/beta/messages/create)

beta.messages.create(MessageCreateParams\*\*kwargs) -\> [BetaMessage](/docs/en/api/beta#beta_message)

post/v1/messages

##### [Count tokens in a Message](/docs/en/api/beta/messages/count_tokens)

beta.messages.count_tokens(MessageCountTokensParams\*\*kwargs) -\> [BetaMessageTokensCount](/docs/en/api/beta#beta_message_tokens_count)

post/v1/messages/count_tokens

##### ModelsExpand Collapse 

class BetaAllThinkingTurns: …

type: Literal\["all"\]

Accepts one of the following:

"all"

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaBashCodeExecutionOutputBlock: …

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

class BetaBashCodeExecutionOutputBlockParam: …

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

class BetaBashCodeExecutionResultBlockParam: …

content: List\[[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

class BetaBashCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlockParam: …

content: List\[[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaCacheControlEphemeral: …

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaCacheCreation: …

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationConfig: …

enabled: bool

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationsConfigParam: …

enabled: Optional\[bool\]

class BetaCitationsDelta: …

citation: Citation

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

type: Literal\["citations_delta"\]

Accepts one of the following:

"citations_delta"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaClearThinking20251015Edit: …

type: Literal\["clear_thinking_20251015"\]

Accepts one of the following:

"clear_thinking_20251015"

keep: Optional\[Keep\]

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns: …

type: Literal\["thinking_turns"\]

Accepts one of the following:

"thinking_turns"

value: int

class BetaAllThinkingTurns: …

type: Literal\["all"\]

Accepts one of the following:

"all"

KeepUnionMember2 = Literal\["all"\]

Accepts one of the following:

"all"

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: int

Number of thinking turns that were cleared.

minimum0

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

class BetaClearToolUses20250919Edit: …

type: Literal\["clear_tool_uses_20250919"\]

Accepts one of the following:

"clear_tool_uses_20250919"

clear_at_least: Optional\[BetaInputTokensClearAtLeast\]

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

clear_tool_inputs: Optional\[Union\[bool, List\[str\], null\]\]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

ClearToolInputsUnionMember0 = bool

ClearToolInputsUnionMember1 = List\[str\]

exclude_tools: Optional\[List\[str\]\]

Tool names whose uses are preserved from clearing

keep: Optional\[BetaToolUsesKeep\]

Number of tool uses to retain in the conversation

type: Literal\["tool_uses"\]

Accepts one of the following:

"tool_uses"

value: int

trigger: Optional\[Trigger\]

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger: …

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

class BetaToolUsesTrigger: …

type: Literal\["tool_uses"\]

Accepts one of the following:

"tool_uses"

value: int

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: int

Number of tool uses that were cleared.

minimum0

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

class BetaCodeExecutionOutputBlock: …

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

class BetaCodeExecutionOutputBlockParam: …

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

class BetaCodeExecutionResultBlockParam: …

content: List\[[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

class BetaCodeExecutionTool20250522: …

name: Literal\["code_execution"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: Literal\["code_execution_20250522"\]

Accepts one of the following:

"code_execution_20250522"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825: …

name: Literal\["code_execution"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

BetaCodeExecutionToolResultBlockContent = [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

class BetaCodeExecutionToolResultBlockParam: …

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlockParam: …

content: List\[[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaCodeExecutionToolResultBlockParamContent = [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlockParam: …

content: List\[[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

BetaCodeExecutionToolResultErrorCode = Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

class BetaCodeExecutionToolResultErrorParam: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCompact20260112Edit: …

Automatically compact older context when reaching the configured trigger threshold.

type: Literal\["compact_20260112"\]

Accepts one of the following:

"compact_20260112"

instructions: Optional\[str\]

Additional instructions for summarization.

pause_after_compaction: Optional\[bool\]

Whether to pause after compaction and return the compaction block to the user.

trigger: Optional\[BetaInputTokensTrigger\]

When to trigger compaction. Defaults to 150000 input tokens.

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

class BetaCompactionBlockParam: …

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: Optional\[str\]

Summary of previously compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaCompactionContentBlockDelta: …

content: Optional\[str\]

type: Literal\["compaction_delta"\]

Accepts one of the following:

"compaction_delta"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

class BetaContainer: …

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

formatdate-time

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

maxLength64

minLength1

class BetaContainerParams: …

Container parameters with skills to be loaded.

id: Optional\[str\]

Container id

skills: Optional\[List\[[BetaSkillParams](/docs/en/api/beta#beta_skill_params)\]\]

List of skills to load in the container

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: Optional\[str\]

Skill version or 'latest' for most recent version

maxLength64

minLength1

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

class BetaContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaContentBlock = [BetaContentBlock](/docs/en/api/beta#beta_content_block)

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockContent = List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

BetaContentBlockParam = [BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)

Regular text content.

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaRequestDocumentBlock: …

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

class BetaSearchResultBlockParam: …

content: List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

class BetaThinkingBlockParam: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlockParam: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaToolResultBlockParam: …

tool_use_id: str

type: Literal\["tool_result"\]

Accepts one of the following:

"tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: Optional\[Union\[str, List\[Content\], null\]\]

Accepts one of the following:

ContentUnionMember0 = str

Content = List\[Content\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaSearchResultBlockParam: …

content: List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

class BetaRequestDocumentBlock: …

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

class BetaToolReferenceBlockParam: …

Tool reference block that can be included in tool_result content.

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error: Optional\[bool\]

class BetaServerToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlockParam: …

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = List\[[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\]

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class BetaWebSearchToolRequestError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaWebFetchToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlockParam: …

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block)

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaCodeExecutionToolResultBlockParam: …

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlockParam: …

content: List\[[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaBashCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlockParam: …

content: List\[[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaTextEditorCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

error_message: Optional\[str\]

class BetaTextEditorCodeExecutionViewResultBlockParam: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

class BetaTextEditorCodeExecutionCreateResultBlockParam: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaToolSearchToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlockParam: …

tool_references: List\[[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaMCPToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaRequestMCPToolResultBlockParam: …

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: Optional\[Union\[str, List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\], null\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockParamContent = List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

is_error: Optional\[bool\]

class BetaContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaCompactionBlockParam: …

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: Optional\[str\]

Summary of previously compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

BetaContentBlockSourceContent = [BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaContextManagementConfig: …

edits: Optional\[List\[Edit\]\]

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit: …

type: Literal\["clear_tool_uses_20250919"\]

Accepts one of the following:

"clear_tool_uses_20250919"

clear_at_least: Optional\[BetaInputTokensClearAtLeast\]

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

clear_tool_inputs: Optional\[Union\[bool, List\[str\], null\]\]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

ClearToolInputsUnionMember0 = bool

ClearToolInputsUnionMember1 = List\[str\]

exclude_tools: Optional\[List\[str\]\]

Tool names whose uses are preserved from clearing

keep: Optional\[BetaToolUsesKeep\]

Number of tool uses to retain in the conversation

type: Literal\["tool_uses"\]

Accepts one of the following:

"tool_uses"

value: int

trigger: Optional\[Trigger\]

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger: …

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

class BetaToolUsesTrigger: …

type: Literal\["tool_uses"\]

Accepts one of the following:

"tool_uses"

value: int

class BetaClearThinking20251015Edit: …

type: Literal\["clear_thinking_20251015"\]

Accepts one of the following:

"clear_thinking_20251015"

keep: Optional\[Keep\]

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns: …

type: Literal\["thinking_turns"\]

Accepts one of the following:

"thinking_turns"

value: int

class BetaAllThinkingTurns: …

type: Literal\["all"\]

Accepts one of the following:

"all"

KeepUnionMember2 = Literal\["all"\]

Accepts one of the following:

"all"

class BetaCompact20260112Edit: …

Automatically compact older context when reaching the configured trigger threshold.

type: Literal\["compact_20260112"\]

Accepts one of the following:

"compact_20260112"

instructions: Optional\[str\]

Additional instructions for summarization.

pause_after_compaction: Optional\[bool\]

Whether to pause after compaction and return the compaction block to the user.

trigger: Optional\[BetaInputTokensTrigger\]

When to trigger compaction. Defaults to 150000 input tokens.

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

class BetaContextManagementResponse: …

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: int

Number of tool uses that were cleared.

minimum0

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: int

Number of thinking turns that were cleared.

minimum0

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

class BetaCountTokensContextManagementResponse: …

original_input_tokens: int

The original token count before context management was applied

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaDocumentBlock: …

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaInputJSONDelta: …

partial_json: str

type: Literal\["input_json_delta"\]

Accepts one of the following:

"input_json_delta"

class BetaInputTokensClearAtLeast: …

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

class BetaInputTokensTrigger: …

type: Literal\["input_tokens"\]

Accepts one of the following:

"input_tokens"

value: int

class BetaJSONOutputFormat: …

schema: Dict\[str, object\]

The JSON schema of the format

type: Literal\["json_schema"\]

Accepts one of the following:

"json_schema"

class BetaMCPToolConfig: …

Configuration for a specific tool in an MCP toolset.

defer_loading: Optional\[bool\]

enabled: Optional\[bool\]

class BetaMCPToolDefaultConfig: …

Default configuration for tools in an MCP toolset.

defer_loading: Optional\[bool\]

enabled: Optional\[bool\]

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockContent = List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

class BetaMCPToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaMCPToolset: …

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

mcp_server_name: str

Name of the MCP server to configure tools for

maxLength255

minLength1

type: Literal\["mcp_toolset"\]

Accepts one of the following:

"mcp_toolset"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

configs: Optional\[Dict\[str, [BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config)\]\]

Configuration overrides for specific tools, keyed by tool name

defer_loading: Optional\[bool\]

enabled: Optional\[bool\]

default_config: Optional\[BetaMCPToolDefaultConfig\]

Default configuration applied to all tools from this server

defer_loading: Optional\[bool\]

enabled: Optional\[bool\]

class BetaMemoryTool20250818: …

name: Literal\["memory"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"memory"

type: Literal\["memory_20250818"\]

Accepts one of the following:

"memory_20250818"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

BetaMemoryTool20250818Command = [BetaMemoryTool20250818Command](/docs/en/api/beta#beta_memory_tool_20250818_command)

Accepts one of the following:

class BetaMemoryTool20250818ViewCommand: …

command: Literal\["view"\]

Command type identifier

Accepts one of the following:

"view"

path: str

Path to directory or file to view

view_range: Optional\[List\[int\]\]

Optional line range for viewing specific lines

class BetaMemoryTool20250818CreateCommand: …

command: Literal\["create"\]

Command type identifier

Accepts one of the following:

"create"

file_text: str

Content to write to the file

path: str

Path where the file should be created

class BetaMemoryTool20250818StrReplaceCommand: …

command: Literal\["str_replace"\]

Command type identifier

Accepts one of the following:

"str_replace"

new_str: str

Text to replace with

old_str: str

Text to search for and replace

path: str

Path to the file where text should be replaced

class BetaMemoryTool20250818InsertCommand: …

command: Literal\["insert"\]

Command type identifier

Accepts one of the following:

"insert"

insert_line: int

Line number where text should be inserted

minimum1

insert_text: str

Text to insert at the specified line

path: str

Path to the file where text should be inserted

class BetaMemoryTool20250818DeleteCommand: …

command: Literal\["delete"\]

Command type identifier

Accepts one of the following:

"delete"

path: str

Path to the file or directory to delete

class BetaMemoryTool20250818RenameCommand: …

command: Literal\["rename"\]

Command type identifier

Accepts one of the following:

"rename"

new_path: str

New path for the file or directory

old_path: str

Current path of the file or directory

class BetaMemoryTool20250818CreateCommand: …

command: Literal\["create"\]

Command type identifier

Accepts one of the following:

"create"

file_text: str

Content to write to the file

path: str

Path where the file should be created

class BetaMemoryTool20250818DeleteCommand: …

command: Literal\["delete"\]

Command type identifier

Accepts one of the following:

"delete"

path: str

Path to the file or directory to delete

class BetaMemoryTool20250818InsertCommand: …

command: Literal\["insert"\]

Command type identifier

Accepts one of the following:

"insert"

insert_line: int

Line number where text should be inserted

minimum1

insert_text: str

Text to insert at the specified line

path: str

Path to the file where text should be inserted

class BetaMemoryTool20250818RenameCommand: …

command: Literal\["rename"\]

Command type identifier

Accepts one of the following:

"rename"

new_path: str

New path for the file or directory

old_path: str

Current path of the file or directory

class BetaMemoryTool20250818StrReplaceCommand: …

command: Literal\["str_replace"\]

Command type identifier

Accepts one of the following:

"str_replace"

new_str: str

Text to replace with

old_str: str

Text to search for and replace

path: str

Path to the file where text should be replaced

class BetaMemoryTool20250818ViewCommand: …

command: Literal\["view"\]

Command type identifier

Accepts one of the following:

"view"

path: str

Path to directory or file to view

view_range: Optional\[List\[int\]\]

Optional line range for viewing specific lines

class BetaMessage: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

formatdate-time

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockContent = List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

context_management: Optional\[BetaContextManagementResponse\]

Context management response.

Information about context management strategies applied during the request.

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: int

Number of tool uses that were cleared.

minimum0

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: int

Number of thinking turns that were cleared.

minimum0

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: Optional\[BetaStopReason\]

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

iterations: Optional\[List\[Iteration\]\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

class BetaMessageDeltaUsage: …

cache_creation_input_tokens: Optional\[int\]

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: Optional\[int\]

The cumulative number of input tokens which were used.

minimum0

iterations: Optional\[List\[Iteration\]\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: int

The cumulative number of output tokens which were used.

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaMessageParam: …

content: Union\[str, List\[[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentUnionMember1 = List\[[BetaContentBlockParam](/docs/en/api/beta#beta_content_block_param)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaRequestDocumentBlock: …

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

class BetaSearchResultBlockParam: …

content: List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

class BetaThinkingBlockParam: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlockParam: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaToolResultBlockParam: …

tool_use_id: str

type: Literal\["tool_result"\]

Accepts one of the following:

"tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: Optional\[Union\[str, List\[Content\], null\]\]

Accepts one of the following:

ContentUnionMember0 = str

Content = List\[Content\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaSearchResultBlockParam: …

content: List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

class BetaRequestDocumentBlock: …

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

class BetaToolReferenceBlockParam: …

Tool reference block that can be included in tool_result content.

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error: Optional\[bool\]

class BetaServerToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlockParam: …

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = List\[[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\]

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class BetaWebSearchToolRequestError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaWebFetchToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlockParam: …

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block)

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaCodeExecutionToolResultBlockParam: …

content: [BetaCodeExecutionToolResultBlockParamContent](/docs/en/api/beta#beta_code_execution_tool_result_block_param_content)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlockParam: …

content: List\[[BetaCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_code_execution_output_block_param)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaBashCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlockParam: …

content: List\[[BetaBashCodeExecutionOutputBlockParam](/docs/en/api/beta#beta_bash_code_execution_output_block_param)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaTextEditorCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

error_message: Optional\[str\]

class BetaTextEditorCodeExecutionViewResultBlockParam: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

class BetaTextEditorCodeExecutionCreateResultBlockParam: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaToolSearchToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlockParam: …

tool_references: List\[[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaMCPToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaRequestMCPToolResultBlockParam: …

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: Optional\[Union\[str, List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\], null\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockParamContent = List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

is_error: Optional\[bool\]

class BetaContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container Files uploaded via this block will be available in the container's input directory.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaCompactionBlockParam: …

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server treats these as no-ops. Empty string content is not allowed.

content: Optional\[str\]

Summary of previously compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

role: Literal\["user", "assistant"\]

Accepts one of the following:

"user"

"assistant"

class BetaMessageTokensCount: …

context_management: Optional\[BetaCountTokensContextManagementResponse\]

Information about context management applied to the message.

original_input_tokens: int

The original token count before context management was applied

input_tokens: int

The total number of tokens across the provided list of messages, system prompt, and tools.

class BetaMetadata: …

user_id: Optional\[str\]

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength256

class BetaOutputConfig: …

effort: Optional\[Literal\["low", "medium", "high", "max"\]\]

All possible effort levels.

Accepts one of the following:

"low"

"medium"

"high"

"max"

format: Optional\[BetaJSONOutputFormat\]

A schema to specify Claude's output format in responses. See [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)

schema: Dict\[str, object\]

The JSON schema of the format

type: Literal\["json_schema"\]

Accepts one of the following:

"json_schema"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

BetaRawContentBlockDelta = [BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta)

Accepts one of the following:

class BetaTextDelta: …

text: str

type: Literal\["text_delta"\]

Accepts one of the following:

"text_delta"

class BetaInputJSONDelta: …

partial_json: str

type: Literal\["input_json_delta"\]

Accepts one of the following:

"input_json_delta"

class BetaCitationsDelta: …

citation: Citation

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

type: Literal\["citations_delta"\]

Accepts one of the following:

"citations_delta"

class BetaThinkingDelta: …

thinking: str

type: Literal\["thinking_delta"\]

Accepts one of the following:

"thinking_delta"

class BetaSignatureDelta: …

signature: str

type: Literal\["signature_delta"\]

Accepts one of the following:

"signature_delta"

class BetaCompactionContentBlockDelta: …

content: Optional\[str\]

type: Literal\["compaction_delta"\]

Accepts one of the following:

"compaction_delta"

class BetaRawContentBlockDeltaEvent: …

delta: [BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta)

Accepts one of the following:

class BetaTextDelta: …

text: str

type: Literal\["text_delta"\]

Accepts one of the following:

"text_delta"

class BetaInputJSONDelta: …

partial_json: str

type: Literal\["input_json_delta"\]

Accepts one of the following:

"input_json_delta"

class BetaCitationsDelta: …

citation: Citation

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

type: Literal\["citations_delta"\]

Accepts one of the following:

"citations_delta"

class BetaThinkingDelta: …

thinking: str

type: Literal\["thinking_delta"\]

Accepts one of the following:

"thinking_delta"

class BetaSignatureDelta: …

signature: str

type: Literal\["signature_delta"\]

Accepts one of the following:

"signature_delta"

class BetaCompactionContentBlockDelta: …

content: Optional\[str\]

type: Literal\["compaction_delta"\]

Accepts one of the following:

"compaction_delta"

index: int

type: Literal\["content_block_delta"\]

Accepts one of the following:

"content_block_delta"

class BetaRawContentBlockStartEvent: …

content_block: ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockContent = List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

index: int

type: Literal\["content_block_start"\]

Accepts one of the following:

"content_block_start"

class BetaRawContentBlockStopEvent: …

index: int

type: Literal\["content_block_stop"\]

Accepts one of the following:

"content_block_stop"

class BetaRawMessageDeltaEvent: …

context_management: Optional\[BetaContextManagementResponse\]

Information about context management strategies applied during the request

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: int

Number of tool uses that were cleared.

minimum0

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: int

Number of thinking turns that were cleared.

minimum0

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

delta: Delta

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

formatdate-time

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

maxLength64

minLength1

stop_reason: Optional\[BetaStopReason\]

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: Optional\[str\]

type: Literal\["message_delta"\]

Accepts one of the following:

"message_delta"

usage: [BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: Optional\[int\]

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: Optional\[int\]

The cumulative number of input tokens which were used.

minimum0

iterations: Optional\[List\[Iteration\]\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: int

The cumulative number of output tokens which were used.

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

class BetaRawMessageStartEvent: …

message: [BetaMessage](/docs/en/api/beta#beta_message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

formatdate-time

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockContent = List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

context_management: Optional\[BetaContextManagementResponse\]

Context management response.

Information about context management strategies applied during the request.

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: int

Number of tool uses that were cleared.

minimum0

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: int

Number of thinking turns that were cleared.

minimum0

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: Optional\[BetaStopReason\]

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

iterations: Optional\[List\[Iteration\]\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["message_start"\]

Accepts one of the following:

"message_start"

class BetaRawMessageStopEvent: …

type: Literal\["message_stop"\]

Accepts one of the following:

"message_stop"

BetaRawMessageStreamEvent = [BetaRawMessageStreamEvent](/docs/en/api/beta#beta_raw_message_stream_event)

Accepts one of the following:

class BetaRawMessageStartEvent: …

message: [BetaMessage](/docs/en/api/beta#beta_message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

formatdate-time

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockContent = List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

context_management: Optional\[BetaContextManagementResponse\]

Context management response.

Information about context management strategies applied during the request.

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: int

Number of tool uses that were cleared.

minimum0

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: int

Number of thinking turns that were cleared.

minimum0

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: Optional\[BetaStopReason\]

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

iterations: Optional\[List\[Iteration\]\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["message_start"\]

Accepts one of the following:

"message_start"

class BetaRawMessageDeltaEvent: …

context_management: Optional\[BetaContextManagementResponse\]

Information about context management strategies applied during the request

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: int

Number of tool uses that were cleared.

minimum0

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: int

Number of thinking turns that were cleared.

minimum0

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

delta: Delta

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

formatdate-time

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

maxLength64

minLength1

stop_reason: Optional\[BetaStopReason\]

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: Optional\[str\]

type: Literal\["message_delta"\]

Accepts one of the following:

"message_delta"

usage: [BetaMessageDeltaUsage](/docs/en/api/beta#beta_message_delta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation_input_tokens: Optional\[int\]

The cumulative number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The cumulative number of input tokens read from the cache.

minimum0

input_tokens: Optional\[int\]

The cumulative number of input tokens which were used.

minimum0

iterations: Optional\[List\[Iteration\]\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: int

The cumulative number of output tokens which were used.

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

class BetaRawMessageStopEvent: …

type: Literal\["message_stop"\]

Accepts one of the following:

"message_stop"

class BetaRawContentBlockStartEvent: …

content_block: ContentBlock

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockContent = List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

index: int

type: Literal\["content_block_start"\]

Accepts one of the following:

"content_block_start"

class BetaRawContentBlockDeltaEvent: …

delta: [BetaRawContentBlockDelta](/docs/en/api/beta#beta_raw_content_block_delta)

Accepts one of the following:

class BetaTextDelta: …

text: str

type: Literal\["text_delta"\]

Accepts one of the following:

"text_delta"

class BetaInputJSONDelta: …

partial_json: str

type: Literal\["input_json_delta"\]

Accepts one of the following:

"input_json_delta"

class BetaCitationsDelta: …

citation: Citation

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

type: Literal\["citations_delta"\]

Accepts one of the following:

"citations_delta"

class BetaThinkingDelta: …

thinking: str

type: Literal\["thinking_delta"\]

Accepts one of the following:

"thinking_delta"

class BetaSignatureDelta: …

signature: str

type: Literal\["signature_delta"\]

Accepts one of the following:

"signature_delta"

class BetaCompactionContentBlockDelta: …

content: Optional\[str\]

type: Literal\["compaction_delta"\]

Accepts one of the following:

"compaction_delta"

index: int

type: Literal\["content_block_delta"\]

Accepts one of the following:

"content_block_delta"

class BetaRawContentBlockStopEvent: …

index: int

type: Literal\["content_block_stop"\]

Accepts one of the following:

"content_block_stop"

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaRedactedThinkingBlockParam: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaRequestDocumentBlock: …

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

class BetaRequestMCPServerToolConfiguration: …

allowed_tools: Optional\[List\[str\]\]

enabled: Optional\[bool\]

class BetaRequestMCPServerURLDefinition: …

name: str

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

authorization_token: Optional\[str\]

tool_configuration: Optional\[BetaRequestMCPServerToolConfiguration\]

allowed_tools: Optional\[List\[str\]\]

enabled: Optional\[bool\]

class BetaRequestMCPToolResultBlockParam: …

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: Optional\[Union\[str, List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\], null\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockParamContent = List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

is_error: Optional\[bool\]

class BetaSearchResultBlockParam: …

content: List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUsage: …

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaSignatureDelta: …

signature: str

type: Literal\["signature_delta"\]

Accepts one of the following:

"signature_delta"

class BetaSkill: …

A skill that was loaded in a container (response model).

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

maxLength64

minLength1

class BetaSkillParams: …

Specification for a skill to be loaded in a container (request model).

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: Optional\[str\]

Skill version or 'latest' for most recent version

maxLength64

minLength1

BetaStopReason = Literal\["end_turn", "max_tokens", "stop_sequence", 5 more\]

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

BetaTextCitation = [BetaTextCitation](/docs/en/api/beta#beta_text_citation)

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

BetaTextCitationParam = [BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaTextDelta: …

text: str

type: Literal\["text_delta"\]

Accepts one of the following:

"text_delta"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionCreateResultBlockParam: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

class BetaTextEditorCodeExecutionToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

error_message: Optional\[str\]

class BetaTextEditorCodeExecutionViewResultBlockParam: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

class BetaTextEditorCodeExecutionCreateResultBlockParam: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

error_message: Optional\[str\]

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionViewResultBlockParam: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaThinkingBlockParam: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaThinkingConfigAdaptive: …

type: Literal\["adaptive"\]

Accepts one of the following:

"adaptive"

class BetaThinkingConfigDisabled: …

type: Literal\["disabled"\]

Accepts one of the following:

"disabled"

class BetaThinkingConfigEnabled: …

budget_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: Literal\["enabled"\]

Accepts one of the following:

"enabled"

BetaThinkingConfigParam = [BetaThinkingConfigParam](/docs/en/api/beta#beta_thinking_config_param)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class BetaThinkingConfigEnabled: …

budget_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: Literal\["enabled"\]

Accepts one of the following:

"enabled"

class BetaThinkingConfigDisabled: …

type: Literal\["disabled"\]

Accepts one of the following:

"disabled"

class BetaThinkingConfigAdaptive: …

type: Literal\["adaptive"\]

Accepts one of the following:

"adaptive"

class BetaThinkingDelta: …

thinking: str

type: Literal\["thinking_delta"\]

Accepts one of the following:

"thinking_delta"

class BetaThinkingTurns: …

type: Literal\["thinking_turns"\]

Accepts one of the following:

"thinking_turns"

value: int

class BetaTool: …

input_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal\["object"\]

Accepts one of the following:

"object"

properties: Optional\[Dict\[str, object\]\]

required: Optional\[List\[str\]\]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

description: Optional\[str\]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: Optional\[bool\]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

type: Optional\[Literal\["custom"\]\]

Accepts one of the following:

"custom"

class BetaToolBash20241022: …

name: Literal\["bash"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal\["bash_20241022"\]

Accepts one of the following:

"bash_20241022"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124: …

name: Literal\["bash"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal\["bash_20250124"\]

Accepts one of the following:

"bash_20250124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

BetaToolChoice = [BetaToolChoice](/docs/en/api/beta#beta_tool_choice)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class BetaToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal\["auto"\]

Accepts one of the following:

"auto"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny: …

The model will use any available tools.

type: Literal\["any"\]

Accepts one of the following:

"any"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal\["tool"\]

Accepts one of the following:

"tool"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal\["none"\]

Accepts one of the following:

"none"

class BetaToolChoiceAny: …

The model will use any available tools.

type: Literal\["any"\]

Accepts one of the following:

"any"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal\["auto"\]

Accepts one of the following:

"auto"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal\["none"\]

Accepts one of the following:

"none"

class BetaToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal\["tool"\]

Accepts one of the following:

"tool"

disable_parallel_tool_use: Optional\[bool\]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolComputerUse20241022: …

display_height_px: int

The height of the display in pixels.

minimum1

display_width_px: int

The width of the display in pixels.

minimum1

name: Literal\["computer"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: Literal\["computer_20241022"\]

Accepts one of the following:

"computer_20241022"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Optional\[int\]

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124: …

display_height_px: int

The height of the display in pixels.

minimum1

display_width_px: int

The width of the display in pixels.

minimum1

name: Literal\["computer"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: Literal\["computer_20250124"\]

Accepts one of the following:

"computer_20250124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Optional\[int\]

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124: …

display_height_px: int

The height of the display in pixels.

minimum1

display_width_px: int

The width of the display in pixels.

minimum1

name: Literal\["computer"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: Literal\["computer_20251124"\]

Accepts one of the following:

"computer_20251124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Optional\[int\]

The X11 display number (e.g. 0, 1) for the display.

minimum0

enable_zoom: Optional\[bool\]

Whether to enable an action to take a zoomed-in screenshot of the screen.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolReferenceBlock: …

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

class BetaToolReferenceBlockParam: …

Tool reference block that can be included in tool_result content.

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaToolResultBlockParam: …

tool_use_id: str

type: Literal\["tool_result"\]

Accepts one of the following:

"tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

content: Optional\[Union\[str, List\[Content\], null\]\]

Accepts one of the following:

ContentUnionMember0 = str

Content = List\[Content\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaSearchResultBlockParam: …

content: List\[[BetaTextBlockParam](/docs/en/api/beta#beta_text_block_param)\]

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

source: str

title: str

type: Literal\["search_result"\]

Accepts one of the following:

"search_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

class BetaRequestDocumentBlock: …

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

class BetaToolReferenceBlockParam: …

Tool reference block that can be included in tool_result content.

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

is_error: Optional\[bool\]

class BetaToolSearchToolBm25_20251119: …

name: Literal\["tool_search_tool_bm25"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_bm25"

type: Literal\["tool_search_tool_bm25_20251119", "tool_search_tool_bm25"\]

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119: …

name: Literal\["tool_search_tool_regex"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_regex"

type: Literal\["tool_search_tool_regex_20251119", "tool_search_tool_regex"\]

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

class BetaToolSearchToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlockParam: …

tool_references: List\[[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolResultErrorParam: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

class BetaToolSearchToolSearchResultBlockParam: …

tool_references: List\[[BetaToolReferenceBlockParam](/docs/en/api/beta#beta_tool_reference_block_param)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

class BetaToolTextEditor20241022: …

name: Literal\["str_replace_editor"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: Literal\["text_editor_20241022"\]

Accepts one of the following:

"text_editor_20241022"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124: …

name: Literal\["str_replace_editor"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: Literal\["text_editor_20250124"\]

Accepts one of the following:

"text_editor_20250124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250429"\]

Accepts one of the following:

"text_editor_20250429"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250728"\]

Accepts one of the following:

"text_editor_20250728"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

max_characters: Optional\[int\]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

BetaToolUnion = [BetaToolUnion](/docs/en/api/beta#beta_tool_union)

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

Accepts one of the following:

class BetaTool: …

input_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal\["object"\]

Accepts one of the following:

"object"

properties: Optional\[Dict\[str, object\]\]

required: Optional\[List\[str\]\]

name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

description: Optional\[str\]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager_input_streaming: Optional\[bool\]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

type: Optional\[Literal\["custom"\]\]

Accepts one of the following:

"custom"

class BetaToolBash20241022: …

name: Literal\["bash"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal\["bash_20241022"\]

Accepts one of the following:

"bash_20241022"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124: …

name: Literal\["bash"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"bash"

type: Literal\["bash_20250124"\]

Accepts one of the following:

"bash_20250124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250522: …

name: Literal\["code_execution"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: Literal\["code_execution_20250522"\]

Accepts one of the following:

"code_execution_20250522"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825: …

name: Literal\["code_execution"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"code_execution"

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20241022: …

display_height_px: int

The height of the display in pixels.

minimum1

display_width_px: int

The width of the display in pixels.

minimum1

name: Literal\["computer"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: Literal\["computer_20241022"\]

Accepts one of the following:

"computer_20241022"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Optional\[int\]

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818: …

name: Literal\["memory"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"memory"

type: Literal\["memory_20250818"\]

Accepts one of the following:

"memory_20250818"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124: …

display_height_px: int

The height of the display in pixels.

minimum1

display_width_px: int

The width of the display in pixels.

minimum1

name: Literal\["computer"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: Literal\["computer_20250124"\]

Accepts one of the following:

"computer_20250124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Optional\[int\]

The X11 display number (e.g. 0, 1) for the display.

minimum0

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022: …

name: Literal\["str_replace_editor"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: Literal\["text_editor_20241022"\]

Accepts one of the following:

"text_editor_20241022"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124: …

display_height_px: int

The height of the display in pixels.

minimum1

display_width_px: int

The width of the display in pixels.

minimum1

name: Literal\["computer"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"computer"

type: Literal\["computer_20251124"\]

Accepts one of the following:

"computer_20251124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

display_number: Optional\[int\]

The X11 display number (e.g. 0, 1) for the display.

minimum0

enable_zoom: Optional\[bool\]

Whether to enable an action to take a zoomed-in screenshot of the screen.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124: …

name: Literal\["str_replace_editor"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_editor"

type: Literal\["text_editor_20250124"\]

Accepts one of the following:

"text_editor_20250124"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250429"\]

Accepts one of the following:

"text_editor_20250429"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728: …

name: Literal\["str_replace_based_edit_tool"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"str_replace_based_edit_tool"

type: Literal\["text_editor_20250728"\]

Accepts one of the following:

"text_editor_20250728"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

input_examples: Optional\[List\[Dict\[str, object\]\]\]

max_characters: Optional\[int\]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

minimum1

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20250305: …

name: Literal\["web_search"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: Literal\["web_search_20250305"\]

Accepts one of the following:

"web_search_20250305"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains: Optional\[List\[str\]\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Optional\[List\[str\]\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

user_location: Optional\[UserLocation\]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal\["approximate"\]

Accepts one of the following:

"approximate"

city: Optional\[str\]

The city of the user.

maxLength255

minLength1

country: Optional\[str\]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional\[str\]

The region of the user.

maxLength255

minLength1

timezone: Optional\[str\]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class BetaWebFetchTool20250910: …

name: Literal\["web_fetch"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_fetch"

type: Literal\["web_fetch_20250910"\]

Accepts one of the following:

"web_fetch_20250910"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains: Optional\[List\[str\]\]

List of domains to allow fetching from

blocked_domains: Optional\[List\[str\]\]

List of domains to block fetching from

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional\[bool\]

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: Optional\[int\]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolBm25_20251119: …

name: Literal\["tool_search_tool_bm25"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_bm25"

type: Literal\["tool_search_tool_bm25_20251119", "tool_search_tool_bm25"\]

Accepts one of the following:

"tool_search_tool_bm25_20251119"

"tool_search_tool_bm25"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119: …

name: Literal\["tool_search_tool_regex"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"tool_search_tool_regex"

type: Literal\["tool_search_tool_regex_20251119", "tool_search_tool_regex"\]

Accepts one of the following:

"tool_search_tool_regex_20251119"

"tool_search_tool_regex"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaMCPToolset: …

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer_loading for all tools from an MCP server, with optional per-tool overrides.

mcp_server_name: str

Name of the MCP server to configure tools for

maxLength255

minLength1

type: Literal\["mcp_toolset"\]

Accepts one of the following:

"mcp_toolset"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

configs: Optional\[Dict\[str, [BetaMCPToolConfig](/docs/en/api/beta#beta_mcp_tool_config)\]\]

Configuration overrides for specific tools, keyed by tool name

defer_loading: Optional\[bool\]

enabled: Optional\[bool\]

default_config: Optional\[BetaMCPToolDefaultConfig\]

Default configuration applied to all tools from this server

defer_loading: Optional\[bool\]

enabled: Optional\[bool\]

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaToolUseBlockParam: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaToolUsesKeep: …

type: Literal\["tool_uses"\]

Accepts one of the following:

"tool_uses"

value: int

class BetaToolUsesTrigger: …

type: Literal\["tool_uses"\]

Accepts one of the following:

"tool_uses"

value: int

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaUsage: …

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

iterations: Optional\[List\[Iteration\]\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

class BetaWebFetchBlockParam: …

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block)

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

class BetaWebFetchTool20250910: …

name: Literal\["web_fetch"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_fetch"

type: Literal\["web_fetch_20250910"\]

Accepts one of the following:

"web_fetch_20250910"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains: Optional\[List\[str\]\]

List of domains to allow fetching from

blocked_domains: Optional\[List\[str\]\]

List of domains to block fetching from

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional\[bool\]

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_content_tokens: Optional\[int\]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

exclusiveMinimum0

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

class BetaWebFetchToolResultBlockParam: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlockParam: …

content: [BetaRequestDocumentBlock](/docs/en/api/beta#beta_request_document_block)

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaContentBlockSource: …

content: Union\[str, List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaContentBlockSourceContent = List\[[BetaContentBlockSourceContent](/docs/en/api/beta#beta_content_block_source_content)\]

Accepts one of the following:

class BetaTextBlockParam: …

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[List\[[BetaTextCitationParam](/docs/en/api/beta#beta_text_citation_param)\]\]

Accepts one of the following:

class BetaCitationCharLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocationParam: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationWebSearchResultLocationParam: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocationParam: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

class BetaImageBlockParam: …

source: Source

Accepts one of the following:

class BetaBase64ImageSource: …

data: str

media_type: Literal\["image/jpeg", "image/png", "image/gif", "image/webp"\]

Accepts one of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaURLImageSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileImageSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["image"\]

Accepts one of the following:

"image"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

type: Literal\["content"\]

Accepts one of the following:

"content"

class BetaURLPDFSource: …

type: Literal\["url"\]

Accepts one of the following:

"url"

url: str

class BetaFileDocumentSource: …

file_id: str

type: Literal\["file"\]

Accepts one of the following:

"file"

type: Literal\["document"\]

Accepts one of the following:

"document"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

citations: Optional\[BetaCitationsConfigParam\]

enabled: Optional\[bool\]

context: Optional\[str\]

title: Optional\[str\]

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchToolResultErrorBlockParam: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

BetaWebFetchToolResultErrorCode = Literal\["invalid_tool_input", "url_too_long", "url_not_allowed", 5 more\]

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

class BetaWebSearchResultBlock: …

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

class BetaWebSearchResultBlockParam: …

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class BetaWebSearchTool20250305: …

name: Literal\["web_search"\]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

"web_search"

type: Literal\["web_search_20250305"\]

Accepts one of the following:

"web_search_20250305"

allowed_callers: Optional\[List\[Literal\["direct", "code_execution_20250825"\]\]\]

Accepts one of the following:

"direct"

"code_execution_20250825"

allowed_domains: Optional\[List\[str\]\]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked_domains: Optional\[List\[str\]\]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

defer_loading: Optional\[bool\]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool_reference from tool search.

max_uses: Optional\[int\]

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: Optional\[bool\]

When true, guarantees schema validation on tool names and inputs

user_location: Optional\[UserLocation\]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal\["approximate"\]

Accepts one of the following:

"approximate"

city: Optional\[str\]

The city of the user.

maxLength255

minLength1

country: Optional\[str\]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: Optional\[str\]

The region of the user.

maxLength255

minLength1

timezone: Optional\[str\]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class BetaWebSearchToolRequestError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

BetaWebSearchToolResultBlockContent = [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

class BetaWebSearchToolResultBlockParam: …

content: [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = List\[[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\]

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class BetaWebSearchToolRequestError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

cache_control: Optional\[BetaCacheControlEphemeral\]

Create a cache control breakpoint at this content block.

type: Literal\["ephemeral"\]

Accepts one of the following:

"ephemeral"

ttl: Optional\[Literal\["5m", "1h"\]\]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

"5m"

"1h"

BetaWebSearchToolResultBlockParamContent = [BetaWebSearchToolResultBlockParamContent](/docs/en/api/beta#beta_web_search_tool_result_block_param_content)

Accepts one of the following:

ResultBlock = List\[[BetaWebSearchResultBlockParam](/docs/en/api/beta#beta_web_search_result_block_param)\]

encrypted_content: str

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

page_age: Optional\[str\]

class BetaWebSearchToolRequestError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

BetaWebSearchToolResultErrorCode = Literal\["invalid_tool_input", "unavailable", "max_uses_exceeded", 3 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

#### MessagesBatches

##### [Create a Message Batch](/docs/en/api/beta/messages/batches/create)

beta.messages.batches.create(BatchCreateParams\*\*kwargs) -\> [BetaMessageBatch](/docs/en/api/beta#beta_message_batch)

post/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/beta/messages/batches/retrieve)

beta.messages.batches.retrieve(strmessage_batch_id, BatchRetrieveParams\*\*kwargs) -\> [BetaMessageBatch](/docs/en/api/beta#beta_message_batch)

get/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/beta/messages/batches/list)

beta.messages.batches.list(BatchListParams\*\*kwargs) -\> SyncPage\[[BetaMessageBatch](/docs/en/api/beta#beta_message_batch)\]

get/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/beta/messages/batches/cancel)

beta.messages.batches.cancel(strmessage_batch_id, BatchCancelParams\*\*kwargs) -\> [BetaMessageBatch](/docs/en/api/beta#beta_message_batch)

post/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/beta/messages/batches/delete)

beta.messages.batches.delete(strmessage_batch_id, BatchDeleteParams\*\*kwargs) -\> [BetaDeletedMessageBatch](/docs/en/api/beta#beta_deleted_message_batch)

delete/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/beta/messages/batches/results)

beta.messages.batches.results(strmessage_batch_id, BatchResultsParams\*\*kwargs) -\> [BetaMessageBatchIndividualResponse](/docs/en/api/beta#beta_message_batch_individual_response)

get/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

class BetaDeletedMessageBatch: …

id: str

ID of the Message Batch.

type: Literal\["message_batch_deleted"\]

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

"message_batch_deleted"

class BetaMessageBatch: …

id: str

Unique object identifier.

The format and length of IDs may change over time.

archived_at: Optional\[datetime\]

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancel_initiated_at: Optional\[datetime\]

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

created_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

ended_at: Optional\[datetime\]

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires_at: datetime

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processing_status: Literal\["in_progress", "canceling", "ended"\]

Processing status of the Message Batch.

Accepts one of the following:

"in_progress"

"canceling"

"ended"

request_counts: [BetaMessageBatchRequestCounts](/docs/en/api/beta#beta_message_batch_request_counts)

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: int

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: int

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: int

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: int

Number of requests in the Message Batch that are processing.

succeeded: int

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results_url: Optional\[str\]

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: Literal\["message_batch"\]

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

"message_batch"

class BetaMessageBatchCanceledResult: …

type: Literal\["canceled"\]

Accepts one of the following:

"canceled"

class BetaMessageBatchErroredResult: …

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response)

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

class BetaInvalidRequestError: …

message: str

type: Literal\["invalid_request_error"\]

Accepts one of the following:

"invalid_request_error"

class BetaAuthenticationError: …

message: str

type: Literal\["authentication_error"\]

Accepts one of the following:

"authentication_error"

class BetaBillingError: …

message: str

type: Literal\["billing_error"\]

Accepts one of the following:

"billing_error"

class BetaPermissionError: …

message: str

type: Literal\["permission_error"\]

Accepts one of the following:

"permission_error"

class BetaNotFoundError: …

message: str

type: Literal\["not_found_error"\]

Accepts one of the following:

"not_found_error"

class BetaRateLimitError: …

message: str

type: Literal\["rate_limit_error"\]

Accepts one of the following:

"rate_limit_error"

class BetaGatewayTimeoutError: …

message: str

type: Literal\["timeout_error"\]

Accepts one of the following:

"timeout_error"

class BetaAPIError: …

message: str

type: Literal\["api_error"\]

Accepts one of the following:

"api_error"

class BetaOverloadedError: …

message: str

type: Literal\["overloaded_error"\]

Accepts one of the following:

"overloaded_error"

request_id: Optional\[str\]

type: Literal\["error"\]

Accepts one of the following:

"error"

type: Literal\["errored"\]

Accepts one of the following:

"errored"

class BetaMessageBatchExpiredResult: …

type: Literal\["expired"\]

Accepts one of the following:

"expired"

class BetaMessageBatchIndividualResponse: …

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom_id: str

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchResult](/docs/en/api/beta#beta_message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult: …

message: [BetaMessage](/docs/en/api/beta#beta_message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

formatdate-time

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockContent = List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

context_management: Optional\[BetaContextManagementResponse\]

Context management response.

Information about context management strategies applied during the request.

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: int

Number of tool uses that were cleared.

minimum0

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: int

Number of thinking turns that were cleared.

minimum0

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: Optional\[BetaStopReason\]

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

iterations: Optional\[List\[Iteration\]\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["succeeded"\]

Accepts one of the following:

"succeeded"

class BetaMessageBatchErroredResult: …

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response)

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

class BetaInvalidRequestError: …

message: str

type: Literal\["invalid_request_error"\]

Accepts one of the following:

"invalid_request_error"

class BetaAuthenticationError: …

message: str

type: Literal\["authentication_error"\]

Accepts one of the following:

"authentication_error"

class BetaBillingError: …

message: str

type: Literal\["billing_error"\]

Accepts one of the following:

"billing_error"

class BetaPermissionError: …

message: str

type: Literal\["permission_error"\]

Accepts one of the following:

"permission_error"

class BetaNotFoundError: …

message: str

type: Literal\["not_found_error"\]

Accepts one of the following:

"not_found_error"

class BetaRateLimitError: …

message: str

type: Literal\["rate_limit_error"\]

Accepts one of the following:

"rate_limit_error"

class BetaGatewayTimeoutError: …

message: str

type: Literal\["timeout_error"\]

Accepts one of the following:

"timeout_error"

class BetaAPIError: …

message: str

type: Literal\["api_error"\]

Accepts one of the following:

"api_error"

class BetaOverloadedError: …

message: str

type: Literal\["overloaded_error"\]

Accepts one of the following:

"overloaded_error"

request_id: Optional\[str\]

type: Literal\["error"\]

Accepts one of the following:

"error"

type: Literal\["errored"\]

Accepts one of the following:

"errored"

class BetaMessageBatchCanceledResult: …

type: Literal\["canceled"\]

Accepts one of the following:

"canceled"

class BetaMessageBatchExpiredResult: …

type: Literal\["expired"\]

Accepts one of the following:

"expired"

class BetaMessageBatchRequestCounts: …

canceled: int

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: int

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: int

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: int

Number of requests in the Message Batch that are processing.

succeeded: int

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

BetaMessageBatchResult = [BetaMessageBatchResult](/docs/en/api/beta#beta_message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult: …

message: [BetaMessage](/docs/en/api/beta#beta_message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

formatdate-time

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockContent = List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

context_management: Optional\[BetaContextManagementResponse\]

Context management response.

Information about context management strategies applied during the request.

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: int

Number of tool uses that were cleared.

minimum0

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: int

Number of thinking turns that were cleared.

minimum0

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: Optional\[BetaStopReason\]

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

iterations: Optional\[List\[Iteration\]\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["succeeded"\]

Accepts one of the following:

"succeeded"

class BetaMessageBatchErroredResult: …

error: [BetaErrorResponse](/docs/en/api/beta#beta_error_response)

error: [BetaError](/docs/en/api/beta#beta_error)

Accepts one of the following:

class BetaInvalidRequestError: …

message: str

type: Literal\["invalid_request_error"\]

Accepts one of the following:

"invalid_request_error"

class BetaAuthenticationError: …

message: str

type: Literal\["authentication_error"\]

Accepts one of the following:

"authentication_error"

class BetaBillingError: …

message: str

type: Literal\["billing_error"\]

Accepts one of the following:

"billing_error"

class BetaPermissionError: …

message: str

type: Literal\["permission_error"\]

Accepts one of the following:

"permission_error"

class BetaNotFoundError: …

message: str

type: Literal\["not_found_error"\]

Accepts one of the following:

"not_found_error"

class BetaRateLimitError: …

message: str

type: Literal\["rate_limit_error"\]

Accepts one of the following:

"rate_limit_error"

class BetaGatewayTimeoutError: …

message: str

type: Literal\["timeout_error"\]

Accepts one of the following:

"timeout_error"

class BetaAPIError: …

message: str

type: Literal\["api_error"\]

Accepts one of the following:

"api_error"

class BetaOverloadedError: …

message: str

type: Literal\["overloaded_error"\]

Accepts one of the following:

"overloaded_error"

request_id: Optional\[str\]

type: Literal\["error"\]

Accepts one of the following:

"error"

type: Literal\["errored"\]

Accepts one of the following:

"errored"

class BetaMessageBatchCanceledResult: …

type: Literal\["canceled"\]

Accepts one of the following:

"canceled"

class BetaMessageBatchExpiredResult: …

type: Literal\["expired"\]

Accepts one of the following:

"expired"

class BetaMessageBatchSucceededResult: …

message: [BetaMessage](/docs/en/api/beta#beta_message)

id: str

Unique object identifier.

The format and length of IDs may change over time.

container: Optional\[BetaContainer\]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires_at: datetime

The time at which the container will expire.

formatdate-time

skills: Optional\[List\[[BetaSkill](/docs/en/api/beta#beta_skill)\]\]

Skills loaded in the container

skill_id: str

Skill ID

maxLength64

minLength1

type: Literal\["anthropic", "custom"\]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version

maxLength64

minLength1

content: List\[[BetaContentBlock](/docs/en/api/beta#beta_content_block)\]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

``` shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

``` shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

``` shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock: …

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal\["thinking"\]

Accepts one of the following:

"thinking"

class BetaRedactedThinkingBlock: …

data: str

type: Literal\["redacted_thinking"\]

Accepts one of the following:

"redacted_thinking"

class BetaToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

type: Literal\["tool_use"\]

Accepts one of the following:

"tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaServerToolUseBlock: …

id: str

input: Dict\[str, object\]

name: Literal\["web_search", "web_fetch", "code_execution", 4 more\]

Accepts one of the following:

"web_search"

"web_fetch"

"code_execution"

"bash_code_execution"

"text_editor_code_execution"

"tool_search_tool_regex"

"tool_search_tool_bm25"

type: Literal\["server_tool_use"\]

Accepts one of the following:

"server_tool_use"

caller: Optional\[Caller\]

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal\["direct"\]

Accepts one of the following:

"direct"

class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool_id: str

type: Literal\["code_execution_20250825"\]

Accepts one of the following:

"code_execution_20250825"

class BetaWebSearchToolResultBlock: …

content: [BetaWebSearchToolResultBlockContent](/docs/en/api/beta#beta_web_search_tool_result_block_content)

Accepts one of the following:

class BetaWebSearchToolResultError: …

error_code: [BetaWebSearchToolResultErrorCode](/docs/en/api/beta#beta_web_search_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"max_uses_exceeded"

"too_many_requests"

"query_too_long"

"request_too_large"

type: Literal\["web_search_tool_result_error"\]

Accepts one of the following:

"web_search_tool_result_error"

UnionMember1 = List\[[BetaWebSearchResultBlock](/docs/en/api/beta#beta_web_search_result_block)\]

encrypted_content: str

page_age: Optional\[str\]

title: str

type: Literal\["web_search_result"\]

Accepts one of the following:

"web_search_result"

url: str

tool_use_id: str

type: Literal\["web_search_tool_result"\]

Accepts one of the following:

"web_search_tool_result"

class BetaWebFetchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock: …

error_code: [BetaWebFetchToolResultErrorCode](/docs/en/api/beta#beta_web_fetch_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"url_too_long"

"url_not_allowed"

"url_not_accessible"

"unsupported_content_type"

"too_many_requests"

"max_uses_exceeded"

"unavailable"

type: Literal\["web_fetch_tool_result_error"\]

Accepts one of the following:

"web_fetch_tool_result_error"

class BetaWebFetchBlock: …

content: [BetaDocumentBlock](/docs/en/api/beta#beta_document_block)

citations: Optional\[BetaCitationConfig\]

Citation configuration for the document

enabled: bool

source: Source

Accepts one of the following:

class BetaBase64PDFSource: …

data: str

media_type: Literal\["application/pdf"\]

Accepts one of the following:

"application/pdf"

type: Literal\["base64"\]

Accepts one of the following:

"base64"

class BetaPlainTextSource: …

data: str

media_type: Literal\["text/plain"\]

Accepts one of the following:

"text/plain"

type: Literal\["text"\]

Accepts one of the following:

"text"

title: Optional\[str\]

The title of the document

type: Literal\["document"\]

Accepts one of the following:

"document"

retrieved_at: Optional\[str\]

ISO 8601 timestamp when the content was retrieved

type: Literal\["web_fetch_result"\]

Accepts one of the following:

"web_fetch_result"

url: str

Fetched content URL

tool_use_id: str

type: Literal\["web_fetch_tool_result"\]

Accepts one of the following:

"web_fetch_tool_result"

class BetaCodeExecutionToolResultBlock: …

content: [BetaCodeExecutionToolResultBlockContent](/docs/en/api/beta#beta_code_execution_tool_result_block_content)

Accepts one of the following:

class BetaCodeExecutionToolResultError: …

error_code: [BetaCodeExecutionToolResultErrorCode](/docs/en/api/beta#beta_code_execution_tool_result_error_code)

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

type: Literal\["code_execution_tool_result_error"\]

Accepts one of the following:

"code_execution_tool_result_error"

class BetaCodeExecutionResultBlock: …

content: List\[[BetaCodeExecutionOutputBlock](/docs/en/api/beta#beta_code_execution_output_block)\]

file_id: str

type: Literal\["code_execution_output"\]

Accepts one of the following:

"code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["code_execution_result"\]

Accepts one of the following:

"code_execution_result"

tool_use_id: str

type: Literal\["code_execution_tool_result"\]

Accepts one of the following:

"code_execution_tool_result"

class BetaBashCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaBashCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"output_file_too_large"

type: Literal\["bash_code_execution_tool_result_error"\]

Accepts one of the following:

"bash_code_execution_tool_result_error"

class BetaBashCodeExecutionResultBlock: …

content: List\[[BetaBashCodeExecutionOutputBlock](/docs/en/api/beta#beta_bash_code_execution_output_block)\]

file_id: str

type: Literal\["bash_code_execution_output"\]

Accepts one of the following:

"bash_code_execution_output"

return_code: int

stderr: str

stdout: str

type: Literal\["bash_code_execution_result"\]

Accepts one of the following:

"bash_code_execution_result"

tool_use_id: str

type: Literal\["bash_code_execution_tool_result"\]

Accepts one of the following:

"bash_code_execution_tool_result"

class BetaTextEditorCodeExecutionToolResultBlock: …

content: Content

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", 2 more\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

"file_not_found"

error_message: Optional\[str\]

type: Literal\["text_editor_code_execution_tool_result_error"\]

Accepts one of the following:

"text_editor_code_execution_tool_result_error"

class BetaTextEditorCodeExecutionViewResultBlock: …

content: str

file_type: Literal\["text", "image", "pdf"\]

Accepts one of the following:

"text"

"image"

"pdf"

num_lines: Optional\[int\]

start_line: Optional\[int\]

total_lines: Optional\[int\]

type: Literal\["text_editor_code_execution_view_result"\]

Accepts one of the following:

"text_editor_code_execution_view_result"

class BetaTextEditorCodeExecutionCreateResultBlock: …

is_file_update: bool

type: Literal\["text_editor_code_execution_create_result"\]

Accepts one of the following:

"text_editor_code_execution_create_result"

class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional\[List\[str\]\]

new_lines: Optional\[int\]

new_start: Optional\[int\]

old_lines: Optional\[int\]

old_start: Optional\[int\]

type: Literal\["text_editor_code_execution_str_replace_result"\]

Accepts one of the following:

"text_editor_code_execution_str_replace_result"

tool_use_id: str

type: Literal\["text_editor_code_execution_tool_result"\]

Accepts one of the following:

"text_editor_code_execution_tool_result"

class BetaToolSearchToolResultBlock: …

content: Content

Accepts one of the following:

class BetaToolSearchToolResultError: …

error_code: Literal\["invalid_tool_input", "unavailable", "too_many_requests", "execution_time_exceeded"\]

Accepts one of the following:

"invalid_tool_input"

"unavailable"

"too_many_requests"

"execution_time_exceeded"

error_message: Optional\[str\]

type: Literal\["tool_search_tool_result_error"\]

Accepts one of the following:

"tool_search_tool_result_error"

class BetaToolSearchToolSearchResultBlock: …

tool_references: List\[[BetaToolReferenceBlock](/docs/en/api/beta#beta_tool_reference_block)\]

tool_name: str

type: Literal\["tool_reference"\]

Accepts one of the following:

"tool_reference"

type: Literal\["tool_search_tool_search_result"\]

Accepts one of the following:

"tool_search_tool_search_result"

tool_use_id: str

type: Literal\["tool_search_tool_result"\]

Accepts one of the following:

"tool_search_tool_result"

class BetaMCPToolUseBlock: …

id: str

input: Dict\[str, object\]

name: str

The name of the MCP tool

server_name: str

The name of the MCP server

type: Literal\["mcp_tool_use"\]

Accepts one of the following:

"mcp_tool_use"

class BetaMCPToolResultBlock: …

content: Union\[str, List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]\]

Accepts one of the following:

ContentUnionMember0 = str

ContentBetaMCPToolResultBlockContent = List\[[BetaTextBlock](/docs/en/api/beta#beta_text_block)\]

citations: Optional\[List\[[BetaTextCitation](/docs/en/api/beta#beta_text_citation)\]\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_char_index: int

file_id: Optional\[str\]

start_char_index: int

type: Literal\["char_location"\]

Accepts one of the following:

"char_location"

class BetaCitationPageLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_page_number: int

file_id: Optional\[str\]

start_page_number: int

type: Literal\["page_location"\]

Accepts one of the following:

"page_location"

class BetaCitationContentBlockLocation: …

cited_text: str

document_index: int

document_title: Optional\[str\]

end_block_index: int

file_id: Optional\[str\]

start_block_index: int

type: Literal\["content_block_location"\]

Accepts one of the following:

"content_block_location"

class BetaCitationsWebSearchResultLocation: …

cited_text: str

encrypted_index: str

title: Optional\[str\]

type: Literal\["web_search_result_location"\]

Accepts one of the following:

"web_search_result_location"

url: str

class BetaCitationSearchResultLocation: …

cited_text: str

end_block_index: int

search_result_index: int

source: str

start_block_index: int

title: Optional\[str\]

type: Literal\["search_result_location"\]

Accepts one of the following:

"search_result_location"

text: str

type: Literal\["text"\]

Accepts one of the following:

"text"

is_error: bool

tool_use_id: str

type: Literal\["mcp_tool_result"\]

Accepts one of the following:

"mcp_tool_result"

class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file_id: str

type: Literal\["container_upload"\]

Accepts one of the following:

"container_upload"

class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid summary (e.g., malformed output from the model). Clients may round-trip compaction blocks with null content; the server treats them as no-ops.

content: Optional\[str\]

Summary of compacted content, or null if compaction failed

type: Literal\["compaction"\]

Accepts one of the following:

"compaction"

context_management: Optional\[BetaContextManagementResponse\]

Context management response.

Information about context management strategies applied during the request.

applied_edits: List\[AppliedEdit\]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_tool_uses: int

Number of tool uses that were cleared.

minimum0

type: Literal\["clear_tool_uses_20250919"\]

The type of context management edit applied.

Accepts one of the following:

"clear_tool_uses_20250919"

class BetaClearThinking20251015EditResponse: …

cleared_input_tokens: int

Number of input tokens cleared by this edit.

minimum0

cleared_thinking_turns: int

Number of thinking turns that were cleared.

minimum0

type: Literal\["clear_thinking_20251015"\]

The type of context management edit applied.

Accepts one of the following:

"clear_thinking_20251015"

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

UnionMember0 = Literal\["claude-opus-4-6", "claude-opus-4-5-20251101", "claude-opus-4-5", 18 more\]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-3-7-sonnet-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-7-sonnet-20250219` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-latest` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-5-haiku-20241022` - Deprecated: Will reach end-of-life on February 19th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-haiku-4-5` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-haiku-4-5-20251001` - Hybrid model, capable of near-instant responses and extended thinking
- `claude-sonnet-4-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-0` - High-performance model with extended thinking
- `claude-4-sonnet-20250514` - High-performance model with extended thinking
- `claude-sonnet-4-5` - Our best model for real-world agents and coding
- `claude-sonnet-4-5-20250929` - Our best model for real-world agents and coding
- `claude-opus-4-0` - Our most capable model
- `claude-opus-4-20250514` - Our most capable model
- `claude-4-opus-20250514` - Our most capable model
- `claude-opus-4-1-20250805` - Our most capable model
- `claude-3-opus-latest` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-opus-20240229` - Deprecated: Will reach end-of-life on January 5th, 2026. Please migrate to a newer model. Visit [https://docs.anthropic.com/en/docs/resources/model-deprecations](https://docs.anthropic.com/en/docs/resources/model-deprecations) for more information.
- `claude-3-haiku-20240307` - Our previous most fast and cost-effective

Accepts one of the following:

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

"claude-3-5-haiku-20241022"

Our fastest model

"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-4-sonnet-20250514"

High-performance model with extended thinking

"claude-sonnet-4-5"

Our best model for real-world agents and coding

"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

"claude-opus-4-0"

Our most capable model

"claude-opus-4-20250514"

Our most capable model

"claude-4-opus-20250514"

Our most capable model

"claude-opus-4-1-20250805"

Our most capable model

"claude-3-opus-latest"

Excels at writing and complex tasks

"claude-3-opus-20240229"

Excels at writing and complex tasks

"claude-3-haiku-20240307"

Our previous most fast and cost-effective

UnionMember1 = str

role: Literal\["assistant"\]

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

"assistant"

stop_reason: Optional\[BetaStopReason\]

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

"end_turn"

"max_tokens"

"stop_sequence"

"tool_use"

"pause_turn"

"compaction"

"refusal"

"model_context_window_exceeded"

stop_sequence: Optional\[str\]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: Literal\["message"\]

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

"message"

usage: [BetaUsage](/docs/en/api/beta#beta_usage)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Optional\[int\]

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Optional\[int\]

The number of input tokens read from the cache.

minimum0

inference_geo: Optional\[str\]

The geographic region where inference was performed for this request.

input_tokens: int

The number of input tokens which were used.

minimum0

iterations: Optional\[List\[Iteration\]\]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (\>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage: …

Token usage for a sampling iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["message"\]

Usage for a sampling iteration

Accepts one of the following:

"message"

class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.

cache_creation: Optional\[BetaCacheCreation\]

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: int

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: int

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: int

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: int

The number of input tokens read from the cache.

minimum0

input_tokens: int

The number of input tokens which were used.

minimum0

output_tokens: int

The number of output tokens which were used.

minimum0

type: Literal\["compaction"\]

Usage for a compaction iteration

Accepts one of the following:

"compaction"

output_tokens: int

The number of output tokens which were used.

minimum0

server_tool_use: Optional\[BetaServerToolUsage\]

The number of server tool requests.

web_fetch_requests: int

The number of web fetch tool requests.

minimum0

web_search_requests: int

The number of web search tool requests.

minimum0

service_tier: Optional\[Literal\["standard", "priority", "batch"\]\]

If the request used the priority, standard, or batch tier.

Accepts one of the following:

"standard"

"priority"

"batch"

type: Literal\["succeeded"\]

Accepts one of the following:

"succeeded"

[](/docs)

[](https://x.com/claudeai)[](https://www.linkedin.com/showcase/claude)[](https://instagram.com/claudeai)

### Solutions

- [AI agents](https://claude.com/solutions/agents)
- [Code modernization](https://claude.com/solutions/code-modernization)
- [Coding](https://claude.com/solutions/coding)
- [Customer support](https://claude.com/solutions/customer-support)
- [Education](https://claude.com/solutions/education)
- [Financial services](https://claude.com/solutions/financial-services)
- [Government](https://claude.com/solutions/government)
- [Life sciences](https://claude.com/solutions/life-sciences)

### Partners

- [Amazon Bedrock](https://claude.com/partners/amazon-bedrock)
- [Google Cloud's Vertex AI](https://claude.com/partners/google-cloud-vertex-ai)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Company

- [Anthropic](https://www.anthropic.com/company)
- [Careers](https://www.anthropic.com/careers)
- [Economic Futures](https://www.anthropic.com/economic-futures)
- [Research](https://www.anthropic.com/research)
- [News](https://www.anthropic.com/news)
- [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)
- [Security and compliance](https://trust.anthropic.com)
- [Transparency](https://www.anthropic.com/transparency)

### Learn

- [Blog](https://claude.com/blog)
- [Catalog](https://claude.ai/catalog/artifacts)
- [Courses](https://www.anthropic.com/learn)
- [Use cases](https://claude.com/resources/use-cases)
- [Connectors](https://claude.com/partners/mcp)
- [Customer stories](https://claude.com/customers)
- [Engineering at Anthropic](https://www.anthropic.com/engineering)
- [Events](https://www.anthropic.com/events)
- [Powered by Claude](https://claude.com/partners/powered-by-claude)
- [Service partners](https://claude.com/partners/services)
- [Startups program](https://claude.com/programs/startups)

### Help and security

- [Availability](https://www.anthropic.com/supported-countries)
- [Status](https://status.claude.com/)
- [Support](https://support.claude.com/)
- [Discord](https://www.anthropic.com/discord)

### Terms and policies

- [Privacy policy](https://www.anthropic.com/legal/privacy)
- [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)
- [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)
- [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)
- [Usage policy](https://www.anthropic.com/legal/aup)
