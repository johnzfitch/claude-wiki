# Claude Code 2.1.59 — Complete Minified Identifier Mappings

**Generated**: 2026-02-28
**Source**: Module analysis reports in `2.1.59/modules/`
**Total unique identifiers**: 258

---

## By Module

### Module 01: Auth & Identity

Core authentication flows and OAuth handling.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `E59` | authLogin | CLI `auth login` dispatch |
| `G59` | authLogout | CLI `auth logout` |
| `M59` | authStatus | CLI `auth status` |
| `bdH` | installOAuthTokens | Store tokens + fetch profile + create API key |
| `GRH` | refreshOAuthToken | Refresh token exchange |
| `$JA` | exchangeCodeForTokens | Authorization code → tokens (PKCE) |
| `IJA` | populateOAuthAccountInfoIfNeeded | Env var account seeding |
| `jX$` | fetchProfileInfo | Profile + subscription type fetch |
| `Th` | isOAuthTokenExpired | Expiry check (5-min buffer) |
| `UV` | (session token getter) | Reads session access token |

---

### Module 02: Model Routing & API

Model selection, request construction, streaming, retry logic.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `C0D` | buildModelParams | Constructs model parameters |
| `CH` | buildAPIRequestBody | Full API request body |
| `l6$` | retryLoop | Exponential backoff retry |
| `gS` | createAnthropicClient | SDK client factory |
| `kb` | normalizeModelID | Model ID normalization |
| `dqA` | getMaxTokensForModel | Max tokens resolver |
| `buD` | supportsThinking | Thinking capability check |
| `kuD` | getCustomThinkingBudget | Custom budget override |
| `NS$` | supportsAdaptiveThinking | Adaptive thinking check |
| `uU` | supportsFastMode | Fast mode capability |
| `ND` | fastModeFeatureFlag | Feature flag check |
| `KG` | fastModeEnabled | Enabled check |
| `qZ` | fastModeDisabled | Disabled check |

---

### Module 03: Permission & Safety

Permission modes, rule resolution, sandbox logic.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `Nj9` | checkPermissions | Core permission check |
| `qj9` | matchDenyRules | Deny rule matcher |
| `Tj9` | matchAskRules | Ask rule matcher |
| `Zj9` | matchAllowRules | Allow rule matcher |
| `gK` | formatPermissionMessage | User-facing message |
| `zj9` | executePermissionRequestHook | Hook integration |
| `bl` | shouldUseSandbox | Sandbox decision |
| `wj9` | isSandboxExcluded | Excluded command check |
| `vh9` | showBypassDialog | BypassPermissions dialog |
| `dyA` | checkWritePermission | File write safety |

---

### Module 04: MCP & Tool Execution

MCP server connection, tool invocation, retry on failure.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `S_$` | connectAllMCPServers | Parallel server connect |
| `x_$` | connectServer | Per-server connect |
| `C4` | sanitizeServerName | Name sanitization |
| `J9H` | isReservedServer | Reserved server check |
| `OAD` | handleReservedTool | Special tool handling |
| `qb1` | getToolUseId | Metadata extraction |
| `i6H` | getOrReconnectClient | Client recovery |
| `Zb1` | callMCPTool | MCP tool call |
| `frH` | createSSETransport | SSE transport |
| `puH` | listResources | Resource list |
| `duH` | listPrompts | Prompt list |

---

### Module 05: Worker & Session

CCRClient, Bun WebWorkers, teammate agents, session persistence.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `VnA` | CCRClient | Cloud runtime worker |
| `Du9` | heartbeatInterval | 20s heartbeat timer |
| `WEB` | selectTransport | Transport selection |
| `miH` | nativeAudioAvailable | Native audio check |
| `_VH` | createInProcessAgent | In-process teammate |
| `GO$` | inProcessRunner | Agent loop |
| `v3H` | compactHistory | History compaction |
| `xHH` | findLatestSession | Session search |
| `liA` | resumeSession | Session resume |
| `cmH` | loadRemoteSession | Remote session load |

---

### Module 06: Telemetry & Feature Flags

