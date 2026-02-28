---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:45:44Z"
source_url: "https://platform.claude.com/docs/en/api/java/messages/batches/delete"
title: "Delete a Message Batch - Claude API Reference"
---
# Delete a Message Batch

[DeletedMessageBatch](/docs/en/api/messages#deleted_message_batch) messages().batches().delete(BatchDeleteParamsparams = BatchDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/messages/batches/{message_batch_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

##### ParametersExpand Collapse 

BatchDeleteParams params

Optional\<String\> messageBatchId

ID of the Message Batch.

##### ReturnsExpand Collapse 

class DeletedMessageBatch:

String id

ID of the Message Batch.

JsonValue; type "message_batch_deleted"constant

"message_batch_deleted"constant

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Delete a Message Batch

Java

``` shiki
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.messages.batches.BatchDeleteParams;
import com.anthropic.models.messages.batches.DeletedMessageBatch;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DeletedMessageBatch deletedMessageBatch = client.messages().batches().delete("message_batch_id");
    }
}
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
