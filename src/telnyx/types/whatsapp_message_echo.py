# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .messaging_error_0b38e7044b import MessagingError0b38e7044b

__all__ = ["WhatsappMessageEcho", "Data", "DataPayload", "DataPayloadBody", "DataPayloadCost", "DataPayloadFrom"]


class DataPayloadBody(BaseModel):
    """Mirrored WhatsApp message content.

    The content property matches the value of `type`.
    """

    id: str
    """Telnyx identifier for the mirrored message."""

    foreign_id: str
    """Meta WhatsApp message identifier, also known as a wamid."""

    timestamp: str
    """Unix timestamp supplied by Meta."""

    type: str
    """WhatsApp message content type."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """WhatsApp user who received the message."""

    from_user_id: Optional[str] = None
    """Opaque recipient identifier when Meta does not supply a phone number."""

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


class DataPayloadCost(BaseModel):
    """No charge is created for a Business app message echo."""

    amount: Optional[str] = None

    currency: Optional[str] = None


class DataPayloadFrom(BaseModel):
    phone_number: str
    """Coexistence-enabled business phone number in E.164 format."""

    carrier: Optional[str] = None

    line_type: Optional[str] = None


class DataPayload(BaseModel):
    id: str
    """Telnyx identifier for the mirrored message."""

    body: DataPayloadBody
    """Mirrored WhatsApp message content.

    The content property matches the value of `type`.
    """

    cost: DataPayloadCost
    """No charge is created for a Business app message echo."""

    direction: Literal["outbound"]
    """Indicates that the business sent the message to the WhatsApp user."""

    errors: List[MessagingError0b38e7044b]

    from_: DataPayloadFrom = FieldInfo(alias="from")

    messaging_profile_id: str

    organization_id: str

    origin: Literal["whatsapp_business_app"]
    """Identifies the WhatsApp Business app as the source of the message."""

    record_type: Literal["message"]

    to: str
    """WhatsApp user who received the Business app message."""

    type: Literal["WHATSAPP"]

    received_at: Optional[datetime] = None

    tags: Optional[List[str]] = None

    webhook_failover_url: Optional[str] = None

    webhook_url: Optional[str] = None


class Data(BaseModel):
    id: str

    event_type: Literal["message.echo"]

    occurred_at: datetime

    payload: DataPayload

    record_type: Literal["event"]


class WhatsappMessageEcho(BaseModel):
    data: Data
