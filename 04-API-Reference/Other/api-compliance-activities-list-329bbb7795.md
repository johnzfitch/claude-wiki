---
title: "Query compliance activities - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/compliance/activities/list"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:07Z"
tags: ["api"]
---

- [Managed Agents](/docs/en/managed-agents/overview)

- [Admin](/docs/en/manage-claude/admin-api)

- Resources
  - [Best practices](/docs/en/about-claude/use-case-guides/overview)
  - [Models & pricing](/docs/en/models/overview)
  - [CLI, SDKs, and libraries](/docs/en/cli-sdks-libraries/overview)
  - [Claude API skill](/docs/en/agents-and-tools/agent-skills/claude-api-skill)
  - [Release notes](/docs/en/release-notes/overview)

[API reference](/docs/en/api/overview)




[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fapi%2Fcompliance%2Factivities%2Flist)





SearchCtrlK

Include beta APIs

Using the API

[Features overview](/docs/en/api/overview)[Beta headers](/docs/en/api/beta-headers)[Errors](/docs/en/api/errors)


Messages


Create a Message


Count tokens in a Message

Batches

Managed Agents

Agents

Environments

Sessions

Deployments

Deployment Runs

Vaults

Memory Stores

Dreams


Files


Upload File


List Files


Download File


Get File Metadata


Delete File


Models


List Models


Get a Model


Skills


Create Skill


List Skills


Get Skill


Delete Skill

Versions


Organization


Get Current Organization

API Keys

External Keys

Federation

Invites

Service Accounts

Users

Workspaces

Rate Limits

Compliance Settings

Usage Report

Cost Report

MCP Tunnels

Analytics

Spend Limits

RBAC Groups

RBAC Roles


Tunnels


Create Tunnel


Get Tunnel


List Tunnels


Archive Tunnel


Reveal Tunnel Token


Rotate Tunnel Token

Certificates


User Profiles


Create User Profile


List User Profiles


Get User Profile


Update User Profile


Create Enrollment URL


Compliance API

Activities


Query compliance activities

Organizations

Groups

Apps

Code


Completions


Create a Text Completion

Support & configuration

[Rate limits](/docs/en/api/rate-limits)[Service tiers](/docs/en/api/service-tiers)[IAM actions (Claude Platform on AWS)](/docs/en/api/claude-platform-on-aws-iam-actions)[Versions](/docs/en/api/versioning)[IP addresses](/docs/en/api/ip-addresses)[Supported regions](/docs/en/api/supported-regions)

Claude Code

[Trigger a routine](/docs/en/api/claude-code/routines-fire)

[Console](/)

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)

Copy page



1.  [API reference](/docs/en/api/http)
2.  [Compliance API](/docs/en/api/http/compliance)
3.  [Activities](/docs/en/api/http/compliance/activities)

# Query compliance activities

GET/v1/compliance/activities

List compliance activities for the authenticated tenant.

The tenant is the caller's parent organization, or — for an organization with no parent — the organization itself. Returns a paginated list of compliance activities that can be filtered by various criteria.

##### Query parameters



activity_types: optional array of "abuse_decision_received" or "account_deleted" or "admin_api_key_created" or 511 more



Filter activities by type. See the response `data` schema for the additional fields each type returns. Cannot be combined with `exclude_activity_types[]`.

One of the following:

"abuse_decision_received"



An external anti-abuse service reported a consequential decision about a sign-in or sign-up attempt.

"account_deleted"



User-initiated self-service account deletion.

"admin_api_key_created"



An admin API key was created.

"admin_api_key_deleted"



An admin API key was deleted.

"admin_api_key_updated"



An admin API key was updated (renamed or activated/deactivated).

"admin_connector_request_resolved"



Admin approved or dismissed pending member requests to enable an MCP connector.

"admin_request_created"



Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).

"admin_setup_checklist_step_delegated"



A step of the Claude Enterprise admin setup checklist was delegated to a teammate — an organization member, or an email address that has not joined the organization yet — replacing any earlier delegation of that step.

"admin_setup_checklist_step_delegation_cancelled"



The delegation of a Claude Enterprise admin setup checklist step was cancelled.

"age_verified"



User age was verified.

"anonymous_mobile_login_attempted"



Anonymous mobile login was attempted.

"api_key_created"



Activity logged when a new API key is created.

"audit_log_export_accessed"



Audit log export file was accessed/downloaded via signed URL.

"audit_log_export_started"



Audit log export was initiated.

"billing_emails_updated"



The organization's billing email recipients were updated.

"ccr_agent_created"



A Claude Code agent was created.

"ccr_agent_deleted"



A Claude Code agent was deleted.

"ccr_agent_proxy_anthropic_oidc_token_exchanged"



The Claude Code agent proxy exchanged a minted identity token for short-lived credentials in the organization's own cloud. Recorded for exchange targets only (such as "aws" and "gcp"; the "direct" target has no exchange step). One event is recorded per exchange call; a request served from the proxy's exchanged-credential cache does not exchange again and is not recorded here. Per-request detail for traffic the credentials were injected into is available in the agent proxy network events.

"ccr_agent_proxy_anthropic_oidc_token_minted"



The Claude Code agent proxy minted a short-lived identity token for an anthropic_oidc credential. One event is recorded per fresh token issuance; a request served from the proxy's short-lived token cache does not mint a new token and is not recorded here. Per-request detail for traffic the credential was injected into is available in the agent proxy network events.

"ccr_agent_proxy_credential_created"



A Claude Code agent proxy credential was created. Credentials hold the secrets the agent proxy injects into requests Claude Code sessions send to approved external services; each credential belongs to an agent proxy profile. Audit events carry only credential names and settings, never the secret material itself.

"ccr_agent_proxy_credential_deleted"



A Claude Code agent proxy credential was deleted. Its secret material was removed and can no longer be sent to any host.

"ccr_agent_proxy_credential_rotated"



A Claude Code agent proxy credential's secret material was replaced. The replacement keeps the same name, profile, and allowed hosts under a new credential identifier, and everything that referenced the old credential now uses the replacement.

"ccr_agent_proxy_credential_updated"



A Claude Code agent proxy credential's settings were updated. Only the display name and the allowed host patterns can be updated; the secret material can only be replaced through a rotation.

"ccr_agent_proxy_destination_deleted"



An agent proxy destination was deleted.

"ccr_agent_proxy_network_events_listed"



A Claude Code network activity export was accessed for the given hour.

"ccr_agent_proxy_profile_bound"



A Claude Code agent proxy profile was bound to a scope, applying its policy to Claude Code sessions in that scope.

"ccr_agent_proxy_profile_created"



A Claude Code agent proxy profile was created. Agent proxy profiles are named, reusable bundles of access policy that administrators bind to parts of the organization.

"ccr_agent_proxy_profile_deleted"



A Claude Code agent proxy profile was deleted, removing its policy from everything it was bound to.

"ccr_agent_proxy_profile_unbound"



A Claude Code agent proxy profile was unbound from a scope, removing its policy from Claude Code sessions in that scope.

"ccr_agent_proxy_profile_updated"



A Claude Code agent proxy profile's configuration was updated.

"ccr_agent_proxy_provisioning_credential_rejected"



An organization owner rejected a credential that a teammate submitted via an agent proxy provisioning link: the credential and its disabled rule were deleted and the link was revoked. The actor is the owner; the submitter is recorded for attribution.

"ccr_agent_proxy_provisioning_link_enabled"



An organization owner enabled a credential that a teammate submitted via an agent proxy provisioning link: the disabled rule created at submission was switched to enforce, so the credential now takes traffic. The actor is the owner; the submitter is the actor on the prior ccr_agent_proxy_provisioning_link_submitted event.

"ccr_agent_proxy_provisioning_link_generated"



An organization owner generated a one-time agent proxy credential provisioning link so a teammate can submit a credential into the target agent proxy profile without holding the owner role.

"ccr_agent_proxy_provisioning_link_revoked"



An organization owner revoked an unfilled agent proxy provisioning link.

"ccr_agent_proxy_provisioning_link_submitted"



A teammate submitted a credential via an agent proxy provisioning link. The credential and a disabled rule are created; the credential takes traffic only after an organization owner enables the submitted credential. This event records the link-mediated lifecycle; the credential itself additionally emits ccr_agent_proxy_credential_created.

"ccr_agent_proxy_rule_created"



An agent proxy rule was created. A rule decides what happens to a session's outbound requests that match it.

"ccr_agent_proxy_rule_deleted"



An agent proxy rule was deleted.

"ccr_agent_proxy_rule_updated"



An agent proxy rule was updated. An update replaces everything the rule matches and does, so the host name patterns here are the rule's complete set after the update.

"ccr_agent_slack_access_scope_created"



A Claude Code agent was granted access to read or write in an additional Slack channel beyond the one it is assigned to.

"ccr_agent_slack_access_scope_deleted"



A Claude Code agent's access to an additional Slack channel was revoked.

"ccr_agent_slack_binding_created"



A Claude Code agent was assigned to a Slack channel or workspace as its dedicated agent.

"ccr_agent_slack_binding_deleted"



A Claude Code agent's assignment to a Slack channel or workspace was removed.

"ccr_agent_updated"



A Claude Code agent's configuration was updated. Also emitted with updated_fields \["is_virtual"\] alone when an auto-provisioned agent is promoted to a configured one, whether by an update request targeting it or by binding an agent proxy profile to it.

"ccr_channel_manager_added"



An org owner/admin assigned an organization member to manage the Claude-in-Slack configuration of one Slack channel.

"ccr_channel_manager_removed"



An org owner/admin removed an organization member's assignment to manage the Claude-in-Slack configuration of one Slack channel.

"ccr_role_channel_assignment_deleted"



CcrRoleChannelAssignmentDeleted is emitted when an org owner/admin removes an RBAC role's channel assignment row (the role reverts to granting zero channels).

"ccr_role_channel_assignment_updated"



CcrRoleChannelAssignmentUpdated is emitted when an org owner/admin sets or replaces the list of Slack channels an RBAC role's holders may configure via the delegated Claude-in-Slack channel-manage surface.

"ccr_session_created"



A Claude Code session was created. A session is one coding interaction with Claude.

"ccr_session_deleted"



A Claude Code session was deleted.

"ccr_session_updated"



A Claude Code session's settings were updated.

"ccr_slack_channel_joined"



Claude's Slack app joined a public Slack channel at an organization administrator's request.

"claude_artifact_access_failed"



An attempt to access an artifact failed.

"claude_artifact_commented"



Comment activity on a published artifact: a comment was added, a thread's resolved state was changed, or a thread was deleted. The actor is the user who performed the action; the comment text itself is stored with the artifact and is not part of this record.

"claude_artifact_comments_viewed"



An artifact's comments were viewed.

"claude_artifact_created"



An artifact was created.

"claude_artifact_duplicated"



A user duplicated an artifact they could view into a new artifact that they own. The actor is the user who created the copy; the source artifact is not modified.

"claude_artifact_external_sharing_permission_updated"



An organization admin allowed one artifact to be shared outside the organization by link while the organization-wide external sharing setting was off, or revoked that permission.

"claude_artifact_invite_accepted"



Someone outside the organization signed in with a verified account for the invited address and accepted an invitation to an artifact, and can now open it; recorded in the artifact owner's organization. The person who accepted is identified by `invitee_email` and `invitee_user_id`.

"claude_artifact_invite_created"



A member invited (or re-invited) an email address outside the organization to an artifact; recorded in the artifact owner's organization with the inviting member as the actor.

"claude_artifact_invite_revoked"



A member withdrew an invitation to an artifact for someone outside the organization, removing any access that invitation had granted; recorded in the artifact owner's organization with that member as the actor.

"claude_artifact_invite_role_updated"



A member changed the access level of an email invitation to an artifact for someone outside the organization, whether the invitation was still pending or had been accepted; recorded in the artifact owner's organization with that member as the actor.

"claude_artifact_published"



A new version of an artifact was published — for an artifact created in a chat this is the action that made it publicly viewable; for an artifact created outside a chat it is recorded when the artifact is saved, including saves of private artifacts, except that automatic saves made while a person keeps editing may be recorded periodically for that person rather than once per save; changes to who can access the artifact are recorded separately as claude_artifact_sharing_updated.

"claude_artifact_sharing_updated"



An artifact's sharing settings were updated.

"claude_artifact_viewed"



An artifact was viewed.

"claude_chat_access_failed"



A user was denied access to a Claude.ai chat conversation.

"claude_chat_created"



User created a chat.

"claude_chat_deleted"



A user deleted a Claude.ai chat conversation.

"claude_chat_deletion_failed"



A request to delete a Claude.ai chat conversation failed.

"claude_chat_settings_updated"



User updated the settings for a conversation.

"claude_chat_snapshot_created"



User created/shared a chat snapshot.

"claude_chat_snapshot_deleted"



User deleted/unshared a chat snapshot.

"claude_chat_snapshot_viewed"



User viewed a chat snapshot (authenticated or public/unauthenticated).

"claude_chat_sync_source_created"



A sync source was connected for syncing external content into Claude chats.

"claude_chat_sync_source_deleted"



A sync source was disconnected from Claude chats.

"claude_chat_sync_source_updated"



A Claude chat sync source's configuration was updated.

"claude_chat_updated"



User updated the chat metadata (e.g name, model).

"claude_chat_viewed"



A user viewed a Claude.ai chat conversation.

"claude_code_credential_revoked"



A Claude Code credential (runner pool key, runner token, or session token) was revoked. The credential itself is never recorded.

"claude_code_review_config_updated"



Claude Code Review configuration was enabled/disabled for an org.

"claude_code_review_repository_added"



A repository was added to org-level Claude Code Review configuration.

"claude_code_review_repository_removed"



A repository was removed from org-level Claude Code Review configuration.

"claude_code_review_repository_updated"



A Claude Code Review repository configuration was updated.

"claude_code_runner_deleted"



A self-hosted runner was forcibly removed from its pool. Sessions assigned to the runner were returned to the pool queue, unless a session had already been requeued repeatedly, in which case it was marked stuck instead of being requeued again.

"claude_code_runner_pool_created"



A self-hosted runner pool for Claude Code was created.

"claude_code_runner_pool_deleted"



A self-hosted runner pool was deleted.

"claude_code_runner_pool_secret_minted"



A registration key for a self-hosted runner pool was minted. Runners present this key to join the pool. The key itself is never recorded.

"claude_code_runner_pool_session_queue_updated"



An admin changed a session's position in its self-hosted runner pool's queue: requeued it onto a different runner, dismissed it from the queue, or re-admitted it for another runner provisioning attempt.

"claude_code_runner_pool_updated"



A self-hosted runner pool's settings were updated.

"claude_code_security_center_config_updated"



Claude Code Security Center scanning was enabled/disabled for an org.

"claude_code_security_scan_cancelled"



In-flight Claude Code Security scans were cancelled for a project.

"claude_code_security_scan_created"



A Claude Code Security scan was started.

"claude_code_security_scan_project_member_updated"



A person's access to a Claude Code Security scan project was granted, changed, or revoked.

"claude_code_security_scan_project_updated"



A Claude Code Security scan project was archived, unarchived, created, or migrated to a new product experience.

"claude_code_security_scan_project_visibility_updated"



A Claude Code Security scan project was shared with the organization or made private.

"claude_code_security_scan_run_updated"



A single Claude Code Security scan run was archived, unarchived, or resumed after a billing pause.

"claude_code_security_scan_schedule_deleted"



A recurring scan schedule was deleted for a Claude Code Security project.

"claude_code_security_scan_schedule_updated"



A recurring scan schedule was set or replaced for a Claude Code Security project.

"claude_code_security_vulnerability_deleted"



A Claude Code Security vulnerability finding was permanently deleted.

"claude_code_security_vulnerability_fix_session_created"



A Claude Code remediation session was created for a Claude Code Security vulnerability finding.

"claude_code_security_vulnerability_updated"



A Claude Code Security vulnerability finding was dismissed, restored, marked fixed, or reopened.

"claude_code_security_webhook_created"



A Claude Code Security outbound webhook was created.

"claude_code_security_webhook_deleted"



A Claude Code Security outbound webhook was deleted.

"claude_code_security_webhook_secret_updated"



The HMAC signing secret for a Claude Code Security webhook was rotated.

"claude_code_security_webhook_updated"



A Claude Code Security outbound webhook was updated.

"claude_code_team_memory_acl_updated"



An RBAC group was added to or removed from the Claude Code team-memory ACL.

"claude_code_team_memory_updated"



Claude Code team memory shared with the organization was updated.

"claude_code_team_onboarding_guide_updated"



A Claude Code team onboarding guide was created, updated, or deleted.

"claude_code_user_marketplaces_updated"



A user's Claude Code plugin marketplace selections were updated on Anthropic servers.

"claude_code_user_memory_updated"



A user's synced private Claude Code memory was updated or deleted on Anthropic servers.

"claude_code_user_plugins_updated"



A user's Claude Code plugin selections — which plugins are installed and enabled — were updated on Anthropic servers.

"claude_code_user_settings_updated"



A user's synced Claude Code settings were updated or deleted on Anthropic servers.

"claude_command_created"



Command was created.

"claude_command_deleted"



Command was deleted.

"claude_command_replaced"



Command was replaced.

"claude_enterprise_upgrade_credit_updated"



An organization admin cancelled, or turned back on, the monthly usage credit the organization receives for upgrading from the Team plan to the Enterprise plan, together with the recurring monthly charge that accompanies it.

"claude_file_access_failed"



A user was denied access to a file in Claude.ai.

"claude_file_deleted"



A file was deleted.

"claude_file_exported"



A file was exported from Claude to an external storage destination.

"claude_file_uploaded"



A file was uploaded.

"claude_file_viewed"



A user viewed a file in Claude.ai.

"claude_gdrive_integration_created"



A Google Drive integration was enabled for the organization.

"claude_gdrive_integration_deleted"



A Google Drive integration was disabled for the organization.

"claude_gdrive_integration_updated"



A Google Drive integration's configuration was updated.

"claude_github_integration_created"



A GitHub integration was enabled for the organization.

"claude_github_integration_deleted"



A GitHub integration was disabled for the organization.

"claude_github_integration_updated"



A GitHub integration's configuration was updated.

"claude_organization_settings_updated"



Organization settings were updated.

"claude_plugin_archive_accessed"



A version archive of a member-owned plugin, containing that member's own files, was downloaded.

"claude_plugin_created"



Plugin was created.

"claude_plugin_deleted"



Plugin was deleted.

"claude_plugin_disabled"



User disabled a plugin for their account.

"claude_plugin_enabled"



User enabled a plugin for their account.

"claude_plugin_replaced"



Plugin was replaced.

"claude_plugin_security_scan_completed"



A security scan of a plugin completed and produced a verdict.

"claude_plugin_updated"



Plugin was updated.

"claude_project_archived"



A Claude project was archived.

"claude_project_created"



A Claude project was created.

"claude_project_deleted"



A Claude project was deleted.

"claude_project_document_access_failed"



An attempt to access a document in a Claude project failed.

"claude_project_document_bulk_deletion_audit_truncated"



A bulk request to delete documents from a Claude project failed with more documents requested than were individually recorded in the audit log.

"claude_project_document_deleted"



A document was deleted from a Claude project.

"claude_project_document_deletion_failed"



A request to delete a document from a Claude project failed.

"claude_project_document_updated"



The content of a document in a Claude project was replaced in place.

"claude_project_document_uploaded"



A document was uploaded to a Claude project.

"claude_project_document_viewed"



A document in a Claude project was viewed.

"claude_project_file_access_failed"



An attempt to access a file in a Claude project failed.

"claude_project_file_bulk_deletion_audit_truncated"



A bulk request to delete files from a Claude project failed with more files requested than were individually recorded in the audit log.

"claude_project_file_deleted"



A file was deleted from a Claude project.

"claude_project_file_deletion_failed"



A request to delete a file from a Claude project failed.

"claude_project_file_uploaded"



A file was uploaded to a Claude project.

"claude_project_reported"



A Claude project was reported.

"claude_project_sharing_updated"



A Claude project's sharing settings were updated.

"claude_project_sync_source_created"



A sync source was connected to a Claude project's knowledge base.

"claude_project_sync_source_deleted"



A sync source was disconnected from a Claude project's knowledge base.

"claude_project_sync_source_updated"



A Claude project sync source's configuration was updated.

"claude_project_viewed"



A Claude project was viewed.

"claude_published_artifact_deleted"



A published artifact was deleted or unpublished — by its creator, by an organization admin, or by Anthropic (for example, when it was removed for a policy violation).

"claude_pubsec_identity_configured"



SAML IdP configuration updated for a public sector organization.

"claude_skill_created"



Skill was created.

"claude_skill_deleted"



Skill was deleted.

"claude_skill_disabled"



User disabled a skill for their account.

"claude_skill_enabled"



User enabled a skill for their account.

"claude_skill_replaced"



Skill was replaced.

"claude_skill_security_scan_completed"



A security scan of a skill completed and produced a verdict.

"claude_user_role_updated"



A user's role within the organization was changed, or the user was added to or removed from the organization.

"claude_user_seat_tier_updated"



An organization member's seat tier was changed. A null `previous_seat_tier` means the member previously had no seat assigned; a null `current_seat_tier` means the seat was removed.

"claude_user_settings_updated"



User updated their personal settings.

"cli_plugin_exec_policy_updated"



Admin set or cleared the per-op permission ceiling for a plugin CLI.

"compliance_api_accessed"



Logging event auto-generated for each compliance API request.

"cowork_session_updated"



A Cowork session was updated.

"design_project_artifact_published"



A Claude Design project's content was published as a claude.ai artifact, making a snapshot of one of its files viewable outside the project's sharing settings.

"design_project_created"



A Claude Design project was created.

"design_project_deleted"



A Claude Design project was deleted.

"design_project_member_added"



A member was granted access to a Claude Design project.

"design_project_member_removed"



A member's access to a Claude Design project was revoked.

"design_project_member_role_updated"



A Claude Design project member's role was changed.

"design_project_published"



A Claude Design template or design system was published, making it discoverable by everyone in its organization.

"design_project_sharing_updated"



A Claude Design project's link-sharing settings were changed — who the project's link works for, and what people opening it through the link may do. Access granted to individual members is reported separately (see design_project_member_added).

"design_project_unpublished"



A Claude Design template or design system was unpublished, removing it from its organization's shared gallery.

"design_project_updated"



A Claude Design project's metadata was updated.

"design_project_version_restored"



A Claude Design project's working tree was rolled back to a previously saved version, replacing its current files with that version's files.



"design_project_viewed"



A Claude Design project's content was read. The surface field records which kind of read — a project open, a full-content read, a single-file read, a saved-version read, or an export request. The actor is the reader.

This activity type is retired: project content reads are no longer recorded. Events of this type may still appear in feeds for reads that occurred while it was active.

"desktop_extension_allowlisted"



A desktop extension was added to an org's allowlist.

"desktop_extension_blocklisted"



A desktop extension was added to the global blocklist.

"desktop_extension_deleted"



A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.

"desktop_extension_removed_from_allowlist"



A desktop extension was removed from an org's allowlist.

"desktop_extension_unblocked"



A desktop extension was removed from the global blocklist.

"desktop_extension_uploaded"



A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.

"desktop_extension_version_uploaded"



A new version of an existing org-owned desktop extension was uploaded.

"domain_claim_initiated"



Domain capture claim initiated over personal accounts on verified domains.

"end_user_invite_requested"



Non-admin member submitted an invite request for a new org member.

"extra_usage_billing_enabled"



Usage credit billing was enabled for an organization.

