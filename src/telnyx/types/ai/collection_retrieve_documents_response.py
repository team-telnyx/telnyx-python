# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CollectionRetrieveDocumentsResponse"]


class CollectionRetrieveDocumentsResponse(BaseModel):
    id: Optional[str] = None

    chunk_index: Optional[int] = None

    chunk_total: Optional[int] = None

    ingested_at: Optional[datetime] = None

    metadata: Optional[Dict[str, object]] = None

    organization_id: Optional[str] = None

    record_created_at: Optional[datetime] = None

    record_id: Optional[str] = None

    record_type: Optional[str] = None
    """The source record kind this chunk came from (e.g.

    `voice`, `meeting_bot`, `message`).
    """

    region: Optional[str] = None

    score: Optional[float] = None
    """Relevance score (higher = more relevant) for ranked search.

    `0.0` for plain catalog listings (when `query` is omitted).
    """

    text: Optional[str] = None

    user_id: Optional[str] = None
