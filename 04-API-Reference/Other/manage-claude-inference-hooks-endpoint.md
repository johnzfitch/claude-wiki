---
title: "Develop an Inference hooks integration - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint"
category: "04-API-Reference/Other"
fetched_at: "2026-10-23T06:28:38Z"
tags: ["api", "hooks", "prompting"]
---

- [Managed Agents](managed-agents-overview.md)

- [Admin](manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Finference-hooks-endpoint)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Plugins API](manage-claude-plugins-api.md)[Workspaces](manage-claude-workspaces.md)[Organization webhooks (beta)](manage-claude-organization-webhooks.md)[User profiles](manage-claude-user-profiles.md)[Verification Portal links](manage-claude-user-profiles-verification-portal.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF with the Admin API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

[OpenTelemetry](manage-claude-opentelemetry.md)

Data & compliance

[Data residency](manage-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)

[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys (CMEK)](manage-claude-cmek.md)

[Inference hooks](manage-claude-inference-hooks.md)

[Overview](manage-claude-inference-hooks.md)[Configure Inference hooks](manage-claude-inference-hooks-configuration.md)[Build an integration](manage-claude-inference-hooks-endpoint.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](playground.md)

[Admin](manage-claude-admin-api.md)Inference hooks

# Develop an Inference hooks integration

Copy page



Build the AI security server that receives signed Inference hooks requests, verifies them, and returns allow or deny verdicts.

Copy page





Inference hooks are available only to Claude Enterprise organizations.

An Inference hooks integration is an AI security server: an HTTPS service that Anthropic calls. For each governed request, your server receives a signed `POST` carrying the conversation transcript and responds with an allow or deny verdict. This page documents the protocol for building that server: the request and verdict schemas, signature verification, and the operational contract.

To turn Inference hooks on and point them at your endpoint, see [Configure Inference hooks](manage-claude-inference-hooks-configuration.md). To learn what Inference hooks are and when to use them, see the [Inference hooks overview](manage-claude-inference-hooks.md).

## Get a first verdict round trip

The smallest working integration is a server that reads each request and allows it. Run one of the following servers, expose it at a public `https://` URL (for example, behind a TLS-terminating reverse proxy on a host you control, not a reverse-tunnel service; see [Receive a request](#receive-a-request)), then have your administrator [set it as the endpoint and test the connection](manage-claude-inference-hooks-configuration.md): the **Test connection** result reports the allow verdict your server returned.

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
# Run with: python server.py
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class VerdictHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"  # keep the connection open between verdicts

    def do_POST(self):
        # Drain the body; transcripts can be megabytes.
        self.rfile.read(int(self.headers.get("Content-Length", 0)))
        verdict = b'{"action": "allow"}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(verdict)))
        self.end_headers()
        self.wfile.write(verdict)


ThreadingHTTPServer(("", 8000), VerdictHandler).serve_forever()
```



These servers accept every request, including unsigned ones. Add [signature verification](#verify-the-signature) before you enforce.

## Receive a request

Anthropic sends an HTTPS `POST` to the URL your administrator configures. The whole configured URL is the endpoint: there is no fixed path suffix, so choose any path that suits your server.

Host your AI security server where Anthropic can reach it: an `https://` URL on port 443, on a publicly routable host (private, loopback, and carrier-grade NAT ranges are refused at connect time), with a certificate that validates against the public CA trust store, responding without redirects. The host must have an IPv4 address, which Anthropic uses even when the host also has IPv6 addresses; a URL whose host is `localhost` or an IPv6 address is refused. The configured URL must be the final destination. Reverse-tunnel hosts (ngrok and similar tunnel services) are not supported: Anthropic's network policy blocks them. Host your server on a domain you control. [Configure Inference hooks](manage-claude-inference-hooks-configuration.md) covers how your administrator sets and tests the URL.

Every request carries these fixed headers, along with any [custom request headers](manage-claude-inference-hooks-configuration.md) your administrator configured and, once your organization has a signing secret, the `webhook-*` signature headers described in [Verify the signature](#verify-the-signature):

| Header            | Value              |
|-------------------|--------------------|
| `Content-Type`    | `application/json` |
| `User-Agent`      | `anthropic-dlp/1`  |
| `Accept-Encoding` | `identity`         |

There are two hook events, told apart by the top-level `type` field. The prompt frame is sent once for each governed inference request, before inference starts. The tool call frame is sent when a model response contains tool calls, before any of them runs, in organizations that have **Validate tool calls** on. Either way, Anthropic waits until your AI security server responds or the verdict timeout elapses.

## The prompt frame

The request body is a JSON object with these fields:

| Field        | Type           | Description                                                                                                                                                                                                                                                           |
|--------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`       | string         | The hook event: `"prompt"` or `"tool_call"` (see [The tool call frame](#the-tool-call-frame)). Other event types will be introduced in the future, so handle an unrecognized value gracefully (see [Forward compatibility](#forward-compatibility)).                  |
| `request_id` | string         | Opaque per-frame identifier for correlation. Equals the `webhook-id` header.                                                                                                                                                                                          |
| `tenant_id`  | string or null | Opaque identifier for the organization the request belongs to.                                                                                                                                                                                                        |
| `actor`      | object         | The principal the request is attributed to, discriminated on `type` (`"user"` is the only value sent today): `id` (a tagged identifier, stable across requests for the same account) and `email_address` (when available). Both `id` and `email_address` can be null. |
| `source`     | object         | The originating application: `application` (see [Source values](#source-values)).                                                                                                                                                                                     |
| `messages`   | array          | The conversation transcript up to the point of inference. See [Content blocks](#content-blocks).                                                                                                                                                                      |
| `session_id` | string or null | Opaque conversation identifier, when one exists. Don't parse it. For Claude Code it is a best-effort, client-asserted session identifier.                                                                                                                             |
| `model`      | string or null | Public model identifier for this request, when available.                                                                                                                                                                                                             |
| `metadata`   | object         | Reserved extension map of string keys to string values, sent empty today. Require nothing from it, and tolerate its absence, its presence, and any keys that appear.                                                                                                  |

An example request body:

```python
{
  "type": "prompt",
  "request_id": "req_abc123",
  "tenant_id": "11111111-1111-1111-1111-111111111111",
  "actor": {
    "type": "user",
    "id": "user_01AbCdEfGhIjKlMnOpQrStUv",
    "email_address": "alice@example.com"
  },
  "source": {
    "application": "claude-ai"
  },
  "session_id": "22222222-2222-2222-2222-222222222222",
  "model": "claude-sonnet-4-5",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Summarize the attached report."
        },
        {
          "type": "attachment",
          "file_name": "q2-report.pdf",
          "media_type": "application/pdf",
          "size_bytes": 48213,
          "text": "Q2 revenue grew 14% quarter over quarter..."
        }
      ]
    }
  ],
  "metadata": {}
}
```



### Content blocks

Each entry in `messages` has a `role` of `user` or `assistant` (tool results appear under the `user` role, matching the public Messages API content model) and a `content` array of blocks discriminated by `type`:

| Block `type`  | Fields                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `text`        | `text`: the text content.                                                                                                                                                                                                                                                                                                                                                                    |
| `tool_use`    | `id`: the identifier the matching tool result references. `tool_name`: the tool's name. `input`: the arguments the model passed to the tool. `tool_info`: on a tool call frame only (left out elsewhere, never `null`), an object that says who runs or provides the tool; see [The tool call frame](#the-tool-call-frame).                                                                  |
| `tool_result` | `content`: the tool's output as text, with parts joined by newlines; binary parts such as images are replaced by placeholder markers, and raw bytes are never sent. `is_error`: whether the tool call failed. `tool_name`: the tool's name, so a policy can condition on tool identity without cross-referencing an earlier block. `tool_use_id`: the `id` of the matching `tool_use` block. |
| `attachment`  | `file_name`: the original file name or path. `media_type`: the attachment's media type. `size_bytes`: the size of the original file. `text`: the text content of the attachment when available, such as extracted document text, an audio transcript, or link metadata. Raw attachment bytes are never sent.                                                                                 |

Apart from `type`, a `text` block's `text`, and a `tool_result` block's `content` and `is_error`, any of these fields can be `null` when the value isn't known; for example, an image arrives as an `attachment` block with `file_name` and `text` set to `null`.

A block whose `type` you don't recognize is a forward-compatible addition. The only field it guarantees is `type`; your policy may inspect whatever other fields are present, but must not reject the request because of an unrecognized type.

### What the transcript contains

The transcript is the conversation as the end user sees it, up to the point of inference: transcript text, tool calls and their results, extracted attachment text, and prior turns. It never includes system prompts, tool definitions, Anthropic-internal context, Claude's hidden reasoning, or raw file bytes.

A turn whose every block is excluded is omitted entirely, so don't assume strict user and assistant alternation.

Transcripts are sent untruncated, so a long conversation with large attachments produces a large request body. In practice the model's context window keeps bodies under about 10 MB, but the protocol allows up to 64 MiB. Several common defaults are much smaller, including nginx `client_max_body_size` at 1 MB and Express `express.json()` at 100 kB, and a rejected body counts as a webhook failure, so under **Allow the request** failure handling an oversized prompt would reach the model uninspected.

### Source values

`source.application` is an open string, not a closed enum. Common values are `claude-ai`, `claude-code`, and `cowork`; [connection tests](manage-claude-inference-hooks-configuration.md) and automatic circuit-breaker [recovery checks](#circuit-breaker) use `config-test`. New values may appear, and your server must not reject a request because of one it doesn't recognize.

Treat `source.application` as advisory routing metadata, not a trust boundary: don't rest a security-critical policy decision on it alone.

## The tool call frame

When Claude produces tool calls, Anthropic sends one tool call frame that lists them. Calls to some of claude.ai's own tools may be left out, and a response whose only tool calls are left out doesn't produce a tool call frame; see [Availability](manage-claude-inference-hooks.md#availability). One verdict covers the whole frame: you can't allow some tool calls and deny others. The frame goes to the same endpoint as the prompt frame, with the same headers, signature, and top-level fields. Tool calls made by code that Claude runs in the code execution tool are sent the same way, in separate tool call frames, before they run.

It differs from the prompt frame in three ways:

- `type` is `"tool_call"`.
- `messages` holds only the latest message, the `assistant` message Claude just produced: any `text` blocks and one `tool_use` block for each tool call the frame lists, in the order the model produced them. Earlier conversation is left out, because the prompt frame sent before that model call carried it. Read the last entry of `messages`, because the protocol may later add earlier messages before it.
- Each `tool_use` block carries a `tool_info` object that says who runs or provides the tool.

Where `session_id` is set, it is the same on both frames. The tool call frame has its own `request_id`, which is opaque like the prompt frame's.

`tool_info` says who runs or provides the tool, not what the tool can reach. It is one of four kinds, told apart by its `type` field, and each kind carries its own fields. Anthropic sends the first of the following kinds that fits the tool. New kinds may appear: accept a `type` you don't recognize, and for such a kind rely only on `type`.

An optional field that doesn't apply is left out, never `null`, so a `tool_info` can be just `{"type": "client"}`. `tool_name` is chosen by whoever defined the tool, and a server's `toolset_name` by whoever wrote the request or named the connector. Don't treat either as a trust boundary.

### Platform tools

A platform tool is one that the Claude API itself runs while it serves the request, such as web search or code execution.

| Field          | Present  | Description                                                                                                         |
|----------------|----------|---------------------------------------------------------------------------------------------------------------------|
| `type`         | Always   | `"platform"`                                                                                                        |
| `tool_type`    | Always   | The tool's versioned type, such as `web_search_20250305`. Match it exactly; don't parse a name or a date out of it. |
| `toolset_name` | Optional | The group of tools it belongs to.                                                                                   |

### Application tools

An application tool is one that the Anthropic application making the request provides itself, such as claude.ai's own tools.

| Field          | Present  | Description                       |
|----------------|----------|-----------------------------------|
| `type`         | Always   | `"application"`                   |
| `toolset_name` | Optional | The group of tools it belongs to. |

A `tool_use` block for a web search tool that claude.ai provides itself:

```python
{
  "type": "tool_use",
  "id": "toolu_01LmNoPqRsTuVwXyZaBcDeFg",
  "tool_name": "web_search",
  "input": {
    "query": "comparable deals for unannounced 4.2B USD Acme Corp acquisition"
  },
  "tool_info": {
    "type": "application"
  }
}
```



claude.ai doesn't always name this tool `web_search`, so don't match on the name alone. `input` always includes the search query and can hold other fields.

### Third-party tools

A third-party tool is one on a server that Anthropic knows of, such as a claude.ai connector or an MCP server that the request names in `mcp_servers`. This doesn't mean Anthropic has vetted the server. In voice mode, a call to a claude.ai connector's tool is `"client"` instead.

| Field             | Present              | Description                                                                                                                                                            |
|-------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`            | Always               | `"third_party"`                                                                                                                                                        |
| `toolset_name`    | Optional             | For a server in `mcp_servers`, the name the request gives the server. For any other server, such as a claude.ai connector, the server's name, copied from `tool_name`. |
| `origin`          | Optional             | The scheme, host, and non-default port of the server's URL. It can be a private or local address, `localhost` included. An absent `origin` means unknown, not safe.    |
| `verified_origin` | Whenever `origin` is | `true` only when Anthropic's servers connect to the server themselves. Treat `false` as an origin that Anthropic hasn't confirmed.                                     |

