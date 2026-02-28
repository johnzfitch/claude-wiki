---
category: "04-API-Reference"
fetched_at: "2026-02-22T13:43:27Z"
source_url: "https://platform.claude.com/docs/en/api/python/beta/skills/list"
title: "List Skills - Claude API Reference"
---
# List Skills

beta.skills.list(SkillListParams\*\*kwargs) -\> SyncPageCursor\[[SkillListResponse](/docs/en/api/beta#skill_list_response)\]

GET/v1/skills

List Skills

##### ParametersExpand Collapse 

limit: Optional\[int\]

Number of results to return per page.

Maximum value is 100. Defaults to 20.

page: Optional\[str\]

Pagination token for fetching a specific page of results.

Pass the value from a previous response's `next_page` field to get the next page of results.

source: Optional\[str\]

Filter skills by source.

If provided, only skills from the specified source will be returned:

- `"custom"`: only return user-created skills
- `"anthropic"`: only return Anthropic-created skills

betas: Optional\[List\[[AnthropicBetaParam](/docs/en/api/beta#anthropic_beta)\]\]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

str

Literal\["message-batches-2024-09-24", "prompt-caching-2024-07-31", "computer-use-2024-10-22", 17 more\]

Accepts one of the following:

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

class SkillListResponse: …

id: str

Unique identifier for the skill.

The format and length of IDs may change over time.

created_at: str

ISO 8601 timestamp of when the skill was created.

display_title: Optional\[str\]

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest_version: Optional\[str\]

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: str

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: str

Object type.

For Skills, this is always `"skill"`.

updated_at: str

ISO 8601 timestamp of when the skill was last updated.

List Skills

Python

``` shiki
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.skills.list()
page = page.data[0]
print(page.id)
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
