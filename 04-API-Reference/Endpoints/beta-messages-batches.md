---
title: "Batches - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/messages/batches"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-09-26T06:38:44Z"
tags: ["api"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fmessages%2Fbatches)

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


Create a Message Batch


Retrieve a Message Batch


List Message Batches


Cancel a Message Batch


Delete a Message Batch


Retrieve Message Batch results

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

[Rate limits](rate-limits.md)[Service tiers](service-tiers.md)[IAM actions (Claude Platform on AWS)](claude-platform-on-aws-iam-actions.md)[Versions](versioning.md)[IP addresses](ip-addresses.md)[Supported regions](supported-regions.md)

Claude Code

[Trigger a routine](claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](http.md)
2.  [Beta](http-beta.md)
3.  [Messages](http-beta-messages.md)

# Batches

##### [Create a Message Batch](https://platform.claude.com/docs/en/api/http/beta/messages/batches/create)

POST/v1/messages/batches

Send a batch of Message creation requests.

##### [Retrieve a Message Batch](https://platform.claude.com/docs/en/api/http/beta/messages/batches/retrieve)

GET/v1/messages/batches/{message_batch_id}

This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.

##### [List Message Batches](https://platform.claude.com/docs/en/api/http/beta/messages/batches/list)

GET/v1/messages/batches

List all Message Batches within a Workspace. Most recently created batches are returned first.

##### [Cancel a Message Batch](https://platform.claude.com/docs/en/api/http/beta/messages/batches/cancel)

POST/v1/messages/batches/{message_batch_id}/cancel

Batches may be canceled any time before processing ends. Once cancellation is initiated, the batch enters a `canceling` state, at which time the system may complete any in-progress, non-interruptible requests before finalizing cancellation.

##### [Delete a Message Batch](https://platform.claude.com/docs/en/api/http/beta/messages/batches/delete)

DELETE/v1/messages/batches/{message_batch_id}

##### [Retrieve Message Batch results](https://platform.claude.com/docs/en/api/http/beta/messages/batches/results)

GET/v1/messages/batches/{message_batch_id}/results

Streams the results of a Message Batch as a `.jsonl` file.

##### Models



BetaDeletedMessageBatch object{ type: "message_batch_deleted", id }

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

BetaMessageBatch object{ type: "message_batch", id, archived_at, 7 more }





BetaMessageBatchCanceledResult object{ type: "canceled" }





type: "canceled"



defaultcanceled



BetaMessageBatchErroredResult object{ type: "errored", error }





type: "errored"



defaulterrored



error: [BetaErrorResponse](http-beta.md#beta_error_response) { type: "error", error, request_id }





type: "error"



defaulterror



error: [BetaError](http-beta.md#beta_error)



One of the following:

request_id: string or null





BetaMessageBatchExpiredResult object{ type: "expired" }





type: "expired"



defaultexpired



BetaMessageBatchIndividualResponse object{ custom_id, result }



This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom_id: string



Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [BetaMessageBatchResult](https://platform.claude.com/docs/en/api/http/beta/messages/batches#beta_message_batch_result)



Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



BetaMessageBatchRequestCounts object{ canceled, errored, expired, 2 more }

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

BetaMessageBatchResult = [BetaMessageBatchSucceededResult](https://platform.claude.com/docs/en/api/http/beta/messages/batches#beta_message_batch_succeeded_result) or [BetaMessageBatchErroredResult](https://platform.claude.com/docs/en/api/http/beta/messages/batches#beta_message_batch_errored_result) or [BetaMessageBatchCanceledResult](https://platform.claude.com/docs/en/api/http/beta/messages/batches#beta_message_batch_canceled_result) or [BetaMessageBatchExpiredResult](https://platform.claude.com/docs/en/api/http/beta/messages/batches#beta_message_batch_expired_result)



Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



BetaMessageBatchSucceededResult object{ type: "succeeded", message }





type: "succeeded"



defaultsucceeded



message: [BetaMessage](http-beta-messages.md#beta_message) { type: "message", id, container, 10 more }
