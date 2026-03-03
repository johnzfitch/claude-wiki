---
category: "04-API-Reference"
fetched_at: "2026-03-03T15:06:56Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/beta/skills/versions"
title: "Versions - Claude API Reference"
---

# Versions

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
