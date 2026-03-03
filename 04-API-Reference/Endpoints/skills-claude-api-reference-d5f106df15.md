---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:03:18Z"
source_url: "https://platform.claude.com/docs/en/api/go/beta/skills"
title: "Skills - Claude API Reference"
---

# Skills

##### [Create Skill](/docs/en/api/beta/skills/create)

client.Beta.Skills.New(ctx, params) (\*[BetaSkillNewResponse](/docs/en/api/beta#BetaSkillNewResponse), error)

POST/v1/skills

##### [List Skills](/docs/en/api/beta/skills/list)

client.Beta.Skills.List(ctx, params) (\*PageCursor\[[BetaSkillListResponse](/docs/en/api/beta#BetaSkillListResponse)\], error)

GET/v1/skills

##### [Get Skill](/docs/en/api/beta/skills/retrieve)

client.Beta.Skills.Get(ctx, skillID, query) (\*[BetaSkillGetResponse](/docs/en/api/beta#BetaSkillGetResponse), error)

GET/v1/skills/{skill_id}

##### [Delete Skill](/docs/en/api/beta/skills/delete)

client.Beta.Skills.Delete(ctx, skillID, body) (\*[BetaSkillDeleteResponse](/docs/en/api/beta#BetaSkillDeleteResponse), error)

DELETE/v1/skills/{skill_id}

#### SkillsVersions

##### [Create Skill Version](/docs/en/api/beta/skills/versions/create)

client.Beta.Skills.Versions.New(ctx, skillID, params) (\*[BetaSkillVersionNewResponse](/docs/en/api/beta#BetaSkillVersionNewResponse), error)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](/docs/en/api/beta/skills/versions/list)

client.Beta.Skills.Versions.List(ctx, skillID, params) (\*PageCursor\[[BetaSkillVersionListResponse](/docs/en/api/beta#BetaSkillVersionListResponse)\], error)

GET/v1/skills/{skill_id}/versions

##### [Get Skill Version](/docs/en/api/beta/skills/versions/retrieve)

client.Beta.Skills.Versions.Get(ctx, version, params) (\*[BetaSkillVersionGetResponse](/docs/en/api/beta#BetaSkillVersionGetResponse), error)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](/docs/en/api/beta/skills/versions/delete)

client.Beta.Skills.Versions.Delete(ctx, version, params) (\*[BetaSkillVersionDeleteResponse](/docs/en/api/beta#BetaSkillVersionDeleteResponse), error)

DELETE/v1/skills/{skill_id}/versions/{version}
