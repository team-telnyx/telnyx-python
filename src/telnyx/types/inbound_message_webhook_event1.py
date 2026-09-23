# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .messaging_inbound_message import MessagingInboundMessage

__all__ = ["InboundMessageWebhookEvent"]


class InboundMessageWebhookEvent(BaseModel):
    data: Optional[MessagingInboundMessage] = None
