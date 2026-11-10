---
title: "Delete file - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/files/delete"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:32Z"
tags: ["api"]
---

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Apps](https://platform.claude.com/docs/en/api/http/compliance/apps)
4.  [Chats](https://platform.claude.com/docs/en/api/http/compliance/apps/chats)
5.  [Files](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/files)

# Delete file

Copy page



API version 2026-10-21

DELETE/v1/compliance/apps/chats/files/{claude_file_id}

Permanently deletes a specific file. This is a destructive operation that cannot be undone.

##### Path parameters

claude_file_id: string



The file ID (tagged ID, e.g., claude_file_abc123)

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



##### Returns



type: optional "claude_file_deleted"



Constant string confirming deletion

defaultclaude_file_deleted

id: string



The ID of the file that was deleted

Delete file

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
