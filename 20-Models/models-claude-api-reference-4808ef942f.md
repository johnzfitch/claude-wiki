---
category: "20-Models"
fetched_at: "2026-03-03T14:57:06Z"
source_url: "https://platform.claude.com/docs/en/api/models"
title: "Models - Claude API Reference"
---

# Models

##### [List Models](/docs/en/api/models/list)

GET/v1/models

##### [Get a Model](/docs/en/api/models/retrieve)

GET/v1/models/{model_id}

##### ModelsExpand Collapse 

ModelInfo = object { id, created_at, display_name, type }

id: string

Unique model identifier.

created_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display_name: string

A human-readable name for the model.

type: "model"

Object type.

For Models, this is always `"model"`.
