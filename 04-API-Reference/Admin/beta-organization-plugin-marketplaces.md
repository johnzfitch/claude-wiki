---
title: "Plugin Marketplaces - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/plugin_marketplaces"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-02T06:26:33Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Plugin Marketplaces

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [List Plugin Marketplaces](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/list)

GET/v1/organizations/plugin_marketplaces

List the plugin marketplaces Plugins live in, newest first: the organization's own and its members' personal ones.

##### [Get Plugin Marketplace](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/retrieve)

GET/v1/organizations/plugin_marketplaces/{marketplace_id}

Retrieve a plugin marketplace by ID.

##### [Update Plugin Marketplace](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/update)

POST/v1/organizations/plugin_marketplaces/{marketplace_id}

Set the default installation setting of one of the organization's own plugin marketplaces. Every Plugin in it without a setting of its own gets this default as its organization-wide setting, including Plugins added later.

##### [Validate Plugin Marketplace Repository](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/validate_repository)

POST/v1/organizations/plugin_marketplaces/validate_repository

Check whether a plugin marketplace held in a public GitHub repository would synchronize into claude.ai, without connecting or storing it.

##### [Validate Plugin Marketplace Archive](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces/validate_archive)

POST/v1/organizations/plugin_marketplaces/validate_archive

Check whether a plugin marketplace, uploaded as a `.zip` of the marketplace directory, would synchronize into claude.ai, without connecting or storing it.

##### Models



BetaPluginMarketplace object{ type: "plugin_marketplace", id, created_at, 7 more }





BetaPluginMarketplaceValidationPluginError object{ error, error_code, name }



error: string



Why the plugin would be skipped by a synchronization.

error_code: string



A stable identifier for the reason — the value to branch on.

name: string



The plugin's name, as its entry in marketplace.json declares it.



BetaPluginMarketplaceValidationPluginWarning object{ error_code, message }



error_code: string



A stable identifier for the kind of warning.

message: string



What would be left out, and why.



BetaPluginMarketplaceValidationPluginWarnings object{ name, warnings }



name: string



The plugin's name, as its entry in marketplace.json declares it.



warnings: array of [BetaPluginMarketplaceValidationPluginWarning](https://platform.claude.com/docs/en/api/http/beta/organization/plugin_marketplaces#beta_plugin_marketplace_validation_plugin_warning) { error_code, message }



The parts of the plugin a synchronization would leave out.

error_code: string



A stable identifier for the kind of warning.

message: string



What would be left out, and why.



BetaPluginMarketplaceValidationReport object{ type: "plugin_marketplace_validation_report", commit_sha, manifest_error, 6 more }



The outcome of validating plugin marketplace content: a report, not a stored object, so nothing in it can be retrieved afterwards.