A `tool_use` block for a tool on an MCP server that the request names `crm` in `mcp_servers`:

```python
{
  "type": "tool_use",
  "id": "toolu_01GhIjKlMnOpQrStUvWxYzAb",
  "tool_name": "crm_search",
  "input": {
    "query": "accounts renewing in Q4"
  },
  "tool_info": {
    "type": "third_party",
    "toolset_name": "crm",
    "origin": "https://mcp.crm.example.com",
    "verified_origin": true
  }
}
```



A `tool_use` block for a tool on a Gmail connector, called in a claude.ai chat:

```python
{
  "type": "tool_use",
  "id": "toolu_01DeFgHiJkLmNoPqRsTuVwXy",
  "tool_name": "mcp__Gmail__search_threads",
  "input": {
    "query": "from:cfo@example.com newer_than:30d"
  },
  "tool_info": {
    "type": "third_party",
    "toolset_name": "Gmail",
    "origin": "https://gmail.mcp.example.com",
    "verified_origin": false
  }
}
```



For a claude.ai connector, `verified_origin` can be `false` even when Anthropic's servers connect to the server themselves.

A name copied from `tool_name` can differ from the name the user sees: `mcp__Google_Drive__search_files` gives `Google_Drive`, not `Google Drive`. It can also end in a short suffix (`Gmail-1a2b3c4d`), for example when another of the user's connectors has the same name. The name isn't a stable identifier and doesn't prove which server the tool is on. When `tool_name` has no server name in it, `toolset_name` is left out.

