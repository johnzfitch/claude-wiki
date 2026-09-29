---
title: "Develop an Inference hooks integration - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/inference-hooks-endpoint"
category: "04-API-Reference/Other"
fetched_at: "2026-09-22T06:29:53Z"
tags: ["api", "hooks", "prompting"]
---

### Cookie settings

We use cookies to deliver and improve our services, analyze site usage, and if you agree, to customize or personalize your experience and market our services to you. You can read our Cookie Policy [here](https://www.anthropic.com/legal/cookies).

CustomizeCustomize Cookie Settings

RejectReject All Cookies

AcceptAccept All Cookies


Claude Platform Docs

- [Messages](/docs/en/intro)

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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Finference-hooks-endpoint)





SearchCtrlK

Organization

[Admin API](/docs/en/manage-claude/admin-api)[User management](/docs/en/manage-claude/user-management)[Workspaces](/docs/en/manage-claude/workspaces)

Authentication

[Overview](/docs/en/manage-claude/authentication)[Create an Admin API key](/docs/en/manage-claude/admin-api-keys)[App Attest](/docs/en/manage-claude/app-attest)[Workload Identity Federation](/docs/en/manage-claude/workload-identity-federation)[Manage WIF via API](/docs/en/manage-claude/wif-admin-api)[WIF reference](/docs/en/manage-claude/wif-reference)

Identity providers

Monitoring

[Usage and Cost API](/docs/en/manage-claude/usage-cost-api)[Rate Limits API](/docs/en/manage-claude/rate-limits-api)[Analytics APIs](/docs/en/manage-claude/analytics-api)[Claude Code Analytics API](/docs/en/manage-claude/claude-code-analytics-api)[Spend Limits API](/docs/en/manage-claude/spend-limits-api)

Data & compliance

[Data residency](/docs/en/manage-claude/data-residency)[API and data retention](/docs/en/manage-claude/api-and-data-retention)[Access Transparency](/docs/en/manage-claude/access-transparency)

[Encryption keys](/docs/en/manage-claude/cmek)

[Inference hooks](/docs/en/manage-claude/inference-hooks)

[Overview](/docs/en/manage-claude/inference-hooks)[Configure Inference hooks](/docs/en/manage-claude/inference-hooks-configuration)[Build an integration](/docs/en/manage-claude/inference-hooks-endpoint)

Compliance API

[Overview](/docs/en/manage-claude/compliance-api)[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)[Activity Feed](/docs/en/manage-claude/compliance-activity-feed)[Chats, files, and projects](/docs/en/manage-claude/compliance-content-data)[Session transcripts](/docs/en/manage-claude/compliance-sessions)[Organizations, users, roles, groups, and settings](/docs/en/manage-claude/compliance-org-data)[Design your integration](/docs/en/manage-claude/compliance-integration-patterns)[Errors](/docs/en/manage-claude/compliance-errors)[FAQ](/docs/en/manage-claude/compliance-faq)

[Console](/)

[Admin](/docs/en/manage-claude/admin-api)Inference hooks

# Develop an Inference hooks integration

Copy page



Build the AI security server that receives signed Inference hooks requests, verifies them, and returns allow or deny verdicts.

Copy page





Inference hooks are in beta and available to Claude Enterprise organizations. Field names, request shapes, and headers may change during the beta.

An Inference hooks integration is an AI security server: an HTTPS service that Anthropic calls. For each governed request, your server receives a signed `POST` carrying the conversation transcript and responds with an allow or deny verdict. This page documents the protocol for building that server: the request and verdict schemas, signature verification, and the operational contract.

To turn Inference hooks on and point them at your endpoint, see [Configure Inference hooks](/docs/en/manage-claude/inference-hooks-configuration). To learn what Inference hooks are and when to use them, see the [Inference hooks overview](/docs/en/manage-claude/inference-hooks).

## Get a first verdict round trip

