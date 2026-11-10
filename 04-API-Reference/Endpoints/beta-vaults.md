---
title: "Vaults - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/beta/vaults"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-05T06:36:14Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

1.  [API reference](http.md)
2.  [Beta](platform-claude-com-http-beta.md)

# Vaults

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

##### [Create a Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/create)

POST/v1/vaults

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Vaults](https://platform.claude.com/docs/en/api/http/beta/vaults/list)

GET/v1/vaults

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Retrieve a Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/retrieve)

GET/v1/vaults/{vault_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update a Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/update)

POST/v1/vaults/{vault_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Delete a Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/delete)

DELETE/v1/vaults/{vault_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Archive a Vault](https://platform.claude.com/docs/en/api/http/beta/vaults/archive)

POST/v1/vaults/{vault_id}/archive

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### Models



BetaManagedAgentsDeletedVault object{ type: "vault_deleted", id }



Confirmation of a deleted vault.

type: "vault_deleted"



id: string



The unique ID of the deleted vault (`vlt_...`).



BetaManagedAgentsVault object{ type: "vault", id, archived_at, 4 more }



A vault that stores credentials for use by agents during sessions.

type: "vault"



id: string



The unique ID of the vault (`vlt_...`).



archived_at: string or null



When the vault was archived. Null if not archived.

formatdate-time



created_at: string



A timestamp in RFC 3339 format

formatdate-time

display_name: string



Human-readable name for the vault.

metadata: map\[string\]



Arbitrary key-value metadata attached to the vault.



updated_at: string



A timestamp in RFC 3339 format

formatdate-time

#### Vaults[Credentials](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials)

##### [Create a Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/create)

POST/v1/vaults/{vault_id}/credentials

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [List Credentials](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/list)

GET/v1/vaults/{vault_id}/credentials

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Retrieve a Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/retrieve)

GET/v1/vaults/{vault_id}/credentials/{credential_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Update a Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/update)

POST/v1/vaults/{vault_id}/credentials/{credential_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Delete a Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/delete)

DELETE/v1/vaults/{vault_id}/credentials/{credential_id}

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Archive a Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/archive)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/archive

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)

##### [Validate an MCP OAuth Credential](https://platform.claude.com/docs/en/api/http/beta/vaults/credentials/mcp_oauth_validate)

POST/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate

Requires `anthropic-beta: ``managed-agents-2026-04-01`. [How to send beta headers](beta-headers.md)