### Client tools

A client tool is any other tool, usually one that the application calling Claude runs. A tool that Anthropic defines but the calling application runs, such as bash or computer use, is a client tool too, and carries its versioned type in `tool_type`. A call to a tool the request doesn't declare is also `"client"`.

A tool on an MCP server that Claude Code connects to directly from the user's computer, such as a local MCP server, is a client tool. Its `tool_info` is `{"type": "client"}`, and its `tool_name` is the name Claude Code gives it, in the form `mcp__<server>__<tool>`.

A deny stops the call before Claude Code runs it. The exchange between Claude Code and a local server doesn't pass through Anthropic, so your AI security server sees the tool's result only when Claude Code sends it back. Its text is then in a `tool_result` block in the next prompt frame.

| Field          | Present  | Description                                                                                                                                    |
|----------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`         | Always   | `"client"`                                                                                                                                     |
| `tool_type`    | Optional | The tool's versioned type, such as `bash_20250124`, when Anthropic defines the tool. Match it exactly; don't parse a name or a date out of it. |
| `toolset_name` | Optional | The group of tools it belongs to, such as `browser`.                                                                                           |

A `tool_use` block for a tool that the calling application declares:

```python
{
  "type": "tool_use",
  "id": "toolu_01AbCdEfGhIjKlMnOpQrStUv",
  "tool_name": "read_file",
  "input": {
    "path": "reports/q3.txt"
  },
  "tool_info": {
    "type": "client"
  }
}
```



A `tool_use` block for bash, which Anthropic defines and the calling application runs:

```python
{
  "type": "tool_use",
  "id": "toolu_01HiJkLmNoPqRsTuVwXyZaBc",
  "tool_name": "bash",
  "input": {
    "command": "ls -la reports/"
  },
  "tool_info": {
    "type": "client",
    "tool_type": "bash_20250124"
  }
}
```



## Return a verdict

Respond with HTTP 200 and a JSON verdict body for both outcomes; the `action` field discriminates. To allow the request:

```python
{
  "action": "allow"
}
```



To deny it:

```python
{
  "action": "deny",
  "deny_reason": "This prompt appears to contain customer payment card data, which your organization's policy does not allow.",
  "reference_id": "scan_01HXPT4R9V"
}
```



| Field          | Constraints                                                     | Semantics                                                                                                                                                                                                                                                                |
|----------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `action`       | `"allow"` or `"deny"`; required                                 | `allow` lets inference proceed; `deny` rejects it.                                                                                                                                                                                                                       |
| `deny_reason`  | string or null; at most 500 characters, longer values truncated | Shown to the end user when `action` is `deny`; ignored on `allow`.                                                                                                                                                                                                       |
| `reference_id` | string or null; at most 50 characters from `[A-Za-z0-9._:/-]`   | Your own identifier for this evaluation. It's recorded on the denial's `inference_hooks_request_denied` [compliance activity](manage-claude-compliance-activity-feed.md) and never shown to the end user. Keep it opaque: no request content and no personal data. |

A deny is never discarded over a formatting problem: an oversize `deny_reason` is truncated, a malformed `reference_id` is silently dropped, and the `action` is still honored.

The reverse doesn't hold. Anything other than HTTP 200 with a parseable verdict is a webhook failure, and your organization's [failure handling](manage-claude-inference-hooks-configuration.md) applies instead of a verdict. In particular:

- Don't signal a deny with an error status. A non-200 response is a failure, not a deny.
- Any `action` value other than `allow` or `deny` is treated as a webhook failure.

Anthropic reads at most 64 KiB of the response body, and the body must be uncompressed. Redirects are not followed, and cookies are ignored. Unknown fields in the verdict body are ignored, so you can return a richer object alongside the fields documented here.

A tool call frame takes the same verdict body, and every rule in this section applies to it unchanged. `allow` lets the tool calls run and the response continues; `deny` stops all of them and ends the response with the same error as a denied prompt, including your `deny_reason`. Text delivered before the first tool call is not taken back.

## Verify the signature

Requests are signed according to the [Standard Webhooks](https://www.standardwebhooks.com/) specification, using three headers. Anthropic sends the header names in lowercase, and proxies are free to re-case them, so look them up case-insensitively.

| Header              | Contents                                                                                                                                                                                                         |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `webhook-id`        | Unique identifier for this delivery. Equals the body's `request_id`. Use it as an idempotency key and as the first component of the signed payload.                                                              |
| `webhook-timestamp` | Unix time in seconds, as a decimal string, when the request was signed. Reject a timestamp more than 5 minutes from your server's clock, in either direction.                                                    |
| `webhook-signature` | One or more space-separated `v1,<base64>` values, each an HMAC-SHA256 over `{webhook-id}.{webhook-timestamp}.{raw body bytes}`. Accept the request if any value matches yours, using a constant-time comparison. |

Two details cause most verification bugs:

- **Verify raw bytes.** Compute the HMAC over the body exactly as received, before any JSON parsing or re-encoding.
- **Decode the secret with a standard base64 decoder.** The signing secret is the value after the `whsec_` prefix, encoded with the standard base64 alphabet (`+` and `/`), as is the signature in the header. A URL-safe decoder derives the wrong key bytes whenever the secret contains `+` or `/`, which is most of the time.

Once your organization has a signing secret, every request Anthropic sends is signed, including the connection test, because the setup flow generates the secret before the first test. [Enabling Inference hooks requires a secret](manage-claude-inference-hooks-configuration.md), so reject any request that arrives unsigned. One exception: an organization that enabled Inference hooks before the secret was required keeps sending unsigned requests until its administrator generates one. Accept unsigned requests only until your administrator confirms the secret exists, then reject them.

[Rotating the secret](manage-claude-inference-hooks-configuration.md#rotate-your-signing-secret) is an immediate cutover, but requests signed with the previous secret can still arrive for about a minute afterward, plus anything already in flight. Have your AI security server accept signatures from both secrets during the switchover so those stragglers aren't rejected.

The following samples are server implementations, so there is no shell tab: an AI security server is a long-running HTTPS service rather than a one-shot request. Each sample uses only the language's standard library; the [Standard Webhooks](https://www.standardwebhooks.com/) project also publishes verification libraries for most languages.

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python



```python
import base64
import hashlib
import hmac
import time

