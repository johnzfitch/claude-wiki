---
category: "Other"
fetched_at: "2026-04-26T00:00:00Z"
source_url: "https://platform.claude.com/docs/en/api/cli/beta/memory_stores/memories/delete.md"
---
## Delete

`$ ant beta:memory-stores:memories delete`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

DeleteMemory

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--expected-content-sha256: optional string`

  Query param: Query parameter for expected_content_sha256

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_memory: object { id, type }`

  - `id: string`

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Example

```cli
ant beta:memory-stores:memories delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
```
