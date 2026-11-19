---
title: "Create Skill - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/skills/create"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-15T06:23:19Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](platform-claude-com-http-beta-skills-create.md).

1.  [API reference](http.md)
2.  [Skills](https://platform.claude.com/docs/en/api/http/skills)

# Create Skill

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/skills

Create Skill

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

##### Body (form-data)



files: array of file



Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

display_name: optional string or null



Human-readable, single-line label for the Skill. Maximum 255 characters. Always set: derived from the SKILL.md frontmatter `name` when omitted at creation. Not unique.

##### Returns



Skill object{ type: "skill", id, created_at, 4 more }



Create Skill

cURL



```python
curl https://api.anthropic.com/v1/skills \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -F 'files[]=@/path/to/file'
```

Response 200



```python
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
```

##### Returns Examples

Response 200



```python
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
