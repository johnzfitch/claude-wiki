---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:01:33Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/messages/batches/delete"
title: "Delete a Message Batch - Claude API Reference"
---
# Delete a Message Batch

messages.batches.delete(message_batch_id) -\> [DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch) { id, type }

DELETE/v1/messages/batches/{message_batch_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse 

message_batch_id: String

ID of the Message Batch.

##### ReturnsExpand Collapse 

class DeletedMessageBatch { id, type }

id: String

ID of the Message Batch.

type: :message_batch_deleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Delete a Message Batch

Ruby

``` shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

deleted_message_batch = anthropic.messages.batches.delete("message_batch_id")

puts(deleted_message_batch)
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