"extra_usage_credit_granted"



A promotional usage credit grant was claimed.

"extra_usage_spend_limit_created"



Usage credit spend limit was created.

"extra_usage_spend_limit_deleted"



Usage credit spend limit was deleted.

"extra_usage_spend_limit_increase_request_approved"



A usage credit spend limit increase request was approved.

"extra_usage_spend_limit_increase_request_denied"



A usage credit spend limit increase request was denied.

"extra_usage_spend_limit_updated"



Usage credit spend limit was updated.

"ghe_configuration_created"



Admin created a GHE configuration.

"ghe_configuration_deleted"



Admin deleted a GHE configuration.

"ghe_configuration_updated"



Admin updated a GHE configuration. Previous/new field pairs are recorded only for settings that changed in the update; secret credentials are never recorded, only whether they were replaced.

"ghe_user_connected"



User connected to a GHE instance.

"ghe_user_disconnected"



User disconnected from a GHE instance.

"ghe_webhook_signature_invalid"



Webhook signature validation failed.

"github_app_installation_linked"



An installation of the Claude GitHub App (a GitHub organization or user account where the App is installed) was linked to the organization, letting the organization's Claude Code features act on that GitHub account's repositories.

"github_app_installation_unlinked"



An installation of the Claude GitHub App was unlinked from the organization, so the organization's Claude Code features can no longer act on that GitHub account's repositories through it.

"github_token_import"



A user attempted to import a personal GitHub access token for use with Claude Code. The `result` field indicates the outcome of the import (imported, rejected, or failed).

"gitlab_configuration_created"



An organization admin created a self-managed GitLab configuration for syncing plugin marketplaces.

"gitlab_configuration_deleted"



An organization admin deleted a self-managed GitLab configuration.

"gitlab_configuration_updated"



An organization admin updated a self-managed GitLab configuration. Previous/new field pairs are recorded only for settings that changed in the update; secret credentials are never recorded, only whether they were replaced.

"group_created"



A group was created (RBAC admin or SCIM provisioning).

"group_deleted"



A group was deleted (RBAC admin or SCIM provisioning).

"group_list_viewed"



Admin viewed the list of RBAC groups.

"group_member_added"



One or more members were added to a group.

"group_member_addition_failed"



A request to add members to a group failed. Some of the requested members may have been added before the failure.

"group_member_list_viewed"



Admin viewed the members of an RBAC group.

"group_member_removal_failed"



A request to remove members from a group failed. Some of the requested members may have been removed before the failure.

"group_member_removed"



One or more members were removed from a group.

"group_project_shares_revoked"



An RBAC group's project shares in one organization were revoked in bulk.

"group_skill_shares_revoked"



An RBAC group's skill shares in one organization were revoked in bulk.

"group_updated"



A group was updated (RBAC admin or SCIM provisioning).

"group_viewed"



A group was viewed.

"group_visibility_updated"



An RBAC group's visibility policy was updated.

"inference_hooks_circuit_breaker_tripped"



The organization's Inference hooks circuit breaker tripped automatically: calls to the organization's Inference hooks endpoint crossed a failure threshold, and inspection was suspended to protect live traffic. While tripped, requests are handled according to the organization's failure handling setting — allowed through uninspected (fail open) or rejected (fail closed) — and no per-request Inference hooks activities are recorded. The tripped state persists until an administrator re-enables Inference hooks inspection (or explicitly resets the circuit breaker).

"inference_hooks_config_deleted"



Inference hooks configuration was removed for the organization.

"inference_hooks_config_updated"



Inference hooks configuration was created or updated for the organization.

"inference_hooks_request_denied"



Inference hooks inspection denied a request. The request was blocked and no model response was produced.

"inference_hooks_request_failed_open"



A request proceeded without Inference hooks inspection because a verdict could not be obtained and the organization's Inference hooks configuration is set to fail open.

"inference_hooks_signing_secret_generated"



A request signing secret was generated for the organization's Inference hooks configuration.

"integration_user_connected"



User connected to an integration.

"integration_user_disconnected"



User disconnected from an integration.

"invoice_collection_method_updated"



Invoice collection method was changed.

"lti_launch_initiated"



LTI launch was initiated.

"lti_launch_success"



LTI launch completed successfully.

"lti_platform_created"



Anthropic staff created an LTI platform integration on behalf of an org.

"lti_platform_updated"



Anthropic staff updated an LTI platform integration on behalf of an org.

"magic_link_login_failed"



A magic link sign-in attempt failed.

"magic_link_login_initiated"



A user requested a magic link sign-in email.

"magic_link_login_succeeded"



A user successfully signed in with a magic link email.

"managed_organization_setup_completed"



Managed (AWS Marketplace) organization setup was completed.

"marketplace_created"



Admin created an organization marketplace.

"marketplace_deleted"



Admin deleted an organization marketplace.

"marketplace_updated"



Admin updated an organization marketplace.

"marketplace_webhook_deleted"



Admin removed the GitHub push webhook for a marketplace.

"marketplace_webhook_provisioned"



Admin provisioned a GitHub push webhook for a marketplace.

"mcp_directory_server_published"



The organization published its approved MCP directory listing.

"mcp_server_created"



An MCP server was added to the organization.

"mcp_server_deleted"



An MCP server was removed from the organization.

"mcp_server_managed_auth_token_exchanged"



A user attempted to obtain an access token for an MCP server via enterprise managed authorization. This event reports the outcomes of attempted token exchanges. Repeated failures with the same cause may be reported once until the cause changes, and requests refused before a token exchange is attempted are not reported, except the "connector_scope_not_granted" and "identity_assertion_refused" failures described under error_type.

"mcp_server_managed_auth_updated"



An MCP server's enterprise managed authorization settings were set, changed, or cleared, including when they were supplied while the server was being added or edited. Fields without a "previous\_" prefix describe the settings after the change and are null when the server has no managed authorization settings afterwards; "previous\_" fields describe the settings before the change and are null when the server had none before (always the case for a newly added server).

"mcp_server_updated"



An MCP server's configuration was updated.

"mcp_tool_policy_updated"



The permission restriction for an MCP tool was set or cleared.

"org_analytics_api_capability_updated"



Organization analytics_api capability was enabled or disabled.

"org_bulk_delete_initiated"



Organization bulk deletion was initiated.

"org_capability_grant_added"



A capability grant was added to a workspace or role.

"org_capability_grant_removed"



A capability grant was removed from a workspace or role.

"org_claude_code_data_sharing_disabled"



Organization Claude Code data sharing was disabled.

"org_claude_code_data_sharing_enabled"



Organization Claude Code data sharing was enabled.

"org_claude_code_desktop_disabled"



Organization Claude Code Desktop was disabled.

"org_claude_code_desktop_enabled"



Organization Claude Code Desktop was enabled.

"org_claude_code_zero_data_retention_disabled"



A primary owner disabled zero data retention for Claude Code, so Claude Code content is retained according to the organization's data retention settings.

"org_compliance_api_settings_updated"



Organization compliance API settings were updated.

"org_connector_domain_guard_updated"



Enterprise admin changed whether connectors are restricted to verified domains.

"org_cowork_act_without_asking_mode_disabled"



The "Act without asking" mode in Cowork was disabled for the organization, so members can no longer let Claude act without asking for approval.

"org_cowork_act_without_asking_mode_enabled"



The "Act without asking" mode in Cowork was enabled for the organization, allowing members to let Claude act without asking for approval.

"org_cowork_agent_disabled"



Organization Cowork Agent was disabled.

"org_cowork_agent_enabled"



Organization Cowork Agent was enabled.

"org_cowork_auto_mode_disabled"



The "Auto" permission mode in Cowork was disabled for the organization, so members can no longer let Claude approve its own actions after a safety check.

"org_cowork_auto_mode_enabled"



The "Auto" permission mode in Cowork was enabled for the organization, allowing members to let Claude approve its own actions after a safety check.

"org_cowork_browser_pane_disabled"



The in-app browser in Cowork was disabled for the organization, so Claude can no longer open or use websites in a browser pane during members' Cowork sessions.

"org_cowork_browser_pane_enabled"



The in-app browser in Cowork was enabled for the organization, letting Claude open and use websites in a browser pane during members' Cowork sessions.

"org_cowork_disabled"



Organization cowork was disabled.

"org_cowork_enabled"



Organization cowork was enabled.

"org_cowork_mcp_always_allow_disabled"



The "Always allow" option for connector tools in Cowork was disabled for the organization, so each use of a connector tool that can make changes requires approval. Read-only connector tools are not affected by this setting.

"org_cowork_mcp_always_allow_enabled"



The "Always allow" option for connector tools in Cowork was enabled for the organization, letting members approve a connector tool that can make changes once and allow its later uses automatically. Read-only connector tools are not affected by this setting.

"org_cowork_otlp_settings_updated"



The organization's Cowork OpenTelemetry monitoring export settings were updated.

"org_cowork_remote_disabled"



Running Cowork in the cloud was disabled for the organization, so members can no longer run Cowork sessions in Anthropic-hosted remote environments.

"org_cowork_remote_enabled"



Running Cowork in the cloud was enabled for the organization, allowing members to run Cowork sessions in Anthropic-hosted remote environments.

"org_creation_blocked"



Organization creation was blocked.

"org_data_export_accessed"



Organization data export file was accessed/downloaded via signed URL.

"org_data_export_completed"



Organization data export was completed.

"org_data_export_started"



Organization data export was started.

"org_data_residency_updated"



The organization's inference data residency settings were updated.

"org_deleted_via_bulk"



Organization was deleted via bulk operation.

"org_deletion_requested"



Organization deletion was requested.

"org_directory_resync_completed"



Organization directory resync completed successfully.

"org_directory_resync_failed"



Organization directory resync failed.

"org_directory_resync_started"



Organization directory resync was started asynchronously.

"org_directory_sync_activated"



Organization directory sync was activated.

"org_directory_sync_add_initiated"



Organization directory sync setup was initiated.

"org_directory_sync_deleted"



Organization directory sync was deleted.

"org_discoverability_disabled"



Admin disabled organization discoverability.

"org_discoverability_enabled"



Admin enabled organization discoverability.

"org_discoverability_settings_updated"



Admin updated organization discoverability settings.

"org_domain_add_initiated"



Organization domain verification was initiated.

"org_domain_removed"



Organization domain was removed.

"org_domain_verified"



Organization domain was verified.

"org_external_key_created"



A CMEK external key config was created.

"org_external_key_deleted"



A CMEK external key config was deleted.

"org_external_key_updated"



A CMEK external key config was updated.

"org_external_key_validated"



A CMEK external key config was validated against the customer's KMS.

"org_hipaa_self_serve_enabled"



A primary owner click-accepted the BAA and enabled HIPAA protections for the organization via the self-serve flow.

"org_invite_link_disabled"



Organization invite link was disabled.

"org_invite_link_generated"



Organization invite link was generated.

"org_invite_link_regenerated"



Organization invite link was regenerated (previous link invalidated).

"org_invite_viewed"



An organization invite was viewed.

"org_invites_listed"



Organization invites were listed.

"org_ip_restriction_created"



Organization IP restriction was created.

"org_ip_restriction_deleted"



Organization IP restriction was deleted.

"org_ip_restriction_updated"



Organization IP restriction was updated.

"org_join_proposal_decided"



Approve or reject decision on a parent-org join proposal.

"org_join_request_approved"



Admin approved a join request.

"org_join_request_created"



User requested to join an organization.

"org_join_request_dismissed"



Admin dismissed a join request.

"org_join_request_instant_approved"



Join request was instantly approved.

"org_join_requests_bulk_dismissed"



Admin bulk-dismissed join requests.

"org_magic_link_second_factor_toggled"



Organization magic link second factor was toggled.

"org_member_invites_disabled"



Admin disabled member invites for the organization.

"org_member_invites_enabled"



Admin enabled member invites for the organization.

"org_members_exported"



Organization members list was exported as CSV.

"org_model_default_updated"



An organization or role default model setting was changed by an administrator.

"org_parent_join_proposal_created"



Organization parent join proposal was created.

"org_parent_search_performed"



Organization parent search was performed.

"org_sso_add_initiated"



Organization SSO setup was initiated.

"org_sso_connection_activated"



Organization SSO connection was activated.

"org_sso_connection_deactivated"



Organization SSO connection was deactivated.

"org_sso_connection_deleted"



Organization SSO connection was deleted.

"org_sso_group_role_mappings_updated"



Organization SSO group role mappings were updated.

"org_sso_provisioning_mode_changed"



Organization SSO provisioning mode was changed.

"org_sso_scim_welcome_email_toggled"



Organization SCIM-provisioned welcome email was toggled.

"org_sso_seat_tier_assignment_toggled"



Organization SSO seat tier assignment was toggled.

"org_sso_seat_tier_mappings_updated"



Organization SSO seat tier mappings were updated.

"org_sso_toggled"



Organization SSO was toggled on or off.

"org_sync_deleting_synchronized_files_started"



Organization started deleting synchronized files.

"org_sync_synchronized_files_deleted"



Organization synchronized files were deleted.

"org_taint_added"



A taint was added to an organization.

"org_taint_removed"



A taint was removed from an organization.

"org_user_deleted"



User was removed from organization.

"org_user_invite_accepted"



Organization user invite was accepted.

"org_user_invite_deleted"



Organization user invite was deleted.

"org_user_invite_re_sent"



Organization user invite was re-sent.

"org_user_invite_rejected"



Organization user invite was rejected.

"org_user_invite_sent"



Organization user invite was sent.

"org_user_left"



User removed themselves from organization.

"org_user_shares_retained"



A member left or was removed from the organization while projects, skills, plugins, or chats they had shared were still shared, and those shares were kept.

"org_user_trusted_devices_revoked"



An organization admin revoked a member's trusted devices and signed the member out of all active sessions.

"org_user_viewed"



An organization user was viewed.

"org_users_listed"



Organization users were listed.

"org_work_across_apps_disabled"



The organization's "Let Claude work across apps" setting was turned off.

"org_work_across_apps_enabled"



The organization's "Let Claude work across apps" setting was turned on.

"organization_address_updated"



The organization's billing or shipping address was updated.

"organization_icon_deleted"



Organization's custom icon deleted.

"organization_icon_updated"



Organization's custom icon uploaded or replaced.

"owned_projects_access_restored"



Access to owned projects was restored.

"payment_method_updated"



The organization's default payment method was updated.

"pending_share_created"



A pending share of a project or skill was created for an email address that is not yet an organization member.

"pending_share_revoked"



A pending share of a project or skill was revoked before the invitee joined the organization.

"phone_code_sent"



User requested a phone verification code.

"phone_code_verified"



User successfully verified their phone code.

"platform_agent_archived"



An agent was archived on the API platform.

"platform_agent_created"



An agent was created on the API platform.

"platform_agent_deleted"



An agent was deleted from the API platform.

"platform_agent_deployment_archived"



An agent deployment was archived on the API platform.

"platform_agent_deployment_created"



An agent deployment was created on the API platform.

"platform_agent_deployment_deleted"



An agent deployment was deleted from the API platform.

"platform_agent_deployment_paused"



An agent deployment was paused on the API platform.

"platform_agent_deployment_run_triggered"



An agent deployment was run on demand on the API platform.

"platform_agent_deployment_unpaused"



An agent deployment was resumed on the API platform.

"platform_agent_deployment_updated"



An agent deployment was updated on the API platform.

"platform_agent_session_archived"



An agent session was archived on the API platform.

"platform_agent_session_created"



An agent session was created on the API platform.

"platform_agent_session_deleted"



An agent session was deleted from the API platform.

"platform_agent_session_resource_added"



A resource was attached to an agent session.

"platform_agent_session_resource_deleted"



A resource attached to an agent session was removed.

"platform_agent_session_resource_updated"



A resource attached to an agent session was updated.

"platform_agent_session_thread_archived"



A thread within an agent session was archived.

"platform_agent_session_updated"



An agent session was updated on the API platform.

"platform_agent_updated"



An agent was updated on the API platform.

"platform_api_key_created"



An API key was created.

"platform_api_key_updated"



An API key was updated.

"platform_app_attest_authentication"



An attested mobile device attempted to exchange an Apple App Attest assertion for Anthropic API credentials.

"platform_billing_upgraded_to_prepaid"



The organization's API billing was upgraded to the prepaid plan.

"platform_clearance_workspace_program_request_cleared"



A workspace's clearance program assignment was removed.

"platform_clearance_workspace_program_request_set"



A workspace's clearance program assignment was created or updated.

"platform_cost_report_viewed"



The cost report was viewed.

"platform_dream_archived"



A Dream (asynchronous memory-consolidation job) was archived.

"platform_dream_cancelled"



A Dream (asynchronous memory-consolidation job) was cancelled before it completed.

"platform_dream_created"



A Dream (asynchronous memory-consolidation job) was created.

"platform_federated_authentication"



A federated workload identity attempted to exchange an OIDC token for Anthropic API credentials.

"platform_federation_issuer_archived"



An OIDC federation issuer was archived.

"platform_federation_issuer_created"



An OIDC federation issuer was created, registering an external identity provider that federation rules can trust for workload authentication.

"platform_federation_issuer_updated"



An OIDC federation issuer was updated.

"platform_federation_rule_archived"



An OIDC federation rule was archived.

"platform_federation_rule_created"



An OIDC federation rule was created, allowing tokens from a federation issuer to authenticate as a service account or user. Rules may additionally match on token claims or a condition expression, which are not included in this event.

"platform_federation_rule_updated"



An OIDC federation rule was updated.

"platform_federation_rule_workspace_added"



A federation rule was enabled for a workspace.

"platform_federation_rule_workspace_removed"



A federation rule was disabled for a workspace.

"platform_file_content_downloaded"



Activity logged when file content is downloaded via GET /v1/files/{file_id}/content.

"platform_file_deleted"



Activity logged when a file is deleted via DELETE /v1/files/{file_id}.

"platform_file_uploaded"



Activity logged when a file is uploaded via POST /v1/files.

"platform_memory_created"



An agent memory document was created.

"platform_memory_deleted"



An agent memory document was deleted.

"platform_memory_store_archived"



An agent memory store was archived. Archived stores reject new memory writes and cannot be attached to new sessions; deletion and redaction remain permitted for privacy scrubbing.

"platform_memory_store_created"



An agent memory store was created.

"platform_memory_store_deleted"



An agent memory store was deleted. Memory content removal may complete asynchronously for very large stores.

"platform_memory_store_updated"



An agent memory store's name, description, or metadata was updated.

"platform_memory_updated"



An agent memory document's content or path was updated.

"platform_memory_version_redacted"



A historical version of an agent memory document was redacted. Redaction scrubs the stored content of a specific version while preserving the version's existence in the history.

"platform_oauth_app_created"



An OAuth app was created.

"platform_oauth_app_revoked"



An OAuth app was revoked.

"platform_oauth_app_updated"



An OAuth app was updated.

"platform_plugin_directory_submission_created"



A plugin directory submission was created on the API platform. A plugin directory submission is a request to list a plugin in the public plugin directory.

"platform_plugin_directory_submission_deleted"



A plugin directory submission was deleted on the API platform.

"platform_plugin_directory_submission_updated"



A plugin directory submission was updated on the API platform.

"platform_service_account_archived"



A service account was archived.

"platform_service_account_created"



A service account was created.

"platform_service_account_updated"



A service account was updated.

"platform_service_account_workspace_member_added"



A service account was added as a member of a workspace.

"platform_service_account_workspace_member_removed"



A service account was removed from a workspace.

"platform_service_account_workspace_member_updated"



A service account's workspace membership role was updated.

"platform_signing_key_created"



Activity logged when a new request-signing key is registered for the org.

"platform_signing_key_deleted"



Activity logged when a signing key is permanently deleted.

"platform_signing_key_rotated"



Activity logged when an in-memory signing key is rotated.

"platform_skill_version_content_downloaded"



The content of a skill version was downloaded through the Skills API.

"platform_skill_version_created"



Activity logged when a skill version is created via POST /v1/skills/{skill_id}/versions.

"platform_skill_version_deleted"



Activity logged when a skill version is deleted via DELETE /v1/skills/{skill_id}/versions/{version}.

"platform_spend_limit_alert_emails_updated"



Spend limit alert email addresses and role targets were updated for an org.

"platform_spend_limit_created"



An org-level fixed-dollar spend limit was created.

"platform_spend_limit_deleted"



An org-level spend limit was removed.

"platform_spend_limit_updated"



An org-level spend limit snooze/ignore state was changed.

"platform_usage_report_claude_code_viewed"



The Claude Code usage report was viewed.

"platform_usage_report_messages_viewed"



The messages usage report was viewed.

"platform_workspace_archived"



A workspace was archived.

"platform_workspace_created"



A workspace was created.

"platform_workspace_inference_data_retention_disabled"



The zero data retention override was disabled for a workspace.

"platform_workspace_inference_data_retention_enabled"



The zero data retention override was enabled for a workspace.

"platform_workspace_member_added"



A member was added to a workspace.

"platform_workspace_member_removed"



A member was removed from a workspace.

"platform_workspace_member_updated"



A workspace member was updated.

"platform_workspace_member_viewed"



A workspace member was viewed.

"platform_workspace_members_listed"



Workspace members were listed.

"platform_workspace_rate_limit_deleted"



A workspace rate limit was deleted.

"platform_workspace_rate_limit_updated"



A workspace rate limit was created or updated.

"platform_workspace_updated"



A workspace was updated.

"plugin_installation_preference_updated"



An org admin changed the installation preference for a plugin.

"prepaid_auto_recharge_disabled"



Auto-recharge was disabled for API prepaid org.

"prepaid_auto_recharge_updated"



Auto-recharge settings were updated for API prepaid org.

"prepaid_extra_usage_auto_reload_disabled"



Prepaid usage credit auto-reload was disabled.

"prepaid_extra_usage_auto_reload_enabled"



Prepaid usage credit auto-reload was enabled.

"prepaid_extra_usage_auto_reload_settings_updated"



Prepaid usage credit auto-reload settings were updated.

"primary_owner_transferred"



Primary owner role was transferred to another org member.

"rbac_role_assigned"



Admin assigned an RBAC custom role to a principal.

"rbac_role_created"



Admin created an RBAC custom role.

"rbac_role_deleted"



Admin deleted an RBAC custom role.



"rbac_role_grant_updated"



Admin requested a capability grant for an RBAC custom role, or removed it.

Records the admin's change to the role. Whether the grant is currently in effect on the role is reported separately.



"rbac_role_permission_added"



Admin added a permission to an RBAC custom role.

Emitted once per requested permission, including permissions the role already had, so a retried request still produces a complete audit record.



"rbac_role_permission_removed"



Admin removed a permission from an RBAC custom role.

Emitted once per requested permission, including permissions the role already lacked, so a retried request still produces a complete audit record.

"rbac_role_unassigned"



Admin unassigned an RBAC custom role from a principal.

"rbac_role_updated"



Admin updated an RBAC custom role.

"role_assignment_granted"



Role assignment was granted.

"role_assignment_revoked"



Role assignment was revoked.

"scim_user_created"



A SCIM user was provisioned.

"scim_user_deleted"



A SCIM user was deleted.

"scim_user_updated"



A SCIM user was updated.

"scoped_api_key_deleted"



A scoped API key was deleted.

"scoped_api_key_updated"



A scoped API key was renamed or its activation state changed.

"seat_tier_changes_cancelled"



Scheduled seat tier downgrades were cancelled.

"seat_tiers_purchased"



Seat tiers were purchased or upgraded on a subscription.

"service_created"



