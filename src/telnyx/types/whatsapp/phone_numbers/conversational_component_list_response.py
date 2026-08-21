# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ...._models import BaseModel
from .whatsapp_conversational_component import WhatsappConversationalComponent

__all__ = ["ConversationalComponentListResponse"]


class ConversationalComponentListResponse(BaseModel):
    data: Optional[WhatsappConversationalComponent] = None
