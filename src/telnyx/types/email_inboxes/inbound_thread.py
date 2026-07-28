# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InboundThread"]


class InboundThread(BaseModel):
    id: str

    created_at: datetime

    inbox_id: str

    labels: List[str]
    """Mutable thread labels used for agent workflow state.

    Independent of the labels on the thread's messages, and distinct from the
    send-time `tags` on outbound messages.
    """

    last_message_at: datetime

    last_message_id: str

    message_count: int
    """Total inbound and outbound messages in the thread."""

    preview: Optional[str] = None

    record_type: Literal["email_thread"]

    subject: Optional[str] = None

    unread_count: int
    """Unread inbound messages; outbound messages never increment this count."""

    updated_at: datetime
