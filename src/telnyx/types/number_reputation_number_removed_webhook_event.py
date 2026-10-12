# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .enterprises.reputation.reputation_number_source import ReputationNumberSource

__all__ = ["NumberReputationNumberRemovedWebhookEvent", "Data", "DataPayload", "Meta"]


class DataPayload(BaseModel):
    enterprise_id: str

    ownership_status: Literal["removed"]

    phone_number: str

    record_type: Literal["reputation_phone_number"]

    removal_reason: Literal["ported_away", "unconfirmed_ownership", "reassigned", "customer_reported"]
    """`ported_away`: you confirmed you no longer own it after a carrier change.

    `unconfirmed_ownership`: the confirmation deadline passed. `reassigned`: the
    number was reported as permanently disconnected. `customer_reported`: you
    reported that you no longer own it. Removing a number yourself with `DELETE`
    sends no event.
    """

    removed_at: datetime

    source: ReputationNumberSource
    """Where the phone number is hosted.

    `telnyx`: in your Telnyx inventory. `external`: a number you own that is hosted
    with another provider.
    """


class Data(BaseModel):
    id: str
    """Identifies the event; the same id is reused if the event is redelivered."""

    event_type: Literal["number_reputation.number.removed"]

    occurred_at: datetime

    payload: DataPayload

    record_type: Literal["event"]


class Meta(BaseModel):
    attempt: int

    delivered_to: str


class NumberReputationNumberRemovedWebhookEvent(BaseModel):
    data: Data

    meta: Meta
