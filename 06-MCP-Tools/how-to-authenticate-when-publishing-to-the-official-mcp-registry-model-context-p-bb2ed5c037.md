---
category: "06-MCP-Tools"
fetched_at: "2026-02-22T14:29:21Z"
source_url: "https://modelcontextprotocol.io/registry/authentication"
title: "How to Authenticate When Publishing to the Official MCP Registry - Model Context Protocol"
---

[Skip to main content](#content-area)

[Model Context Protocol home page](/)

Search...

⌘K

- [Blog](https://blog.modelcontextprotocol.io)
- [GitHub](https://github.com/modelcontextprotocol)

Search...

Navigation

Publishing

How to Authenticate When Publishing to the Official MCP Registry

[Documentation](/docs/getting-started/intro)

[Extensions](/extensions/overview)

[Specification](/specification/2025-11-25)

[Registry](/registry/about)

[Community](/community/contributing)

- [](/registry/about)
  About

&nbsp;

- [](/registry/quickstart)
  Quickstart: Publish a Server

&nbsp;

- [](/registry/faq)
  FAQ

##### Publishing

- [](/registry/package-types)
  Package Types
- [](/registry/remote-servers)
  Remote Servers
- [](/registry/authentication)
  Authentication
- [](/registry/versioning)
  Versioning
- [](/registry/github-actions)
  GitHub Actions
- [](/registry/moderation-policy)
  Moderation Policy

##### Consuming

- [](/registry/registry-aggregators)
  Registry Aggregators

- [](/registry/terms-of-service)
  Terms of Service

On this page

- [GitHub Authentication](#github-authentication)
- [DNS Authentication](#dns-authentication)
- [HTTP Authentication](#http-authentication)

Publishing

# How to Authenticate When Publishing to the Official MCP Registry

Copy page

Copy page

The MCP Registry is currently in preview. Breaking changes or data resets may occur before general availability. If you encounter any issues, please report them on [GitHub](https://github.com/modelcontextprotocol/registry/issues).

You must authenticate before publishing to the official MCP Registry. The MCP Registry supports different authentication methods. Which authentication method you choose determines the namespace of your server’s name. If you choose GitHub-based authentication, your server’s name in `server.json` **MUST** be of the form `io.github.username/*` (or `io.github.orgname/*`). For example, `io.github.alice/weather-server`. If you choose domain-based authentication, your server’s name in `server.json` **MUST** be of the form `com.example.*/*`, where `com.example` is the reverse-DNS form of your domain name. For example, `io.modelcontextprotocol/everything`.

| Authentication | Name Format | Example Name |
|----|----|----|
| GitHub-based | `io.github.username/*` or `io.github.orgname/*` | `io.github.alice/weather-server` |
| domain-based | `com.example.*/*` | `io.modelcontextprotocol/everything` |

## 

[​](#github-authentication)

GitHub Authentication

GitHub authentication uses an OAuth flow initiated by the `mcp-publisher` CLI tool. To perform GitHub authentication, navigate to your server project directory and run:

Copy

``` shiki
mcp-publisher login github
```

You should see output like:

Output

Copy

``` shiki
Logging in with github...

To authenticate, please:
1. Go to: https://github.com/login/device
2. Enter code: ABCD-1234
3. Authorize this application
Waiting for authorization...
```

Visit the link, follow the prompts, and enter the authorization code that was printed in the terminal (e.g., `ABCD-1234` in the above output). Once complete, go back to the terminal, and you should see output like:

Output

Copy

``` shiki
Successfully authenticated!
✓ Successfully logged in
```

## 

[​](#dns-authentication)

DNS Authentication

DNS authentication is a domain-based authentication method that relies on a DNS TXT record. To perform DNS authentication using the `mcp-publisher` CLI tool, run the following commands in your server project directory to generate a TXT record based on a public/private key pair:

Ed25519

ECDSA P-384

Google KMS

Azure Key Vault

Copy

``` shiki
MY_DOMAIN="example.com"

# Generate public/private key pair using Ed25519
openssl genpkey -algorithm Ed25519 -out key.pem

# Generate TXT record
PUBLIC_KEY="$(openssl pkey -in key.pem -pubout -outform DER | tail -c 32 | base64)"
echo "${MY_DOMAIN}. IN TXT \"v=MCPv1; k=ed25519; p=${PUBLIC_KEY}\""
```

Then add the TXT record using your DNS provider’s control panel. It may take several minutes for the TXT record to propagate. After the TXT record has propagated, log in using the `mcp-publisher login` command:

Ed25519

ECDSA P-384

Google KMS

Azure Key Vault

Copy

``` shiki
MY_DOMAIN="example.com"

PRIVATE_KEY="$(openssl pkey -in key.pem -noout -text | grep -A3 "priv:" | tail -n +2 | tr -d ' :\n')"
mcp-publisher login dns --domain "${MY_DOMAIN}" --private-key "${PRIVATE_KEY}"
```

## 

[​](#http-authentication)

HTTP Authentication

HTTP authentication is a domain-based authentication method that relies on a `/.well-known/mcp-registry-auth` file hosted on your domain. For example, `https://example.com/.well-known/mcp-registry-auth`. To perform HTTP authentication using the `mcp-publisher` CLI tool, run the following commands in your server project directory to generate an `mcp-registry-auth` file based on a public/private key pair:

Ed25519

ECDSA P-384

Google KMS

Azure Key Vault

Copy

``` shiki
# Generate public/private key pair using Ed25519
openssl genpkey -algorithm Ed25519 -out key.pem

# Generate mcp-registry-auth file
PUBLIC_KEY="$(openssl pkey -in key.pem -pubout -outform DER | tail -c 32 | base64)"
echo "v=MCPv1; k=ed25519; p=${PUBLIC_KEY}" > mcp-registry-auth
```

Then host the `mcp-registry-auth` file at `/.well-known/mcp-registry-auth` on your domain. After the file is hosted, log in using the `mcp-publisher login` command:

Ed25519

ECDSA P-384

Google KMS

Azure Key Vault

Copy

``` shiki
MY_DOMAIN="example.com"
PRIVATE_KEY="$(openssl pkey -in key.pem -noout -text | grep -A3 "priv:" | tail -n +2 | tr -d ' :\n')"
mcp-publisher login http --domain "${MY_DOMAIN}" --private-key "${PRIVATE_KEY}"
```

Was this page helpful?

Yes

No

[Remote Servers](/registry/remote-servers)[Versioning](/registry/versioning)

[github](https://github.com/modelcontextprotocol)
