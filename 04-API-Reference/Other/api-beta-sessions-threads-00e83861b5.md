---
title: "Threads - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/threads"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:38:50Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fbeta%2Fsessions%2Fthreads)





SearchCtrlK

Include beta APIsThe API you’re viewing is only available in beta

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions


Create Session


List Sessions


Get Session


Update Session


Delete Session


Archive Session

Events

Resources

Threads


List Session Threads


Get Session Thread


Archive Session Thread

Events

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

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

Copy page



cURL

1.  [API reference](/docs/en/api/http)
2.  [Beta](/docs/en/api/http/beta)
3.  [Sessions](/docs/en/api/http/beta/sessions)

# Threads

##### [List Session Threads](/docs/en/api/http/beta/sessions/threads/list)

GET/v1/sessions/{session_id}/threads

##### [Get Session Thread](/docs/en/api/http/beta/sessions/threads/retrieve)

GET/v1/sessions/{session_id}/threads/{thread_id}

##### [Archive Session Thread](/docs/en/api/http/beta/sessions/threads/archive)

POST/v1/sessions/{session_id}/threads/{thread_id}/archive

##### Models



BetaManagedAgentsSessionThread object{ type: "session_thread", id, agent, 8 more }



An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.



BetaManagedAgentsSessionThreadStats object{ active_seconds, duration_seconds, startup_seconds }



Timing statistics for a session thread.



active_seconds: optional number



Cumulative time in seconds the thread spent actively running. Excludes idle time.

formatdouble



duration_seconds: optional number



Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

formatdouble



startup_seconds: optional number



Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

formatdouble



BetaManagedAgentsSessionThreadStatus = "running" or "idle" or "rescheduling" or "terminated"



SessionThreadStatus enum

One of the following:

"running"



"idle"



"rescheduling"



"terminated"





BetaManagedAgentsSessionThreadUsage object{ active_seconds, cache_creation, cache_read_input_tokens, 4 more }



Cumulative token usage for a session thread across all turns.



BetaManagedAgentsStreamSessionThreadEvents = [BetaManagedAgentsUserMessageEvent](/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_message_event) or [BetaManagedAgentsUserInterruptEvent](/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_interrupt_event) or [BetaManagedAgentsUserToolConfirmationEvent](/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_tool_confirmation_event) or 34 more



Server-sent event in a single thread's stream.

One of the following:

#### Threads[Events](/docs/en/api/http/beta/sessions/threads/events)

##### [List Session Thread Events](/docs/en/api/http/beta/sessions/threads/events/list)

GET/v1/sessions/{session_id}/threads/{thread_id}/events

##### [Stream Session Thread Events](/docs/en/api/http/beta/sessions/threads/events/stream)

GET/v1/sessions/{session_id}/threads/{thread_id}/stream
