---
title: "Dreams - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/managed-agents/dreams"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:39Z"
tags: ["api", "billing"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanaged-agents%2Fdreams)





SearchCtrlK

First steps

[Overview](managed-agents-overview.md)[Quickstart](managed-agents-quickstart.md)[Build in Console](managed-agents-onboarding.md)[Migration](managed-agents-migration.md)

Define your agent

[Agent setup](managed-agents-agent-setup.md)[Tools](managed-agents-tools.md)[MCP connector](managed-agents-mcp-connector.md)[Permission policies](managed-agents-permission-policies.md)[Agent Skills](managed-agents-skills.md)

Configure agent environment

[Cloud environment setup](managed-agents-environments.md)[Cloud sandbox reference](managed-agents-cloud-sandboxes-reference.md)

[Self-hosted sandboxes](managed-agents-self-hosted-sandboxes.md)

Delegate work to your agent

[Start a session](managed-agents-sessions.md)[Session operations](managed-agents-session-operations.md)[Session event stream](managed-agents-events-and-streaming.md)[Session budgets](managed-agents-budgets.md)[Subscribe to webhooks](managed-agents-webhooks.md)[Define outcomes](managed-agents-define-outcomes.md)[Authenticate with vaults](managed-agents-vaults.md)

Manage agent context

[Access GitHub](managed-agents-github.md)[Attach and download files](managed-agents-files.md)

Build persistent memory

[Memory stores](managed-agents-memory.md)[Dreams](managed-agents-dreams.md)

Advanced orchestration

[Multiagent orchestration](managed-agents-multiagent-orchestration.md)[Scheduled deployments](managed-agents-scheduled-deployments.md)

Reference

[Managed Agents reference](managed-agents-reference.md)

Working with files

[Files API](../Guides/build-with-claude-files.md)[PDF support](../Guides/build-with-claude-pdf-support.md)

[Images and vision](../Guides/build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Claude Platform on AWS](../Guides/build-with-claude-claude-platform-on-aws.md)

[Console](usage-limits.md)

[Managed Agents](managed-agents-overview.md)Build persistent memory

# Dreams

Copy page



Let Claude reflect on past sessions to curate an agent's memory and surface new insights.

Copy page





