---
title: "Claude Code MCP Knowledgebase"
category: "06-MCP-Tools/General"
tags: ["agents", "claude-code", "cli", "connectors", "desktop", "hooks", "mcp", "oauth"]
---

# Claude Code MCP Knowledgebase

Last updated: 2026-03-08

Scope:
- Primary target: Claude Code 2.1.70
- Historical comparison points: 2.1.55, 2.1.59
- Evidence sources: extracted BunFS JS, direct binary string search, existing reverse-engineering reports in this repo, and session-level tracing with `pyghidra-lite` and `llmx`

## Executive Summary

Claude Code 2.1.70 has broad, real MCP support. It is not limited to `tools/list` and `tools/call`; the extracted JS shows support for prompts, resources, templates, sampling, elicitation, and roots. MCP is still fundamentally a JS-layer subsystem embedded in the Bun payload, not a native Ghidra-visible subsystem in the conventional sense. That matches earlier 2.1.59 reporting and the structure of the current binary.

The most important 2.1.70-specific addition is not generic MCP itself, but stronger MCP-adjacent control planes:
- full MCP OAuth lifecycle handling
- new hook events for MCP elicitation
- a Claude.ai-managed connector path that materializes remote servers as `claudeai-proxy` MCP configs

The strongest negative result from this session is also important: I found no evidence in 2.1.70 for MCP `app-ext`, `ext-apps`, or `ui://` resource rendering. Claude Code appears to support standard MCP plus Anthropic-managed connectors, but not the app-extension UI model implied by those markers.

## Evidence Base

Direct 2.1.70 JS evidence:
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:73`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:118`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:557`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:1658`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:1722`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:2464`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:4346`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:5918`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12742`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12861`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12885`

Supporting reports already present in this repo:
- `/home/zack/claude-binary/reports/mcp-agent-knowledgebase.md`
- `/home/zack/claude-binary/2.1.59/modules/SUMMARY.md`
- `/home/zack/claude-binary/2.1.70/modules/hooks.md`
- `/home/zack/claude-binary/2.1.70/modules/hooks-changes.md`
- `/home/zack/claude-binary/2.1.70/ENV_VARS_DEEP_DIVE.md`
- `/home/zack/claude-binary/2.1.70/ENV_VARS_COMPLETE_GUIDE.md`
- `/home/zack/claude-binary/2.1.70/reports/DELTA.md`
- `/home/zack/claude-binary/2.1.70/reports/index.json`
- `/home/zack/claude-binary/2.1.70/reports/p2-string-labeling.md`
- `/home/zack/claude-binary/reports/binary-intel-2.1.59-vs-2.1.55/diff.md`
- `/home/zack/claude-binary/reports/binary-intel-2.1.59-vs-2.1.55/analysis_old.json`

Repo-local operational notes:
- `/home/zack/claude-binary/CLAUDE.md:43`

Session-only binary findings:
- Deep string search on `/home/zack/claude-binary/2.1.70/claude` found:
  - `user:mcp_servers`
  - `/v1/mcp_servers?limit=1000`
  - `claudeai-proxy`
  - `/settings/connectors`
  - `/mcp/start-auth/`
  - `https://api.anthropic.com/api/claude_code_shared_session_transcripts`
- Deep string search found no hits for:
  - `app-ext`
  - `ext-apps`
  - `ui://`

## 1. What Claude Code Actually Supports

### 1.1 Standard MCP Surface

The extracted 2.1.70 JS contains schema and client support for standard MCP requests and notifications beyond tools. The strongest direct markers were observed around `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:43` and `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:557`.

Confirmed or strongly evidenced methods:
- `initialize`
- `tools/list`
- `tools/call`
- `prompts/list`
- `prompts/get`
- `resources/list`
- `resources/read`
- `resources/templates/list`
- `sampling/createMessage`
- `elicitation/create`
- `roots/list`
- `notifications/initialized`

The transport client class near `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:557` shows request handlers for `sampling/createMessage` and `elicitation/create`, which is stronger evidence than plain string presence because it demonstrates request validation and response handling.

### 1.2 Tool, Prompt, and Resource Naming

MCP tool names are normalized into Claude-facing tool IDs with the pattern:
- `mcp__<server>__<tool>`

This is visible in the naming helpers around `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:118`.

Important consequences:
- Tool permissions are expressed against these prefixed names.
- Prompt commands are also surfaced in this namespace.
- MCP-origin tools are treated specially throughout filtering, loading, and status display.

