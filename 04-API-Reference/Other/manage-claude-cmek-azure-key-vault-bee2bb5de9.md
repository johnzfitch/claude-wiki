---
title: "Configure Azure Key Vault for CMEK - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek-azure-key-vault"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:42Z"
tags: ["api"]
---

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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fcmek-azure-key-vault)

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

[Overview](/docs/en/manage-claude/cmek)[AWS KMS](/docs/en/manage-claude/cmek-aws-kms)[Google Cloud KMS](/docs/en/manage-claude/cmek-google-cloud-kms)[Azure Key Vault](/docs/en/manage-claude/cmek-azure-key-vault)

[Inference hooks](/docs/en/manage-claude/inference-hooks)

Compliance API

[Overview](/docs/en/manage-claude/compliance-api)[Set up the Compliance API](/docs/en/manage-claude/compliance-api-access)[Activity Feed](/docs/en/manage-claude/compliance-activity-feed)[Chats, files, and projects](/docs/en/manage-claude/compliance-content-data)[Session transcripts](/docs/en/manage-claude/compliance-sessions)[Organizations, users, roles, groups, and settings](/docs/en/manage-claude/compliance-org-data)[Design your integration](/docs/en/manage-claude/compliance-integration-patterns)[Errors](/docs/en/manage-claude/compliance-errors)[FAQ](/docs/en/manage-claude/compliance-faq)

[Console](/)

[Admin](/docs/en/manage-claude/admin-api)Encryption keys

# Configure Azure Key Vault for CMEK

Copy page



Use Azure Key Vault to provide an encryption key for your organization.

Copy page



Configure with the /claude-api skill in Claude Code



```python
claude "/claude-api help me configure a customer-managed encryption key with Azure Key Vault"
```

This guide walks through configuring an Azure Key Vault key as a [customer-managed encryption key (CMEK)](/docs/en/manage-claude/cmek) for your Anthropic organization.



Enabling CMEK is permanent. If your Key Vault key is deleted or disabled, Anthropic cannot recover the data encrypted under it. Review the [warnings and limitations](/docs/en/manage-claude/cmek) before you start.

## Prerequisites

- An Azure Key Vault with **RBAC authorization enabled** (`enableRbacAuthorization: true`) and **public network access allowed**. Anthropic calls your vault over the public data-plane endpoint; private endpoints are not supported.
- **Purge protection enabled** (`enablePurgeProtection: true`) on the vault. Without it, a deleted key can be permanently purged during the soft-delete retention window, causing irreversible loss of your CMEK-protected data. Purge protection cannot be disabled once enabled.
- Permissions to create keys in the vault and to assign RBAC roles on it.
- Permissions to create service principals in your Entra tenant (`Application Administrator`, `Cloud Application Administrator`, or an equivalent custom role).
- An Anthropic Admin API key for your organization.
- The [`az` CLI](https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest) installed and authenticated.
- **Diagnostic Settings** configured on the vault to route the `AuditEvent` log category to Log Analytics, a storage account, or an event hub. Azure Key Vault does not emit data-plane audit logs (such as `KeyWrap`, `KeyUnwrap`, and `KeyGet`) by default, so without this you get no audit trail for Anthropic's key operations.

## Anthropic app information

To have Anthropic use your encryption key, you must configure an Anthropic multitenant application ID and display name. Those values are:

| Field                          | Value                                  |
|:-------------------------------|:---------------------------------------|
| Multitenant app client ID (US) | `8635ae1a-3e5d-44e8-a4ed-e0f614466f87` |
| App display name               | `anthropic-cmek-client-us`             |



Use only this published client ID and display name. Never trust an identifier provided over email, chat, or any onboarding channel.

## Encryption key setup

1.  1

    ### Consent to the Anthropic multitenant application

    This creates a service principal in your Entra tenant for Anthropic's CMEK client application. The application requests no Microsoft Graph permissions; it exists solely as a federation target for Key Vault data-plane access.

    ``` shiki
    az ad sp create --id 8635ae1a-3e5d-44e8-a4ed-e0f614466f87
    ```

    

    From the output, capture the `id` field. This is the service principal's object ID in your tenant, which you use when you assign the RBAC role.

    ``` shiki
    {
      "appId": "8635ae1a-3e5d-44e8-a4ed-e0f614466f87",
      "displayName": "anthropic-cmek-client-us",
      "id": "<sp-object-id>"
    }
    ```

    

    If the service principal already exists in your tenant (from a prior attempt or another integration), `az ad sp create` exits with an "already exists" error. Fetch its object ID instead:

    ``` shiki
    az ad sp show --id 8635ae1a-3e5d-44e8-a4ed-e0f614466f87 --query id -o tsv
    ```

    

    This step has no Portal equivalent. If you do not have the Azure CLI installed locally, open Cloud Shell from the Portal's top navigation bar. After the command succeeds, you can find the service principal's object ID in **Microsoft Entra ID \> Enterprise applications** by clearing the default application-type filter and searching for `anthropic-cmek-client-us`.

