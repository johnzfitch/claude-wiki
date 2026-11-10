---
title: "Get Compliance Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/compliance_settings/retrieve"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:37Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings)

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

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Returns



BetaComplianceSettings object{ type: "compliance_settings", state }





type: "compliance_settings"



defaultcompliance_settings



state: [BetaComplianceSettingsState](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings#beta_compliance_settings_state)



Whether the Compliance API is enabled for this organization.

One of the following:



BetaComplianceSettingsStateEnabled object{ type: "enabled" }





type: "enabled"



defaultenabled



BetaComplianceSettingsStateDisabled object{ type: "disabled" }

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
