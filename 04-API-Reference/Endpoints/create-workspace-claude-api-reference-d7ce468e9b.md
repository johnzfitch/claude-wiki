---
category: "04-API-Reference"
fetched_at: "2026-02-22T14:26:01Z"
source_url: "https://platform.claude.com/docs/en/api/admin/workspaces/create"
title: "Create Workspace - Claude API Reference"
---
# Create Workspace

POST/v1/organizations/workspaces

Create Workspace

##### Body ParametersJSONExpand Collapse 

name: string

Name of the Workspace.

data_residency: optional object { allowed_inference_geos, default_inference_geo, workspace_geo }

Data residency configuration for the workspace. If omitted, defaults to workspace_geo=`"us"`, allowed_inference_geos=`"unrestricted"`, and default_inference_geo=`"global"`.

allowed_inference_geos: optional array of string or "unrestricted"

Permitted inference geo values. Defaults to 'unrestricted' if omitted, which allows all geos. Use the string 'unrestricted' to allow all geos, or a list of specific geos.

Accepts one of the following:

UnionMember0 = array of string

UnionMember1 = "unrestricted"

default_inference_geo: optional string

Default inference geo applied when requests omit the parameter. Defaults to 'global' if omitted. Must be a member of allowed_inference_geos unless allowed_inference_geos is `"unrestricted"`.

workspace_geo: optional string

Geographic region for workspace data storage. Immutable after creation. Defaults to 'us' if omitted.

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

Create Workspace

``` shiki
curl https://api.anthropic.com/v1/organizations/workspaces \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY" \
