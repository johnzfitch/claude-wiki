---
title: "Security Posture - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/organizations/security_posture"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-18T06:27:25Z"
tags: ["api", "security"]
---

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](../Other/manage-claude-compliance-api-access.md)

Copy page



API version 2026-10-21

1.  [API reference](../Endpoints/http.md)
2.  [Compliance API](../Endpoints/http-compliance.md)
3.  [Organizations](https://platform.claude.com/docs/en/api/http/compliance/organizations)

# Security Posture

Copy page



API version 2026-10-21

##### [Get an organization's security posture](https://platform.claude.com/docs/en/api/http/compliance/organizations/security_posture/retrieve)

GET/v1/compliance/organizations/{organization_id}/security_posture

Get an organization's security controls and their current results.

##### Models



SecurityPostureRetrieveResponse object{ type: "security_posture", comments_status, controls, 2 more }



An organization's security controls and their results at one moment.
