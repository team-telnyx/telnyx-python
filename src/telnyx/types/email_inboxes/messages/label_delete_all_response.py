# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._models import BaseModel
from ...inbound_message import InboundMessage

__all__ = ["LabelDeleteAllResponse"]


class LabelDeleteAllResponse(BaseModel):
    data: InboundMessage
