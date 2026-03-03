---
category: "02-Claude-Code-CLI"
fetched_at: "2026-03-03T15:08:40Z"
source_url: "https://code.claude.com/docs/en/amazon-bedrock"
title: "Claude Code on Amazon Bedrock - Claude Code Docs"
---

# Claude Code on Amazon Bedrock


Learn about configuring Claude Code through Amazon Bedrock, including setup, IAM configuration, and troubleshooting.


## 

[​](#prerequisites)

Prerequisites

Before configuring Claude Code with Bedrock, ensure you have:

- An AWS account with Bedrock access enabled
- Access to desired Claude models (for example, Claude Sonnet 4.6) in Bedrock
- AWS CLI installed and configured (optional - only needed if you don’t have another mechanism for getting credentials)
- Appropriate IAM permissions

If you are deploying Claude Code to multiple users, [pin your model versions](#4-pin-model-versions) to prevent breakage when Anthropic releases new models.

## 

[​](#setup)

Setup

### 

[​](#1-submit-use-case-details)

1. Submit use case details

First-time users of Anthropic models are required to submit use case details before invoking a model. This is done once per account.

1.  Ensure you have the right IAM permissions (see more on that below)
2.  Navigate to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/)
3.  Select **Chat/Text playground**
4.  Choose any Anthropic model and you will be prompted to fill out the use case form

### 

[​](#2-configure-aws-credentials)

2. Configure AWS credentials

Claude Code uses the default AWS SDK credential chain. Set up your credentials using one of these methods: **Option A: AWS CLI configuration**

Report incorrect code

Copy


``` shiki
aws configure
```

**Option B: Environment variables (access key)**

Report incorrect code

Copy


``` shiki
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
export AWS_SESSION_TOKEN=your-session-token
```

**Option C: Environment variables (SSO profile)**

Report incorrect code

Copy


``` shiki
aws sso login --profile=<your-profile-name>

export AWS_PROFILE=your-profile-name
```

**Option D: AWS Management Console credentials**

Report incorrect code

Copy


``` shiki
aws login
```

[Learn more](https://docs.aws.amazon.com/signin/latest/userguide/command-line-sign-in.html) about `aws login`. **Option E: Bedrock API keys**

Report incorrect code

Copy


``` shiki
export AWS_BEARER_TOKEN_BEDROCK=your-bedrock-api-key
```

Bedrock API keys provide a simpler authentication method without needing full AWS credentials. [Learn more about Bedrock API keys](https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/).

#### 

[​](#advanced-credential-configuration)

Advanced credential configuration

Claude Code supports automatic credential refresh for AWS SSO and corporate identity providers. Add these settings to your Claude Code settings file (see [Settings](/docs/en/settings) for file locations). When Claude Code detects that your AWS credentials are expired (either locally based on their timestamp or when Bedrock returns a credential error), it will automatically run your configured `awsAuthRefresh` and/or `awsCredentialExport` commands to obtain new credentials before retrying the request.

##### Example configuration

Report incorrect code

Copy


``` shiki
{
  "awsAuthRefresh": "aws sso login --profile myprofile",
  "env": {
    "AWS_PROFILE": "myprofile"
  }
}
```

##### Configuration settings explained

**`awsAuthRefresh`**: Use this for commands that modify the `.aws` directory, such as updating credentials, SSO cache, or config files. The command’s output is displayed to the user, but interactive input isn’t supported. This works well for browser-based SSO flows where the CLI displays a URL or code and you complete authentication in the browser. **`awsCredentialExport`**: Only use this if you can’t modify `.aws` and must directly return credentials. Output is captured silently and not shown to the user. The command must output JSON in this format:

Report incorrect code

Copy


``` shiki
{
  "Credentials": {
    "AccessKeyId": "value",
    "SecretAccessKey": "value",
    "SessionToken": "value"
  }
}
```

### 

[​](#3-configure-claude-code)

3. Configure Claude Code

Set the following environment variables to enable Bedrock:

Report incorrect code

Copy


``` shiki
# Enable Bedrock integration
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=us-east-1  # or your preferred region

# Optional: Override the region for the small/fast model (Haiku)
export ANTHROPIC_SMALL_FAST_MODEL_AWS_REGION=us-west-2
```

When enabling Bedrock for Claude Code, keep the following in mind:

- `AWS_REGION` is a required environment variable. Claude Code does not read from the `.aws` config file for this setting.
- When using Bedrock, the `/login` and `/logout` commands are disabled since authentication is handled through AWS credentials.
- You can use settings files for environment variables like `AWS_PROFILE` that you don’t want to leak to other processes. See [Settings](/docs/en/settings) for more information.

### 

[​](#4-pin-model-versions)

4. Pin model versions

Pin specific model versions for every deployment. If you use model aliases (`sonnet`, `opus`, `haiku`) without pinning, Claude Code may attempt to use a newer model version that isn’t available in your Bedrock account, breaking existing users when Anthropic releases updates.

Set these environment variables to specific Bedrock model IDs:

Report incorrect code

Copy


``` shiki
export ANTHROPIC_DEFAULT_OPUS_MODEL='us.anthropic.claude-opus-4-6-v1'
export ANTHROPIC_DEFAULT_SONNET_MODEL='us.anthropic.claude-sonnet-4-6'
export ANTHROPIC_DEFAULT_HAIKU_MODEL='us.anthropic.claude-haiku-4-5-20251001-v1:0'
```

These variables use cross-region inference profile IDs (with the `us.` prefix). If you use a different region prefix or application inference profiles, adjust accordingly. For current and legacy model IDs, see [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview). See [Model configuration](/docs/en/model-config#pin-models-for-third-party-deployments) for the full list of environment variables. Claude Code uses these default models when no pinning variables are set:

| Model type       | Default value                                 |
|:-----------------|:----------------------------------------------|
| Primary model    | `global.anthropic.claude-sonnet-4-6`          |
| Small/fast model | `us.anthropic.claude-haiku-4-5-20251001-v1:0` |

To customize models further, use one of these methods:

Report incorrect code

Copy


``` shiki
# Using inference profile ID
export ANTHROPIC_MODEL='global.anthropic.claude-sonnet-4-6'
export ANTHROPIC_SMALL_FAST_MODEL='us.anthropic.claude-haiku-4-5-20251001-v1:0'

# Using application inference profile ARN
export ANTHROPIC_MODEL='arn:aws:bedrock:us-east-2:your-account-id:application-inference-profile/your-model-id'

# Optional: Disable prompt caching if needed
export DISABLE_PROMPT_CACHING=1
```

[Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) may not be available in all regions.

## 

[​](#iam-configuration)

IAM configuration

Create an IAM policy with the required permissions for Claude Code:

Report incorrect code

Copy


``` shiki
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowModelAndInferenceProfileAccess",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream",
        "bedrock:ListInferenceProfiles"
      ],
      "Resource": [
        "arn:aws:bedrock:*:*:inference-profile/*",
        "arn:aws:bedrock:*:*:application-inference-profile/*",
        "arn:aws:bedrock:*:*:foundation-model/*"
      ]
    },
    {
      "Sid": "AllowMarketplaceSubscription",
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:ViewSubscriptions",
        "aws-marketplace:Subscribe"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:CalledViaLast": "bedrock.amazonaws.com"
        }
      }
    }
  ]
}
```

For more restrictive permissions, you can limit the Resource to specific inference profile ARNs. For details, see [Bedrock IAM documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html).

Create a dedicated AWS account for Claude Code to simplify cost tracking and access control.

## 

[​](#aws-guardrails)

AWS Guardrails

[Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) let you implement content filtering for Claude Code. Create a Guardrail in the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/), publish a version, then add the Guardrail headers to your [settings file](/docs/en/settings). Enable Cross-Region inference on your Guardrail if you’re using cross-region inference profiles. Example configuration:

Report incorrect code

Copy


``` shiki
{
  "env": {
    "ANTHROPIC_CUSTOM_HEADERS": "X-Amzn-Bedrock-GuardrailIdentifier: your-guardrail-id\nX-Amzn-Bedrock-GuardrailVersion: 1"
  }
}
```

## 

[​](#troubleshooting)

Troubleshooting

If you encounter region issues:

- Check model availability: `aws bedrock list-inference-profiles --region your-region`
- Switch to a supported region: `export AWS_REGION=us-east-1`
- Consider using inference profiles for cross-region access

If you receive an error “on-demand throughput isn’t supported”:

- Specify the model as an [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html) ID

Claude Code uses the Bedrock [Invoke API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) and does not support the Converse API.

## 

[​](#additional-resources)

Additional resources

- [Bedrock documentation](https://docs.aws.amazon.com/bedrock/)
- [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
- [Bedrock inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)
- [Claude Code on Amazon Bedrock: Quick Setup Guide](https://community.aws/content/2tXkZKrZzlrlu0KfH8gST5Dkppq/claude-code-on-amazon-bedrock-quick-setup-guide)- [Claude Code Monitoring Implementation (Bedrock)](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock/blob/main/assets/docs/MONITORING.md)