The smallest working integration is a server that reads each request and allows it. Run one of the following servers, expose it at a public `https://` URL (for example, behind a TLS-terminating reverse proxy on a host you control, not a reverse-tunnel service; see [Receive a request](#receive-a-request)), then have your administrator [set it as the endpoint and test the connection](/docs/en/manage-claude/inference-hooks-configuration): the **Test connection** result reports the allow verdict your server returned.

Python

TypeScript

C#

Go

Java

PHP

Ruby

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

Host your AI security server where Anthropic can reach it: an `https://` URL on port 443, on a publicly routable host (private, loopback, and carrier-grade NAT ranges are refused at connect time), with a certificate that validates against the public CA trust store, responding without redirects. The configured URL must be the final destination. Reverse-tunnel hosts (ngrok and similar tunnel services) are not supported: Anthropic's network policy blocks them. Host your server on a domain you control. [Configure Inference hooks](/docs/en/manage-claude/inference-hooks-configuration) covers how your administrator sets and tests the URL.

Every request carries these fixed headers, along with any [custom request headers](/docs/en/manage-claude/inference-hooks-configuration) your administrator configured and, once your organization has a signing secret, the `webhook-*` signature headers described in [Verify the signature](#verify-the-signature):

| Header            | Value              |
|-------------------|--------------------|
| `Content-Type`    | `application/json` |
| `User-Agent`      | `anthropic-dlp/1`  |
| `Accept-Encoding` | `identity`         |

There is one hook event today: the prompt frame, sent once per governed inference request, before inference begins. Anthropic holds the request until your AI security server responds or the verdict timeout elapses.

## The prompt frame

The request body is a JSON object with these fields:

| Field        | Type           | Description                                                                                                                                                                                                                                                           |
|--------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`       | string         | The hook event. Always `"prompt"` today; other event types will be introduced in the future, so handle an unrecognized value gracefully (see [Forward compatibility](#forward-compatibility)).                                                                        |
| `request_id` | string         | Opaque per-inference-call identifier for correlation. Equals the `webhook-id` header.                                                                                                                                                                                 |
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
| `tool_use`    | `id`: the identifier the matching tool result references. `tool_name`: the tool's name. `input`: the arguments the model passed to the tool.                                                                                                                                                                                                                                                 |
| `tool_result` | `content`: the tool's output as text, with parts joined by newlines; binary parts such as images are replaced by placeholder markers, and raw bytes are never sent. `is_error`: whether the tool call failed. `tool_name`: the tool's name, so a policy can condition on tool identity without cross-referencing an earlier block. `tool_use_id`: the `id` of the matching `tool_use` block. |
| `attachment`  | `file_name`: the original file name or path. `media_type`: the attachment's media type. `size_bytes`: the size of the original file. `text`: the text content of the attachment when available, such as extracted document text, an audio transcript, or link metadata. Raw attachment bytes are never sent.                                                                                 |

Apart from `type`, a `text` block's `text`, and a `tool_result` block's `content` and `is_error`, any of these fields can be `null` when the value isn't known; for example, an image arrives as an `attachment` block with `file_name` and `text` set to `null`.

A block whose `type` you don't recognize is a forward-compatible addition. The only field it guarantees is `type`; your policy may inspect whatever other fields are present, but must not reject the request because of an unrecognized type.

### What the transcript contains

The transcript is the conversation as the end user sees it, up to the point of inference: transcript text, tool calls and their results, extracted attachment text, and prior turns. It never includes system prompts, tool definitions, Anthropic-internal context, Claude's hidden reasoning, or raw file bytes.

A turn whose every block is excluded is omitted entirely, so don't assume strict user and assistant alternation.

Transcripts are sent untruncated, so a long conversation with large attachments produces a large request body. In practice the model's context window keeps bodies under about 10 MB, but the protocol allows up to 64 MiB. Several common defaults are much smaller, including nginx `client_max_body_size` at 1 MB and Express `express.json()` at 100 kB, and a rejected body counts as a webhook failure, so under **Allow the request** failure handling an oversized prompt would reach the model uninspected.

### Source values

`source.application` is an open string, not a closed enum. Common values are `claude-ai`, `claude-code`, and `cowork`; [connection tests](/docs/en/manage-claude/inference-hooks-configuration) and automatic circuit-breaker [recovery checks](#circuit-breaker) use `config-test`. New values may appear, and your server must not reject a request because of one it doesn't recognize.

Treat `source.application` as advisory routing metadata, not a trust boundary: don't rest a security-critical policy decision on it alone.

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
| `reference_id` | string or null; at most 50 characters from `[A-Za-z0-9._:/-]`   | Your own identifier for this evaluation. It's recorded on the denial's `inference_hooks_request_denied` [compliance activity](/docs/en/manage-claude/compliance-activity-feed) and never shown to the end user. Keep it opaque: no request content and no personal data. |

A deny is never discarded over a formatting problem: an oversize `deny_reason` is truncated, a malformed `reference_id` is silently dropped, and the `action` is still honored.

The reverse doesn't hold. Anything other than HTTP 200 with a parseable verdict is a webhook failure, and your organization's [failure handling](/docs/en/manage-claude/inference-hooks-configuration) applies instead of a verdict. In particular:

- Don't signal a deny with an error status. A non-200 response is a failure, not a deny.
- Any `action` value other than `allow` or `deny` is treated as a webhook failure.

Anthropic reads at most 64 KiB of the response body, and the body must be uncompressed. Redirects are not followed, and cookies are ignored. Unknown fields in the verdict body are ignored, so you can return a richer object alongside the fields documented here.

## Verify the signature

Requests are signed per the [Standard Webhooks](https://www.standardwebhooks.com/) specification, using three headers. Anthropic sends the header names in lowercase, and proxies are free to re-case them, so look them up case-insensitively.

| Header              | Contents                                                                                                                                                                                                         |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `webhook-id`        | Unique identifier for this delivery. Equals the body's `request_id`. Use it as an idempotency key and as the first component of the signed payload.                                                              |
| `webhook-timestamp` | Unix time in seconds, as a decimal string, when the request was signed. Reject a timestamp more than five minutes from your server's clock, in either direction.                                                 |
| `webhook-signature` | One or more space-separated `v1,<base64>` values, each an HMAC-SHA256 over `{webhook-id}.{webhook-timestamp}.{raw body bytes}`. Accept the request if any value matches yours, using a constant-time comparison. |

Two details cause most verification bugs:

- **Verify raw bytes.** Compute the HMAC over the body exactly as received, before any JSON parsing or re-encoding.
- **Decode the secret with a standard base64 decoder.** The signing secret is the value after the `whsec_` prefix, encoded with the standard base64 alphabet (`+` and `/`), as is the signature in the header. A URL-safe decoder derives the wrong key bytes whenever the secret contains `+` or `/`, which is most of the time.

Once your organization has a signing secret, every request Anthropic sends is signed, including the connection test, because the setup flow generates the secret before the first test. [Enabling Inference hooks requires a secret](/docs/en/manage-claude/inference-hooks-configuration), so reject any request that arrives unsigned. One exception: an organization that enabled Inference hooks before the secret was required keeps sending unsigned requests until its administrator generates one. Accept unsigned requests only until your administrator confirms the secret exists, then reject them.

[Rotating the secret](/docs/en/manage-claude/inference-hooks-configuration#rotate-your-signing-secret) is an immediate cutover, but requests signed with the previous secret can still arrive for about a minute afterward, plus anything already in flight. Have your AI security server accept signatures from both secrets during the switchover so those stragglers aren't rejected.

The following samples are server implementations, so there is no shell tab: an AI security server is a long-running HTTPS service rather than a one-shot request. Each sample uses only the language's standard library; the [Standard Webhooks](https://www.standardwebhooks.com/) project also publishes verification libraries for most languages.

Python

TypeScript

C#

Go

Java

PHP

Ruby

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

Your administrator sets a verdict timeout between 1 and 10,000ms (5,000ms by default). The budget covers the entire exchange: connection, TLS handshake, request, and response.

Anthropic retries exactly once, after a 100ms delay, and only when the connection attempt fails. The retry shares the same timeout budget and carries the same `webhook-id` and the same signature. Once your AI security server has responded, the exchange is never retried.

### Webhook failures

Timeouts, non-200 statuses (redirects included), unparseable or oversized response bodies, and unreachable endpoints are all webhook failures. A webhook failure never becomes a deny; instead, your organization's [failure handling](/docs/en/manage-claude/inference-hooks-configuration) setting decides whether the affected request is blocked or proceeds without inspection.

### Circuit breaker

Sustained webhook failures attributable to your AI security server trip a circuit breaker that stops enforcement: Anthropic stops contacting your server, and failure handling applies to every request.

Starting 10 minutes after the trip, Anthropic checks whether your server has recovered: at most about once per minute it sends your server the same synthetic test request that **Test connection** sends (`source.application` is `config-test`), signed like any other request and carrying no user content. Respond to it normally. A valid verdict, allow or deny, resets the breaker and enforcement resumes; a webhook failure leaves the breaker tripped, and the checks continue. An administrator can also reset the breaker at any time, and administrator configuration changes stop the automatic checks; see [Circuit breaker](/docs/en/manage-claude/inference-hooks-configuration#circuit-breaker).

Each trip is recorded as an `inference_hooks_circuit_breaker_tripped` activity in the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed), one activity per trip. While the breaker is tripped, no per-request Inference hooks activities are recorded, so the trip activity is the feed's only record of the tripped window.

### Latency

Enforcement adds your AI security server's round trip to the latency of every governed request in your organization. Keep the verdict fast, and load-test your server before rolling it out to a large organization.

### Source IP addresses

Requests to your AI security server originate from `160.79.106.0/24`, part of Anthropic's published [outbound IP ranges](/docs/en/api/ip-addresses). Allowlist that block, not the inbound ranges on the same page, which don't cover it. Allowlisting narrows your server's exposure, but it is not a substitute for signature verification: the block carries Anthropic egress traffic beyond Inference hooks.

## Forward compatibility

The protocol grows without breaking correctly written servers. Your server must ignore:

- Unknown top-level fields on the prompt frame.
- Unknown keys in `metadata`.
- New `source.application` values.
- New `actor.type` values. `actor` is a union discriminated on `type`, and `"user"` is the only kind sent today; a future kind guarantees only that `type` is present.
- Content blocks with an unrecognized `type`.

Never reject a request because of an unrecognized block type or field; read the fields you know and skip the rest.

Other hook event types will be introduced in the future. A new event type is an addition your server can't handle by skipping a field: the request still needs a verdict. When the top-level `type` is a value you don't recognize, return an allow verdict rather than an error status; an error response is a [webhook failure](#webhook-failures), and sustained failures trip the [circuit breaker](#circuit-breaker).

## Design your integration

A production AI security server makes a few design choices beyond the wire protocol.

**Deduplicate on `webhook-id`.** The `webhook-id` header is unique per delivery and equals the body's `request_id`, and a connection-failure retry reuses it, so it works as an idempotency key. If you record verdicts, key the records on it.

**Record verdicts and join denials.** Store each verdict you return along with its `reference_id`. Every denial is recorded as an `inference_hooks_request_denied` compliance activity carrying the `reference_id` your server returned, so you can join denials in the [Activity Feed](/docs/en/manage-claude/compliance-activity-feed) to the matching records in your own system.

**Archive with an always-allow server.** To capture transcripts in real time without policing them, return `{"action": "allow"}` unconditionally and persist the frame after responding. This is a push-based alternative to polling the [Compliance API](/docs/en/manage-claude/compliance-api), and answering before you persist keeps your round trip out of the user's critical path.

**Write `deny_reason` for the end user.** The text you return is what the user sees when their request is blocked, truncated at 500 characters. Tell them what to change, such as which kind of content to remove, rather than emitting a scanner code that only your team can interpret.

## Next steps

[Configure Inference hooks](/docs/en/manage-claude/inference-hooks-configuration)

Enable Inference hooks, connect and test your endpoint, and control enforcement, failure handling, and rollout.

[Inference hooks overview](/docs/en/manage-claude/inference-hooks)

What Inference hooks are, how the verdict round trip works, and when to use them.
