---
category: "04-API-Reference"
fetched_at: "2026-03-03T14:59:08Z"
source_url: "https://platform.claude.com/docs/en/api/typescript/beta/skills/list"
title: "List Skills - Claude API Reference"
---

# List Skills

client.beta.skills.list(SkillListParams { limit, page, source, betas } params?, RequestOptionsoptions?): PageCursor\<[SkillListResponse](/docs/en/api/beta#skill_list_response) { id, created_at, display_title, 4 more } \>

GET/v1/skills

List Skills

##### ParametersExpand Collapse 

params: SkillListParams { limit, page, source, betas }

limit?: number

Query param: Number of results to return per page.

Maximum value is 100. Defaults to 20.

page?: string \| null

Query param: Pagination token for fetching a specific page of results.

Pass the value from a previous response's `next_page` field to get the next page of results.

source?: string \| null

Query param: Filter skills by source.

If provided, only skills from the specified source will be returned:

- `"custom"`: only return user-created skills
- `"anthropic"`: only return Anthropic-created skills

betas?: Array\<[AnthropicBeta](/docs/en/api/beta#anthropic_beta)\>

Header param: Optional header to specify the beta version(s) you want to use.

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

SkillListResponse { id, created_at, display_title, 4 more }

id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

created_at: string

ISO 8601 timestamp of when the skill was created.

display_title: string \| null

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest_version: string \| null

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: string

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: string

Object type.

For Skills, this is always `"skill"`.

updated_at: string

ISO 8601 timestamp of when the skill was last updated.

List Skills

TypeScript

``` shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const skillListResponse of client.beta.skills.list()) {
  console.log(skillListResponse.id);
}
```

Response 200

``` shiki
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200

``` shiki
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
