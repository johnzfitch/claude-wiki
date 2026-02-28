---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:37:57Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/skills/versions"
title: "Versions - Claude API Reference"
---
# Versions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

client.beta.skills.versions.create(stringskillID, VersionCreateParams { files, betas } params?, RequestOptionsoptions?): [VersionCreateResponse](/docs/en/api/beta#version_create_response) { id, created_at, description, 5 more }

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

client.beta.skills.versions.list(stringskillID, VersionListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor\<[VersionListResponse](/docs/en/api/beta#version_list_response) { id, created_at, description, 5 more } \>

GET/v1/skills/{skill_id}/versions

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

client.beta.skills.versions.retrieve(stringversion, VersionRetrieveParams { skill_id, betas } params, RequestOptionsoptions?): [VersionRetrieveResponse](/docs/en/api/beta#version_retrieve_response) { id, created_at, description, 5 more }

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

client.beta.skills.versions.delete(stringversion, VersionDeleteParams { skill_id, betas } params, RequestOptionsoptions?): [VersionDeleteResponse](/docs/en/api/beta#version_delete_response) { id, type }

DELETE/v1/skills/{skill_id}/versions/{version}
