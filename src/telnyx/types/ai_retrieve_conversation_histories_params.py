# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AIRetrieveConversationHistoriesParams"]


class AIRetrieveConversationHistoriesParams(TypedDict, total=False):
    q: Required[str]
    """Natural language search query.

    The text is embedded into a 1024-dimensional vector and compared against indexed
    record chunks using kNN cosine similarity.
    """

    record_type: Required[Literal["voice", "message", "ai_pipeline_storage", "knowledge_base"]]
    """The type of records to search.

    Each record type is stored in a separate vector index.
    """

    filter_document_id: Annotated[str, PropertyInfo(alias="filter[document_id]")]
    """Filter by document identifier (exact match).

    Populated for knowledge_base records.
    """

    filter_ingested_at_gte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[ingested_at][gte]", format="iso8601")
    ]
    """
    Only include records ingested (chunked, embedded, and indexed) on or after this
    ISO 8601 timestamp.
    """

    filter_ingested_at_lte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[ingested_at][lte]", format="iso8601")
    ]
    """
    Only include records ingested (chunked, embedded, and indexed) on or before this
    ISO 8601 timestamp.
    """

    filter_record_created_at_gte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[record_created_at][gte]", format="iso8601")
    ]
    """
    Only include records whose original creation time is on or after this ISO 8601
    timestamp.
    """

    filter_record_created_at_lte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[record_created_at][lte]", format="iso8601")
    ]
    """
    Only include records whose original creation time is on or before this ISO 8601
    timestamp.
    """

    filter_record_id: Annotated[str, PropertyInfo(alias="filter[record_id]")]
    """Filter to chunks belonging to a specific parent record (exact match)."""

    filter_region_in: Annotated[str, PropertyInfo(alias="filter[region][in]")]
    """Filter by the region stored on the record.

    Comma-separated to match multiple regions (USA, DEU, AUS, UAE). Distinct from
    the `region` parameter, which selects which cluster(s) are queried.
    """

    filter_retention: Annotated[str, PropertyInfo(alias="filter[retention]")]
    """Filter by retention policy (exact match).

    Filter-only: not returned in the response body.
    """

    filter_user_id: Annotated[str, PropertyInfo(alias="filter[user_id]")]
    """Filter to records owned by a specific user (exact match)."""

    min_score: float
    """Minimum cosine similarity score threshold (0.0 to 1.0).

    Results below this threshold are excluded.
    """

    region: Literal["USA", "DEU", "AUS", "UAE"]
    """Restrict search to a specific region's OpenSearch cluster.

    When omitted, all regions are queried in parallel (fan-out) and results are
    merged by cosine similarity score.
    """

    top_k: int
    """Maximum number of results to return. Defaults to 20, maximum 100."""
