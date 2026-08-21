# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EmbeddingURLParams"]


class EmbeddingURLParams(TypedDict, total=False):
    bucket_name: Required[str]
    """Name of the bucket to store the embeddings. This bucket must already exist."""

    url: Required[str]
    """The URL of the webpage to embed"""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
