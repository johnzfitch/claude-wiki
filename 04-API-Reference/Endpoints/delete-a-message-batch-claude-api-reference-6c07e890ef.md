---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:36:35Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/messages/batches/delete"
title: "Delete a Message Batch - Claude API Reference"
---
# Delete a Message Batch

client.beta.messages.batches.delete(stringmessageBatchID, BatchDeleteParams { betas } params?, RequestOptionsoptions?): [BetaDeletedMessageBatch](/docs/en/api/beta#beta_deleted_message_batch) { id, type }

DELETE/v1/messages/batches/{message_batch_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse 

messageBatchID: string

ID of the Message Batch.

params: BatchDeleteParams { betas }

betas?: Array\<[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\>

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" \| "prompt-caching-2024-07-31" \| "computer-use-2024-10-22" \| 17 more

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

##### ReturnsExpand Collapse 

BetaDeletedMessageBatch { id, type }

id: string

ID of the Message Batch.

type: "message_batch_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Delete a Message Batch

TypeScript

``` shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaDeletedMessageBatch = await client.beta.messages.batches.delete('message_batch_id');

console.log(betaDeletedMessageBatch.id);
```

Response 200

``` shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

##### Returns Examples

Response 200

``` shiki
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
