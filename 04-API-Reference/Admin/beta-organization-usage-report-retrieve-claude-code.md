---
title: "Get Claude Code Usage Report - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/usage_report/retrieve_claude_code"
category: "04-API-Reference/Admin"
fetched_at: "2026-09-27T06:27:06Z"
tags: ["api", "claude-code"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [CLI, SDKs, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/usage-limits.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Forganization%2Fusage_report%2Fretrieve_claude_code)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](../Endpoints/overview.md)[Beta headers](../Endpoints/beta-headers.md)[Errors](../Endpoints/errors.md)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report


Get Messages Usage Report


Get Claude Code Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](../Endpoints/rate-limits.md)[Service tiers](../Endpoints/service-tiers.md)[IAM actions (Claude Platform on AWS)](../Endpoints/claude-platform-on-aws-iam-actions.md)[Versions](../Endpoints/versioning.md)[IP addresses](../Endpoints/ip-addresses.md)[Supported regions](../Endpoints/supported-regions.md)

Claude Code

[Trigger a routine](../Endpoints/claude-code-routines-fire.md)

[Console](../Other/usage-limits.md)

Copy page



cURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/http-beta.md)
3.  [Organization](http-beta-organization.md)
4.  [Usage Report](https://platform.claude.com/docs/en/api/http/beta/organization/usage_report)

# Get Claude Code Usage Report

GET/v1/organizations/usage_report/claude_code

Retrieve daily aggregated usage metrics for Claude Code users. Enables organizations to analyze developer productivity and build custom dashboards.

##### Query parameters



starting_at: string



UTC date in YYYY-MM-DD format. Returns metrics for this single day only.

formatdate

pattern^\d{4}-\d{2}-\d{2}\$



limit: optional number



Number of records per page (default: 20, max: 1000).

default20

minimum1

maximum1000

page: optional string



Opaque cursor token from previous response's `next_page` field.

##### Returns



BetaClaudeCodeUsageReport object{ data, has_more, next_page }



Get Claude Code Usage Report

cURL



```python
curl https://api.anthropic.com/v1/organizations/usage_report/claude_code \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "actor": {
        "email_address": "user@emaildomain.com",
        "type": "user_actor"
      },
      "core_metrics": {
        "commits_by_claude_code": 8,
        "lines_of_code": {
          "added": 342,
          "removed": 128
        },
        "num_sessions": 15,
        "pull_requests_by_claude_code": 2
      },
      "customer_type": "api",
      "date": "2025-08-08T00:00:00Z",
      "is_remote": false,
      "model_breakdown": [
        {
          "estimated_cost": {
            "amount": 186,
            "currency": "USD"
          },
          "model": "claude-opus-5",
          "tokens": {
            "cache_creation": 2340,
            "cache_read": 8790,
            "input": 45230,
            "output": 12450
          }
        },
        {
          "estimated_cost": {
            "amount": 42,
            "currency": "USD"
          },
          "model": "claude-sonnet-5",
          "tokens": {
            "cache_creation": 890,
            "cache_read": 3420,
            "input": 23100,
            "output": 5680
          }
        }
      ],
      "organization_id": "12345678-1234-5678-1234-567812345678",
      "terminal_type": "iTerm.app",
      "tool_actions": {
        "edit_tool": {
          "accepted": 25,
          "rejected": 3
        },
        "multi_edit_tool": {
          "accepted": 12,
          "rejected": 1
        },
        "notebook_edit_tool": {
          "accepted": 5,
          "rejected": 2
        },
        "write_tool": {
          "accepted": 8,
          "rejected": 0
        }
      },
      "subscription_type": "enterprise"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "actor": {
        "email_address": "user@emaildomain.com",
        "type": "user_actor"
      },
      "core_metrics": {
        "commits_by_claude_code": 8,
        "lines_of_code": {
          "added": 342,
          "removed": 128
        },
        "num_sessions": 15,
        "pull_requests_by_claude_code": 2
      },
      "customer_type": "api",
      "date": "2025-08-08T00:00:00Z",
      "is_remote": false,
      "model_breakdown": [
        {
          "estimated_cost": {
            "amount": 186,
            "currency": "USD"
          },
          "model": "claude-opus-5",
          "tokens": {
            "cache_creation": 2340,
            "cache_read": 8790,
            "input": 45230,
            "output": 12450
          }
        },
        {
          "estimated_cost": {
            "amount": 42,
            "currency": "USD"
          },
          "model": "claude-sonnet-5",
          "tokens": {
            "cache_creation": 890,
            "cache_read": 3420,
            "input": 23100,
            "output": 5680
          }
        }
      ],
      "organization_id": "12345678-1234-5678-1234-567812345678",
      "terminal_type": "iTerm.app",
      "tool_actions": {
        "edit_tool": {
          "accepted": 25,
          "rejected": 3
        },
        "multi_edit_tool": {
          "accepted": 12,
          "rejected": 1
        },
        "notebook_edit_tool": {
          "accepted": 5,
          "rejected": 2
        },
        "write_tool": {
          "accepted": 8,
          "rejected": 0
        }
      },
      "subscription_type": "enterprise"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