GrowthBook, Statsig, event sampling.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `xlA` | GrowthBook | Remote feature eval |
| `p$H` | initGrowthBook | GrowthBook init |
| `rM` | syncGateCheck | Synchronous gate |
| `IL` | syncFeatureValue | Synchronous value |
| `jlA` | asyncFeatureValue | Async value |
| `uLB` | asyncGate | Async gate |
| `Tv$` | timeGatedCheck | TTL-based cache |
| `sXL` | trackExperiment | Experiment tracking |
| `qnH` | samplingConfig | Lazy init |
| `zv$` | clearCaches | Clear all caches |

---

### Module 07: Native Runtime

JSC engine, GC, NAPI modules, worker threads.

| Minified | Readable Name | Size/Context |
|----------|---------------|--------------|
| `FUN_0485a3e0` | JSC_GC_RefDecrement | Most-called (52K refs) |
| `FUN_048efce0` | JSC_PropertyHashLookup | Hash table lookup (24K refs) |
| `FUN_03111620` | readAgentRuleEnvVar | CLAUDE_CODE_AGENT_RULE_ reader |
| `FUN_02fec150` | parseAgentRule | Native rule parser |
| `FUN_046444b0` | Worker_exitHandler | Bun WebCore Worker.cpp |
| `FUN_05da1fd0` | (JIT_dispatchTable?) | 818KB, likely dispatch |
| `FUN_05ebb180` | (large_state_machine) | 477KB |
| `FUN_05e8cb20` | (complex_parser) | 190KB |

---

### Module 08: Plugin System

Marketplace loading, plugin install, zip cache mode.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `WQ` | getPluginCacheDir | Cache directory resolver |
| `fj` | isZipCacheMode | Zip cache check |
| `skH` | zipCachePath | Cache path |
| `a2A` | knownMarketplacesPath | Registry path |
| `AsI` | marketplacesDir | Marketplaces directory |
| `LsI` | pluginsDir | Plugins directory |
| `rZ` | installMarketplace | Marketplace install |
| `aZ` | installPlugin | Plugin install |
| `FgH` | installPluginFull | Full install flow |
| `y1H` | checkPolicyAllowed | Enterprise policy check |

---

### Module 09: File Operations & Search

Git ls-files, ripgrep, Rust FileIndex, Fuse.js fallback.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `D_9` | listProjectFiles | Git → ripgrep |
| `H_9` | loadRustFileIndex | NAPI module loader |
| `L_9` | gitLsFiles | Git ls-files w/ untracked |
| `E_9` | searchIndex | Rust index or Fuse.js |
| `B_9` | refreshCache | Cache refresh |
| `fuA` | lazyInitCache | Lazy singleton |
| `RgD` | generateFileSuggestions | Public API |
| `igD` | isBinaryOrGenerated | Binary/lock file detection |
| `xgD` | loadIgnorePatterns | .ignore / .rgignore |
| `M_9` | readdirImmediate | Immediate dir listing |

---

### Module 10: Voice & Audio

New in 2.1.59. Audio capture, voice stream WebSocket, STT.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `fLB` | selectRecordingBackend | Native → arecord → SoX |
| `udA` | createVoiceStream | WebSocket voice_stream |
| `Ic9` | normalizeLanguage | Language code mapping |
| `Lc9` | languageAliases | Alias map |
| `Ec9` | calculateRMSLevel | Audio level calc |
| `eO9` | toggleVoiceMode | `/voice` command |
| `HLB` | startNativeCapture | Native capture |
| `ALB` | audioCaptureModule | NAPI module |
| `miH` | isNativeCaptureAvailable | Availability check |
| `BLB` | getSoxInstallCommand | Platform-specific cmd |

---

### Hooks System

