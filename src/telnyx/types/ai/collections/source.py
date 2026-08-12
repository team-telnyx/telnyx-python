# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel
from .source_type import SourceType

__all__ = ["Source"]


class Source(BaseModel):
    id: Optional[str] = None

    bucket_id: Optional[str] = None
    """The Telnyx Storage bucket name. Present only for `bucket` sources."""

    collection_id: Optional[str] = None

    record_type: Optional[str] = None
    """Identifies the record type. Always `ai_collection_source`."""

    source_type: Optional[SourceType] = None
    """The type of Telnyx data attached as a source.

    `bucket` requires an additional `bucket_id`. Only `voice` is searchable today;
    `meeting_bot`, `message`, and `bucket` attach but are not yet searchable (Coming
    soon).
    """

    status: Optional[str] = None
