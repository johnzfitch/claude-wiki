---
category: "20-Models"
fetched_at: "2026-02-22T14:20:27Z"
source_url: "https://platform.claude.com/docs/en/api/csharp/models"
title: "Models - Claude API Reference"
---
# Models

##### [List Models](/docs/en/api/models/list)

[ModelListPageResponse](/docs/en/api/models#ModelListPageResponse) Models.List(ModelListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

[ModelInfo](/docs/en/api/models#model_info) Models.Retrieve(ModelRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class ModelInfo:

required string ID

Unique model identifier.

required DateTimeOffset CreatedAt

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

required string DisplayName

A human-readable name for the model.

JsonElement Type "model"constant

Object type.

For Models, this is always `"model"`.
