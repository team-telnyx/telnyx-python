# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["BucketCreatePresignedURLParams"]


class BucketCreatePresignedURLParams(TypedDict, total=False):
    bucket_name: Required[Annotated[str, PropertyInfo(alias="bucketName")]]

    ttl: int
    """The time to live of the token in seconds"""
