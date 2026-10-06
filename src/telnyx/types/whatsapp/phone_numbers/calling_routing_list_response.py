# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._models import BaseModel
from .whatsapp_calling_routing_data import WhatsappCallingRoutingData

__all__ = ["CallingRoutingListResponse"]


class CallingRoutingListResponse(BaseModel):
    data: WhatsappCallingRoutingData
