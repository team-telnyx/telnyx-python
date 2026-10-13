# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WhatsappWabaAddedWebhookEvent", "Data", "DataPayload"]


class DataPayload(BaseModel):
    event_id: str
    """Signup session ID."""

    record_type: Literal["waba_account_added"]

    status: Literal["SUCCESS", "FAILURE"]
    """Signup session outcome."""

    waba_id: str
    """Meta WhatsApp Business Account identifier."""

    errors: Optional[List[str]] = None
    """Errors recorded during provisioning."""

    phone_numbers: Optional[List[str]] = None
    """Phone numbers found on the WABA.

    Omitted for standard sessions started with a phone_number_id, and for sessions
    that fail before Telnyx fetches the numbers.
    """


class Data(BaseModel):
    id: str

    event_type: Literal["whatsapp.waba_added"]

    occurred_at: datetime

    payload: DataPayload

    record_type: Literal["event"]


class WhatsappWabaAddedWebhookEvent(BaseModel):
    data: Data