Activity logged when an org service is explicitly created.

"service_deleted"



Activity logged when an org service is deleted.

"service_key_created"



Activity logged when a new org service key is created.

"service_key_revoked"



Activity logged when an org service key is revoked.

"session_revoked"



User revoked a specific session.

"session_share_accessed"



Session share was accessed.

"session_share_created"



Session share was created.

"session_share_revoked"



Session share was revoked.

"slack_workspace_claim_revoked"



A Slack workspace or Enterprise Grid organization was disconnected from the organization for Claude in Slack.

"slack_workspace_claimed"



A Slack workspace or Enterprise Grid organization was connected to the organization for Claude in Slack.

"social_login_succeeded"



A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

"sso_login_failed"



An SSO sign-in attempt failed.

"sso_login_initiated"



A user started an SSO sign-in flow.

"sso_login_succeeded"



A user successfully signed in with SSO.

"sso_second_factor_magic_link"



SSO second factor magic link was used.

"step_up_authentication_failed"



An additional identity check failed.

"step_up_authentication_succeeded"



The user completed an additional identity check to confirm a sensitive action.

"step_up_credential_enrolled"



A user enrolled a passkey for confirming sensitive actions on their account.

"subscription_cancellation_scheduled"



Subscription cancellation was scheduled at end of billing period.

"subscription_quantity_updated"



Contracted subscription seat quantity was updated.

"subscription_renewed"



A cancelled subscription was renewed.

"subscription_resumed"



A scheduled subscription cancellation was reversed.

"subscription_started"



A new subscription was created (Team or Enterprise).

"subscription_upgraded"



Subscription plan was upgraded (e.g. Team to Enterprise).

"trusted_device_credential_rotated"



The identity-verification credential of a trusted device was rotated to a new key.

"trusted_device_enrolled"



A device was enrolled as a trusted device for the user's account. Trusted devices can be used to confirm the user's identity for sensitive actions.

"trusted_device_revoked"



A trusted device was removed from the user's account.

"tunnel_archived"



An MCP tunnel was archived.

"tunnel_certificate_added"



An inner-TLS CA certificate was added to a tunnel.

"tunnel_certificate_revoked"



An inner-TLS CA certificate was revoked from a tunnel.

"tunnel_created"



An MCP tunnel was created.

"tunnel_token_minted"



An OAuth bearer token for the tunnel management API was minted.

"tunnel_token_revealed"



The Cloudflare connector secret for a tunnel was revealed to the caller.

"tunnel_token_revoked"



An OAuth bearer token for the tunnel management API was revoked.



"tunnel_token_rotated"



The Cloudflare connector secret for a tunnel was rotated.

`tunnel_token_id` is the id of the *newly-issued* token. The previous token is invalidated by the rotation and its id is not recorded here.

"user_consent_recorded"



User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

"user_consent_revoked"



User revoked a previously granted consent for a specific entity.

"user_logged_out"



A user signed out of one or all sessions.

"verification_evidence_submitted"



Verification evidence was submitted for an organization's verification.

"verification_program_application_created"



An organization applied to a verification program.

"workspace_member_spend_limit_created"



A per-member or workspace-default Claude Code spend limit was created.

"workspace_member_spend_limit_deleted"



A per-member or workspace-default Claude Code spend limit was deleted.

"workspace_member_spend_limit_updated"



A per-member Claude Code spend limit amount was updated.

"workspace_spend_limit_alert_emails_updated"



Spend limit alert email recipients were updated for a workspace.

"workspace_spend_limit_created"



A workspace-level API spend limit was created.

"workspace_spend_limit_deleted"



A workspace-level API spend limit was deleted.

actor_ids: optional array of string



Filter activities by actor IDs (currently only `user_...` IDs are supported). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

after_id: optional string



Pagination cursor for retrieving the next page of results. To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

before_id: optional string



Pagination cursor for retrieving the previous page of results. To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



created_at: optional object{ gt, gte, lt, lte }





gt: optional string



Filter activities created after this time (RFC 3339 format)

formatdate-time



gte: optional string



Filter activities created at or after this time (RFC 3339 format)

formatdate-time



lt: optional string



Filter activities created before this time (RFC 3339 format)

formatdate-time



lte: optional string



Filter activities created at or before this time (RFC 3339 format)

formatdate-time



exclude_activity_types: optional array of "abuse_decision_received" or "account_deleted" or "admin_api_key_created" or 511 more



Exclude activities of these types. Cannot be combined with `activity_types[]`.

One of the following:

"abuse_decision_received"



An external anti-abuse service reported a consequential decision about a sign-in or sign-up attempt.

"account_deleted"



User-initiated self-service account deletion.

"admin_api_key_created"



An admin API key was created.

"admin_api_key_deleted"



An admin API key was deleted.

"admin_api_key_updated"



An admin API key was updated (renamed or activated/deactivated).

"admin_connector_request_resolved"



Admin approved or dismissed pending member requests to enable an MCP connector.

"admin_request_created"



Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).

"admin_setup_checklist_step_delegated"



A step of the Claude Enterprise admin setup checklist was delegated to a teammate — an organization member, or an email address that has not joined the organization yet — replacing any earlier delegation of that step.

"admin_setup_checklist_step_delegation_cancelled"



The delegation of a Claude Enterprise admin setup checklist step was cancelled.

"age_verified"



User age was verified.

"anonymous_mobile_login_attempted"



Anonymous mobile login was attempted.

"api_key_created"



Activity logged when a new API key is created.

"audit_log_export_accessed"



Audit log export file was accessed/downloaded via signed URL.

"audit_log_export_started"



Audit log export was initiated.

"billing_emails_updated"



The organization's billing email recipients were updated.

"ccr_agent_created"



A Claude Code agent was created.

"ccr_agent_deleted"



A Claude Code agent was deleted.

"ccr_agent_proxy_anthropic_oidc_token_exchanged"



The Claude Code agent proxy exchanged a minted identity token for short-lived credentials in the organization's own cloud. Recorded for exchange targets only (such as "aws" and "gcp"; the "direct" target has no exchange step). One event is recorded per exchange call; a request served from the proxy's exchanged-credential cache does not exchange again and is not recorded here. Per-request detail for traffic the credentials were injected into is available in the agent proxy network events.

"ccr_agent_proxy_anthropic_oidc_token_minted"



The Claude Code agent proxy minted a short-lived identity token for an anthropic_oidc credential. One event is recorded per fresh token issuance; a request served from the proxy's short-lived token cache does not mint a new token and is not recorded here. Per-request detail for traffic the credential was injected into is available in the agent proxy network events.

"ccr_agent_proxy_credential_created"



A Claude Code agent proxy credential was created. Credentials hold the secrets the agent proxy injects into requests Claude Code sessions send to approved external services; each credential belongs to an agent proxy profile. Audit events carry only credential names and settings, never the secret material itself.

"ccr_agent_proxy_credential_deleted"



A Claude Code agent proxy credential was deleted. Its secret material was removed and can no longer be sent to any host.

"ccr_agent_proxy_credential_rotated"



A Claude Code agent proxy credential's secret material was replaced. The replacement keeps the same name, profile, and allowed hosts under a new credential identifier, and everything that referenced the old credential now uses the replacement.

"ccr_agent_proxy_credential_updated"



A Claude Code agent proxy credential's settings were updated. Only the display name and the allowed host patterns can be updated; the secret material can only be replaced through a rotation.

"ccr_agent_proxy_destination_deleted"



An agent proxy destination was deleted.

"ccr_agent_proxy_network_events_listed"



A Claude Code network activity export was accessed for the given hour.

"ccr_agent_proxy_profile_bound"



A Claude Code agent proxy profile was bound to a scope, applying its policy to Claude Code sessions in that scope.

"ccr_agent_proxy_profile_created"



A Claude Code agent proxy profile was created. Agent proxy profiles are named, reusable bundles of access policy that administrators bind to parts of the organization.

"ccr_agent_proxy_profile_deleted"



A Claude Code agent proxy profile was deleted, removing its policy from everything it was bound to.

"ccr_agent_proxy_profile_unbound"



A Claude Code agent proxy profile was unbound from a scope, removing its policy from Claude Code sessions in that scope.

"ccr_agent_proxy_profile_updated"



A Claude Code agent proxy profile's configuration was updated.

"ccr_agent_proxy_provisioning_credential_rejected"



An organization owner rejected a credential that a teammate submitted via an agent proxy provisioning link: the credential and its disabled rule were deleted and the link was revoked. The actor is the owner; the submitter is recorded for attribution.

"ccr_agent_proxy_provisioning_link_enabled"



An organization owner enabled a credential that a teammate submitted via an agent proxy provisioning link: the disabled rule created at submission was switched to enforce, so the credential now takes traffic. The actor is the owner; the submitter is the actor on the prior ccr_agent_proxy_provisioning_link_submitted event.

"ccr_agent_proxy_provisioning_link_generated"



An organization owner generated a one-time agent proxy credential provisioning link so a teammate can submit a credential into the target agent proxy profile without holding the owner role.

"ccr_agent_proxy_provisioning_link_revoked"



An organization owner revoked an unfilled agent proxy provisioning link.

"ccr_agent_proxy_provisioning_link_submitted"



A teammate submitted a credential via an agent proxy provisioning link. The credential and a disabled rule are created; the credential takes traffic only after an organization owner enables the submitted credential. This event records the link-mediated lifecycle; the credential itself additionally emits ccr_agent_proxy_credential_created.

"ccr_agent_proxy_rule_created"



An agent proxy rule was created. A rule decides what happens to a session's outbound requests that match it.

"ccr_agent_proxy_rule_deleted"



An agent proxy rule was deleted.

"ccr_agent_proxy_rule_updated"



An agent proxy rule was updated. An update replaces everything the rule matches and does, so the host name patterns here are the rule's complete set after the update.

"ccr_agent_slack_access_scope_created"



A Claude Code agent was granted access to read or write in an additional Slack channel beyond the one it is assigned to.

"ccr_agent_slack_access_scope_deleted"



A Claude Code agent's access to an additional Slack channel was revoked.

"ccr_agent_slack_binding_created"



A Claude Code agent was assigned to a Slack channel or workspace as its dedicated agent.

"ccr_agent_slack_binding_deleted"



A Claude Code agent's assignment to a Slack channel or workspace was removed.

"ccr_agent_updated"



A Claude Code agent's configuration was updated. Also emitted with updated_fields \["is_virtual"\] alone when an auto-provisioned agent is promoted to a configured one, whether by an update request targeting it or by binding an agent proxy profile to it.

"ccr_channel_manager_added"



An org owner/admin assigned an organization member to manage the Claude-in-Slack configuration of one Slack channel.

"ccr_channel_manager_removed"



An org owner/admin removed an organization member's assignment to manage the Claude-in-Slack configuration of one Slack channel.

"ccr_role_channel_assignment_deleted"



CcrRoleChannelAssignmentDeleted is emitted when an org owner/admin removes an RBAC role's channel assignment row (the role reverts to granting zero channels).

"ccr_role_channel_assignment_updated"



CcrRoleChannelAssignmentUpdated is emitted when an org owner/admin sets or replaces the list of Slack channels an RBAC role's holders may configure via the delegated Claude-in-Slack channel-manage surface.

"ccr_session_created"



A Claude Code session was created. A session is one coding interaction with Claude.

"ccr_session_deleted"



A Claude Code session was deleted.

"ccr_session_updated"



A Claude Code session's settings were updated.

"ccr_slack_channel_joined"



Claude's Slack app joined a public Slack channel at an organization administrator's request.

"claude_artifact_access_failed"



An attempt to access an artifact failed.

"claude_artifact_commented"



Comment activity on a published artifact: a comment was added, a thread's resolved state was changed, or a thread was deleted. The actor is the user who performed the action; the comment text itself is stored with the artifact and is not part of this record.

"claude_artifact_comments_viewed"



An artifact's comments were viewed.

"claude_artifact_created"



An artifact was created.

"claude_artifact_duplicated"



A user duplicated an artifact they could view into a new artifact that they own. The actor is the user who created the copy; the source artifact is not modified.

"claude_artifact_external_sharing_permission_updated"



An organization admin allowed one artifact to be shared outside the organization by link while the organization-wide external sharing setting was off, or revoked that permission.

"claude_artifact_invite_accepted"



Someone outside the organization signed in with a verified account for the invited address and accepted an invitation to an artifact, and can now open it; recorded in the artifact owner's organization. The person who accepted is identified by `invitee_email` and `invitee_user_id`.

"claude_artifact_invite_created"



A member invited (or re-invited) an email address outside the organization to an artifact; recorded in the artifact owner's organization with the inviting member as the actor.

"claude_artifact_invite_revoked"



A member withdrew an invitation to an artifact for someone outside the organization, removing any access that invitation had granted; recorded in the artifact owner's organization with that member as the actor.

"claude_artifact_invite_role_updated"



A member changed the access level of an email invitation to an artifact for someone outside the organization, whether the invitation was still pending or had been accepted; recorded in the artifact owner's organization with that member as the actor.

"claude_artifact_published"



A new version of an artifact was published — for an artifact created in a chat this is the action that made it publicly viewable; for an artifact created outside a chat it is recorded when the artifact is saved, including saves of private artifacts, except that automatic saves made while a person keeps editing may be recorded periodically for that person rather than once per save; changes to who can access the artifact are recorded separately as claude_artifact_sharing_updated.

"claude_artifact_sharing_updated"



An artifact's sharing settings were updated.

"claude_artifact_viewed"



An artifact was viewed.

"claude_chat_access_failed"



A user was denied access to a Claude.ai chat conversation.

"claude_chat_created"



User created a chat.

"claude_chat_deleted"



A user deleted a Claude.ai chat conversation.

"claude_chat_deletion_failed"



A request to delete a Claude.ai chat conversation failed.

"claude_chat_settings_updated"



User updated the settings for a conversation.

"claude_chat_snapshot_created"



User created/shared a chat snapshot.

"claude_chat_snapshot_deleted"



User deleted/unshared a chat snapshot.

"claude_chat_snapshot_viewed"



User viewed a chat snapshot (authenticated or public/unauthenticated).

"claude_chat_sync_source_created"



A sync source was connected for syncing external content into Claude chats.

"claude_chat_sync_source_deleted"



A sync source was disconnected from Claude chats.

"claude_chat_sync_source_updated"



A Claude chat sync source's configuration was updated.

"claude_chat_updated"



User updated the chat metadata (e.g name, model).

"claude_chat_viewed"



A user viewed a Claude.ai chat conversation.

"claude_code_credential_revoked"



A Claude Code credential (runner pool key, runner token, or session token) was revoked. The credential itself is never recorded.

"claude_code_review_config_updated"



Claude Code Review configuration was enabled/disabled for an org.

"claude_code_review_repository_added"



A repository was added to org-level Claude Code Review configuration.

"claude_code_review_repository_removed"



A repository was removed from org-level Claude Code Review configuration.

"claude_code_review_repository_updated"



A Claude Code Review repository configuration was updated.

"claude_code_runner_deleted"



A self-hosted runner was forcibly removed from its pool. Sessions assigned to the runner were returned to the pool queue, unless a session had already been requeued repeatedly, in which case it was marked stuck instead of being requeued again.

"claude_code_runner_pool_created"



A self-hosted runner pool for Claude Code was created.

"claude_code_runner_pool_deleted"



A self-hosted runner pool was deleted.

"claude_code_runner_pool_secret_minted"



A registration key for a self-hosted runner pool was minted. Runners present this key to join the pool. The key itself is never recorded.

"claude_code_runner_pool_session_queue_updated"



An admin changed a session's position in its self-hosted runner pool's queue: requeued it onto a different runner, dismissed it from the queue, or re-admitted it for another runner provisioning attempt.

"claude_code_runner_pool_updated"



A self-hosted runner pool's settings were updated.

"claude_code_security_center_config_updated"



Claude Code Security Center scanning was enabled/disabled for an org.

"claude_code_security_scan_cancelled"



In-flight Claude Code Security scans were cancelled for a project.

"claude_code_security_scan_created"



A Claude Code Security scan was started.

"claude_code_security_scan_project_member_updated"



A person's access to a Claude Code Security scan project was granted, changed, or revoked.

"claude_code_security_scan_project_updated"



A Claude Code Security scan project was archived, unarchived, created, or migrated to a new product experience.

"claude_code_security_scan_project_visibility_updated"



A Claude Code Security scan project was shared with the organization or made private.

"claude_code_security_scan_run_updated"



A single Claude Code Security scan run was archived, unarchived, or resumed after a billing pause.

"claude_code_security_scan_schedule_deleted"



A recurring scan schedule was deleted for a Claude Code Security project.

"claude_code_security_scan_schedule_updated"



A recurring scan schedule was set or replaced for a Claude Code Security project.

"claude_code_security_vulnerability_deleted"



A Claude Code Security vulnerability finding was permanently deleted.

"claude_code_security_vulnerability_fix_session_created"



A Claude Code remediation session was created for a Claude Code Security vulnerability finding.

"claude_code_security_vulnerability_updated"



A Claude Code Security vulnerability finding was dismissed, restored, marked fixed, or reopened.

"claude_code_security_webhook_created"



A Claude Code Security outbound webhook was created.

"claude_code_security_webhook_deleted"



A Claude Code Security outbound webhook was deleted.

"claude_code_security_webhook_secret_updated"



The HMAC signing secret for a Claude Code Security webhook was rotated.

"claude_code_security_webhook_updated"



A Claude Code Security outbound webhook was updated.

"claude_code_team_memory_acl_updated"



An RBAC group was added to or removed from the Claude Code team-memory ACL.

"claude_code_team_memory_updated"



Claude Code team memory shared with the organization was updated.

"claude_code_team_onboarding_guide_updated"



A Claude Code team onboarding guide was created, updated, or deleted.

"claude_code_user_marketplaces_updated"



A user's Claude Code plugin marketplace selections were updated on Anthropic servers.

"claude_code_user_memory_updated"



A user's synced private Claude Code memory was updated or deleted on Anthropic servers.

"claude_code_user_plugins_updated"



A user's Claude Code plugin selections — which plugins are installed and enabled — were updated on Anthropic servers.

"claude_code_user_settings_updated"



A user's synced Claude Code settings were updated or deleted on Anthropic servers.

"claude_command_created"



Command was created.

"claude_command_deleted"



Command was deleted.

"claude_command_replaced"



Command was replaced.

"claude_enterprise_upgrade_credit_updated"



An organization admin cancelled, or turned back on, the monthly usage credit the organization receives for upgrading from the Team plan to the Enterprise plan, together with the recurring monthly charge that accompanies it.

"claude_file_access_failed"



A user was denied access to a file in Claude.ai.

"claude_file_deleted"



A file was deleted.

"claude_file_exported"



A file was exported from Claude to an external storage destination.

"claude_file_uploaded"



A file was uploaded.

"claude_file_viewed"



A user viewed a file in Claude.ai.

"claude_gdrive_integration_created"



A Google Drive integration was enabled for the organization.

"claude_gdrive_integration_deleted"



A Google Drive integration was disabled for the organization.

"claude_gdrive_integration_updated"



A Google Drive integration's configuration was updated.

"claude_github_integration_created"



A GitHub integration was enabled for the organization.

"claude_github_integration_deleted"



A GitHub integration was disabled for the organization.

"claude_github_integration_updated"



A GitHub integration's configuration was updated.

"claude_organization_settings_updated"



Organization settings were updated.

"claude_plugin_archive_accessed"



A version archive of a member-owned plugin, containing that member's own files, was downloaded.

"claude_plugin_created"



Plugin was created.

"claude_plugin_deleted"



Plugin was deleted.

"claude_plugin_disabled"



User disabled a plugin for their account.

"claude_plugin_enabled"



User enabled a plugin for their account.

"claude_plugin_replaced"



Plugin was replaced.

"claude_plugin_security_scan_completed"



A security scan of a plugin completed and produced a verdict.

"claude_plugin_updated"



Plugin was updated.

"claude_project_archived"



A Claude project was archived.

"claude_project_created"



A Claude project was created.

"claude_project_deleted"



A Claude project was deleted.

"claude_project_document_access_failed"



An attempt to access a document in a Claude project failed.

"claude_project_document_bulk_deletion_audit_truncated"



A bulk request to delete documents from a Claude project failed with more documents requested than were individually recorded in the audit log.

"claude_project_document_deleted"



A document was deleted from a Claude project.

"claude_project_document_deletion_failed"



A request to delete a document from a Claude project failed.

"claude_project_document_updated"



The content of a document in a Claude project was replaced in place.

"claude_project_document_uploaded"



A document was uploaded to a Claude project.

"claude_project_document_viewed"



A document in a Claude project was viewed.

"claude_project_file_access_failed"



An attempt to access a file in a Claude project failed.

"claude_project_file_bulk_deletion_audit_truncated"



A bulk request to delete files from a Claude project failed with more files requested than were individually recorded in the audit log.

"claude_project_file_deleted"



A file was deleted from a Claude project.

"claude_project_file_deletion_failed"



A request to delete a file from a Claude project failed.

"claude_project_file_uploaded"



A file was uploaded to a Claude project.

"claude_project_reported"



A Claude project was reported.

"claude_project_sharing_updated"



A Claude project's sharing settings were updated.

"claude_project_sync_source_created"



A sync source was connected to a Claude project's knowledge base.

"claude_project_sync_source_deleted"



A sync source was disconnected from a Claude project's knowledge base.

"claude_project_sync_source_updated"



A Claude project sync source's configuration was updated.

"claude_project_viewed"



A Claude project was viewed.

"claude_published_artifact_deleted"



A published artifact was deleted or unpublished — by its creator, by an organization admin, or by Anthropic (for example, when it was removed for a policy violation).

"claude_pubsec_identity_configured"



SAML IdP configuration updated for a public sector organization.

"claude_skill_created"



Skill was created.

"claude_skill_deleted"



Skill was deleted.

"claude_skill_disabled"



User disabled a skill for their account.

"claude_skill_enabled"



User enabled a skill for their account.

"claude_skill_replaced"



Skill was replaced.

"claude_skill_security_scan_completed"



A security scan of a skill completed and produced a verdict.

"claude_user_role_updated"



A user's role within the organization was changed, or the user was added to or removed from the organization.

"claude_user_seat_tier_updated"



An organization member's seat tier was changed. A null `previous_seat_tier` means the member previously had no seat assigned; a null `current_seat_tier` means the seat was removed.

"claude_user_settings_updated"



User updated their personal settings.

"cli_plugin_exec_policy_updated"



Admin set or cleared the per-op permission ceiling for a plugin CLI.

"compliance_api_accessed"



Logging event auto-generated for each compliance API request.

"cowork_session_updated"



A Cowork session was updated.

"design_project_artifact_published"



A Claude Design project's content was published as a claude.ai artifact, making a snapshot of one of its files viewable outside the project's sharing settings.

"design_project_created"



A Claude Design project was created.

"design_project_deleted"



A Claude Design project was deleted.

"design_project_member_added"



A member was granted access to a Claude Design project.

"design_project_member_removed"



A member's access to a Claude Design project was revoked.

"design_project_member_role_updated"



A Claude Design project member's role was changed.

"design_project_published"



A Claude Design template or design system was published, making it discoverable by everyone in its organization.

"design_project_sharing_updated"



A Claude Design project's link-sharing settings were changed — who the project's link works for, and what people opening it through the link may do. Access granted to individual members is reported separately (see design_project_member_added).

"design_project_unpublished"



A Claude Design template or design system was unpublished, removing it from its organization's shared gallery.

"design_project_updated"



A Claude Design project's metadata was updated.

