---
title: "Get artifact metadata - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:31Z"
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
4.  [Artifacts](https://platform.claude.com/docs/en/api/http/compliance/apps/artifacts)

# Get artifact metadata

Copy page



API version 2026-10-21

GET/v1/compliance/apps/artifacts/{artifact_version_id}

Returns metadata for an artifact version, without the content body.

Use the sibling `/content` endpoint to fetch the artifact text. The `md5` and `size_bytes` fields here are computed over the UTF-8 encoding of that text, so a DLP consumer can dedupe or match hashes without downloading every artifact.

##### Path parameters

artifact_version_id: string



The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

"x-api-key": optional string



##### Returns

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

Get artifact metadata

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "id",
  "artifact_type": "artifact_type",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
  "md5": "md5",
  "size_bytes": 0,
  "title": "title",
  "version_id": "version_id"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "artifact_type": "artifact_type",
  "claude_chat_id": "claude_chat_id",
  "created_at": "2019-12-27T18:11:19.117Z",
