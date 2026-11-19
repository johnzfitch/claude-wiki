---
title: "Activities - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/activities"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:36:07Z"
tags: ["api"]
---

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)

# Activities

Copy page



API version 2026-10-21

##### [Query compliance activities](https://platform.claude.com/docs/en/api/http/compliance/activities/list)

GET/v1/compliance/activities

List compliance activities for the authenticated tenant.

##### Models



ActivityListResponse = AbuseDecisionReceived or AccountDeleted or AccountMigrationCompleted or 589 more
