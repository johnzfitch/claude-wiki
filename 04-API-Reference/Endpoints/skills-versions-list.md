---
title: "List Skill Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/skills/versions/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:33:45Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/list).

1.  [API reference](http.md)
2.  [Skills](https://platform.claude.com/docs/en/api/http/skills)
3.  [Versions](https://platform.claude.com/docs/en/api/http/skills/versions)

# List Skill Versions

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/skills/{skill_id}/versions

List Skill Versions

##### Path parameters



skill_id: string



Unique identifier for the skill.

The format and length of IDs may change over time.

##### Query parameters



limit: optional number



Number of results to return per page.

Ranges from `1` to `1000`. Defaults to `20`.

default20

minimum1

maximum1000

page: optional string



Optionally set to the `next_page` token from the previous response.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).



"anthropic-workspace-id": optional string



Optional header to select the Workspace for this request. The value is a Workspace ID (for example, `wrkspc_011CZkZaBF1tNoB5wlCeusgy`).

Only needed for credentials that can act on more than one Workspace. A credential that belongs to a specific Workspace may omit it; if sent, it must match that Workspace.

##### Returns



data: array of [SkillVersion](https://platform.claude.com/docs/en/api/http/skills/versions#skill_version) { type: "skill_version", id, created_at, 3 more }



List of skills.

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



next_page: string or null



Token for fetching the next page of results.

If `null`, there are no more results available. Pass this value to the `page` parameter in the next request to get the next page.

List Skill Versions

cURL



```python
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "description",
      "name": "name",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "skill_version"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "id": "id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "description",
      "name": "name",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
