# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...shared.reputation_data import ReputationData
from .reputation_number_source import ReputationNumberSource
from .reputation_ownership_status import ReputationOwnershipStatus

__all__ = ["ReputationPhoneNumber"]


class ReputationPhoneNumber(BaseModel):
    id: Optional[str] = None

    confirm_by: Optional[datetime] = None
    """Deadline to confirm you still own the number.

    Set only while `ownership_status` is `pending_confirmation`.
    """

    created_at: Optional[datetime] = None

    enterprise_id: Optional[str] = None

    flag_reason: Optional[str] = None
    """Why the number's ownership was flagged.

    `carrier_changed` when an ownership check found the number with a different
    carrier.
    """

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
    """E.164 with leading `+`."""

    removal_reason: Optional[
        Literal["ported_away", "unconfirmed_ownership", "reassigned", "customer_reported", "customer_removed"]
    ] = None
    """Why a number was removed.

    `ported_away`: you confirmed the number left your control after a carrier
    change. `unconfirmed_ownership`: a carrier change was not confirmed before the
    deadline. `reassigned`: the number was reported as permanently disconnected.
    `customer_reported`: you reported that you no longer own the number.
    `customer_removed`: you removed the number.
    """

    removed_at: Optional[datetime] = None
    """When the number was removed. Set only for removed numbers."""

    reputation_data: Optional[ReputationData] = None
    """Reputation snapshot for a phone number.

    Each metric is a 0–100 score; `spam_risk` is a coarse bucket. Field set may grow
    over time - read by key.
    """

    source: Optional[ReputationNumberSource] = None
    """Where the phone number is hosted.

    `telnyx`: in your Telnyx inventory. `external`: a number you own that is hosted
    with another provider.
    """

    updated_at: Optional[datetime] = None
