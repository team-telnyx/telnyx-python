# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["WhatsappReaction"]


class WhatsappReaction(BaseModel):
    emoji: Optional[str] = None

    message_id: Optional[str] = None