The earlier report `/home/zack/claude-binary/reports/mcp-agent-knowledgebase.md:275` also documents that `prompts/list` entries become slash commands of the form `/mcp__<server>__<prompt_name>`.

### 1.3 Instructions Injection

Claude Code ingests MCP server `instructions` from the initialize response and folds them into the system prompt. The earlier focused report at `/home/zack/claude-binary/reports/mcp-agent-knowledgebase.md:32` through `:96` is still the clearest write-up of this behavior.

High-confidence takeaways:
- MCP `instructions` are always-on prompt material, not user-invoked content.
- They are rebuilt as connected servers change.
- They are appropriate for usage guidance and domain framing, not ephemeral state.

### 1.4 Resources and Prompts Are First-Class

Claude Code is not “tool-only MCP.”

Evidence:
- Direct JS method support at `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:43` and `:557`
- Existing report coverage in `/home/zack/claude-binary/reports/mcp-agent-knowledgebase.md:275` onward
- Historical string evidence for MCP resource at-mention behavior in `/home/zack/claude-binary/reports/binary-intel-2.1.59-vs-2.1.55/analysis_old.json:5036`

What is verified vs. historical:
- Verified now: resources APIs exist in 2.1.70 JS.
- Historically evidenced: there are telemetry strings consistent with at-mentioned MCP resources.
- Not fully re-traced in this session: the complete current 2.1.70 user-facing resource mention flow.

## 2. Transport and Config Model

### 2.1 Config Scopes

The MCP config scope enum in 2.1.70 includes:
- `local`
- `user`
- `project`
- `dynamic`
- `enterprise`
- `claudeai`
- `managed`

This is visible in schema code around `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:5918`.

Operationally:
- `local`, `user`, `project` are ordinary filesystem-backed config layers.
- `dynamic` is runtime-added.
- `enterprise` / `managed` are organization-controlled.
- `claudeai` is used for Anthropic-managed connector-discovered servers.

### 2.2 Internal Transport Types

Internal MCP config shapes in 2.1.70 include:
- `stdio`
- `sse`
- `http`
- `ws`
- `sse-ide`
- `ws-ide`
- `sdk`
- `claudeai-proxy`

The transport union is visible in the schema block around `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:5918`.

Historical note:
- The 2.1.59 module summary at `/home/zack/claude-binary/2.1.59/modules/SUMMARY.md:59` reported five transport types: `stdio`, `sse`, `http`, `claudeai-proxy`, and `sdk`.
- By 2.1.70, the schema clearly also includes IDE-specific and websocket forms internally.

### 2.3 User-Addable vs. Internally Known

Not every internal transport is necessarily first-class in the CLI add-flow.

The CLI-side type validator around `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:5918` and nearby command handlers only explicitly expose some transport choices to direct user addition, especially `stdio`, `sse`, and `http`.

This matters because:
- `sse-ide`, `ws-ide`, and `claudeai-proxy` are real internal types
- but they are system-constructed or integration-driven, not general user-authored transport types in the same way

## 3. Connection Lifecycle and Runtime Behavior

### 3.1 Connection and Loading

The runtime connects configured MCP clients, loads their tools/resources/commands, and merges them into app state. This shows up in the connection code, loading code, and `mcp_status` serialization around:
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12742`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12885`

From the 2.1.59 module summary:
- `/home/zack/claude-binary/2.1.59/modules/SUMMARY.md:60` notes SSE reconnect support and MCP being JS-layer.

### 3.2 Non-Blocking vs Blocking Connect

The repo’s existing 2.1.70 env-var report documents:
- `MCP_CONNECTION_NONBLOCKING`
- `MCP_TIMEOUT`
- `MCP_TOOL_TIMEOUT`

See:
- `/home/zack/claude-binary/2.1.70/ENV_VARS_DEEP_DIVE.md:550`
- `/home/zack/claude-binary/2.1.70/ENV_VARS_DEEP_DIVE.md:578`
- `/home/zack/claude-binary/2.1.70/ENV_VARS_DEEP_DIVE.md:606`

High-signal behavior:
- `MCP_TIMEOUT` governs server startup/connect timeout
- `MCP_TOOL_TIMEOUT` governs per-tool execution timeout
- `MCP_CONNECTION_NONBLOCKING` allows startup to continue before MCP is fully connected

