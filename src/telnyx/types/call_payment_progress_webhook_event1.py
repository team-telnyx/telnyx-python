# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallPaymentProgressWebhookEvent", "Data", "DataPayload"]


class DataPayload(BaseModel):
    attempt: Optional[int] = None
    """Current 1-based attempt number for the step."""

    bank_account_number: Optional[str] = None
    """Masked bank account number with only the last two digits visible."""

    bank_account_type: Optional[str] = None
    """Bank account type, when available."""

    bank_routing_number: Optional[str] = None
    """Bank routing number collected from the caller."""

    call_control_id: Optional[str] = None
    """Call ID used to issue commands via Call Control API."""

    call_leg_id: Optional[str] = None
    """ID unique to the call leg."""

    call_session_id: Optional[str] = None
    """ID shared by related call legs in the same call session."""

    client_state: Optional[str] = None
    """Base64-encoded state received from the command."""

    connection_id: Optional[str] = None
    """Call Control App ID used in the call."""

    error_type: Optional[
        Literal[
            "timeout",
            "invalid-card-number",
            "invalid-card-type",
            "invalid-date",
            "invalid-security-code",
            "invalid-postal-code",
            "invalid-bank-routing-number",
            "invalid-bank-account-number",
            "input-matching-failed",
        ]
    ] = None
    """Step-level error when payment collection fails."""

    expiration_date: Optional[str] = None
    """Card expiration date in MMYY format."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """Number or SIP URI placing the call."""

    payment_card_number: Optional[str] = None
    """Masked card number with only the last four digits visible."""

    payment_card_postal_code: Optional[str] = None
    """Billing postal code collected from the caller."""

    payment_card_type: Optional[
        Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    ] = None
    """Detected card type. Present only for the recognized card brands listed below."""

    payment_connector: Optional[str] = None
    """Name of the Pay connector used."""

    payment_method: Optional[Literal["credit-card", "ach-debit"]] = None
    """Payment method being collected."""

    payment_status: Optional[Literal["completed", "failed", "processing"]] = None
    """Status of the current payment step."""

    payment_step: Optional[
        Literal[
            "payment-card-number",
            "expiration-date",
            "postal-code",
            "security-code",
            "bank-routing-number",
            "bank-account-number",
            "payment-processing",
        ]
    ] = None
    """Current payment collection or processing step."""

    security_code: Optional[str] = None
    """Fully masked card security code."""

    to: Optional[str] = None
    """Destination number or SIP URI of the call."""


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the event."""

    event_type: Optional[Literal["call.payment.progress"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallPaymentProgressWebhookEvent(BaseModel):
    data: Optional[Data] = None
