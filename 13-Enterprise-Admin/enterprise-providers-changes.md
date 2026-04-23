---
title: "Enterprise Providers Changes: 2.1.59 → 2.1.70"
category: "13-Enterprise-Admin"
tags: ["bedrock", "enterprise"]
---

# Enterprise Providers Changes: 2.1.59 → 2.1.70

## Overview

2.1.70 adds **Microsoft Foundry** as a third enterprise provider, making Claude Code
work across three hyperscaler platforms:

```
                      ┌─────────────────────────────────┐
                      │         Claude Code CLI         │ 
                      └────────────┬────────────────────┘
                                   │ provider selection
              ┌────────────────────┼────────────────────────┐
              │                    │                        │
    ┌─────────▼──────────┐ ┌───────▼───────┐  ┌─────────────▼────────────────────┐
    │   AWS Bedrock      │ │ Google Vertex │  │       Microsoft Foundry          │  ← NEW
    │ CLAUDE_CODE_USE_   │ │  AI (exists)  │  │     CLAUDE_CODE_USE_FOUNDRY      │
    │    BEDROCK         │ └───────────────┘  │        + Azure AD Auth           │          
    │  + IAM/STS chain   │                    │        + FOUNDRY_RESOURCE        │ 
    │  + SSO support     │                    │                                  │
    └────────────────────┘                    └──────────────────────────────────┘
```

## Microsoft Foundry (New)

### Authentication Flow
```
CLAUDE_CODE_USE_FOUNDRY=true
  → FoundryClient(baseURL=ANTHROPIC_FOUNDRY_BASE_URL,
                  apiKey=ANTHROPIC_FOUNDRY_API_KEY,
                  resource=ANTHROPIC_FOUNDRY_RESOURCE)
  → DefaultAzureCredential (MSAL / Azure AD)
  OR
  CLAUDE_CODE_SKIP_FOUNDRY_AUTH=true → empty credential
```

### Restrictions
- Fast mode unavailable: "Fast mode is not available on Bedrock, Vertex, or Foundry"
- Telemetry disabled when Foundry active
- Feedback command disabled when Foundry active

### Model naming (inferred)
The `foundry` slot in the model map (e.g., `sonnet37.foundry`) likely uses
Azure-specific model deployment names, not claude-* IDs.

## AWS Bedrock Expansion

### New Headers (2.1.70 only)
| Header | Purpose |
|--------|---------|
| `X-Amzn-Bedrock-GuardrailIdentifier` | AWS Guardrails policy ID |
| `X-Amzn-Bedrock-GuardrailVersion` | Guardrails version |
| `X-Amzn-Bedrock-Service-Tier` | Service tier selection |
| `X-Amzn-Bedrock-PerformanceConfig-Latency` | Latency optimization |
| `X-Amzn-Bedrock-Trace` | Request tracing |

### New Bedrock APIs
- **Reranking**: `VectorSearchBedrockRerankingConfiguration`, `BEDROCK_RERANKING_MODEL`
- **Inference Profiles**: `ListInferenceProfilesCommand`, `GetInferenceProfileCommand`
- **Prompt Routers**: `paginateListPromptRouters`
- **Provisioned Throughput**: `paginateListProvisionedModelThroughputs`

### New Auth Options
- `AWS_BEARER_TOKEN_BEDROCK` — bearer token (simpler than IAM role chain)
- `CLAUDE_CODE_SKIP_BEDROCK_AUTH` — skip auth (for testing/custom endpoints)
- `ANTHROPIC_BEDROCK_BASE_URL` — custom Bedrock endpoint

## Model Routing Map (2.1.70)

```javascript
// Each model has 4 provider variants
const modelMap = {
  haiku35:  { firstParty: "claude-haiku-3-5-...", bedrock: "...", vertex: "...", foundry: "..." },
  haiku45:  { firstParty: "claude-haiku-4-5-...", ... },
  sonnet35: { ... },
  sonnet37: { firstParty: "claude-3-7-sonnet-20250219", bedrock: "...", vertex: "claude-3-7-sonnet@20250219", foundry: "claude-3-7-sonnet" },
  sonnet40: { ... },
  sonnet45: { ... },  // NEW
  sonnet46: { ... },  // NEW — current model (claude-sonnet-4-6)
  opus40:   { ... },
  opus41:   { ... },  // NEW
  opus45:   { ... },  // NEW
  opus46:   { ... },  // NEW
}
```
