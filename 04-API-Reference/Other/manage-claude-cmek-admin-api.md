---
title: "Add and attach an encryption key with the Admin API - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek-admin-api"
category: "04-API-Reference/Other"
fetched_at: "2026-11-17T06:24:44Z"
tags: ["api"]
---

# Add and attach an encryption key with the Admin API

Copy page



Create, validate, and attach a customer-managed encryption key with three Admin API calls.

Copy page



These calls work on Claude Platform. On Claude Enterprise or Claude Platform on AWS, follow [your setup page](manage-claude-cmek.md#set-it-up).

Creating an external key is what **Add key** does in the Claude Console, and validating it is what **Verify** does.

## Before you start

- Customer-managed encryption keys (CMEK) are [turned on for your organization](manage-claude-cmek.md#availability).
- You have an [Admin API key](manage-claude-admin-api-keys.md). The samples read it from `ANTHROPIC_API_KEY`.
- You’ve created your key in [AWS KMS](manage-claude-cmek-aws-kms.md#encryption-key-setup), [Google Cloud KMS](manage-claude-cmek-google-cloud-kms.md#encryption-key-setup), or [Azure Key Vault](manage-claude-cmek-azure-key-vault.md#encryption-key-setup), and kept the values the setup steps tell you to copy.
- You have a workspace that [retains data](manage-claude-cmek-data-retention.md#data-retention), ideally a new one, because [existing data stays under Anthropic’s key](manage-claude-cmek-how-it-works.md#when-your-key-takes-effect).

## Create, validate, and attach the key

1.  1

    ### Create the external key

    AWS
    Google Cloud
    Azure

    AWS

    Replace `<friendly-name>` with a display name and `<key-arn-from-create-key-step>` with the key ARN.

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    client = anthropic.Anthropic()

    external_key = client.organization.external_keys.create(
        display_name="<friendly-name>",
        geo="us",
        provider_config={"type": "aws", "kms_arn": "<key-arn-from-create-key-step>"},
    )

    print(f"id: {external_key.id}")
    print(f"display_name: {external_key.display_name}")
    ```

    Google Cloud

    Replace `<friendly-name>` with a display name. Replace the value that starts with `projects/` with the full key resource name.

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    client = anthropic.Anthropic()

    external_key = client.organization.external_keys.create(
        display_name="<friendly-name>",
        geo="us",
        provider_config={
            "type": "gcp",
            "key_name": "projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>",
        },
    )

    print(f"id: {external_key.id}")
    print(f"display_name: {external_key.display_name}")
    ```

    Azure

    Replace the placeholders:

    - `<friendly-name>`: a display name
    - `https://<your-vault-name>.vault.azure.net/`: the vault URI
    - `<your-key-name>`: the key name
    - `<your-tenant-id>`: the vault’s tenant ID

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    client = anthropic.Anthropic()

    external_key = client.organization.external_keys.create(
        display_name="<friendly-name>",
        geo="us",
        provider_config={
            "type": "azure",
            "vault_uri": "https://<your-vault-name>.vault.azure.net/",
            "key_name": "<your-key-name>",
            "tenant_id": "<your-tenant-id>",
        },
    )

    print(f"id: {external_key.id}")
    print(f"display_name: {external_key.display_name}")
    ```

    The `id` in the response is the external key ID. Copy it for the next two steps.

    ``` shiki
    {
      "type": "external_key",
      "id": "ekey_<id>",
      "display_name": "<friendly-name>"
    }
    ```

    

2.  2

    ### Validate the key

    Replace `ekey_<id>` with the external key ID.

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    client = anthropic.Anthropic()

    validation = client.organization.external_keys.validate("ekey_<id>")

    print(f"status: {validation.status}")
    print(f"error: {validation.error}")
    ```

    A successful response looks like this:

    ``` shiki
    { "type": "external_key_validation", "status": "success", "error": null }
    ```

    

    If `status` is `failure`, the `error` field says why. See [Troubleshoot CMEK](manage-claude-cmek-troubleshooting.md).

3.  3

    ### Attach the key to a workspace

    
    Attaching a key [can’t be undone](manage-claude-cmek-key-lifecycle.md#what-each-action-does). If the key is deleted, Anthropic can’t recover the data it protects.

    Replace `<workspace-id>` with the workspace ID, which starts with `wrkspc_`, and `ekey_<id>` with the external key ID.

    cURL
    CLI
    Python
    TypeScript
    C#
    Go
    Java
    PHP
    Ruby

    Python

    

    ``` shiki
    client = anthropic.Anthropic()

    workspace = client.organization.workspaces.update(
        "<workspace-id>", external_key_id="ekey_<id>"
    )

    print(f"id: {workspace.id}")
    print(f"external_key_id: {workspace.external_key_id}")
    ```

    The response shows the attached key’s ID in `external_key_id`. If the request is refused, [look up the error](manage-claude-cmek-troubleshooting.md#refused).