2.  2

    ### Create an RSA key in your vault

    Azure Key Vault does not support symmetric key wrapping, so the key must be RSA (3072-bit or larger) with `wrapKey` and `unwrapKey` in its allowed operations.

    The `--tags` option adds the organization tag, `anthropic-org-<ORGANIZATION_UUID>` with the value `true`, where `<ORGANIZATION_UUID>` is your Anthropic organization ID in lowercase. The tag is required for Anthropic to validate the key.

    
    **Finding your organization ID:** Copy the **Organization ID** field under **Settings \> Organization** in the Claude Console, or under **Organization settings \> Organization** in claude.ai, or read the `id` field from the [Organization Info](/docs/en/api/beta/organization/retrieve) endpoint. Use the bare UUID, not the `org_`-prefixed ID.

    ``` shiki
    az keyvault key create \
      --vault-name <VAULT_NAME> \
      --name <KEY_NAME> \
      --kty RSA --size 3072 \
      --ops wrapKey unwrapKey \
      --tags anthropic-org-<ORGANIZATION_UUID>=true
    ```

    

    For HSM-backed keys, use `--kty RSA-HSM` (requires a Premium-SKU vault). Software-protected RSA keys are acceptable for this integration.

    From the Portal, open your Key Vault, select **Keys**, then **Generate/Import**. Set the key type to RSA and the size to 3072 or larger. To restrict the key to wrap and unwrap only, open the key version, scroll to **Permitted operations**, and uncheck everything except **Wrap Key** and **Unwrap Key**.

    On the **Create a key** page, also add the organization tag under **Tags**.

    To share one key among several Anthropic organizations, add one such tag for each organization. A key version can carry at most 15 tags, including your own.

    
    To add the tag to a key you already have, open the key's current version in the Portal, select the link next to **Tags**, add the tag, and click **Save**. With the Azure CLI, run `az keyvault key set-attributes --vault-name <VAULT_NAME> --name <KEY_NAME> --tags anthropic-org-<ORGANIZATION_UUID>=true`. Its `--tags` option replaces the version's tags, so also put each tag the version already has in `--tags`, as `name=value`. For a key in a Managed HSM, use `--hsm-name <HSM_NAME>` instead of `--vault-name`.

3.  3

    ### Grant the Anthropic service principal access to your key

    Assign the `Key Vault Crypto User` role to the service principal from the first step, scoped to the **individual key** rather than the whole vault.

    ``` shiki
    VAULT_ID=$(az keyvault show --name <your-vault-name> --query id -o tsv)

    az role assignment create \
      --role "Key Vault Crypto User" \
      --assignee-object-id <sp-object-id> \
      --assignee-principal-type ServicePrincipal \
      --scope "${VAULT_ID}/keys/<your-key-name>"
    ```

    

    The built-in `Key Vault Crypto User` role grants key cryptographic operations (encrypt, decrypt, wrap, unwrap, sign, verify) plus key read on its assigned scope. The `--ops wrapKey unwrapKey` restriction you set on the key in the previous step further narrows which of those operations can succeed against this key, so in practice Anthropic can only wrap and unwrap.

    From the Portal, open the **key** (not the vault), select its **Access control (IAM)** tab, click **Add \> Add role assignment**, select **Key Vault Crypto User**, and assign it to the `anthropic-cmek-client-us` service principal.

    
    **Dedicated vault alternative:** Microsoft recommends a dedicated vault per application with roles assigned at the vault scope. If you provision a vault that holds only this Anthropic CMEK key, you can assign the role at the vault scope instead and the effect is identical. Scope to the individual key when the key lives in a shared vault.

4.  4

    ### Verify your vault configuration

    ``` shiki
    az keyvault show --name <your-vault-name> \
      --query "{rbac:properties.enableRbacAuthorization, purge:properties.enablePurgeProtection, pub:properties.publicNetworkAccess, net:properties.networkAcls.defaultAction, ipRules:properties.networkAcls.ipRules, uri:properties.vaultUri, tenantId:properties.tenantId}"
    ```

    

    Confirm that:

    - `rbac` is `true`.
    - `purge` is `true`. If it is `false` or `null`, enable purge protection on the vault before proceeding. Without it, a soft-deleted key can be permanently purged during the retention window, making your CMEK-protected data unrecoverable.
    - `pub` is `"Enabled"`. If it is `"Disabled"`, Anthropic cannot reach the vault over its public data-plane endpoint and validation fails.
    - `net` is `"Allow"`, or, if it is `"Deny"`, that `ipRules` include Anthropic's egress ranges (contact Anthropic for the current list).
    - `uri` is the vault URI you use when you register the key.
    - `tenantId` is the tenant that governs the vault. Use this value as `tenant_id` when you register the key, not the tenant of your currently-active subscription (the two can differ in cross-tenant setups).

## Register the key with Anthropic

How you register the key depends on which product you use.

Claude Platform

Claude Enterprise

You can set up the key in the Claude Console or through the Admin API, with the same result.

Claude Console

API

1.  1

    ### Register the key with Anthropic

    In the Claude Console, open **Settings \> Encryption keys** and click **Add key**. Enter a display name, choose **Azure Key Vault**, and click **Continue**. Fill in **Vault URI**, **Key name**, and **Tenant ID**, and click **Add**.

    The key details step shows the organization tag. Add it to the key, as [the create step](#organization-tag) describes, before you click **Add**.

2.  2

    ### Validate the key

    On the **Encryption keys** page, click **Verify** next to the key. **Connected** appears when the check passes. If it fails, a message gives the reason.

3.  3

    ### Attach the key to a workspace

    In the Claude Console, go to [Manage \> Security](/settings/workspaces/default/security-compliance) and select the workspace in the workspace picker at the top of the sidebar. Under **Encryption key**, select the key, click **Save**, and confirm. Attaching a key can't be undone. For a workspace that already receives requests, the key can take [up to a day to take effect](/docs/en/manage-claude/cmek#how-it-works).

## Terraform

For infrastructure-as-code deployments, the same steps map to the `azurerm` and `azuread` providers.
