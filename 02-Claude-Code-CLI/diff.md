---
title: "Claude Binary Intel Diff"
category: "02-Claude-Code-CLI"
tags: ["claude-code"]
---

# Claude Binary Intel Diff

- New: `/home/zack/claude-binary/2.1.74/2.1.74`
- Old: `/home/zack/.local/share/claude/versions/2.1.72`
- Generated (UTC): `2026-03-12T04:12:21.993635+00:00`

## flags
- added: `5`
- removed: `0`
### added
- `--auto-approve`
- `--kill-after`
- `--preserve-status`
- `--remote-control`
- `--signal`

## internal_flags
- added: `1`
- removed: `0`
### added
- `--remote-control`

## env_vars
- added: `5`
- removed: `1`
### added
- `ANTHROPIC_FOUNDRY_AUTH_TOKEN`
- `ANTHROPIC_UNIX_SOCKET`
- `CLAUDE_CODE_FRAME_TIMING_LOG`
- `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS`
- `CLAUDE_SONNET_4_6`
### removed
- `CLAUDE_CODE_TWO_STAGE_CLASSIFIER`

## domains
- added: `0`
- removed: `0`

## model_ids
- added: `2`
- removed: `0`
### added
- `claude-code-feedback`
- `claude-for-hiring`

## bunfs_paths
- added: `0`
- removed: `0`

## code_tokens
- added: `14`
- removed: `7`
### added
- `tengu_auto_mode_state`
- `tengu_chair_sermon`
- `tengu_compact_failedul`
- `tengu_hawthorn_steeple`
- `tengu_hawthorn_window`
- `tengu_image_resize_fallbackw`
- `tengu_marble_whisper2`
- `tengu_message_level_tool_result_budget_enforced`
- `tengu_orchid_trellis`
- `tengu_pewter_ledger`
- `tengu_tool_empty_result`
- `tengu_tool_result_persisted_message_budget`
- `tengu_voice_recording_completed`
- `tengu_voice_stream_early_retry`
### removed
- `tengu_marble_whisper`
- `tengu_native_version_cleanupk`
- `tengu_output_style_command_inline`
- `tengu_output_style_command_inline_help`
- `tengu_output_style_command_menu`
- `tengu_pdf_page_extractionm`
- `tengu_unexpected_tool_resulti`

## http_methods_with_url_context
- added: `0`
- removed: `0`

## urls
- added: `14`
- removed: `10`
### added
- `http://${w}:${q.port}/sse`
- `http://169.254.169.254${FSD`
- `https://${p}/${x}/${d`
- `https://${q}/${K`
- `https://${S}/${h}/${u`
- `https://code.claude.com/docs/en/microsoft-foundryj`
- `https://code.claude.com/docs/en/network-config`
- `https://code.claude.com/docs/en/remote-control`
- `https://example.com/mcp`
- `https://github.com/${fH`
- `https://github.com/${H}/compare/${P}...${z}?quick_pull=1&title=${encodeURIComponent(Xsf)}&body=${encodeURIComponent(Gsf`
- `https://github.com/${MH`
- `https://github.com/${x}/${d`
- `https://login.microsoftonline.com/${fz1}/`
### removed
- `http://${P}:${M.port}/sse`
- `http://169.254.169.254${yhf`
- `https://${h}/${R}/${x`
- `https://${K}/${q`
- `https://${p}/${b}/${d`
- `https://github.com/${_H`
- `https://github.com/${b}/${d`
- `https://github.com/${EH`
- `https://github.com/${H}/compare/${P}...${z}?quick_pull=1&title=${encodeURIComponent(Xa8)}&body=${encodeURIComponent(Ga8`
- `https://login.microsoftonline.com/${nP1}/`

