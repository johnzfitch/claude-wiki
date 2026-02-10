---
category: "04-API-Reference"
fetched_at: "2026-02-07T10:10:23Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/messages/batches"
title: "Batches - Claude API Reference"
---

Copy page

Ruby

# Batches

##### [Create a Message Batch](/docs/en/api/messages/batches/create)

messages.batches.create(\*\*kwargs) -\> [MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more }

post/v1/messages/batches

##### [Retrieve a Message Batch](/docs/en/api/messages/batches/retrieve)

messages.batches.retrieve(message_batch_id) -\> [MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more }

get/v1/messages/batches/{message_batch_id}

##### [List Message Batches](/docs/en/api/messages/batches/list)

messages.batches.list(\*\*kwargs) -\> Page\<[MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more } \>

get/v1/messages/batches

##### [Cancel a Message Batch](/docs/en/api/messages/batches/cancel)

messages.batches.cancel(message_batch_id) -\> [MessageBatch](/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more }

post/v1/messages/batches/{message_batch_id}/cancel

##### [Delete a Message Batch](/docs/en/api/messages/batches/delete)

messages.batches.delete(message_batch_id) -\> [DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch) { id, type }

delete/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](/docs/en/api/messages/batches/results)

messages.batches.results(message_batch_id) -\> [MessageBatchIndividualResponse](/docs/en/api/messages#message_batch_individual_response) { custom_id, result }

get/v1/messages/batches/{message_batch_id}/results

##### ModelsExpand Collapse 

class DeletedMessageBatch { id, type }

id: String

ID of the Message Batch.

type: :message_batch_deleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

:message_batch_deleted

class MessageBatch { id, archived_at, cancel_initiated_at, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

archived_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancel_initiated_at: Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

created_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

ended_at: Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires_at: Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

processing_status: :in_progress \| :canceling \| :ended

Processing status of the Message Batch.

Accepts one of the following:

:in_progress

:canceling

:ended

request_counts: [MessageBatchRequestCounts](/docs/en/api/messages#message_batch_request_counts) { canceled, errored, expired, 2 more }

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.

succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results_url: String

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: :message_batch

Object type.

For Message Batches, this is always `"message_batch"`.

Accepts one of the following:

:message_batch

class MessageBatchCanceledResult { type }

type: :canceled

Accepts one of the following:

:canceled

class MessageBatchErroredResult { error, type }

error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

class InvalidRequestError { message, type }

message: String

type: :invalid_request_error

Accepts one of the following:

:invalid_request_error

class AuthenticationError { message, type }

message: String

type: :authentication_error

Accepts one of the following:

:authentication_error

class BillingError { message, type }

message: String

type: :billing_error

Accepts one of the following:

:billing_error

class PermissionError { message, type }

message: String

type: :permission_error

Accepts one of the following:

:permission_error

class NotFoundError { message, type }

message: String

type: :not_found_error

Accepts one of the following:

:not_found_error

class RateLimitError { message, type }

message: String

type: :rate_limit_error

Accepts one of the following:

:rate_limit_error

class GatewayTimeoutError { message, type }

message: String

type: :timeout_error

Accepts one of the following:

:timeout_error

class APIErrorObject { message, type }

message: String

type: :api_error

Accepts one of the following:

:api_error

class OverloadedError { message, type }

message: String

type: :overloaded_error

Accepts one of the following:

:overloaded_error

request_id: String

type: :error

Accepts one of the following:

:error

type: :errored

Accepts one of the following:

:errored

class MessageBatchExpiredResult { type }

type: :expired

Accepts one of the following:

:expired

class MessageBatchIndividualResponse { custom_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom_id: String

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [MessageBatchResult](/docs/en/api/messages#message_batch_result)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult { message, type }

message: [Message](/docs/en/api/messages#message) { id, content, model, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: Array\[[ContentBlock](/docs/en/api/messages#content_block)\]

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

class TextBlock { citations, text, type }

citations: Array\[[TextCitation](/docs/en/api/messages#text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

Accepts one of the following:

:redacted_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

Accepts one of the following:

:tool_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash\[Symbol, untyped\]

name: :web_search

Accepts one of the following:

:web_search

type: :server_tool_use

Accepts one of the following:

:server_tool_use

class WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :max_uses_exceeded \| 3 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Accepts one of the following:

:web_search_tool_result_error

Array\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

encrypted_content: String

page_age: String

title: String

type: :web_search_result

Accepts one of the following:

:web_search_result

url: String

tool_use_id: String

type: :web_search_tool_result

Accepts one of the following:

:web_search_tool_result

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" \| :"claude-opus-4-5-20251101" \| :"claude-opus-4-5" \| 18 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

stop_reason: [StopReason](/docs/en/api/messages#stop_reason)

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

:end_turn

:max_tokens

:stop_sequence

:tool_use

:pause_turn

:refusal

stop_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

minimum0

inference_geo: String

The geographic region where inference was performed for this request.

input_tokens: Integer

The number of input tokens which were used.

minimum0

output_tokens: Integer

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests }

The number of server tool requests.

web_search_requests: Integer

The number of web search tool requests.

minimum0

service_tier: :standard \| :priority \| :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :succeeded

Accepts one of the following:

:succeeded

class MessageBatchErroredResult { error, type }

error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

class InvalidRequestError { message, type }

message: String

type: :invalid_request_error

Accepts one of the following:

:invalid_request_error

class AuthenticationError { message, type }

message: String

type: :authentication_error

Accepts one of the following:

:authentication_error

class BillingError { message, type }

message: String

type: :billing_error

Accepts one of the following:

:billing_error

class PermissionError { message, type }

message: String

type: :permission_error

Accepts one of the following:

:permission_error

class NotFoundError { message, type }

message: String

type: :not_found_error

Accepts one of the following:

:not_found_error

class RateLimitError { message, type }

message: String

type: :rate_limit_error

Accepts one of the following:

:rate_limit_error

class GatewayTimeoutError { message, type }

message: String

type: :timeout_error

Accepts one of the following:

:timeout_error

class APIErrorObject { message, type }

message: String

type: :api_error

Accepts one of the following:

:api_error

class OverloadedError { message, type }

message: String

type: :overloaded_error

Accepts one of the following:

:overloaded_error

request_id: String

type: :error

Accepts one of the following:

:error

type: :errored

Accepts one of the following:

:errored

class MessageBatchCanceledResult { type }

type: :canceled

Accepts one of the following:

:canceled

class MessageBatchExpiredResult { type }

type: :expired

Accepts one of the following:

:expired

class MessageBatchRequestCounts { canceled, errored, expired, 2 more }

canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.

succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

MessageBatchResult = [MessageBatchSucceededResult](/docs/en/api/messages#message_batch_succeeded_result) { message, type } \| [MessageBatchErroredResult](/docs/en/api/messages#message_batch_errored_result) { error, type } \| [MessageBatchCanceledResult](/docs/en/api/messages#message_batch_canceled_result) { type } \| [MessageBatchExpiredResult](/docs/en/api/messages#message_batch_expired_result) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class MessageBatchSucceededResult { message, type }

message: [Message](/docs/en/api/messages#message) { id, content, model, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: Array\[[ContentBlock](/docs/en/api/messages#content_block)\]

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

class TextBlock { citations, text, type }

citations: Array\[[TextCitation](/docs/en/api/messages#text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

Accepts one of the following:

:redacted_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

Accepts one of the following:

:tool_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash\[Symbol, untyped\]

name: :web_search

Accepts one of the following:

:web_search

type: :server_tool_use

Accepts one of the following:

:server_tool_use

class WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :max_uses_exceeded \| 3 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Accepts one of the following:

:web_search_tool_result_error

Array\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

encrypted_content: String

page_age: String

title: String

type: :web_search_result

Accepts one of the following:

:web_search_result

url: String

tool_use_id: String

type: :web_search_tool_result

Accepts one of the following:

:web_search_tool_result

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" \| :"claude-opus-4-5-20251101" \| :"claude-opus-4-5" \| 18 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

stop_reason: [StopReason](/docs/en/api/messages#stop_reason)

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

:end_turn

:max_tokens

:stop_sequence

:tool_use

:pause_turn

:refusal

stop_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

minimum0

inference_geo: String

The geographic region where inference was performed for this request.

input_tokens: Integer

The number of input tokens which were used.

minimum0

output_tokens: Integer

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests }

The number of server tool requests.

web_search_requests: Integer

The number of web search tool requests.

minimum0

service_tier: :standard \| :priority \| :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :succeeded

Accepts one of the following:

:succeeded

class MessageBatchErroredResult { error, type }

error: [ErrorResponse](/docs/en/api/$shared#error_response) { error, request_id, type }

error: [ErrorObject](/docs/en/api/$shared#error_object)

Accepts one of the following:

class InvalidRequestError { message, type }

message: String

type: :invalid_request_error

Accepts one of the following:

:invalid_request_error

class AuthenticationError { message, type }

message: String

type: :authentication_error

Accepts one of the following:

:authentication_error

class BillingError { message, type }

message: String

type: :billing_error

Accepts one of the following:

:billing_error

class PermissionError { message, type }

message: String

type: :permission_error

Accepts one of the following:

:permission_error

class NotFoundError { message, type }

message: String

type: :not_found_error

Accepts one of the following:

:not_found_error

class RateLimitError { message, type }

message: String

type: :rate_limit_error

Accepts one of the following:

:rate_limit_error

class GatewayTimeoutError { message, type }

message: String

type: :timeout_error

Accepts one of the following:

:timeout_error

class APIErrorObject { message, type }

message: String

type: :api_error

Accepts one of the following:

:api_error

class OverloadedError { message, type }

message: String

type: :overloaded_error

Accepts one of the following:

:overloaded_error

request_id: String

type: :error

Accepts one of the following:

:error

type: :errored

Accepts one of the following:

:errored

class MessageBatchCanceledResult { type }

type: :canceled

Accepts one of the following:

:canceled

class MessageBatchExpiredResult { type }

type: :expired

Accepts one of the following:

:expired

class MessageBatchSucceededResult { message, type }

message: [Message](/docs/en/api/messages#message) { id, content, model, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

content: Array\[[ContentBlock](/docs/en/api/messages#content_block)\]

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

class TextBlock { citations, text, type }

citations: Array\[[TextCitation](/docs/en/api/messages#text_citation)\]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class CitationCharLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_char_index: Integer

file_id: String

start_char_index: Integer

type: :char_location

Accepts one of the following:

:char_location

class CitationPageLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_page_number: Integer

file_id: String

start_page_number: Integer

type: :page_location

Accepts one of the following:

:page_location

class CitationContentBlockLocation { cited_text, document_index, document_title, 4 more }

cited_text: String

document_index: Integer

document_title: String

end_block_index: Integer

file_id: String

start_block_index: Integer

type: :content_block_location

Accepts one of the following:

:content_block_location

class CitationsWebSearchResultLocation { cited_text, encrypted_index, title, 2 more }

cited_text: String

encrypted_index: String

title: String

type: :web_search_result_location

Accepts one of the following:

:web_search_result_location

url: String

class CitationsSearchResultLocation { cited_text, end_block_index, search_result_index, 4 more }

cited_text: String

end_block_index: Integer

search_result_index: Integer

source: String

start_block_index: Integer

title: String

type: :search_result_location

Accepts one of the following:

:search_result_location

text: String

type: :text

Accepts one of the following:

:text

class ThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class RedactedThinkingBlock { data, type }

data: String

type: :redacted_thinking

Accepts one of the following:

:redacted_thinking

class ToolUseBlock { id, input, name, type }

id: String

input: Hash\[Symbol, untyped\]

name: String

type: :tool_use

Accepts one of the following:

:tool_use

class ServerToolUseBlock { id, input, name, type }

id: String

input: Hash\[Symbol, untyped\]

name: :web_search

Accepts one of the following:

:web_search

type: :server_tool_use

Accepts one of the following:

:server_tool_use

class WebSearchToolResultBlock { content, tool_use_id, type }

content: [WebSearchToolResultBlockContent](/docs/en/api/messages#web_search_tool_result_block_content)

Accepts one of the following:

class WebSearchToolResultError { error_code, type }

error_code: :invalid_tool_input \| :unavailable \| :max_uses_exceeded \| 3 more

Accepts one of the following:

:invalid_tool_input

:unavailable

:max_uses_exceeded

:too_many_requests

:query_too_long

:request_too_large

type: :web_search_tool_result_error

Accepts one of the following:

:web_search_tool_result_error

Array\[[WebSearchResultBlock](/docs/en/api/messages#web_search_result_block) { encrypted_content, page_age, title, 2 more } \]

encrypted_content: String

page_age: String

title: String

type: :web_search_result

Accepts one of the following:

:web_search_result

url: String

tool_use_id: String

type: :web_search_tool_result

Accepts one of the following:

:web_search_tool_result

model: [Model](/docs/en/api/messages#model)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" \| :"claude-opus-4-5-20251101" \| :"claude-opus-4-5" \| 18 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

stop_reason: [StopReason](/docs/en/api/messages#stop_reason)

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

:end_turn

:max_tokens

:stop_sequence

:tool_use

:pause_turn

:refusal

stop_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [Usage](/docs/en/api/messages#usage) { cache_creation, cache_creation_input_tokens, cache_read_input_tokens, 5 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache_creation: [CacheCreation](/docs/en/api/messages#cache_creation) { ephemeral_1h_input_tokens, ephemeral_5m_input_tokens }

Breakdown of cached tokens by TTL

ephemeral_1h_input_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral_5m_input_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache_creation_input_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache_read_input_tokens: Integer

The number of input tokens read from the cache.

minimum0

inference_geo: String

The geographic region where inference was performed for this request.

input_tokens: Integer

The number of input tokens which were used.

minimum0

output_tokens: Integer

The number of output tokens which were used.

minimum0

server_tool_use: [ServerToolUsage](/docs/en/api/messages#server_tool_usage) { web_search_requests }

The number of server tool requests.

web_search_requests: Integer

The number of web search tool requests.

minimum0

service_tier: :standard \| :priority \| :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :succeeded

Accepts one of the following:

:succeeded

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
