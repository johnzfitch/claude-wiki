---
title: "Api Cli Beta Vaults Archive Fb33B123F3"
source_url: "https://platform.claude.com/docs/en/api/cli/beta/vaults/archive.md"
category: "Other"
fetched_at: "2026-04-26T00:00:00Z"
tags: ["api", "cli"]
---

## Archive

`$ ant beta:vaults archive`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `--vault-id: string`

  Path parameter vault_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_vault: object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

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

### Example

```cli
ant beta:vaults archive \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```
