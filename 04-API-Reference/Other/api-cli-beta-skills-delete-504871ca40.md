---
category: "Other"
fetched_at: "2026-04-26T00:00:00Z"
source_url: "https://platform.claude.com/docs/en/api/cli/beta/skills/delete.md"
---
## Delete

`$ ant beta:skills delete`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `--skill-id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillDeleteResponse: object { id, type }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: string`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```cli
ant beta:skills delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```
