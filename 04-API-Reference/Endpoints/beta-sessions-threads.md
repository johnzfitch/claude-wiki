---
title: "Threads - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/sessions/threads"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-13T06:35:57Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)
3.  [Sessions](https://platform.claude.com/docs/en/api/http/beta/sessions)

# Threads

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Session Threads](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/list)

GET/v1/sessions/{session_id}/threads

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Get Session Thread](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/retrieve)

GET/v1/sessions/{session_id}/threads/{thread_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Archive Session Thread](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/archive)

POST/v1/sessions/{session_id}/threads/{thread_id}/archive

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### Models



BetaManagedAgentsInlineAgent object{ type: "inline", description, execution_identity, 6 more }



An agent that has no Agent resource, and so no `id` or `version`. It is defined inline, in a workflow run's plan or when a session thread is spawned, and is not saved.



BetaManagedAgentsSessionThread object{ type: "session_thread", id, agent, 9 more }



An execution thread within a `session`. Each session has one primary thread plus zero or more child threads.

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

BetaManagedAgentsStreamSessionThreadEvents = [BetaManagedAgentsUserMessageEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_message_event) or [BetaManagedAgentsUserInterruptEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_interrupt_event) or [BetaManagedAgentsUserToolConfirmationEvent](https://platform.claude.com/docs/en/api/http/beta/sessions/events#beta_managed_agents_user_tool_confirmation_event) or 41 more



Server-sent event in a single thread's stream.

One of the following:

#### Threads[Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events)

##### [List Session Thread Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events/list)

GET/v1/sessions/{session_id}/threads/{thread_id}/events

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).

##### [Stream Session Thread Events](https://platform.claude.com/docs/en/api/http/beta/sessions/threads/events/stream)

GET/v1/sessions/{session_id}/threads/{thread_id}/stream

Requires `anthropic-beta: ``managed-agents-2026-04-01`. Learn [how to send beta headers](beta-headers.md).
