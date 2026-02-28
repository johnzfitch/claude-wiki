---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:05:16Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/beta/skills/delete"
title: "Delete Skill - Claude API Reference"
---
# Delete Skill

beta.skills.delete(skill_id, \*\*kwargs) -\> [SkillDeleteResponse](/docs/en/api/beta#skill_delete_response) { id, type }

DELETE/v1/skills/{skill_id}

Delete Skill

##### ParametersExpand Collapse 

skill_id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

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

class SkillDeleteResponse { id, type }

id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

type: String

Deleted object type.

For Skills, this is always `"skill_deleted"`.

Delete Skill

Ruby

``` shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

skill = anthropic.beta.skills.delete("skill_id")

puts(skill)
```

Response 200

``` shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

##### Returns Examples

Response 200

``` shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
