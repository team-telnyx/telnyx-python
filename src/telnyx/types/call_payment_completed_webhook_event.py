# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CallPaymentCompletedWebhookEvent", "Data", "DataPayload"]


class DataPayload(BaseModel):
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

    charge_id: Optional[str] = None
    """Charge identifier returned for a successful charge transaction."""

    client_state: Optional[str] = None
    """Base64-encoded state received from the command."""

    connection_id: Optional[str] = None
    """Call Control App ID used in the call."""

    connector_error: Union[str, Dict[str, object], None] = None
    """Additional connector error information, when supplied by the processor."""

    expiration_date: Optional[str] = None
    """Card expiration date in MMYY format."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """Number or SIP URI placing the call."""

    pay_error_code: Optional[str] = None
    """Error code returned by the payment connector or processor."""

    payment_card_number: Optional[str] = None
    """Masked card number with only the last four digits visible."""

    payment_card_postal_code: Optional[str] = None
    """Billing postal code collected from the caller."""

    payment_card_type: Optional[
        Literal["visa", "mastercard", "amex", "optima", "discover", "diners-club", "jcb", "maestro", "enroute"]
    ] = None
    """Detected card type. Present only for the recognized card brands listed below."""

    payment_confirmation_code: Optional[str] = None
    """Payment confirmation code returned by the processor, when available."""

    payment_connector: Optional[str] = None
    """Name of the Pay connector used."""

    payment_error: Optional[str] = None
    """Step-level or processor error associated with the final result."""

    payment_method: Optional[Literal["credit-card", "ach-debit"]] = None
    """Payment method being collected."""

    result: Optional[
        Literal["success", "payment-connector-error", "internal-error", "too-many-failed-attempts", "cancelled"]
    ] = None
    """Final Pay session result."""

    security_code: Optional[str] = None
    """Fully masked card security code."""

    to: Optional[str] = None
    """Destination number or SIP URI of the call."""

    token_id: Optional[str] = None
    """Token identifier returned for a successful tokenize transaction."""


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the event."""

    event_type: Optional[Literal["call.payment.completed"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 datetime when the event occurred."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class CallPaymentCompletedWebhookEvent(BaseModel):
    data: Optional[Data] = None
