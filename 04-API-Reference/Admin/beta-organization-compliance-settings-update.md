---
title: "Update Compliance Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/compliance_settings/update"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:16Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)
4.  [Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings)

# Update Compliance Settings

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/compliance_settings

Update your organization's Compliance Settings.

Setting `state` to `enabled` turns on the Compliance API and begins capturing organization activity events. Setting it to `disabled` turns both off. Access Transparency events are an exception: they are still captured while the Compliance API is disabled, and the Compliance API activity feed returns them once it is enabled again. `state` reflects whether the Compliance API is enabled.

A request that sets `state` to its current value succeeds and leaves the resource unchanged. A `disabled` request stays in effect until a later `enabled` request or the organization's next provisioning action that enables Access Transparency: enabling Access Transparency also enables the Compliance API, which serves its activity events, so such provisioning (including re-runs) re-enables the Compliance API even after a `disabled` request. Automated provisioning never disables compliance settings.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](../Endpoints/versioning.md).

##### Body



state: [BetaComplianceSettingsStateParam](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings#beta_compliance_settings_state_param)



Desired state. Accepts the string shorthand "enabled" or "disabled" in place of the object form; the response always returns the canonical object form.

One of the following:



BetaComplianceSettingsStateEnabledParam object{ type: "enabled" }



type: "enabled"





BetaComplianceSettingsStateDisabledParam object{ type: "disabled" }



type: "disabled"



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

Update Compliance Settings

cURL



```python
curl https://api.anthropic.com/v1/organizations/compliance_settings \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
