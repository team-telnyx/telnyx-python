# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EmailRecipient"]


class EmailRecipient(BaseModel):
    id: str
    """Recipient UUID."""

    address: Optional[str] = None
    """Recipient email address. Null for BCC recipients (redacted for privacy)."""

    billable: bool
    """Whether this recipient's delivery is billable (set on queue acceptance)."""

    kind: Literal["to", "cc", "bcc"]

    message_id: str
    """Parent email message UUID."""

    record_type: Literal["email_recipient"]

    status: Literal["queued", "sending", "sent", "deferred", "delivered", "bounced", "failed", "gw_reject", "cancelled"]
    """Current per-recipient delivery status."""

    delivered_at: Optional[datetime] = None

    failed_at: Optional[datetime] = None

    sent_at: Optional[datetime] = None

    smtp_code: Optional[int] = None
    """SMTP response code when available (e.g. 550 for bounces)."""

    smtp_response: Optional[str] = None
    """SMTP response message when available."""
