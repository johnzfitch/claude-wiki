---
title: "Webhooks - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/organization/webhooks"
category: "04-API-Reference/Admin"
fetched_at: "2026-11-14T06:24:53Z"
tags: ["api", "hooks"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](../Endpoints/http.md)
2.  [Beta](../Endpoints/platform-claude-com-http-beta.md)
3.  [Organization](platform-claude-com-http-beta-organization.md)

# Webhooks

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/create)

POST/v1/organizations/webhooks

Requires `anthropic-beta: ``webhooks-2026-10-07`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Create an organization webhook endpoint.

##### [List Organization Webhook Endpoints](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/list)

GET/v1/organizations/webhooks

Requires `anthropic-beta: ``webhooks-2026-10-07`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

List the organization's webhook endpoints.

##### [Get Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/retrieve)

GET/v1/organizations/webhooks/{webhook_endpoint_id}

Requires `anthropic-beta: ``webhooks-2026-10-07`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Retrieve an organization webhook endpoint by ID.

##### [Update Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/update)

POST/v1/organizations/webhooks/{webhook_endpoint_id}

Requires `anthropic-beta: ``webhooks-2026-10-07`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Update an organization webhook endpoint. Only the fields you send are changed.

##### [Delete Organization Webhook Endpoint](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/delete)

DELETE/v1/organizations/webhooks/{webhook_endpoint_id}

Requires `anthropic-beta: ``webhooks-2026-10-07`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Delete an organization webhook endpoint.

##### [Regenerate Organization Webhook Endpoint Signing Secret](https://platform.claude.com/docs/en/api/http/beta/organization/webhooks/regenerate_signing_secret)

POST/v1/organizations/webhooks/{webhook_endpoint_id}/regenerate_signing_secret

Requires `anthropic-beta: ``webhooks-2026-10-07`. Learn [how to send beta headers](../Endpoints/beta-headers.md).

Replace an organization webhook endpoint's signing secret. The old secret stops working immediately. The new secret is returned only in this response.

##### Models



BetaDeletedOrganizationWebhookEndpoint object{ type: "webhook_endpoint_deleted", id }



A deleted organization webhook endpoint.



type: "webhook_endpoint_deleted"



Always `webhook_endpoint_deleted`.

defaultwebhook_endpoint_deleted

id: string



ID of the deleted webhook endpoint.



BetaNewOrganizationWebhookEndpoint object{ id, created_at, description, 7 more }



A new organization webhook endpoint, with its signing secret.



BetaOrganizationWebhookEndpoint object{ id, created_at, description, 6 more }



A webhook endpoint that belongs to the organization rather than to one of its workspaces.



BetaOrganizationWebhookEndpointSigningSecret object{ signing_secret }



An organization webhook endpoint's new signing secret.

signing_secret: string



The new signing secret. Deliveries are signed with it from now on, and no other response returns it.



BetaOrganizationWebhookEndpointState = "disabled" or "enabled"



Whether deliveries are sent to an organization webhook endpoint.