TOLERANCE_SECONDS = 300


def verify(secret: str, headers: dict[str, str], body: bytes) -> bool:
    """Return True if the body was signed by Anthropic for this organization.

    Anthropic sends header names in lowercase, but proxies are free to
    re-case them, so normalize the lookup to lowercase.
    """
    lowercased = {name.lower(): value for name, value in headers.items()}
    try:
        message_id = lowercased["webhook-id"]
        timestamp = lowercased["webhook-timestamp"]
        signatures = lowercased["webhook-signature"]
    except KeyError:
        return False  # unsigned request: not from Anthropic

    try:
        signed_at = int(timestamp)
    except ValueError:
        return False
    if abs(time.time() - signed_at) > TOLERANCE_SECONDS:
        return False  # replayed, or the clocks disagree

    try:
        key = base64.b64decode(secret.removeprefix("whsec_"), validate=True)
    except ValueError:
        return False  # misconfigured secret: reject rather than crash

    payload = f"{message_id}.{timestamp}.".encode() + body
    expected = b"v1," + base64.b64encode(
        hmac.new(key, payload, hashlib.sha256).digest()
    )

    # Compare bytes: compare_digest on str raises on non-ASCII input.
    return any(
        hmac.compare_digest(expected, candidate.encode())
        for candidate in signatures.split()
    )
