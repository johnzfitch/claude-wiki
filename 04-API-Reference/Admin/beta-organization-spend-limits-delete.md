---
title: "Delete Spend Limit - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/spend_limits/delete"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:40Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Spend Limits](https://platform.claude.com/docs/en/api/http/beta/organization/spend_limits)

# Delete Spend Limit

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/organizations/spend_limits/{spend_limit_id}

Delete a spend limit.

For a Claude Enterprise organization, this deletes a per-user override, and the member falls back to any inherited spend limit at that period. Its seat-tier, group, and organization-level rows cannot be deleted via this endpoint. A Claude Console organization deletes its organization and workspace limits, but not its `usage_tier` limit. Deleting organization and workspace limits through the API is in an early access preview.

##### Path parameters

spend_limit_id: string



ID of the Spend Limit.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns



type: "spend_limit_deleted"



defaultspend_limit_deleted

id: string



Delete Spend Limit

cURL



```python
curl https://api.anthropic.com/v1/organizations/spend_limits/$SPEND_LIMIT_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
