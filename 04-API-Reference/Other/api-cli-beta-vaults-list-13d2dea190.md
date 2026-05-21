---
title: "Api Cli Beta Vaults List 13D2Dea190"
source_url: "https://platform.claude.com/docs/en/api/cli/beta/vaults/list.md"
category: "Other"
fetched_at: "2026-04-26T00:00:00Z"
tags: ["api", "cli"]
---

## List

`$ ant beta:vaults list`

**get** `/v1/vaults`

List Vaults

### Parameters

- `--include-archived: optional boolean`

  Query param: Whether to include archived vaults in the results.

- `--limit: optional number`

  Query param: Maximum number of vaults to return per page. Defaults to 20, maximum 100.

- `--page: optional string`

  Query param: Opaque pagination token from a previous `list_vaults` response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListVaultsResponse: object { data, next_page }`

  Response containing a paginated list of vaults.

  - `data: optional array of BetaManagedAgentsVault`

    List of vaults.

    - `id: string`

      Unique identifier for the vault.

    - `archived_at: string`

      A timestamp in RFC 3339 format

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `display_name: string`

      Human-readable name for the vault.

    - `metadata: map[string]`

      Arbitrary key-value metadata attached to the vault.

    - `type: "vault"`

      - `"vault"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

  - `next_page: optional string`

    Pagination token for the next page, or null if no more results.

### Example

```cli
ant beta:vaults list \
  --api-key my-anthropic-api-key
```
