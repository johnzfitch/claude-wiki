---
title: "Detach Bundle - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/claude_tag/bundles/targets/delete"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-08T06:24:15Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Claude Tag](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag)
5.  [Bundles](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles)
6.  [Targets](https://platform.claude.com/docs/en/api/http/beta/organization/claude_tag/bundles/targets)

# Detach Bundle

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/organizations/claude_tag/bundles/{bundle_id}/targets/{target_id}

Requires `anthropic-beta: ``experimental-claude-tag-2026-10-21`. [How to send beta headers](../Endpoints/beta-headers.md)

Detach a Bundle from a Slack channel or a Slack workspace. A repeated detach returns 404.

##### Path parameters

bundle_id: string



The Bundle's identifier, starting with `capp_`.

target_id: string



The Bundle Target's identifier, starting with `btgt_`. Attach Bundle and List Bundle Targets return it. It is never the identifier of the channel or workspace.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).



"anthropic-beta": optional array of [AnthropicBeta](../Endpoints/platform-claude-com-http-beta.md#anthropic_beta)



This endpoint is in beta: requests must send `experimental-claude-tag-2026-10-21` in this header.

One of the following:

string



"message-batches-2024-09-24"



"prompt-caching-2024-07-31"



"computer-use-2024-10-22"



"computer-use-2025-01-24"



"pdfs-2024-09-25"



"token-counting-2024-11-01"



"token-efficient-tools-2025-02-19"



"output-128k-2025-02-19"



"files-api-2025-04-14"



"mcp-client-2025-04-04"



"mcp-client-2025-11-20"



"dev-full-thinking-2025-05-14"



"interleaved-thinking-2025-05-14"



"code-execution-2025-05-22"



"extended-cache-ttl-2025-04-11"



"context-1m-2025-08-07"



"context-management-2025-06-27"



"model-context-window-exceeded-2025-08-26"



"skills-2025-10-02"



"fast-mode-2026-02-01"



"output-300k-2026-03-24"



"user-profiles-2026-03-24"



"user-profiles-2026-08-18"



"user-profiles-2026-09-04"



"advisor-tool-2026-03-01"



"managed-agents-2026-04-01"



"cache-diagnosis-2026-04-07"



"dreaming-2026-04-21"



"thinking-token-count-2026-05-13"



"server-side-fallback-2026-06-01"



"server-side-fallback-2026-07-01"



"fallback-credit-2026-06-01"



"fallback-credit-2026-07-01"



"agent-memory-2026-07-22"



"mid-conversation-tool-changes-2026-07-01"



"compact-2026-01-12"



"computer-use-2025-11-24"



"mcp-tunnels-2026-06-22"



"structured-outputs-2025-11-13"



"task-budgets-2026-03-13"



"thinking-display-updates-2026-08-18"



"ce-user-management-2026-07-13"



"mid-conversation-output-config-2026-07-01"



"thinking-binding-controls-2026-08-01"



"mid-conversation-system-clear-at-2026-08-21"



"compact-2026-09-04"



"inline-tools-2026-09-15"



"mcp-client-2026-09-15"



"ce-plugins-2026-09-01"



"spend-limit-reads-2026-09-26"



"telemetry-destinations-2026-08-11"



"webhooks-2026-10-07"



"message-threads-2026-08-12"



"analytics-usage-cost-2026-08-24"



"experimental-claude-tag-2026-10-21"



##### Returns



BetaClaudeTagDeletedBundleTarget object{ type: "bundle_target_deleted", id }



Confirms that a Bundle was detached.

type: "bundle_target_deleted"



id: string



The identifier the Bundle Target had.

Detach Bundle

cURL



```python
curl https://api.anthropic.com/v1/organizations/claude_tag/bundles/$BUNDLE_ID/targets/$TARGET_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H 'anthropic-beta: experimental-claude-tag-2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "id",
  "type": "bundle_target_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "id",
  "type": "bundle_target_deleted"
