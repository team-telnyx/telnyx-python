# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CollectionRetrieveDocumentsParams"]


class CollectionRetrieveDocumentsParams(TypedDict, total=False):
    filter: Dict[str, object]
    """Field filters applied before ranking, using `filter[field][operator]=value`.

    Supported operators: `eq` (default), `in`, `gte`, `gt`, `lte`, `lt`, `contains`.
    Known fields: `record_type`, `record_id`, `user_id`, `record_created_at`,
    `ingested_at`; any other name resolves to a `metadata.<field>` filter. Example:
    `filter[record_id][eq]=rec_123`.
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number to return (1-based). Defaults to 1."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of results per page. Defaults to 20."""

    query: str
    """Natural-language search query.

    When provided, the text is matched against the collection's document chunks
    using the collection's `retrieval_type` (vector or hybrid). When omitted,
    documents are returned as a plain catalog listing.
    """

    retrieval_type: Literal["vector", "hybrid", "keyword"]
    """Reserved; not yet functional.

    A value supplied here is accepted but ignored — it does not override the
    collection's configured strategy, and it is not echoed back. Searches run
    `vector` retrieval, and `meta.retrieval_type` reports the mode that actually
    ran. To change retrieval strategy, set it on the collection's settings
    subresource.
    """

    sources: str
    """Comma-separated list of source types to restrict the search to.

    When omitted, all of the collection's sources are searched.
    """

    top_k: int
    """Maximum number of ranked results to consider.

    When omitted, the collection's configured `top_k` setting is used.
    """
