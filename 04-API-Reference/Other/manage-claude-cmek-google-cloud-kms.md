---
title: "Configure Google Cloud KMS for CMEK - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms"
category: "04-API-Reference/Other"
fetched_at: "2026-10-20T06:37:53Z"
tags: ["api"]
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


[Console](playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fcmek-google-cloud-kms)





SearchCtrlK

Organization

[Admin API](manage-claude-admin-api.md)[User management](manage-claude-user-management.md)[Plugins API](manage-claude-plugins-api.md)[Workspaces](manage-claude-workspaces.md)

Authentication

[Overview](manage-claude-authentication.md)[Create an Admin API key](manage-claude-admin-api-keys.md)[App Attest](manage-claude-app-attest.md)[Workload Identity Federation](manage-claude-workload-identity-federation.md)[Manage WIF via API](manage-claude-wif-admin-api.md)[WIF reference](manage-claude-wif-reference.md)

Identity providers

Monitoring

[Usage and Cost API](manage-claude-usage-cost-api.md)[Rate Limits API](manage-claude-rate-limits-api.md)[Analytics APIs](manage-claude-analytics-api.md)[Claude Code Analytics API](manage-claude-claude-code-analytics-api.md)[Spend Limits API](manage-claude-spend-limits-api.md)

[OpenTelemetry](manage-claude-opentelemetry.md)

Data & compliance

[Data residency](manage-claude-data-residency.md)[API and data retention](manage-claude-api-and-data-retention.md)

[Access Transparency](manage-claude-access-transparency.md)

[Encryption keys (CMEK)](manage-claude-cmek.md)

[Overview](manage-claude-cmek.md)[Google Cloud KMS](manage-claude-cmek-google-cloud-kms.md)[Azure Key Vault](manage-claude-cmek-azure-key-vault.md)

[AWS KMS](manage-claude-cmek-aws-kms.md)

[Inference hooks](manage-claude-inference-hooks.md)

Compliance API

[Overview](manage-claude-compliance-api.md)[Set up the Compliance API](manage-claude-compliance-api-access.md)[Activity Feed](manage-claude-compliance-activity-feed.md)[Chats, files, and projects](manage-claude-compliance-content-data.md)[Session transcripts](manage-claude-compliance-sessions.md)[Organizations, users, roles, groups, and settings](manage-claude-compliance-org-data.md)[Design your integration](manage-claude-compliance-integration-patterns.md)[Errors](manage-claude-compliance-errors.md)[FAQ](manage-claude-compliance-faq.md)

[Console](playground.md)

[Admin](manage-claude-admin-api.md)Encryption keys (CMEK)

# Configure Google Cloud KMS for CMEK

Copy page



Use Google Cloud KMS to provide an encryption key for your organization.

Copy page



Claude Code

Let Claude Code set up this feature for you

Run in

`❯``/claude-api`` help me configure a customer-managed encryption key with Google Cloud KMS`



This guide shows how to use a Google Cloud KMS key as a [customer-managed encryption key (CMEK)](manage-claude-cmek.md) for your Anthropic organization.



Enabling CMEK is permanent. If your KMS key is deleted or disabled, Anthropic cannot recover the data encrypted under it. Review the [warnings and limitations](manage-claude-cmek.md) before you begin.

## Prerequisites

