# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WhatsappAccountUpdate", "Data", "DataPayload"]


class DataPayload(BaseModel):
    event: str
    """Account event reported by Meta.

    Coexistence lifecycle values include `ACCOUNT_OFFBOARDED`,
    `ACCOUNT_RECONNECTED`, and `PARTNER_REMOVED`. Preserve unknown values for
    forward compatibility.
    """

    record_type: Literal["whatsapp_account"]

    waba_id: str
    """Meta WhatsApp Business Account identifier."""


class Data(BaseModel):
    id: str

    event_type: Literal["whatsapp.account.update"]

    occurred_at: datetime

    payload: DataPayload

    record_type: Literal["event"]


class WhatsappAccountUpdate(BaseModel):
    data: Data