```

## Operational semantics

### Timeout and retry

Your administrator sets a verdict timeout between 1 and 10,000ms (5,000ms by default). The budget covers the entire exchange: connection, TLS handshake, request, and response. The same timeout applies to tool call frames.

Anthropic retries exactly once, after a 100ms delay, and only when the connection attempt fails. The retry shares the same timeout budget and carries the same `webhook-id` and the same signature. Once your AI security server has responded, the exchange is never retried.

### Webhook failures

Timeouts, non-200 statuses (redirects included), unparseable or oversized response bodies, and unreachable endpoints are all webhook failures. A webhook failure never becomes a deny; instead, your organization's [failure handling](manage-claude-inference-hooks-configuration.md) setting determines whether the affected request is blocked or proceeds without inspection.

### Circuit breaker

Sustained webhook failures attributable to your AI security server trip a circuit breaker that stops enforcement: Anthropic stops contacting your server, and failure handling applies to every request.

Starting 10 minutes after the trip, Anthropic checks whether your server has recovered: at most about once per minute it sends your server the same synthetic test request that **Test connection** sends (`source.application` is `config-test`), signed like any other request and carrying no user content. Respond to it normally. A valid verdict, allow or deny, resets the breaker and enforcement resumes; a webhook failure leaves the breaker tripped, and the checks continue. An administrator can also reset the breaker at any time, and administrator configuration changes stop the automatic checks; see [Circuit breaker](manage-claude-inference-hooks-configuration.md#circuit-breaker).

Prompt frames and tool call frames share one circuit breaker, and failures on either count toward it.

Each trip is recorded as an `inference_hooks_circuit_breaker_tripped` activity in the [Activity Feed](manage-claude-compliance-activity-feed.md), one activity for each trip. While the breaker is tripped, no per-request Inference hooks activities are recorded, so the trip activity is the feed's only record of the tripped window.

### Latency

Enforcement adds your AI security server's round trip to the latency of every governed request in your organization. With **Validate tool calls** on, a response that produces a tool call frame also waits for its verdict, in shadow mode as well. Keep the verdict fast, and load-test your server before rolling it out to a large organization.

### Source IP addresses

Requests to your AI security server originate from `160.79.106.0/24`, part of Anthropic's published [outbound IP ranges](../Endpoints/ip-addresses.md). Allowlist that block, not the inbound ranges on the same page, which don't cover it. Allowlisting narrows your server's exposure, but it is not a substitute for signature verification: the block carries Anthropic egress traffic beyond Inference hooks.

## Forward compatibility

The protocol grows without breaking correctly written servers. Your server must ignore:

- Unknown top-level fields on either frame.
- Unknown keys in `metadata`.
- New `source.application` values.
- New `actor.type` values. `actor` is a union discriminated on `type`, and `"user"` is the only kind sent today; a future kind guarantees only that `type` is present.
- Content blocks with an unrecognized `type`.
- Messages with a `role` other than `user` or `assistant`, which a later revision may add.

Never reject a request because of an unrecognized block type or field; read the fields you know and skip the rest.

Other hook event types will be introduced in the future. A new event type is an addition your server can't handle by skipping a field: the request still needs a verdict. When the top-level `type` is a value you don't recognize, return an allow verdict rather than an error status; an error response is a [webhook failure](#webhook-failures), and sustained failures trip the [circuit breaker](#circuit-breaker).

## Design your integration

A production AI security server makes a few design choices beyond the wire protocol.

**Deduplicate on `webhook-id`.** The `webhook-id` header is unique for each delivery and equals the body's `request_id`, and a connection-failure retry reuses it, so it works as an idempotency key. If you record verdicts, key the records on it.

**Record verdicts and join denials.** Store each verdict you return along with its `reference_id`. Every denial is recorded as an `inference_hooks_request_denied` compliance activity carrying the `reference_id` your server returned, so you can join denials in the [Activity Feed](manage-claude-compliance-activity-feed.md) to the matching records in your own system.

**Archive with an always-allow server.** To capture transcripts in real time without policing them, return `{"action": "allow"}` unconditionally and persist the frame after responding. This is a push-based alternative to polling the [Compliance API](manage-claude-compliance-api.md), and answering before you persist keeps your round trip out of the user's critical path.

**Write `deny_reason` for the end user.** The text you return is what the user sees when their request is blocked, truncated at 500 characters. Tell them what to change, such as which kind of content to remove, rather than emitting a scanner code that only your team can interpret.

## Next steps

[Configure Inference hooks](manage-claude-inference-hooks-configuration.md)

Enable Inference hooks, connect and test your endpoint, and control enforcement, failure handling, and rollout.

[Inference hooks overview](manage-claude-inference-hooks.md)

What Inference hooks are, how the verdict round trip works, and when to use them.
