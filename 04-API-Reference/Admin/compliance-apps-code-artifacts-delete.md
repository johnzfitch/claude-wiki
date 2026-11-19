---
title: "Delete Code Artifact - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/code/artifacts/delete"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-16T06:24:40Z"
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
4.  [Code](https://platform.claude.com/docs/en/api/http/compliance/apps/code)
5.  [Artifacts](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts)

# Delete Code Artifact

Copy page



API version 2026-10-21

DELETE/v1/compliance/apps/code/artifacts/{artifact_id}

Permanently deletes a Code Artifact and all its versions. This is a destructive operation that cannot be undone. A 200 response means the deletion is initiated and the Artifact is claimed; content removal completes asynchronously.

Returns 404 for Artifacts that don't exist or belong to another parent organization. Returns 404 on a repeated delete of an already-deleted Artifact.

##### Path parameters

artifact_id: string



The Artifact ID (tagged ID, e.g., cart_abc123)

##### Headers



"anthropic-version": string



The version of the Claude API to use. Send an available version on every request. A request that sends any other value, including an empty one, returns a 400 error. This endpoint treats a request that omits this header as version `2023-06-01`; some other Compliance API endpoints return a 400 error instead.

See [API versions](../Endpoints/versioning.md) for the available versions.

"x-api-key": optional string



##### Returns



type: "code_artifact_deleted"



Constant string confirming deletion

defaultcode_artifact_deleted

id: string



The ID of the Artifact that was deleted

Delete Code Artifact

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/code/artifacts/$ARTIFACT_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "cart_xyz789",
  "type": "code_artifact_deleted"
