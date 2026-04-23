---
title: "Env var runtime behavior (binary-derived)"
category: "19-Reference"
---

# Env var runtime behavior (binary-derived)

Binaries analyzed:
- /home/zack/.local/share/claude/versions/2.1.55
- /home/zack/.local/share/claude/versions/2.1.59

## 2.1.55-introduced vars

- CLAUDE_CODE_ACCOUNT_UUID
  - Used in startup auth bootstrap (`A5A`): read alongside `CLAUDE_CODE_USER_EMAIL` and `CLAUDE_CODE_ORGANIZATION_UUID`.
  - If all three are present, seeds in-memory OAuth account state before profile fetch.
  - If access-token profile fetch succeeds, fetched profile overrides env-seeded values.
  - First occurrence offset in 2.1.55: `106574142`.

- CLAUDE_CODE_USER_EMAIL
  - Same path as above; paired with account/org UUID for OAuth account bootstrap.
  - First occurrence offset in 2.1.55: `106574181`.

- CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS
  - Parsed as positive integer milliseconds (`H9H`), default constant `120000` ms.
  - Applied to plugin marketplace git operations: `fetch`, `checkout`, `pull`, and timeout error messaging.
  - First occurrence offset in 2.1.55: `108338029`.

- CLAUDE_CODE_WORKER_EPOCH
  - Required integer for CCR worker lifecycle (`CCRClient.initialize`).
  - Missing/invalid value throws hard error.
  - Injected into worker status/heartbeat/event payloads as `worker_epoch`; 409 mismatch triggers shutdown.
  - First occurrence offset in 2.1.55: `113617025`.

- SAFEUSER
  - Used only in the built-in `commit-push-pr` prompt template context.
  - Explicitly used to prefix branch names; fallback to `USER`/`whoami` when empty.
  - First occurrence offset in 2.1.55: `111809690`.

## 2.1.59-introduced vars

- AUDIO_CAPTURE_NODE_PATH
  - Overrides path of native audio capture `.node` module loaded via `require(...)`.
  - If unset, loader falls back to bundled platform path (`audio-capture/<arch-os>/audio-capture.node`).
  - First occurrence offset in 2.1.59: `112724773`.

- CLAUDE_CODE_OAUTH_REFRESH_TOKEN
  - Enables non-browser login path in `authLogin` (`E59`).
  - Requires `CLAUDE_CODE_OAUTH_SCOPES`; then calls refresh-token exchange (`GRH(refreshToken,{scopes})`) and installs resulting OAuth tokens.
  - On success prints `Login successful.` and exits 0; on failure prints error and exits 1.
  - First occurrence offset in 2.1.59: `110848691`.

- CLAUDE_CODE_OAUTH_SCOPES
  - Mandatory when refresh-token login path is used.
  - Parsed as whitespace-separated scopes (`split(/\s+/).filter(Boolean)`) and passed to token exchange.
  - Missing value prints guidance and exits 1.
  - First occurrence offset in 2.1.59: `110848747`.

- CLAUDE_CODE_PLUGIN_USE_ZIP_CACHE
  - Boolean gate for plugin ZIP-cache path.
  - When enabled, plugin cache helpers read `CLAUDE_CODE_PLUGIN_CACHE_DIR` and use zip-cache files (`known_marketplaces.json`, marketplace/plugin cache dirs).
  - First occurrence offset in 2.1.59: `107983531`.

- P4PORT
  - In VCS detection (`KUL`), if set, it force-adds `perforce` to detected VCS types.
  - This is feature detection hinting, not itself a connection routine.
  - First occurrence offset in 2.1.59: `104390904`.

- VOICE_STREAM_BASE_URL
  - Overrides WebSocket base URL for voice speech-to-text streaming.
  - If unset, defaults to derived Claude origin (`https`->`wss`) and appends `/api/ws/speech_to_text/voice_stream`.
  - First occurrence offset in 2.1.59: `112721274`.
