# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NumberReputationExternalVerificationStatusChangedWebhookEvent", "Data", "DataPayload", "Meta"]


class DataPayload(BaseModel):
    enterprise_id: str

    record_type: Literal["reputation_external_verification"]

    reviewed_at: datetime
    """When the review decision was made.

    Always set: this event is only sent after a review.
    """

    status: Literal["approved", "rejected"]
    """The review outcome.

    `pending` is never delivered: the event is sent only once the proof is reviewed.
    """

    rejection_reason: Optional[str] = None
    """Set only when `status` is `rejected`."""


class Data(BaseModel):
    id: str
    """Identifies the event; the same id is reused if the event is redelivered."""

    event_type: Literal["number_reputation.external_verification.status_changed"]

    occurred_at: datetime

    payload: DataPayload

    record_type: Literal["event"]


class Meta(BaseModel):
    attempt: int

    delivered_to: str


class NumberReputationExternalVerificationStatusChangedWebhookEvent(BaseModel):
    data: Data

    meta: Meta
