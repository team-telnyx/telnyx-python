# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HostedNumberOrderEventWebhookEvent", "Data", "DataPayload", "DataPayloadNumber"]


class DataPayloadNumber(BaseModel):
    status: Optional[
        Literal[
            "deleted",
            "failed",
            "failed_activation",
            "failed_carrier_rejected",
            "failed_ineligible_carrier",
            "failed_number_already_hosted",
            "failed_number_not_found",
            "failed_ownership_verification",
            "failed_timeout",
            "ownership_successful",
            "pending",
            "provisioning",
            "successful",
        ]
    ] = None
    """Current status of this phone number within the order."""

    value: Optional[str] = None
    """Phone number in +E.164 format."""


class DataPayload(BaseModel):
    """Payload delivered with every messaging_hosted_numbers_orders.* event.

    `approval_deadline` and `decision` are meaningful only for `internal_transfer_*` events.
    """

    approval_deadline: Optional[int] = None
    """
    Unix timestamp (seconds) by which the losing organization must respond before
    auto-approval. Populated on internal-transfer events once an approval window has
    been issued.
    """

    decision: Optional[Literal["pending", "approved", "rejected"]] = None
    """Approval decision for the internal transfer.

    Defaults to `pending` for non-internal-transfer events.
    """

    numbers: Optional[List[DataPayloadNumber]] = None

    order_id: Optional[str] = None
    """The ID of the hosted number order."""

    order_status: Optional[
        Literal[
            "pending",
            "provisioning",
            "successful",
            "failed",
            "deleted",
            "carrier_rejected",
            "compliance_review_failed",
            "incomplete_documentation",
            "incorrect_billing_information",
            "ineligible_carrier",
            "loa_file_invalid",
            "loa_file_successful",
        ]
    ] = None
    """Current status of the order."""

    profile_id: Optional[str] = None
    """The messaging profile associated with the order."""

    user_id: Optional[str] = None
    """The organization that owns the order."""


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the event."""

    event_type: Optional[
        Literal[
            "messaging_hosted_numbers_orders.created",
            "messaging_hosted_numbers_orders.updated",
            "messaging_hosted_numbers_orders.deleted",
            "messaging_hosted_numbers_orders.internal_transfer_detected",
            "messaging_hosted_numbers_orders.internal_transfer_approval_requested",
            "messaging_hosted_numbers_orders.internal_transfer_approved",
            "messaging_hosted_numbers_orders.internal_transfer_rejected",
            "messaging_hosted_numbers_orders.internal_transfer_auto_approved",
        ]
    ] = None
    """The type of event being delivered.

    Internal transfer events are only emitted for orders where the numbers are
    already active on another Telnyx account.
    """

    occurred_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the event was generated."""

    payload: Optional[DataPayload] = None
    """Payload delivered with every messaging_hosted_numbers_orders.\\** event.

    `approval_deadline` and `decision` are meaningful only for `internal_transfer_*`
    events.
    """

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class HostedNumberOrderEventWebhookEvent(BaseModel):
    data: Optional[Data] = None
