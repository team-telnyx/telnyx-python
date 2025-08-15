# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .inference_embedding_bucket_ids_param import InferenceEmbeddingBucketIDsParam

__all__ = ["RetrievalToolParam"]


class RetrievalToolParam(TypedDict, total=False):
    retrieval: Required[InferenceEmbeddingBucketIDsParam]

    type: Required[Literal["retrieval"]]
