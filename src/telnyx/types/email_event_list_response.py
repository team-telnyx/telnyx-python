# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .time_range import TimeRange
from .email_webhook_recipient import EmailWebhookRecipient

__all__ = [
    "EmailEventListResponse",
    "Data",
    "DataPayload",
    "DataPayloadBcc",
    "DataPayloadCc",
    "DataPayloadFrom",
    "DataPayloadTo",
    "Meta",
]

DataPayloadBcc: TypeAlias = Union[EmailWebhookRecipient, Literal["redacted"]]

DataPayloadCc: TypeAlias = Union[EmailWebhookRecipient, str]


class DataPayloadFrom(BaseModel):
    """Sender projection in account event polling.

    The display name is explicitly null when the message has no sender name.
    """

    email: str

    name: Optional[str] = None


DataPayloadTo: TypeAlias = Union[EmailWebhookRecipient, str]


class DataPayload(BaseModel):
    """Payload returned by GET /email_events.

    Every row includes id, status, and occurred_at. Recipient-scoped rows also include recipient_id, from, subject, and exactly one object-valued to, cc, or bcc field. Legacy or message-scoped rows can omit recipient_id and use object-valued or string-valued to/cc fields, including an empty string when no address exists; bcc is redacted. If the related message or recipient cannot be loaded, the minimal fallback can omit from, subject, and recipient fields. Additional persisted public evidence can be present.
    """

    id: str
    """Email message UUID."""

    occurred_at: datetime

    status: Literal[
        "queued",
        "deferred",
        "scheduled",
        "cancelled",
        "sandbox",
        "sending",
        "sent",
        "failed",
        "delivered",
        "bounced",
        "complained",
        "suppressed",
        "rejected",
        "opened",
        "clicked",
        "unsubscribed",
        "daily_limit_exceeded",
        "scan_deferred",
        "quarantined",
        "quarantine_released",
        "quarantine_release_dispatched",
        "quarantine_rejected",
        "quarantine_expired",
        "gw_reject",
        "injection_timeout",
        "expired",
    ]
    """Stored event outcome slug, not the authoritative recipient status.

    Account polling returns the stored name, including suppression, scan, and
    quarantine lifecycle names. Webhooks retain legacy payload names: gateway
    rejections use failed and MTA expirations use bounced. New sharp stored rows can
    expose gw_reject, injection_timeout, or expired. Use the envelope
    canonical_event_type to identify the outcome across surfaces.
    """

    bcc: Optional[DataPayloadBcc] = None

    cc: Optional[DataPayloadCc] = None
    """Legacy message-scoped address, or an empty string when absent."""

    from_: Optional[DataPayloadFrom] = FieldInfo(alias="from", default=None)
    """Sender projection in account event polling.

    The display name is explicitly null when the message has no sender name.
    """

    recipient_id: Optional[str] = None
    """Durable email recipient UUID. Present for recipient-scoped events."""

    subject: Optional[str] = None

    to: Optional[DataPayloadTo] = None
    """Legacy message-scoped address, or an empty string when absent."""

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


class Data(BaseModel):
    """An account-polling event.

    The envelope is webhook-shaped, but polling preserves stored-event cardinality: queued, sending, sandbox, cancelled, and daily_limit_exceeded message events fan out per recipient; scheduled remains one message-scoped row. Payload fields vary among recipient-scoped, message-scoped, and minimal fallback rows.
    """

    id: str
    """Event UUID."""

    canonical_event_type: str
    """Additive canonical outcome name, prefixed with `email.`.

    Gateway rejection is `email.gw_reject`, ambiguous injection timeout is
    `email.injection_timeout`, and MTA expiration is `email.expired`. Unchanged
    outcomes retain their names. Existing stored rows are translated only when
    recorded payload evidence proves the outcome; a legacy failed row is not guessed
    or sharpened.
    """

    event_type: str
    """Legacy customer-visible event name, prefixed with `email.`.

    Gateway rejections render `email.failed`; MTA expirations render
    `email.bounced`. Webhook subscription allowlists match the legacy name.
    """

    occurred_at: datetime

    payload: DataPayload
    """Payload returned by GET /email_events.

    Every row includes id, status, and occurred_at. Recipient-scoped rows also
    include recipient_id, from, subject, and exactly one object-valued to, cc, or
    bcc field. Legacy or message-scoped rows can omit recipient_id and use
    object-valued or string-valued to/cc fields, including an empty string when no
    address exists; bcc is redacted. If the related message or recipient cannot be
    loaded, the minimal fallback can omit from, subject, and recipient fields.
    Additional persisted public evidence can be present.
    """

    recipient_id: Optional[str] = None
    """Durable email recipient UUID.

    Present for recipient-scoped events, including each queued, sending, sandbox,
    cancelled, and daily_limit_exceeded fan-out event.
    """


class Meta(BaseModel):
    page_size: int

    time_range: TimeRange

    page_cursor: Optional[str] = None
    """Cursor for the next page, when more results are available."""


class EmailEventListResponse(BaseModel):
    data: List[Data]

    meta: Meta
