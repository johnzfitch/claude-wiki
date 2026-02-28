---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:04:58Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/beta/skills/create"
title: "Create Skill - Claude API Reference"
---
# Create Skill

beta.skills.create(\*\*kwargs) -\> [SkillCreateResponse](/docs/en/api/beta#skill_create_response) { id, created_at, display_title, 4 more }

POST/v1/skills

Create Skill

##### ParametersExpand Collapse 

display_title: String

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

files: Array\[String\]

Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

anthropic_beta: Array\[[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" \| :"prompt-caching-2024-07-31" \| :"computer-use-2024-10-22" \| 17 more

Accepts one of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

##### ReturnsExpand Collapse 

class SkillCreateResponse { id, created_at, display_title, 4 more }

id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

created_at: String

ISO 8601 timestamp of when the skill was created.

display_title: String

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest_version: String

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: String

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: String

Object type.

For Skills, this is always `"skill"`.

updated_at: String

ISO 8601 timestamp of when the skill was last updated.

Create Skill

Ruby

``` shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

skill = anthropic.beta.skills.create

puts(skill)
```

Response 200

``` shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200

``` shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
