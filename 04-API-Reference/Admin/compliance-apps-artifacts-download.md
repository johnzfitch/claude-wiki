---
title: "Download artifact content - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/artifacts/download"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:36:08Z"
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

# Download artifact content

Copy page



API version 2026-10-21

GET/v1/compliance/apps/artifacts/{artifact_version_id}/content

Download the content of an artifact version for compliance purposes.

Returns the full text content of the artifact version.

##### Path parameters

artifact_version_id: string



The artifact version ID (tagged ID, e.g., claude_artifact_version_abc123)

##### Headers



"anthropic-version": string



The version of the Claude API to use. Send an available version on every request. A request that sends any other value, including an empty one, returns a 400 error. This endpoint treats a request that omits this header as version `2023-06-01`; some other Compliance API endpoints return a 400 error instead.

See [API versions](../Endpoints/versioning.md) for the available versions.

"x-api-key": optional string



Download artifact content

cURL



```python
curl https://api.anthropic.com/v1/compliance/apps/artifacts/$ARTIFACT_VERSION_ID/content \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
