---
title: "Delete External Key - Claude API Reference"
source_url: "https://platform.claude.com/docs/en/api/organization/external_keys/delete"
category: "04-API-Reference/Endpoints"
fetched_at: "2026-11-18T06:27:51Z"
tags: ["api"]
---

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL



A beta version of this method exists and may have additional functionality. [View the beta version](https://platform.claude.com/docs/en/api/http/beta/organization/external_keys/delete).

1.  [API reference](http.md)
2.  [Organization](https://platform.claude.com/docs/en/api/http/organization)
3.  [External Keys](https://platform.claude.com/docs/en/api/http/organization/external_keys)

# Delete External Key

Copy page



API version 2026-10-21

cURLCLITypeScriptPythonJavaGoRubyC#PHPcURL

DELETE/v1/organizations/external_keys/{external_key_id}

Delete an external key config.

The request is rejected if any workspace still references this config.

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

type: "external_key_deleted"



defaultexternal_key_deleted

id: string



ID of the deleted External Key.

Delete External Key

cURL



```python
curl https://api.anthropic.com/v1/organizations/external_keys/$EXTERNAL_KEY_ID \
    -X DELETE \
    -H 'anthropic-version: 2026-10-21' \
    -H "Authorization: Bearer $ANTHROPIC_API_KEY"
```

Response 200



```python
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```

##### Returns Examples

Response 200



```python
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
