# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel
from .email_event_type import EmailEventType

__all__ = ["MessageEvent"]


class MessageEvent(BaseModel):
    occurred_at: datetime

    type: EmailEventType

    payload: Optional[Dict[str, object]] = None
