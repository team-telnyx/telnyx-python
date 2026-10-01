# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["AssistantWhatsappResponse"]


class AssistantWhatsappResponse(BaseModel):
    conversation_id: str
    """ID of the conversation created for this WhatsApp chat."""

    message_id: str
    """ID of the WhatsApp template message that was sent."""
