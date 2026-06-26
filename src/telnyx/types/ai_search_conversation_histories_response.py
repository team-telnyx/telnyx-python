# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AISearchConversationHistoriesResponse", "Data", "Meta"]


class Data(BaseModel):
    """A single search result representing one chunk of a conversation history record.

    Records are split into chunks of up to 480 tokens with 64-token overlap at ingestion time.
    """

    id: str
    """Unique chunk identifier."""

    chunk_index: int
    """Zero-based index of this chunk within the parent record."""

    chunk_total: int
    """Total number of chunks the parent record was split into."""

    ingested_at: datetime
    """When the record was chunked, embedded, and indexed (ISO 8601)."""

    organization_id: str
    """Identifier of the organization that owns this record."""

    record_created_at: datetime
    """When the original record was created (ISO 8601)."""

    record_id: str
    """Identifier of the parent record.

    Multiple chunks from the same record share this ID.
    """

    region: Literal["USA", "DEU", "AUS", "UAE"]
    """The region where this record is stored."""

    score: float
    """Cosine similarity score between the query vector and this chunk's vector.

    Higher values indicate greater semantic relevance.
    """

    text: str
    """The text content of this chunk (up to 480 tokens)."""

    user_id: str
    """Identifier of the user who owns this record."""

    metadata: Optional[Dict[str, object]] = None
    """Arbitrary metadata attached to the record at ingestion time.

    Filterable via filter[field]=value query parameters.
    """


class Meta(BaseModel):
    """Pagination metadata following the standard Telnyx V2 API format."""

    page_number: int
    """Current page number (1-based), matching the requested page[number]."""

    page_size: int
    """Number of results per page, matching the requested page[size]."""

    total_pages: int
    """Total number of pages."""

    total_results: int
    """Total number of matching results across all queried regions."""


class AISearchConversationHistoriesResponse(BaseModel):
    """Search response following the standard Telnyx V2 API format."""

    data: List[Data]
    """
    Ranked list of matching text chunks, sorted by cosine similarity score
    descending.
    """

    meta: Meta
    """Pagination metadata following the standard Telnyx V2 API format."""
