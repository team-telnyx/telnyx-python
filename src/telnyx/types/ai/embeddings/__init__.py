# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .bucket_list_response import BucketListResponse as BucketListResponse
    from .bucket_retrieve_response import BucketRetrieveResponse as BucketRetrieveResponse


def __getattr__(name: str) -> Any:
    if name == "BucketRetrieveResponse":
        from .bucket_retrieve_response import BucketRetrieveResponse

        return BucketRetrieveResponse
    if name == "BucketListResponse":
        from .bucket_list_response import BucketListResponse

        return BucketListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
