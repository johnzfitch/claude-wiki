---
title: "Sessions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/sessions"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-07T06:23:51Z"
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

# Sessions

Copy page



API version 2026-10-21

#### Sessions[Local](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local)

##### [List local sessions](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/list)

GET/v1/compliance/apps/sessions/local

List local sessions across the organizations the key may read.

##### [Retrieve a local session](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/retrieve)

GET/v1/compliance/apps/sessions/local/{local_session_id}

Retrieve one local session.

#### SessionsLocal[Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/messages)

##### [Retrieve local session messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/local/messages/list)

GET/v1/compliance/apps/sessions/local/{local_session_id}/messages

Read one local session's transcript, oldest-first by default.

#### Sessions[Remote](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote)

##### [List remote sessions](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote/list)

GET/v1/compliance/apps/sessions/remote

List remote sessions (Cowork sessions that run in Anthropic-managed cloud environments) across the organizations the key may read.

#### SessionsRemote[Messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote/messages)

##### [Retrieve remote session messages](https://platform.claude.com/docs/en/api/http/compliance/apps/sessions/remote/messages/list)

GET/v1/compliance/apps/sessions/remote/{claude_remote_session_id}/messages

Retrieve one remote session's transcript: user prompts, assistant responses, and tool calls and results. Thinking blocks and images are not included.