Hook execution pipeline, matchers, event executors.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `ay` | hookExecutionPipeline | Main async generator |
| `ncA` | getMatchingHooks | Find hooks matching event+matcher |
| `bj9` | collectAllHooks | Merge all sources |
| `yJ` | createBaseHookInput | Build base JSON input |
| `Av$` | executeShellHook | Shell command spawn |
| `pDB` | parseHookOutput | JSON output → result |
| `mDB` | validateHookOutput | Schema validation |
| `hj9` | matchHookPattern | Matcher logic |
| `jDB` | processPromptHook | Single-turn model query (L6208) |
| `RDB` | processAgentHook | Multi-turn agent (L6212) |
| `xDB` | createStopVerifierTool | StructuredOutput verifier |
| `sR$` | expandHookPrompt | Template variable expansion |
| `eR$` | enforceToolCall | Force StructuredOutput call |
| `kq` | combineAbortSignals | Timeout + parent signals |
| `Y5` | getDefaultSmallModel | ANTHROPIC_SMALL_FAST_MODEL or Haiku |
| `Mu` | queryModelForHook | Single-turn query |
| `uN` | agentLoop | Multi-turn agent loop |
| `WB` | createHookMessage | Hook result message |
| `FnH` | hookResultSchema | {ok: boolean, reason?: string} |
| `yj9` | hookOutputSchema | Sync hook output |
| `jj9` | asyncHookSchema | {async: true, ...} |
| `oR$` | hookConfigUnion | yj9 \| jj9 |

Event-specific executors:
| `wkA` | executePreToolHooks | PreToolUse |
| `ZkA` | executePostToolHooks | PostToolUse |
| `qkA` | executePostToolUseFailureHooks | PostToolUseFailure |
| `ykA` | executeStopHooks | Stop |
| `acA` | executeUserPromptSubmitHooks | UserPromptSubmit |
| `RkA` | executeTeammateIdleHooks | TeammateIdle |
| `XlH` | executeTaskCompletedHooks | TaskCompleted |
| `zqA` | executeSessionStartHooks | SessionStart |
| `VuA` | executeSessionEndHooks | SessionEnd |
| `NqA` | executeSetupHooks | Setup |
| `RyA` | executeSubagentStartHooks | SubagentStart |
| `f2$` | executePreCompactHooks | PreCompact |
| `oEH` | executePermissionRequestHooks | PermissionRequest |
| `ENA` | executeNotificationHooks | Notification |
| `XCH` | executeConfigChangeHooks | ConfigChange |
| `ZO$` | executeWorktreeCreateHook | WorktreeCreate |
| `qO$` | executeWorktreeRemoveHook | WorktreeRemove |

Other:
| `JCH` | executeHooksOutsideREPL | Non-REPL execution |
| `ocA` | executeStatusLineCommand | StatusLine display |
| `JuA` | executeFileSuggestionCommand | Custom file provider |
| `wO$` | hasWorktreeCreateHook | Hook existence check |
| `UCH` | hasBlockingResult | Blocking result check |
| `lDB` | countHookTypes | Type count telemetry |
| `cDB` | countPluginHooks | Plugin hook count |
| `dDB` | isInternalCallback | Internal filter |
| `zX` | getHookIdentifier | Human-readable ID |

---

### Safety & Alignment

201 functions across 8 subsystems. Top-level orchestration:

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `b_` | assembleSystemPrompt | Top-level system prompt |
| `WcI` | securityPolicyStatement | Security policy text |
| `jw1` | executingActionsWithCare | Action care instructions |
| `xw1` | systemRules | System-level rules |
| `Sw1` | overEngineeringPrevention | Keep it simple |
| `ww1` | hookInstructions | Hook system docs |
| `BTA` | filterToolsForContext | Tool filtering |
| `FcA` | bashPermissionOrchestrator | Bash permission flow |
| `vLB` | resolvePermissionMode | Mode resolution |

Command injection detection (10 checks):
| `hk` | commandInjectionCheck | Top-level check |
| `FJ9` | fastPathSafeCheck | Safe literal check |
| `CJ9` | commandSubstitutionCheck | $(...) / `...` |
| `VJ9` | heredocSubstitutionCheck | <<EOF patterns |
| `OJ9` | backslashWhitespaceCheck | Backslash escapes |
| `YJ9` | shellMetacharCheck | Shell metacharacters |
| `SJ9` | braceExpansionCheck | {a,b,c} expansion |
| `ZJ9` | ifsInjectionCheck | IFS manipulation |
| `jJ9` | unicodeWhitespaceCheck | Unicode spaces |
| `wJ9` | malformedTokenCheck | Malformed tokens |
| `xJ9` | midWordHashCheck | Mid-word # |
| `qJ9` | procEnvironCheck | /proc filesystem |
| `mJ9` | criticalPathCheck | Critical paths |
| `PJ9` | gitCommitCheck | Git commit validation |
| `_J9` | jqSafetyCheck | jq command safety |
| `lJ9` | validateCommandPaths | Path validation |

