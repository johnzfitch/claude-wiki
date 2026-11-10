---
title: "Download file content - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/files/download"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:01Z"
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

# Download file content

Copy page



API version 2026-10-21

GET/v1/compliance/apps/chats/files/{claude_file_id}/content

Downloads the binary content of a file referenced in chat messages.

##### Path parameters

claude_file_id: string



The file ID (tagged ID, e.g., claude_file_abc123). Also use this endpoint for any id in `chat_messages[].generated_files[].id` that starts with `claude_file_`.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



Download file content

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/chats/files/$CLAUDE_FILE_ID/content \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
