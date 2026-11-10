---
title: "Batch processing - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/batch-processing"
category: "04-API-Reference/Guides"
fetched_at: "2026-11-05T06:36:39Z"
tags: ["api", "rag"]
---

# Batch processing

Copy page



Process large volumes of Messages requests asynchronously with the Message Batches API, cutting costs by 50 percent and increasing throughput.

Copy page



Batch processing

Feature of  
[Messages API](build-with-claude-working-with-messages.md)

[APIs](#feature-availability)  
Messages APIAvailableManaged AgentsNot available

[Cloud platforms](#availability-feature-support)  
Claude APIAvailableClaude Platform on AWSAvailableClaude Models on Google CloudAnthropic managedAvailable

[Data handling](#feature-data-handling)  
Not ZDR eligibleNot HIPAA eligible

Batch processing is a powerful approach for handling large volumes of requests efficiently. Instead of processing requests one at a time with immediate responses, batch processing allows you to submit multiple requests together for asynchronous processing. This pattern is particularly useful when:

- You need to process large volumes of data
- Immediate responses are not required
- You want to optimize for cost efficiency
- You’re running large-scale evaluations or analyses

The Message Batches API is Anthropic’s first implementation of this pattern.

# Message Batches API

The Message Batches API is a powerful, cost-effective way to asynchronously process large volumes of [Messages](../Endpoints/messages-create.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. requests. This approach is well-suited to tasks that do not require immediate responses, with most batches finishing in less than 1 hour while reducing costs by 50 percent and increasing throughput.

You can [explore the API reference directly](../Endpoints/messages-batches-create.md), in addition to this guide.

## How the Message Batches API works

When you send a request to the Message Batches API:

1.  The system creates a new Message Batch with the provided Messages requests.
2.  The batch is then processed asynchronously, with each request handled independently.
3.  You can poll for the status of the batch and retrieve results when processing has ended for all requests.

This is especially useful for bulk operations that don’t require immediate results, such as:

- Large-scale evaluations: Process thousands of test cases efficiently.
- Content moderation: Analyze large volumes of user-generated content asynchronously.
- Data analysis: Generate insights or summaries for large datasets.
- Bulk content generation: Create large amounts of text for various purposes (for example, product descriptions, article summaries).

### Batch limitations

- A Message Batch is limited to either 100,000 Message requests or 256 MB in size, whichever is reached first.
- The system processes each batch as fast as possible, with most batches completing within 1 hour. You can access batch results when all messages have completed or after 24 hours, whichever comes first. Batches expire if processing does not complete within 24 hours.
- Batch results are available for 29 days after creation. After that, you can still view the Batch, but its results will no longer be available for download.
- Batches are scoped to a [Workspace](../Other/playground.md) in the Claude Console. You may view all batches (and their results) that were created within the Workspace your request runs in.
- Rate limits apply to both Batches API HTTP requests and the number of requests within a batch waiting to be processed. See [Message Batches API rate limits](../Endpoints/rate-limits.md#message-batches-api). Additionally, processing might be slowed down based on current demand and your request volume. In that case, you might see more requests expiring after 24 hours.
- Because of high throughput and concurrent processing, batches may go slightly over the [spend limit](../Other/playground.md) configured in the Claude Console for your Workspace.
- Each batched request must have [`max_tokens`](../Endpoints/messages-create.md#create.max_tokens)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. of at least `1`. `max_tokens: 0` ([cache pre-warming](build-with-claude-prompt-caching.md#pre-warming-the-cache)) is not supported inside a batch, because an ephemeral cache entry written during batch processing would likely expire before the follow-up request runs.

### Supported models

All [active models](../../20-Models/about-claude-models-overview.md) support the Message Batches API.

### What can be batched

Almost any request you can make to the Messages API can be included in a batch. This includes:

- Vision
- Tool use, including all [server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md) (web search, web fetch, code execution, MCP connectors, advisor, and tool search)
- System messages
- Multi-turn conversations
- Extended thinking
- Most beta features

Because each request in the batch is processed independently, you can mix different types of requests within a single batch.

A small number of Messages API parameters are **not** supported in batch requests. Including any of these returns a validation error:

| Parameter | Why |
|----|----|
| `stream: true` | Batch results come back as a single file, not a stream. |
| `speed` ([Fast mode](build-with-claude-fast-mode.md)) | Fast mode tunes synchronous latency, which doesn’t apply to asynchronous batch processing. |
| `fallbacks` ([Server-side fallback](build-with-claude-refusals-and-fallback.md#server-side-fallback)) | Server-side fallback doesn’t apply to batches. To retry refused requests, see [Refusals in Message Batches](build-with-claude-refusals-and-fallback.md#refusals-in-message-batches). |
| `max_tokens: 0` | See [Batch limitations](#batch-limitations). |



Because batches can take longer than 5 minutes to process, consider using the [1-hour cache duration](build-with-claude-prompt-caching.md#1-hour-cache-duration) with prompt caching for better cache hit rates when processing batches with shared context.

## Pricing

The Batches API offers significant cost savings. All usage is charged at 50 percent of the standard API prices.

[TABLE]

## How to use the Message Batches API

### Prepare and create your batch

A Message Batch is composed of a list of requests to create a Message. The shape of an individual request comprises:

- A unique [`custom_id`](../Endpoints/messages-batches-create.md#create.requests.custom_id)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. for identifying the Messages request. Must be 1 to 64 characters and contain only alphanumeric characters, hyphens, and underscores (matching `^[a-zA-Z0-9_-]{1,64}$`).
- A [`params`](../Endpoints/messages-batches-create.md#create.requests.params)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. object with the standard [Messages API](../Endpoints/messages-create.md) parameters

You can [create a batch](../Endpoints/messages-batches-create.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. by passing this list into the `requests` parameter:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

client = anthropic.Anthropic()

message_batch = client.messages.batches.create(
    requests=[
        Request(
            custom_id="my-first-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-5-5",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": "Hello, world",
                    }
                ],
            ),
        ),
        Request(
            custom_id="my-second-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-5-5",
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": "Hi again, friend",
                    }
                ],
            ),
        ),
    ]
)

print(message_batch)
```

In this example, two separate requests are batched together for asynchronous processing. Each request has a unique `custom_id` and contains the standard parameters you’d use for a Messages API call.



**Test your batch requests with the Messages API**

Validation of the `params` object for each message request is performed asynchronously, and validation errors are returned when processing of the entire batch has ended. You can ensure that you are building your input correctly by verifying your request shape with the [Messages API](../Endpoints/messages-create.md) first.

When a batch is first created, the response has a processing status of `in_progress`.

Output



```python
{
  "id": "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
  "type": "message_batch",
  "processing_status": "in_progress",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": null,
  "results_url": null
}
```

### Tracking your batch

The Message Batch’s [`processing_status`](../Endpoints/messages-batches-retrieve.md#message_batch.processing_status)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. field indicates the stage of processing the batch is in. It starts as `in_progress`, then updates to `ended` once all the requests in the batch have finished processing, and results are ready. You can monitor the state of your batch by visiting the [Console](https://platform.claude.com/settings/workspaces/default/batches), or using the retrieval endpoint.

#### [Retrieve a Message Batch](../Endpoints/messages-batches-retrieve.md)

GET/v1/messages/batches/{message_batch_id}

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

##### Path parameters `message_batch_id`

message_batch_id: string



ID of the Message Batch.

##### Headers `anthropic-version` `anthropic-workspace-id`



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns `type` `id` `archived_at` `cancel_initiated_at` `created_at` `ended_at` +4 more



MessageBatch object{ type: "message_batch", id, archived_at, 7 more }



#### Polling for Message Batch completion

To poll a Message Batch, you’ll need its `id`, which is provided in the response when creating a batch or by listing batches. You can implement a polling loop that checks the batch status periodically until processing has ended:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
import time

client = anthropic.Anthropic()

MESSAGE_BATCH_ID = "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d"

message_batch = None
while True:
    message_batch = client.messages.batches.retrieve(MESSAGE_BATCH_ID)
    if message_batch.processing_status == "ended":
        break

    print(f"Batch {MESSAGE_BATCH_ID} is still processing...")
    time.sleep(60)
print(message_batch)
```

### Listing all Message Batches

You can list all Message Batches in your Workspace using the [list endpoint](../Endpoints/messages-batches-list.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.. The API supports pagination, automatically fetching additional pages as needed:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

# Automatically fetches more pages as needed.
for message_batch in client.messages.batches.list(limit=20):
    print(message_batch)
```

### Retrieving batch results

Once batch processing has ended, each Messages request in the batch has a result. There are four result types:

| Result type | Description |
|----|----|
| `succeeded` | Request was successful. Includes the message result. |
| `errored` | Request encountered an error and a message was not created. Possible errors include invalid requests and internal server errors. You will not be billed for these requests. |
| `canceled` | User canceled the batch before this request could be sent to the model. You will not be billed for these requests. |
| `expired` | Batch reached its 24-hour expiration before this request could be sent to the model. You will not be billed for these requests. |

The batch’s `request_counts` object counts the requests still processing and the requests with each result type.



request_counts: [MessageBatchRequestCounts](https://platform.claude.com/docs/en/api/http/messages/batches#message_batch_request_counts) { canceled, errored, expired, 2 more }



Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



canceled: number



Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

default0



errored: number



Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

default0



expired: number



Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

default0



processing: number



Number of requests in the Message Batch that are processing.

default0



succeeded: number



Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

default0

Results of the batch are available for download at the [`results_url`](../Endpoints/messages-batches-retrieve.md#message_batch.results_url)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. property on the Message Batch, and if the organization permission allows, in the Console. Because of the potentially large size of the results, it’s recommended to [stream results](../Endpoints/messages-batches-results.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. back rather than download them all at once.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

# Stream results file in memory-efficient chunks, processing one at a time
for result in client.messages.batches.results(
    "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d",
):
    outcome = result.result
    match outcome.type:
        case "succeeded":
            print(f"Success! {result.custom_id}")
        case "errored":
            if outcome.error.error.type == "invalid_request_error":
                # Request body must be fixed before re-sending request
                print(f"Validation error {result.custom_id}")
            else:
                # Request can be retried directly
                print(f"Server error {result.custom_id}")
        case "expired":
            print(f"Request expired {result.custom_id}")
```

The results are in `.jsonl` format, where each line is a valid JSON object representing the result of a single request in the Message Batch. For each streamed result, you can do something different depending on its `custom_id` and result type. Here is an example set of results:

.jsonl file



```python
{"custom_id":"my-second-request","result":{"type":"succeeded","message":{"id":"msg_014VwiXbi91y3JMjcpyGBHX5","type":"message","role":"assistant","model":"claude-opus-5-5","content":[{"type":"text","text":"Hello again! It's nice to see you. How can I assist you today? Is there anything specific you'd like to chat about or any questions you have?"}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":11,"output_tokens":36}}}}
{"custom_id":"my-first-request","result":{"type":"succeeded","message":{"id":"msg_01FqfsLoHwgeFbguDgpz48m7","type":"message","role":"assistant","model":"claude-opus-5-5","content":[{"type":"text","text":"Hello! How can I assist you today? Feel free to ask me any questions or let me know if there's anything you'd like to chat about."}],"stop_reason":"end_turn","stop_sequence":null,"usage":{"input_tokens":10,"output_tokens":34}}}}
```

If your result has an error, its `result.error` will be set to the standard [error shape](../Endpoints/errors.md#error-shapes).

Batch results use the API version of the request that created the batch.



**Batch results may not match input order**

Batch results can be returned in any order, and may not match the ordering of requests when the batch was created. In the preceding example, the result for the second batch request is returned before the first. To correctly match results with their corresponding requests, always use the `custom_id` field.

### Canceling a Message Batch

You can cancel a Message Batch that is currently processing using the [cancel endpoint](../Endpoints/messages-batches-cancel.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return.. Immediately after cancellation, a batch’s `processing_status` will be `canceling`. You can use the same polling technique described earlier to wait until cancellation is finalized. Canceled batches end up with a status of `ended` and may contain partial results for requests that were processed before cancellation.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client = anthropic.Anthropic()

MESSAGE_BATCH_ID = "msgbatch_01HkcTjaV5uDC8jWR4ZsDV8d"

message_batch = client.messages.batches.cancel(
    MESSAGE_BATCH_ID,
)
print(message_batch)
```

The response shows the batch in a `canceling` state:

Output



```python
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch",
  "processing_status": "canceling",
  "request_counts": {
    "processing": 2,
    "succeeded": 0,
    "errored": 0,
    "canceled": 0,
    "expired": 0
  },
  "ended_at": null,
  "created_at": "2024-09-24T18:37:24.100435Z",
  "expires_at": "2024-09-25T18:37:24.100435Z",
  "cancel_initiated_at": "2024-09-24T18:39:03.114875Z",
  "results_url": null
}
```

### Using prompt caching with Message Batches

The Message Batches API supports prompt caching, allowing you to potentially reduce costs and processing time for batch requests. The pricing discounts from prompt caching and Message Batches can stack, providing even greater cost savings when both features are used together. However, because batch requests are processed asynchronously and concurrently, cache hits are provided on a best-effort basis. Users typically experience cache hit rates ranging from 30 percent to 98 percent, depending on their traffic patterns.

To maximize the likelihood of cache hits in your batch requests:

1.  Include identical `cache_control` blocks in every Message request within your batch.
2.  Maintain a steady stream of requests to prevent cache entries from expiring after their 5-minute lifetime.
3.  Structure your requests to share as much cached content as possible.

Example of implementing prompt caching in a batch:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request

client = anthropic.Anthropic()

message_batch = client.messages.batches.create(
    requests=[
        Request(
            custom_id="my-first-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-5-5",
                max_tokens=1024,
                system=[
                    {
                        "type": "text",
                        "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n",
                    },
                    {
                        "type": "text",
                        "text": "<the entire contents of Pride and Prejudice>",
                        "cache_control": {"type": "ephemeral"},
                    },
                ],
                messages=[
                    {
                        "role": "user",
                        "content": "Analyze the major themes in Pride and Prejudice.",
                    }
                ],
            ),
        ),
        Request(
            custom_id="my-second-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-5-5",
                max_tokens=1024,
                system=[
                    {
                        "type": "text",
                        "text": "You are an AI assistant tasked with analyzing literary works. Your goal is to provide insightful commentary on themes, characters, and writing style.\n",
                    },
                    {
                        "type": "text",
                        "text": "<the entire contents of Pride and Prejudice>",
                        "cache_control": {"type": "ephemeral"},
                    },
                ],
                messages=[
                    {
                        "role": "user",
                        "content": "Write a summary of Pride and Prejudice.",
                    }
                ],
            ),
        ),
    ]
)
```

In this example, both requests in the batch include identical system messages and the full text of Pride and Prejudice marked with `cache_control` to increase the likelihood of cache hits.

### Server tools and the agentic loop

All [server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md) (web search, web fetch, code execution, MCP connectors, advisor, and tool search) work in batch requests. The batch worker runs the same server-side agentic loop as the synchronous Messages API.

Because there is no open connection to maintain, the batch loop can run **more iterations in a turn** than a synchronous request before it returns `stop_reason: "pause_turn"`. If a batch result comes back with `pause_turn`, the turn did not complete; you can continue it by submitting the paused assistant content in a follow-up request (batch or synchronous) exactly as shown in the [pause_turn continuation pattern](../Agents-Tools/agents-and-tools-tool-use-server-tools.md#the-server-side-loop-and-pause-turn).

The batch worker additionally throttles `web_search` for each organization so that highly concurrent batch processing does not exhaust your organization’s web-search rate limit. The batch retries throttled requests automatically; you don’t need to handle this yourself, but very large web-search batches might take longer to complete.

### Extended output (beta)

The `output-300k-2026-03-24` beta header raises the `max_tokens` cap to 300,000 for batch requests using Claude Opus 5.5, Claude Opus 5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, or Claude Haiku 5.5. Include the header to generate outputs far longer than the standard 128k `max_tokens` limit in a single turn.



Extended output is available on the Message Batches API only, not the synchronous Messages API. It is supported on the Claude API and Claude Platform on AWS, and is not currently available on Amazon Bedrock, Claude Models on Google Cloud (Google managed), or Microsoft Foundry.

Use extended output for long-form generation such as book-length drafts and technical documentation, exhaustive structured data extraction, large code-generation scaffolds, and long reasoning chains.

A single 300k-token generation can take over an hour to complete, so plan your batch submissions with the 24-hour processing window in mind. Standard batch pricing (50 percent of standard API prices) applies.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
from anthropic.types.beta.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.beta.messages.batch_create_params import Request

client = anthropic.Anthropic()

message_batch = client.beta.messages.batches.create(
    betas=["output-300k-2026-03-24"],
    requests=[
        Request(
            custom_id="long-form-request",
            params=MessageCreateParamsNonStreaming(
                model="claude-opus-5-5",
                max_tokens=300_000,
                messages=[
                    {
                        "role": "user",
                        "content": "Write a comprehensive technical guide to building distributed systems, covering architecture patterns, consistency models, fault tolerance, and operational best practices.",
                    }
                ],
            ),
        ),
    ],
)

print(message_batch)
```

### Best practices for effective batching

To use the Batches API effectively:

- Monitor batch processing status regularly and implement appropriate retry logic for failed requests.
- Use meaningful `custom_id` values to easily match results with requests, because order is not guaranteed.
- Consider breaking very large datasets into multiple batches for better manageability.
- Dry run a single request shape with the Messages API to avoid validation errors.

### Troubleshooting common issues

If experiencing unexpected behavior:

- Verify that the total batch request size doesn’t exceed 256 MB. If the request size is too large, you might get a 413 `request_too_large` error.
- Check that you’re using [supported models](#supported-models) for all requests in the batch.
- Ensure each request in the batch has a unique `custom_id`.
- Ensure that it has been less than 29 days since batch `created_at` (not processing `ended_at`) time. If over 29 days have passed, results will no longer be viewable.
- Confirm that the batch has not been canceled.

Note that the failure of one request in a batch does not affect the processing of other requests.

## Batch storage and privacy

- **Workspace isolation:** Batches are isolated within the Workspace they are created in. They can only be accessed by API requests in that same Workspace, or users with permission to view Workspace batches in the Console.

- **Result availability:** Batch results are available for 29 days after the batch is created, allowing ample time for retrieval and processing.

## FAQ

### How long does it take for a batch to process?

Batches might take up to 24 hours for processing, but many complete sooner. Actual processing time depends on the size of the batch, current demand, and your request volume. It is possible for a batch to expire and not complete within 24 hours.

### Is the Batches API available for all models?

See [Supported models](#supported-models) for the list of supported models.

### Can I use the Message Batches API with other API features?

Yes, the Message Batches API supports nearly all features available in the Messages API, including most beta features. A small number of parameters (`stream`, `speed`, `fallbacks`, and `max_tokens: 0`) are not supported. See [What can be batched](#what-can-be-batched) for the full list.

### How does the Message Batches API affect pricing?

The Message Batches API offers a 50 percent discount on all usage compared to standard API prices. This applies to input tokens, output tokens, and any special tokens. For more on pricing, visit [Pricing](../../17-Billing-Plans/pricing.md#anthropic-api).

### Can I update a batch after it’s been submitted?

No, once a batch has been submitted, it cannot be modified. If you need to make changes, cancel the current batch and submit a new one. Note that cancellation might not take immediate effect.

### Are there Message Batches API rate limits and do they interact with the Messages API rate limits?

The Message Batches API has HTTP requests-based rate limits in addition to limits on the number of requests in need of processing. See [Message Batches API rate limits](../Endpoints/rate-limits.md#message-batches-api). Usage of the Batches API does not affect rate limits in the Messages API.

### How do I handle errors in my batch requests?

When you retrieve the results, each request has a `result` field indicating whether it `succeeded`, `errored`, was `canceled`, or `expired`. For `errored` results, additional error information is provided. View the error response object in the [API reference](../Endpoints/messages-batches-create.md).

### How does the Message Batches API handle privacy and data separation?

The Message Batches API is designed with strong privacy and data separation measures:

1.  Batches and their results are isolated within the Workspace in which they were created. This means they can only be accessed by API requests in that same Workspace.
2.  Each request within a batch is processed independently, with no data leakage between requests.
3.  Results are only available for a limited time (29 days), and follow Anthropic’s [data retention policy](../../13-Enterprise-Admin/how-long-do-you-store-personal-data.md).
4.  Downloading batch results in the Console can be disabled on the organization level or on a per-workspace basis.

### Can I use prompt caching in the Message Batches API?

Yes, it is possible to use prompt caching with the Message Batches API. However, because asynchronous batch requests can be processed concurrently and in any order, cache hits are provided on a best-effort basis.

## Availability

Batch processing is available on every model.

### API support

[Messages API](build-with-claude-working-with-messages.md)

StatusAvailable

Cloud platforms

- Claude API
- [Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)
- [Claude Models on Google Cloud](build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)Anthropic managed

[Managed Agents](../Other/managed-agents-overview.md)

StatusNot available

### Data handling

[Data handling overview](../Other/manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/messages/batches`

Zero data retentionNot eligible

29-day retention; async storage required. [Learn more](build-with-claude-batch-processing.md#data-retention)

HIPAANot eligible

Batch processing stores request and response data for up to 29 days after batch creation. You can delete a message batch at any time after processing using the [`DELETE /v1/messages/batches/{batch_id}`](../Endpoints/messages-batches-delete.md)Preview with links to the API reference available — press Tab until focus enters the card, Escape to return. endpoint. To delete an in-progress batch, cancel it first. Asynchronous processing requires server-side storage of both inputs and outputs until batch completion and result retrieval.

## Next steps



[Search results](build-with-claude-search-results.md)

Get natural citations for RAG applications by providing search results with source attribution.



[Prompt caching](build-with-claude-prompt-caching.md)

Reduce cost and latency by caching prompt prefixes shared across requests in a batch.