Path safety:
| `pyA` | validatePath | Path validation |
| `kyA` | isPathAllowed | Allow check |
| `wfH` | isUncPath | UNC path check |
| `JU` | resolveSymlinks | Symlink resolution |

Sandbox:
| `RL` | sandboxConfig | Sandbox config |
| `bl` | shouldUseSandbox | Decision logic |
| `wj9` | isSandboxExcluded | Exclusion check |
| `Cj9` | sandboxAutoAllowCheck | Auto-allow gate |
| `ZS9` | sandboxSystemPrompt | Sandbox prompt |

Policy settings:
| `FNA` | loadRemoteSettings | Load remote policy |
| `Sw$` | getEffectiveRemoteSettings | Effective settings |
| `pmH` | getRemoteSettingsPath | Path resolver |
| `cZD` | detectPolicySource | Source detection |
| `$k` | isEnterpriseEligible | Enterprise check |

Rule engine:
| `jcA` | matchRulesForTool | Rule matcher |
| `pR$` | checkStaticDenyRules | Static deny |
| `Jl` | getAllDenyRules | All deny |
| `aYH` | getAllAllowRules | All allow |
| `oYH` | getAllAskRules | All ask |

---

### Skills System

Named Markdown prompts, fork/inline execution.

| Minified | Readable Name | Context |
|----------|---------------|---------|
| `FuH` | loadSkillsFromDir | Directory scanner |
| `reI` | createSkillObject | Skill factory |
| `jR1` | loadLegacyCommands | .claude/commands/ |
| `jCA` | loadAllSkills | Memoized main loader |
| `Lx9` | loadBundledAndPluginSkills | Bundled + plugin |
| `rV` | getMergedSkills | Merged view (memoized) |
| `rz` | getModelInvocableSkills | For model context |
| `iV$` | getSkillToolSkills | Skill tool discovery |
| `vk` | skillExists | Name existence check |
| `My` | findSkillByName | Find (throws if missing) |
| `yTD` | executeSkillInline | Inline execution entry |
| `RTD` | executeSkillInlineBody | Inline body |
| `mF9` | executeSkillForked | Forked (agent) execution |
| `nF9` | isEmptyContext | Auto-allow predicate |
| `XW` | registerBundledSkill | Register bundled |
| `nHB` | getBundledSkills | Get all bundled |
| `T6H` | activateConditionalSkills | File touch activation |
| `q6H` | discoverSkillsDynamic | Dynamic discovery |
| `Z6H` | findSkillDirsInHierarchy | Parent dir search |
| `ddA` | clearSkillCaches | Clear caches |
| `Zj` | reloadAllSkills | Full reload |
| `EHH` | SkillTool | The `Skill` tool object |
| `JK` | "Skill" | Tool name constant |
| `Cs` | activeSkillsMap | Active skills |
| `KuH` | inactiveSkillsMap | Conditional (inactive) |

---

### Tools Inventory

30 built-in tools, 16 deferred.

| Var | Tool Name | Deferred |
|-----|-----------|----------|
| `rD` | Bash | no |
| `aD` | Read | no |
| `d1` | Write | no |
| `NB` | Edit | no |
| `of` | Glob | no |
| `j9` | Grep | no |
| `fQ` | WebFetch | yes |
| `Xz` | WebSearch | yes |
| `$6` | NotebookEdit | no |
| `w1` | Task | no |
| `Ym` | TaskOutput | yes |
| `_m` | TaskStop | yes |
| `MX` | AskUserQuestion | yes |
| `Ad` | TodoWrite | no |
| `JK` | Skill | yes |
| `qV` | ToolSearch | no |
| `ZV` | ExitPlanMode | yes |
| `x2$` | EnterPlanMode | no |
| `j2$` | EnterWorktree | yes |
| `Sb` | TaskCreate | yes |
| `l3H` | TaskGet | yes |
| `Uj` | TaskUpdate | yes |
| `i3H` | TaskList | yes |
| `cc` | TeamCreate | yes |
| `ldH` | TeamDelete | yes |
| `Rd` | SendMessage | yes |
| `RwA` | ListMcpResourcesTool | no |
| — | ReadMcpResourceTool | no |
| `ZQ` | StructuredOutput | no |
| `fkA` | LSP | yes |

