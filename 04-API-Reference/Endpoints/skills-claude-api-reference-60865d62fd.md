---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:43:15Z"
source_url: "https://platform.claude.com/docs/en/api/python/beta/skills"
title: "Skills - Claude API Reference"
---
# Skills

##### [Create Skill](/docs/en/api/beta/skills/create)

beta.skills.create(SkillCreateParams\*\*kwargs) -\> [SkillCreateResponse](/docs/en/api/beta#skill_create_response)

POST/v1/skills

##### [List Skills](/docs/en/api/beta/skills/list)

beta.skills.list(SkillListParams\*\*kwargs) -\> SyncPageCursor\[[SkillListResponse](/docs/en/api/beta#skill_list_response)\]

GET/v1/skills

##### [Get Skill](/docs/en/api/beta/skills/retrieve)

beta.skills.retrieve(strskill_id, SkillRetrieveParams\*\*kwargs) -\> [SkillRetrieveResponse](/docs/en/api/beta#skill_retrieve_response)

GET/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/beta/skills/delete)

beta.skills.delete(strskill_id, SkillDeleteParams\*\*kwargs) -\> [SkillDeleteResponse](/docs/en/api/beta#skill_delete_response)

DELETE/v1/skills/{skill_id}

#### SkillsVersions

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