"design_project_version_restored"



A Claude Design project's working tree was rolled back to a previously saved version, replacing its current files with that version's files.



"design_project_viewed"



A Claude Design project's content was read. The surface field records which kind of read — a project open, a full-content read, a single-file read, a saved-version read, or an export request. The actor is the reader.

This activity type is retired: project content reads are no longer recorded. Events of this type may still appear in feeds for reads that occurred while it was active.

"desktop_extension_allowlisted"



A desktop extension was added to an org's allowlist.

"desktop_extension_blocklisted"



A desktop extension was added to the global blocklist.

"desktop_extension_deleted"



A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.

"desktop_extension_removed_from_allowlist"



A desktop extension was removed from an org's allowlist.

"desktop_extension_unblocked"



A desktop extension was removed from the global blocklist.

"desktop_extension_uploaded"



A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.

"desktop_extension_version_uploaded"



A new version of an existing org-owned desktop extension was uploaded.

"domain_claim_initiated"



Domain capture claim initiated over personal accounts on verified domains.

"end_user_invite_requested"



Non-admin member submitted an invite request for a new org member.

"extra_usage_billing_enabled"



Usage credit billing was enabled for an organization.

"extra_usage_credit_granted"



A promotional usage credit grant was claimed.

"extra_usage_spend_limit_created"



Usage credit spend limit was created.

"extra_usage_spend_limit_deleted"



Usage credit spend limit was deleted.

"extra_usage_spend_limit_increase_request_approved"



A usage credit spend limit increase request was approved.

"extra_usage_spend_limit_increase_request_denied"



A usage credit spend limit increase request was denied.

"extra_usage_spend_limit_updated"



Usage credit spend limit was updated.

"ghe_configuration_created"



Admin created a GHE configuration.

"ghe_configuration_deleted"



Admin deleted a GHE configuration.

"ghe_configuration_updated"



Admin updated a GHE configuration. Previous/new field pairs are recorded only for settings that changed in the update; secret credentials are never recorded, only whether they were replaced.

"ghe_user_connected"



User connected to a GHE instance.

"ghe_user_disconnected"



User disconnected from a GHE instance.

"ghe_webhook_signature_invalid"



Webhook signature validation failed.

"github_app_installation_linked"



An installation of the Claude GitHub App (a GitHub organization or user account where the App is installed) was linked to the organization, letting the organization's Claude Code features act on that GitHub account's repositories.

"github_app_installation_unlinked"



An installation of the Claude GitHub App was unlinked from the organization, so the organization's Claude Code features can no longer act on that GitHub account's repositories through it.

"github_token_import"



A user attempted to import a personal GitHub access token for use with Claude Code. The `result` field indicates the outcome of the import (imported, rejected, or failed).

"gitlab_configuration_created"



An organization admin created a self-managed GitLab configuration for syncing plugin marketplaces.

"gitlab_configuration_deleted"



An organization admin deleted a self-managed GitLab configuration.

"gitlab_configuration_updated"



An organization admin updated a self-managed GitLab configuration. Previous/new field pairs are recorded only for settings that changed in the update; secret credentials are never recorded, only whether they were replaced.

"group_created"



A group was created (RBAC admin or SCIM provisioning).

"group_deleted"



A group was deleted (RBAC admin or SCIM provisioning).

"group_list_viewed"



Admin viewed the list of RBAC groups.

"group_member_added"



One or more members were added to a group.

"group_member_addition_failed"



A request to add members to a group failed. Some of the requested members may have been added before the failure.

"group_member_list_viewed"



Admin viewed the members of an RBAC group.

"group_member_removal_failed"



A request to remove members from a group failed. Some of the requested members may have been removed before the failure.

"group_member_removed"



One or more members were removed from a group.

"group_project_shares_revoked"



An RBAC group's project shares in one organization were revoked in bulk.

"group_skill_shares_revoked"



An RBAC group's skill shares in one organization were revoked in bulk.

"group_updated"



A group was updated (RBAC admin or SCIM provisioning).

"group_viewed"



A group was viewed.

"group_visibility_updated"



An RBAC group's visibility policy was updated.

"inference_hooks_circuit_breaker_tripped"



The organization's Inference hooks circuit breaker tripped automatically: calls to the organization's Inference hooks endpoint crossed a failure threshold, and inspection was suspended to protect live traffic. While tripped, requests are handled according to the organization's failure handling setting — allowed through uninspected (fail open) or rejected (fail closed) — and no per-request Inference hooks activities are recorded. The tripped state persists until an administrator re-enables Inference hooks inspection (or explicitly resets the circuit breaker).

"inference_hooks_config_deleted"



Inference hooks configuration was removed for the organization.

"inference_hooks_config_updated"



Inference hooks configuration was created or updated for the organization.

"inference_hooks_request_denied"



Inference hooks inspection denied a request. The request was blocked and no model response was produced.

"inference_hooks_request_failed_open"



A request proceeded without Inference hooks inspection because a verdict could not be obtained and the organization's Inference hooks configuration is set to fail open.

"inference_hooks_signing_secret_generated"



A request signing secret was generated for the organization's Inference hooks configuration.

"integration_user_connected"



User connected to an integration.

"integration_user_disconnected"



User disconnected from an integration.

"invoice_collection_method_updated"



Invoice collection method was changed.

"lti_launch_initiated"



LTI launch was initiated.

"lti_launch_success"



LTI launch completed successfully.

"lti_platform_created"



Anthropic staff created an LTI platform integration on behalf of an org.

"lti_platform_updated"



Anthropic staff updated an LTI platform integration on behalf of an org.

"magic_link_login_failed"



A magic link sign-in attempt failed.

"magic_link_login_initiated"



A user requested a magic link sign-in email.

"magic_link_login_succeeded"



A user successfully signed in with a magic link email.

"managed_organization_setup_completed"



Managed (AWS Marketplace) organization setup was completed.

"marketplace_created"



Admin created an organization marketplace.

"marketplace_deleted"



Admin deleted an organization marketplace.

"marketplace_updated"



Admin updated an organization marketplace.

"marketplace_webhook_deleted"



Admin removed the GitHub push webhook for a marketplace.

"marketplace_webhook_provisioned"



Admin provisioned a GitHub push webhook for a marketplace.

"mcp_directory_server_published"



The organization published its approved MCP directory listing.

"mcp_server_created"



An MCP server was added to the organization.

"mcp_server_deleted"



An MCP server was removed from the organization.

"mcp_server_managed_auth_token_exchanged"



A user attempted to obtain an access token for an MCP server via enterprise managed authorization. This event reports the outcomes of attempted token exchanges. Repeated failures with the same cause may be reported once until the cause changes, and requests refused before a token exchange is attempted are not reported, except the "connector_scope_not_granted" and "identity_assertion_refused" failures described under error_type.

"mcp_server_managed_auth_updated"



An MCP server's enterprise managed authorization settings were set, changed, or cleared, including when they were supplied while the server was being added or edited. Fields without a "previous\_" prefix describe the settings after the change and are null when the server has no managed authorization settings afterwards; "previous\_" fields describe the settings before the change and are null when the server had none before (always the case for a newly added server).

"mcp_server_updated"



An MCP server's configuration was updated.

"mcp_tool_policy_updated"



The permission restriction for an MCP tool was set or cleared.

"org_analytics_api_capability_updated"



Organization analytics_api capability was enabled or disabled.

"org_bulk_delete_initiated"



Organization bulk deletion was initiated.

"org_capability_grant_added"



A capability grant was added to a workspace or role.

"org_capability_grant_removed"



A capability grant was removed from a workspace or role.

"org_claude_code_data_sharing_disabled"



Organization Claude Code data sharing was disabled.

"org_claude_code_data_sharing_enabled"



Organization Claude Code data sharing was enabled.

"org_claude_code_desktop_disabled"



Organization Claude Code Desktop was disabled.

"org_claude_code_desktop_enabled"



Organization Claude Code Desktop was enabled.

"org_claude_code_zero_data_retention_disabled"



A primary owner disabled zero data retention for Claude Code, so Claude Code content is retained according to the organization's data retention settings.

"org_compliance_api_settings_updated"



Organization compliance API settings were updated.

"org_connector_domain_guard_updated"



Enterprise admin changed whether connectors are restricted to verified domains.

"org_cowork_act_without_asking_mode_disabled"



The "Act without asking" mode in Cowork was disabled for the organization, so members can no longer let Claude act without asking for approval.

"org_cowork_act_without_asking_mode_enabled"



The "Act without asking" mode in Cowork was enabled for the organization, allowing members to let Claude act without asking for approval.

"org_cowork_agent_disabled"



Organization Cowork Agent was disabled.

"org_cowork_agent_enabled"



Organization Cowork Agent was enabled.

"org_cowork_auto_mode_disabled"



The "Auto" permission mode in Cowork was disabled for the organization, so members can no longer let Claude approve its own actions after a safety check.

"org_cowork_auto_mode_enabled"



The "Auto" permission mode in Cowork was enabled for the organization, allowing members to let Claude approve its own actions after a safety check.

"org_cowork_browser_pane_disabled"



The in-app browser in Cowork was disabled for the organization, so Claude can no longer open or use websites in a browser pane during members' Cowork sessions.

"org_cowork_browser_pane_enabled"



The in-app browser in Cowork was enabled for the organization, letting Claude open and use websites in a browser pane during members' Cowork sessions.

"org_cowork_disabled"



Organization cowork was disabled.

"org_cowork_enabled"



Organization cowork was enabled.

"org_cowork_mcp_always_allow_disabled"



The "Always allow" option for connector tools in Cowork was disabled for the organization, so each use of a connector tool that can make changes requires approval. Read-only connector tools are not affected by this setting.

"org_cowork_mcp_always_allow_enabled"



The "Always allow" option for connector tools in Cowork was enabled for the organization, letting members approve a connector tool that can make changes once and allow its later uses automatically. Read-only connector tools are not affected by this setting.

"org_cowork_otlp_settings_updated"



The organization's Cowork OpenTelemetry monitoring export settings were updated.

"org_cowork_remote_disabled"



Running Cowork in the cloud was disabled for the organization, so members can no longer run Cowork sessions in Anthropic-hosted remote environments.

"org_cowork_remote_enabled"



Running Cowork in the cloud was enabled for the organization, allowing members to run Cowork sessions in Anthropic-hosted remote environments.

"org_creation_blocked"



Organization creation was blocked.

"org_data_export_accessed"



Organization data export file was accessed/downloaded via signed URL.

"org_data_export_completed"



Organization data export was completed.

"org_data_export_started"



Organization data export was started.

"org_data_residency_updated"



The organization's inference data residency settings were updated.

"org_deleted_via_bulk"



Organization was deleted via bulk operation.

"org_deletion_requested"



Organization deletion was requested.

"org_directory_resync_completed"



Organization directory resync completed successfully.

"org_directory_resync_failed"



Organization directory resync failed.

"org_directory_resync_started"



Organization directory resync was started asynchronously.

"org_directory_sync_activated"



Organization directory sync was activated.

"org_directory_sync_add_initiated"



Organization directory sync setup was initiated.

"org_directory_sync_deleted"



Organization directory sync was deleted.

"org_discoverability_disabled"



Admin disabled organization discoverability.

"org_discoverability_enabled"



Admin enabled organization discoverability.

"org_discoverability_settings_updated"



Admin updated organization discoverability settings.

"org_domain_add_initiated"



Organization domain verification was initiated.

"org_domain_removed"



Organization domain was removed.

"org_domain_verified"



Organization domain was verified.

"org_external_key_created"



A CMEK external key config was created.

"org_external_key_deleted"



A CMEK external key config was deleted.

"org_external_key_updated"



A CMEK external key config was updated.

"org_external_key_validated"



A CMEK external key config was validated against the customer's KMS.

"org_hipaa_self_serve_enabled"



A primary owner click-accepted the BAA and enabled HIPAA protections for the organization via the self-serve flow.

"org_invite_link_disabled"



Organization invite link was disabled.

"org_invite_link_generated"



Organization invite link was generated.

"org_invite_link_regenerated"



Organization invite link was regenerated (previous link invalidated).

"org_invite_viewed"



An organization invite was viewed.

"org_invites_listed"



Organization invites were listed.

"org_ip_restriction_created"



Organization IP restriction was created.

"org_ip_restriction_deleted"



Organization IP restriction was deleted.

"org_ip_restriction_updated"



Organization IP restriction was updated.

"org_join_proposal_decided"



Approve or reject decision on a parent-org join proposal.

"org_join_request_approved"



Admin approved a join request.

"org_join_request_created"



User requested to join an organization.

"org_join_request_dismissed"



Admin dismissed a join request.

"org_join_request_instant_approved"



Join request was instantly approved.

"org_join_requests_bulk_dismissed"



Admin bulk-dismissed join requests.

"org_magic_link_second_factor_toggled"



Organization magic link second factor was toggled.

"org_member_invites_disabled"



Admin disabled member invites for the organization.

"org_member_invites_enabled"



Admin enabled member invites for the organization.

"org_members_exported"



Organization members list was exported as CSV.

"org_model_default_updated"



An organization or role default model setting was changed by an administrator.

"org_parent_join_proposal_created"



Organization parent join proposal was created.

"org_parent_search_performed"



Organization parent search was performed.

"org_sso_add_initiated"



Organization SSO setup was initiated.

"org_sso_connection_activated"



Organization SSO connection was activated.

"org_sso_connection_deactivated"



Organization SSO connection was deactivated.

"org_sso_connection_deleted"



Organization SSO connection was deleted.

"org_sso_group_role_mappings_updated"



Organization SSO group role mappings were updated.

"org_sso_provisioning_mode_changed"



Organization SSO provisioning mode was changed.

"org_sso_scim_welcome_email_toggled"



Organization SCIM-provisioned welcome email was toggled.

"org_sso_seat_tier_assignment_toggled"



Organization SSO seat tier assignment was toggled.

"org_sso_seat_tier_mappings_updated"



Organization SSO seat tier mappings were updated.

"org_sso_toggled"



Organization SSO was toggled on or off.

"org_sync_deleting_synchronized_files_started"



Organization started deleting synchronized files.

"org_sync_synchronized_files_deleted"



Organization synchronized files were deleted.

"org_taint_added"



A taint was added to an organization.

"org_taint_removed"



A taint was removed from an organization.

"org_user_deleted"



User was removed from organization.

"org_user_invite_accepted"



Organization user invite was accepted.

"org_user_invite_deleted"



Organization user invite was deleted.

"org_user_invite_re_sent"



Organization user invite was re-sent.

"org_user_invite_rejected"



Organization user invite was rejected.

"org_user_invite_sent"



Organization user invite was sent.

"org_user_left"



User removed themselves from organization.

"org_user_shares_retained"



A member left or was removed from the organization while projects, skills, plugins, or chats they had shared were still shared, and those shares were kept.

"org_user_trusted_devices_revoked"



An organization admin revoked a member's trusted devices and signed the member out of all active sessions.

"org_user_viewed"



An organization user was viewed.

"org_users_listed"



Organization users were listed.

"org_work_across_apps_disabled"



The organization's "Let Claude work across apps" setting was turned off.

"org_work_across_apps_enabled"



The organization's "Let Claude work across apps" setting was turned on.

"organization_address_updated"



The organization's billing or shipping address was updated.

"organization_icon_deleted"



Organization's custom icon deleted.

"organization_icon_updated"



Organization's custom icon uploaded or replaced.

"owned_projects_access_restored"



Access to owned projects was restored.

"payment_method_updated"



The organization's default payment method was updated.

"pending_share_created"



A pending share of a project or skill was created for an email address that is not yet an organization member.

"pending_share_revoked"



A pending share of a project or skill was revoked before the invitee joined the organization.

"phone_code_sent"



User requested a phone verification code.

"phone_code_verified"



User successfully verified their phone code.

"platform_agent_archived"



An agent was archived on the API platform.

"platform_agent_created"



An agent was created on the API platform.

"platform_agent_deleted"



An agent was deleted from the API platform.

"platform_agent_deployment_archived"



An agent deployment was archived on the API platform.

"platform_agent_deployment_created"



An agent deployment was created on the API platform.

"platform_agent_deployment_deleted"



An agent deployment was deleted from the API platform.

"platform_agent_deployment_paused"



An agent deployment was paused on the API platform.

"platform_agent_deployment_run_triggered"



An agent deployment was run on demand on the API platform.

"platform_agent_deployment_unpaused"



An agent deployment was resumed on the API platform.

"platform_agent_deployment_updated"



An agent deployment was updated on the API platform.

"platform_agent_session_archived"



An agent session was archived on the API platform.

"platform_agent_session_created"



An agent session was created on the API platform.

"platform_agent_session_deleted"



An agent session was deleted from the API platform.

"platform_agent_session_resource_added"



A resource was attached to an agent session.

"platform_agent_session_resource_deleted"



A resource attached to an agent session was removed.

"platform_agent_session_resource_updated"



A resource attached to an agent session was updated.

"platform_agent_session_thread_archived"



A thread within an agent session was archived.

"platform_agent_session_updated"



An agent session was updated on the API platform.

"platform_agent_updated"



An agent was updated on the API platform.

"platform_api_key_created"



An API key was created.

"platform_api_key_updated"



An API key was updated.

"platform_app_attest_authentication"



An attested mobile device attempted to exchange an Apple App Attest assertion for Anthropic API credentials.

"platform_billing_upgraded_to_prepaid"



The organization's API billing was upgraded to the prepaid plan.

"platform_clearance_workspace_program_request_cleared"



A workspace's clearance program assignment was removed.

"platform_clearance_workspace_program_request_set"



A workspace's clearance program assignment was created or updated.

"platform_cost_report_viewed"



The cost report was viewed.

"platform_dream_archived"



A Dream (asynchronous memory-consolidation job) was archived.

"platform_dream_cancelled"



A Dream (asynchronous memory-consolidation job) was cancelled before it completed.

"platform_dream_created"



A Dream (asynchronous memory-consolidation job) was created.

"platform_federated_authentication"



A federated workload identity attempted to exchange an OIDC token for Anthropic API credentials.

"platform_federation_issuer_archived"



An OIDC federation issuer was archived.

"platform_federation_issuer_created"



An OIDC federation issuer was created, registering an external identity provider that federation rules can trust for workload authentication.

"platform_federation_issuer_updated"



An OIDC federation issuer was updated.

"platform_federation_rule_archived"



An OIDC federation rule was archived.

"platform_federation_rule_created"



An OIDC federation rule was created, allowing tokens from a federation issuer to authenticate as a service account or user. Rules may additionally match on token claims or a condition expression, which are not included in this event.

"platform_federation_rule_updated"



An OIDC federation rule was updated.

"platform_federation_rule_workspace_added"



A federation rule was enabled for a workspace.

"platform_federation_rule_workspace_removed"



A federation rule was disabled for a workspace.

"platform_file_content_downloaded"



Activity logged when file content is downloaded via GET /v1/files/{file_id}/content.

"platform_file_deleted"



Activity logged when a file is deleted via DELETE /v1/files/{file_id}.

"platform_file_uploaded"



Activity logged when a file is uploaded via POST /v1/files.

"platform_memory_created"



An agent memory document was created.

"platform_memory_deleted"



An agent memory document was deleted.

"platform_memory_store_archived"



An agent memory store was archived. Archived stores reject new memory writes and cannot be attached to new sessions; deletion and redaction remain permitted for privacy scrubbing.

"platform_memory_store_created"



An agent memory store was created.

"platform_memory_store_deleted"



An agent memory store was deleted. Memory content removal may complete asynchronously for very large stores.

"platform_memory_store_updated"



An agent memory store's name, description, or metadata was updated.

"platform_memory_updated"



An agent memory document's content or path was updated.

"platform_memory_version_redacted"



A historical version of an agent memory document was redacted. Redaction scrubs the stored content of a specific version while preserving the version's existence in the history.

"platform_oauth_app_created"



An OAuth app was created.

"platform_oauth_app_revoked"



An OAuth app was revoked.

"platform_oauth_app_updated"



An OAuth app was updated.

"platform_plugin_directory_submission_created"



A plugin directory submission was created on the API platform. A plugin directory submission is a request to list a plugin in the public plugin directory.

"platform_plugin_directory_submission_deleted"



A plugin directory submission was deleted on the API platform.

"platform_plugin_directory_submission_updated"



A plugin directory submission was updated on the API platform.

"platform_service_account_archived"



A service account was archived.

"platform_service_account_created"



A service account was created.

"platform_service_account_updated"



A service account was updated.

"platform_service_account_workspace_member_added"



A service account was added as a member of a workspace.

"platform_service_account_workspace_member_removed"



A service account was removed from a workspace.

"platform_service_account_workspace_member_updated"



A service account's workspace membership role was updated.

"platform_signing_key_created"



Activity logged when a new request-signing key is registered for the org.

"platform_signing_key_deleted"



Activity logged when a signing key is permanently deleted.

"platform_signing_key_rotated"



Activity logged when an in-memory signing key is rotated.

"platform_skill_version_content_downloaded"



The content of a skill version was downloaded through the Skills API.

"platform_skill_version_created"



Activity logged when a skill version is created via POST /v1/skills/{skill_id}/versions.

"platform_skill_version_deleted"



Activity logged when a skill version is deleted via DELETE /v1/skills/{skill_id}/versions/{version}.

"platform_spend_limit_alert_emails_updated"



Spend limit alert email addresses and role targets were updated for an org.

"platform_spend_limit_created"



An org-level fixed-dollar spend limit was created.

"platform_spend_limit_deleted"



An org-level spend limit was removed.

"platform_spend_limit_updated"



An org-level spend limit snooze/ignore state was changed.

"platform_usage_report_claude_code_viewed"



The Claude Code usage report was viewed.

"platform_usage_report_messages_viewed"



The messages usage report was viewed.

"platform_workspace_archived"



A workspace was archived.

"platform_workspace_created"



A workspace was created.

"platform_workspace_inference_data_retention_disabled"



The zero data retention override was disabled for a workspace.

"platform_workspace_inference_data_retention_enabled"



The zero data retention override was enabled for a workspace.

"platform_workspace_member_added"



A member was added to a workspace.

"platform_workspace_member_removed"



A member was removed from a workspace.

"platform_workspace_member_updated"



A workspace member was updated.

"platform_workspace_member_viewed"



A workspace member was viewed.

"platform_workspace_members_listed"



Workspace members were listed.

"platform_workspace_rate_limit_deleted"



A workspace rate limit was deleted.

"platform_workspace_rate_limit_updated"



A workspace rate limit was created or updated.

"platform_workspace_updated"



A workspace was updated.

"plugin_installation_preference_updated"



An org admin changed the installation preference for a plugin.

"prepaid_auto_recharge_disabled"



Auto-recharge was disabled for API prepaid org.

"prepaid_auto_recharge_updated"



Auto-recharge settings were updated for API prepaid org.

"prepaid_extra_usage_auto_reload_disabled"



Prepaid usage credit auto-reload was disabled.

"prepaid_extra_usage_auto_reload_enabled"



Prepaid usage credit auto-reload was enabled.

"prepaid_extra_usage_auto_reload_settings_updated"



Prepaid usage credit auto-reload settings were updated.

"primary_owner_transferred"



Primary owner role was transferred to another org member.

"rbac_role_assigned"



Admin assigned an RBAC custom role to a principal.

"rbac_role_created"



Admin created an RBAC custom role.

"rbac_role_deleted"



Admin deleted an RBAC custom role.



"rbac_role_grant_updated"



Admin requested a capability grant for an RBAC custom role, or removed it.

