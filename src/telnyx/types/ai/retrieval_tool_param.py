# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RetrievalToolParam"]


class RetrievalToolParam(TypedDict, total=False):
    retrieval: Required["BucketIDsParam"]

    type: Required[Literal["retrieval"]]


from .bucket_ids_param import BucketIDsParam
