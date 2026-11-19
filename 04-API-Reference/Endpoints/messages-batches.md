---
title: "Batches - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/messages/batches"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:36:15Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/messages/batches).

1.  [API reference](http.md)
2.  [Messages](https://platform.claude.com/docs/en/api/http/messages)

# Batches

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

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

##### Models



DeletedMessageBatch object{ type: "message_batch_deleted", id }





type: "message_batch_deleted"



Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

defaultmessage_batch_deleted

id: string



ID of the Message Batch.



MessageBatch object{ type: "message_batch", id, archived_at, 7 more }





MessageBatchCanceledResult object{ type: "canceled" }





type: "canceled"



defaultcanceled



MessageBatchErroredResult object{ type: "errored", error }





type: "errored"



defaulterrored



error: [ErrorResponse](https://platform.claude.com/docs/en/api/http/$shared#error_response) { type: "error", error, request_id }





type: "error"



defaulterror



error: [ErrorObject](https://platform.claude.com/docs/en/api/http/$shared#error_object)



One of the following:

request_id: string or null





MessageBatchExpiredResult object{ type: "expired" }





type: "expired"



defaultexpired



MessageBatchIndividualResponse object{ custom_id, result }



This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom_id: string



Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [MessageBatchResult](https://platform.claude.com/docs/en/api/http/messages/batches#message_batch_result)



Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



MessageBatchRequestCounts object{ canceled, errored, expired, 2 more }



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

MessageBatchResult = [MessageBatchSucceededResult](https://platform.claude.com/docs/en/api/http/messages/batches#message_batch_succeeded_result) or [MessageBatchErroredResult](https://platform.claude.com/docs/en/api/http/messages/batches#message_batch_errored_result) or [MessageBatchCanceledResult](https://platform.claude.com/docs/en/api/http/messages/batches#message_batch_canceled_result) or [MessageBatchExpiredResult](https://platform.claude.com/docs/en/api/http/messages/batches#message_batch_expired_result)



Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



MessageBatchSucceededResult object{ type: "succeeded", message }





type: "succeeded"



defaultsucceeded



message: [Message](https://platform.claude.com/docs/en/api/http/messages#message) { type: "message", id, container, 8 more }