Records the admin's change to the role. Whether the grant is currently in effect on the role is reported separately.



"rbac_role_permission_added"



Admin added a permission to an RBAC custom role.

Emitted once per requested permission, including permissions the role already had, so a retried request still produces a complete audit record.



"rbac_role_permission_removed"



Admin removed a permission from an RBAC custom role.

Emitted once per requested permission, including permissions the role already lacked, so a retried request still produces a complete audit record.

"rbac_role_unassigned"



Admin unassigned an RBAC custom role from a principal.

"rbac_role_updated"



Admin updated an RBAC custom role.

"role_assignment_granted"



Role assignment was granted.

"role_assignment_revoked"



Role assignment was revoked.

"scim_user_created"



A SCIM user was provisioned.

"scim_user_deleted"



A SCIM user was deleted.

"scim_user_updated"



A SCIM user was updated.

"scoped_api_key_deleted"



A scoped API key was deleted.

"scoped_api_key_updated"



A scoped API key was renamed or its activation state changed.

"seat_tier_changes_cancelled"



Scheduled seat tier downgrades were cancelled.

"seat_tiers_purchased"



Seat tiers were purchased or upgraded on a subscription.

"service_created"



Activity logged when an org service is explicitly created.

"service_deleted"



Activity logged when an org service is deleted.

"service_key_created"



Activity logged when a new org service key is created.

"service_key_revoked"



Activity logged when an org service key is revoked.

"session_revoked"



User revoked a specific session.

"session_share_accessed"



Session share was accessed.

"session_share_created"



Session share was created.

"session_share_revoked"



Session share was revoked.

"slack_workspace_claim_revoked"



A Slack workspace or Enterprise Grid organization was disconnected from the organization for Claude in Slack.

"slack_workspace_claimed"



A Slack workspace or Enterprise Grid organization was connected to the organization for Claude in Slack.

"social_login_succeeded"



A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).

"sso_login_failed"



An SSO sign-in attempt failed.

"sso_login_initiated"



A user started an SSO sign-in flow.

"sso_login_succeeded"



A user successfully signed in with SSO.

"sso_second_factor_magic_link"



SSO second factor magic link was used.

"step_up_authentication_failed"



An additional identity check failed.

"step_up_authentication_succeeded"



The user completed an additional identity check to confirm a sensitive action.

"step_up_credential_enrolled"



A user enrolled a passkey for confirming sensitive actions on their account.

"subscription_cancellation_scheduled"



Subscription cancellation was scheduled at end of billing period.

"subscription_quantity_updated"



Contracted subscription seat quantity was updated.

"subscription_renewed"



A cancelled subscription was renewed.

"subscription_resumed"



A scheduled subscription cancellation was reversed.

"subscription_started"



A new subscription was created (Team or Enterprise).

"subscription_upgraded"



Subscription plan was upgraded (e.g. Team to Enterprise).

"trusted_device_credential_rotated"



The identity-verification credential of a trusted device was rotated to a new key.

"trusted_device_enrolled"



A device was enrolled as a trusted device for the user's account. Trusted devices can be used to confirm the user's identity for sensitive actions.

"trusted_device_revoked"



A trusted device was removed from the user's account.

"tunnel_archived"



An MCP tunnel was archived.

"tunnel_certificate_added"



An inner-TLS CA certificate was added to a tunnel.

"tunnel_certificate_revoked"



An inner-TLS CA certificate was revoked from a tunnel.

"tunnel_created"



An MCP tunnel was created.

"tunnel_token_minted"



An OAuth bearer token for the tunnel management API was minted.

"tunnel_token_revealed"



The Cloudflare connector secret for a tunnel was revealed to the caller.

"tunnel_token_revoked"



An OAuth bearer token for the tunnel management API was revoked.



"tunnel_token_rotated"



The Cloudflare connector secret for a tunnel was rotated.

`tunnel_token_id` is the id of the *newly-issued* token. The previous token is invalidated by the rotation and its id is not recorded here.

"user_consent_recorded"



User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).

"user_consent_revoked"



User revoked a previously granted consent for a specific entity.

"user_logged_out"



A user signed out of one or all sessions.

"verification_evidence_submitted"



Verification evidence was submitted for an organization's verification.

"verification_program_application_created"



An organization applied to a verification program.

"workspace_member_spend_limit_created"



A per-member or workspace-default Claude Code spend limit was created.

"workspace_member_spend_limit_deleted"



A per-member or workspace-default Claude Code spend limit was deleted.

"workspace_member_spend_limit_updated"



A per-member Claude Code spend limit amount was updated.

"workspace_spend_limit_alert_emails_updated"



Spend limit alert email recipients were updated for a workspace.

"workspace_spend_limit_created"



A workspace-level API spend limit was created.

"workspace_spend_limit_deleted"



A workspace-level API spend limit was deleted.



limit: optional number



Maximum results (default: 100, max: 5000)

default100

minimum1

maximum5000



order: optional "asc" or "desc"



Sort direction by `created_at`. `desc` (default) returns newest-first; `asc` returns oldest-first for incremental sync. Activities become queryable after a short asynchronous ingestion delay. When using `asc` with `after_id` for incremental sync, late-arriving rows with timestamps behind the cursor will be skipped; consumers that need at-least-once delivery should periodically re-poll an overlap window via `created_at.gte` and deduplicate by `id`. `after_id` and `before_id` are relative to this order.

defaultdesc

One of the following:

"asc"



"desc"



organization_ids: optional array of string



Filter activities by organization IDs (accepts `org_...` or organization UUID). Enumerate IDs via `GET /v1/compliance/organizations`.

user_ids: optional array of string



Alias for `actor_ids[]`, for consistency with other compliance routes. If both are provided, the lists are merged.

##### Headers

"x-api-key": optional string



##### Returns



data: optional array of AbuseDecisionReceived or AccountDeleted or AdminAPIKeyCreated or 511 more



List of activity records. Each element's `type` field identifies which activity it is and which additional fields are present.

One of the following:



AbuseDecisionReceived object{ type: "abuse_decision_received", actor, decision, 5 more }



An external anti-abuse service reported a consequential decision about a sign-in or sign-up attempt.



AccountDeleted object{ type: "account_deleted", actor, id, 3 more }



User-initiated self-service account deletion.



AdminAPIKeyCreated object{ type: "admin_api_key_created", actor, admin_api_key_id, 5 more }



An admin API key was created.



AdminAPIKeyDeleted object{ type: "admin_api_key_deleted", actor, admin_api_key_id, 4 more }



An admin API key was deleted.



AdminAPIKeyUpdated object{ type: "admin_api_key_updated", actor, admin_api_key_id, 5 more }



An admin API key was updated (renamed or activated/deactivated).



AdminConnectorRequestResolved object{ type: "admin_connector_request_resolved", actor, decision, 6 more }



Admin approved or dismissed pending member requests to enable an MCP connector.



AdminRequestCreated object{ type: "admin_request_created", actor, request_type, 4 more }



Admin request created by an org member (seat upgrade, limit increase, join org, end-user invite).



AdminSetupChecklistStepDelegated object{ type: "admin_setup_checklist_step_delegated", actor, step, 6 more }



A step of the Claude Enterprise admin setup checklist was delegated to a teammate — an organization member, or an email address that has not joined the organization yet — replacing any earlier delegation of that step.



AdminSetupChecklistStepDelegationCancelled object{ type: "admin_setup_checklist_step_delegation_cancelled", actor, step, 4 more }



The delegation of a Claude Enterprise admin setup checklist step was cancelled.



AgeVerified object{ type: "age_verified", actor, id, 3 more }



User age was verified.



AnonymousMobileLoginAttempted object{ type: "anonymous_mobile_login_attempted", actor, id, 3 more }



Anonymous mobile login was attempted.



APIKeyCreated object{ type: "api_key_created", actor, api_key_id, 6 more }



Activity logged when a new API key is created.



ClaudeArtifactAccessFailed object{ type: "claude_artifact_access_failed", actor, id, 6 more }



An attempt to access an artifact failed.



ClaudeArtifactCommented object{ type: "claude_artifact_commented", actor, claude_artifact_id, 9 more }



Comment activity on a published artifact: a comment was added, a thread's resolved state was changed, or a thread was deleted. The actor is the user who performed the action; the comment text itself is stored with the artifact and is not part of this record.



ClaudeArtifactCommentsViewed object{ type: "claude_artifact_comments_viewed", actor, claude_artifact_id, 5 more }



An artifact's comments were viewed.



ClaudeArtifactCreated object{ type: "claude_artifact_created", actor, claude_artifact_id, 4 more }



An artifact was created.



ClaudePublishedArtifactDeleted object{ type: "claude_published_artifact_deleted", actor, claude_published_artifact_id, 4 more }



A published artifact was deleted or unpublished — by its creator, by an organization admin, or by Anthropic (for example, when it was removed for a policy violation).



ClaudeArtifactPublished object{ type: "claude_artifact_published", actor, artifact_type, 10 more }



A new version of an artifact was published — for an artifact created in a chat this is the action that made it publicly viewable; for an artifact created outside a chat it is recorded when the artifact is saved, including saves of private artifacts, except that automatic saves made while a person keeps editing may be recorded periodically for that person rather than once per save; changes to who can access the artifact are recorded separately as claude_artifact_sharing_updated.



ClaudeArtifactSharingUpdated object{ type: "claude_artifact_sharing_updated", actor, audience, 14 more }



An artifact's sharing settings were updated.



ClaudeArtifactViewed object{ type: "claude_artifact_viewed", actor, claude_artifact_id, 5 more }



An artifact was viewed.



AuditLogExportAccessed object{ type: "audit_log_export_accessed", actor, id, 3 more }



Audit log export file was accessed/downloaded via signed URL.



AuditLogExportStarted object{ type: "audit_log_export_started", actor, id, 5 more }



Audit log export was initiated.



BillingEmailsUpdated object{ type: "billing_emails_updated", actor, id, 6 more }



The organization's billing email recipients were updated.



CcrAgentCreated object{ type: "ccr_agent_created", actor, agent_id, 11 more }



A Claude Code agent was created.



CcrAgentDeleted object{ type: "ccr_agent_deleted", actor, agent_id, 7 more }



A Claude Code agent was deleted.



CcrAgentProxyAnthropicOidcTokenExchanged object{ type: "ccr_agent_proxy_anthropic_oidc_token_exchanged", actor, agent_id, 13 more }



The Claude Code agent proxy exchanged a minted identity token for short-lived credentials in the organization's own cloud. Recorded for exchange targets only (such as "aws" and "gcp"; the "direct" target has no exchange step). One event is recorded per exchange call; a request served from the proxy's exchanged-credential cache does not exchange again and is not recorded here. Per-request detail for traffic the credentials were injected into is available in the agent proxy network events.



CcrAgentProxyAnthropicOidcTokenMinted object{ type: "ccr_agent_proxy_anthropic_oidc_token_minted", actor, agent_id, 15 more }



The Claude Code agent proxy minted a short-lived identity token for an anthropic_oidc credential. One event is recorded per fresh token issuance; a request served from the proxy's short-lived token cache does not mint a new token and is not recorded here. Per-request detail for traffic the credential was injected into is available in the agent proxy network events.



CcrAgentProxyCredentialCreated object{ type: "ccr_agent_proxy_credential_created", actor, credential_id, 10 more }



A Claude Code agent proxy credential was created. Credentials hold the secrets the agent proxy injects into requests Claude Code sessions send to approved external services; each credential belongs to an agent proxy profile. Audit events carry only credential names and settings, never the secret material itself.



CcrAgentProxyCredentialDeleted object{ type: "ccr_agent_proxy_credential_deleted", actor, credential_id, 6 more }



A Claude Code agent proxy credential was deleted. Its secret material was removed and can no longer be sent to any host.



CcrAgentProxyCredentialRotated object{ type: "ccr_agent_proxy_credential_rotated", actor, credential_id, 11 more }



A Claude Code agent proxy credential's secret material was replaced. The replacement keeps the same name, profile, and allowed hosts under a new credential identifier, and everything that referenced the old credential now uses the replacement.



CcrAgentProxyCredentialUpdated object{ type: "ccr_agent_proxy_credential_updated", actor, credential_id, 10 more }



A Claude Code agent proxy credential's settings were updated. Only the display name and the allowed host patterns can be updated; the secret material can only be replaced through a rotation.



CcrAgentProxyDestinationDeleted object{ type: "ccr_agent_proxy_destination_deleted", actor, deleted_with_profile, 7 more }



An agent proxy destination was deleted.



CcrAgentProxyNetworkEventsListed object{ type: "ccr_agent_proxy_network_events_listed", actor, failed, 5 more }



A Claude Code network activity export was accessed for the given hour.



CcrAgentProxyProfileBound object{ type: "ccr_agent_proxy_profile_bound", actor, profile_id, 6 more }



A Claude Code agent proxy profile was bound to a scope, applying its policy to Claude Code sessions in that scope.



CcrAgentProxyProfileCreated object{ type: "ccr_agent_proxy_profile_created", actor, display_name, 7 more }



A Claude Code agent proxy profile was created. Agent proxy profiles are named, reusable bundles of access policy that administrators bind to parts of the organization.



CcrAgentProxyProfileDeleted object{ type: "ccr_agent_proxy_profile_deleted", actor, deleted_credential_count, 10 more }



A Claude Code agent proxy profile was deleted, removing its policy from everything it was bound to.



CcrAgentProxyProfileUnbound object{ type: "ccr_agent_proxy_profile_unbound", actor, profile_id, 6 more }



A Claude Code agent proxy profile was unbound from a scope, removing its policy from Claude Code sessions in that scope.



CcrAgentProxyProfileUpdated object{ type: "ccr_agent_proxy_profile_updated", actor, profile_id, 6 more }



A Claude Code agent proxy profile's configuration was updated.



CcrAgentProxyProvisioningCredentialRejected object{ type: "ccr_agent_proxy_provisioning_credential_rejected", actor, credential_id, 8 more }



An organization owner rejected a credential that a teammate submitted via an agent proxy provisioning link: the credential and its disabled rule were deleted and the link was revoked. The actor is the owner; the submitter is recorded for attribution.



CcrAgentProxyProvisioningLinkEnabled object{ type: "ccr_agent_proxy_provisioning_link_enabled", actor, credential_id, 7 more }



An organization owner enabled a credential that a teammate submitted via an agent proxy provisioning link: the disabled rule created at submission was switched to enforce, so the credential now takes traffic. The actor is the owner; the submitter is the actor on the prior ccr_agent_proxy_provisioning_link_submitted event.



CcrAgentProxyProvisioningLinkGenerated object{ type: "ccr_agent_proxy_provisioning_link_generated", actor, link_id, 5 more }



An organization owner generated a one-time agent proxy credential provisioning link so a teammate can submit a credential into the target agent proxy profile without holding the owner role.



CcrAgentProxyProvisioningLinkRevoked object{ type: "ccr_agent_proxy_provisioning_link_revoked", actor, link_id, 5 more }



An organization owner revoked an unfilled agent proxy provisioning link.



CcrAgentProxyProvisioningLinkSubmitted object{ type: "ccr_agent_proxy_provisioning_link_submitted", actor, credential_id, 8 more }



A teammate submitted a credential via an agent proxy provisioning link. The credential and a disabled rule are created; the credential takes traffic only after an organization owner enables the submitted credential. This event records the link-mediated lifecycle; the credential itself additionally emits ccr_agent_proxy_credential_created.



CcrAgentProxyRuleCreated object{ type: "ccr_agent_proxy_rule_created", action, actor, 20 more }



An agent proxy rule was created. A rule decides what happens to a session's outbound requests that match it.



CcrAgentProxyRuleDeleted object{ type: "ccr_agent_proxy_rule_deleted", actor, deleted_with_profile, 7 more }



An agent proxy rule was deleted.



CcrAgentProxyRuleUpdated object{ type: "ccr_agent_proxy_rule_updated", action, actor, 21 more }



An agent proxy rule was updated. An update replaces everything the rule matches and does, so the host name patterns here are the rule's complete set after the update.



CcrAgentSlackAccessScopeCreated object{ type: "ccr_agent_slack_access_scope_created", actor, agent_id, 7 more }



A Claude Code agent was granted access to read or write in an additional Slack channel beyond the one it is assigned to.



CcrAgentSlackAccessScopeDeleted object{ type: "ccr_agent_slack_access_scope_deleted", actor, agent_id, 6 more }



A Claude Code agent's access to an additional Slack channel was revoked.



CcrAgentSlackBindingCreated object{ type: "ccr_agent_slack_binding_created", actor, agent_id, 6 more }



A Claude Code agent was assigned to a Slack channel or workspace as its dedicated agent.



CcrAgentSlackBindingDeleted object{ type: "ccr_agent_slack_binding_deleted", actor, agent_id, 6 more }



A Claude Code agent's assignment to a Slack channel or workspace was removed.



CcrAgentUpdated object{ type: "ccr_agent_updated", actor, agent_id, 10 more }



A Claude Code agent's configuration was updated. Also emitted with updated_fields \["is_virtual"\] alone when an auto-provisioned agent is promoted to a configured one, whether by an update request targeting it or by binding an agent proxy profile to it.



CcrChannelManagerAdded object{ type: "ccr_channel_manager_added", actor, agent_id, 7 more }



An org owner/admin assigned an organization member to manage the Claude-in-Slack configuration of one Slack channel.



CcrChannelManagerRemoved object{ type: "ccr_channel_manager_removed", actor, agent_id, 7 more }



An org owner/admin removed an organization member's assignment to manage the Claude-in-Slack configuration of one Slack channel.



CcrRoleChannelAssignmentDeleted object{ type: "ccr_role_channel_assignment_deleted", actor, previous_channel_count, 5 more }



CcrRoleChannelAssignmentDeleted is emitted when an org owner/admin removes an RBAC role's channel assignment row (the role reverts to granting zero channels).



CcrRoleChannelAssignmentUpdated object{ type: "ccr_role_channel_assignment_updated", actor, channel_count, 7 more }



CcrRoleChannelAssignmentUpdated is emitted when an org owner/admin sets or replaces the list of Slack channels an RBAC role's holders may configure via the delegated Claude-in-Slack channel-manage surface.



CcrSessionCreated object{ type: "ccr_session_created", actor, session_id, 5 more }



A Claude Code session was created. A session is one coding interaction with Claude.



CcrSessionDeleted object{ type: "ccr_session_deleted", actor, session_id, 4 more }



A Claude Code session was deleted.



CcrSessionUpdated object{ type: "ccr_session_updated", actor, session_id, 5 more }



A Claude Code session's settings were updated.



CcrSlackChannelJoined object{ type: "ccr_slack_channel_joined", actor, slack_channel_id, 5 more }



Claude's Slack app joined a public Slack channel at an organization administrator's request.



ClaudeChatSettingsUpdated object{ type: "claude_chat_settings_updated", actor, claude_chat_id, 5 more }



User updated the settings for a conversation.



ClaudeChatSnapshotCreated object{ type: "claude_chat_snapshot_created", actor, claude_chat_id, 5 more }



User created/shared a chat snapshot.



ClaudeChatSnapshotDeleted object{ type: "claude_chat_snapshot_deleted", actor, claude_chat_snapshot_id, 5 more }



User deleted/unshared a chat snapshot.



ClaudeChatSnapshotViewed object{ type: "claude_chat_snapshot_viewed", actor, claude_chat_snapshot_id, 5 more }



User viewed a chat snapshot (authenticated or public/unauthenticated).



ClaudeArtifactDuplicated object{ type: "claude_artifact_duplicated", actor, claude_artifact_id, 6 more }



A user duplicated an artifact they could view into a new artifact that they own. The actor is the user who created the copy; the source artifact is not modified.



ClaudeArtifactExternalSharingPermissionUpdated object{ type: "claude_artifact_external_sharing_permission_updated", action, actor, 5 more }



An organization admin allowed one artifact to be shared outside the organization by link while the organization-wide external sharing setting was off, or revoked that permission.



ClaudeArtifactInviteAccepted object{ type: "claude_artifact_invite_accepted", actor, claude_artifact_id, 8 more }



Someone outside the organization signed in with a verified account for the invited address and accepted an invitation to an artifact, and can now open it; recorded in the artifact owner's organization. The person who accepted is identified by `invitee_email` and `invitee_user_id`.



ClaudeArtifactInviteCreated object{ type: "claude_artifact_invite_created", actor, claude_artifact_id, 7 more }



A member invited (or re-invited) an email address outside the organization to an artifact; recorded in the artifact owner's organization with the inviting member as the actor.



ClaudeArtifactInviteRevoked object{ type: "claude_artifact_invite_revoked", actor, claude_artifact_id, 8 more }



A member withdrew an invitation to an artifact for someone outside the organization, removing any access that invitation had granted; recorded in the artifact owner's organization with that member as the actor.



ClaudeArtifactInviteRoleUpdated object{ type: "claude_artifact_invite_role_updated", actor, claude_artifact_id, 9 more }



A member changed the access level of an email invitation to an artifact for someone outside the organization, whether the invitation was still pending or had been accepted; recorded in the artifact owner's organization with that member as the actor.



ClaudeChatAccessFailed object{ type: "claude_chat_access_failed", actor, claude_chat_id, 4 more }



A user was denied access to a Claude.ai chat conversation.



ClaudeChatCreated object{ type: "claude_chat_created", actor, claude_chat_id, 5 more }



User created a chat.



ClaudeChatDeleted object{ type: "claude_chat_deleted", actor, claude_chat_id, 5 more }



A user deleted a Claude.ai chat conversation.



ClaudeChatDeletionFailed object{ type: "claude_chat_deletion_failed", actor, claude_chat_id, 4 more }



A request to delete a Claude.ai chat conversation failed.



ClaudeChatSyncSourceCreated object{ type: "claude_chat_sync_source_created", actor, claude_chat_sync_source_id, 6 more }



A sync source was connected for syncing external content into Claude chats.



ClaudeChatSyncSourceDeleted object{ type: "claude_chat_sync_source_deleted", actor, claude_chat_sync_source_id, 5 more }



A sync source was disconnected from Claude chats.



ClaudeChatSyncSourceUpdated object{ type: "claude_chat_sync_source_updated", actor, claude_chat_sync_source_id, 7 more }



A Claude chat sync source's configuration was updated.



ClaudeChatUpdated object{ type: "claude_chat_updated", actor, claude_chat_id, 5 more }



User updated the chat metadata (e.g name, model).



ClaudeChatViewed object{ type: "claude_chat_viewed", actor, claude_chat_id, 5 more }



A user viewed a Claude.ai chat conversation.



ClaudeCodeCredentialRevoked object{ type: "claude_code_credential_revoked", actor, credential_type, 11 more }



A Claude Code credential (runner pool key, runner token, or session token) was revoked. The credential itself is never recorded.



ClaudeCodeReviewConfigUpdated object{ type: "claude_code_review_config_updated", actor, enabled, 15 more }



Claude Code Review configuration was enabled/disabled for an org.



ClaudeCodeReviewRepositoryAdded object{ type: "claude_code_review_repository_added", actor, config_id, 7 more }



A repository was added to org-level Claude Code Review configuration.



ClaudeCodeReviewRepositoryRemoved object{ type: "claude_code_review_repository_removed", actor, config_id, 6 more }



A repository was removed from org-level Claude Code Review configuration.



ClaudeCodeReviewRepositoryUpdated object{ type: "claude_code_review_repository_updated", actor, config_id, 8 more }



A Claude Code Review repository configuration was updated.



ClaudeCodeRunnerDeleted object{ type: "claude_code_runner_deleted", actor, runner_id, 5 more }