Repo-local note:
- `/home/zack/claude-binary/CLAUDE.md:43` recommends keeping a global `MCP_TOOL_TIMEOUT` low and overriding long-running servers per-server, which matches the architecture of long-running reverse-engineering MCP servers like `pyghidra-lite`

### 3.3 Delta Prompting for MCP Tool State

2.1.70 added instruction-delta support for MCP tool prompt material:
- `/home/zack/claude-binary/2.1.70/ENV_VARS_DEEP_DIVE.md:495`
- `/home/zack/claude-binary/2.1.70/ENV_VARS_COMPLETE_GUIDE.md:236`

This appears to reduce prompt overhead when the current MCP tool set changes by emitting deltas rather than the full MCP tool schema every turn.

## 4. OAuth and Auth Model

### 4.1 MCP OAuth Exists as a Real Subsystem

The most consistent 2.1.70 report consensus is that MCP OAuth became a first-class subsystem.

Supporting reports:
- `/home/zack/claude-binary/2.1.70/reports/DELTA.md:67`
- `/home/zack/claude-binary/2.1.70/reports/index.json:59`
- `/home/zack/claude-binary/2.1.70/reports/p2-string-labeling.md:116`
- `/home/zack/claude-binary/2.1.70/ENV_VARS_COMPLETE_GUIDE.md:142`

Observed characteristics:
- token refresh
- 401 handling
- unified auth field `apiKeyOrOAuthToken`
- per-server OAuth configuration for HTTP/SSE-style servers
- cleanup and telemetry

### 4.2 Relevant Scopes and Endpoints

The OAuth config block at `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:73` defines:
- `user:profile`
- `user:inference`
- `user:sessions:claude_code`
- `user:mcp_servers`
- `org:create_api_key`

It also defines:
- `https://api.anthropic.com`
- `https://platform.claude.com/oauth/authorize`
- `https://claude.ai/oauth/authorize`
- `https://platform.claude.com/v1/oauth/token`
- `/api/oauth/claude_cli/create_api_key`
- `/api/oauth/claude_cli/roles`
- `MCP_PROXY_URL`
- `MCP_PROXY_PATH`

### 4.3 OAuth-Related Environment Variables

Direct report evidence exists for:
- `CLAUDE_CODE_OAUTH_REFRESH_TOKEN`
- `CLAUDE_CODE_OAUTH_SCOPES`
- `MCP_CLIENT_SECRET`
- `MCP_OAUTH_CALLBACK_PORT`

See `/home/zack/claude-binary/2.1.70/ENV_VARS_COMPLETE_GUIDE.md:147`.

Historical report evidence from 2.1.59 also includes:
- `MCP_PROXY_PATH`
- `MCP_PROXY_URL`
- `MCP_REMOTE_SERVER_CONNECTION_BATCH_SIZE`
- `MCP_SERVER_CONNECTION_BATCH_SIZE`
- `MCP_TIMEOUT`
- `MCP_TOOL_TIMEOUT`
- `CLAUDE_AGENT_SDK_MCP_NO_PREFIX`

See `/home/zack/claude-binary/reports/binary-intel-2.1.59-vs-2.1.55/analysis_old.json:1682`.

## 5. Claude.ai Connectors and `claudeai-proxy`

### 5.1 What It Is

2.1.70 contains an Anthropic-managed connector discovery path that fetches remote server descriptors from Anthropic and materializes them as MCP configs with:
- `type: "claudeai-proxy"`
- `scope: "claudeai"`

This is not generic third-party UI-extension support. It is Anthropic’s own connector control plane layered on top of MCP concepts.

### 5.2 Gate, Fetch, Normalize

The core logic lives at `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:2464`.

Behavior observed directly in that block:
- feature flag: `tengu_claudeai_mcp_connectors`
- env kill switch: `ENABLE_CLAUDEAI_MCP_SERVERS`
- required OAuth scope: `user:mcp_servers`
- beta header: `mcp-servers-2025-12-04`
- fetch route: `GET ${BASE_API_URL}/v1/mcp_servers?limit=1000`
- each returned server is turned into a `claudeai-proxy` config object

Historical note:
- the binary-intel diff from 2.1.59 vs 2.1.55 already showed a connector-related string: `/home/zack/claude-binary/reports/binary-intel-2.1.59-vs-2.1.55/diff.md:56`

