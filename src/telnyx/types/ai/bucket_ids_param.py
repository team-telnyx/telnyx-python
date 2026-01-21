# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BucketIDsParam"]


class BucketIDsParam(TypedDict, total=False):
    bucket_ids: Required[SequenceNotStr[str]]
    """
    List of
    [embedded storage buckets](https://developers.telnyx.com/api-reference/embeddings/embed-documents)
    to use for retrieval-augmented generation.
    """

    max_num_results: int
    """The maximum number of results to retrieve as context for the language model."""
