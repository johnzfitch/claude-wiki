---
title: "Compliance Settings - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/compliance_settings"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-02T06:26:59Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this API exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/compliance_settings).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)

# Compliance Settings

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Get Compliance Settings](https://platform.claude.com/docs/en/api/http/organization/compliance_settings/retrieve)

GET/v1/organizations/compliance_settings

Retrieve your organization's Compliance Settings.

##### [Update Compliance Settings](https://platform.claude.com/docs/en/api/http/organization/compliance_settings/update)

POST/v1/organizations/compliance_settings

Update your organization's Compliance Settings.

##### Models



ComplianceSettingsState = [ComplianceSettingsStateEnabled](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state_enabled) or [ComplianceSettingsStateDisabled](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state_disabled)



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



ComplianceSettingsStateDisabled object{ type: "disabled" }





type: "disabled"



defaultdisabled



ComplianceSettingsStateDisabledParam object{ type: "disabled" }



type: "disabled"





ComplianceSettingsStateEnabled object{ type: "enabled" }





type: "enabled"



defaultenabled



ComplianceSettingsStateEnabledParam object{ type: "enabled" }



type: "enabled"





ComplianceSettingsStateParam = [ComplianceSettingsStateEnabledParam](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state_enabled_param) or [ComplianceSettingsStateDisabledParam](https://platform.claude.com/docs/en/api/http/organization/compliance_settings#compliance_settings_state_disabled_param)



One of the following:



ComplianceSettingsStateEnabledParam object{ type: "enabled" }



type: "enabled"





ComplianceSettingsStateDisabledParam object{ type: "disabled" }



type: "disabled"



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
