---
title: "Memory Versions - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/memory_stores/memory_versions"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:35:48Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [Memory Stores](https://platform.claude.com/docs/en/api/http/beta/memory_stores)

# Memory Versions

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Memory Versions](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/list)

GET/v1/memory_stores/{memory_store_id}/memory_versions

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Retrieve a Memory Version](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/retrieve)

GET/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Redact a Memory Version](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions/redact)

POST/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact

Requires `anthropic-beta: ``agent-memory-2026-07-22` or `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### Models



BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_session_actor) or [BetaManagedAgentsAPIActor](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_api_actor) or [BetaManagedAgentsUserActor](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_user_actor) or [BetaManagedAgentsServiceAccountActor](https://platform.claude.com/docs/en/api/http/beta/memory_stores/memory_versions#beta_managed_agents_service_account_actor)



Identifies who performed an operation. Recorded when the operation happens and not updated afterwards, so the ID may refer to a user, service account, API key, or session that has since been deleted.

One of the following:



BetaManagedAgentsAPIActor object{ type: "api_actor", api_key_id }



A direct caller of the public API, identified by the API key that authenticated the request.

type: "api_actor"





api_key_id: string



ID of the API key (an `apikey_...` value). This identifies the key, not the secret.

minLength1



BetaManagedAgentsMemoryVersion object{ type: "memory_version", id, created_at, 10 more }



One entry in a memory's history, recording a single change and who made it.

Every change to a memory adds one version. Only redaction can change a version after that. Versions belong to the memory store and stay after the memory is deleted. Each version is retained for at least the version retention period after it was written, unless the store itself is deleted.

Retrieving a redacted version succeeds, with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`. Check `redacted_at` to find out whether a version was redacted.

See the [memory guide](../Other/managed-agents-memory.md#audit-memory-changes) to learn more about memory versions.



BetaManagedAgentsMemoryVersionOperation = "created" or "modified" or "deleted"



The kind of change that a memory version records.

Every change to a memory adds one version. If you update a memory and nothing changes, the memory doesn't get a new version.

One of the following:

"created"



The memory was created. The first version in any memory's lineage.

"modified"



The memory's `content`, `path`, or both were changed via update. Writes the agent makes through the filesystem mount also appear as `modified`.

"deleted"



The memory was deleted. The `content`, `content_size_bytes`, and `content_sha256` fields are `null` on this version. The preceding version, while it is retained, records the deleted content's size and hash.



BetaManagedAgentsServiceAccountActor object{ type: "service_account_actor", service_account_id }



A workload authenticated as a service account, for example via Workload Identity Federation.

type: "service_account_actor"





service_account_id: string



ID of the service account (a `svac_...` value).

minLength1



BetaManagedAgentsSessionActor object{ type: "session_actor", session_id }



An agent acting during a session, for example through the session's mounted filesystem. It names the session itself, not the user or API key that started the session.

type: "session_actor"





session_id: string



ID of the session (a `sesn_...` value). Look up the session via [Retrieve a session](beta-sessions-retrieve.md) for further provenance.

minLength1



BetaManagedAgentsUserActor object{ type: "user_actor", user_id }



A human user, for example acting through the Anthropic Console.

type: "user_actor"





user_id: string



ID of the user (a `user_...` value).
