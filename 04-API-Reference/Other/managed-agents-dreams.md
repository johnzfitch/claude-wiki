---
title: "Dreams - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/dreams"
category: "04-API-Reference/Other"
fetched_at: "2026-11-05T06:37:09Z"
tags: ["api", "billing"]
---

# Dreams

Copy page



Let Claude review past sessions to curate an agent’s memory and surface new insights.

Copy page



Dreams

Feature of  
[Managed Agents](managed-agents-overview.md)

[Status](#availability-feature-support)  
Research preview

[Cloud platforms](#availability-feature-support)  
Claude APIAvailable

[Beta header](#feature-beta-headers)  
Both
- `managed-agents-2026-04-01`
  
- `dreaming-2026-04-21`
  

[Data handling](#feature-data-handling)  
Not ZDR eligibleNot HIPAA eligible

Dreams are in research preview

[Request access(opens in new tab)](https://claude.com/form/claude-managed-agents)

Agents write to their [memory stores](managed-agents-memory.md) as they work, but these writes are local and incremental: over many sessions a memory store accumulates duplicates, contradictions, and stale entries.

**Dreams** let Claude clean that up. A dream reads an existing memory store alongside past session transcripts, then produces a new, reorganized memory store: duplicates merged, stale or contradicted entries replaced with the latest value, and new insights surfaced.

The input store is never modified, so you can review the output and discard it if you don’t like the result.

## How it works

A **dream** is an asynchronous job that takes:

- a pre-existing **memory store:** the store Claude verifies, deduplicates, and reorganizes, and
- 1 to 100 **sessions:** past transcripts Claude mines for patterns and insights to fold into the output.

The dream produces another **output memory store**, separate from the input. The output store ID appears in the dream’s `outputs` array shortly after the dream starts `running`, once the workflow has cloned the input store; a `running` dream can briefly report an empty `outputs` array.

## Create a dream

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
dream = client.beta.dreams.create(
    inputs=[
        {"type": "memory_store", "memory_store_id": store_id},
        {"type": "sessions", "session_ids": [session_a, session_b]},
    ],
    model="claude-opus-5-5",
    instructions="Focus on coding-style preferences; ignore one-off debugging notes.",
)
print(dream.id)  # drm_01...
```

Dreaming inputs include the pre-existing memory store and an array of sessions. The model you choose runs the dreaming pipeline. Only [select models](#feature-availability) are supported. You can optionally pass `instructions` to steer the dreaming process. See [Steer with instructions](#steer-with-instructions).

The response is the full `dream` resource with `status: "pending"`:

```python
{
  "type": "dream",
  "id": "drm_01AbCDefGhIjKlMnOpQrStUv",
  "status": "pending",
  "inputs": [
    { "type": "memory_store", "memory_store_id": "memstore_01Hx..." },
    { "type": "sessions", "session_ids": ["sesn_01...", "sesn_02..."] }
  ],
  "outputs": [],
  "model": { "id": "claude-opus-5-5" },
  "instructions": "Focus on coding-style preferences; ignore one-off debugging notes.",
  "session_id": null,
  "created_at": "2026-04-29T17:04:10Z",
  "ended_at": null,
  "archived_at": null,
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "cache_read_input_tokens": 0,
    "cache_creation_input_tokens": 0
  },
  "error": null
}
```





If you only have session transcripts and no existing store, [create an empty memory store](managed-agents-memory.md#create-a-memory-store) first and pass it as the `memory_store` input.

### Steer with instructions

The optional `instructions` field steers what the dreaming pipeline synthesizes. It is applied throughout the pipeline: what to read closely, what to merge or drop, and how to structure the output store.

Use `instructions` for high-level synthesis guidance such as focus areas (“focus on coding-style preferences”), content to preserve unchanged, or output conventions you want applied across the store. The pipeline is a synthesis pass over the inputs, not an editor applied to the text of the store, so imperative directives that target specific lines (“change sentence X to Y,” “fix the count in section Z”) generally produce no change. To make targeted edits to individual memories, use the [Memory Stores API](managed-agents-memory.md#view-and-edit-memories) on the output store directly.

## Track progress

Dreams run asynchronously and typically take minutes to a few hours, driven by the number of input transcripts. Poll the dream by ID to check status:

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
while dream.status in ("pending", "running"):
    time.sleep(10)
    dream = client.beta.dreams.retrieve(dream.id)
    print(f"status={dream.status} input_tokens={dream.usage.input_tokens}")
```

### Lifecycle

| `status` | Meaning |
|----|----|
| `pending` | Dream successfully created and queued. |
| `running` | The pipeline is processing. `usage` updates as work progresses. |
| `completed` | Finished successfully. The `outputs` value is the new memory store. |
| `failed` | Dreaming run ended with an error. The output memory store is left as-is with whatever was written before failure. |
| `canceled` | Dreaming run canceled. The output memory store is left as-is. |

### Watch the pipeline run

Once a dream is `running`, its `session_id` field points at the underlying [session](managed-agents-sessions.md) running the pipeline. You can stream that session’s [events](managed-agents-events-and-streaming.md) to observe what the dream is reading and writing in real time. The session is archived (not deleted) when the dream reaches a terminal state, so the transcript remains available afterward.

## Use the output

When `status` reaches `completed`, the `memory_store` entry in `outputs` references a fully populated store. It’s an ordinary memory store in your workspace. Review it with the [Memory Stores API](managed-agents-memory.md#view-and-edit-memories) or in the Claude Console, then either:

- **Use it:** attach it to future sessions as a `memory_store` resource in place of (or alongside) the input memory store, or
- **Discard it:** [delete the memory store](../Endpoints/beta-memory-stores-delete.md) or [archive the memory store](../Endpoints/beta-memory-stores-archive.md).

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
# After the dream ends, the output holds the rebuilt memory store
output_store_id = next(
    output.memory_store_id for output in dream.outputs if output.type == "memory_store"
)

session = client.beta.sessions.create(
    agent=agent_id,
    environment_id=environment_id,
    resources=[
        {"type": "memory_store", "memory_store_id": output_store_id},
    ],
)
```

The dream itself never deletes or modifies its inputs. On `failed` or `canceled` the output store persists with partial contents so you can inspect what was produced before stopping; clean it up through the Memory Stores API if you don’t need it.



While a dream is `pending` or `running`, the 400 guard applies to archiving the dream itself, not its stores. Archiving or deleting an *input* memory store mid-run (or deleting an input session) will cause the dream to fail with `input_memory_store_unavailable` or `input_session_unavailable`.

## Cancel a dream

Cancel moves a `pending` or `running` dream to `canceled` immediately. Canceling an already-`canceled` dream is an idempotent no-op; canceling a `completed` or `failed` dream returns 400.



After cancellation, the dream’s `usage` fields might continue to update for a few seconds while in-flight work winds down. Poll the dream until `usage` stabilizes if you need the final count.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client.beta.dreams.cancel(dream.id)
```

## Archive a dream

Archive sets `archived_at` on a dream that has reached a terminal state (`completed`, `failed`, or `canceled`); `status` is left unchanged. Archived dreams are excluded from default list responses but remain readable by ID. Archiving an already-archived dream is an idempotent no-op. Archiving a `pending` or `running` dream returns 400; cancel it first. There is no unarchive.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
client.beta.dreams.archive(dream.id)
```

Archiving a dream does not touch its output memory store; manage that separately through the [Memory Stores API](managed-agents-memory.md#view-and-edit-memories).

## List dreams

Returns all non-archived dreams in the workspace, newest first. Use `limit` (default 20, max 100) and the `page` cursor to paginate. Set `include_archived` to `true` to include archived dreams.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
for listed_dream in client.beta.dreams.list(limit=20):
    print(listed_dream.id, listed_dream.status)
```

## Errors

A non-exhaustive list of possible dreaming errors follows.

| `error.type` | When |
|----|----|
| `timeout` | The pipeline exceeded its runtime budget. |
| `internal_error` | Unclassified pipeline failure. |
| `memory_store_org_limit_exceeded` | Your organization hit its memory-store cap while the pipeline was provisioning working storage. |
| `input_memory_store_too_large` | The input memory store exceeds the pipeline’s size limit. |
| `input_memory_store_unavailable` | The input memory store was archived or deleted after the dream was created. |
| `input_session_unavailable` | An input session was deleted after the dream was created. |

## Billing

Dreams are billed at standard API token rates for the model you select; `usage` on the resource reports the exact totals. Cost scales roughly linearly with the number and length of input sessions. Start with a small batch of sessions and scale up once you’re satisfied with the curation quality.

## Limits

Default rate limits apply to dream creation while this feature is in research preview. [Contact support](https://support.claude.com) if you need higher limits.

## Availability

Dreams are in research preview on select models.

### API support

StatusResearch preview

Cloud platforms

- Claude API

Models

- [Claude Mythos 5.1](../../20-Models/models-mythos-5-1-overview.md)Not supported
- [Claude Mythos 5](../../20-Models/models-mythos-5-overview.md)Not supported
- Claude Mythos PreviewNot supported
- [Claude Haiku 5.5](../../20-Models/models-haiku-5-5-overview.md)Not supported
- [Claude Haiku 4.5](../../20-Models/models-haiku-4-5-overview.md)Not supported
- [Claude Opus 4.6](../../20-Models/models-opus-4-6-overview.md)Not supported
- [Claude Opus 4.5](../../20-Models/models-opus-4-5-overview.md)Not supported
- [Claude Sonnet 4.5](../../20-Models/models-sonnet-4-5-overview.md)Not supported
- All other models

### Required beta headers

[Beta headers overview](../Endpoints/beta-headers.md)

Beta headers allow you to access experimental features and new model capabilities before they become part of the standard API.

Header

- `managed-agents-2026-04-01`
  

Header

- `dreaming-2026-04-21`
  

Dream endpoints require the `dreaming-2026-04-21` beta header. The `managed-agents-2026-04-01` header on its own doesn’t grant access to dreams. Session calls use `managed-agents-2026-04-01`, and memory store calls use `agent-memory-2026-07-22`. The SDK sets the right header on each call.

### Data handling

[Data handling overview](manage-claude-api-and-data-retention.md#feature-eligibility)

Applicable endpoints

- `/v1/agents`
- `/v1/sessions`
- `/v1/environments`

Zero data retentionNot eligible

Sessions are stateful resources; transcripts persist until you delete them. Applies to all Managed Agents sub-features, including Self-hosted sandboxes.

HIPAANot eligible

Applies to all Managed Agents sub-features, including Self-hosted sandboxes.
