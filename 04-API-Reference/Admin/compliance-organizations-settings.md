---
title: "Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/settings"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-13T06:36:14Z"
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

# Settings

Copy page



API version 2026-10-21

##### [Get effective organization settings](https://platform.claude.com/docs/en/api/http/compliance/organizations/settings/retrieve)

GET/v1/compliance/organizations/{organization_id}/settings

Retrieve the effective settings for an organization.

##### Models



SettingRetrieveResponse object{ type: "effective_organization_settings", api_keys, organization_id, settings }



The resolved settings in force for one organization at read time.

Settings appear at most once each, in a fixed relative order, and values reflect the enforced state. A setting the organization's administrators cannot change — for example, one controlled by Anthropic policy or not available to the organization — is omitted from the list. Settings that report a compliance arrangement with Anthropic are the exception: the HIPAA and Access Transparency settings are always included; the API zero data retention setting is reported for Claude Console organizations, and the Claude Code zero data retention and customer-managed encryption keys (CMEK) settings for Claude Enterprise organizations. Each reports whether the arrangement is in place at the organization level; a retention setting on an individual workspace is not reflected.
