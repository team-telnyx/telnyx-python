# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["InferenceEmbeddingBucketIDsParam"]


class InferenceEmbeddingBucketIDsParam(TypedDict, total=False):
    bucket_ids: Required[List[str]]
    """
    List of
    [embedded storage buckets](https://developers.telnyx.com/api/inference/inference-embedding/post-embedding)
    to use for retrieval-augmented generation.
    """

    max_num_results: int
    """The maximum number of results to retrieve as context for the language model."""