Dreaming is a research preview feature. [Request access](https://claude.com/form/claude-managed-agents) to try it.

Agents write to their [memory stores](managed-agents-memory.md) as they work, but these writes are local and incremental: over many sessions a memory store accumulates duplicates, contradictions, and stale entries.

**Dreams** let Claude clean that up. A dream reads an existing memory store alongside past session transcripts, then produces a new, reorganized memory store: duplicates merged, stale or contradicted entries replaced with the latest value, and new insights surfaced.

The input store is never modified, so you can review the output and discard it if you don't like the result.



Dream endpoints are gated by the `dreaming-2026-04-21` beta header; the `managed-agents-2026-04-01` header on its own doesn't grant access to dreams. The dream-endpoint examples on this page send both headers; session and memory-store calls need only `managed-agents-2026-04-01`. The SDK sets these automatically.

## How it works

A **dream** is an asynchronous job that takes:

- a pre-existing **memory store:** the store Claude verifies, deduplicates, and reorganizes, and
- 1 to 100 **sessions:** past transcripts Claude mines for patterns and insights to fold into the output.

The dream produces another **output memory store**, separate from the input. The output store ID appears in the dream's `outputs[]` shortly after the dream starts `running`, once the workflow has cloned the input store; a `running` dream can briefly report an empty `outputs[]`.

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



```python
dream = client.beta.dreams.create(
    inputs=[
        {"type": "memory_store", "memory_store_id": store_id},
        {"type": "sessions", "session_ids": [session_a, session_b]},
    ],
    model="claude-opus-4-8",
    instructions="Focus on coding-style preferences; ignore one-off debugging notes.",
)
print(dream.id)  # drm_01...
```

Dreaming inputs include the pre-existing memory store and an array of sessions. The selected model runs the dreaming pipeline. During the research preview, `claude-opus-5`, `claude-fable-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-sonnet-5`, and `claude-sonnet-4-6` are supported. You can optionally pass `instructions` to steer the dreaming process. See [Steer with instructions](#steer-with-instructions).

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
  "model": { "id": "claude-opus-4-8" },
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

Use `instructions` for high-level synthesis guidance such as focus areas ("focus on coding-style preferences"), content to preserve unchanged, or output conventions you want applied across the store. The pipeline is a synthesis pass over the inputs, not an editor applied to the text of the store, so imperative directives that target specific lines ("change sentence X to Y", "fix the count in section Z") generally produce no change. To make targeted edits to individual memories, use the [Memory Stores API](managed-agents-memory.md#view-and-edit-memories) on the output store directly.

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



```python
while dream.status in ("pending", "running"):
    time.sleep(10)
    dream = client.beta.dreams.retrieve(dream.id)
    print(f"status={dream.status} input_tokens={dream.usage.input_tokens}")
```

### Lifecycle

| `status`    | Meaning                                                                                                           |
|-------------|-------------------------------------------------------------------------------------------------------------------|
| `pending`   | Dream successfully created and queued.                                                                            |
| `running`   | The pipeline is processing. `usage` updates as work progresses.                                                   |
| `completed` | Finished successfully. The `outputs[]` value is the new memory store.                                             |
| `failed`    | Dreaming run ended with an error. The output memory store is left as-is with whatever was written before failure. |
| `canceled`  | Dreaming run canceled. The output memory store is left as-is.                                                     |

### Watch the pipeline run

Once a dream is `running`, its `session_id` field points at the underlying [session](managed-agents-sessions.md) running the pipeline. You can stream that session's [events](managed-agents-events-and-streaming.md) to observe what the dream is reading and writing in real time. The session is archived (not deleted) when the dream reaches a terminal state, so the transcript remains available afterward.

## Use the output

When `status` reaches `completed`, the `memory_store` entry in `outputs[]` references a fully populated store. It's an ordinary memory store in your workspace. Review it with the [Memory Stores API](managed-agents-memory.md#view-and-edit-memories) or in the Console, then either:

- **Leverage it:** attach it to future sessions as a `memory_store` resource in place of (or alongside) the input memory store, or
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

The dream itself never deletes or modifies its inputs. On `failed` or `canceled` the output store persists with partial contents so you can inspect what was produced before stopping; clean it up through the Memory Stores API if you don't need it.



While a dream is `pending` or `running`, the 400 guard applies to archiving the dream itself, not its stores. Archiving or deleting an *input* memory store mid-run (or deleting an input session) will cause the dream to fail with `input_memory_store_unavailable` or `input_session_unavailable`.

## Cancel a dream

Cancel moves a `pending` or `running` dream to `canceled` immediately. Canceling an already-`canceled` dream is an idempotent no-op; canceling a `completed` or `failed` dream returns 400.



After cancellation, the dream's `usage` fields might continue to update for a few seconds while in-flight work winds down. Poll the dream until `usage` stabilizes if you need the final count.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby

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



```python
client.beta.dreams.archive(dream.id)
```

Archiving a dream does not touch its output memory store; manage that separately through the [Memory Stores API](managed-agents-memory.md#view-and-edit-memories).

## List dreams

Returns all non-archived dreams in the workspace, newest first. Use `limit` (default 20, max 100) and the `page` cursor to paginate. Pass `include_archived=true` to include archived dreams.

cURL

CLI

Python

TypeScript

C#

Go

Java

PHP

Ruby



```python
for listed_dream in client.beta.dreams.list(limit=20):
    print(listed_dream.id, listed_dream.status)
```

## Errors

A non-exhaustive list of possible dreaming errors follows.

| `error.type`                      | When                                                                                            |
|-----------------------------------|-------------------------------------------------------------------------------------------------|
| `timeout`                         | The pipeline exceeded its runtime budget.                                                       |
| `internal_error`                  | Unclassified pipeline failure.                                                                  |
| `memory_store_org_limit_exceeded` | Your organization hit its memory-store cap while the pipeline was provisioning working storage. |
| `input_memory_store_too_large`    | The input memory store exceeds the pipeline's size limit.                                       |
| `input_memory_store_unavailable`  | The input memory store was archived or deleted after the dream was created.                     |
| `input_session_unavailable`       | An input session was deleted after the dream was created.                                       |

## Billing

Dreams are billed at standard API token rates for the model you select; `usage` on the resource reports the exact totals. Cost scales roughly linearly with the number and length of input sessions. Start with a small batch of sessions and scale up once you're satisfied with the curation quality.

## Limits

| Limit                 | Value                                                                                                           |
|-----------------------|-----------------------------------------------------------------------------------------------------------------|
| Sessions per dream    | 100                                                                                                             |
| `instructions` length | 4,096 characters                                                                                                |
| Supported models      | `claude-opus-5`, `claude-fable-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-sonnet-5`, `claude-sonnet-4-6` |

Default rate limits apply to dream creation while this feature is in research preview. [Contact support](https://support.claude.com) if you need higher limits.
