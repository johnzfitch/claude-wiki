---
category: "13-Enterprise-Admin"
source_url: "https://support.claude.com/en/articles/9970975-how-to-access-audit-logs"
---


Audit logs are available only for Enterprise organizations. 

Organization Owners and Primary Owners can export data within Admin settings > Data and Privacy and clicking the "Export logs" button. Upon triggering this export, all audit logs for the organization within the past 180 days will be aggregated. The Owner who requested the export will receive an email containing a download link, which is active for 24 hours. Note that there may be a delay between triggering the export and receiving the email as logs are aggregated.

 

Please note that title and content of chats and projects are not available to be exported in audit logs (only their unique identifiers will be exported). However, chat inputs/outputs will be exportable by Primary Owners via data exports.

 

Log Structure

Audit logs consist of the following columns:

Column Name

 

Type

 

Description 

created_at

 

datetime

 

When the log was written

actor_info

 

dict[str, Any]

 

Information on the actor, if available

event

 

AuditEventType

 

Type of event.

event_info

 

 

dict[str, Any]

 

 

Other relevant information for a given event type.

entity_info

 

dict[str, Any]

 

Entity affected by the operation, if relevant. In general, the entity represents what is affected by the event.

ip_address

 

str | None

 

IP Address corresponding to the event, if available.

device_id

 

str | None

 

Device ID corresponding to the event, if available.

user_agent

 

str | None

 

User Agent header corresponding to the event, if available. Contains information detailing the program used to execute the event.

client_platform

 

str | None

 

Client Platform corresponding to the event, if available. Corresponds to mobile platforms, either iOS or Android.

Entities

The entities that can be affected by events. Entity info follows this structure:

Field Name

 

Field Type

 

Notes

type

 

AuditEntityType

 

Type of the entity.

uuid

 

str

 

UUID for the entity.

name

 

str | None

 

Name for the entity, when available

metadata

 

dict[str, Any] | None

 

Metadata related to the entity, when available

AuditEntityType

 

Metadata

 

Description

account

 

email_address: email address on the account

 

User accounts. 

invite

 

role: Role the invite is for

 

Invite to join a team/organization

chat_project

 

is_private: The visibility of the project

 

Project consisting of chats

chat_project_document

 

project_uuid: UUID of the project this document is related to

 

Document in the knowledge base of a chat project

chat_conversation

 

project_uuid: UUID of the project this conversation is a part of, if relevant

 

Chat conversation with Claude. Can be in a project or standalone. 

file

 

n/a

 

File uploaded to Claude

sso_connection

 

connection_type: Type of SSO connection

 

state: Connection state

 

domains: Domain(s) related to SSO connection

 

SSO connection 

Recorded Events

Event

 

Description

 

Event Info

 

Entity Type

 

Date added

user_verified_phone_code

 

User verified using the sent phone code.

 

phone_number: The phone number used

 

channel: SMS or Call

 

n/a

 

2024-09-04

user_signed_out

 

User signed out from their account.

 

 

 

n/a

 

2024-09-04

user_signed_in_sso

 

User signed in via SSO.

 

domain: The relevant SSO domain

 

n/a

 

2024-09-04

user_signed_in_google

 

User signed in via Google.

 

email_address: The email address used.

 

n/a

 

2024-09-04

user_signed_in_apple

 

User signed in via Apple.

 

email_address: The email address used.

 

n/a

 

2024-09-04

user_sent_phone_code

 

User sent a phone code.

 

phone_number: The phone number used

 

channel: SMS or Call

 

n/a

 

2024-09-04

user_requested_magic_link

 

User requested a magic link.

 

email_address: The email address the link is sent to.

 

is_successful: Whether the request is successful or not.

 

n/a

 

2024-09-04

user_name_changed

 

User changed the name on their account.

 

old_name: The previous name.

 

new_name: The new name.

 

n/a

 

2024-09-04

user_attempted_magic_link_verification

 

User attempted to verify using a magic link

 

email_address: The email address the link is sent to.

 

