---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:20:15Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/messages/batches/delete"
title: "Delete a Message Batch - Claude API Reference"
---
# Delete a Message Batch

[DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch) Messages.Batches.Delete(BatchDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/messages/batches/{message_batch_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse 

BatchDeleteParams parameters

required string messageBatchID

ID of the Message Batch.

##### ReturnsExpand Collapse 

class DeletedMessageBatch:

required string ID

ID of the Message Batch.

JsonElement Type "message_batch_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Delete a Message Batch

C#

``` shiki
BatchDeleteParams parameters = new() { MessageBatchID = "message_batch_id" };

var deletedMessageBatch = await client.Messages.Batches.Delete(parameters);

Console.WriteLine(deletedMessageBatch);
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
