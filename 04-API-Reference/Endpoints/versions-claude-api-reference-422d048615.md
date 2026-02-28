---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:43:44Z"
source_url: "https://platform.claude.com/docs/en/api/python/beta/skills/versions"
title: "Versions - Claude API Reference"
---
# Versions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

beta.skills.versions.create(strskill_id, VersionCreateParams\*\*kwargs) -\> [VersionCreateResponse](/docs/en/api/beta#version_create_response)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

beta.skills.versions.list(strskill_id, VersionListParams\*\*kwargs) -\> SyncPageCursor\[[VersionListResponse](/docs/en/api/beta#version_list_response)\]

GET/v1/skills/{skill_id}/versions

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

beta.skills.versions.retrieve(strversion, VersionRetrieveParams\*\*kwargs) -\> [VersionRetrieveResponse](/docs/en/api/beta#version_retrieve_response)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

beta.skills.versions.delete(strversion, VersionDeleteParams\*\*kwargs) -\> [VersionDeleteResponse](/docs/en/api/beta#version_delete_response)

DELETE/v1/skills/{skill_id}/versions/{version}
