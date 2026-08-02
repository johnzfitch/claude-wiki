---
title: "OAuth Client Credentials - Model Context Protocol"
source_url: "https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials"
category: "06-MCP-Tools"
fetched_at: "2026-08-02T05:39:26Z"
tags: ["cli", "mcp", "oauth"]
---

## On this page

- [What it is](#what-it-is)
- [When to use it](#when-to-use-it)
- [How it works](#how-it-works)
  - [JWT Bearer Assertions (recommended)](#jwt-bearer-assertions-recommended)
  - [Client Secrets](#client-secrets)
- [Implementation guide](#implementation-guide)
  - [For MCP clients](#for-mcp-clients)
  - [For MCP servers](#for-mcp-servers)
- [SDK examples](#sdk-examples)
  - [Using a client secret](#using-a-client-secret)
  - [Using a JWT private key](#using-a-jwt-private-key)
- [Client support](#client-support)
- [Related resources](#related-resources)

Authorization Extensions

# OAuth Client Credentials

Copy pageCopy page

Machine-to-machine authentication for MCP using the OAuth 2.0 client credentials flow

Copy pageCopy page

The OAuth Client Credentials extension (`io.modelcontextprotocol/oauth-client-credentials`) adds support for the [OAuth 2.0 client credentials flow](https://datatracker.ietf.org/doc/html/rfc6749#section-4.4) to MCP. This enables automated systems to connect to MCP servers without interactive user authorization.

## Specification

Full technical specification for the OAuth Client Credentials extension.


[​](#what-it-is)

What it is

The standard MCP authorization flow requires a user to interactively approve access — a browser opens, the user logs in, and grants permission. That works well for humans, but breaks down when there’s no user present. The OAuth Client Credentials extension solves this by letting a client authenticate using application-level credentials (a client ID and secret, or a signed JWT assertion) rather than delegated user credentials. The client proves its identity directly to the authorization server, which issues an access token without requiring a browser redirect or user interaction.


[​](#when-to-use-it)

When to use it

Use OAuth Client Credentials when:

- **Background services** need to call MCP tools on a schedule or in response to events, without a user present
- **CI/CD pipelines** invoke MCP servers as part of automated build, test, or deployment workflows
- **Server-to-server integrations** connect two backend systems where there’s no end user involved
- **Daemon processes** or long-running workers need persistent access to MCP resources

If your integration has a human user who should explicitly authorize access, use the standard MCP authorization flow instead.


[​](#how-it-works)

How it works

The extension supports two credential formats:


[​](#jwt-bearer-assertions-recommended)

JWT Bearer Assertions (recommended)

Defined in [RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523), JWT Bearer Assertions let the client sign a token with its private key and present it as proof of identity. The authorization server validates the signature using the client’s registered public key. The JWT assertion typically includes:

- `iss`: Client ID (the issuer)
- `sub`: Client ID (subject being authenticated)
- `aud`: Authorization server token endpoint URL
- `exp`: Expiration time
- `iat`: Issued-at time


[​](#client-secrets)

Client Secrets

For simpler deployments, the extension also supports the standard client credentials flow using a `client_id` and `client_secret`. The client sends its credentials directly to the authorization server’s token endpoint and receives an access token in return.

Client secrets are **long-lived credentials** that grant access without user interaction. If a secret is leaked, an attacker can silently authenticate as your application until the secret is rotated. To reduce risk:

- Store secrets in a secrets manager, never in source code or environment files checked into version control.
- Rotate secrets on a regular schedule and immediately after any suspected compromise.
- Scope credentials to the minimum permissions required.
- Prefer JWT assertions when possible — they are short-lived and do not require transmitting the signing key.


[​](#implementation-guide)

Implementation guide


[​](#for-mcp-clients)

For MCP clients

To use the OAuth Client Credentials extension, your client must:

1

Declare support

Include the extension in its per-request capabilities:

```python
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "...",
  "params": {
    // Other fields...
    "_meta": {
      // Other fields...
      "io.modelcontextprotocol/clientCapabilities": {
        "extensions": {
          "io.modelcontextprotocol/oauth-client-credentials": {},
        },
      },
    },
  },
}
```

2

Obtain an access token

Request a token from the authorization server using the client credentials grant before connecting to the MCP server.

3

Include the token

Pass the token in the `Authorization` header of HTTP requests to the MCP server:

```python
Authorization: Bearer <access_token>
```

4

Handle token refresh

Client credentials tokens typically have shorter lifetimes than user-delegated tokens. Implement token refresh logic to obtain a new token before expiry.


[​](#for-mcp-servers)

For MCP servers

To accept client credentials tokens, your server must:

1

Validate the token

On each request, verify the JWT signature and claims against your authorization server’s public keys (usually via a JWKS endpoint).

2

Check scopes

Ensure the token includes the required scopes for the requested operation.

3

Advertise support

Optionally (but recommended for discoverability), include the extension in the `server/discover` response:

```python
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    // Other fields...
    "capabilities": {
      "extensions": {
        "io.modelcontextprotocol/oauth-client-credentials": {},
      },
    },
  },
}
```


[​](#sdk-examples)

SDK examples

The official MCP SDKs provide built-in support for client credentials authentication. Both handle token acquisition and refresh automatically.

1

Install the SDK

- TypeScript

- Python

```python
npm install @modelcontextprotocol/client
```

```python
pip install mcp
```

2

Create a provider and connect

Choose the credential format that matches your setup:


[​](#using-a-client-secret)

Using a client secret

- TypeScript

- Python

```python
import {
  Client,
  ClientCredentialsProvider,
  StreamableHTTPClientTransport,
} from "@modelcontextprotocol/client";

const provider = new ClientCredentialsProvider({
  clientId: "my-service",
  clientSecret: "s3cr3t",
});

const client = new Client(
  { name: "my-service", version: "1.0.0" },
  { capabilities: {} },
);

const transport = new StreamableHTTPClientTransport(
  new URL("https://mcp.example.com/mcp"),
  { authProvider: provider },
);

await client.connect(transport);

// Use the client
const tools = await client.listTools();
console.log(
  "Available tools:",
  tools.tools.map((t) => t.name),
);

await transport.close();
```

```python
import asyncio

import httpx2

from mcp import Client
from mcp.client.auth.extensions.client_credentials import (
    ClientCredentialsOAuthProvider,
)
from mcp.client.streamable_http import streamable_http_client
from mcp.shared.auth import OAuthClientInformationFull, OAuthToken


class InMemoryTokenStorage:
    def __init__(self) -> None:
        self.tokens: OAuthToken | None = None
        self.client_info: OAuthClientInformationFull | None = None

    async def get_tokens(self) -> OAuthToken | None:
        return self.tokens

    async def set_tokens(self, tokens: OAuthToken) -> None:
        self.tokens = tokens

    async def get_client_info(self) -> OAuthClientInformationFull | None:
        return self.client_info

    async def set_client_info(self, client_info: OAuthClientInformationFull) -> None:
        self.client_info = client_info


provider = ClientCredentialsOAuthProvider(
    server_url="https://mcp.example.com/mcp",
    storage=InMemoryTokenStorage(),
    client_id="my-service",
    client_secret="s3cr3t",
    scopes="read write",
)


async def main() -> None:
    async with httpx2.AsyncClient(auth=provider) as http_client:
        transport = streamable_http_client(
            "https://mcp.example.com/mcp",
            http_client=http_client,
        )
        async with Client(transport) as client:
            # Use the client
            tools = await client.list_tools()
            print("Available tools:", [t.name for t in tools.tools])


if __name__ == "__main__":
    asyncio.run(main())
```


[​](#using-a-jwt-private-key)

Using a JWT private key

- TypeScript

- Python

```python
import {
  Client,
  PrivateKeyJwtProvider,
  StreamableHTTPClientTransport,
} from "@modelcontextprotocol/client";

const provider = new PrivateKeyJwtProvider({
  clientId: "my-service",
  privateKey: process.env.CLIENT_PRIVATE_KEY_PEM,
  algorithm: "RS256",
});

const client = new Client(
  { name: "my-service", version: "1.0.0" },
  { capabilities: {} },
);

const transport = new StreamableHTTPClientTransport(
  new URL("https://mcp.example.com/mcp"),
  { authProvider: provider },
);

await client.connect(transport);

// Use the client
const tools = await client.listTools();
console.log(
  "Available tools:",
  tools.tools.map((t) => t.name),
);

await transport.close();
```

```python
import asyncio
from pathlib import Path

import httpx2

from mcp import Client
from mcp.client.auth.extensions.client_credentials import (
    PrivateKeyJWTOAuthProvider,
    SignedJWTParameters,
)
from mcp.client.streamable_http import streamable_http_client
from mcp.shared.auth import OAuthClientInformationFull, OAuthToken


class InMemoryTokenStorage:
    def __init__(self) -> None:
        self.tokens: OAuthToken | None = None
        self.client_info: OAuthClientInformationFull | None = None

    async def get_tokens(self) -> OAuthToken | None:
        return self.tokens

    async def set_tokens(self, tokens: OAuthToken) -> None:
        self.tokens = tokens

    async def get_client_info(self) -> OAuthClientInformationFull | None:
        return self.client_info

    async def set_client_info(self, client_info: OAuthClientInformationFull) -> None:
        self.client_info = client_info


# Create a signed JWT assertion provider from key parameters
jwt_params = SignedJWTParameters(
    issuer="my-service",
    subject="my-service",
    signing_key=Path("private_key.pem").read_text(),
    signing_algorithm="RS256",
    lifetime_seconds=300,
)

provider = PrivateKeyJWTOAuthProvider(
    server_url="https://mcp.example.com/mcp",
    storage=InMemoryTokenStorage(),
    client_id="my-service",
    assertion_provider=jwt_params.create_assertion_provider(),
    scopes="read write",
)


async def main() -> None:
    async with httpx2.AsyncClient(auth=provider) as http_client:
        transport = streamable_http_client(
            "https://mcp.example.com/mcp",
            http_client=http_client,
        )
        async with Client(transport) as client:
            # Use the client
            tools = await client.list_tools()
            print("Available tools:", [t.name for t in tools.tools])


if __name__ == "__main__":
    asyncio.run(main())
```


[​](#client-support)

Client support

Support for this extension varies by client. Extensions are opt-in and never active by default.

Check the [client matrix](/extensions/client-matrix) for current implementation status across MCP clients.


[​](#related-resources)

Related resources

## ext-auth repository

Source code and reference implementations

## Full specification

Technical specification with normative requirements

## RFC 6749 — Client Credentials Grant

The underlying OAuth 2.0 specification

## RFC 7523 — JWT Bearer Assertions

JWT assertion format specification
