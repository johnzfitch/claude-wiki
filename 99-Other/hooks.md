Interesting! Some things I thought were new are actually already in 2.1.59:
  - agent_type and model fields in SessionStart — already in 2.1.59
  - last_assistant_message in Stop and SubagentStop — already in 2.1.59

  So the real changes are:
  1. New hook events: Elicitation, ElicitationResult, InstructionsLoaded
  2. New asyncRewake field on command hooks
  3. New httpHookAllowedEnvVars enterprise policy setting

  4. New allowedHttpHookUrls enterprise policy allowlist for HTTP hooks
  5. Private IP blocking for HTTP hooks with DNS resolution check
  (ERR_HTTP_HOOK_BLOCKED_ADDRESS)
  6. Sandbox proxy support for HTTP hooks (routes through sandbox when sandboxing
  is enabled)

  The headers field is a bit confusing — the metrics show it as unchanged between
  versions, but I'm seeing references to it in the HTTP hook schema, so I need to
  verify whether that's actually a new feature or if it was already there. that was
   also present in 2.1.59.

  Looking at the schema snippet from the first search, I can see the headers field
  in the HTTP hook object and the allowedEnvVars per-hook field. The headers stayed
   the same (8→8) but allowedEnvVars jumped from 2 to 10, which suggests it might
  be new in 2.1.70. Let me verify whether the per-hook allowedEnvVars and the
  global httpHookAllowedEnvVars were both introduced in this version by checking
  the HTTP hook schema from 2.1.59.New hook event types (3 new):
  1. Elicitation — fires when an MCP server requests user data input. Fields:
  mcp_server_name, message, mode (form|url), url, elicitation_id, requested_schema.
   Hook can override with accept/decline/cancel + content.
  2. ElicitationResult — fires after user responds to an elicitation. Fields:
  mcp_server_name, elicitation_id, mode, action (accept|decline|cancel), content.
  Hook can override action.

  3. InstructionsLoaded — fires when a CLAUDE.md / memory file is loaded. Fields:
  file_path, memory_type (User|Project|Local|Managed), load_reason
  (session_start|nested_traversal|path_glob_match|include), globs,
  trigger_file_path, parent_file_path.

  Command hook new fields:
  - asyncRewake: boolean — runs in background but wakes model on exit code 2
  (blocking error). Implies async.

  HTTP hook expanded (security hardening):
  - allowedHttpHookUrls policy being added to restrict which URLs hooks can call.
  - httpHookAllowedEnvVars creates a global allowlist that intersects with per-hook
   settings for environment variable access.
  - DNS resolution now checks all resolved IPs against private ranges (10.x,
  172.16-31.x, 192.168.x, 169.254.x) while allowing loopback for local development,
   with an error code for blocked addresses.
  - When sandboxing is active, HTTP hooks route through the sandbox proxy, and
  redirects are disabled.
New Events (3)

  1. Elicitation — fired when an MCP server requests user input (elicitation
  dialog)
  - Input: mcp_server_name, message, mode (form|url), url, elicitation_id,
  requested_schema
  - hookSpecificOutput: action (accept|decline|cancel), content
  - Hook can pre-fill the form, auto-accept, or auto-decline

  - If hook returns action: "decline" → "Elicitation denied by hook" blocking error

  2. ElicitationResult — fired after user responds to an elicitation dialog
  - Input: mcp_server_name, elicitation_id, mode, action, content
  - hookSpecificOutput: action (accept|decline|cancel), content
  - Hook can override what gets submitted back to the MCP server
  - If hook returns action: "decline" → "Elicitation result blocked by hook"
  blocking error

  3. InstructionsLoaded — fired when instructions are loaded from an MCP server,
  allowing hooks to inspect or modify the loaded instructions before they're
  processed.

  Now I'm looking at HTTP hook security hardening, specifically DNS resolution and
  private IP blocking to prevent requests to internal networks. Before making any
  HTTP request, the system resolves the hostname and checks each resulting IP
  address against a blocklist of private and link-local ranges, including IPv4
  addresses like 10.x.x.x and 172.16-31.x.x.

  x, plus IPv6 ranges for unique local and link-local addresses, while allowing
  loopback addresses for local development. There's also a new enterprise policy
  setting called allowedHttpHookUrls that acts as an allowlist for which URLs HTTP
  hooks can target, supporting wildcard patterns.

  Beyond that, there's another policy layer with httpHookAllowedEnvVars that
  intersects with per-hook environment variable permissions—so even if a hook
  config allows reading certain env vars, the global policy can further restrict
  what's actually accessible. The sandbox proxy routing bypasses DNS checks
  entirely when sandboxing is enabled, and redirects are explicitly disabled for
  security.

  For command hooks, there's a new asyncRewake mode that runs the hook in the
  background but can wake the model if it exits with a blocking error code, giving
  more control than fire-and-forget async execution. I'm also adding a new
  bypass_permissions_disabled reason to the SessionEnd event to track when bypass
  mode gets turned off.
