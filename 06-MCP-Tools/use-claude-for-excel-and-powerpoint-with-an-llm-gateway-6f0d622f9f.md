---
category: "06-MCP-Tools"
fetched_at: "2026-03-12T08:19:47Z"
source_url: "https://support.claude.com/en/articles/13945233-use-claude-for-excel-and-powerpoint-with-an-llm-gateway"
title: "Use Claude for Excel and PowerPoint with an LLM gateway | Claude Help Center"
---

4.  Use Claude for Excel and PowerPoint with an LLM gateway

# Use Claude for Excel and PowerPoint with an LLM gateway

Updated today


If your organization routes Claude through an internal LLM gateway connected to AWS Bedrock, Google Cloud Vertex AI, or Microsoft Azure, you can use the Claude for Excel and Claude for PowerPoint add-ins without a Claude account.

This is the same gateway pattern used by Claude Code. If your organization already runs **[Claude Code through an LLM gateway](https://code.claude.com/docs/en/llm-gateway)**, you can point the Office add-ins at the same endpoint—no new infrastructure is required.

## Requirements

- Claude for Excel or Claude for PowerPoint installed (from Microsoft Marketplace or deployed by your admin)

- A gateway URL and API token from your IT team

Your organization's IT team manages the gateway. If you don't have these credentials, contact them—Anthropic can't provide or reset them for you.

------------------------------------------------------------------------

## Gateway connection instructions for end users

An administrator needs to deploy Claude for Excel or PowerPoint to your organization before you can connect. For instructions, refer to the following sections:

- **[Get started with Claude for Excel](https://support.claude.com/en/articles/12650343-use-claude-in-excel#h_7992217c45)**

- **[Get started with Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-in-powerpoint#h_dc8c1ce2ac)**

After your admin deploys the add-ins, follow these steps:

1.  Open Excel or PowerPoint and launch the Claude add-in.

2.  On the sign-in screen, select "Enterprise gateway."

3.  Enter the **Gateway URL** and **API token** your IT team provided.

    - **Gateway URL**: The HTTPS base URL of your LLM proxy (for example, `https://llm-gateway.yourcompany.com`).

    - **API token**: The bearer token your proxy expects. The add-in sends this in the `Authorization: Bearer <token>` header with every request.

4.  The add-in checks the connection by sending a test request to the gateway. If it succeeds, you'll see the main app experience.

Your credentials are stored locally in your browser's `localStorage` within the add-in's sandboxed iframe. They aren't synced to Anthropic's servers. Because the Office add-in runs inside a sandboxed iframe within the Microsoft application, it can't use your OS keychain the way Claude Code does—for this reason, only enter gateway-issued tokens, not raw cloud provider credentials.

### Change or update your gateway

If your API token expires or your IT team gives you a new URL, go to "Settings" in the add-in sidebar, enter the new values, and select "Test connection."

------------------------------------------------------------------------

## Gateway requirements for IT teams

The Office add-ins only support the Anthropic Messages API format via the Unified endpoint. This is more specific than Claude Code, which also supports Bedrock InvokeModel and Vertex rawPredict formats directly.

### Required endpoints

Your gateway must expose these two endpoints:

[TABLE]

### Required headers

The gateway must forward the following request headers from the add-in to the upstream provider:

- `anthropic-beta` — Enables beta features required by the add-in.

- `anthropic-version` — Specifies the API version for request/response format.

Failure to forward these headers may result in reduced functionality or prevent the add-in from working.

### Model discovery

On login, the add-in validates the token via GET /v1/messages and then attempts to discover available Claude models via GET /v1/models. If your gateway doesn't expose a model list at that path, the add-in falls back to prompting the user for a model ID manually.

### Differences from Claude Code gateway setup

[TABLE]

------------------------------------------------------------------------

## Example gateway configuration with LiteLLM

Many organizations use [**LiteLLM**](https://github.com/BerriAI/litellm) as their gateway. Below is a minimal `litellm_config.yaml` for routing Office add-in requests to Anthropic, Bedrock, or Vertex.

**Note:** LiteLLM is third-party open-source software and is not maintained by Anthropic.

### Routing to Anthropic directly

**yaml**

    model_list:
      - model_name: claude-sonnet-4-5-20250929
        litellm_params:
          model: claude-sonnet-4-5-20250929
          api_key: os.environ/ANTHROPIC_API_KEY

    litellm_settings:
      drop_params: true
      # Enable the unified Anthropic endpoint
      # This is what the Office add-in will call

### Routing to Amazon Bedrock

**yaml**

    model_list:
      - model_name: claude-sonnet-4-5-20250929
        litellm_params:
          model: bedrock/anthropic.claude-sonnet-4-5-20250929-v1:0
          aws_region_name: us-east-1

    litellm_settings:
      drop_params: true

### Routing to Google Cloud Vertex AI

**Update your litellm_config.yaml:**

    model_list:
      - model_name: claude-sonnet-4-5-20250929
        litellm_params:
          model: vertex_ai/claude-sonnet-4-5-20250929
          vertex_project: your-gcp-project-id
          vertex_location: us-east5

    litellm_settings:
      drop_params: true

### Routing to Azure

**Update your litellm_config.yaml:**

    model_list:
      - model_name: claude-sonnet-4-5-20250929
        litellm_params:
          model: azure_ai/claude-sonnet-4-5-20250929
          api_base: https://your-resource.services.ai.azure.com/anthropic
          api_key: os.environ/AZURE_API_KEY
          extra_headers:
            x-api-key: os.environ/AZURE_API_KEY

    litellm_settings:
      drop_params: true

For detailed setup instructions, refer to **[LiteLLM's Anthropic format documentation](https://docs.litellm.ai/)**.

------------------------------------------------------------------------

## What Anthropic collects

When you use the add-ins through a gateway, Anthropic collects information in accordance with AWS Bedrock, Google Cloud Vertex AI, or Microsoft Azure's terms **and is consistent with Anthropic's arrangements with customers**. Anthropic does not have access to a customer's AWS, Google, or Microsoft instance, including prompts or outputs it contains. **Anthropic does not train generative models with such content or use it for other purposes.** Anthropic **can** access to metadata--such as tool use, token counts, and other items--**and use such metadata for** analytic and product improvement purposes.

For details on what your organization's gateway logs, contact your IT team.

------------------------------------------------------------------------

## How this differs from signing in with a Claude account

When you sign in with a Claude account, the add-ins connect directly to Anthropic. When you connect through a gateway, the add-ins send requests to your organization's infrastructure instead, and your IT team controls how that traffic is routed and logged.

Some features that rely on having a Claude account aren't available through a gateway yet, but we’re working on adding support soon:

[TABLE]

If your team needs these features, talk to your Claude admin about which sign-in path fits your organization.

------------------------------------------------------------------------

## Troubleshooting

### "Connection refused" or network error

The gateway URL is unreachable from the user's network. Verify the URL is correct, the gateway is running, and there are no firewall or VPN restrictions blocking the connection.

### 401 Unauthorized or "Invalid token"

The auth token is invalid or expired. Confirm the token with your IT team. Gateway tokens are managed by your organization, not Anthropic.

### 403 Forbidden or "Access denied"

The token is valid but lacks the right permissions. For Bedrock, verify the gateway's IAM role has bedrock:InvokeModel permissions. For Vertex, verify the service account has aiplatform.endpoints.predict permissions. Contact your IT admin for the correct permissions.

### 404 Not Found

The add-in couldn't reach the expected API path. Verify the gateway URL is the base URL (for example, https://litellm-server:4000) — don't include /v1/messages in the URL field.

### 500 or other server errors

The gateway encountered an internal error. Check your gateway logs (for example, docker logs litellm if using LiteLLM) for upstream provider errors. Try the request again, and contact your IT admin if the issue persists.

### "No models available"

The add-in couldn't find Claude models on your gateway. Your gateway may not expose a model list at GET /model/info. Your IT team can either configure the gateway to serve a model list or give you a specific model ID to enter manually when prompted.

### Streaming responses fail or hang

Verify that your gateway supports Server-Sent Events (SSE) pass-through. Some proxy configurations strip or buffer SSE connections, which prevents streaming responses from reaching the add-in.

### A feature I expected isn't there

Connectors, Skills, file uploads, and memory aren't available through an enterprise gateway. If you need these, ask your admin about signing in with a Claude account instead.

------------------------------------------------------------------------

Related Articles


Claude Code FAQ


Use Claude for Excel


Use Claude for PowerPoint


Public Sector FAQs


Work across Excel and PowerPoint
