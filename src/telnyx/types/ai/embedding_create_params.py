# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EmbeddingCreateParams"]


class EmbeddingCreateParams(TypedDict, total=False):
    bucket_name: Required[str]

    document_chunk_overlap_size: int

    document_chunk_size: int

    embedding_model: Literal["thenlper/gte-large", "intfloat/multilingual-e5-large"]
    """Supported models to vectorize and embed documents."""

    loader: Literal["default", "intercom"]
    """Supported types of custom document loaders for embeddings."""
