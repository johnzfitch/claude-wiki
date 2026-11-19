---
title: "Resources - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/resources"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:33:29Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [Sessions](https://platform.claude.com/docs/en/api/http/beta/sessions)

# Resources

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Add Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/add)

POST/v1/sessions/{session_id}/resources

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [List Session Resources](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/list)

GET/v1/sessions/{session_id}/resources

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Get Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/retrieve)

GET/v1/sessions/{session_id}/resources/{resource_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Update Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/update)

POST/v1/sessions/{session_id}/resources/{resource_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Delete Session Resource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources/delete)

DELETE/v1/sessions/{session_id}/resources/{resource_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### Models



BetaManagedAgentsDeleteSessionResource object{ type: "session_resource_deleted", id }



Confirmation of resource deletion.

type: "session_resource_deleted"



id: string





BetaManagedAgentsFileResource object{ type: "file", id, created_at, 3 more }



type: "file"



id: string





created_at: string



A timestamp in RFC 3339 format

formatdate-time

file_id: string



mount_path: string





updated_at: string



A timestamp in RFC 3339 format

formatdate-time



BetaManagedAgentsGitHubRepositoryResource object{ type: "github_repository", id, created_at, 4 more }





BetaManagedAgentsMemoryStoreResource object{ type: "memory_store", memory_store_id, access, 4 more }



A memory store attached to an agent session.



BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_github_repository_resource) or [BetaManagedAgentsFileResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_file_resource) or [BetaManagedAgentsMemoryStoreResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_memory_store_resource)



One of the following:



ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_github_repository_resource) or [BetaManagedAgentsFileResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_file_resource) or [BetaManagedAgentsMemoryStoreResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_memory_store_resource)



The requested session resource.

One of the following:



ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_github_repository_resource) or [BetaManagedAgentsFileResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_file_resource) or [BetaManagedAgentsMemoryStoreResource](https://platform.claude.com/docs/en/api/http/beta/sessions/resources#beta_managed_agents_memory_store_resource)



The updated session resource.
