---
category: "20-Models"
fetched_at: "2026-03-03T15:06:22Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/beta/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/beta/models/list)

[ModelListPageResponse](/docs/en/api/beta#ModelListPageResponse) Beta.Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

[BetaModelInfo](/docs/en/api/beta#beta_model_info) Beta.Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class BetaModelInfo:

required string ID

Unique model identifier.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

required string DisplayName

A human-readable name for the model.

JsonElement Type "model"constant

Object type.

For Models, this is always `"model"`.
