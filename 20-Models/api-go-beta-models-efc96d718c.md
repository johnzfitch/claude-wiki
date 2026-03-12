---
category: "20-Models"
fetched_at: "2026-03-12T08:17:11Z"
source_url: "https://platform.claude.com/docs/en/api/go/beta/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/beta/models/list)

client.Beta.Models.List(ctx, params) (\*Page\[[BetaModelInfo](/docs/en/api/beta#beta_model_info)\], error)

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

client.Beta.Models.Get(ctx, modelID, query) (\*[BetaModelInfo](/docs/en/api/beta#beta_model_info), error)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

type BetaModelInfo struct{…}

ID string

Unique model identifier.

CreatedAt Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

DisplayName string

A human-readable name for the model.

Type Model

Object type.

For Models, this is always `"model"`.
