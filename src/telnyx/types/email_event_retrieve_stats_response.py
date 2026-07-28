# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel
from .time_range import TimeRange

__all__ = ["EmailEventRetrieveStatsResponse", "Data", "DataCounts", "DataRates"]


class DataCounts(BaseModel):
    """Recipient-level outcome counts for the queried time range.

    Each to, cc, and bcc recipient counts separately; repeated events of the same type for the same message and recipient count once. Partial MTA injection results count successful recipients as sent and unsuccessful recipients as failed. Only the ten listed event types are counted; other valid event types (scheduled, cancelled, sandbox, sending, rejected) are not included in stats.
    """

    bounced: int

    clicked: int

    complained: int

    deferred: int

    delivered: int

    failed: int

    opened: int

    queued: int

    sent: int

    unsubscribed: int


class DataRates(BaseModel):
    """Recipient-level event rates as percentages, rounded to 2 decimal places."""

    bounce_rate: float
    """Bounced recipients / queued recipients as a percentage."""

    click_rate: float
    """Recipients clicked / recipients opened as a percentage."""

    complaint_rate: float
    """
    Recipients with a complaint feedback report / delivered recipients as a
    percentage.
    """

    deferred_rate: float
    """Deferred recipients / queued recipients as a percentage."""

    delivery_rate: float
    """Delivered recipients / queued recipients as a percentage."""

    open_rate: float
    """Recipients opened / recipients delivered as a percentage."""


class Data(BaseModel):
    counts: DataCounts
    """Recipient-level outcome counts for the queried time range.

    Each to, cc, and bcc recipient counts separately; repeated events of the same
    type for the same message and recipient count once. Partial MTA injection
    results count successful recipients as sent and unsuccessful recipients as
    failed. Only the ten listed event types are counted; other valid event types
    (scheduled, cancelled, sandbox, sending, rejected) are not included in stats.
    """

    rates: DataRates
    """Recipient-level event rates as percentages, rounded to 2 decimal places."""

    record_type: Literal["email_event_stats"]

    time_range: TimeRange


class EmailEventRetrieveStatsResponse(BaseModel):
    data: Data