### 5.3 Status, Auth, and UI Routing

`claudeai-proxy` is not just a hidden config type. It is threaded through status, reconnect, and auth UI behavior.

Key locations:
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12742`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12861`
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12885`

Observed behavior:
- `mcp_status` includes `claudeai-proxy` configs
- 401s on proxy connections can produce `needs-auth`
- toggle / reconnect paths know about this type explicitly
- the UI shows authenticate / clear-auth actions specific to `claudeai-proxy`

Session-confirmed binary strings also include:
- `/settings/connectors`
- `/mcp/start-auth/`

This strongly suggests:
- auth starts from Claude.ai connector settings or organization-specific start-auth routes
- connector auth is treated differently from ordinary SSE/HTTP OAuth

### 5.4 `MCP_PROXY_URL` and `MCP_PROXY_PATH`

The endpoint constants are defined directly at `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:73`.

What is confirmed:
- these constants exist
- the connector discovery path exists
- `claudeai-proxy` configs are first-class config objects

What is not fully traced yet:
- the exact late-stage point where `MCP_PROXY_URL` and `MCP_PROXY_PATH` are combined into the outbound transport URL used for proxy calls

## 6. Hooks, Elicitation, and MCP-to-User Input

### 6.1 Elicitation Is New and Important

2.1.70 added MCP-specific hook points around elicitation.

The cleanest current report is:
- `/home/zack/claude-binary/2.1.70/modules/hooks.md:27`

New hook events:
- `Elicitation`
- `ElicitationResult`
- `InstructionsLoaded`

The more detailed walkthrough is in:
- `/home/zack/claude-binary/2.1.70/modules/hooks-changes.md:38`

### 6.2 Runtime Handling

The print/streaming loop near `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12885` installs MCP request and notification handlers for elicitation flow.

Observed behavior:
- Claude receives `elicitation/create` from MCP
- hooks may intercept or pre-resolve it
- the UI can present form or URL-style elicitation
- completion notifications are handled and surfaced

This is one of the clearest places where Claude Code goes beyond plain “tool invocation” MCP into interactive human-in-the-loop protocol handling.

## 7. Plugin, Agent, and Desktop Integration

### 7.1 Plugins Can Declare MCP Servers

The 2.1.59 summary already documented that plugins can bundle `mcpServers`:
- `/home/zack/claude-binary/2.1.59/modules/SUMMARY.md:111`

That means Claude Code’s plugin system can become an MCP distribution mechanism, not just a local command/skill system.

### 7.2 MCP and Agent/Skill Composition

The earlier report `/home/zack/claude-binary/reports/mcp-agent-knowledgebase.md` remains valuable for a different angle: it explains how MCP instructions, prompts, agents, and skills interact in the final prompt surface.

Important practical point:
- MCP is not isolated from Claude’s higher-level orchestration features
- MCP tools can be restricted into custom agents
- MCP prompts can be turned into slash commands
- plugins can package agents and skills that consume MCP tools

### 7.3 Claude Desktop Import

2.1.70 includes logic to read Claude Desktop MCP config on supported platforms and import it into Claude Code flows. The desktop import helper appears near the MCP CLI command handlers around:
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12885`

This is another sign that MCP is treated as a durable product surface, not an experimental code path.

## 8. CLI and User-Facing MCP Management

The CLI supports dedicated MCP subcommands. Relevant handlers appear in the command block around:
- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js:12885`

User-facing operations evidenced there:
- list
- get
- add from JSON
- add from Claude Desktop config
- remove
- reset project `.mcp.json` choices
- serve

The environment-variable guide marks older MCP CLI feature flags as removed by 2.1.70:
- `/home/zack/claude-binary/2.1.70/ENV_VARS_COMPLETE_GUIDE.md:45`

Interpretation:
- MCP CLI is no longer a gated experiment
- the remaining gating is around specific features such as connector discovery, not MCP itself

## 9. What Is Not Supported or Not Yet Proven

### 9.1 No Evidence for `app-ext`, `ext-apps`, or `ui://`

This session checked:
- extracted JS text in `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js`
- deep strings in `/home/zack/claude-binary/2.1.70/claude`

Result:
- no `app-ext`
- no `ext-apps`
- no `ui://`

Conclusion:
- there is no current evidence that Claude Code 2.1.70 can render MCP app-extension UIs or `ui://` resources
- the `claudeai-proxy` path should not be mistaken for `app-ext`

