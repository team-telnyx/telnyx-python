# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .inbound_message import InboundMessage

__all__ = ["InboundMessageWebhookEvent"]


class InboundMessageWebhookEvent(BaseModel):
    data: Optional[InboundMessage] = None
