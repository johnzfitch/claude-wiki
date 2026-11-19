---
title: "Code - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/apps/code"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-16T06:24:43Z"
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

# Code

Copy page



API version 2026-10-21

#### Code[Artifacts](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts)

##### [List Code Artifacts](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts/list)

GET/v1/compliance/apps/code/artifacts

List Claude Code Artifacts owned by organizations under the parent organization.

##### [Download Code Artifact Version Content](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts/retrieve_version)

GET/v1/compliance/apps/code/artifacts/{artifact_id}/versions/{version_id}

Streams the content of one version of an Artifact as the response body, in chunks with no `Content-Length`. With `multi_file_format=zip`, a version with more than one file, other than a Claude Doc's or a Claude Sheet's (an Artifact whose `artifact_type` is `claude_docs` or `claude_sheets`), comes back as a ZIP archive of its files.

##### [Download Code Artifact Content](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts/download)

GET/v1/compliance/apps/code/artifacts/{artifact_id}/content

Streams an Artifact's current content as the response body, in chunks with no `Content-Length`.

##### [Delete Code Artifact](https://platform.claude.com/docs/en/api/http/compliance/apps/code/artifacts/delete)

DELETE/v1/compliance/apps/code/artifacts/{artifact_id}

Permanently deletes a Code Artifact and all its versions. This is a destructive operation that cannot be undone. A 200 response means the deletion is initiated and the Artifact is claimed; content removal completes asynchronously.
