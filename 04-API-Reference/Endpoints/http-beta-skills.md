---
title: "Skills - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/skills"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:35:59Z"
tags: ["api", "skills"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)

# Skills

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Skill](platform-claude-com-http-beta-skills-create.md)

POST/v1/skills

##### [List Skills](platform-claude-com-http-beta-skills-list.md)

GET/v1/skills

##### [Get Skill](platform-claude-com-http-beta-skills-retrieve.md)

GET/v1/skills/{skill_id}

##### [Delete Skill](platform-claude-com-http-beta-skills-delete.md)

DELETE/v1/skills/{skill_id}

##### Models



BetaDeletedSkill object{ type: "skill_deleted", id }





type: "skill_deleted"



Deleted object type.

For Skills, this is always `"skill_deleted"`.

defaultskill_deleted



id: string



Unique identifier for the skill.

The format and length of IDs may change over time.



BetaSkill object{ type: "skill", id, created_at, 4 more }





BetaSkillSource object{ type }





type: "custom" or "anthropic" or "anthropic_example" or "plugin"



Where the Skill comes from.

Possible values:

- `"custom"`: authored by the platform user; private to their workspace
- `"anthropic"`: published by Anthropic; shared and read-only
- `"anthropic_example"`: Anthropic-published sample Skill
- `"plugin"`: resolved from an installed plugin

One of the following:

"custom"



"anthropic"



"anthropic_example"



"plugin"



#### Skills[Versions](https://platform.claude.com/docs/en/api/http/beta/skills/versions)

##### [Create Skill Version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/create)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](https://platform.claude.com/docs/en/api/http/beta/skills/versions/list)

GET/v1/skills/{skill_id}/versions

##### [Download Skill Version Content](https://platform.claude.com/docs/en/api/http/beta/skills/versions/download)

GET/v1/skills/{skill_id}/versions/{version}/content

Download a skill version's content as a zip archive.

##### [Get Skill Version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/retrieve)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/delete)

DELETE/v1/skills/{skill_id}/versions/{version}
