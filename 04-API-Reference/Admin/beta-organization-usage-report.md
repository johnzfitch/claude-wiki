---
title: "Usage Report - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/usage_report"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:36:01Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Usage Report

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Get Messages Usage Report](https://platform.claude.com/docs/en/api/http/beta/organization/usage_report/retrieve_messages)

GET/v1/organizations/usage_report/messages

\[Legacy\] Get a report of your organization's Messages API usage, aggregated into time buckets.

##### [Get Claude Code Usage Report](https://platform.claude.com/docs/en/api/http/beta/organization/usage_report/retrieve_claude_code)

GET/v1/organizations/usage_report/claude_code

Retrieve daily aggregated usage metrics for Claude Code users. Enables organizations to analyze developer productivity and build custom dashboards.

##### Models



BetaClaudeCodeUsageReport object{ data, has_more, next_page }





BetaMessagesUsageReport object{ data, has_more, next_page }
