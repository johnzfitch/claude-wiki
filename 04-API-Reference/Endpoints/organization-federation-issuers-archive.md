---
title: "Archive Federation Issuer - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/federation/issuers/archive"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:19Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/archive).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Federation](https://platform.claude.com/docs/en/api/http/organization/federation)
4.  [Issuers](https://platform.claude.com/docs/en/api/http/organization/federation/issuers)

# Archive Federation Issuer

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/federation_issuers/{federation_issuer_id}/archive

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Archive a federation issuer.

Idempotent; re-archiving returns the issuer with its original `archived_at`. Rejected with 400 if any live (non-archived) federation rule still references the issuer; archive those rules first (a rule's issuer cannot be changed), or recreate them against another issuer.

##### Path parameters

federation_issuer_id: string



ID of the federation issuer to archive.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



FederationIssuer object{ type: "federation_issuer", id, archived_at, 12 more }



Registered external OIDC identity provider.

Records an external IdP the organization trusts for the RFC 7523 jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

Archive Federation Issuer

cURL



```python
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID/archive \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