is_successful: Whether the verification is successful or not.

 

n/a

 

2024-09-04

project_visibility_changed

 

The visibility of a project has been changed by a user.

 

updated_privacy: The new privacy/visibility of the project.

 

chat_project

 

2024-09-04

project_renamed

 

A project has been renamed by a user.

 

 

 

chat_project

 

2024-09-04

project_document_deleted

 

A document has been deleted from a project’s knowledge base.

 

 

 

chat_project_document

 

2024-09-04

project_document_created

 

A document has been added to a project’s knowledge base.

 

 

 

chat_project_document

 

2024-09-04

project_deleted

 

A project has been deleted by a user.

 

 

 

chat_project

 

2024-09-04

project_created

 

A project has been created by a user.

 

 

 

chat_project

 

2024-09-04

org_user_invite_sent

 

An invite was sent to the user to join the organization.

 

 

 

chat_project

 

2024-09-04

org_user_invite_rejected

 

A previously sent invite to a user was rejected.

 

invited_role: Role that the invitation was for.

 

invite

 

2024-09-04

org_user_invite_re_sent

 

An invite was re-sent to the user to join the organization.

 

invited_email_address: Email address invite is sent to.

 

invited_role: Role the invite is for.

 

invite_uuid: UUID for the created invite.

 

account

 

2024-09-04

org_user_invite_deleted

 

A previously sent invite to a user was deleted.

 

invited_email_address: Email address invite is sent to.

 

invited_role: Role the invite is for.

 

invite

 

2024-09-04

org_user_invite_accepted

 

A previously sent invite to a user was accepted.

 

invited_role: Role the invite is for.

 

invite

 

2024-09-04

org_user_deleted

 

A user was deleted from the organization.

 

 

 

account

 

2024-09-04

org_sso_toggled

 

SSO connections for the organization have been toggled.

 

sso_enforced: Whether SSO is enforced or not.

 

 

 

2024-09-04

org_sso_connection_deleted

 

A previously existing SSO connection has been deleted.

 

 

 

sso_connection

 

2024-09-10

org_sso_connection_deactivated

 

A previously existing SSO connection has been deactivated.

 

 

 

sso_connection

 

2024-09-10

org_sso_connection_activated

 

A new SSO connection has been activated.

 

 

 

sso_connection

 

2024-09-10

org_sso_add_initiated

 

An attempt to add SSO for this organization has been initiated.

 

 

 

n/a

 

2024-09-04

org_jit_toggled

 

JIT for the organization has been toggled.

 

jit_provisioning_enabled: Whether this feature is enabled.

 

n/a

 

2024-09-04

org_domain_verified

 

Domain capture was verified for this organization.

 

domain: Domain that has been verified.

 

n/a

 

2024-09-04

org_domain_add_initiated

 

Domain capture was initiated for this organization.

 

 

 

n/a

 

2024-09-04

org_data_export_started

 

Organization data export started.

 

export_type: All organization data.

 

initiated_by_anthropic: Did Anthropic start the export (yes/no)?

 

n/a

 

07/15/2025

org_data_export_completed

 

Organization data export completed.

 

export_type: All organization data.

 initiated_by_anthropic: Did Anthropic start the export (yes/no)?

 

n/a

 

07/15/2025

file_uploaded

 

A file has been uploaded.

 

 

 

file

 

2024-09-04

conversation_renamed

 

A conversation has been renamed.

 

new_name: New name for the conversation.

 

chat_conversation

 

2024-09-04

conversation_deleted

 

A conversation has been deleted.

 

 

 

chat_conversation

 

2024-09-04

conversation_created

 

A conversation has been created.

 

 

 

chat_conversation

 

2024-09-04

Related Articles
Roles and Permissions
Important Considerations Before Enabling Single Sign-On (SSO) and JIT/SCIM Provisioning
What happens to a user's data when they are removed from a Team or Enterprise organization?
Usage Analytics for Team and Enterprise Plans
Managing members on Team and Enterprise plans