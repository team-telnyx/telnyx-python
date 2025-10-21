# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .messaging_error import MessagingError

__all__ = [
    "InboundMessageWebhookEvent",
    "Data",
    "DataPayload",
    "DataPayloadCc",
    "DataPayloadCost",
    "DataPayloadCostBreakdown",
    "DataPayloadCostBreakdownCarrierFee",
    "DataPayloadCostBreakdownRate",
    "DataPayloadFrom",
    "DataPayloadMedia",
    "DataPayloadTo",
]


class DataPayloadCc(BaseModel):
    carrier: Optional[str] = None
    """The carrier of the receiver."""

    line_type: Optional[Literal["Wireline", "Wireless", "VoWiFi", "VoIP", "Pre-Paid Wireless", ""]] = None
    """The line-type of the receiver."""

    phone_number: Optional[str] = None
    """Receiving address (+E.164 formatted phone number or short code)."""

    status: Optional[
        Literal["queued", "sending", "sent", "delivered", "sending_failed", "delivery_failed", "delivery_unconfirmed"]
    ] = None


class DataPayloadCost(BaseModel):
    amount: Optional[str] = None
    """The amount deducted from your account."""

    currency: Optional[str] = None
    """The ISO 4217 currency identifier."""


class DataPayloadCostBreakdownCarrierFee(BaseModel):
    amount: Optional[str] = None
    """The carrier fee amount."""

    currency: Optional[str] = None
    """The ISO 4217 currency identifier."""


class DataPayloadCostBreakdownRate(BaseModel):
    amount: Optional[str] = None
    """The rate amount applied."""

    currency: Optional[str] = None
    """The ISO 4217 currency identifier."""


class DataPayloadCostBreakdown(BaseModel):
    carrier_fee: Optional[DataPayloadCostBreakdownCarrierFee] = None

    rate: Optional[DataPayloadCostBreakdownRate] = None


class DataPayloadFrom(BaseModel):
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


class DataPayloadMedia(BaseModel):
    content_type: Optional[str] = None
    """The MIME type of the requested media."""

    hash_sha256: Optional[str] = None
    """The SHA256 hash of the requested media."""

    size: Optional[int] = None
    """The size of the requested media."""

    url: Optional[str] = None
    """The url of the media requested to be sent."""


class DataPayloadTo(BaseModel):
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


class DataPayload(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    cc: Optional[List[DataPayloadCc]] = None

    completed_at: Optional[datetime] = None
    """Not used for inbound messages."""

    cost: Optional[DataPayloadCost] = None

    cost_breakdown: Optional[DataPayloadCostBreakdown] = None
    """Detailed breakdown of the message cost components."""

    direction: Optional[Literal["inbound"]] = None
    """The direction of the message.

    Inbound messages are sent to you whereas outbound messages are sent from you.
    """

    encoding: Optional[str] = None
    """Encoding scheme used for the message body."""

    errors: Optional[List[MessagingError]] = None
    """
    These errors may point at addressees when referring to unsuccessful/unconfirmed
    delivery statuses.
    """

    from_: Optional[DataPayloadFrom] = FieldInfo(alias="from", default=None)

    media: Optional[List[DataPayloadMedia]] = None

    messaging_profile_id: Optional[str] = None
    """Unique identifier for a messaging profile."""

    parts: Optional[int] = None
    """Number of parts into which the message's body must be split."""

    received_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the message request was received."""

    record_type: Optional[Literal["message"]] = None
    """Identifies the type of the resource."""

    sent_at: Optional[datetime] = None
    """Not used for inbound messages."""

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

    to: Optional[List[DataPayloadTo]] = None

    type: Optional[Literal["SMS", "MMS"]] = None
    """The type of message. This value can be either 'sms' or 'mms'."""

    valid_until: Optional[datetime] = None
    """Not used for inbound messages."""

    webhook_failover_url: Optional[str] = None
    """
    The failover URL where webhooks related to this message will be sent if sending
    to the primary URL fails.
    """

    webhook_url: Optional[str] = None
    """The URL where webhooks related to this message will be sent."""


class Data(BaseModel):
    id: Optional[str] = None
    """Identifies the type of resource."""

    event_type: Optional[Literal["message.received"]] = None
    """The type of event being delivered."""

    occurred_at: Optional[datetime] = None
    """ISO 8601 formatted date indicating when the resource was created."""

    payload: Optional[DataPayload] = None

    record_type: Optional[Literal["event"]] = None
    """Identifies the type of the resource."""


class InboundMessageWebhookEvent(BaseModel):
    data: Optional[Data] = None