Tool aliases (OHI mapping):
| `w1` | Task (internal) |
| `_m` | KillShell (alias for TaskStop) |
| `Ym` | AgentOutputTool / BashOutputTool (alias for TaskOutput) |

---

## Key Environment Variables

All `CLAUDE_CODE_*` and related environment variables.

| Env Var | Module | Purpose |
|---------|--------|---------|
| `ANTHROPIC_API_KEY` | M01 | Direct API key auth |
| `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` | M01 | Bootstrap OAuth session |
| `CLAUDE_CODE_ACCOUNT_UUID` | M01 | Pre-set account UUID |
| `CLAUDE_CODE_ORGANIZATION_UUID` | M01 | Pre-set org UUID |
| `CLAUDE_CODE_SESSION_ACCESS_TOKEN` | M01 | Session token (sk-ant-sid prefix) |
| `CLAUDE_CODE_WEBSOCKET_AUTH_FILE_DESCRIPTOR` | M01 | FD token source |
| `CLAUDE_CODE_AGENT_RULE_` | M03/M07 | Native agent rule (parsed in FUN_03111620) |
| `CLAUDE_CODE_WORKER_EPOCH` | M05 | CCRClient epoch (required integer) |
| `CLAUDE_CODE_USE_CCR_V2` | M05 | SSE-based CCR transport |
| `CLAUDE_CODE_POST_FOR_SESSION_INGRESS_V2` | M05 | HTTP POST ingress mode |
| `CLAUDE_CODE_MAX_RETRIES` | M02 | Override 10-retry default |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | M02 | Override max output tokens |
| `CLAUDE_CODE_DISABLE_THINKING` | M02 | Disable thinking entirely |
| `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` | M02 | Disable adaptive thinking |
| `CLAUDE_ENABLE_STREAM_WATCHDOG` | M02 | Enable stream idle watchdog |
| `FALLBACK_FOR_ALL_PRIMARY_MODELS` | M02 | Enable model fallback |
| `MAX_THINKING_TOKENS` | M02 | Override thinking budget |
| `CLAUDE_AGENT_SDK_MCP_NO_PREFIX` | M04 | Skip mcp__ prefix for sdk transport |
| `MCP_CONNECTION_NONBLOCKING` | M04 | Don't block startup on MCP |
| `CLAUDE_CODE_PLUGIN_USE_ZIP_CACHE` | M08 | Enable ZIP cache mode |
| `CLAUDE_CODE_PLUGIN_CACHE_DIR` | M08 | Override plugin cache dir |
| `CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS` | M08 | Git op timeout (120s default) |
| `CLAUDE_CODE_REMOTE` | M08 | Use HTTPS GitHub URLs (vs SSH) |
| `VOICE_STREAM_BASE_URL` | M10 | Override voice stream endpoint |
| `AUDIO_CAPTURE_NODE_PATH` | M10 | Override audio-capture.node path |
| `DISABLE_TELEMETRY` | M06 | Disable telemetry |
| `CLAUDE_CODE_ENABLE_TELEMETRY` | M06 | Enable telemetry |
| `DO_NOT_TRACK` | M06 | Global telemetry disable |
| `ANTHROPIC_SMALL_FAST_MODEL` | Hooks | Default hook model |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Hooks | Haiku model override |
| `CLAUDE_CODE_SIMPLE` | Hooks | Disable hooks globally |
| `CLAUDE_CODE_SHELL_PREFIX` | Hooks | Prepend to hook commands |
| `CLAUDE_PROJECT_DIR` | Hooks | Injected into hook env |
| `CLAUDE_PLUGIN_ROOT` | Hooks | Injected for plugin hooks |
| `CLAUDE_ENV_FILE` | Hooks | SessionStart/Setup only |

---

## Telemetry Event Namespace

All `tengu_*` events across the codebase.

