---
title: "User Preferences - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/user_preferences"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:36:09Z"
tags: ["api"]
---

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Organizations](https://platform.claude.com/docs/en/api/http/compliance/organizations)

# User Preferences

Copy page



API version 2026-10-21

##### [List organization members' personal preferences](https://platform.claude.com/docs/en/api/http/compliance/organizations/user_preferences/list)

GET/v1/compliance/organizations/{org_uuid}/user_preferences

This endpoint is in beta.

##### Models



UserPreferenceListResponse object{ conversation_preferences, cowork_global_instructions, user }



The personal preferences a member of the organization has written in their settings.

conversation_preferences: string or null



The member's "Instructions for Claude" text from their personal settings, with leading and trailing whitespace removed. `null` when the member has never set it or has cleared it.

cowork_global_instructions: string or null



The member's "Global instructions" text for Cowork, Claude's desktop agent, with leading and trailing whitespace removed. `null` when the member has never set it or has cleared it.



user: object{ id, email_address }



The organization member.
