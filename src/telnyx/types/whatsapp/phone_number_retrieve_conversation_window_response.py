# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PhoneNumberRetrieveConversationWindowResponse", "Data"]


class Data(BaseModel):
    last_user_message_at: Optional[datetime] = None
    """Timestamp of the last inbound message that opened the window"""

    window_active: Optional[bool] = None
    """Whether the 24-hour conversation window is currently open"""

    window_expires_at: Optional[datetime] = None
    """When the window closes. Null if no active window."""

    window_type: Optional[str] = None
    """Window type. Currently always 24h when present."""


class PhoneNumberRetrieveConversationWindowResponse(BaseModel):
    data: Optional[Data] = None
