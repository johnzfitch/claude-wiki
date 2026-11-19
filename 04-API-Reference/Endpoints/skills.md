---
title: "Skills - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/skills"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-14T06:25:39Z"
tags: ["api", "skills"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-skills.md).

1.  [API reference](http.md)

# Skills

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Skill](https://platform.claude.com/docs/en/api/http/skills/create)

POST/v1/skills

##### [List Skills](https://platform.claude.com/docs/en/api/http/skills/list)

GET/v1/skills

##### [Get Skill](https://platform.claude.com/docs/en/api/http/skills/retrieve)

GET/v1/skills/{skill_id}

##### [Delete Skill](https://platform.claude.com/docs/en/api/http/skills/delete)

DELETE/v1/skills/{skill_id}

##### Models



DeletedSkill object{ type: "skill_deleted", id }

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

Skill object{ type: "skill", id, created_at, 4 more }





SkillReadBlockedUndecryptableErrorDetails object{ error_code }



A custom skill the request names is stored under an encryption key state the workspace cannot currently decrypt.

error_code: "skill_read_blocked_undecryptable"





SkillSource object{ type }

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

#### Skills[Versions](https://platform.claude.com/docs/en/api/http/skills/versions)

##### [Create Skill Version](https://platform.claude.com/docs/en/api/http/skills/versions/create)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](https://platform.claude.com/docs/en/api/http/skills/versions/list)

GET/v1/skills/{skill_id}/versions

##### [Get Skill Version](https://platform.claude.com/docs/en/api/http/skills/versions/retrieve)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](https://platform.claude.com/docs/en/api/http/skills/versions/delete)

DELETE/v1/skills/{skill_id}/versions/{version}
