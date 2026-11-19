---
title: "List Message Batches - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/messages/batches/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:36:16Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/messages/batches/list).

1.  [API reference](http.md)
2.  [Messages](https://platform.claude.com/docs/en/api/http/messages)
3.  [Batches](https://platform.claude.com/docs/en/api/http/messages/batches)

# List Message Batches

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/messages/batches

List all Message Batches within a Workspace. Most recently created batches are returned first.

Learn more about the Message Batches API in our [user guide](../Guides/build-with-claude-batch-processing.md)

##### Query parameters

after_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

before_id: optional string



ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.



limit: optional number



Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

default20

minimum1

maximum1000

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



data: array of [MessageBatch](https://platform.claude.com/docs/en/api/http/messages/batches#message_batch) { type: "message_batch", id, archived_at, 7 more }





type: "message_batch"



Object type.

For Message Batches, this is always `"message_batch"`.

defaultmessage_batch



id: string



Unique object identifier.

The format and length of IDs may change over time.



archived_at: string or null



RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time



cancel_initiated_at: string or null



RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time



created_at: string



RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time



ended_at: string or null



RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time



expires_at: string



RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time



processing_status: "in_progress" or "canceling" or "ended"



Processing status of the Message Batch.

One of the following:

"in_progress"



"canceling"



"ended"



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



results_url: string or null



URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

first_id: string or null



First ID in the `data` list. Can be used as the `before_id` for the previous page.

has_more: boolean



Indicates if there are more results in the requested page direction.

last_id: string or null



Last ID in the `data` list. Can be used as the `after_id` for the next page.

List Message Batches

cURL



```python
curl https://api.anthropic.com/v1/messages/batches \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "archived_at": "2024-08-20T18:37:24.100435Z",
      "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
      "created_at": "2024-08-20T18:37:24.100435Z",
      "ended_at": "2024-08-20T18:37:24.100435Z",
      "expires_at": "2024-08-20T18:37:24.100435Z",
      "processing_status": "in_progress",
      "request_counts": {
        "canceled": 10,
        "errored": 30,
        "expired": 10,
        "processing": 100,
        "succeeded": 50
      },
      "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
      "type": "message_batch"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
      "archived_at": "2024-08-20T18:37:24.100435Z",
      "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
      "created_at": "2024-08-20T18:37:24.100435Z",
      "ended_at": "2024-08-20T18:37:24.100435Z",
      "expires_at": "2024-08-20T18:37:24.100435Z",
      "processing_status": "in_progress",
      "request_counts": {
        "canceled": 10,
        "errored": 30,
        "expired": 10,
        "processing": 100,
        "succeeded": 50
      },
      "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