### Auth (M01)
- `tengu_oauth_token_exchange_success`
- `tengu_oauth_token_refresh_success`
- `tengu_oauth_token_refresh_failure`
- `tengu_oauth_roles_stored`
- `tengu_oauth_api_key`
- `tengu_login_from_refresh_token` (new 2.1.59)
- `tengu_oauth_flow_start`
- `tengu_oauth_success`
- `tengu_oauth_error`
- `tengu_oauth_token_exchange_error`
- `tengu_oauth_storage_warning`
- `tengu_oauth_profile_fetch_success`

### API (M02)
- `tengu_api_success`
- `tengu_api_error`
- `tengu_api_retry`
- `tengu_max_tokens_reached`
- `tengu_context_window_exceeded`
- `tengu_streaming_stall`
- `tengu_streaming_idle_timeout`
- `tengu_streaming_error`
- `tengu_stream_no_events`
- `tengu_max_tokens_context_overflow_adjustment`
- `tengu_api_opus_fallback_triggered`
- `tengu_api_custom_529_overloaded_error`
- `tengu_startup_manual_model_config`

### MCP (M04)
- `tengu_mcp_server_connection_failed`
- `tengu_mcp_tools_commands_loaded`

### Workers (M05)
- `cli_worker_lifecycle_initialized`
- `cli_worker_epoch_mismatch`
- `tengu_continue`

### Telemetry/FF (M06)
- `tengu_voice_recording_started` (new 2.1.59)
- `tengu_voice_toggled` (new 2.1.59)
- `tengu_amber_quartz` (new 2.1.59, unknown)
- `tengu_slate_ridge` (new 2.1.59, unknown)
- `tengu_session_memory` (new 2.1.59)
- `tengu_scratch` (new 2.1.59)
- `tengu_worktree_detection` (new 2.1.59)

### Plugins (M08)
- `tengu_plugin_installed`
- `tengu_headless_plugin_install`
- `tengu_official_marketplace_auto_install`

### File Search (M09)
- `tengu_file_suggestions_git_ls_files`
- `tengu_file_suggestions_ripgrep`
- `tengu_file_suggestions_query`

### Permissions (M03)
- `tengu_trust_dialog_accept`
- `tengu_bypass_permissions_mode_dialog_shown`
- `tengu_bypass_permissions_mode_dialog_accept`

### Hooks
- `tengu_run_hook`
- `tengu_repl_hook_finished`
- `tengu_hook_created`
- `tengu_hook_deleted`
- `tengu_agent_stop_hook_success`
- `tengu_agent_stop_hook_error`
- `tengu_agent_stop_hook_max_turns`

### Skills
- `tengu_skill_tool_invocation`
- `tengu_skill_tool_slash_prefix`
- `tengu_skill_file_changed`
- `tengu_skill_loaded`
- `tengu_skill_improvement_survey`
- `tengu_dynamic_skills_changed`

---

## Usage Notes

1. **Minified identifiers are not stable across versions** — they are subject to change with build optimizations.

2. **Context is critical** — many symbols (like `E59`, `G59`, `M59`) follow patterns (auth commands in M01).

3. **Line references** are from `cli.js` (11,832 lines) — use with `less +<line> 2.1.59_bunfs_extracted/src/entrypoints/cli.js`.

4. **Native functions** (FUN_*) are from Ghidra analysis — offsets are stable within a binary version but change between builds.

5. **Tool symbols** (`rD`, `aD`, etc.) are referenced in `OHI` alias map and `Hv9` activity labels.

---

## Cross-Reference Index

### Auth → Other Modules
- Auth tokens → API headers (M02: `B5().headers`)
- OAuth session → Voice requirement (M10: `Vq()`)
- Trust → Hooks execution (Hooks: `$v$()`)
- Auth change → GrowthBook re-init (M06: `D_H()`)

### Hooks → Other Modules
- PermissionRequest → Permission system (M03: `Nj9`)
- Prompt/agent hooks → Model API (M02: `Mu`, `uN`)
- MCP tool intercept → MCP (M04: `updatedMCPToolOutput`)

### Safety → All Modules
- System prompt → All tool contexts
- Command injection → Bash tool (Tools: `rD`)
- Path validation → File tools (Tools: `aD`, `d1`, `NB`)
- Sandbox → Bash execution (M03: `bl`, `wj9`)

---

**End of Identifier Mappings**
