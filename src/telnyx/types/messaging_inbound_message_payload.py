# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .messaging_error_0b38e7044b import MessagingError0b38e7044b

__all__ = [
    "MessagingInboundMessagePayload",
    "Body",
    "BodyEdit",
    "BodyRevoke",
    "Cc",
    "Cost",
    "CostBreakdown",
    "CostBreakdownCarrierFee",
    "CostBreakdownRate",
    "From",
    "Media",
    "ToUnionMember0",
]


class BodyEdit(BaseModel):
    """Details for an edited WhatsApp message."""

    message: Dict[str, object]
    """Replacement WhatsApp message content. Its shape depends on the message type."""

    original_message_id: str
    """
    Telnyx message ID when a mapping exists, otherwise the original Meta WhatsApp
    message ID. Treat this value as opaque.
    """


class BodyRevoke(BaseModel):
    """Details for a revoked WhatsApp message."""

    original_message_id: str
    """
    Telnyx message ID when a mapping exists, otherwise the original Meta WhatsApp
    message ID. Treat this value as opaque.
    """


class Body(BaseModel):
    """WhatsApp message body.

    For message edits and revocations, inspect `type` and the corresponding `edit` or `revoke` object.
    """

    id: Optional[str] = None
    """Telnyx identifier for this webhook message."""

    edit: Optional[BodyEdit] = None
    """Details for an edited WhatsApp message."""

    foreign_id: Optional[str] = None
    """Meta WhatsApp message identifier for this webhook event."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """WhatsApp sender in E.164 format."""

    revoke: Optional[BodyRevoke] = None
    """Details for a revoked WhatsApp message."""

    timestamp: Optional[str] = None
    """Unix timestamp supplied by Meta."""

    type: Optional[str] = None
    """WhatsApp message body type.

    Edit and revoke events use `edit` and `revoke`, respectively.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Cc(BaseModel):
    carrier: Optional[str] = None
    """The carrier of the receiver."""

    line_type: Optional[Literal["Wireline", "Wireless", "VoWiFi", "VoIP", "Pre-Paid Wireless", ""]] = None
    """The line-type of the receiver."""

    phone_number: Optional[str] = None
    """Receiving address (+E.164 formatted phone number or short code)."""

    status: Optional[
        Literal["queued", "sending", "sent", "delivered", "sending_failed", "delivery_failed", "delivery_unconfirmed"]
    ] = None


class Cost(BaseModel):
    amount: Optional[str] = None
    """The amount deducted from your account."""

    currency: Optional[str] = None
    """The ISO 4217 currency identifier."""


class CostBreakdownCarrierFee(BaseModel):
    amount: Optional[str] = None
    """The carrier fee amount."""

    currency: Optional[str] = None
    """The ISO 4217 currency identifier."""


class CostBreakdownRate(BaseModel):
    amount: Optional[str] = None
    """The rate amount applied."""

    currency: Optional[str] = None
    """The ISO 4217 currency identifier."""


class CostBreakdown(BaseModel):
    """Detailed breakdown of the message cost components."""

    carrier_fee: Optional[CostBreakdownCarrierFee] = None

    rate: Optional[CostBreakdownRate] = None


class From(BaseModel):
    carrier: Optional[str] = None
    """The carrier of the sender."""

    line_type: Optional[Literal["Wireline", "Wireless", "VoWiFi", "VoIP", "Pre-Paid Wireless", ""]] = None
    """The line-type of the sender."""

    phone_number: Optional[str] = None
    """
    Sending address (+E.164 formatted phone number, alphanumeric sender ID, or short
    code).
    """

    status: Optional[Literal["received", "delivered"]] = None


class Media(BaseModel):
    content_type: Optional[str] = None
    """The MIME type of the requested media."""

    hash_sha256: Optional[str] = None
    """The SHA256 hash of the requested media."""

    size: Optional[int] = None
    """The size of the requested media."""

    url: Optional[str] = None
    """The url of the media requested to be sent."""


class ToUnionMember0(BaseModel):
    carrier: Optional[str] = None
    """The carrier of the receiver."""

    line_type: Optional[Literal["Wireline", "Wireless", "VoWiFi", "VoIP", "Pre-Paid Wireless", ""]] = None
    """The line-type of the receiver."""

    phone_number: Optional[str] = None
    """Receiving address (+E.164 formatted phone number or short code)."""

    status: Optional[
        Literal[
            "queued",
            "sending",
            "sent",
            "delivered",
            "sending_failed",
            "delivery_failed",
            "delivery_unconfirmed",
            "webhook_delivered",
        ]
    ] = None


class MessagingInboundMessagePayload(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    body: Optional[Body] = None
    """WhatsApp message body.

    For message edits and revocations, inspect `type` and the corresponding `edit`
    or `revoke` object.
    """

    cc: Optional[List[Cc]] = None

    completed_at: Optional[datetime] = None
    """Not used for inbound messages."""

    cost: Optional[Cost] = None

    cost_breakdown: Optional[CostBreakdown] = None
    """Detailed breakdown of the message cost components."""

    direction: Optional[Literal["inbound"]] = None
    """The direction of the message.

    Inbound messages are sent to you whereas outbound messages are sent from you.
    """

    encoding: Optional[str] = None
    """Encoding scheme used for the message body."""

    errors: Optional[List[MessagingError0b38e7044b]] = None
    """
    These errors may point at addressees when referring to unsuccessful/unconfirmed
    delivery statuses.
    """

    from_: Optional[From] = FieldInfo(alias="from", default=None)

    media: Optional[List[Media]] = None

    messaging_profile_id: Optional[str] = None
    """Unique identifier for a messaging profile."""

    num_chars: Optional[int] = None
    """The number of characters in the message text"""

    organization_id: Optional[str] = None
    """Unique identifier for a messaging profile."""

    parts: Optional[int] = None
    """Number of parts into which the message's body must be split."""

    received_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the message request was received."""

    record_type: Optional[Literal["message"]] = None
    """Identifies the type of the resource."""

    sent_at: Optional[datetime] = None
    """Not used for inbound messages."""

    subject: Optional[str] = None
    """Message subject."""

    tags: Optional[List[str]] = None
    """Tags associated with the resource."""

    tcr_campaign_billable: Optional[bool] = None
    """Indicates whether the TCR campaign is billable."""

    tcr_campaign_id: Optional[str] = None
    """The Campaign Registry (TCR) campaign ID associated with the message."""

    tcr_campaign_registered: Optional[str] = None
    """The registration status of the TCR campaign."""

    text: Optional[str] = None
    """Message body (i.e., content) as a non-empty string.

    **Required for SMS**
    """

    to: Union[List[ToUnionMember0], str, None] = None
    """Receiving address.

    SMS and MMS webhooks use an array of recipients. WhatsApp webhooks use one E.164
    phone number.
    """

    type: Optional[Literal["SMS", "MMS", "WHATSAPP"]] = None
    """The messaging channel used for the message."""

    valid_until: Optional[datetime] = None
    """Not used for inbound messages."""

    webhook_failover_url: Optional[str] = None
    """
    The failover URL where webhooks related to this message will be sent if sending
    to the primary URL fails.
    """

    webhook_url: Optional[str] = None
    """The URL where webhooks related to this message will be sent."""
