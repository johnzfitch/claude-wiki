---
title: "New Functions Module: 2.1.70"
category: "19-Reference"
---

# New Functions Module: 2.1.70

## Summary

**+8,660 functions** (60,300 → 68,960), estimated from `.text` size delta (+4,340,776 bytes).

Fast-profile analysis does not enumerate individual functions. The new functions are
attributed to subsystems based on string evidence from the JS payload diff.

## Attribution by Subsystem

| Subsystem | Evidence | Estimated new functions |
|-----------|----------|------------------------|
| model-routing (Foundry) | AWS SDK, FoundryClient, DefaultAzureCredential | ~2,000–3,000 |
| model-routing (Bedrock expanded) | @aws-sdk/client-bedrock, reranking, inference profiles | ~1,500–2,000 |
| auth (MCP OAuth) | OAuth lifecycle, token refresh | ~500–800 |
| session (remote control) | RemoteSessionManager, keepalives | ~500–800 |
| voice (audio capture) | audio-capture.node integration | ~200–400 |
| worker (token recovery) | max_output_tokens_recovery | ~100–200 |
| team (CoWork) | teammate_id, memory sync | ~200–400 |
| runtime (exception tables) | .gcc_except_table/.eh_frame | ~1,000–2,000 |
| **Total attributed** | | **~6,000–9,600** |

Note: Range reflects uncertainty from minification. The AWS SDK bundles (Bedrock + Foundry)
likely account for the bulk of new functions due to their comprehensive API surface.

## BunFS JS Payload New Code

From the cli.js diff (+6,882 lines added, -5,688 removed, net +1,194):

### High-frequency new identifiers
| Pattern | Occurrences (new lines) |
|---------|------------------------|
| `pr` / `PR` / `Pr` | ~25,000 |
| `Token` / `token` | ~5,000 |
| `Agent` / `agent` | ~2,800 |
| `hook` / `Hook` | ~1,800 |
| `mcp` / `MCP` / `Mcp` | ~1,700 |
| `Permission` / `permission` | ~1,500 |
| `team` / `Team` | ~1,100 |
| `SSO` / `sso` | ~900 |
| `Credential` / `credential` | ~1,100 |
| `plan` / `Plan` | ~800 |
| `Sandbox` / `sandbox` | ~400 |
| `Worktree` / `worktree` | ~280 |
| `LSP` | ~157 |
| `Transcri` | ~187 |
| `audio` / `voice` | ~280 |

### New class names (filtered from new JS lines)
- `BedrockClient`, `BedrockRuntimeClient`, `AmazonBedrockControlPlaneService`
- `CognitoIdentityClient`, `AWSCognitoIdentityService`
- `AssumeRoleCommand`, `AssumeRoleWithWebIdentityCommand`
- `GetCredentialsForIdentityCommand`, `GetRoleCredentialsCommand`
- `ExternalAccountClient`, `BaseExternalAccountClient`, `UserRefreshClient`
- `PluggableAuthClient`, `IdTokenClient`, `DownscopedClient`
- `OAuthClientAuthHandler`
- `RemoteSessionManager`
- `ConnectivityState`
- `HttpsProxyAgent`, `HttpProxyAgent`, `NodeHttpHandler`
- `ProxyTracerProvider`
- `FileWatcherCertificateProvider`
- `FoundryClient` (inferred from string context)
- `ExitPlanMode` (tool class)
- `CountTokensCommand`
- `ListInferenceProfilesCommand`, `GetInferenceProfileCommand`

## Functions to Investigate (for full analysis)

When a complete Ghidra analysis of 2.1.70 is available:
1. Search `no-callers` functions — likely new entry points or new MCP tool handlers
2. Functions calling into `RemoteSessionManager` — remote control architecture
3. Functions in `.init_array` (7 new) — new startup subsystems
4. Functions with `voice|audio|transcript` string references — audio pipeline
