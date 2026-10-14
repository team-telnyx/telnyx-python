# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .reputation_number_source import ReputationNumberSource
from .reputation_ownership_status import ReputationOwnershipStatus

__all__ = ["NumberRetrieveOwnershipResponse", "Data", "DataHistory"]


class DataHistory(BaseModel):
    event_type: Optional[str] = None
    """`added`, `check`, `flag`, `confirm` or `removed`."""

    occurred_at: Optional[datetime] = None

    outcome: Optional[str] = None
    """What the event found or did, for example `unchanged` or `carrier_changed`."""


class Data(BaseModel):
    baseline_carrier: Optional[str] = None
    """
    Service provider ID (SPID) of the carrier that held the number when its
    ownership was last established.
    """

    baseline_recorded_at: Optional[datetime] = None

    confirm_by: Optional[datetime] = None

    flag_reason: Optional[str] = None

    history: Optional[List[DataHistory]] = None
    """Ownership events, most recent first."""

    last_checked_at: Optional[datetime] = None
    """When ownership of the number was last checked."""

    ownership_status: Optional[ReputationOwnershipStatus] = None
    """Result of ongoing ownership checks.

    `verified`: the number is with the carrier on record. `pending_confirmation`:
    the number's carrier changed, or a periodic ownership re-verification is due;
    confirm you still own it before `confirm_by`. `flagged`: a periodic
    re-verification went unanswered; the number stays monitored and is not removed,
    but confirm ownership (`POST .../ownership_confirm`) to return it to `verified`.
    `removed`: the number is no longer monitored; returned by
    `POST .../ownership_confirm` with `still_own: false`, and when listing numbers
    with `filter[ownership_status]=removed`.
    """

    phone_number: Optional[str] = None

    source: Optional[ReputationNumberSource] = None
    """Where the phone number is hosted.

    `telnyx`: in your Telnyx inventory. `external`: a number you own that is hosted
    with another provider.
    """


class NumberRetrieveOwnershipResponse(BaseModel):
    data: Data
