# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["RetrievalSettings"]


class RetrievalSettings(BaseModel):
    """How documents are retrieved when searching the collection."""

    retrieval_type: Optional[Literal["vector", "hybrid"]] = None
    """Retrieval strategy.

    `vector` runs semantic similarity search; `hybrid` combines vector similarity
    with keyword matching; `keyword` runs lexical (BM25) matching. `keyword` is not
    accepted yet: setting it returns 422 `unsupported_retrieval_type`. A collection
    set to `hybrid` is accepted here but cannot be searched until hybrid execution
    ships.
    """

    top_k: Optional[int] = None
    """Number of top results to retrieve (1–50)."""