A self-hosted runner was forcibly removed from its pool. Sessions assigned to the runner were returned to the pool queue, unless a session had already been requeued repeatedly, in which case it was marked stuck instead of being requeued again.



ClaudeCodeRunnerPoolCreated object{ type: "claude_code_runner_pool_created", actor, display_name, 5 more }



A self-hosted runner pool for Claude Code was created.



ClaudeCodeRunnerPoolDeleted object{ type: "claude_code_runner_pool_deleted", actor, runner_pool_id, 5 more }



A self-hosted runner pool was deleted.



ClaudeCodeRunnerPoolSecretMinted object{ type: "claude_code_runner_pool_secret_minted", actor, jti, 7 more }



A registration key for a self-hosted runner pool was minted. Runners present this key to join the pool. The key itself is never recorded.



ClaudeCodeRunnerPoolSessionQueueUpdated object{ type: "claude_code_runner_pool_session_queue_updated", action, actor, 7 more }



An admin changed a session's position in its self-hosted runner pool's queue: requeued it onto a different runner, dismissed it from the queue, or re-admitted it for another runner provisioning attempt.



ClaudeCodeRunnerPoolUpdated object{ type: "claude_code_runner_pool_updated", actor, display_name, 6 more }



A self-hosted runner pool's settings were updated.



ClaudeCodeSecurityCenterConfigUpdated object{ type: "claude_code_security_center_config_updated", actor, enabled, 5 more }



Claude Code Security Center scanning was enabled/disabled for an org.



ClaudeCodeSecurityScanCancelled object{ type: "claude_code_security_scan_cancelled", actor, scan_project_id, 5 more }



In-flight Claude Code Security scans were cancelled for a project.



ClaudeCodeSecurityScanCreated object{ type: "claude_code_security_scan_created", actor, scan_id, 5 more }



A Claude Code Security scan was started.



ClaudeCodeSecurityScanProjectMemberUpdated object{ type: "claude_code_security_scan_project_member_updated", action, actor, 8 more }



A person's access to a Claude Code Security scan project was granted, changed, or revoked.



ClaudeCodeSecurityScanProjectUpdated object{ type: "claude_code_security_scan_project_updated", action, actor, 6 more }



A Claude Code Security scan project was archived, unarchived, created, or migrated to a new product experience.



ClaudeCodeSecurityScanProjectVisibilityUpdated object{ type: "claude_code_security_scan_project_visibility_updated", action, actor, 7 more }



A Claude Code Security scan project was shared with the organization or made private.



ClaudeCodeSecurityScanRunUpdated object{ type: "claude_code_security_scan_run_updated", action, actor, 5 more }



A single Claude Code Security scan run was archived, unarchived, or resumed after a billing pause.



ClaudeCodeSecurityScanScheduleDeleted object{ type: "claude_code_security_scan_schedule_deleted", actor, scan_project_id, 4 more }



A recurring scan schedule was deleted for a Claude Code Security project.



ClaudeCodeSecurityScanScheduleUpdated object{ type: "claude_code_security_scan_schedule_updated", actor, cadence, 5 more }



A recurring scan schedule was set or replaced for a Claude Code Security project.



ClaudeCodeSecurityVulnerabilityDeleted object{ type: "claude_code_security_vulnerability_deleted", actor, scan_id, 5 more }



A Claude Code Security vulnerability finding was permanently deleted.



ClaudeCodeSecurityVulnerabilityFixSessionCreated object{ type: "claude_code_security_vulnerability_fix_session_created", actor, scan_id, 6 more }



A Claude Code remediation session was created for a Claude Code Security vulnerability finding.



ClaudeCodeSecurityVulnerabilityUpdated object{ type: "claude_code_security_vulnerability_updated", action, actor, 6 more }



A Claude Code Security vulnerability finding was dismissed, restored, marked fixed, or reopened.



ClaudeCodeSecurityWebhookCreated object{ type: "claude_code_security_webhook_created", actor, url, 6 more }



A Claude Code Security outbound webhook was created.



ClaudeCodeSecurityWebhookDeleted object{ type: "claude_code_security_webhook_deleted", actor, webhook_id, 5 more }



A Claude Code Security outbound webhook was deleted.



ClaudeCodeSecurityWebhookSecretUpdated object{ type: "claude_code_security_webhook_secret_updated", actor, webhook_id, 5 more }



The HMAC signing secret for a Claude Code Security webhook was rotated.



ClaudeCodeSecurityWebhookUpdated object{ type: "claude_code_security_webhook_updated", actor, webhook_id, 5 more }



A Claude Code Security outbound webhook was updated.



ClaudeCodeTeamMemoryACLUpdated object{ type: "claude_code_team_memory_acl_updated", action, actor, 7 more }



An RBAC group was added to or removed from the Claude Code team-memory ACL.



ClaudeCodeTeamMemoryUpdated object{ type: "claude_code_team_memory_updated", actor, deleted_all, 12 more }



Claude Code team memory shared with the organization was updated.



ClaudeCodeTeamOnboardingGuideUpdated object{ type: "claude_code_team_onboarding_guide_updated", action, actor, 9 more }



A Claude Code team onboarding guide was created, updated, or deleted.



ClaudeCodeUserMarketplacesUpdated object{ type: "claude_code_user_marketplaces_updated", actor, deleted_all, 10 more }



A user's Claude Code plugin marketplace selections were updated on Anthropic servers.



ClaudeCodeUserMemoryUpdated object{ type: "claude_code_user_memory_updated", actor, deleted_all, 11 more }



A user's synced private Claude Code memory was updated or deleted on Anthropic servers.



ClaudeCodeUserPluginsUpdated object{ type: "claude_code_user_plugins_updated", actor, deleted_all, 10 more }



A user's Claude Code plugin selections — which plugins are installed and enabled — were updated on Anthropic servers.



ClaudeCodeUserSettingsUpdated object{ type: "claude_code_user_settings_updated", actor, deleted_all, 10 more }



A user's synced Claude Code settings were updated or deleted on Anthropic servers.



ClaudeEnterpriseUpgradeCreditUpdated object{ type: "claude_enterprise_upgrade_credit_updated", action, actor, 4 more }



An organization admin cancelled, or turned back on, the monthly usage credit the organization receives for upgrading from the Team plan to the Enterprise plan, together with the recurring monthly charge that accompanies it.



ClaudeFileAccessFailed object{ type: "claude_file_access_failed", actor, claude_file_id, 7 more }



A user was denied access to a file in Claude.ai.



ClaudeFileExported object{ type: "claude_file_exported", actor, export_destination, 7 more }



A file was exported from Claude to an external storage destination.



ClaudeFileViewed object{ type: "claude_file_viewed", actor, claude_file_id, 7 more }



A user viewed a file in Claude.ai.



ClaudePluginArchiveAccessed object{ type: "claude_plugin_archive_accessed", actor, marketplace_id, 7 more }



A version archive of a member-owned plugin, containing that member's own files, was downloaded.



ClaudeProjectSyncSourceCreated object{ type: "claude_project_sync_source_created", actor, claude_project_id, 7 more }



A sync source was connected to a Claude project's knowledge base.



ClaudeProjectSyncSourceDeleted object{ type: "claude_project_sync_source_deleted", actor, claude_project_id, 6 more }



A sync source was disconnected from a Claude project's knowledge base.



ClaudeProjectSyncSourceUpdated object{ type: "claude_project_sync_source_updated", actor, claude_project_id, 8 more }



A Claude project sync source's configuration was updated.



ClaudeUserSeatTierUpdated object{ type: "claude_user_seat_tier_updated", actor, user_email, 7 more }



An organization member's seat tier was changed. A null `previous_seat_tier` means the member previously had no seat assigned; a null `current_seat_tier` means the seat was removed.



CliPluginExecPolicyUpdated object{ type: "cli_plugin_exec_policy_updated", actor, cli_name, 10 more }



Admin set or cleared the per-op permission ceiling for a plugin CLI.



ClaudeCommandCreated object{ type: "claude_command_created", actor, id, 5 more }



Command was created.



ClaudeCommandDeleted object{ type: "claude_command_deleted", actor, id, 5 more }



Command was deleted.



ClaudeCommandReplaced object{ type: "claude_command_replaced", actor, id, 5 more }



Command was replaced.



ComplianceAPIAccessed object{ type: "compliance_api_accessed", actor, request_id, 8 more }



Logging event auto-generated for each compliance API request.



CoworkSessionUpdated object{ type: "cowork_session_updated", actor, cowork_session_id, 5 more }



A Cowork session was updated.



DesignProjectArtifactPublished object{ type: "design_project_artifact_published", actor, design_project_id, 6 more }



A Claude Design project's content was published as a claude.ai artifact, making a snapshot of one of its files viewable outside the project's sharing settings.



DesignProjectCreated object{ type: "design_project_created", actor, creation_method, 7 more }



A Claude Design project was created.



DesignProjectDeleted object{ type: "design_project_deleted", actor, design_project_id, 4 more }



A Claude Design project was deleted.



DesignProjectMemberAdded object{ type: "design_project_member_added", actor, design_project_id, 8 more }



A member was granted access to a Claude Design project.



DesignProjectMemberRemoved object{ type: "design_project_member_removed", actor, design_project_id, 7 more }



A member's access to a Claude Design project was revoked.



DesignProjectMemberRoleUpdated object{ type: "design_project_member_role_updated", actor, design_project_id, 9 more }



A Claude Design project member's role was changed.



DesignProjectPublished object{ type: "design_project_published", actor, design_project_id, 5 more }



A Claude Design template or design system was published, making it discoverable by everyone in its organization.



DesignProjectSharingUpdated object{ type: "design_project_sharing_updated", actor, design_project_id, 9 more }



A Claude Design project's link-sharing settings were changed — who the project's link works for, and what people opening it through the link may do. Access granted to individual members is reported separately (see design_project_member_added).



DesignProjectUnpublished object{ type: "design_project_unpublished", actor, design_project_id, 5 more }



A Claude Design template or design system was unpublished, removing it from its organization's shared gallery.



DesignProjectUpdated object{ type: "design_project_updated", actor, design_project_id, 6 more }



A Claude Design project's metadata was updated.



DesignProjectVersionRestored object{ type: "design_project_version_restored", actor, design_project_id, 5 more }



A Claude Design project's working tree was rolled back to a previously saved version, replacing its current files with that version's files.



DesignProjectViewed object{ type: "design_project_viewed", actor, design_project_id, 7 more }



A Claude Design project's content was read. The surface field records which kind of read — a project open, a full-content read, a single-file read, a saved-version read, or an export request. The actor is the reader.

This activity type is retired: project content reads are no longer recorded. Events of this type may still appear in feeds for reads that occurred while it was active.



DesktopExtensionAllowlisted object{ type: "desktop_extension_allowlisted", actor, extension_id, 4 more }



A desktop extension was added to an org's allowlist.



DesktopExtensionBlocklisted object{ type: "desktop_extension_blocklisted", actor, extension_id, 4 more }



A desktop extension was added to the global blocklist.



DesktopExtensionDeleted object{ type: "desktop_extension_deleted", actor, extension_id, 5 more }



A desktop extension was deleted, either globally by an admin or org-scoped by an org owner.



DesktopExtensionRemovedFromAllowlist object{ type: "desktop_extension_removed_from_allowlist", actor, extension_id, 4 more }



A desktop extension was removed from an org's allowlist.



DesktopExtensionUnblocked object{ type: "desktop_extension_unblocked", actor, extension_id, 4 more }



A desktop extension was removed from the global blocklist.



DesktopExtensionUploaded object{ type: "desktop_extension_uploaded", actor, extension_id, 5 more }



A desktop extension was uploaded, either globally by an admin or org-scoped by an org owner.



DesktopExtensionVersionUploaded object{ type: "desktop_extension_version_uploaded", actor, extension_id, 5 more }



A new version of an existing org-owned desktop extension was uploaded.



InferenceHooksConfigDeleted object{ type: "inference_hooks_config_deleted", actor, id, 3 more }



Inference hooks configuration was removed for the organization.



InferenceHooksConfigUpdated object{ type: "inference_hooks_config_updated", actor, enabled, 15 more }



Inference hooks configuration was created or updated for the organization.



InferenceHooksSigningSecretGenerated object{ type: "inference_hooks_signing_secret_generated", actor, rotated, 4 more }



A request signing secret was generated for the organization's Inference hooks configuration.



DomainClaimInitiated object{ type: "domain_claim_initiated", actor, id, 3 more }



Domain capture claim initiated over personal accounts on verified domains.



EndUserInviteRequested object{ type: "end_user_invite_requested", actor, invitee_email, 4 more }



Non-admin member submitted an invite request for a new org member.



ExtraUsageBillingEnabled object{ type: "extra_usage_billing_enabled", actor, id, 3 more }



Usage credit billing was enabled for an organization.



ExtraUsageCreditGranted object{ type: "extra_usage_credit_granted", actor, id, 3 more }



A promotional usage credit grant was claimed.



ExtraUsageSpendLimitCreated object{ type: "extra_usage_spend_limit_created", actor, id, 8 more }



Usage credit spend limit was created.



ExtraUsageSpendLimitDeleted object{ type: "extra_usage_spend_limit_deleted", actor, id, 5 more }



Usage credit spend limit was deleted.



ExtraUsageSpendLimitIncreaseRequestApproved object{ type: "extra_usage_spend_limit_increase_request_approved", actor, id, 7 more }



A usage credit spend limit increase request was approved.



ExtraUsageSpendLimitIncreaseRequestDenied object{ type: "extra_usage_spend_limit_increase_request_denied", actor, id, 5 more }



A usage credit spend limit increase request was denied.



ExtraUsageSpendLimitUpdated object{ type: "extra_usage_spend_limit_updated", actor, id, 8 more }



Usage credit spend limit was updated.



ClaudeFileDeleted object{ type: "claude_file_deleted", actor, claude_file_id, 5 more }



A file was deleted.



ClaudeFileUploaded object{ type: "claude_file_uploaded", actor, claude_file_id, 7 more }



A file was uploaded.



GheConfigurationCreated object{ type: "ghe_configuration_created", actor, ghe_configuration_id, 7 more }



Admin created a GHE configuration.



GheConfigurationDeleted object{ type: "ghe_configuration_deleted", actor, ghe_configuration_id, 7 more }



Admin deleted a GHE configuration.



GheConfigurationUpdated object{ type: "ghe_configuration_updated", actor, ghe_configuration_id, 20 more }



Admin updated a GHE configuration. Previous/new field pairs are recorded only for settings that changed in the update; secret credentials are never recorded, only whether they were replaced.



GheUserConnected object{ type: "ghe_user_connected", actor, id, 4 more }



User connected to a GHE instance.



GheUserDisconnected object{ type: "ghe_user_disconnected", actor, id, 4 more }



User disconnected from a GHE instance.



GheWebhookSignatureInvalid object{ type: "ghe_webhook_signature_invalid", actor, ghe_configuration_id, 4 more }



Webhook signature validation failed.



ClaudeGitHubIntegrationCreated object{ type: "claude_github_integration_created", actor, integration_id, 8 more }



A GitHub integration was enabled for the organization.



ClaudeGitHubIntegrationDeleted object{ type: "claude_github_integration_deleted", actor, integration_id, 8 more }



A GitHub integration was disabled for the organization.



ClaudeGitHubIntegrationUpdated object{ type: "claude_github_integration_updated", actor, integration_id, 6 more }



A GitHub integration's configuration was updated.






An installation of the Claude GitHub App (a GitHub organization or user account where the App is installed) was linked to the organization, letting the organization's Claude Code features act on that GitHub account's repositories.






An installation of the Claude GitHub App was unlinked from the organization, so the organization's Claude Code features can no longer act on that GitHub account's repositories through it.






A user attempted to import a personal GitHub access token for use with Claude Code. The `result` field indicates the outcome of the import (imported, rejected, or failed).



GitlabConfigurationCreated object{ type: "gitlab_configuration_created", actor, gitlab_configuration_id, 7 more }



An organization admin created a self-managed GitLab configuration for syncing plugin marketplaces.



GitlabConfigurationDeleted object{ type: "gitlab_configuration_deleted", actor, gitlab_configuration_id, 7 more }



An organization admin deleted a self-managed GitLab configuration.



GitlabConfigurationUpdated object{ type: "gitlab_configuration_updated", actor, gitlab_configuration_id, 13 more }



An organization admin updated a self-managed GitLab configuration. Previous/new field pairs are recorded only for settings that changed in the update; secret credentials are never recorded, only whether they were replaced.



ClaudeGdriveIntegrationCreated object{ type: "claude_gdrive_integration_created", actor, integration_id, 5 more }



A Google Drive integration was enabled for the organization.



ClaudeGdriveIntegrationDeleted object{ type: "claude_gdrive_integration_deleted", actor, integration_id, 5 more }



A Google Drive integration was disabled for the organization.



ClaudeGdriveIntegrationUpdated object{ type: "claude_gdrive_integration_updated", actor, integration_id, 5 more }



A Google Drive integration's configuration was updated.



GroupCreated object{ type: "group_created", actor, group_id, 5 more }



A group was created (RBAC admin or SCIM provisioning).



GroupDeleted object{ type: "group_deleted", actor, group_id, 4 more }



A group was deleted (RBAC admin or SCIM provisioning).



GroupListViewed object{ type: "group_list_viewed", actor, id, 3 more }



Admin viewed the list of RBAC groups.



GroupMemberAdded object{ type: "group_member_added", actor, group_id, 5 more }



One or more members were added to a group.



GroupMemberAdditionFailed object{ type: "group_member_addition_failed", actor, group_id, 5 more }



A request to add members to a group failed. Some of the requested members may have been added before the failure.



GroupMemberListViewed object{ type: "group_member_list_viewed", actor, group_id, 4 more }



Admin viewed the members of an RBAC group.



GroupMemberRemovalFailed object{ type: "group_member_removal_failed", actor, group_id, 5 more }



A request to remove members from a group failed. Some of the requested members may have been removed before the failure.



GroupMemberRemoved object{ type: "group_member_removed", actor, group_id, 5 more }



One or more members were removed from a group.



GroupProjectSharesRevoked object{ type: "group_project_shares_revoked", actor, group_id, 6 more }



An RBAC group's project shares in one organization were revoked in bulk.



GroupSkillSharesRevoked object{ type: "group_skill_shares_revoked", actor, group_id, 7 more }



An RBAC group's skill shares in one organization were revoked in bulk.



GroupUpdated object{ type: "group_updated", actor, group_id, 4 more }



A group was updated (RBAC admin or SCIM provisioning).



GroupViewed object{ type: "group_viewed", actor, group_id, 4 more }



A group was viewed.



GroupVisibilityUpdated object{ type: "group_visibility_updated", actor, group_id, 6 more }



An RBAC group's visibility policy was updated.



InferenceHooksCircuitBreakerTripped object{ type: "inference_hooks_circuit_breaker_tripped", actor, fail_mode, 6 more }



The organization's Inference hooks circuit breaker tripped automatically: calls to the organization's Inference hooks endpoint crossed a failure threshold, and inspection was suspended to protect live traffic. While tripped, requests are handled according to the organization's failure handling setting — allowed through uninspected (fail open) or rejected (fail closed) — and no per-request Inference hooks activities are recorded. The tripped state persists until an administrator re-enables Inference hooks inspection (or explicitly resets the circuit breaker).



InferenceHooksRequestDenied object{ type: "inference_hooks_request_denied", actor, id, 7 more }



Inference hooks inspection denied a request. The request was blocked and no model response was produced.



InferenceHooksRequestFailedOpen object{ type: "inference_hooks_request_failed_open", actor, reason, 7 more }



A request proceeded without Inference hooks inspection because a verdict could not be obtained and the organization's Inference hooks configuration is set to fail open.



IntegrationUserConnected object{ type: "integration_user_connected", actor, id, 7 more }



User connected to an integration.



IntegrationUserDisconnected object{ type: "integration_user_disconnected", actor, id, 6 more }



User disconnected from an integration.



InvoiceCollectionMethodUpdated object{ type: "invoice_collection_method_updated", actor, id, 4 more }



Invoice collection method was changed.



UserLoggedOut object{ type: "user_logged_out", actor, id, 3 more }



A user signed out of one or all sessions.



LtiLaunchInitiated object{ type: "lti_launch_initiated", actor, id, 3 more }



LTI launch was initiated.



LtiLaunchSuccess object{ type: "lti_launch_success", actor, id, 3 more }



LTI launch completed successfully.



LtiPlatformCreated object{ type: "lti_platform_created", actor, lti_platform_id, 5 more }



Anthropic staff created an LTI platform integration on behalf of an org.



LtiPlatformUpdated object{ type: "lti_platform_updated", actor, lti_platform_id, 5 more }



Anthropic staff updated an LTI platform integration on behalf of an org.



MagicLinkLoginFailed object{ type: "magic_link_login_failed", actor, id, 3 more }



A magic link sign-in attempt failed.



MagicLinkLoginInitiated object{ type: "magic_link_login_initiated", actor, id, 3 more }



A user requested a magic link sign-in email.



MagicLinkLoginSucceeded object{ type: "magic_link_login_succeeded", actor, id, 5 more }



A user successfully signed in with a magic link email.



ManagedOrganizationSetupCompleted object{ type: "managed_organization_setup_completed", actor, id, 3 more }



Managed (AWS Marketplace) organization setup was completed.



MarketplaceCreated object{ type: "marketplace_created", actor, marketplace_id, 5 more }



Admin created an organization marketplace.



MarketplaceDeleted object{ type: "marketplace_deleted", actor, marketplace_id, 4 more }



Admin deleted an organization marketplace.



MarketplaceUpdated object{ type: "marketplace_updated", actor, marketplace_id, 5 more }



Admin updated an organization marketplace.



MarketplaceWebhookDeleted object{ type: "marketplace_webhook_deleted", actor, marketplace_id, 4 more }



Admin removed the GitHub push webhook for a marketplace.



MarketplaceWebhookProvisioned object{ type: "marketplace_webhook_provisioned", actor, marketplace_id, 5 more }



Admin provisioned a GitHub push webhook for a marketplace.



McpDirectoryServerPublished object{ type: "mcp_directory_server_published", actor, mcp_directory_server_id, 5 more }



The organization published its approved MCP directory listing.



McpServerCreated object{ type: "mcp_server_created", actor, mcp_server_id, 5 more }



An MCP server was added to the organization.



McpServerDeleted object{ type: "mcp_server_deleted", actor, mcp_server_id, 5 more }



An MCP server was removed from the organization.



McpServerManagedAuthTokenExchanged object{ type: "mcp_server_managed_auth_token_exchanged", actor, managed_auth_mode, 12 more }



A user attempted to obtain an access token for an MCP server via enterprise managed authorization. This event reports the outcomes of attempted token exchanges. Repeated failures with the same cause may be reported once until the cause changes, and requests refused before a token exchange is attempted are not reported, except the "connector_scope_not_granted" and "identity_assertion_refused" failures described under error_type.



McpServerManagedAuthUpdated object{ type: "mcp_server_managed_auth_updated", actor, mcp_server_id, 15 more }



An MCP server's enterprise managed authorization settings were set, changed, or cleared, including when they were supplied while the server was being added or edited. Fields without a "previous\_" prefix describe the settings after the change and are null when the server has no managed authorization settings afterwards; "previous\_" fields describe the settings before the change and are null when the server had none before (always the case for a newly added server).



McpServerUpdated object{ type: "mcp_server_updated", actor, mcp_server_id, 5 more }



An MCP server's configuration was updated.



