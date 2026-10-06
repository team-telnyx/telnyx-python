# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WhatsappCallingRoutingData"]


class WhatsappCallingRoutingData(BaseModel):
    connection_id: Optional[str] = None
    """ID of the routing connection, or `null` when none is set."""

    phone_number: str
    """Phone number in E.164 format, with a leading `+`."""

    record_type: Literal["whatsapp_calling_routing"]
    """Identifies the type of the resource."""
