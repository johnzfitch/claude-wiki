---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:49:06Z"
source_url: "https://platform.claude.com/docs/en/api/java/beta/skills"
title: "Skills - Claude API Reference"
---
# Skills

##### [Create Skill](/docs/en/api/beta/skills/create)

[SkillCreateResponse](/docs/en/api/beta#SkillCreateResponse) beta().skills().create(SkillCreateParamsparams = SkillCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/skills

##### [List Skills](/docs/en/api/beta/skills/list)

SkillListPage beta().skills().list(SkillListParamsparams = SkillListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills

##### [Get Skill](/docs/en/api/beta/skills/retrieve)

[SkillRetrieveResponse](/docs/en/api/beta#SkillRetrieveResponse) beta().skills().retrieve(SkillRetrieveParamsparams = SkillRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/beta/skills/delete)

[SkillDeleteResponse](/docs/en/api/beta#SkillDeleteResponse) beta().skills().delete(SkillDeleteParamsparams = SkillDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/skills/{skill_id}

#### SkillsVersions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

[VersionCreateResponse](/docs/en/api/beta#VersionCreateResponse) beta().skills().versions().create(VersionCreateParamsparams = VersionCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

VersionListPage beta().skills().versions().list(VersionListParamsparams = VersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills/{skill_id}/versions

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

[VersionRetrieveResponse](/docs/en/api/beta#VersionRetrieveResponse) beta().skills().versions().retrieve(VersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

[VersionDeleteResponse](/docs/en/api/beta#VersionDeleteResponse) beta().skills().versions().delete(VersionDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/skills/{skill_id}/versions/{version}
