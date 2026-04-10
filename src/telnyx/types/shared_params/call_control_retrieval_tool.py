# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .call_control_bucket_ids import CallControlBucketIDs

__all__ = ["CallControlRetrievalTool"]


class CallControlRetrievalTool(TypedDict, total=False):
    retrieval: Required[CallControlBucketIDs]

    type: Required[Literal["retrieval"]]
