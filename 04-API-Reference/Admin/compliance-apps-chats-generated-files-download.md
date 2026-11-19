---
title: "Download a Claude-generated file - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/download"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:33:40Z"
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
5.  [Generated Files](https://platform.claude.com/docs/en/api/http/compliance/apps/chats/generated_files)

# Download a Claude-generated file

Copy page



API version 2026-10-21

GET/v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content

Downloads the binary content of a file the assistant created via tool use.

##### Path parameters

claude_gen_file_id: string



The generated-file id (e.g., 'claude_gen_file_abc123') as returned in `chat_messages[].generated_files[].id` from `GET /v1/compliance/apps/chats/{claude_chat_id}/messages`. An id that does not start with `claude_gen_file_` returns a 400 error. `generated_files` can also list ids that start with `claude_file_`; request those from `GET /v1/compliance/apps/chats/files/{claude_file_id}/content` instead.

##### Headers



"anthropic-version": string



The version of the Claude API to use. Send an available version on every request. A request that sends any other value, including an empty one, returns a 400 error. This endpoint treats a request that omits this header as version `2023-06-01`; some other Compliance API endpoints return a 400 error instead.

See [API versions](../Endpoints/versioning.md) for the available versions.

"x-api-key": optional string



Download a Claude-generated file

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/chats/generated-files/$CLAUDE_GEN_FILE_ID/content \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
