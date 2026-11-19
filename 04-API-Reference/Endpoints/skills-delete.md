---
title: "Delete Skill - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/skills/delete"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-14T06:25:01Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-skills-delete.md).

1.  [API reference](http.md)
2.  [Skills](https://platform.claude.com/docs/en/api/http/skills)

# Delete Skill

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/skills/{skill_id}

Delete Skill

##### Path parameters



skill_id: string



Unique identifier for the skill.

The format and length of IDs may change over time.

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

Delete Skill

cURL



```python
curl https://api.anthropic.com/v1/skills/$SKILL_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
