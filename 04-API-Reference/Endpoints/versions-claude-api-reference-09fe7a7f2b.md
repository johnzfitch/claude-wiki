---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:03:21Z"
source_url: "https://platform.claude.com/docs/en/api/go/beta/skills/versions"
title: "Versions - Claude API Reference"
---

# Versions

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
