---
title: "Compliance Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/compliance_settings"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-05T06:35:57Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Compliance Settings

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Get Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings/retrieve)

GET/v1/organizations/compliance_settings

Retrieve your organization's Compliance Settings.

##### [Update Compliance Settings](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings/update)

POST/v1/organizations/compliance_settings

Update your organization's Compliance Settings.

##### Models

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



BetaComplianceSettingsState = [BetaComplianceSettingsStateEnabled](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings#beta_compliance_settings_state_enabled) or [BetaComplianceSettingsStateDisabled](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings#beta_compliance_settings_state_disabled)



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



BetaComplianceSettingsStateDisabled object{ type: "disabled" }





type: "disabled"



defaultdisabled



BetaComplianceSettingsStateDisabledParam object{ type: "disabled" }



type: "disabled"





BetaComplianceSettingsStateEnabled object{ type: "enabled" }





type: "enabled"



defaultenabled



BetaComplianceSettingsStateEnabledParam object{ type: "enabled" }



type: "enabled"





BetaComplianceSettingsStateParam = [BetaComplianceSettingsStateEnabledParam](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings#beta_compliance_settings_state_enabled_param) or [BetaComplianceSettingsStateDisabledParam](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings#beta_compliance_settings_state_disabled_param)



One of the following:



BetaComplianceSettingsStateEnabledParam object{ type: "enabled" }



type: "enabled"





BetaComplianceSettingsStateDisabledParam object{ type: "disabled" }
