# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RetrievalSettingsParam"]


class RetrievalSettingsParam(TypedDict, total=False):
    """How documents are retrieved when searching the collection."""

    retrieval_type: Literal["vector", "hybrid", "keyword"]
    """Retrieval strategy.

    `vector` runs semantic similarity search; `hybrid` combines vector similarity
    with keyword matching; `keyword` runs lexical (BM25) matching.
    """

    top_k: int
    """Number of top results to retrieve (1–50)."""