### 9.2 Some Historical Signals Are Not Fully Re-traced in 2.1.70

Examples:
- at-mentioned resource behavior is hinted by older telemetry strings
- some report text around `InstructionsLoaded` mixes CLAUDE.md/memory-file loading and MCP instruction loading

These are worth keeping in mind, but they are lower-confidence than the direct 2.1.70 JS evidence above.

## 10. Historical Timeline

### By 2.1.59

Strongly evidenced:
- MCP was already a substantial JS-layer subsystem
- transport types included `stdio`, `sse`, `http`, `claudeai-proxy`, `sdk`
- plugins could declare `mcpServers`
- Claude Code already exposed MCP tools via `mcp__<server>__<tool>`

Sources:
- `/home/zack/claude-binary/2.1.59/modules/SUMMARY.md:59`
- `/home/zack/claude-binary/reports/mcp-agent-knowledgebase.md:3`

### 2.1.59 to 2.1.70

Most significant MCP-adjacent growth:
- MCP OAuth lifecycle became a clearly surfaced subsystem
- new hook events for elicitation
- MCP instruction delta mode
- MCP CLI env flags removed because the CLI path is now stable

Sources:
- `/home/zack/claude-binary/2.1.70/reports/DELTA.md:67`
- `/home/zack/claude-binary/2.1.70/modules/hooks.md:5`
- `/home/zack/claude-binary/2.1.70/ENV_VARS_COMPLETE_GUIDE.md:45`
- `/home/zack/claude-binary/2.1.70/ENV_VARS_COMPLETE_GUIDE.md:49`

## 11. Practical Model of Claude Code MCP

The most accurate mental model I can defend from the evidence is:

1. MCP lives primarily in the embedded JS application, not in bespoke native code.
2. Claude Code merges MCP servers from several config scopes and integration sources.
3. Connected MCP servers contribute tools, prompts, resources, and instructions into Claude’s operating context.
4. Auth is layered:
   - generic API key path
   - per-server HTTP/SSE OAuth path
   - Anthropic-managed connector discovery and `claudeai-proxy`
5. Hooks, permissions, and the broader agent system all wrap MCP rather than sitting beside it.

This makes MCP in Claude Code feel less like a single feature and more like a substrate:
- tool bus
- prompt extension surface
- resource surface
- human-input bridge through elicitation
- managed connector surface through Claude.ai

## 12. Open Questions

These are the main unresolved items after this session:

- The exact runtime construction point for `MCP_PROXY_URL` plus `MCP_PROXY_PATH` into a live transport URL was not fully traced end-to-end.
- Current 2.1.70 behavior for resource mentions and resource templates was not exhaustively re-walked in UI flows.
- `managed` scope semantics were not fully separated from `enterprise` in this pass.
- No proof of `app-ext` was found, but absence of evidence in a minified bundle is still weaker than a confirmed negative from product documentation or runtime instrumentation.

## 13. Recommended Next Dives

If more reverse-engineering time is available, the highest-value follow-ups are:

1. Trace `claudeai-proxy` transport creation from config object to outbound HTTP request.
2. Reconstruct the resource mention path in 2.1.70, including `resources/read` and resource-template expansion.
3. Diff 2.1.59 and 2.1.70 specifically around MCP auth and hook code paths.
4. Confirm whether any hidden UI or resource-rendering surface exists under a non-obvious name rather than `app-ext`.

## Appendix: Highest-Signal Files

Use these first if you need to rebuild this knowledgebase quickly:

- `/home/zack/claude-binary/2.1.70_bunfs_extracted/src/entrypoints/cli.js`
- `/home/zack/claude-binary/reports/mcp-agent-knowledgebase.md`
- `/home/zack/claude-binary/2.1.59/modules/SUMMARY.md`
- `/home/zack/claude-binary/2.1.70/modules/hooks.md`
- `/home/zack/claude-binary/2.1.70/modules/hooks-changes.md`
- `/home/zack/claude-binary/2.1.70/ENV_VARS_DEEP_DIVE.md`
- `/home/zack/claude-binary/2.1.70/ENV_VARS_COMPLETE_GUIDE.md`
- `/home/zack/claude-binary/2.1.70/reports/DELTA.md`
- `/home/zack/claude-binary/2.1.70/reports/index.json`
- `/home/zack/claude-binary/2.1.70/reports/p2-string-labeling.md`
