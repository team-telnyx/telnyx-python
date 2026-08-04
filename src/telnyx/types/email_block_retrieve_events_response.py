# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .offset_meta import OffsetMeta

__all__ = ["EmailBlockRetrieveEventsResponse", "Data"]


class Data(BaseModel):
    id: str

    actor: str
    """Free-text (`user_id`/`org_id`/`api_key`/`dev_bypass`/`system`/`manual`)."""

    event_type: Literal["created", "removed", "expired", "override_used"]

    occurred_at: datetime

    reason: str
    """Free-text snapshot of the block's reason at event time."""

    record_type: Literal["email_block_event"]
    """View-only."""

    source: str
    """Free-text snapshot of the block's source at event time."""

    meta: Optional[Dict[str, object]] = None
    """`null` when the schema field is nil (the context usually sets it to `{}`)."""


class EmailBlockRetrieveEventsResponse(BaseModel):
    data: List[Data]

    meta: OffsetMeta
