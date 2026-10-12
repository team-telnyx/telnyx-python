# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .enterprises.reputation.reputation_number_source import ReputationNumberSource

__all__ = ["NumberReputationNumberFlaggedWebhookEvent", "Data", "DataPayload", "Meta"]


class DataPayload(BaseModel):
    confirm_by: datetime
    """
    Confirm ownership before this time or the number is removed (carrier change) or
    flagged (re-verification).
    """

    enterprise_id: str

    flag_reason: Literal["carrier_changed", "reverification_due"]
    """`carrier_changed`: the number moved to a different carrier.

    `reverification_due`: the periodic ownership re-verification is due.
    """

    ownership_status: Literal["pending_confirmation"]

    phone_number: str

    record_type: Literal["reputation_phone_number"]

    source: ReputationNumberSource
    """Where the phone number is hosted.

    `telnyx`: in your Telnyx inventory. `external`: a number you own that is hosted
    with another provider.
    """


class Data(BaseModel):
    id: str
    """Identifies the event; the same id is reused if the event is redelivered."""

    event_type: Literal["number_reputation.number.flagged"]

    occurred_at: datetime

    payload: DataPayload

    record_type: Literal["event"]


class Meta(BaseModel):
    attempt: int

    delivered_to: str


class NumberReputationNumberFlaggedWebhookEvent(BaseModel):
    data: Data

    meta: Meta
