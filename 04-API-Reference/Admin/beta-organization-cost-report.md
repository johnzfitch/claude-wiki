---
title: "Cost Report - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/cost_report"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:34:14Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Cost Report

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Get Cost Report](https://platform.claude.com/docs/en/api/http/beta/organization/cost_report/retrieve)

GET/v1/organizations/cost_report

\[Legacy\] Get a report of your organization's Claude API costs in USD, aggregated into daily buckets.

##### Models



BetaCostReport object{ data, has_more, next_page }
