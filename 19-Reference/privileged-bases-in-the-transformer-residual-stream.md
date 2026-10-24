---
title: "Privileged bases in the transformer residual stream \\ Anthropic"
source_url: "https://www.anthropic.com/research/privileged-bases-in-the-transformer-residual-stream"
category: "19-Reference"
fetched_at: "2026-10-21T06:30:29Z"
tags: ["news-research"]
---

# Privileged bases in the transformer residual stream

[Read Paper](https://transformer-circuits.pub/2023/privileged-basis/index.html)

- Published

  Mar 16, 2023

- Team

  [Interpretability](team-interpretability.md)

- Topics

  - [Interpretability](https://www.anthropic.com/search?topic=interpretability)
  - [Training](https://www.anthropic.com/search?topic=training)

Related articles

- Interpretability

  Sep 14, 2022

  [Toy models of superposition](toy-models-of-superposition.md)

[View more](https://www.anthropic.com/search?topic=interpretability)

### Abstract

Our mathematical theories of the Transformer architecture suggest that individual coordinates in the residual stream should have no special significance (that is, the basis directions should be in some sense "arbitrary" and no more likely to encode information than random directions). Recent work has shown that this observation is false in practice. We investigate this phenomenon and provisionally conclude that the per-dimension normalizers in the Adam optimizer are to blame for the effect.  
  
We explore two other obvious sources of basis dependency in a Transformer: Layer normalization, and finite-precision floating-point calculations. We confidently rule these out as being the source of the observed basis-alignment.
