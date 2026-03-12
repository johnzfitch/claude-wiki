---
category: "04-API-Reference"
fetched_at: "2026-03-12T08:17:16Z"
source_url: "https://platform.claude.com/docs/en/api/ruby/beta/skills/versions/list"
title: "List Skill Versions - Claude API Reference"
---

# List Skill Versions

beta.skills.versions.list(skill_id, \*\*kwargs) -\> PageCursor\<[VersionListResponse](/docs/en/api/beta#version_list_response) { id, created_at, description, 5 more } \>

GET/v1/skills/{skill_id}/versions

List Skill Versions

##### ParametersExpand Collapse 

skill_id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

limit: Integer

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

page: String

Optionally set to the `next_page` token from the previous response.

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

class VersionListResponse { id, created_at, description, 5 more }

id: String

Unique identifier for the skill version.

The format and length of IDs may change over time.

created_at: String

ISO 8601 timestamp of when the skill version was created.

description: String

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

directory: String

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

name: String

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill_id: String

Identifier for the skill that this version belongs to.

type: String

Object type.

For Skill Versions, this is always `"skill_version"`.

version: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

List Skill Versions

Ruby

``` shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.skills.versions.list("skill_id")

puts(page)
```

Response 200

``` shiki
{
  "data": [
    {
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
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
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
