---
title: "Update Federation Issuer - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/federation/issuers/update"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:20Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/federation/issuers/update).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [Federation](https://platform.claude.com/docs/en/api/http/organization/federation)
4.  [Issuers](https://platform.claude.com/docs/en/api/http/organization/federation/issuers)

# Update Federation Issuer

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/federation_issuers/{federation_issuer_id}

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](../Other/manage-claude-wif-admin-api.md).

Partially update a federation issuer.

Setting `jwks` replaces the full JWKS shape at once. Archived issuers cannot be updated; this returns 400. Create a new issuer instead.

Updating an issuer that backs a rule with a scope outside `workspace:developer` or `workspace:inference` requires a Console session.

##### Path parameters

federation_issuer_id: string



ID of the federation issuer to update.

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Body

check_jti: optional boolean or null



Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.



issuer_url: optional string or null



Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

minLength1



jwks: optional [JWKSDiscovery](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#jwks_discovery) or [JWKSExplicitURL](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#jwks_explicit_url) or [JWKSInline](https://platform.claude.com/docs/en/api/http/organization/federation/issuers#jwks_inline) or null



Replaces the entire JWKS configuration.

One of the following:



JWKSDiscovery object{ type: "discovery", ca_cert_pem, discovery_base }



JWKS via the issuer's OIDC discovery document.

type: "discovery"





ca_cert_pem: optional string or null



Optional custom CA (PEM) for TLS verification of the JWKS fetch.

maxLength8192

discovery_base: optional string or null



Set when the discovery URL differs from `issuer_url`.



JWKSExplicitURL object{ type: "explicit_url", url, ca_cert_pem }



JWKS fetched from a fixed endpoint.

type: "explicit_url"





url: string



JWKS endpoint.

minLength1



ca_cert_pem: optional string or null



Optional custom CA (PEM) for TLS verification of the JWKS fetch.

maxLength8192



JWKSInline object{ type: "inline", keys }



JWKS supplied directly; no network fetch.

type: "inline"





keys: array of map\[unknown\]



Inline JWK objects.

minItems1

jwks_polling_disabled: optional boolean or null



Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.



max_jwt_lifetime_seconds: optional number or null



Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

minimum1

maximum176400



name: optional string or null



Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

minLength1

maxLength255

##### Returns



FederationIssuer object{ type: "federation_issuer", id, archived_at, 12 more }



Registered external OIDC identity provider.

Records an external IdP the organization trusts for the RFC 7523 jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

Update Federation Issuer

cURL



```python
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY" \
    -d '{}'
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
