---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:37:51Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/skills/delete"
title: "Delete Skill - Claude API Reference"
---
# Delete Skill

client.beta.skills.delete(stringskillID, SkillDeleteParams { betas } params?, RequestOptionsoptions?): [SkillDeleteResponse](/docs/en/api/beta#skill_delete_response) { id, type }

DELETE/v1/skills/{skill_id}

Delete Skill

##### ParametersExpand Collapse 

skillID: string

Unique identifier for the skill.

The format and length of IDs may change over time.

params: SkillDeleteParams { betas }

betas?: Array\<[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\>

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" \| "prompt-caching-2024-07-31" \| "computer-use-2024-10-22" \| 17 more

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

##### ReturnsExpand Collapse 

SkillDeleteResponse { id, type }

id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

type: string

Deleted object type.

For Skills, this is always `"skill_deleted"`.

Delete Skill

TypeScript

``` shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const skill = await client.beta.skills.delete('skill_id');

console.log(skill.id);
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
