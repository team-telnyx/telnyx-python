# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .email_address import EmailAddress
from ..message_event import MessageEvent

__all__ = ["EmailMessage", "Attachment"]


class Attachment(BaseModel):
    """EDR-aligned attachment metadata. The base64 `content` is never returned."""

    content_id: Optional[str] = None
    """MIME Content-ID for inline references."""

    content_type: str

    disposition: str
    """MIME disposition (e.g.

    `attachment` or `inline`). Runtime passes through the stored value without
    enforcing an enum.
    """

    filename: str

    sha256: Optional[str] = None
    """SHA-256 hex digest of the attachment content."""

    size_bytes: Optional[int] = None
    """Attachment size in bytes."""

    url: Optional[str] = None
    """Telnyx-hosted public URL for the attachment content."""


class EmailMessage(BaseModel):
    id: str

    attachments: List[Attachment]

    bcc: List[EmailAddress]

    cc: List[EmailAddress]

    created_at: datetime

    events: List[MessageEvent]

    from_: EmailAddress = FieldInfo(alias="from")

    record_type: Literal["email_message"]

    reply_to: Optional[str] = None

    status: Literal[
        "queued",
        "scheduled",
        "cancelled",
        "sandbox",
        "sending",
        "sent",
        "failed",
        "deferred",
        "delivered",
        "bounced",
        "complained",
        "rejected",
        "opened",
        "clicked",
        "unsubscribed",
    ]
    """Current status of an email message.

    Lifecycle statuses (queued, scheduled, etc.) are set on creation. Delivery
    statuses (delivered, bounced, etc.) are updated by delivery event consumers.
    """

    subject: str

    template_id: Optional[str] = None

    template_variables: Dict[str, object]

    to: List[EmailAddress]

    inline_css: Optional[bool] = None
    """Present when true in the immediate create response.

    Not persisted; absent on subsequent GET requests.
    """

    recipient_statuses: Optional[Dict[str, int]] = None
    """Per-status recipient counts for the message.

    Present only for outbound messages with recipient rows. Keys are recipient
    statuses, values are counts. Example: `{"delivered": 998, "bounced": 2}`.
    """

    sandbox: Optional[bool] = None
    """Present when sandbox mode was used."""

    scheduled_at: Optional[datetime] = None
    """Present when a scheduled_at value was stored.

    Persists even after the scheduled send has been processed or cancelled.
    """
