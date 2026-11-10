---
title: "Remote - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/sessions/remote"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-07T06:23:43Z"
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
4.  [Sessions](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions)

# Remote

Copy page



API version 2026-10-21

##### [List remote sessions](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote/list)

GET/v1/compliance/apps/sessions/remote

List remote sessions (Cowork sessions that run in Anthropic-managed cloud environments) across the organizations the key may read.

##### Models



RemoteListResponse object{ id, agent_id, claude_project_id, 7 more }



Metadata for one remote session, as returned in the list response and in the messages response's `session` field.

Carries session attributes only, not transcript content. Use the messages endpoint to retrieve a session's transcript.

#### Remote[Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote/messages)

##### [Retrieve remote session messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote/messages/list)

GET/v1/compliance/apps/sessions/remote/{claude_remote_session_id}/messages

Retrieve one remote session's transcript: user prompts, assistant responses, and tool calls and results. Thinking blocks and images are not included.
