---
title: "Get Compliance Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/compliance_settings/retrieve"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-02T06:26:39Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings/retrieve).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Compliance Settings](https://platform.claude.com/docs/en/api/http/organization/compliance_settings)

# Get Compliance Settings

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

GET/v1/organizations/compliance_settings

Retrieve your organization's Compliance Settings.

Compliance Settings is a singleton resource: there is exactly one per organization, addressed without an identifier. The `state` field reflects whether the Compliance API is enabled. An organization with a parent organization reads the state inherited from the parent's configuration.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



OrganizationComplianceSettings object{ type: "compliance_settings", state }





type: "compliance_settings"



defaultcompliance_settings



state: [ComplianceSettingsState](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state)



Whether the Compliance API is enabled for this organization.

One of the following:



ComplianceSettingsStateEnabled object{ type: "enabled" }





type: "enabled"



defaultenabled



ComplianceSettingsStateDisabled object{ type: "disabled" }





type: "disabled"



defaultdisabled

Get Compliance Settings

cURL



```python
curl https://api.anthropic.com/v1/organizations/compliance_settings \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
