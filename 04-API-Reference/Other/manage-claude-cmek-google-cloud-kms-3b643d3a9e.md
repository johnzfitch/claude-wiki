---
title: "Configure Google Cloud KMS for CMEK - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/manage-claude/cmek-google-cloud-kms"
category: "04-API-Reference/Other"
fetched_at: "2026-09-26T06:39:34Z"
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


[Console](/)[Log in](/login?returnTo=%2Fdocs%2Fen%2Fmanage-claude%2Fcmek-google-cloud-kms)

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

# Configure Google Cloud KMS for CMEK

Copy page



Use Google Cloud KMS to provide an encryption key for your organization.

Copy page



Configure with the /claude-api skill in Claude Code



```python
claude "/claude-api help me configure a customer-managed encryption key with Google Cloud KMS"
```

This guide walks through configuring a Google Cloud KMS key as a [customer-managed encryption key (CMEK)](/docs/en/manage-claude/cmek) for your Anthropic organization.



Enabling CMEK is permanent. If your KMS key is deleted or disabled, Anthropic cannot recover the data encrypted under it. Review the [warnings and limitations](/docs/en/manage-claude/cmek) before you begin.

## Prerequisites

- A Google Cloud project with billing enabled.
- The Cloud KMS API enabled (`cloudkms.googleapis.com`).
- Permissions to create KMS key rings and keys, and to set IAM policy on them (`roles/cloudkms.admin` or equivalent).
- An Anthropic Admin API key for your organization.
- The [`gcloud` CLI](https://cloud.google.com/cli) installed and authenticated.
- Cloud KMS **Data Access audit logs** enabled for the project (IAM & Admin \> Audit Logs \> Cloud Key Management Service, with `DATA_READ` and `DATA_WRITE`). These are off by default; without them, Anthropic's encrypt and decrypt operations produce no entries in Cloud Logging.

## Anthropic service account email

To have Anthropic use your encryption key, you must give Anthropic's service account a key it can use for encrypting data. The service account email for Anthropic CMEK is:

``` block
anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com
```





Use only this published service account email. Never trust an identifier provided over email, chat, or any onboarding channel.



**Domain restricted sharing:** If your project is under a Google Cloud organization that enforces `constraints/iam.allowedPolicyMemberDomains`, the following IAM bindings are rejected because the Anthropic service account is outside your organization. You need either a project-level carve-out on that constraint, or to add Anthropic's Cloud Identity customer ID (format `C0xxxxxxxx`) to the allowed list. Contact Anthropic for the customer ID if needed.

## Encryption key setup

1.  1

    ### Create or choose a key ring

    Skip this step if you already have a key ring to reuse. Key rings are regional. Choose a single-region US location such as `us-east5` that matches the Anthropic geography you are configuring. Multi-region locations like `us` and `global` are not supported.

    ``` shiki
    gcloud kms keyrings create <your-keyring-name> \
      --project=<your-project-id> \
      --location=<region>
    ```

    

2.  2

    ### Create the crypto key

    Create a symmetric key with the `ENCRYPT_DECRYPT` purpose. Anthropic strongly recommends HSM protection: Cloud KMS HSM keys are FIPS 140-2 Level 3 validated, and the cost delta over software keys is small.

    The `--labels` option adds the organization label, `anthropic-org-<ORGANIZATION_UUID>` with the value `true`, where `<ORGANIZATION_UUID>` is your Anthropic organization ID in lowercase. The label is required for Anthropic to validate the key.

    
    **Finding your organization ID:** Copy the **Organization ID** field under **Settings \> Organization** in the Claude Console, or under **Organization settings \> Organization** in claude.ai, or read the `id` field from the [Organization Info](/docs/en/api/beta/organization/retrieve) endpoint. Use the bare UUID, not the `org_`-prefixed ID.

    ``` shiki
    gcloud kms keys create <KEY_NAME> \
      --project=<PROJECT_ID> \
      --location=<REGION> \
      --keyring=<KEYRING_NAME> \
      --purpose=encryption \
      --protection-level=hsm \
      --labels=anthropic-org-<ORGANIZATION_UUID>=true
    ```

    

    For software protection instead, omit `--protection-level=hsm`. Nothing else in this guide changes.

    You can also create the key from the Google Cloud Console. Open the key ring, click **Create key**, select **Generated key**, set the purpose and algorithm to symmetric encrypt and decrypt, and choose **HSM** under protection level.

    To share one key among several Anthropic organizations, add one such label for each organization. A key can carry at most 64 labels, including your own.

    
    To add the label to a key that doesn't have it, run `gcloud kms keys update <KEY_NAME> --project=<PROJECT_ID> --location=<REGION> --keyring=<KEYRING_NAME> --update-labels=anthropic-org-<ORGANIZATION_UUID>=true`. It merges the label with any labels the key already has.

3.  3

    ### Grant Anthropic's service account access to the key

    Two key-level IAM bindings are required. Both are scoped to the single crypto key, not project-wide or keyring-wide.

    Encrypt and decrypt, which Anthropic uses to encrypt and decrypt the data keys that protect your workspace data (envelope encryption):

    ``` shiki
    gcloud kms keys add-iam-policy-binding <your-key-name> \
      --project=<your-project-id> \
      --location=<region> \
      --keyring=<your-keyring-name> \
      --member="serviceAccount:anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com" \
      --role=roles/cloudkms.cryptoKeyEncrypterDecrypter
    ```

    

    Viewer, for the metadata read (`cryptoKeys.get`) Anthropic performs at startup to validate the key's purpose and algorithm:

    ``` shiki
    gcloud kms keys add-iam-policy-binding <your-key-name> \
      --project=<your-project-id> \
      --location=<region> \
      --keyring=<your-keyring-name> \
      --member="serviceAccount:anthropic-cmek-client-us@gcp-anthropic-cmek-clients.iam.gserviceaccount.com" \
      --role=roles/cloudkms.viewer
    ```

    

    From the Console, select the key, open the **Permissions** panel, click **Grant access**, and add the service account with both the Cloud KMS CryptoKey Encrypter/Decrypter and Cloud KMS Viewer roles. Make sure you are on the key's permissions page, not the key ring or project, so the grant is scoped to this key only.

4.  4

    ### Note the full key resource name

    You pass this to Anthropic when you register the key. The format is:

    ``` block
    projects/<your-project-id>/locations/<region>/keyRings/<your-keyring-name>/cryptoKeys/<your-key-name>
    ```

    

    Retrieve it with:

    ``` shiki
    gcloud kms keys describe <your-key-name> \
      --project=<your-project-id> \
      --location=<region> \
      --keyring=<your-keyring-name> \
      --format="value(name)"
    ```

    

    From the Console, open the key's details page and click **Copy resource name**.

## Register the key with Anthropic

How you register the key depends on which product you use.

Claude Platform

Claude Enterprise

You can set up the key in the Claude Console or through the Admin API, with the same result.

Claude Console

API

1.  1

    ### Register the key with Anthropic

    In the Claude Console, open **Settings \> Encryption keys** and click **Add key**. Enter a display name, choose **Google Cloud KMS**, and click **Continue**. Paste the full key resource name into **Key resource name**, and click **Add**.

    The key details step shows the organization label. Add it to the key, as [the create step](#organization-label) describes, before you click **Add**.

2.  2

    ### Validate the key

    On the **Encryption keys** page, click **Verify** next to the key. **Connected** appears when the check passes. If it fails, a message gives the reason.

3.  3

    ### Attach the key to a workspace

    In the Claude Console, go to [Manage \> Security](/settings/workspaces/default/security-compliance) and select the workspace in the workspace picker at the top of the sidebar. Under **Encryption key**, select the key, click **Save**, and confirm. Attaching a key can't be undone. For a workspace that already receives requests, the key can take [up to a day to take effect](/docs/en/manage-claude/cmek#how-it-works).

## Terraform

For infrastructure-as-code deployments, the same steps map to the `google` provider with the `google_kms_key_ring`, `google_kms_crypto_key`, and `google_kms_crypto_key_iam_member` resources.
