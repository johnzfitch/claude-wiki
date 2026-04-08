# Module 04: MCP & Tool Execution

## Overview
MCP is entirely JS-layer. The system supports 5 transport types, lazy capability detection, tool name prefixing (`mcp__<server>__<tool>`), and retry on session failure. Tools expose permission hooks, concurrency hints, and destructive/read-only annotations.

## Transport Types
| Type | Description |
|------|------------|
| `stdio` | Subprocess with stdin/stdout |
| `sse` | Server-Sent Events (HTTP GET + POST) |
| `http` | HTTP streaming |
| `claudeai-proxy` | Claude.ai proxied MCP |
| `sdk` | In-process SDK agent (no prefix by default if `CLAUDE_AGENT_SDK_MCP_NO_PREFIX`) |

## MCP Server Connection Flow
```
S_$(serverConfigs) → Promise → resolves when all N servers connected
  x_$(callback, configs) → connect each server in parallel
  Per server:
    1. Connect with transport
    2. Fetch tools/list, resources/list, prompts/list
    3. Track metrics: connectionDurationMs, totalServers, stdioCount, sseCount, etc.
    4. tengu_mcp_server_connection_failed on error

  When all L servers connected:
    tengu_mcp_tools_commands_loaded {tools_count, commands_count, commands_metadata_length}
```

## Tool Name Construction
```
mcp__<sanitized_server_name>__<sanitized_tool_name>
  C4(name) → sanitizes name for use in identifier
  Exception: sdk type + CLAUDE_AGENT_SDK_MCP_NO_PREFIX → use raw tool name
  Exception: J9H(serverName) → reserved server (OAD(toolName) — special handling)
```

## Tool Metadata (from MCP tool annotations)
```javascript
{
  isConcurrencySafe: () => annotations?.readOnlyHint ?? false,
  isReadOnly:        () => annotations?.readOnlyHint ?? false,
  isDestructive:     () => annotations?.destructiveHint ?? false,
  isOpenWorld:       () => annotations?.openWorldHint ?? false,
  userFacingName:    () => `${server} - ${annotations?.title || name} (MCP)`
}
```

## Tool Permission (checkPermissions)
```
MCP tools always return: {behavior: "passthrough", message: "MCPTool requires permission."}
  → suggestions: [{type:"addRules", rules:[{toolName:"mcp__server__tool"}], behavior:"allow", destination:"localSettings"}]
  → Always defers to user-level allow/deny rules
```

## Tool Execution (`call`)
```
call(args, ctx, ..., onProgress):
  1. qb1(ctx) → get toolUseId → meta: {"claudecode/toolUseId": id}
  2. onProgress → mcp_progress {status:"started", serverName, toolName}
  3. Retry loop (F=0; F<=1; F++):
     i6H(client) → get/reconnect client connection
     Zb1({client, tool, args, meta, signal, onProgress}) → call tool
     on swA (session error) + F<1 → retry after recovery
  4. onProgress → mcp_progress {status:"completed" or "failed", elapsedTimeMs}
  5. return {data: content, mcpMeta: {_meta, structuredContent} if present}
```

## SSE Transport (`createSSETransport (frH)`)
```
States: connecting → connected → reconnecting → closing → closed

Reconnection logic:
  - Max reconnect window: 600s (sk9)
  - Initial delay: 1s (ok9), max: 30s (tk9), jitter: ±25%
  - Liveness timeout: 45s (ek9) without any event → reconnect
  - POST retries: 10 attempts, 500ms → 8s backoff (Au9)
  - 401/403/404 → no retry (Hu9 set)
  - Refresh headers on reconnect if refreshHeaders() provided

Liveness: resetLivenessTimer() on each received event
```

## Resources & Prompts
```
resources/list → puH(client) → [{uri, name, ...server}]
prompts/list   → duH(client) → MCP slash commands:
  name: "mcp__<server>__<prompt_name>"
  userFacingName: "<server>:<name> (MCP)"
  getPromptForCommand(args) → client.getPrompt({name, arguments: VXL(argNames, args)})
```

## MCP Config Scopes
```
scope: "user" | "project" | "dynamic" | "enterprise"
Dynamic configs: from --mcp-config flag (JSON string or file path)
Enterprise: enterprise MCP lock prevents dynamic config changes
  → if xuH() && DH (strict): error "cannot use --strict-mcp-config with enterprise config"
  → if xuH() && ZH not empty: error "cannot dynamically configure MCP servers with enterprise config"
```

## Server Status in UI
```
type: "connected" | "pending" | "needs-auth" | "failed"
  connected  → tick (✓)
  pending    → radioOff (○)
  needs-auth → triangleUpOutline (△)
  failed     → cross (✗)
```

## MCP Config Loading
```
MCP connection behavior at startup:
  _B = (b$ || o) && !MCP_CONNECTION_NONBLOCKING
  → if _B: blocks startup until MCP connected (non-interactive + no stdin mode)
  → else: loads async, startup continues

  DH (--strict-mcp-config): skip filesystem-sourced MCP configs
  pH = DH ? Promise.resolve({servers:{}}) : p6H() (load from all sources)
```

## Plugin MCP Integration
```
Plugins can declare mcpServers in manifest:
  - String URL to MCPB file
  - Array of URLs (first valid one used)
  ikH(mcpbUrl, pluginPath, pluginId, ..., config) → configure MCP server
  "Configuration saved. Restart Claude Code for changes to take effect."
```

## CCR v2 Transport
```
CLAUDE_CODE_USE_CCR_V2 → SSE-based transport to /worker/events/stream
Otherwise:
  ws:/wss: → WebSocket transport
  http/https: → HTTP-based SSE
```
