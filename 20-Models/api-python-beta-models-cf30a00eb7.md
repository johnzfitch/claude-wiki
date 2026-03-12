---
category: "20-Models"
fetched_at: "2026-03-12T08:16:41Z"
source_url: "https://platform.claude.com/docs/en/api/python/beta/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/beta/models/list)

beta.models.list(ModelListParams\*\*kwargs) -\> SyncPage\[[BetaModelInfo](/docs/en/api/beta#beta_model_info)\]

GET/v1/models

##### [Get a Model](/docs/en/api/beta/models/retrieve)

beta.models.retrieve(strmodel_id, ModelRetrieveParams\*\*kwargs) -\> [BetaModelInfo](/docs/en/api/beta#beta_model_info)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

class BetaModelInfo: …

id: str

Unique model identifier.

created_at: datetime

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: str

A human-readable name for the model.

type: Literal\["model"\]

Object type.

For Models, this is always `"model"`.
