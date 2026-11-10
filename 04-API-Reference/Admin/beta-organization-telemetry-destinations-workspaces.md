---
title: "Workspaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/telemetry_destinations/workspaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-07T06:23:50Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Telemetry Destinations](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations)

# Workspaces

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Telemetry Destination Workspaces](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/list)

GET/v1/organizations/telemetry_destinations/{destination_id}/workspaces

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](../Endpoints/beta-headers.md)

List the workspaces on a destination's workspace list, newest entry first.

##### [Add a Telemetry Destination Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/add)

POST/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](../Endpoints/beta-headers.md)

Add one workspace to a destination's workspace list.

##### [Remove a Telemetry Destination Workspace](https://platform.claude.com/docs/en/api/http/beta/organization/telemetry_destinations/workspaces/remove)

DELETE/v1/organizations/telemetry_destinations/{destination_id}/workspaces/{workspace_id}

Requires `anthropic-beta: ``telemetry-destinations-2026-08-11`. [How to send beta headers](../Endpoints/beta-headers.md)

Remove one workspace from a destination's workspace list.

##### Models



BetaDeletedTelemetryDestinationWorkspace object{ type: "telemetry_destination_workspace_deleted", telemetry_destination_id, workspace_id }



Confirmation that a workspace was removed from a destination's list.

type: "telemetry_destination_workspace_deleted"



telemetry_destination_id: string



ID of the telemetry destination (`tdst_...`).

workspace_id: string



ID of the workspace that was removed (`wrkspc_...`).



BetaTelemetryDestinationWorkspace object{ type: "telemetry_destination_workspace", created_at, telemetry_destination_id, workspace_id }



A workspace on a telemetry destination's workspace list.

Under `include`, the destination covers the workspace. Under `exclude`, the destination covers every workspace except this one. The entry doesn't have an `id`. Its `telemetry_destination_id` and `workspace_id` together identify it.

type: "telemetry_destination_workspace"





created_at: string



Time the workspace was added to the list.

formatdate-time

telemetry_destination_id: string



ID of the telemetry destination (`tdst_...`).

workspace_id: string



ID of the workspace (`wrkspc_...`).
