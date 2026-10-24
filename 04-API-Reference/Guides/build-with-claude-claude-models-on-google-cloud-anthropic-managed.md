---
title: "Claude Models on Google Cloud (Anthropic managed) - Claude Platform Docs"
source_url: "https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed"
category: "04-API-Reference/Guides"
fetched_at: "2026-10-23T06:28:50Z"
tags: ["api", "authentication", "billing"]
---

- [Managed Agents](../Other/managed-agents-overview.md)

- [Admin](../Other/manage-claude-admin-api.md)

- Resources
  - [Best practices](../About/about-claude-use-case-guides-overview.md)
  - [Models & pricing](../../20-Models/about-claude-models-overview.md)
  - [SDKs, CLI, and libraries](../Other/cli-sdks-libraries-overview.md)
  - [Claude API skill](../Agents-Tools/agents-and-tools-agent-skills-claude-api-skill.md)
  - [Release notes](../../20-Models/release-notes-overview.md)

[API reference](../Endpoints/overview.md)




[Console](../Other/playground.md)[Log in](https://platform.claude.com/login?returnTo=%2Fdocs%2Fen%2Fbuild-with-claude%2Fclaude-models-on-google-cloud%2Fanthropic-managed)





SearchCtrlK

First steps

[Intro to Claude](../../01-Getting-Started/intro.md)[Get your API key](../Other/get-api-key.md)[Quickstart](../../01-Getting-Started/get-started.md)[Authentication](../Other/manage-claude-authentication.md)

Building with Claude

[Features overview](build-with-claude-overview.md)[Using the Messages API](build-with-claude-working-with-messages.md)[Stop reasons and fallback](build-with-claude-handling-stop-reasons.md)[Refusals and fallback](build-with-claude-refusals-and-fallback.md)[Fallback credit](build-with-claude-fallback-credit.md)

Model capabilities

[Effort](build-with-claude-effort.md)[Task budgets (beta)](build-with-claude-task-budgets.md)[Fast mode](build-with-claude-fast-mode.md)[Structured outputs](build-with-claude-structured-outputs.md)[Citations](build-with-claude-citations.md)[Streaming Messages](build-with-claude-streaming.md)[Batch processing](build-with-claude-batch-processing.md)[Search results](build-with-claude-search-results.md)[Streaming refusals](../Test-Evaluate/test-and-evaluate-strengthen-guardrails-handle-streaming-refusals.md)[Multilingual support](build-with-claude-multilingual-support.md)[Embeddings](build-with-claude-embeddings.md)

[Thinking](build-with-claude-thinking.md)

Tools

[Overview](../Agents-Tools/agents-and-tools-tool-use-overview.md)[How tool use works](../Agents-Tools/agents-and-tools-tool-use-how-tool-use-works.md)[Tutorial: Build a tool-using agent](../Agents-Tools/agents-and-tools-tool-use-build-a-tool-using-agent.md)[Define tools](../Agents-Tools/agents-and-tools-tool-use-implement-tool-use.md)[Handle tool calls](../Agents-Tools/agents-and-tools-tool-use-handle-tool-calls.md)[Parallel tool use](../Agents-Tools/agents-and-tools-tool-use-parallel-tool-use.md)[Tool runner (SDK)](../Agents-Tools/agents-and-tools-tool-use-tool-runner.md)[Strict tool use](../Agents-Tools/agents-and-tools-tool-use-strict-tool-use.md)[Server tools](../Agents-Tools/agents-and-tools-tool-use-server-tools.md)[Web search tool](../Agents-Tools/agents-and-tools-tool-use-web-search-tool.md)[Web fetch tool](../Agents-Tools/agents-and-tools-tool-use-web-fetch-tool.md)[Code execution tool](../Agents-Tools/agents-and-tools-tool-use-code-execution-tool.md)[Advisor tool](../Agents-Tools/agents-and-tools-tool-use-advisor-tool.md)[Tool search tool](../Agents-Tools/agents-and-tools-tool-use-tool-search-tool.md)[Memory tool](../Agents-Tools/agents-and-tools-tool-use-memory-tool.md)[Bash tool](../Agents-Tools/agents-and-tools-tool-use-bash-tool.md)[Text editor tool](../Agents-Tools/agents-and-tools-tool-use-text-editor-tool.md)[Browser and computer use (SDK)](../Agents-Tools/agents-and-tools-tool-use-browser-use-sdk.md)[Computer use tool](../Agents-Tools/agents-and-tools-tool-use-computer-use-tool.md)[Browser use tool](../Agents-Tools/agents-and-tools-tool-use-browser-use-tool.md)[Troubleshooting](../Agents-Tools/agents-and-tools-tool-use-troubleshooting-tool-use.md)

Tool infrastructure

[Tool reference](../Agents-Tools/agents-and-tools-tool-use-tool-reference.md)[Manage tool context](../Agents-Tools/agents-and-tools-tool-use-manage-tool-context.md)[Tool combinations](../Agents-Tools/agents-and-tools-tool-use-tool-combinations.md)[Tool use with prompt caching](../Agents-Tools/agents-and-tools-tool-use-tool-use-with-prompt-caching.md)[Programmatic tool calling](../Agents-Tools/agents-and-tools-tool-use-programmatic-tool-calling.md)[Fine-grained tool streaming](../Agents-Tools/agents-and-tools-tool-use-fine-grained-tool-streaming.md)

Context management

[Context windows](build-with-claude-context-windows.md)[Context editing](build-with-claude-context-editing.md)[Prompt caching](build-with-claude-prompt-caching.md)[Mid-conversation system messages and tool changes](build-with-claude-mid-conversation-system-messages.md)[Build an orchestration mode](build-with-claude-mid-conversation-effort-example.md)[Cache diagnostics](build-with-claude-cache-diagnostics.md)[Token counting](build-with-claude-token-counting.md)

[Compaction](build-with-claude-compaction.md)

Working with files

[Files API](build-with-claude-files.md)[PDF support](build-with-claude-pdf-support.md)

[Images and vision](build-with-claude-vision.md)

Skills

[Overview](../Agents-Tools/agents-and-tools-agent-skills-overview.md)[Quickstart](../Agents-Tools/agents-and-tools-agent-skills-quickstart.md)[Best practices](../Agents-Tools/agents-and-tools-agent-skills-best-practices.md)[Skills for enterprise](../Agents-Tools/agents-and-tools-agent-skills-enterprise.md)[Skills in the API](build-with-claude-skills-guide.md)

MCP

[Remote MCP servers](../Agents-Tools/agents-and-tools-remote-mcp-servers.md)[MCP connector](../Agents-Tools/agents-and-tools-mcp-connector.md)

[MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md)

Claude on cloud platforms

[Amazon Bedrock (Opus 4.7 and later)](build-with-claude-claude-in-amazon-bedrock.md)[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude-claude-on-amazon-bedrock-legacy.md)[Claude Platform on AWS](build-with-claude-claude-platform-on-aws.md)[Microsoft Foundry](build-with-claude-claude-in-microsoft-foundry.md)

[Google Cloud](build-with-claude-claude-models-on-google-cloud-overview.md)

[Overview](build-with-claude-claude-models-on-google-cloud-overview.md)[Anthropic-managed](build-with-claude-claude-models-on-google-cloud-anthropic-managed.md)[Google-managed](build-with-claude-claude-models-on-google-cloud-google-managed.md)

[Console](../Other/playground.md)

[Messages](../../01-Getting-Started/intro.md)Google Cloud

# Claude Models on Google Cloud (Anthropic managed)

Copy page



Claude Models on Google Cloud (Anthropic managed) is the Claude API, run by Anthropic and reached through your Google Cloud project.

Copy page



Google Cloud handles access and billing for Claude Models on Google Cloud (Anthropic managed). To compare the two Google Cloud offerings, or to check which one you use, see [Claude Models on Google Cloud](build-with-claude-claude-models-on-google-cloud-overview.md).

## Set up your account

To set up your account for Claude Models on Google Cloud (Anthropic managed), you need the following:

- Permission to purchase in Google Cloud Marketplace on your billing account
- Permission to enable services on the project
- An [IAM role that lets you open the Claude Console](#using-the-claude-console), which you need for step 4

These steps create a new Anthropic organization for your Google Cloud project. It's separate from any Anthropic organization your company already has. That includes a Claude Enterprise organization. To move from an existing organization, see [Moving from an existing Anthropic organization](#moving-from-an-existing-anthropic-organization).

If you have an existing discount, contact your Anthropic or Google Cloud account representative before you start these steps. Discounts can't be applied to past usage.

1.  1

    ### Subscribe in Marketplace

    1.  Open [Google Cloud Marketplace](https://console.cloud.google.com/marketplace) and find the **Claude Models on Google Cloud (Anthropic managed)** listing.
    2.  Click **Subscribe** and complete the purchase flow.
    3.  Return to the listing and click **Manage on Console**. This opens the Claude page in the Google Cloud console.

    To return to the Claude page later, select your project in the Google Cloud console. Then go to **Agent Platform \> Models \> Claude Platform** and select **Anthropic managed**.

2.  2

    ### Enable the services

    Enable two services on every project that calls Claude Models on Google Cloud (Anthropic managed):

    - `claude.googleapis.com` serves the API for Claude Models on Google Cloud (Anthropic managed). This service also defines the IAM permissions. Calls fail without it.
    - `anthropic-managed-claude.cloudpartnerservices.goog` is the Marketplace service that attributes the project's usage to your subscription.

    CLI

    

    ``` shiki
    gcloud services enable claude.googleapis.com \
      anthropic-managed-claude.cloudpartnerservices.goog \
      --project=my-project-id
    ```

    Replace `my-project-id` with your project ID.

    You can also enable both from the Claude page or from **APIs & Services**. Enabling is a one-time step for each project. To check that both services are enabled, run `gcloud services list --enabled --project=my-project-id` and look for both names.

3.  3

    ### Set up your Anthropic organization

    1.  On the Claude page, click **Activate**.
    2.  In the Anthropic setup flow, enter a contact email address.
    3.  Open the setup link sent to that address.
    4.  Fill in the organization's name, entity type, country, and intended use.
    5.  Accept Anthropic's Commercial Terms of Service and Usage Policy.

    The contact address is used only for setup and service notices. For how people open the Claude Console after setup, see [Using the Claude Console](#using-the-claude-console).

4.  4

    ### Open the Claude Console

    When your Anthropic organization is active, the button on the Claude page changes to **Open Claude Console**. Click it. Google Cloud checks your IAM access. Then it redirects your browser to `platform.claude.com`. You're signed in to the new organization.

    While you're in the Claude Console, [find your workspace ID](#find-your-workspace-id) and copy it. Everyone who calls Claude Models on Google Cloud (Anthropic managed) needs it. Pass it on to your developers.

To add another project, repeat these steps in that project, starting from step 2.

### Troubleshooting account setup

If you run into one of the following problems while you set up Claude Models on Google Cloud (Anthropic managed), apply its fix:

- **`gcloud services enable` can't find `anthropic-managed-claude.cloudpartnerservices.goog`:** Run the command as the account that completed the Marketplace purchase, or contact your Anthropic account representative.
- **A permission error on your first API call:** Check that `claude.googleapis.com` is enabled on the project you're calling. Check that the caller has `roles/claude.user` or `roles/claude.admin` on that project. For what each role allows, see [IAM roles](#iam-roles). A new grant or a newly enabled service can take a moment to apply.
- **"Signed in as a different account" after following the setup link:** Click **Log out and continue**. Then use the email address you entered in step 3.
- **The button says "Finish Setup" instead of "Open Claude Console":** Your Anthropic organization exists, but its setup isn't complete. An administrator has to finish the organization details form.
- **The Usage page shows no data after your first API call:** Usage data can take a few minutes to appear in the Claude Console.

## Manage access

### IAM roles

Claude Models on Google Cloud (Anthropic managed) has three predefined IAM roles. Grant roles on the project.

[TABLE]

For example, the following command lets a service account call Claude Models on Google Cloud (Anthropic managed):

CLI



```python
gcloud projects add-iam-policy-binding my-project-id \
  --member="serviceAccount:my-app@my-project-id.iam.gserviceaccount.com" \
  --role="roles/claude.user"
```

For permissions, predefined roles, and audit log types, see [IAM permissions for Claude Models on Google Cloud (Anthropic managed)](../Endpoints/claude-models-on-google-cloud-anthropic-managed-iam-permissions.md).

Enabling `claude.googleapis.com` creates a service agent for the project. Don't remove its role grants. Removing them stops Claude Models on Google Cloud (Anthropic managed) from working in the project.

### Using the Claude Console

With Claude Models on Google Cloud (Anthropic managed), you can't use an email address to sign in to your Anthropic organization. Instead, click **Open Claude Console** on the [Claude page](#set-up-your-account) in the Google Cloud console. Google Cloud IAM controls who can open the Claude Console. Of the three predefined [IAM roles](#iam-roles), only `roles/claude.admin` on the project lets you open the Claude Console.

### Workspaces

In Claude Models on Google Cloud (Anthropic managed), setup creates your Anthropic organization with one workspace, the Default Workspace. To create more workspaces, [open the Claude Console](#using-the-claude-console) and go to **Settings \> Workspaces**. On the same page, you can rename or archive any workspace except the Default Workspace. Each workspace has its own [workspace ID](#find-your-workspace-id). Files, skills, batches, Claude Managed Agents sessions, and other workspace resources belong to the workspace whose ID you [set for the request](#project-location-and-workspace-resolution).

You grant [IAM roles](#iam-roles) on the project, so a role applies to every workspace in that project. When teams need separate access, give each team its own Google Cloud project. Each project has its own Anthropic organization, so repeat the [setup steps](#set-up-your-account) in each project, starting from step 2.

## Before making API calls

To call Claude Models on Google Cloud (Anthropic managed), you need the following:

1.  A Google Cloud project with an active subscription and an Anthropic organization whose setup is complete. See [Set up your account](#set-up-your-account).
2.  The [gcloud CLI](https://cloud.google.com/sdk/docs/install) installed, for local development.
3.  The `roles/claude.user` role, granted on the project to the identity that makes the calls.
4.  Application Default Credentials for that identity. See [Authentication](#authentication).
5.  Your project ID and your [workspace ID](#find-your-workspace-id).

To grant the role to your own account for local development, run the following command. You need permission to change the project's IAM policy.

CLI



```python
gcloud projects add-iam-policy-binding my-project-id \
  --member="user:you@example.com" \
  --role="roles/claude.user"
```

Replace `my-project-id` with your project ID. Replace `you@example.com` with your Google account's email address. To see the project gcloud is using, run `gcloud config get-value project`. For service accounts and the other roles, see [IAM roles](#iam-roles).

### Find your workspace ID

To find your workspace ID for Claude Models on Google Cloud (Anthropic managed), [open the Claude Console](#using-the-claude-console) and go to **Settings \> Workspaces**. The ID starts with `wrkspc_`. If you can't open the Claude Console, ask someone who can open it to send you the ID.

Set the project and workspace as environment variables so that the SDK client and the [`ant` CLI](../Other/cli-sdks-libraries-cli-quickstart.md) pick them up:

CLI



```python
export ANTHROPIC_GOOGLE_CLOUD_PROJECT="my-project-id"
export ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID="wrkspc_01AbCdEf23GhIj"
```

### Install an SDK

The [SDK client](../Other/cli-sdks-libraries-overview.md) for Claude Models on Google Cloud (Anthropic managed) is `AnthropicGoogleCloud`. The client resolves your Google credentials. It also builds the base URL from your project, location, and workspace ID.



The SDK client for Claude Models on Google Cloud (Anthropic managed) is in beta.

Install the package that provides the client:

Python

TypeScript

C#

Go

Java

PHP

Ruby

Python

```python
pip install -U "anthropic[google_cloud]"
```



To use the `ant` CLI instead, [install or update the CLI](../Other/cli-sdks-libraries-cli-quickstart.md#installation) to the latest version. A version without support for Claude Models on Google Cloud (Anthropic managed) ignores the `ANTHROPIC_GOOGLE_CLOUD_*` variables. It then does one of the following:

- Sends the request to the Claude API with any other credential you've set up
- Fails with an authentication error

## Making requests

Claude Models on Google Cloud (Anthropic managed) serves Claude API endpoints under a base URL that names your project, a location, and your workspace:

``` block
https://claude.googleapis.com/v1/projects/{project}/locations/global/workspaces/{workspace}/invoke
```



The [organization-level routes](#iam-roles), whose paths start with `/v1/organizations/`, use a base URL without the workspace:

``` block
https://claude.googleapis.com/v1/projects/{project}/locations/global/claudeOrganization/invoke
```



If you don't [set the base URL](#project-location-and-workspace-resolution), the SDK client chooses between these two for each request.

Append the Claude API path to the base URL. For example, the [Messages API](../Endpoints/messages-create.md) is at `.../invoke/v1/messages`. Three things differ from a Claude API request:

- **Base URL:** The project-scoped URLs shown earlier, in place of `https://api.anthropic.com`.
- **Authentication:** An `Authorization: Bearer` header with a Google access token. Don't send an `x-api-key` header.
- **Workspace:** The workspace ID is part of the URL. Don't send an `anthropic-workspace-id` header.

Everything else is the same as on the Claude API, including the following:

- The `anthropic-version` and `anthropic-beta` headers
- The request body
- Streaming
- The response

Code samples elsewhere in this documentation create the Claude API client and read an API key. To run one with Claude Models on Google Cloud (Anthropic managed), replace its import and client constructor with the ones in the following examples. For a cURL sample, apply the three differences listed earlier.

Before running these examples, complete the steps in [Before making API calls](#before-making-api-calls).

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

```python
from anthropic import AnthropicGoogleCloud

client = AnthropicGoogleCloud()

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(message)
```

The cURL example asks gcloud for an Application Default Credentials token. Access tokens are short-lived. Generate one for each session instead of storing it.

### API model IDs

Claude Models on Google Cloud (Anthropic managed) uses the same model IDs as the Claude API, for example `claude-opus-5-5`. For the models and their IDs, see [Models overview](../../20-Models/about-claude-models-overview.md).

In Claude Models on Google Cloud (Anthropic managed), a request for a model that isn't available to your Anthropic organization returns an error. The error message reads `Model {model} is not available for this organization's inference configuration.`

## Project, location, and workspace resolution

The client for Claude Models on Google Cloud (Anthropic managed) takes the settings in the following table. A value you pass when you create the client wins over the environment variable. To set the project and workspace ID explicitly, pass `project` and `workspace_id`.

| Setting      | Environment variable                                          | If unset                                                                                                                   |
|:-------------|:--------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| Project ID   | `ANTHROPIC_GOOGLE_CLOUD_PROJECT`, then `GOOGLE_CLOUD_PROJECT` | The project that Application Default Credentials reports, when the credential type carries one                             |
| Workspace ID | `ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID`                         | The client raises an error unless you set the base URL. [Organization-level routes](#iam-roles) don't need a workspace ID. |
| Location     | `ANTHROPIC_GOOGLE_CLOUD_LOCATION`                             | `global`                                                                                                                   |
| Base URL     | `ANTHROPIC_GOOGLE_CLOUD_BASE_URL`                             | Derived from the project, location, and workspace ID                                                                       |

Leave the location at `global`. The location is separate from where inference runs, so for US-only inference, set `inference_geo: "us"` on each request, as described in [Data residency](../Other/manage-claude-data-residency.md#inference-geo).

The `ant` CLI takes the same settings as flags:

- **Project ID:** `--google-cloud-project`
- **Workspace ID:** `--google-cloud-workspace-id`
- **Location:** `--google-cloud-location`
- **Base URL:** `--google-cloud-base-url`

The CLI uses Claude Models on Google Cloud (Anthropic managed) when the project, workspace ID, or location is set. Setting `GOOGLE_CLOUD_PROJECT`, the base URL, or both isn't enough.

## Authentication

Each request to Claude Models on Google Cloud (Anthropic managed) carries a Google OAuth 2.0 access token in an `Authorization: Bearer` header. The token has the `https://www.googleapis.com/auth/cloud-platform` scope.

Google Cloud handles access. Its gateway at `claude.googleapis.com` does the following for each request:

1.  Checks your Google Cloud credentials.
2.  Checks that the caller holds the IAM permission that the request needs. If the caller doesn't, Google Cloud returns an HTTP 403 error.
3.  Forwards the request to Anthropic. Anthropic validates the request.

To grant permissions, see [IAM roles](#iam-roles).

The SDK client gets the token from [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) (ADC). Any credential source that ADC supports works:

- **Local development:** Run `gcloud auth application-default login`.
- **On Google Cloud:** The client automatically uses the service account attached to the workload, for example on Compute Engine, GKE, or Cloud Run.
- **A service account key file:** Set `GOOGLE_APPLICATION_CREDENTIALS` to its path.
- **Workload Identity Federation and service account impersonation:** Configure them as you would for any Google Cloud API.

Check that ADC is working:

CLI



```python
gcloud auth application-default print-access-token
```

Claude Models on Google Cloud (Anthropic managed) doesn't use API keys. In the Claude Console, you can't create API keys for the Anthropic organization that setup creates. The SDK client for Claude Models on Google Cloud (Anthropic managed) ignores these environment variables:

- `ANTHROPIC_API_KEY`
- `ANTHROPIC_AUTH_TOKEN`
- `ANTHROPIC_BASE_URL`

### Credential precedence

The SDK client for Claude Models on Google Cloud (Anthropic managed) checks for credentials in the following order. The client uses the first one it finds:

1.  A token provider that you pass as `token_provider` when you create the client. It's a function or token source that returns an access token. The client asks it for a token on every request. Caching and refreshing the token are up to you.
2.  A Google credentials object that you pass as `credentials` when you create the client. The Go SDK doesn't have this option.
3.  Application Default Credentials.

Go and Java differ from the other SDKs:

- **Go:** For option 1, the client takes an `oauth2.TokenSource`. It caches the token until the token expires.
- **Java:** Use `GoogleCloudBackend.fromEnv()` to read Application Default Credentials and the environment variables in [Project, location, and workspace resolution](#project-location-and-workspace-resolution).

The client has no environment variable of its own for the credential. Use ADC's `GOOGLE_APPLICATION_CREDENTIALS` instead.

If your requests go through a proxy that attaches the token for you, set `skip_auth`. The client then sends no `Authorization` header. You can't combine this setting with the preceding credential options.

When the `ant` CLI uses Claude Models on Google Cloud (Anthropic managed), it always gets the token from Application Default Credentials. It takes no token provider, credentials object, or setting to skip authentication.

Before you use `ant` with Claude Models on Google Cloud (Anthropic managed), make sure none of these is set:

- An API key
- An authentication token
- `--profile` or `ANTHROPIC_PROFILE`, if it names a [configuration profile](../Other/manage-claude-wif-reference.md#profile-configuration-file) that the CLI can authenticate with
- Any of Anthropic's federation variables:
  - `ANTHROPIC_FEDERATION_RULE_ID`
  - `ANTHROPIC_ORGANIZATION_ID`
  - `ANTHROPIC_SERVICE_ACCOUNT_ID`
  - `ANTHROPIC_IDENTITY_TOKEN`
  - `ANTHROPIC_IDENTITY_TOKEN_FILE`

If one is set, the CLI uses that credential instead of the Google Cloud settings from [Find your workspace ID](#find-your-workspace-id). If only some of the federation variables are set, the CLI stops with an error. When more than one credential is set, the CLI prints a note naming the one it uses.

Also leave `ANTHROPIC_WORKSPACE_ID` and the `--workspace-id` flag unset. The CLI still sends that value as an `anthropic-workspace-id` header. Requests to Claude Models on Google Cloud (Anthropic managed) must not carry that header. Set the workspace with `--google-cloud-workspace-id` or `ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID` instead.

Like the SDK client, the CLI doesn't send requests for Claude Models on Google Cloud (Anthropic managed) to `--base-url` or `ANTHROPIC_BASE_URL`.

## Feature support

This section lists features that work on Claude Models on Google Cloud (Anthropic managed) and features that aren't supported there. It doesn't list every Claude API feature, and it doesn't say whether an unlisted feature works.

The following features work on Claude Models on Google Cloud (Anthropic managed) as they do on the Claude API:

- **Fast mode:** [Fast mode](build-with-claude-fast-mode.md) for Claude Opus 5.5.


- **Beta features:** If a beta is limited to selected organizations on the Claude API, the Anthropic organization that setup creates needs the same access.
- **Tools:** [Tool use](../Agents-Tools/agents-and-tools-tool-use-overview.md), including:
  - Web search
  - Web fetch
  - Code execution
  - The memory tool
  - The advisor tool
  - The MCP connector
- **Skills and files:** [Agent Skills](../Agents-Tools/agents-and-tools-agent-skills-overview.md) and the [Files API](build-with-claude-files.md).
- **Model capabilities:**
  - [Prompt caching](build-with-claude-prompt-caching.md)
  - [Extended thinking](build-with-claude-thinking.md)
  - [Server-side fallback](build-with-claude-refusals-and-fallback.md#server-side-fallback)
  - [Streaming](build-with-claude-streaming.md)
  - [Structured outputs](build-with-claude-structured-outputs.md)
  - [Token counting](build-with-claude-token-counting.md)
- **Batches and models:** The [Message Batches API](build-with-claude-batch-processing.md) and the Models API.

To turn the [Compliance API](../Other/manage-claude-compliance-api.md) on or off for the Anthropic organization that setup creates, [open the Claude Console](#using-the-claude-console), go to **Settings \> Compliance**, and use the **Compliance API** toggle.

Customer-managed encryption keys (CMEK) are available with Google Cloud KMS keys. To activate CMEK for the Anthropic organization that setup creates, see [Customer-managed encryption keys](../Other/manage-claude-cmek.md). To set up a key, follow [Configure Google Cloud KMS for CMEK](../Other/manage-claude-cmek-google-cloud-kms.md). Then register, verify, and attach the key in the [Claude Console](#using-the-claude-console), as the setup page's **Claude Console** tab describes.

### Claude Managed Agents

[Claude Managed Agents](../Other/managed-agents-overview.md) is available through Claude Models on Google Cloud (Anthropic managed), including the following:

- [Agents](../Other/managed-agents-agent-setup.md)
- [Environments](../Other/managed-agents-environments.md)
- [Sessions](../Other/managed-agents-sessions.md)
- [Credential vaults](../Other/managed-agents-vaults.md)
- [Memory stores](../Other/managed-agents-memory.md)
- [Scheduled deployments](../Other/managed-agents-scheduled-deployments.md)
- [Self-hosted sandboxes](../Other/managed-agents-self-hosted-sandboxes.md)

Access is checked when a session or a deployment is created, not while it runs:

- **Running sessions keep running.** If you revoke Google Cloud access from the identity that created a session, the session doesn't stop. To stop it, send it a [`user.interrupt` event](../Other/managed-agents-events-and-streaming.md#integrating-events) by itself. After the session is `idle`, you can archive or delete it.
- **Scheduled deployments keep running.** A deployment doesn't re-check its creator's access on each scheduled run. To stop it, pause, update, or archive it.

When you remove a user or rotate a service account, review the sessions and deployments that identity created.

### Features not supported

The following aren't supported on Claude Models on Google Cloud (Anthropic managed):

- **API keys:** Authentication is through Google Cloud credentials only.
- **MCP tunnels:** [MCP tunnels](../Agents-Tools/agents-and-tools-mcp-tunnels-overview.md) aren't available on Claude Models on Google Cloud (Anthropic managed).
- **[Memory stores on self-hosted environments](../Other/managed-agents-self-hosted-sandboxes-memory.md):** Memory stores aren't supported for sessions on self-hosted environments.
- **Pre-built self-hosted sandbox workers:** The [self-hosted workers](../Other/managed-agents-self-hosted-sandboxes-workers.md) in the `ant` CLI and in the Python, TypeScript, and Go SDKs don't support Claude Models on Google Cloud (Anthropic managed). Instead, implement your own worker that calls the [Environments Work endpoints](../Endpoints/beta-environments-work.md) directly. For the roles and permissions your worker needs, see [IAM permissions for environments](../Endpoints/claude-models-on-google-cloud-anthropic-managed-iam-permissions.md#environments).

### Context window

Context window sizes on Claude Models on Google Cloud (Anthropic managed) are the same as on the Claude API. For each model's limit, see [Context windows](build-with-claude-context-windows.md).

## Billing, rate limits, and logging

### Rate limits

Anthropic manages rate limits for Claude Models on Google Cloud (Anthropic managed). To request higher limits, contact your Anthropic account representative or [contact sales](https://claude.com/contact-sales). For how rate limits are measured and reported, see [Rate limits](../Endpoints/rate-limits.md).

### Billing

Claude Models on Google Cloud (Anthropic managed) bills through Google Cloud Marketplace. Anthropic meters your usage. It reports the usage to Google Cloud in Claude Consumption Units. One Claude Consumption Unit is \$0.01 USD. The charges appear on your Google Cloud bill. Anthropic doesn't send a separate invoice.

View usage and cost data on the **Usage** and **Cost** pages in the [Claude Console](#using-the-claude-console).

If you have a Google Cloud spend commitment, usage counts toward it the way other Marketplace purchases do.

### Data retention

Anthropic is the data processor for Claude Models on Google Cloud (Anthropic managed). Some supporting services, such as Anthropic's trust and safety systems, process data outside Google Cloud.

Claude Models on Google Cloud (Anthropic managed) follows the same data retention policy as the Claude API. See [API and data retention](../Other/manage-claude-api-and-data-retention.md). Zero Data Retention (ZDR) is available on request. Contact your Anthropic account representative.

A ZDR arrangement on another Anthropic organization doesn't carry over to your organization for Claude Models on Google Cloud (Anthropic managed).

### Monitoring and logging

[Cloud Audit Logs](https://cloud.google.com/logging/docs/audit) records API activity for Claude Models on Google Cloud (Anthropic managed) in your project. The entries appear under the `claude.googleapis.com` service. Each API route belongs to one of two log types:

- **Data Access logs:** These cover most routes, including messages, batches, files, skills, models, and most Claude Managed Agents resources. They're off by default.
- **Admin Activity logs:** These cover the other routes, including the encryption key routes and most credential vault routes. The exception is the route for `vaults.verify`, which is Data Access. Admin Activity logs are always on.

To keep a record of requests, turn on Data Access logs for `claude.googleapis.com` in your project's audit log settings.

For audit log types by route, see [IAM permissions for Claude Models on Google Cloud (Anthropic managed)](../Endpoints/claude-models-on-google-cloud-anthropic-managed-iam-permissions.md).

#### Request IDs

Successful responses from Claude Models on Google Cloud (Anthropic managed) carry the [`request-id`](../Endpoints/errors.md#request-id) header.

## Moving from an existing Anthropic organization

You can't convert an existing Anthropic organization into an organization for Claude Models on Google Cloud (Anthropic managed). That includes an organization you use with the Claude API directly.

Plan the move as a cutover to a new organization:

- **Create the new organization first.** Follow [Set up your account](#set-up-your-account).
- **Recreate access and configuration.** API keys, workspaces, and Claude Console settings don't carry over. Grant [IAM roles](#iam-roles) on the project instead of creating API keys. To recreate your workspaces, see [Workspaces](#workspaces). For ZDR arrangements, see [Data retention](#data-retention).
- **Plan for stored resources.** Files, skills, batches, and Claude Managed Agents resources stay in the existing organization.
- **Update your integration.** For what changes and what stays the same, see [Making requests](#making-requests). For features that aren't supported, see [Features not supported](#features-not-supported).
- **Cut over on your own schedule.** The two organizations are independent and can serve traffic in parallel. You can move workloads gradually. The existing organization keeps its current billing. Before you shift production traffic, check the [rate limits for Claude Models on Google Cloud (Anthropic managed)](#rate-limits).

## Migrating from Claude Models on Google Cloud (Google managed)

To move to Claude Models on Google Cloud (Anthropic managed), complete the following steps. Before you move workloads that rely on a ZDR arrangement, see [Data retention](#data-retention). For what changes when you move, see [How the two Google Cloud offerings differ](build-with-claude-claude-models-on-google-cloud-overview.md#how-the-two-google-cloud-offerings-differ).

1.  1

    ### Set up your account

    Complete every step in [Set up your account](#set-up-your-account).

2.  2

    ### Set up access

    Grant `roles/claude.user` to each identity that calls Claude Models on Google Cloud (Anthropic managed). Set your project and workspace ID as environment variables. For both, see [Before making API calls](#before-making-api-calls).

3.  3

    ### Install the SDK package

    Install the package that provides the client for Claude Models on Google Cloud (Anthropic managed). See [Install an SDK](#install-an-sdk).

4.  4

    ### Replace the import and the client

    Change the code that imports and creates your client. Use `AnthropicGoogleCloud` in place of `AnthropicVertex`. In a cURL request, change the URL, the headers, and the body. Your current code creates a client for Claude Models on Google Cloud (Google managed). For example, the following code creates that client with the global endpoint:

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
    from anthropic import AnthropicVertex

    project_id = "MY_PROJECT_ID"
    region = "global"

    client = AnthropicVertex(project_id=project_id, region=region)
    ```

    The following code creates the client for Claude Models on Google Cloud (Anthropic managed):

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
    from anthropic import AnthropicGoogleCloud

    client = AnthropicGoogleCloud()
    ```

    The new client reads your project and workspace ID from the environment variables you set in [Find your workspace ID](#find-your-workspace-id). You don't pass them when you create the client. Your Messages API calls stay as they are, except for the model IDs and features in the next step.

5.  5

    ### Check model IDs and features

    - **Model IDs:** If you use a model earlier than Claude 4.6, replace the `@` before the snapshot date in its ID with a hyphen. For example, `claude-haiku-4-5@20251001` becomes `claude-haiku-4-5-20251001`. For the models and their IDs, see [API model IDs](#api-model-ids).
    - **Features:** Check [Feature support](#feature-support) for each feature your code uses.
    - **Location:** If you use a multi-region or regional endpoint today, check which location Claude Models on Google Cloud (Anthropic managed) uses. See [Project, location, and workspace resolution](#project-location-and-workspace-resolution).

6.  6

    ### Run a test request

    Run the request in [Making requests](#making-requests) to check that your setup works. Then run your own code. If a call fails with a permission error, see [Troubleshooting account setup](#troubleshooting-account-setup). Before you move production traffic, check the [rate limits for Claude Models on Google Cloud (Anthropic managed)](#rate-limits).

## Next steps



[Features overview](build-with-claude-overview.md)

Explore Claude's features.



[IAM permissions](../Endpoints/claude-models-on-google-cloud-anthropic-managed-iam-permissions.md)

Look up permissions, roles, and audit log types.



[Model deprecations](../../20-Models/about-claude-model-deprecations.md)

As safer and more capable models launch, Anthropic regularly retires older ones. See all API deprecations, along with recommended replacements.

[Google Cloud Marketplace](https://console.cloud.google.com/marketplace)

Manage your subscription and billing.
