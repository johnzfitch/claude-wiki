---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:23:37Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/beta/skills"
title: "Skills - Claude API Reference"
---
# Skills

##### [Create Skill](/docs/en/api/beta/skills/create)

[SkillCreateResponse](/docs/en/api/beta#SkillCreateResponse) Beta.Skills.Create(SkillCreateParams?parameters, CancellationTokencancellationToken = default)

POST/v1/skills

##### [List Skills](/docs/en/api/beta/skills/list)

[SkillListPageResponse](/docs/en/api/beta#SkillListPageResponse) Beta.Skills.List(SkillListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/skills

##### [Get Skill](/docs/en/api/beta/skills/retrieve)

[SkillRetrieveResponse](/docs/en/api/beta#SkillRetrieveResponse) Beta.Skills.Retrieve(SkillRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/beta/skills/delete)

[SkillDeleteResponse](/docs/en/api/beta#SkillDeleteResponse) Beta.Skills.Delete(SkillDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill_id}

#### SkillsVersions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

[VersionCreateResponse](/docs/en/api/beta#VersionCreateResponse) Beta.Skills.Versions.Create(VersionCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

[VersionListPageResponse](/docs/en/api/beta#VersionListPageResponse) Beta.Skills.Versions.List(VersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill_id}/versions

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

[VersionRetrieveResponse](/docs/en/api/beta#VersionRetrieveResponse) Beta.Skills.Versions.Retrieve(VersionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

[VersionDeleteResponse](/docs/en/api/beta#VersionDeleteResponse) Beta.Skills.Versions.Delete(VersionDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/skills/{skill_id}/versions/{version}
