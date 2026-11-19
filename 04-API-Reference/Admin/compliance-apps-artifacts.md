---
title: "Artifacts - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/artifacts"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:34:32Z"
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

# Artifacts

Copy page



API version 2026-10-21

##### [Get artifact metadata](https://platform.claude.com/docs/en/api/http/compliance/apps/artifacts/retrieve)

GET/v1/compliance/apps/artifacts/{artifact_version_id}

Returns metadata for an artifact version, without the content body.

##### [Download artifact content](https://platform.claude.com/docs/en/api/http/compliance/apps/artifacts/download)

GET/v1/compliance/apps/artifacts/{artifact_version_id}/content

Download the content of an artifact version for compliance purposes.

##### Models



ArtifactRetrieveResponse object{ id, artifact_type, claude_chat_id, 5 more }



Artifact version metadata for GET /v1/compliance/apps/artifacts/{artifact_version_id}.

Returns metadata only. Use the sibling `/content` endpoint to fetch the artifact body.

id: string



Artifact ID e.g. 'claude_artifact_abc123'

artifact_type: string or null



MIME-like artifact type e.g. 'application/vnd.ant.code'

claude_chat_id: string



The chat this artifact belongs to



created_at: string



Artifact version creation timestamp

formatdate-time

md5: string



Lowercase hex MD5 of the artifact content (UTF-8 encoded). Matches the `content` field returned by the sibling `/content` endpoint.

size_bytes: number



Size in bytes of the artifact content (UTF-8 encoded)

title: string or null



Artifact title

version_id: string



Artifact version ID e.g. 'claude_artifact_version_abc123'
