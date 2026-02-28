---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:26:07Z"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/retrieve"
title: "Get Workspace - Claude API Reference"
---
# Get Workspace

GET/v1/organizations/workspaces/{workspace_id}

Get Workspace

##### Path ParametersExpand Collapse 

workspace_id: string

ID of the Workspace.

##### ReturnsExpand Collapse 

Workspace = object { id, archived_at, created_at, 4 more }

id: string

ID of the Workspace.

archived_at: string

RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

created_at: string

RFC 3339 datetime string indicating when the Workspace was created.

data_residency: object { allowed_inference_geos, default_inference_geo, workspace_geo }

Data residency configuration.

allowed_inference_geos: array of string or "unrestricted"

Permitted inference geo values. 'unrestricted' means all geos are allowed.

Accepts one of the following:

UnionMember0 = array of string

UnionMember1 = "unrestricted"

default_inference_geo: string

Default inference geo applied when requests omit the parameter.

workspace_geo: string

Geographic region for workspace data storage. Immutable after creation.

display_color: string

Hex color code representing the Workspace in the Anthropic Console.

name: string

Name of the Workspace.

type: "workspace"

Object type.

For Workspaces, this is always `"workspace"`.

Get Workspace

``` shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
