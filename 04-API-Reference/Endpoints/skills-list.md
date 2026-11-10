---
title: "List Skills - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/skills/list"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:26:53Z"
tags: ["api", "skills"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-skills-list.md).

1.  [API reference](http.md)
2.  [Skills](https://platform.claude.com/docs/en/api/http/skills)

# List Skills

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/skills

List Skills

##### Query parameters



limit: optional number



Number of results to return per page.

Ranges from `1` to `1000`. Defaults to `20`.

default20

minimum1

maximum1000



page: optional string



Pagination token for fetching a specific page of results.

Pass the value from a previous response's `next_page` field to get the next page of results.



source: optional string



Filter skills by source.

If provided, only skills from the specified source will be returned:

- `"custom"`: only return user-created skills
- `"anthropic"`: only return Anthropic-created skills

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

data: array of [Skill](https://platform.claude.com/docs/en/api/http/skills#skill) { type: "skill", id, created_at, 4 more }



List of skills.



type: "skill"



Object type.

For Skills, this is always `"skill"`.

defaultskill



id: string



Unique identifier for the skill.

The format and length of IDs may change over time.



created_at: string



ISO 8601 timestamp of when the skill was created.

formatdate-time

display_name: string



Human-readable, single-line label for the Skill. Maximum 255 characters. Always set: derived from the SKILL.md frontmatter `name` when omitted at creation. Not unique.

latest_version_id: string



ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.



source: [SkillSource](https://platform.claude.com/docs/en/api/http/skills#skill_source) { type }



Where the Skill comes from.

Possible values:

- `"custom"`: authored by the platform user; private to their workspace
- `"anthropic"`: published by Anthropic; shared and read-only
- `"anthropic_example"`: Anthropic-published sample Skill
- `"plugin"`: resolved from an installed plugin

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



updated_at: string



ISO 8601 timestamp of when the skill was last updated.

formatdate-time



next_page: string or null



Token for fetching the next page of results.

If `null`, there are no more results available. Pass this value to the `page` parameter in the next request to get the next page.

List Skills

cURL



```python
curl https://api.anthropic.com/v1/skills \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "display_name",
      "latest_version_id": "latest_version_id",
      "source": {
        "type": "custom"
      },
      "type": "skill",
      "updated_at": "2024-10-30T23:58:27.427722Z"
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
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "display_name",
      "latest_version_id": "latest_version_id",
      "source": {
        "type": "custom"
      },
      "type": "skill",
      "updated_at": "2024-10-30T23:58:27.427722Z"
