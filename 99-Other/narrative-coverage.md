# Narrative Coverage: 0.105 alpha.1 -> 0.106 alpha.5

This maps all changed lines into per-transition subsystem buckets; together these buckets cover every insertion/deletion in scope.

## 01. rust-v0.105.0-alpha.1 -> rust-v0.105.0-alpha.2

- Delta: +352 / -56 across 17 files and 7 commits.
- Primary change buckets: `codex-rs/core` 346 lines (+325/-21); `codex-rs/tui` 60 lines (+26/-34); `codex-rs/Cargo.toml` 2 lines (+1/-1).
- Functional intent (from commit subjects): nit: change model for phase 1 (#12137); feat: validate agent config file paths (#12133); feat: memory usage metrics (#12120); feat: phase 2 usage (#12121); feat: phase 1 and phase 2 e2e latencies (#12124); Enable default status line indicators in TUI config (#12015).
- Highest-impact files: `codex-rs/core/src/memories/usage.rs` 122 (+122/-0); `codex-rs/core/src/config/mod.rs` 117 (+110/-7); `codex-rs/tui/src/chatwidget.rs` 54 (+25/-29); `codex-rs/core/src/memories/phase2.rs` 49 (+48/-1); `codex-rs/core/src/agent/control.rs` 11 (+11/-0); `codex-rs/core/src/memories/mod.rs` 9 (+8/-1).

## 02. rust-v0.105.0-alpha.2 -> rust-v0.105.0-alpha.3

- Delta: +759 / -212 across 11 files and 7 commits.
- Primary change buckets: `codex-rs/core` 969 lines (+758/-211); `codex-rs/Cargo.toml` 2 lines (+1/-1).
- Functional intent (from commit subjects): memories: bump rollout summary slug cap to 60 (#12167); fix: file watcher (#12105); Fixed a hole in token refresh logic for app server (#11802); Disable collab tools during review delegation (#12157); feat: better slug for rollout summaries (#12135); Stop filtering model tools in js_repl_tools_only mode (#12069).
- Highest-impact files: `codex-rs/core/tests/suite/auth_refresh.rs` 228 (+200/-28); `codex-rs/core/src/memories/storage.rs` 214 (+191/-23); `codex-rs/core/src/file_watcher.rs` 193 (+168/-25); `codex-rs/core/src/memories/tests.rs` 110 (+103/-7); `codex-rs/core/src/tools/spec.rs` 103 (+0/-103); `codex-rs/core/src/auth.rs` 98 (+79/-19).

## 03. rust-v0.105.0-alpha.3 -> rust-v0.105.0-alpha.4

- Delta: +4396 / -198 across 69 files and 13 commits.
- Primary change buckets: `codex-rs/app-server` 1662 lines (+1544/-118); `codex-rs/app-server-protocol` 1491 lines (+1489/-2); `codex-rs/core` 672 lines (+635/-37); `codex-rs/state` 546 lines (+543/-3).
- Functional intent (from commit subjects): feat: sub-agent injection (#12152); Adjust memories rollout defaults (#12231); Update docs links for feature flag notice (#12164); fix(linux-sandbox): mount /dev in bwrap sandbox (#12081); [apps] Update apps allowlist. (#12211); Stabilize app-server detached review and running-resume tests (#12203).
- Highest-impact files: `codex-rs/app-server/src/thread_status.rs` 630 (+630/-0); `codex-rs/state/src/runtime.rs` 533 (+530/-3); `codex-rs/app-server/tests/suite/v2/thread_status.rs` 240 (+240/-0); `codex-rs/app-server-protocol/schema/json/codex_app_server_protocol.schemas.json` 228 (+228/-0); `codex-rs/app-server/src/bespoke_event_handling.rs` 196 (+130/-66); `codex-rs/core/tests/suite/subagent_notifications.rs` 196 (+196/-0).

## 04. rust-v0.105.0-alpha.4 -> rust-v0.105.0-alpha.5

- Delta: +808 / -268 across 47 files and 15 commits.
- Primary change buckets: `codex-rs/core` 882 lines (+640/-242); `codex-rs/app-server-protocol` 126 lines (+122/-4); `codex-rs/tui` 21 lines (+18/-3); `SECURITY.md` 13 lines (+13/-0).
- Functional intent (from commit subjects): try fix 2 (#12264); Undo stack size Bazel test hack (#12258); Revert "feat: no timeout mode on ue" (#12256); chore: consolidate new() and initialize() for McpConnectionManager (#12255); feat: no timeout mode on ue (#12250); chore: increase stack size for everyone (#12254).
- Highest-impact files: `codex-rs/core/src/codex.rs` 197 (+109/-88); `codex-rs/core/src/config/mod.rs` 108 (+108/-0); `codex-rs/core/src/models_manager/manager.rs` 98 (+80/-18); `codex-rs/core/src/mcp_tool_call.rs` 86 (+65/-21); `codex-rs/core/src/mcp_connection_manager.rs` 72 (+55/-17); `codex-rs/core/src/shell_snapshot.rs` 58 (+31/-27).

## 05. rust-v0.105.0-alpha.5 -> rust-v0.105.0-alpha.6

- Delta: +1520 / -125 across 41 files and 5 commits.
- Primary change buckets: `codex-rs/app-server-protocol` 992 lines (+913/-79); `codex-rs/core` 535 lines (+507/-28); `codex-rs/protocol` 85 lines (+75/-10); `codex-rs/app-server` 31 lines (+24/-7).
- Functional intent (from commit subjects): app-server tests: reduce intermittent nextest LEAK via graceful child shutdown (#12266); Clarify cumulative proposed_plan behavior in Plan mode (#12265); Skip removed features during metrics emission (#12253); feat: add Reject approval policy with granular prompt rejection controls (#12087).
- Highest-impact files: `codex-rs/core/src/exec_policy.rs` 182 (+175/-7); `codex-rs/core/src/safety.rs` 103 (+99/-4); `codex-rs/core/src/mcp_connection_manager.rs` 90 (+82/-8); `codex-rs/app-server-protocol/schema/json/ClientRequest.json` 83 (+76/-7); `codex-rs/app-server-protocol/schema/json/codex_app_server_protocol.schemas.json` 83 (+76/-7); `codex-rs/core/src/tools/sandboxing.rs` 63 (+60/-3).

## 06. rust-v0.105.0-alpha.6 -> rust-v0.105.0-alpha.7

- Delta: +5935 / -1143 across 118 files and 22 commits.
- Primary change buckets: `codex-rs/core` 3082 lines (+2575/-507); `codex-rs/app-server-protocol` 2044 lines (+1944/-100); `codex-rs/tui` 829 lines (+599/-230); `codex-rs/app-server` 680 lines (+525/-155).
- Functional intent (from commit subjects): feat: better agent picker in TUI (#12332); feat: cleaner TUI for sub-agents (#12327); Add MCP server context to otel tool_result logs (#12267); disable collab for phase 2 (#12326); chore: better agent names (#12328); feat: add nick name to sub-agents (#12320).
- Highest-impact files: `codex-rs/core/src/mcp_connection_manager.rs` 791 (+631/-160); `codex-rs/tui/src/multi_agents.rs` 583 (+410/-173); `codex-rs/app-server-protocol/src/protocol/thread_history.rs` 577 (+480/-97); `codex-rs/app-server/src/codex_message_processor.rs` 307 (+252/-55); `codex-rs/core/src/agent/control.rs` 291 (+273/-18); `codex-rs/app-server-protocol/schema/json/EventMsg.json` 237 (+237/-0).

## 07. rust-v0.105.0-alpha.7 -> rust-v0.105.0-alpha.8

- Delta: +481 / -247 across 19 files and 6 commits.
- Primary change buckets: `codex-rs/utils` 364 lines (+148/-216); `codex-rs/app-server` 129 lines (+120/-9); `codex-rs/state` 127 lines (+118/-9); `codex-rs/core` 57 lines (+56/-1).
- Functional intent (from commit subjects): app-server: add JSON tracing logs (#12287); Reuse connection between turns (#12294); fix: nick name at thread/read (#12347); fix: simplify macOS sleep inhibitor FFI (#12340); feat: do not enqueue phase 2 if not necessary (#12344).
- Highest-impact files: `codex-rs/utils/sleep-inhibitor/src/macos_inhibitor.rs` 192 (+0/-192); `codex-rs/state/src/runtime.rs` 116 (+111/-5); `codex-rs/utils/sleep-inhibitor/src/macos.rs` 107 (+107/-0); `codex-rs/app-server/src/lib.rs` 70 (+62/-8); `codex-rs/app-server/src/codex_message_processor.rs` 52 (+52/-0); `codex-rs/Cargo.lock` 34 (+23/-11).

## 08. rust-v0.105.0-alpha.8 -> rust-v0.105.0-alpha.9

- Delta: +3355 / -1066 across 100 files and 16 commits.
- Primary change buckets: `codex-rs/core` 2358 lines (+1673/-685); `codex-rs/app-server` 573 lines (+461/-112); `codex-rs/login` 474 lines (+450/-24); `codex-rs/app-server-protocol` 438 lines (+413/-25).
- Functional intent (from commit subjects): Move sanitizer into codex-secrets (#12306); Add ability to attach extra files to feedback (#12370); docs: use --locked when installing cargo-nextest (#12377); [apps] Enforce simple logo url format. (#12374); core tests: use hermetic mock server in review suite (#12291); app-server: harden disconnect cleanup paths (#12218).
- Highest-impact files: `codex-rs/core/src/tools/network_approval.rs` 711 (+317/-394); `codex-rs/core/src/connectors.rs` 488 (+483/-5); `codex-rs/app-server/src/transport.rs` 344 (+309/-35); `codex-rs/core/src/seatbelt.rs` 233 (+224/-9); `codex-rs/login/src/server.rs` 201 (+178/-23); `codex-rs/core/src/mcp_tool_call.rs` 170 (+131/-39).

## 09. rust-v0.105.0-alpha.9 -> rust-v0.105.0-alpha.10

- Delta: +7699 / -35995 across 113 files and 17 commits.
- Primary change buckets: `codex-rs/app-server-protocol` 41187 lines (+5349/-35838); `codex-rs/core` 990 lines (+983/-7); `codex-rs/tui` 854 lines (+784/-70); `codex-rs/app-server` 453 lines (+416/-37).
- Functional intent (from commit subjects): ignore v1 in JSON schema codegen (#12408); test(app-server): wait for turn/completed in turn_start tests (#12376); feat: use OAI Responses API MessagePhase type directly in App Server v2 (#12422); fix: address flakiness in thread_resume_rejoins_running_thread_even_with_override_mismatch (#12381); Add experimental realtime websocket backend prompt override (#12418); Improve Plan mode reasoning selection flow (#12303).
- Highest-impact files: `codex-rs/app-server-protocol/schema/json/codex_app_server_protocol.schemas.json` 9466 (+2834/-6632); `codex-rs/app-server-protocol/schema/json/ServerNotification.json` 8581 (+1432/-7149); `codex-rs/app-server-protocol/schema/json/v1/SessionConfiguredNotification.json` 5617 (+0/-5617); `codex-rs/app-server-protocol/schema/json/v1/ForkConversationResponse.json` 5595 (+0/-5595); `codex-rs/app-server-protocol/schema/json/v1/ResumeConversationResponse.json` 5595 (+0/-5595); `codex-rs/app-server-protocol/schema/json/ClientRequest.json` 1823 (+229/-1594).

## 10. rust-v0.105.0-alpha.10 -> rust-v0.105.0-alpha.11

- Delta: +2671 / -2445 across 232 files and 11 commits.
- Primary change buckets: `codex-rs/core` 3526 lines (+1839/-1687); `codex-rs/tui` 559 lines (+281/-278); `codex-rs/codex-api` 233 lines (+0/-233); `codex-rs/skills` 231 lines (+230/-1).
- Functional intent (from commit subjects): Delete AggregatedStream (#12441); chore: delete empty codex-rs/code file (#12440); refactor(core): move embedded system skills into codex-skills crate (#12435); fix: codex-arg0 no longer depends on codex-core (#12434); chore: remove codex-core public protocol/shell re-exports (#12432); Collapse waited message (#12430).
- Highest-impact files: `codex-rs/core/tests/suite/compact_resume_fork.rs` 719 (+142/-577); `codex-rs/core/src/codex.rs` 715 (+583/-132); `codex-rs/core/src/compact.rs` 458 (+219/-239); `codex-rs/core/src/skills/system.rs` 198 (+2/-196); `codex-rs/skills/src/lib.rs` 195 (+195/-0); `codex-rs/core/tests/suite/approvals.rs` 192 (+185/-7).

## 11. rust-v0.105.0-alpha.11 -> rust-v0.105.0-alpha.12

- Delta: +7867 / -825 across 75 files and 14 commits.
- Primary change buckets: `codex-rs/tui` 6062 lines (+5590/-472); `codex-rs/linux-sandbox` 1654 lines (+1502/-152); `codex-rs/core` 860 lines (+675/-185); `codex-rs/Cargo.lock` 109 lines (+95/-14).
- Functional intent (from commit subjects): feat(tui): syntax highlighting via syntect with theme picker (#11447); Make shell detection tests      robust to Nix shell paths (#12476); fix: make realtime conversation flake test order-insensitive (#12475); Revert "Route inbound realtime text into turn start or steer" (#12479); Route inbound realtime text into turn start or steer (#12469); fix(tui): preserve URL clickability across all TUI views (#12067).
- Highest-impact files: `codex-rs/tui/src/render/highlight.rs` 1207 (+1033/-174); `codex-rs/tui/src/diff_render.rs` 887 (+810/-77); `codex-rs/linux-sandbox/src/proxy_routing.rs` 796 (+796/-0); `codex-rs/tui/src/bottom_pane/list_selection_view.rs` 625 (+603/-22); `codex-rs/tui/src/theme_picker.rs` 620 (+620/-0); `codex-rs/tui/src/wrapping.rs` 610 (+608/-2).

## 12. rust-v0.105.0-alpha.12 -> rust-v0.105.0-alpha.13

- Delta: +573 / -22 across 18 files and 5 commits.
- Primary change buckets: `codex-rs/tui` 302 lines (+299/-3); `codex-rs/core` 146 lines (+146/-0); `codex-rs/app-server` 114 lines (+101/-13); `codex-rs/shell-command` 22 lines (+18/-4).
- Functional intent (from commit subjects): Send events to realtime api (#12423); fix(core) exec policy parsing 3 (#12485); feat(tui) /clear (#12444); app-server: retain thread listener across disconnects (#12373).
- Highest-impact files: `codex-rs/tui/src/app.rs` 173 (+173/-0); `codex-rs/app-server/src/codex_message_processor.rs` 83 (+74/-9); `codex-rs/core/tests/suite/realtime_conversation.rs` 81 (+81/-0); `codex-rs/core/src/codex.rs` 65 (+65/-0); `codex-rs/tui/src/custom_terminal.rs` 55 (+53/-2); `codex-rs/app-server/src/thread_state.rs` 31 (+27/-4).

## 13. rust-v0.105.0-alpha.13 -> rust-v0.105.0-alpha.14

- Delta: +2627 / -303 across 41 files and 17 commits.
- Primary change buckets: `.codex` 1124 lines (+1124/-0); `codex-rs/core` 679 lines (+598/-81); `codex-rs/tui` 658 lines (+552/-106); `codex-rs/app-server` 243 lines (+166/-77).
- Functional intent (from commit subjects): feat: keep dead agents in the agent picker (#12570); fix: TUI constraint (#12571); chore: phase 2 name (#12568); chore: add doc to memories (#12565); chore: awaiter (#12562); chore: nit name (#12559).
- Highest-impact files: `.codex/skills/babysit-pr/scripts/gh_pr_watch.py` 805 (+805/-0); `codex-rs/core/tests/suite/realtime_conversation.rs` 251 (+251/-0); `codex-rs/app-server/tests/suite/v2/turn_start_zsh_fork.rs` 235 (+161/-74); `.codex/skills/babysit-pr/SKILL.md` 185 (+185/-0); `codex-rs/tui/src/chatwidget/tests.rs` 182 (+182/-0); `codex-rs/tui/src/app.rs` 171 (+124/-47).

## 14. rust-v0.105.0-alpha.14 -> rust-v0.105.0-alpha.15

- Delta: +227 / -28 across 16 files and 8 commits.
- Primary change buckets: `codex-rs/exec` 65 lines (+47/-18); `.github` 61 lines (+59/-2); `codex-rs/core` 46 lines (+41/-5); `codex-rs/utils` 46 lines (+46/-0).
- Functional intent (from commit subjects): chore: better bazel test logs (#12576); feat: land sqlite (#12141); feat: role metrics multi-agent (#12579); Allow exec resume to parse output-last-message flag after command (#12541); chore: rename memory feature flag (#12580); feat: add uuid helper (#12500).
- Highest-impact files: `.github/workflows/bazel.yml` 61 (+59/-2); `codex-rs/utils/string/src/lib.rs` 43 (+43/-0); `codex-rs/exec/tests/suite/resume.rs` 35 (+18/-17); `codex-rs/exec/src/cli.rs` 30 (+29/-1); `codex-rs/cli/src/main.rs` 28 (+28/-0); `codex-rs/core/src/tools/handlers/multi_agents.rs` 23 (+23/-0).

## 15. rust-v0.105.0-alpha.15 -> rust-v0.105.0-alpha.16

- Delta: +832 / -566 across 47 files and 10 commits.
- Primary change buckets: `codex-rs/tui` 578 lines (+355/-223); `codex-rs/shell-escalation` 316 lines (+246/-70); `codex-rs/Cargo.lock` 179 lines (+99/-80); `codex-rs/exec-server` 165 lines (+57/-108).
- Functional intent (from commit subjects): fix(tui): recover on owned wrap mapping mismatch (#12609); fix: add ellipsis for truncated status indicator (#12540); Use Arc-based ToolCtx in tool runtimes (#12583); chore(deps): bump syn from 2.0.114 to 2.0.117 in /codex-rs (#12529); chore(deps): bump libc from 0.2.180 to 0.2.182 in /codex-rs (#12528); app-server: box request dispatch future to reduce stack pressure (#12421).
- Highest-impact files: `codex-rs/Cargo.lock` 179 (+99/-80); `codex-rs/tui/src/wrapping.rs` 166 (+160/-6); `codex-rs/tui/src/app.rs` 120 (+63/-57); `codex-rs/shell-escalation/src/unix/escalate_server.rs` 115 (+78/-37); `codex-rs/exec-server/src/unix/mcp.rs` 105 (+34/-71); `codex-rs/tui/src/line_truncation.rs` 100 (+100/-0).

## 16. rust-v0.105.0-alpha.16 -> rust-v0.105.0-alpha.17

- Delta: +7513 / -2969 across 135 files and 21 commits.
- Primary change buckets: `codex-rs/core` 3002 lines (+2477/-525); `codex-rs/tui` 2685 lines (+2617/-68); `codex-rs/exec-server` 1422 lines (+0/-1422); `codex-rs/Cargo.lock` 972 lines (+667/-305).
- Functional intent (from commit subjects): fix: replay after `/agent` (#12663); memories: tighten memory lookup guidance and citation requirements (#12635); feat: mutli agents persist config overrides (#12667); memories: tighten consolidation prompt schema and indexing guidance (#12653); Simplify skill tracking (#12652); chore: rm hardcoded PRESETS list (#12650).
- Highest-impact files: `codex-rs/Cargo.lock` 972 (+667/-305); `codex-rs/tui/src/bottom_pane/chat_composer.rs` 807 (+799/-8); `codex-rs/tui/src/app/pending_interactive_replay.rs` 579 (+579/-0); `codex-rs/tui/src/voice.rs` 517 (+517/-0); `codex-rs/core/tests/suite/realtime_conversation.rs` 437 (+435/-2); `codex-rs/core/src/models_manager/model_presets.rs` 371 (+3/-368).

## 17. rust-v0.105.0-alpha.17 -> rust-v0.105.0-alpha.18

- Delta: +2235 / -265 across 55 files and 5 commits.
- Primary change buckets: `codex-rs/core` 1840 lines (+1601/-239); `codex-rs/tui` 332 lines (+313/-19); `codex-rs/utils` 131 lines (+130/-1); `codex-rs/protocol` 110 lines (+106/-4).
- Functional intent (from commit subjects): ctrl-L (clears terminal but does not start a new chat)  (#12628); feat(core) Introduce Feature::RequestPermissions (#11871); feat: use process group to kill the PTY (#12688); Send warmup request (#11258).
- Highest-impact files: `codex-rs/core/tests/suite/request_permissions.rs` 595 (+595/-0); `codex-rs/core/src/sandboxing/mod.rs` 195 (+190/-5); `codex-rs/core/tests/suite/client_websockets.rs` 192 (+180/-12); `codex-rs/core/src/client.rs` 176 (+122/-54); `codex-rs/tui/src/bottom_pane/approval_overlay.rs` 174 (+169/-5); `codex-rs/tui/src/app.rs` 119 (+105/-14).

## 18. rust-v0.105.0-alpha.18 -> rust-v0.105.0-alpha.19

- Delta: +2057 / -739 across 39 files and 5 commits.
- Primary change buckets: `codex-rs/core` 1376 lines (+733/-643); `codex-rs/network-proxy` 1102 lines (+1090/-12); `codex-rs/tui` 132 lines (+129/-3); `codex-rs/app-server` 118 lines (+54/-64).
- Functional intent (from commit subjects): fix: also try matching namespaced prefix for modelinfo candidate (#12658); Fix @mention token parsing in chat composer (#12643); feat: run zsh fork shell tool via shell-escalation (#12649); feat(network-proxy): add MITM support and gate limited-mode CONNECT (#9859).
- Highest-impact files: `codex-rs/core/src/zsh_exec_bridge/mod.rs` 570 (+0/-570); `codex-rs/network-proxy/src/mitm.rs` 482 (+482/-0); `codex-rs/core/src/tools/runtimes/shell/unix_escalation.rs` 463 (+463/-0); `codex-rs/network-proxy/src/certs.rs` 344 (+344/-0); `codex-rs/tui/src/bottom_pane/chat_composer.rs` 130 (+127/-3); `codex-rs/network-proxy/src/http_proxy.rs` 120 (+110/-10).

## 19. rust-v0.105.0-alpha.19 -> rust-v0.105.0-alpha.20

- Delta: +5920 / -395 across 67 files and 9 commits.
- Primary change buckets: `codex-rs/core` 3022 lines (+2780/-242); `codex-rs/tui` 1574 lines (+1469/-105); `codex-rs/state` 883 lines (+883/-0); `codex-rs/utils` 394 lines (+389/-5).
- Functional intent (from commit subjects): revert audio scope (#12700); Agent jobs (spawn_agents_on_csv) + progress UI (#10935); Honor `project_root_markers` when discovering `AGENTS.md` (#12639); Add TUI realtime conversation mode (#12687); refactor: remove unused seatbelt unix socket arg (#12707); Ensure shell command skills trigger approval (#12697).
- Highest-impact files: `codex-rs/core/src/tools/handlers/agent_jobs.rs` 1227 (+1227/-0); `codex-rs/tui/src/diff_render.rs` 636 (+558/-78); `codex-rs/state/src/runtime.rs` 567 (+567/-0); `codex-rs/core/tests/suite/agent_jobs.rs` 424 (+424/-0); `codex-rs/core/tests/suite/skill_approval.rs` 319 (+275/-44); `codex-rs/tui/src/voice.rs` 317 (+317/-0).

## 20. rust-v0.105.0-alpha.20 -> rust-v0.105.0-alpha.21

- Delta: +285 / -42 across 11 files and 4 commits.
- Primary change buckets: `codex-rs/tui` 267 lines (+267/-0); `codex-rs/core` 41 lines (+1/-40); `codex-rs/app-server` 17 lines (+16/-1); `codex-rs/Cargo.toml` 2 lines (+1/-1).
- Functional intent (from commit subjects): Add app-server event tracing (#12695); feat(tui) - /copy (#12613); fix: temp remove citation (#12711).
- Highest-impact files: `codex-rs/tui/src/chatwidget/tests.rs` 198 (+198/-0); `codex-rs/tui/src/chatwidget.rs` 47 (+47/-0); `codex-rs/core/templates/memories/read_path.md` 41 (+1/-40); `codex-rs/tui/src/clipboard_text.rs` 11 (+11/-0); `codex-rs/app-server/src/codex_message_processor.rs` 7 (+6/-1); `codex-rs/app-server/src/message_processor.rs` 6 (+6/-0).

## 21. rust-v0.105.0-alpha.21 -> rust-v0.105.0-alpha.22

- Delta: +1225 / -468 across 52 files and 9 commits.
- Primary change buckets: `codex-rs/core` 759 lines (+557/-202); `codex-rs/app-server` 598 lines (+530/-68); `codex-rs/shell-escalation` 135 lines (+9/-126); `codex-rs/arg0` 69 lines (+57/-12).
- Functional intent (from commit subjects): Fix js_repl view_image attachments in nested tool calls (#12725); add AWS_LC_SYS_NO_JITTER_ENTROPY=1 to release musl build step to unblock releases (#12720); feat: pass helper executable paths via Arg0DispatchPaths (#12719); fix: clarify the value of SkillMetadata.path (#12729); fix(js_repl): surface uncaught kernel errors and reset cleanly (#12636); codex-rs/app-server: graceful websocket restart on Ctrl-C (#12517).
- Highest-impact files: `codex-rs/core/src/tools/js_repl/mod.rs` 346 (+306/-40); `codex-rs/app-server/tests/suite/v2/connection_handling_websocket_unix.rs` 237 (+237/-0); `codex-rs/app-server/src/lib.rs` 160 (+147/-13); `codex-rs/core/src/tools/runtimes/shell/unix_escalation.rs` 104 (+47/-57); `codex-rs/shell-escalation/src/unix/core_shell_escalation.rs` 73 (+0/-73); `codex-rs/arg0/src/lib.rs` 69 (+57/-12).

## 22. rust-v0.105.0-alpha.22 -> rust-v0.105.0-alpha.23

- Delta: +2603 / -632 across 75 files and 12 commits.
- Primary change buckets: `codex-rs/core` 1462 lines (+984/-478); `codex-rs/app-server-protocol` 967 lines (+930/-37); `codex-rs/tui` 329 lines (+257/-72); `codex-rs/app-server` 224 lines (+220/-4).
- Functional intent (from commit subjects): Surface skill permission profiles in zsh-fork exec approvals (#12753); fix: keep shell escalation exec paths absolute (#12750); feat: zsh-fork forces scripts/**/* for skills to trigger a prompt (#12730); feat(ui): add network approval persistence plumbing (#12358); tests(js_repl): remove node-related skip paths from js_repl tests (#12185); fix: chatwidget was not honoring approval_id for an ExecApprovalRequestEvent (#12746).
- Highest-impact files: `codex-rs/core/tests/suite/skill_approval.rs` 249 (+245/-4); `codex-rs/core/tests/suite/js_repl.rs` 235 (+235/-0); `codex-rs/app-server-protocol/schema/json/codex_app_server_protocol.schemas.json` 234 (+227/-7); `codex-rs/core/src/tools/js_repl/mod.rs` 221 (+5/-216); `codex-rs/core/src/tools/runtimes/shell/unix_escalation.rs` 221 (+174/-47); `codex-rs/tui/src/bottom_pane/approval_overlay.rs` 183 (+142/-41).

## 23. rust-v0.105.0-alpha.23 -> rust-v0.105.0-alpha.24

- Delta: +2377 / -177 across 61 files and 7 commits.
- Primary change buckets: `codex-rs/core` 1234 lines (+1067/-167); `codex-rs/app-server-protocol` 546 lines (+543/-3); `codex-rs/tui` 399 lines (+397/-2); `codex-rs/app-server` 293 lines (+291/-2).
- Functional intent (from commit subjects): Display pending child-thread approvals in TUI (#12767); feat: record whether a skill script is approved for the session (#12756); Support external agent config detect and import (#12660); feat: add search term to thread list (#12578); fix: flaky test due to second-resolution for thread ordering (#12692); feat: add service name to app-server (#12319).
- Highest-impact files: `codex-rs/core/src/external_agent_config.rs` 920 (+920/-0); `codex-rs/app-server-protocol/schema/json/codex_app_server_protocol.schemas.json` 150 (+150/-0); `codex-rs/core/tests/suite/model_tools.rs` 149 (+0/-149); `codex-rs/tui/src/bottom_pane/pending_thread_approvals.rs` 147 (+147/-0); `codex-rs/tui/src/app.rs` 139 (+139/-0); `codex-rs/app-server-protocol/schema/json/ClientRequest.json` 125 (+125/-0).

## 24. rust-v0.105.0-alpha.24 -> rust-v0.105.0-alpha.25

- Delta: +2536 / -413 across 30 files and 5 commits.
- Primary change buckets: `codex-rs/utils` 1421 lines (+1353/-68); `codex-rs/core` 1186 lines (+842/-344); `codex-rs/test-macros` 178 lines (+178/-0); `codex-rs/state` 140 lines (+140/-0).
- Functional intent (from commit subjects): nit: migration (#12772); feat: record memory usage (#12761); feat: adding stream parser (#12666); feat: add large stack test macro (#12768).
- Highest-impact files: `codex-rs/core/src/codex.rs` 356 (+257/-99); `codex-rs/utils/stream-parser/src/utf8_stream.rs` 333 (+333/-0); `codex-rs/utils/stream-parser/src/inline_hidden_tag.rs` 323 (+323/-0); `codex-rs/core/tests/suite/items.rs` 308 (+308/-0); `codex-rs/utils/stream-parser/src/proposed_plan.rs` 212 (+212/-0); `codex-rs/core/src/proposed_plan_parser.rs` 185 (+0/-185).

## 25. rust-v0.105.0-alpha.25 -> rust-v0.105.0-alpha.26

- Delta: +113 / -92 across 10 files and 4 commits.
- Primary change buckets: `codex-rs/core` 119 lines (+35/-84); `codex-rs/otel` 82 lines (+75/-7); `codex-rs/Cargo.toml` 3 lines (+2/-1); `codex-rs/Cargo.lock` 1 lines (+1/-0).
- Functional intent (from commit subjects): feat: fix sqlite home (#12787); chore: unify max depth parameter (#12770); otel: add host.name resource attribute to logs/traces via gethostname (#12352).
- Highest-impact files: `codex-rs/otel/src/otel_provider.rs` 81 (+74/-7); `codex-rs/core/src/config/mod.rs` 63 (+19/-44); `codex-rs/core/src/tools/handlers/multi_agents.rs` 37 (+13/-24); `codex-rs/core/config.schema.json` 8 (+1/-7); `codex-rs/core/src/agent/guards.rs` 5 (+0/-5); `codex-rs/core/src/tools/handlers/agent_jobs.rs` 5 (+2/-3).

## 26. rust-v0.105.0-alpha.26 -> rust-v0.106.0-alpha.1

- Delta: +3346 / -661 across 43 files and 4 commits.
- Primary change buckets: `codex-rs/network-proxy` 1098 lines (+1048/-50); `codex-rs/app-server-protocol` 949 lines (+947/-2); `codex-rs/Cargo.lock` 834 lines (+341/-493); `codex-rs/app-server` 761 lines (+761/-0).
- Functional intent (from commit subjects): Add app-server v2 thread realtime API (#12715); Promote js_repl to experimental with Node requirement (#12712); feat(network-proxy): add embedded OTEL policy audit logging (#12046).
- Highest-impact files: `codex-rs/Cargo.lock` 834 (+341/-493); `codex-rs/network-proxy/src/network_policy.rs` 631 (+582/-49); `codex-rs/app-server/tests/suite/v2/realtime_conversation.rs` 392 (+392/-0); `MODULE.bazel.lock` 230 (+128/-102); `codex-rs/app-server-protocol/schema/json/codex_app_server_protocol.schemas.json` 224 (+224/-0); `codex-rs/app-server-protocol/schema/json/ServerNotification.json` 214 (+214/-0).

## 27. rust-v0.106.0-alpha.1 -> rust-v0.106.0-alpha.2

- Delta: +200 / -33 across 8 files and 3 commits.
- Primary change buckets: `codex-rs/core` 98 lines (+85/-13); `codex-rs/codex-api` 75 lines (+56/-19); `codex-rs/Cargo.lock` 53 lines (+53/-0); `MODULE.bazel.lock` 4 lines (+4/-0).
- Functional intent (from commit subjects): Handle websocket timeout (#12791); Revert "fix(bazel): replace askama templates with include_str! in memories" (#12795).
- Highest-impact files: `codex-rs/codex-api/src/endpoint/responses_websocket.rs` 75 (+56/-19); `codex-rs/Cargo.lock` 53 (+53/-0); `codex-rs/core/src/memories/prompts.rs` 53 (+40/-13); `codex-rs/core/tests/suite/client_websockets.rs` 38 (+38/-0); `codex-rs/core/BUILD.bazel` 6 (+6/-0); `MODULE.bazel.lock` 4 (+4/-0).

## 28. rust-v0.106.0-alpha.2 -> rust-v0.106.0-alpha.3

- Delta: +165 / -25 across 3 files and 2 commits.
- Primary change buckets: `codex-rs/core` 188 lines (+164/-24); `codex-rs/Cargo.toml` 2 lines (+1/-1).
- Functional intent (from commit subjects): fix: enforce sandbox envelope for zsh fork execution (#12800).
- Highest-impact files: `codex-rs/core/src/tools/runtimes/shell/unix_escalation.rs` 100 (+76/-24); `codex-rs/core/tests/suite/skill_approval.rs` 88 (+88/-0); `codex-rs/Cargo.toml` 2 (+1/-1).

## 29. rust-v0.106.0-alpha.3 -> rust-v0.106.0-alpha.4

- Delta: +3797 / -338 across 68 files and 9 commits.
- Primary change buckets: `codex-rs/app-server-protocol` 2448 lines (+2400/-48); `codex-rs/app-server` 1446 lines (+1215/-231); `codex-rs/core` 199 lines (+146/-53); `codex-rs/protocol` 24 lines (+24/-0).
- Functional intent (from commit subjects): only use preambles for realtime (#12806); feat(app-server): thread/unsubscribe API (#10954); make 5.3-codex visible in cli for api users (#12808); fix: harden zsh fork tests and keep subcommand approvals deterministic (#12809); Update Codex docs success link (#12805); Add simple realtime text logs (#12807).
- Highest-impact files: `codex-rs/app-server/tests/suite/v2/thread_unsubscribe.rs` 383 (+383/-0); `codex-rs/app-server-protocol/schema/json/codex_app_server_protocol.schemas.json` 306 (+261/-45); `codex-rs/app-server/src/codex_message_processor.rs` 227 (+193/-34); `codex-rs/app-server-protocol/schema/json/EventMsg.json` 172 (+172/-0); `codex-rs/app-server/tests/suite/v2/dynamic_tools.rs` 142 (+136/-6); `codex-rs/app-server/tests/suite/v2/thread_archive.rs` 139 (+139/-0).

## 30. rust-v0.106.0-alpha.4 -> rust-v0.106.0-alpha.5

- Delta: +84 / -557 across 11 files and 4 commits.
- Primary change buckets: `codex-rs/core` 534 lines (+47/-487); `codex-rs/app-server` 103 lines (+36/-67); `codex-rs/Cargo.toml` 2 lines (+1/-1); `codex-rs/linux-sandbox` 2 lines (+0/-2).
- Functional intent (from commit subjects): only use preambles for realtime (#12831); Revert "Ensure shell command skills trigger approval (#12697)" (#12721); Revert "only use preambles for realtime" (#12830).
- Highest-impact files: `codex-rs/core/tests/suite/skill_approval.rs` 298 (+7/-291); `codex-rs/core/src/skills/invocation_utils.rs` 152 (+11/-141); `codex-rs/app-server/tests/suite/v2/skill_approval.rs` 99 (+35/-64); `codex-rs/core/src/codex.rs` 39 (+22/-17); `codex-rs/core/src/tools/handlers/shell.rs` 34 (+7/-27); `codex-rs/core/src/exec.rs` 8 (+0/-8).

