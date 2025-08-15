# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["InferenceEmbeddingBucketIDs"]


class InferenceEmbeddingBucketIDs(BaseModel):
    bucket_ids: List[str]
    """
    List of
    [embedded storage buckets](https://developers.telnyx.com/api/inference/inference-embedding/post-embedding)
    to use for retrieval-augmented generation.
    """

    max_num_results: Optional[int] = None
    """The maximum number of results to retrieve as context for the language model."""