McpToolPolicyUpdated object{ type: "mcp_tool_policy_updated", actor, mcp_server_id, 7 more }



The permission restriction for an MCP tool was set or cleared.



OrgAnalyticsAPICapabilityUpdated object{ type: "org_analytics_api_capability_updated", actor, id, 5 more }



Organization analytics_api capability was enabled or disabled.



OrgBulkDeleteInitiated object{ type: "org_bulk_delete_initiated", actor, id, 3 more }



Organization bulk deletion was initiated.



OrgCapabilityGrantAdded object{ type: "org_capability_grant_added", actor, grant_type, 6 more }



A capability grant was added to a workspace or role.



OrgCapabilityGrantRemoved object{ type: "org_capability_grant_removed", actor, grant_type, 6 more }



A capability grant was removed from a workspace or role.



OrgClaudeCodeDataSharingDisabled object{ type: "org_claude_code_data_sharing_disabled", actor, id, 5 more }



Organization Claude Code data sharing was disabled.



OrgClaudeCodeDataSharingEnabled object{ type: "org_claude_code_data_sharing_enabled", actor, id, 5 more }



Organization Claude Code data sharing was enabled.



OrgClaudeCodeDesktopDisabled object{ type: "org_claude_code_desktop_disabled", actor, id, 5 more }



Organization Claude Code Desktop was disabled.



OrgClaudeCodeDesktopEnabled object{ type: "org_claude_code_desktop_enabled", actor, id, 5 more }



Organization Claude Code Desktop was enabled.



OrgClaudeCodeZeroDataRetentionDisabled object{ type: "org_claude_code_zero_data_retention_disabled", actor, id, 3 more }



A primary owner disabled zero data retention for Claude Code, so Claude Code content is retained according to the organization's data retention settings.



OrgComplianceAPISettingsUpdated object{ type: "org_compliance_api_settings_updated", actor, id, 5 more }



Organization compliance API settings were updated.



OrgConnectorDomainGuardUpdated object{ type: "org_connector_domain_guard_updated", actor, enforced, 4 more }



Enterprise admin changed whether connectors are restricted to verified domains.



OrgCoworkActWithoutAskingModeDisabled object{ type: "org_cowork_act_without_asking_mode_disabled", actor, id, 3 more }



The "Act without asking" mode in Cowork was disabled for the organization, so members can no longer let Claude act without asking for approval.



OrgCoworkActWithoutAskingModeEnabled object{ type: "org_cowork_act_without_asking_mode_enabled", actor, id, 3 more }



The "Act without asking" mode in Cowork was enabled for the organization, allowing members to let Claude act without asking for approval.



OrgCoworkAgentDisabled object{ type: "org_cowork_agent_disabled", actor, id, 5 more }



Organization Cowork Agent was disabled.



OrgCoworkAgentEnabled object{ type: "org_cowork_agent_enabled", actor, id, 5 more }



Organization Cowork Agent was enabled.



OrgCoworkAutoModeDisabled object{ type: "org_cowork_auto_mode_disabled", actor, id, 3 more }



The "Auto" permission mode in Cowork was disabled for the organization, so members can no longer let Claude approve its own actions after a safety check.



OrgCoworkAutoModeEnabled object{ type: "org_cowork_auto_mode_enabled", actor, id, 3 more }



The "Auto" permission mode in Cowork was enabled for the organization, allowing members to let Claude approve its own actions after a safety check.



OrgCoworkBrowserPaneDisabled object{ type: "org_cowork_browser_pane_disabled", actor, id, 3 more }



The in-app browser in Cowork was disabled for the organization, so Claude can no longer open or use websites in a browser pane during members' Cowork sessions.



OrgCoworkBrowserPaneEnabled object{ type: "org_cowork_browser_pane_enabled", actor, id, 3 more }



The in-app browser in Cowork was enabled for the organization, letting Claude open and use websites in a browser pane during members' Cowork sessions.



OrgCoworkDisabled object{ type: "org_cowork_disabled", actor, id, 5 more }



Organization cowork was disabled.



OrgCoworkEnabled object{ type: "org_cowork_enabled", actor, id, 5 more }



Organization cowork was enabled.



OrgCoworkMcpAlwaysAllowDisabled object{ type: "org_cowork_mcp_always_allow_disabled", actor, id, 3 more }



The "Always allow" option for connector tools in Cowork was disabled for the organization, so each use of a connector tool that can make changes requires approval. Read-only connector tools are not affected by this setting.



OrgCoworkMcpAlwaysAllowEnabled object{ type: "org_cowork_mcp_always_allow_enabled", actor, id, 3 more }



The "Always allow" option for connector tools in Cowork was enabled for the organization, letting members approve a connector tool that can make changes once and allow its later uses automatically. Read-only connector tools are not affected by this setting.



OrgCoworkOtlpSettingsUpdated object{ type: "org_cowork_otlp_settings_updated", actor, id, 12 more }



The organization's Cowork OpenTelemetry monitoring export settings were updated.



OrgCoworkRemoteDisabled object{ type: "org_cowork_remote_disabled", actor, id, 3 more }



Running Cowork in the cloud was disabled for the organization, so members can no longer run Cowork sessions in Anthropic-hosted remote environments.



OrgCoworkRemoteEnabled object{ type: "org_cowork_remote_enabled", actor, id, 3 more }



Running Cowork in the cloud was enabled for the organization, allowing members to run Cowork sessions in Anthropic-hosted remote environments.



OrgCreationBlocked object{ type: "org_creation_blocked", actor, id, 4 more }



Organization creation was blocked.



OrgDataExportAccessed object{ type: "org_data_export_accessed", actor, id, 4 more }



Organization data export file was accessed/downloaded via signed URL.



OrgDataExportCompleted object{ type: "org_data_export_completed", actor, id, 4 more }



Organization data export was completed.



OrgDataExportStarted object{ type: "org_data_export_started", actor, id, 5 more }



Organization data export was started.



OrgDataResidencyUpdated object{ type: "org_data_residency_updated", actor, id, 4 more }



The organization's inference data residency settings were updated.



OrgDeletedViaBulk object{ type: "org_deleted_via_bulk", actor, id, 3 more }



Organization was deleted via bulk operation.



OrgDeletionRequested object{ type: "org_deletion_requested", actor, id, 3 more }



Organization deletion was requested.



OrgDirectoryResyncCompleted object{ type: "org_directory_resync_completed", actor, resync_uuid, 4 more }



Organization directory resync completed successfully.



OrgDirectoryResyncFailed object{ type: "org_directory_resync_failed", actor, resync_uuid, 4 more }



Organization directory resync failed.



OrgDirectoryResyncStarted object{ type: "org_directory_resync_started", actor, resync_uuid, 5 more }



Organization directory resync was started asynchronously.



OrgDirectorySyncActivated object{ type: "org_directory_sync_activated", actor, id, 3 more }



Organization directory sync was activated.



OrgDirectorySyncAddInitiated object{ type: "org_directory_sync_add_initiated", actor, id, 3 more }



Organization directory sync setup was initiated.



OrgDirectorySyncDeleted object{ type: "org_directory_sync_deleted", actor, id, 3 more }



Organization directory sync was deleted.



OrgDiscoverabilityDisabled object{ type: "org_discoverability_disabled", actor, id, 3 more }



Admin disabled organization discoverability.



OrgDiscoverabilityEnabled object{ type: "org_discoverability_enabled", actor, id, 3 more }



Admin enabled organization discoverability.



OrgDiscoverabilitySettingsUpdated object{ type: "org_discoverability_settings_updated", actor, id, 3 more }



Admin updated organization discoverability settings.



OrgDomainAddInitiated object{ type: "org_domain_add_initiated", actor, id, 3 more }



Organization domain verification was initiated.



OrgDomainRemoved object{ type: "org_domain_removed", actor, id, 4 more }



Organization domain was removed.



OrgDomainVerified object{ type: "org_domain_verified", actor, id, 4 more }



Organization domain was verified.



OrgExternalKeyCreated object{ type: "org_external_key_created", actor, external_key_id, 5 more }



A CMEK external key config was created.



OrgExternalKeyDeleted object{ type: "org_external_key_deleted", actor, external_key_id, 4 more }



A CMEK external key config was deleted.



OrgExternalKeyUpdated object{ type: "org_external_key_updated", actor, external_key_id, 5 more }



A CMEK external key config was updated.



OrgExternalKeyValidated object{ type: "org_external_key_validated", actor, external_key_id, 5 more }



A CMEK external key config was validated against the customer's KMS.



OrgHipaaSelfServeEnabled object{ type: "org_hipaa_self_serve_enabled", actor, baa_content_hash, 6 more }



A primary owner click-accepted the BAA and enabled HIPAA protections for the organization via the self-serve flow.



OrgIPRestrictionCreated object{ type: "org_ip_restriction_created", actor, id, 3 more }



Organization IP restriction was created.



OrgIPRestrictionDeleted object{ type: "org_ip_restriction_deleted", actor, id, 3 more }



Organization IP restriction was deleted.



OrgIPRestrictionUpdated object{ type: "org_ip_restriction_updated", actor, id, 3 more }



Organization IP restriction was updated.



OrgInviteLinkDisabled object{ type: "org_invite_link_disabled", actor, id, 3 more }



Organization invite link was disabled.



OrgInviteLinkGenerated object{ type: "org_invite_link_generated", actor, id, 3 more }



Organization invite link was generated.



OrgInviteLinkRegenerated object{ type: "org_invite_link_regenerated", actor, id, 3 more }



Organization invite link was regenerated (previous link invalidated).



OrgInviteViewed object{ type: "org_invite_viewed", actor, invite_id, 4 more }



An organization invite was viewed.



OrgInvitesListed object{ type: "org_invites_listed", actor, id, 3 more }



Organization invites were listed.



OrgJoinProposalDecided object{ type: "org_join_proposal_decided", actor, approved, 4 more }



Approve or reject decision on a parent-org join proposal.



OrgJoinRequestApproved object{ type: "org_join_request_approved", actor, id, 3 more }



Admin approved a join request.



OrgJoinRequestCreated object{ type: "org_join_request_created", actor, id, 3 more }



User requested to join an organization.



OrgJoinRequestDismissed object{ type: "org_join_request_dismissed", actor, id, 3 more }



Admin dismissed a join request.



OrgJoinRequestInstantApproved object{ type: "org_join_request_instant_approved", actor, id, 3 more }



Join request was instantly approved.



OrgJoinRequestsBulkDismissed object{ type: "org_join_requests_bulk_dismissed", actor, id, 3 more }



Admin bulk-dismissed join requests.



OrgMagicLinkSecondFactorToggled object{ type: "org_magic_link_second_factor_toggled", actor, enabled, 4 more }



Organization magic link second factor was toggled.



OrgMemberInvitesDisabled object{ type: "org_member_invites_disabled", actor, id, 3 more }



Admin disabled member invites for the organization.



OrgMemberInvitesEnabled object{ type: "org_member_invites_enabled", actor, id, 3 more }



Admin enabled member invites for the organization.



OrgMembersExported object{ type: "org_members_exported", actor, id, 3 more }



Organization members list was exported as CSV.



OrgModelDefaultUpdated object{ type: "org_model_default_updated", action, actor, 9 more }



An organization or role default model setting was changed by an administrator.



OrgParentJoinProposalCreated object{ type: "org_parent_join_proposal_created", actor, id, 3 more }



Organization parent join proposal was created.



OrgParentSearchPerformed object{ type: "org_parent_search_performed", actor, id, 3 more }



Organization parent search was performed.



OrgSSOAddInitiated object{ type: "org_sso_add_initiated", actor, id, 3 more }



Organization SSO setup was initiated.



OrgSSOConnectionActivated object{ type: "org_sso_connection_activated", actor, id, 5 more }



Organization SSO connection was activated.



OrgSSOConnectionDeactivated object{ type: "org_sso_connection_deactivated", actor, id, 4 more }



Organization SSO connection was deactivated.



OrgSSOConnectionDeleted object{ type: "org_sso_connection_deleted", actor, id, 4 more }



Organization SSO connection was deleted.



OrgSSOGroupRoleMappingsUpdated object{ type: "org_sso_group_role_mappings_updated", actor, id, 3 more }



Organization SSO group role mappings were updated.



OrgSSOProvisioningModeChanged object{ type: "org_sso_provisioning_mode_changed", actor, id, 5 more }



Organization SSO provisioning mode was changed.



OrgSSOScimWelcomeEmailToggled object{ type: "org_sso_scim_welcome_email_toggled", actor, enabled, 5 more }



Organization SCIM-provisioned welcome email was toggled.



OrgSSOSeatTierAssignmentToggled object{ type: "org_sso_seat_tier_assignment_toggled", actor, enabled, 5 more }



Organization SSO seat tier assignment was toggled.



OrgSSOSeatTierMappingsUpdated object{ type: "org_sso_seat_tier_mappings_updated", actor, id, 5 more }



Organization SSO seat tier mappings were updated.



OrgSSOToggled object{ type: "org_sso_toggled", actor, enabled, 4 more }



Organization SSO was toggled on or off.



OrgSyncDeletingSynchronizedFilesStarted object{ type: "org_sync_deleting_synchronized_files_started", actor, id, 3 more }



Organization started deleting synchronized files.



OrgSyncSynchronizedFilesDeleted object{ type: "org_sync_synchronized_files_deleted", actor, id, 3 more }



Organization synchronized files were deleted.



OrgTaintAdded object{ type: "org_taint_added", actor, id, 5 more }



A taint was added to an organization.



OrgTaintRemoved object{ type: "org_taint_removed", actor, id, 4 more }



A taint was removed from an organization.



OrgUserDeleted object{ type: "org_user_deleted", actor, id, 5 more }



User was removed from organization.



OrgUserInviteAccepted object{ type: "org_user_invite_accepted", actor, id, 5 more }



Organization user invite was accepted.



OrgUserInviteDeleted object{ type: "org_user_invite_deleted", actor, id, 4 more }



Organization user invite was deleted.



OrgUserInviteReSent object{ type: "org_user_invite_re_sent", actor, id, 6 more }



Organization user invite was re-sent.



OrgUserInviteRejected object{ type: "org_user_invite_rejected", actor, id, 4 more }



Organization user invite was rejected.



OrgUserInviteSent object{ type: "org_user_invite_sent", actor, id, 7 more }



Organization user invite was sent.



OrgUserLeft object{ type: "org_user_left", actor, id, 4 more }



User removed themselves from organization.



OrgUserSharesRetained object{ type: "org_user_shares_retained", actor, resource_count, 11 more }



A member left or was removed from the organization while projects, skills, plugins, or chats they had shared were still shared, and those shares were kept.



OrgUserTrustedDevicesRevoked object{ type: "org_user_trusted_devices_revoked", actor, completed, 7 more }



An organization admin revoked a member's trusted devices and signed the member out of all active sessions.



OrgUserViewed object{ type: "org_user_viewed", actor, user_id, 4 more }



An organization user was viewed.



OrgUsersListed object{ type: "org_users_listed", actor, id, 3 more }



Organization users were listed.



OrgWorkAcrossAppsDisabled object{ type: "org_work_across_apps_disabled", actor, id, 5 more }



The organization's "Let Claude work across apps" setting was turned off.



OrgWorkAcrossAppsEnabled object{ type: "org_work_across_apps_enabled", actor, id, 5 more }



The organization's "Let Claude work across apps" setting was turned on.



OrganizationAddressUpdated object{ type: "organization_address_updated", actor, id, 7 more }



The organization's billing or shipping address was updated.



OrganizationIconDeleted object{ type: "organization_icon_deleted", actor, id, 3 more }



Organization's custom icon deleted.



OrganizationIconUpdated object{ type: "organization_icon_updated", actor, id, 3 more }



Organization's custom icon uploaded or replaced.



ClaudeOrganizationSettingsUpdated object{ type: "claude_organization_settings_updated", actor, updates, 4 more }



Organization settings were updated.



OwnedProjectsAccessRestored object{ type: "owned_projects_access_restored", actor, id, 4 more }



Access to owned projects was restored.



PaymentMethodUpdated object{ type: "payment_method_updated", actor, id, 3 more }



The organization's default payment method was updated.



PendingShareCreated object{ type: "pending_share_created", actor, invitee_email, 7 more }



A pending share of a project or skill was created for an email address that is not yet an organization member.



PendingShareRevoked object{ type: "pending_share_revoked", actor, invitee_email, 6 more }



A pending share of a project or skill was revoked before the invitee joined the organization.



PhoneCodeSent object{ type: "phone_code_sent", actor, id, 3 more }



User requested a phone verification code.



PhoneCodeVerified object{ type: "phone_code_verified", actor, id, 3 more }



User successfully verified their phone code.



PlatformAgentArchived object{ type: "platform_agent_archived", actor, agent_id, 5 more }



An agent was archived on the API platform.



PlatformAgentCreated object{ type: "platform_agent_created", actor, agent_id, 5 more }



An agent was created on the API platform.



PlatformAgentDeleted object{ type: "platform_agent_deleted", actor, agent_id, 5 more }



An agent was deleted from the API platform.



PlatformAgentDeploymentArchived object{ type: "platform_agent_deployment_archived", actor, deployment_id, 5 more }



An agent deployment was archived on the API platform.



PlatformAgentDeploymentCreated object{ type: "platform_agent_deployment_created", actor, deployment_id, 5 more }



An agent deployment was created on the API platform.



PlatformAgentDeploymentDeleted object{ type: "platform_agent_deployment_deleted", actor, deployment_id, 5 more }



An agent deployment was deleted from the API platform.



PlatformAgentDeploymentPaused object{ type: "platform_agent_deployment_paused", actor, deployment_id, 5 more }



An agent deployment was paused on the API platform.



PlatformAgentDeploymentRunTriggered object{ type: "platform_agent_deployment_run_triggered", actor, deployment_id, 5 more }



An agent deployment was run on demand on the API platform.



PlatformAgentDeploymentUnpaused object{ type: "platform_agent_deployment_unpaused", actor, deployment_id, 5 more }



An agent deployment was resumed on the API platform.



PlatformAgentDeploymentUpdated object{ type: "platform_agent_deployment_updated", actor, deployment_id, 5 more }



An agent deployment was updated on the API platform.



PlatformAgentSessionArchived object{ type: "platform_agent_session_archived", actor, session_id, 5 more }



An agent session was archived on the API platform.



PlatformAgentSessionCreated object{ type: "platform_agent_session_created", actor, session_id, 5 more }



An agent session was created on the API platform.



PlatformAgentSessionDeleted object{ type: "platform_agent_session_deleted", actor, session_id, 5 more }



An agent session was deleted from the API platform.



PlatformAgentSessionResourceAdded object{ type: "platform_agent_session_resource_added", actor, resource_id, 6 more }



A resource was attached to an agent session.



PlatformAgentSessionResourceDeleted object{ type: "platform_agent_session_resource_deleted", actor, resource_id, 6 more }



A resource attached to an agent session was removed.



PlatformAgentSessionResourceUpdated object{ type: "platform_agent_session_resource_updated", actor, resource_id, 6 more }



A resource attached to an agent session was updated.



PlatformAgentSessionThreadArchived object{ type: "platform_agent_session_thread_archived", actor, session_id, 6 more }



A thread within an agent session was archived.



PlatformAgentSessionUpdated object{ type: "platform_agent_session_updated", actor, session_id, 5 more }



An agent session was updated on the API platform.



PlatformAgentUpdated object{ type: "platform_agent_updated", actor, agent_id, 5 more }



An agent was updated on the API platform.



PlatformAPIKeyCreated object{ type: "platform_api_key_created", actor, api_key_id, 7 more }



An API key was created.



PlatformAPIKeyUpdated object{ type: "platform_api_key_updated", actor, api_key_id, 5 more }



An API key was updated.



PlatformAppAttestAuthentication object{ type: "platform_app_attest_authentication", actor, id, 6 more }



An attested mobile device attempted to exchange an Apple App Attest assertion for Anthropic API credentials.



PlatformBillingUpgradedToPrepaid object{ type: "platform_billing_upgraded_to_prepaid", actor, previous_billing_type, 4 more }



The organization's API billing was upgraded to the prepaid plan.



PlatformClearanceWorkspaceProgramRequestCleared object{ type: "platform_clearance_workspace_program_request_cleared", actor, program_slug, 5 more }



A workspace's clearance program assignment was removed.



PlatformClearanceWorkspaceProgramRequestSet object{ type: "platform_clearance_workspace_program_request_set", actor, opt_decision, 6 more }



A workspace's clearance program assignment was created or updated.



PlatformCostReportViewed object{ type: "platform_cost_report_viewed", actor, id, 3 more }



The cost report was viewed.



PlatformDreamArchived object{ type: "platform_dream_archived", actor, dream_id, 5 more }



A Dream (asynchronous memory-consolidation job) was archived.



PlatformDreamCancelled object{ type: "platform_dream_cancelled", actor, dream_id, 5 more }



A Dream (asynchronous memory-consolidation job) was cancelled before it completed.



PlatformDreamCreated object{ type: "platform_dream_created", actor, dream_id, 5 more }



A Dream (asynchronous memory-consolidation job) was created.



PlatformFederatedAuthentication object{ type: "platform_federated_authentication", actor, id, 7 more }



A federated workload identity attempted to exchange an OIDC token for Anthropic API credentials.



PlatformFederationIssuerArchived object{ type: "platform_federation_issuer_archived", actor, federation_issuer_id, 4 more }



An OIDC federation issuer was archived.



PlatformFederationIssuerCreated object{ type: "platform_federation_issuer_created", actor, federation_issuer_id, 8 more }



An OIDC federation issuer was created, registering an external identity provider that federation rules can trust for workload authentication.



PlatformFederationIssuerUpdated object{ type: "platform_federation_issuer_updated", actor, federation_issuer_id, 5 more }



An OIDC federation issuer was updated.



PlatformFederationRuleArchived object{ type: "platform_federation_rule_archived", actor, federation_rule_id, 4 more }



An OIDC federation rule was archived.



PlatformFederationRuleCreated object{ type: "platform_federation_rule_created", actor, applies_to_all_workspaces, 13 more }



An OIDC federation rule was created, allowing tokens from a federation issuer to authenticate as a service account or user. Rules may additionally match on token claims or a condition expression, which are not included in this event.



PlatformFederationRuleUpdated object{ type: "platform_federation_rule_updated", actor, federation_rule_id, 5 more }



An OIDC federation rule was updated.



PlatformFederationRuleWorkspaceAdded object{ type: "platform_federation_rule_workspace_added", actor, federation_rule_id, 5 more }



A federation rule was enabled for a workspace.



PlatformFederationRuleWorkspaceRemoved object{ type: "platform_federation_rule_workspace_removed", actor, federation_rule_id, 5 more }



A federation rule was disabled for a workspace.



PlatformFileContentDownloaded object{ type: "platform_file_content_downloaded", actor, file_id, 4 more }



Activity logged when file content is downloaded via GET /v1/files/{file_id}/content.



PlatformFileDeleted object{ type: "platform_file_deleted", actor, file_id, 4 more }



Activity logged when a file is deleted via DELETE /v1/files/{file_id}.



PlatformFileUploaded object{ type: "platform_file_uploaded", actor, file_id, 5 more }



Activity logged when a file is uploaded via POST /v1/files.



PlatformMemoryCreated object{ type: "platform_memory_created", actor, memory_id, 7 more }



An agent memory document was created.



PlatformMemoryDeleted object{ type: "platform_memory_deleted", actor, memory_id, 7 more }



An agent memory document was deleted.



