---
title: "Delete Skill Version - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/skills/versions/delete"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-06T06:26:54Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/skills/versions/delete).

1.  [API reference](http.md)
2.  [Skills](https://platform.claude.com/docs/en/api/http/skills)
3.  [Versions](https://platform.claude.com/docs/en/api/http/skills/versions)

# Delete Skill Version

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/skills/{skill_id}/versions/{version}

Delete Skill Version

##### Path parameters



skill_id: string



Unique identifier for the skill.

The format and length of IDs may change over time.



version: string



Identifies the skill version by its version ID.

Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

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

Delete Skill Version

cURL



```python
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions/$VERSION \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "id",
  "type": "skill_version_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "type": "skill_version_deleted"
