---
title: "Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/skills/versions"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-15T06:23:20Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/skills/versions).

1.  [API reference](http.md)
2.  [Skills](https://platform.claude.com/docs/en/api/http/skills)

# Versions

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Skill Version](https://platform.claude.com/docs/en/api/http/skills/versions/create)

POST/v1/skills/{skill_id}/versions

##### [List Skill Versions](https://platform.claude.com/docs/en/api/http/skills/versions/list)

GET/v1/skills/{skill_id}/versions

##### [Get Skill Version](https://platform.claude.com/docs/en/api/http/skills/versions/retrieve)

GET/v1/skills/{skill_id}/versions/{version}

##### [Delete Skill Version](https://platform.claude.com/docs/en/api/http/skills/versions/delete)

DELETE/v1/skills/{skill_id}/versions/{version}

##### Models



DeletedSkillVersion object{ type: "skill_version_deleted", id }





type: "skill_version_deleted"



Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

defaultskill_version_deleted

id: string



Unique identifier for this Skill Version. The id addresses the version in paths and pins it in references.



SkillVersion object{ type: "skill_version", id, created_at, 3 more }





type: "skill_version"



Object type.

For Skill Versions, this is always `"skill_version"`.

defaultskill_version

id: string



Unique identifier for this Skill Version. The id addresses the version in paths and pins it in references.



created_at: string



ISO 8601 timestamp of when the skill was created.

formatdate-time



description: string



Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

name: string



The Skill's immutable kebab-case slug, set at creation from the first upload's SKILL.md frontmatter `name` (or its enclosing directory). Every later upload must resolve to the same value. Also the top-level directory of the Skill's mounted files and the base name of a downloaded archive.



skill_id: string



Unique identifier for the skill.

The format and length of IDs may change over time.