PlatformMemoryStoreArchived object{ type: "platform_memory_store_archived", actor, memory_store_id, 5 more }



An agent memory store was archived. Archived stores reject new memory writes and cannot be attached to new sessions; deletion and redaction remain permitted for privacy scrubbing.



PlatformMemoryStoreCreated object{ type: "platform_memory_store_created", actor, memory_store_id, 5 more }



An agent memory store was created.



PlatformMemoryStoreDeleted object{ type: "platform_memory_store_deleted", actor, memory_store_id, 5 more }



An agent memory store was deleted. Memory content removal may complete asynchronously for very large stores.



PlatformMemoryStoreUpdated object{ type: "platform_memory_store_updated", actor, memory_store_id, 5 more }



An agent memory store's name, description, or metadata was updated.



PlatformMemoryUpdated object{ type: "platform_memory_updated", actor, memory_id, 7 more }



An agent memory document's content or path was updated.



PlatformMemoryVersionRedacted object{ type: "platform_memory_version_redacted", actor, memory_id, 7 more }



A historical version of an agent memory document was redacted. Redaction scrubs the stored content of a specific version while preserving the version's existence in the history.



PlatformOAuthAppCreated object{ type: "platform_oauth_app_created", actor, oauth_app_id, 5 more }



An OAuth app was created.



PlatformOAuthAppRevoked object{ type: "platform_oauth_app_revoked", actor, oauth_app_id, 4 more }



An OAuth app was revoked.



PlatformOAuthAppUpdated object{ type: "platform_oauth_app_updated", actor, oauth_app_id, 5 more }



An OAuth app was updated.



PlatformPluginDirectorySubmissionCreated object{ type: "platform_plugin_directory_submission_created", actor, plugin_name, 5 more }



A plugin directory submission was created on the API platform. A plugin directory submission is a request to list a plugin in the public plugin directory.



PlatformPluginDirectorySubmissionDeleted object{ type: "platform_plugin_directory_submission_deleted", actor, submission_id, 4 more }



A plugin directory submission was deleted on the API platform.



PlatformPluginDirectorySubmissionUpdated object{ type: "platform_plugin_directory_submission_updated", actor, status, 5 more }



A plugin directory submission was updated on the API platform.



PlatformServiceAccountArchived object{ type: "platform_service_account_archived", actor, service_account_id, 4 more }



A service account was archived.



PlatformServiceAccountCreated object{ type: "platform_service_account_created", actor, organization_role, 5 more }



A service account was created.



PlatformServiceAccountUpdated object{ type: "platform_service_account_updated", actor, service_account_id, 5 more }



A service account was updated.



PlatformServiceAccountWorkspaceMemberAdded object{ type: "platform_service_account_workspace_member_added", actor, service_account_id, 6 more }



A service account was added as a member of a workspace.



PlatformServiceAccountWorkspaceMemberRemoved object{ type: "platform_service_account_workspace_member_removed", actor, service_account_id, 5 more }



A service account was removed from a workspace.



PlatformServiceAccountWorkspaceMemberUpdated object{ type: "platform_service_account_workspace_member_updated", actor, service_account_id, 6 more }



A service account's workspace membership role was updated.



PlatformSigningKeyCreated object{ type: "platform_signing_key_created", actor, algorithm, 7 more }



Activity logged when a new request-signing key is registered for the org.



PlatformSigningKeyDeleted object{ type: "platform_signing_key_deleted", actor, algorithm, 7 more }



Activity logged when a signing key is permanently deleted.



PlatformSigningKeyRotated object{ type: "platform_signing_key_rotated", actor, algorithm, 7 more }



Activity logged when an in-memory signing key is rotated.



PlatformSkillVersionContentDownloaded object{ type: "platform_skill_version_content_downloaded", actor, skill_id, 5 more }



The content of a skill version was downloaded through the Skills API.



PlatformSkillVersionCreated object{ type: "platform_skill_version_created", actor, skill_id, 5 more }



Activity logged when a skill version is created via POST /v1/skills/{skill_id}/versions.



PlatformSkillVersionDeleted object{ type: "platform_skill_version_deleted", actor, skill_id, 5 more }



Activity logged when a skill version is deleted via DELETE /v1/skills/{skill_id}/versions/{version}.



PlatformSpendLimitAlertEmailsUpdated object{ type: "platform_spend_limit_alert_emails_updated", actor, id, 5 more }



Spend limit alert email addresses and role targets were updated for an org.



PlatformSpendLimitCreated object{ type: "platform_spend_limit_created", actor, id, 5 more }



An org-level fixed-dollar spend limit was created.



PlatformSpendLimitDeleted object{ type: "platform_spend_limit_deleted", actor, id, 4 more }



An org-level spend limit was removed.



PlatformSpendLimitUpdated object{ type: "platform_spend_limit_updated", actor, id, 5 more }



An org-level spend limit snooze/ignore state was changed.



PlatformUsageReportClaudeCodeViewed object{ type: "platform_usage_report_claude_code_viewed", actor, id, 3 more }



The Claude Code usage report was viewed.



PlatformUsageReportMessagesViewed object{ type: "platform_usage_report_messages_viewed", actor, id, 3 more }



The messages usage report was viewed.



PlatformWorkspaceArchived object{ type: "platform_workspace_archived", actor, workspace_id, 4 more }



A workspace was archived.



PlatformWorkspaceCreated object{ type: "platform_workspace_created", actor, workspace_id, 4 more }



A workspace was created.



PlatformWorkspaceInferenceDataRetentionDisabled object{ type: "platform_workspace_inference_data_retention_disabled", actor, workspace_id, 5 more }



The zero data retention override was disabled for a workspace.



PlatformWorkspaceInferenceDataRetentionEnabled object{ type: "platform_workspace_inference_data_retention_enabled", actor, workspace_id, 5 more }



The zero data retention override was enabled for a workspace.



PlatformWorkspaceMemberAdded object{ type: "platform_workspace_member_added", actor, user_id, 5 more }



A member was added to a workspace.



PlatformWorkspaceMemberRemoved object{ type: "platform_workspace_member_removed", actor, user_id, 5 more }



A member was removed from a workspace.



PlatformWorkspaceMemberUpdated object{ type: "platform_workspace_member_updated", actor, user_id, 6 more }



A workspace member was updated.



PlatformWorkspaceMemberViewed object{ type: "platform_workspace_member_viewed", actor, user_id, 5 more }



A workspace member was viewed.



PlatformWorkspaceMembersListed object{ type: "platform_workspace_members_listed", actor, workspace_id, 4 more }



Workspace members were listed.



PlatformWorkspaceRateLimitDeleted object{ type: "platform_workspace_rate_limit_deleted", actor, limiter_type, 6 more }



A workspace rate limit was deleted.



PlatformWorkspaceRateLimitUpdated object{ type: "platform_workspace_rate_limit_updated", actor, limiter_type, 7 more }



A workspace rate limit was created or updated.



PlatformWorkspaceUpdated object{ type: "platform_workspace_updated", actor, workspace_id, 5 more }



A workspace was updated.



ClaudePluginCreated object{ type: "claude_plugin_created", actor, id, 5 more }



Plugin was created.



ClaudePluginDeleted object{ type: "claude_plugin_deleted", actor, id, 5 more }



Plugin was deleted.



ClaudePluginDisabled object{ type: "claude_plugin_disabled", actor, id, 6 more }



User disabled a plugin for their account.



ClaudePluginEnabled object{ type: "claude_plugin_enabled", actor, id, 6 more }



User enabled a plugin for their account.



PluginInstallationPreferenceUpdated object{ type: "plugin_installation_preference_updated", actor, marketplace_id, 10 more }



An org admin changed the installation preference for a plugin.



ClaudePluginReplaced object{ type: "claude_plugin_replaced", actor, id, 5 more }



Plugin was replaced.



ClaudePluginSecurityScanCompleted object{ type: "claude_plugin_security_scan_completed", actor, scan_id, 8 more }



A security scan of a plugin completed and produced a verdict.



ClaudePluginUpdated object{ type: "claude_plugin_updated", actor, id, 5 more }



Plugin was updated.



PrepaidAutoRechargeDisabled object{ type: "prepaid_auto_recharge_disabled", actor, id, 3 more }



Auto-recharge was disabled for API prepaid org.



PrepaidAutoRechargeUpdated object{ type: "prepaid_auto_recharge_updated", actor, id, 5 more }



Auto-recharge settings were updated for API prepaid org.



PrepaidExtraUsageAutoReloadDisabled object{ type: "prepaid_extra_usage_auto_reload_disabled", actor, id, 3 more }



Prepaid usage credit auto-reload was disabled.



PrepaidExtraUsageAutoReloadEnabled object{ type: "prepaid_extra_usage_auto_reload_enabled", actor, id, 3 more }



Prepaid usage credit auto-reload was enabled.



PrepaidExtraUsageAutoReloadSettingsUpdated object{ type: "prepaid_extra_usage_auto_reload_settings_updated", actor, id, 3 more }



Prepaid usage credit auto-reload settings were updated.



PrimaryOwnerTransferred object{ type: "primary_owner_transferred", actor, new_owner_id, 5 more }



Primary owner role was transferred to another org member.



ClaudeProjectArchived object{ type: "claude_project_archived", actor, claude_project_id, 4 more }



A Claude project was archived.



ClaudeProjectCreated object{ type: "claude_project_created", actor, claude_project_id, 4 more }



A Claude project was created.



ClaudeProjectDeleted object{ type: "claude_project_deleted", actor, claude_project_id, 4 more }



A Claude project was deleted.



ClaudeProjectDocumentAccessFailed object{ type: "claude_project_document_access_failed", actor, claude_project_id, 6 more }



An attempt to access a document in a Claude project failed.



ClaudeProjectDocumentBulkDeletionAuditTruncated object{ type: "claude_project_document_bulk_deletion_audit_truncated", actor, audited_count, 6 more }



A bulk request to delete documents from a Claude project failed with more documents requested than were individually recorded in the audit log.



ClaudeProjectDocumentDeleted object{ type: "claude_project_document_deleted", actor, claude_project_document_id, 6 more }



A document was deleted from a Claude project.



ClaudeProjectDocumentDeletionFailed object{ type: "claude_project_document_deletion_failed", actor, claude_project_id, 6 more }



A request to delete a document from a Claude project failed.



ClaudeProjectDocumentUpdated object{ type: "claude_project_document_updated", actor, claude_project_document_id, 6 more }



The content of a document in a Claude project was replaced in place.



ClaudeProjectDocumentUploaded object{ type: "claude_project_document_uploaded", actor, claude_project_document_id, 6 more }



A document was uploaded to a Claude project.



ClaudeProjectDocumentViewed object{ type: "claude_project_document_viewed", actor, claude_project_document_id, 6 more }



A document in a Claude project was viewed.



ClaudeProjectFileAccessFailed object{ type: "claude_project_file_access_failed", actor, claude_file_id, 5 more }



An attempt to access a file in a Claude project failed.



ClaudeProjectFileBulkDeletionAuditTruncated object{ type: "claude_project_file_bulk_deletion_audit_truncated", actor, audited_count, 6 more }



A bulk request to delete files from a Claude project failed with more files requested than were individually recorded in the audit log.



ClaudeProjectFileDeleted object{ type: "claude_project_file_deleted", actor, claude_file_id, 5 more }



A file was deleted from a Claude project.



ClaudeProjectFileDeletionFailed object{ type: "claude_project_file_deletion_failed", actor, claude_project_id, 5 more }



A request to delete a file from a Claude project failed.



ClaudeProjectFileUploaded object{ type: "claude_project_file_uploaded", actor, claude_file_id, 6 more }



A file was uploaded to a Claude project.



ClaudeProjectReported object{ type: "claude_project_reported", actor, claude_project_id, 4 more }



A Claude project was reported.



ClaudeProjectSharingUpdated object{ type: "claude_project_sharing_updated", actor, audience, 5 more }



A Claude project's sharing settings were updated.



ClaudeProjectViewed object{ type: "claude_project_viewed", actor, claude_project_id, 5 more }



A Claude project was viewed.



ClaudePubsecIdentityConfigured object{ type: "claude_pubsec_identity_configured", actor, idp_saml_config_updated, 6 more }



SAML IdP configuration updated for a public sector organization.



RbacRoleAssigned object{ type: "rbac_role_assigned", actor, principal_id, 6 more }



Admin assigned an RBAC custom role to a principal.



RbacRoleCreated object{ type: "rbac_role_created", actor, role_id, 5 more }



Admin created an RBAC custom role.



RbacRoleDeleted object{ type: "rbac_role_deleted", actor, role_id, 4 more }



Admin deleted an RBAC custom role.



RbacRoleGrantUpdated object{ type: "rbac_role_grant_updated", action, actor, 6 more }



Admin requested a capability grant for an RBAC custom role, or removed it.

Records the admin's change to the role. Whether the grant is currently in effect on the role is reported separately.



RbacRolePermissionAdded object{ type: "rbac_role_permission_added", action, actor, 7 more }



Admin added a permission to an RBAC custom role.

Emitted once per requested permission, including permissions the role already had, so a retried request still produces a complete audit record.



RbacRolePermissionRemoved object{ type: "rbac_role_permission_removed", action, actor, 7 more }



Admin removed a permission from an RBAC custom role.

Emitted once per requested permission, including permissions the role already lacked, so a retried request still produces a complete audit record.



RbacRoleUnassigned object{ type: "rbac_role_unassigned", actor, principal_id, 6 more }



Admin unassigned an RBAC custom role from a principal.



RbacRoleUpdated object{ type: "rbac_role_updated", actor, role_id, 4 more }



Admin updated an RBAC custom role.



RoleAssignmentGranted object{ type: "role_assignment_granted", actor, id, 9 more }



Role assignment was granted.



RoleAssignmentRevoked object{ type: "role_assignment_revoked", actor, id, 9 more }



Role assignment was revoked.



SSOLoginFailed object{ type: "sso_login_failed", actor, id, 3 more }



An SSO sign-in attempt failed.



SSOLoginInitiated object{ type: "sso_login_initiated", actor, id, 3 more }



A user started an SSO sign-in flow.



SSOLoginSucceeded object{ type: "sso_login_succeeded", actor, id, 5 more }



A user successfully signed in with SSO.



SSOSecondFactorMagicLink object{ type: "sso_second_factor_magic_link", actor, id, 3 more }



SSO second factor magic link was used.



ScimUserCreated object{ type: "scim_user_created", actor, user_id, 4 more }



A SCIM user was provisioned.



ScimUserDeleted object{ type: "scim_user_deleted", actor, user_id, 4 more }



A SCIM user was deleted.



ScimUserUpdated object{ type: "scim_user_updated", actor, user_id, 4 more }



A SCIM user was updated.



ScopedAPIKeyDeleted object{ type: "scoped_api_key_deleted", actor, api_key_id, 6 more }



A scoped API key was deleted.



ScopedAPIKeyUpdated object{ type: "scoped_api_key_updated", actor, api_key_id, 5 more }



A scoped API key was renamed or its activation state changed.



SeatTierChangesCancelled object{ type: "seat_tier_changes_cancelled", actor, id, 3 more }



Scheduled seat tier downgrades were cancelled.



SeatTiersPurchased object{ type: "seat_tiers_purchased", actor, id, 4 more }



Seat tiers were purchased or upgraded on a subscription.



ServiceCreated object{ type: "service_created", actor, service_name, 4 more }



Activity logged when an org service is explicitly created.



ServiceDeleted object{ type: "service_deleted", actor, service_name, 4 more }



Activity logged when an org service is deleted.



ServiceKeyCreated object{ type: "service_key_created", actor, is_service_created, 8 more }



Activity logged when a new org service key is created.



ServiceKeyRevoked object{ type: "service_key_revoked", actor, service_key_id, 5 more }



Activity logged when an org service key is revoked.



SessionRevoked object{ type: "session_revoked", actor, id, 3 more }



User revoked a specific session.



SessionShareAccessed object{ type: "session_share_accessed", actor, id, 4 more }



Session share was accessed.



SessionShareCreated object{ type: "session_share_created", actor, id, 5 more }



Session share was created.



SessionShareRevoked object{ type: "session_share_revoked", actor, id, 5 more }



Session share was revoked.



ClaudeSkillCreated object{ type: "claude_skill_created", actor, id, 8 more }



Skill was created.



ClaudeSkillDeleted object{ type: "claude_skill_deleted", actor, id, 10 more }



Skill was deleted.



ClaudeSkillDisabled object{ type: "claude_skill_disabled", actor, id, 5 more }



User disabled a skill for their account.



ClaudeSkillEnabled object{ type: "claude_skill_enabled", actor, id, 5 more }



User enabled a skill for their account.



ClaudeSkillReplaced object{ type: "claude_skill_replaced", actor, id, 8 more }



Skill was replaced.



ClaudeSkillSecurityScanCompleted object{ type: "claude_skill_security_scan_completed", actor, scan_id, 8 more }



A security scan of a skill completed and produced a verdict.



SlackWorkspaceClaimRevoked object{ type: "slack_workspace_claim_revoked", actor, slack_team_id, 5 more }



A Slack workspace or Enterprise Grid organization was disconnected from the organization for Claude in Slack.



SlackWorkspaceClaimed object{ type: "slack_workspace_claimed", actor, slack_team_id, 5 more }



A Slack workspace or Enterprise Grid organization was connected to the organization for Claude in Slack.



SocialLoginSucceeded object{ type: "social_login_succeeded", actor, provider, 6 more }



A user successfully signed in with a social identity provider (Google, Apple, or Microsoft).



StepUpAuthenticationFailed object{ type: "step_up_authentication_failed", actor, method, 6 more }



An additional identity check failed.



StepUpAuthenticationSucceeded object{ type: "step_up_authentication_succeeded", actor, method, 5 more }



The user completed an additional identity check to confirm a sensitive action.



StepUpCredentialEnrolled object{ type: "step_up_credential_enrolled", actor, credential_id, 4 more }



A user enrolled a passkey for confirming sensitive actions on their account.



SubscriptionCancellationScheduled object{ type: "subscription_cancellation_scheduled", actor, id, 3 more }



Subscription cancellation was scheduled at end of billing period.



SubscriptionQuantityUpdated object{ type: "subscription_quantity_updated", actor, added_seats, 6 more }



Contracted subscription seat quantity was updated.



SubscriptionRenewed object{ type: "subscription_renewed", actor, id, 5 more }



A cancelled subscription was renewed.



SubscriptionResumed object{ type: "subscription_resumed", actor, id, 3 more }



A scheduled subscription cancellation was reversed.



SubscriptionStarted object{ type: "subscription_started", actor, id, 6 more }



A new subscription was created (Team or Enterprise).



SubscriptionUpgraded object{ type: "subscription_upgraded", actor, id, 5 more }



Subscription plan was upgraded (e.g. Team to Enterprise).



TrustedDeviceCredentialRotated object{ type: "trusted_device_credential_rotated", actor, trusted_device_id, 4 more }



The identity-verification credential of a trusted device was rotated to a new key.



TrustedDeviceEnrolled object{ type: "trusted_device_enrolled", actor, enrollment_method, 6 more }



A device was enrolled as a trusted device for the user's account. Trusted devices can be used to confirm the user's identity for sensitive actions.



TrustedDeviceRevoked object{ type: "trusted_device_revoked", actor, reason, 6 more }



A trusted device was removed from the user's account.



TunnelArchived object{ type: "tunnel_archived", actor, tunnel_id, 4 more }



An MCP tunnel was archived.



TunnelCertificateAdded object{ type: "tunnel_certificate_added", actor, certificate_id, 6 more }



An inner-TLS CA certificate was added to a tunnel.



TunnelCertificateRevoked object{ type: "tunnel_certificate_revoked", actor, certificate_id, 6 more }



An inner-TLS CA certificate was revoked from a tunnel.



TunnelCreated object{ type: "tunnel_created", actor, tunnel_id, 5 more }



An MCP tunnel was created.



TunnelTokenMinted object{ type: "tunnel_token_minted", actor, token_id, 5 more }



An OAuth bearer token for the tunnel management API was minted.



TunnelTokenRevealed object{ type: "tunnel_token_revealed", actor, tunnel_id, 5 more }



The Cloudflare connector secret for a tunnel was revealed to the caller.



TunnelTokenRevoked object{ type: "tunnel_token_revoked", actor, token_id, 5 more }



An OAuth bearer token for the tunnel management API was revoked.



TunnelTokenRotated object{ type: "tunnel_token_rotated", actor, tunnel_id, 6 more }



The Cloudflare connector secret for a tunnel was rotated.

`tunnel_token_id` is the id of the *newly-issued* token. The previous token is invalidated by the rotation and its id is not recorded here.



UserConsentRecorded object{ type: "user_consent_recorded", actor, consent_type, 6 more }



User granted a consent for a specific entity (e.g. consumer health consent for an MCP server).



UserConsentRevoked object{ type: "user_consent_revoked", actor, id, 7 more }



User revoked a previously granted consent for a specific entity.



ClaudeUserRoleUpdated object{ type: "claude_user_role_updated", actor, user_email, 7 more }



A user's role within the organization was changed, or the user was added to or removed from the organization.



ClaudeUserSettingsUpdated object{ type: "claude_user_settings_updated", actor, updates, 4 more }



User updated their personal settings.



VerificationEvidenceSubmitted object{ type: "verification_evidence_submitted", actor, verification_id, 5 more }



Verification evidence was submitted for an organization's verification.



VerificationProgramApplicationCreated object{ type: "verification_program_application_created", actor, program_slug, 4 more }



An organization applied to a verification program.



WorkspaceMemberSpendLimitCreated object{ type: "workspace_member_spend_limit_created", actor, id, 7 more }



A per-member or workspace-default Claude Code spend limit was created.



WorkspaceMemberSpendLimitDeleted object{ type: "workspace_member_spend_limit_deleted", actor, id, 6 more }



A per-member or workspace-default Claude Code spend limit was deleted.



WorkspaceMemberSpendLimitUpdated object{ type: "workspace_member_spend_limit_updated", actor, id, 7 more }



A per-member Claude Code spend limit amount was updated.



WorkspaceSpendLimitAlertEmailsUpdated object{ type: "workspace_spend_limit_alert_emails_updated", actor, id, 5 more }



Spend limit alert email recipients were updated for a workspace.



WorkspaceSpendLimitCreated object{ type: "workspace_spend_limit_created", actor, id, 6 more }



A workspace-level API spend limit was created.



WorkspaceSpendLimitDeleted object{ type: "workspace_spend_limit_deleted", actor, id, 5 more }



A workspace-level API spend limit was deleted.

first_id: optional string or null





has_more: optional boolean



defaultfalse

last_id: optional string or null



Query compliance activities

cURL



```python
curl https://api.anthropic.com/v1/compliance/activities \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```python
{
  "data": [
    {
      "actor": {
        "api_key_id": "api_key_id",
        "ip_address": "ip_address",
        "user_agent": "user_agent",
        "type": "api_actor"
      },
      "decision": "blocked",
      "id": "id",
      "abuse_session_id": "abuse_session_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "organization_id": "organization_id",
      "organization_uuid": "organization_uuid",
      "type": "abuse_decision_received"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

##### Returns Examples

Response 200



```python
{
  "data": [
    {
      "actor": {
        "api_key_id": "api_key_id",
        "ip_address": "ip_address",
        "user_agent": "user_agent",
        "type": "api_actor"
      },
      "decision": "blocked",
      "id": "id",
      "abuse_session_id": "abuse_session_id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "organization_id": "organization_id",
      "organization_uuid": "organization_uuid",
      "type": "abuse_decision_received"
