# Claude Code Binary Diff: 2.1.42 → 2.1.50

**Method:** ELF section analysis + Bun SFE bundle string extraction
**Built:** 2.1.42 @ 2026-02-13T18:56:17Z → 2.1.50 @ 2026-02-20T23:09:04Z (~7 days)
**Build IDs:** `84084c1e...` → `54a45ee1...`
**Binary size:** 223,423,030 → 225,124,924 bytes (+1.7MB)
**`.text` section:** +338,752 bytes of new native code
**Bundle size:** 101,962,184 → 102,302,152 bytes (+340KB of JS)

---

## Key Changes

### 1. OAuth Authentication System (NEW)
Full OAuth token flow added — the largest single feature addition.

New telemetry events:
- `tengu_oauth_api_key` — API key obtained via OAuth
- `tengu_oauth_profile_fetch_success / _roles_stored / _token_exchange_success`
- `tengu_oauth_token_refresh_lock_error / _retry / _retry_limit_reached`
- `tengu_oauth_token_refresh_race_recovered / _resolved`
- `tengu_oauth_tokens_inference_only / _not_claude_ai / _save_exception / _save_failed / _saved`

New API endpoints: `/api/oauth/profile`, `/api/claude_cli_profile`

### 2. Remote Control / Mobile Pairing (NEW)
- `/remote-control` endpoint
- `/remote-control is active. Code in CLI or at`
- `/mobile to use Claude Code from the Claude app on your phone`
- `/code/sessions`, `/events/`, `/delivery`, `/archive`
- `/resume: enriched / found / loading sessions for cwd=`

### 3. New Model Reference
- `claude-sonnet-4-6` explicitly referenced

### 4. Fast Mode Overflow Handling (NEW)
- `tengu_fast_mode_fallback_triggered`
- `tengu_fast_mode_overage_rejected`
- `tengu_api_key_saved_to_config`

### 5. Auto Background Agents (NEW)
- `tengu_auto_background_agents`
- UI: `All background agents killed`, `Already in a worktree session`
- UI: `Agent worktree has changes, keeping:`, `All changes and commits will be lost.`

### 6. Org "Penguin Mode" (NEW)
- `tengu_org_penguin_mode_fetch_failed`
- `/api/claude_code_penguin_mode`

### 7. Destructive Command Warning (NEW)
- `tengu_destructive_command_warning`

### 8. File Operation Tracking (NEW)
- `tengu_file_operation`, `tengu_file_suggestions_query`, `tengu_claudemd__initial_load`

### 9. New/Removed Experiment Codenames
Added: `birch_mist`, `crystal_beam`, `marble_sandcastle`, `marble_lantern_disabled`, `moth_copse`, `oak_drum`, `pebble_leaf_prune`
Removed: `coral_fern`, `mulberry_fog`

---

## Removed in 2.1.50

| Removed | Notes |
|---------|-------|
| `tengu_teleport_first_message_error/success` | Teleport feature removed |
| `tengu_prompt_coaching` | Prompt coaching UX gone |
| `tengu_bug_report_submitted` | Bug report flow removed |
| `tengu_plan_remote_*` (3 flags) | Plan remote session flags |
| `tengu_mcp_cli_command_executed / _status` | MCP CLI mode tracking |
| `tengu_memdir_disabled / _loaded` | Memory directory |
| `tengu_model_response_keyword_detected` | Response keyword detector |
| `tengu_code_change_view_opened / code_diff_cli / code_diff_footer_setting_changed` | Code diff UI |
| `tengu_input_background / file_write_optimization / fork_agent_query / watched_file_stat_error` | Misc |
| `tengu_claude_md_permission_error / rules_md_permission_error` | MD permission errors |
| `claude-code-mcp-cli` model ID | MCP CLI pseudo-model |
| `claude-plugin-temp-` model ID | Temp plugin model |
| `mcpCliEndpoint / mcpbPath / mcp_cli_mode` etc | MCP CLI internals |

---

## Build Infrastructure
- Rust source paths moved from developer macbooks (`/Users/amorriscode/`, `/Users/hellja/`) → Artifactory CI (`/root/.cargo/registry/src/artifactory.infra.ant.dev-...`)
- `regex-automata` 0.4.13 → 0.4.14
- New Rust deps: `flate2-1.1.9`, `bat-0.26.1`, `nucleo-0.5.0`, `aho-corasick-1.1.4`, `globset-0.4.18`
- Bun `1.3.10`

---

## Summary
Biggest additions: **OAuth** (full token lifecycle replacing direct API key flows), **remote/mobile control** (driving Claude Code from the Claude iOS/Android app), **auto background agents** with worktree management, and `claude-sonnet-4-6` appearing explicitly. Removals: "teleport", prompt coaching, old MCP CLI mode tracking, and build infra standardized to internal Artifactory CI.
