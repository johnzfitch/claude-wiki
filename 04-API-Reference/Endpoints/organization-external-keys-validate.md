---
title: "Validate External Key - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/external_keys/validate"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:52Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/validate).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [External Keys](https://platform.claude.com/docs/en/api/http/organization/external_keys)

# Validate External Key

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

POST/v1/organizations/external_keys/{external_key_id}/validate

Validate an external key config against the customer's KMS.

Anthropic performs an encrypt/decrypt roundtrip against the configured KMS key and waits up to 30 seconds for the result. The response status is `success` if the roundtrip succeeded, or `failure` with an error message if it failed or timed out.

##### Path parameters



external_key_id: string



ID of the External Key.

maxLength2048

##### Headers



"anthropic-version": optional string



The version of the Claude API you want to use.

Read more about versioning and our version history [here](versioning.md).

##### Returns



type: "external_key_validation"



defaultexternal_key_validation

error: string or null



Error message when status is `failure`. Null otherwise.



status: "failure" or "success"



`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

One of the following:

"failure"



"success"



Validate External Key

cURL



```python
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID/validate \
    -X POST \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "error": "error",
  "status": "failure",
  "type": "external_key_validation"
}
```

##### Returns Examples

Response 200



```python
{
  "error": "error",
  "status": "failure",
  "type": "external_key_validation"
