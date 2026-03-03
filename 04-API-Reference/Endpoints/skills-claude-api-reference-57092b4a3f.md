---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:04:30Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/beta/skills"
title: "Skills - Claude API Reference"
---

# Skills

##### [Create Skill](/docs/en/api/beta/skills/create)

beta.skills.create(\*\*kwargs) -\> [SkillCreateResponse](/docs/en/api/beta#skill_create_response) { id, created_at, display_title, 4 more }

POST/v1/skills

##### [List Skills](/docs/en/api/beta/skills/list)

beta.skills.list(\*\*kwargs) -\> PageCursor\<[SkillListResponse](/docs/en/api/beta#skill_list_response) { id, created_at, display_title, 4 more } \>

GET/v1/skills

##### [Get Skill](/docs/en/api/beta/skills/retrieve)

beta.skills.retrieve(skill_id, \*\*kwargs) -\> [SkillRetrieveResponse](/docs/en/api/beta#skill_retrieve_response) { id, created_at, display_title, 4 more }

GET/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/beta/skills/delete)

beta.skills.delete(skill_id, \*\*kwargs) -\> [SkillDeleteResponse](/docs/en/api/beta#skill_delete_response) { id, type }

DELETE/v1/skills/{skill_id}

#### SkillsVersions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

beta.skills.versions.create(skill_id, \*\*kwargs) -\> [VersionCreateResponse](/docs/en/api/beta#version_create_response) { id, created_at, description, 5 more }

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

beta.skills.versions.list(skill_id, \*\*kwargs) -\> PageCursor\<[VersionListResponse](/docs/en/api/beta#version_list_response) { id, created_at, description, 5 more } \>

GET/v1/skills/{skill_id}/versions

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

beta.skills.versions.retrieve(version, \*\*kwargs) -\> [VersionRetrieveResponse](/docs/en/api/beta#version_retrieve_response) { id, created_at, description, 5 more }

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

beta.skills.versions.delete(version, \*\*kwargs) -\> [VersionDeleteResponse](/docs/en/api/beta#version_delete_response) { id, type }

DELETE/v1/skills/{skill_id}/versions/{version}