- A Google Cloud project with billing enabled.
- The Cloud KMS API enabled (`cloudkms.googleapis.com`).
- Permissions to create KMS key rings and keys, and to set IAM policy on them (`roles/cloudkms.admin` or equivalent).
- Cloud KMS Data Access audit logs (Data Read and Data Write) turned on for the project, so that Cloud Logging records Anthropic's use of your key. They're off by default. To turn them on, see Google's [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access).
- To create the key from the command line, the [`gcloud` CLI](https://cloud.google.com/cli) installed and authenticated.
- To register the key through the API, an Anthropic Admin API key for your organization.

## Anthropic service account email

In this guide, you give the following Anthropic service account access to your key:

``` block
anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com
```





Use only this published service account email. Never trust an identifier provided over email, chat, or any onboarding channel.



**Domain restricted sharing:** If your Google Cloud organization enforces `constraints/iam.allowedPolicyMemberDomains`, it rejects the IAM bindings for this service account. Add a project-level exception to that constraint, or add Anthropic's Cloud Identity customer ID (format `C0xxxxxxxx`) to the allowed list. Contact Anthropic for the customer ID.

## Encryption key setup

The key must meet these requirements:

- **Location:** Use a single-region US location, such as `us-east5`. Multi-region locations such as `us` and `global` aren't supported. See [Availability and regions](manage-claude-cmek.md#availability-and-regions).
- **Type:** Use a symmetric key with the `ENCRYPT_DECRYPT` purpose. Anthropic strongly recommends HSM protection.
- **Organization label:** Add the label `anthropic-org-<ORGANIZATION_UUID>` with the value `true`. Replace `<ORGANIZATION_UUID>` with your Anthropic organization ID in lowercase. Validation fails without this label. To label an existing key, see [Keys you already have](#existing-key-label).
- **Access:** Give Anthropic's service account the `roles/cloudkms.cryptoKeyEncrypterDecrypter` and `roles/cloudkms.viewer` roles on the key itself.



**Finding your organization ID:** Use the bare UUID, not the `org_`-prefixed ID. Copy it from one of these places:

- **Claude Console:** the **Organization ID** field on the [Organization](playground.md) page (`platform.claude.com/settings/organization`)
- **claude.ai:** the **Organization ID** field under **Organization settings \> Organization**
- **Admin API:** the `id` field from the [Organization Info](../Endpoints/organization-retrieve.md) endpoint

Google Cloud Console

gcloud CLI

Google Cloud Console

1.  1

    ### Create or choose a key ring

    In the Google Cloud console, go to the [Key management](https://console.cloud.google.com/security/kms) page. Open a key ring in a single-region US location, such as `us-east5`, or create one.

2.  2

    ### Configure the key

    Click **Create key** and enter a name. Select these options:

    - **Protection level:** HSM
    - **Key material:** Generated key
    - **Purpose:** Symmetric encrypt/decrypt
    - **Algorithm:** Google symmetric key

3.  3

    ### Add the organization label

    Click **Additional settings**, then **Add label**. Enter the organization label:

    - **Key 1:** `anthropic-org-<ORGANIZATION_UUID>`
    - **Value 1:** `true`

    Click **Create**.

4.  4

    ### Open the key's permissions

    On the key ring details page, select the checkbox next to the key. Open the **Permissions** panel and click **Grant access**.

5.  5

    ### Grant Anthropic's service account access to the key

    Check that **Resource** shows the key, not the key ring or project. Enter these values:

    - **New principals:** `anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com`
    - **Role:** Cloud KMS CryptoKey Encrypter/Decrypter

    Click **Add another role** and select **Cloud KMS Viewer**. Click **Save**.

6.  6

    ### Copy the full key resource name

    On the key ring details page, open the key's **Actions** menu and click **Copy resource name**.

gcloud CLI

In each command, replace these placeholders:

- **`<your-project-id>`:** your Google Cloud project ID
- **`<region>`:** the key's location, such as `us-east5`
- **`<your-keyring-name>`:** the key ring's name
- **`<your-key-name>`:** the key's name
- **`<ORGANIZATION_UUID>`:** your Anthropic organization ID in lowercase

1.  1

    ### Create or choose a key ring

    Skip this step if you already have a key ring to reuse.

    ``` shiki
    gcloud kms keyrings create <your-keyring-name> \
      --project=<your-project-id> \
      --location=<region>
    ```

    

2.  2

    ### Create the key

    ``` shiki
    gcloud kms keys create <your-key-name> \
      --project=<your-project-id> \
      --location=<region> \
      --keyring=<your-keyring-name> \
      --purpose=encryption \
      --protection-level=hsm \
      --labels=anthropic-org-<ORGANIZATION_UUID>=true
    ```

    

    For software protection, omit `--protection-level=hsm`.

3.  3

    ### Grant Anthropic's service account access to the key

    Run both commands:

    ``` shiki
    gcloud kms keys add-iam-policy-binding <your-key-name> \
      --project=<your-project-id> \
      --location=<region> \
      --keyring=<your-keyring-name> \
      --member="serviceAccount:anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com" \
      --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
    ```

    

    ``` shiki
    gcloud kms keys add-iam-policy-binding <your-key-name> \
      --project=<your-project-id> \
      --location=<region> \
      --keyring=<your-keyring-name> \
      --member="serviceAccount:anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com" \
      --role=roles/cloudkms.viewer
    ```

    

4.  4

    ### Get the full key resource name

    ``` shiki
    gcloud kms keys describe <your-key-name> \
      --project=<your-project-id> \
      --location=<region> \
      --keyring=<your-keyring-name> \
      --format="value(name)"
    ```

    

You register the key with its full resource name, in this format:

``` block
projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>
```





**Keys you already have:** Add the organization label with this command, in Cloud Shell or with the gcloud CLI:

```python
gcloud kms keys update <your-key-name> \
  --project=<your-project-id> \
  --location=<region> \
  --keyring=<your-keyring-name> \
  --update-labels=anthropic-org-<ORGANIZATION_UUID>=true
```



The placeholders match the parts of the key's full resource name. The command merges the label with any labels the key already has. Then grant access and copy the resource name as the preceding steps describe.

To share one key among several Anthropic organizations, add one organization label for each.

## Register the key with Anthropic

Claude Platform

Claude Enterprise

Claude Platform

Claude Console

API

Claude Console

1.  1

    ### Open the encryption key settings

    In the Claude Console, go to the [Data retention](playground.md#encryption-keys) page (`platform.claude.com/settings/privacy`). If you don't see **Encryption keys**, select **Organization** from the dropdown menu at the top of the page.

2.  2

    ### Add the key

    Under **Encryption keys**, click **Add key**. Enter a **Display name** and select **Google Cloud KMS**. Click **Continue**.

3.  3

    ### Enter the key resource name

    The dialog box shows an **Organization label**. Check that your key has this label. Paste the full key resource name into **Key resource name** and click **Add**.

4.  4

    ### Validate the key

    In the **Encryption keys** list, click **Verify** next to the key. **Connected** appears when the check passes. If it fails, see [Troubleshoot validation](#troubleshoot-validation) for common causes.

5.  5

    ### Attach the key to a workspace

    Attaching a key can't be undone. If you can, attach it to a new workspace before that workspace receives any requests. In a workspace that already receives requests, the key can take [up to a day to take effect](manage-claude-cmek.md#how-it-works).

    On the Data retention page, select the workspace from the dropdown menu at the top of the page. Under **Encryption key**, select the key and click **Save**.

6.  6

    ### Confirm the change

    Select the checkbox to confirm that you have read the CMEK documentation, then click **Confirm**.

API

1.  1

    ### Create the external key

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

    The `id` field of the response contains the external key ID. Copy it for the next two steps:

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

    If validation fails, see [Troubleshoot validation](#troubleshoot-validation).

3.  3

    ### Attach the key to a workspace

    Attaching a key can't be undone. If you can, attach it to a new workspace before that workspace receives any requests. In a workspace that already receives requests, the key can take [up to a day to take effect](manage-claude-cmek.md#how-it-works).

    Replace `<workspace-id>` with the workspace ID and `ekey_<id>` with the external key ID.

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

Claude Enterprise

On Claude Enterprise, CMEK applies to the whole organization, and an organization can have only one key.

1.  1

    ### Open the encryption key settings

    Go to [claude.ai \> Organization settings \> Data and privacy](https://claude.ai/admin-settings/data-privacy-controls) and find **Encryption keys**.

2.  2

    ### Add the key

    Click **Add key**. Enter a **Display name** and select **Google Cloud KMS**. Select the checkbox to confirm that you have read the CMEK documentation, then click **Continue**.

3.  3

    ### Enter the key resource name

    The dialog box shows an **Organization label**. Check that your key has this label. Paste the full key resource name into **Key resource name** and click **Add**.

4.  4

    ### Confirm that validation passed

    When the check passes, **Encryption key configured** appears, and your organization is CMEK-protected from then on. If the check fails, see [Troubleshoot validation](#troubleshoot-validation).

## Troubleshoot validation

If validation fails, common causes are:

- **Wrong organization label:** Make sure the key has the [organization label](#organization-label), with your bare organization ID in lowercase.
- **VPC Service Controls:** A service perimeter that protects Cloud KMS in your project can block Anthropic. Add Anthropic to an access level on the perimeter, or exclude the key's project from it.
- **Domain restricted sharing:** The `constraints/iam.allowedPolicyMemberDomains` org policy blocks the binding for Anthropic's service account. To check that the binding is there, run `gcloud kms keys get-iam-policy <your-key-name> --project=<your-project-id> --location=<region> --keyring=<your-keyring-name>`. To allow it, see [Anthropic service account email](#anthropic-service-account-email).
- **Disabled or destroyed key version:** Confirm that the key's primary version is enabled.

## Terraform

To create the key with Terraform, use the `google_kms_key_ring`, `google_kms_crypto_key`, and `google_kms_crypto_key_iam_member` resources from the `google` provider.
