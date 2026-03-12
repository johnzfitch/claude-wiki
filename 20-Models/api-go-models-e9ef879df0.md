---
category: "20-Models"
fetched_at: "2026-03-12T08:17:09Z"
source_url: "https://platform.claude.com/docs/en/api/go/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/models/list)

client.Models.List(ctx, params) (\*Page\[[ModelInfo](/docs/en/api/models#model_info)\], error)

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

client.Models.Get(ctx, modelID, query) (\*[ModelInfo](/docs/en/api/models#model_info), error)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

type ModelInfo struct{…}

ID string

Unique model identifier.

CreatedAt Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

DisplayName string

A human-readable name for the model.

Type Model

Object type.

For Models, this is always `"model"`.
