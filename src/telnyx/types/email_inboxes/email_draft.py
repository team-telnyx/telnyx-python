# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .email_address import EmailAddress

__all__ = ["EmailDraft"]


class EmailDraft(BaseModel):
    """An unsent, mutable draft message belonging to an inbox."""

    id: str

    inbox_id: str

    record_type: Literal["email_draft"]

    status: Literal["draft", "sending", "sent"]
    """`draft` until the draft is sent.

    A sent draft is retained for audit and becomes immutable.
    """

    attachments: Optional[List[Dict[str, object]]] = None

    bcc: Optional[List[EmailAddress]] = None

    cc: Optional[List[EmailAddress]] = None

    created_at: Optional[datetime] = None

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """Sender address. Defaults to the inbox address at send time when null."""

    from_name: Optional[str] = None

    headers: Optional[Dict[str, str]] = None
    """Custom headers. Reply drafts carry `In-Reply-To` and `References`."""

    html_body: Optional[str] = None

    labels: Optional[List[str]] = None
    """Mutable mailbox-state labels. Not propagated to Email Detail Records."""

    metadata: Optional[Dict[str, object]] = None
    """Arbitrary customer-defined metadata."""

    reply_to: Optional[str] = None

    reply_to_message_id: Optional[str] = None
    """Inbound message this draft replies to. Server-owned; set only on reply drafts."""

    sent_at: Optional[datetime] = None

    sent_message_id: Optional[str] = None
    """The email message created when this draft was sent."""

    subject: Optional[str] = None

    tags: Optional[List[str]] = None
    """
    Transport/reporting attribution tags, propagated to Email Detail Records at send
    time.
    """

    text_body: Optional[str] = None

    thread_id: Optional[str] = None
    """Conversation thread inherited from the parent message."""

    to: Optional[List[EmailAddress]] = None

    updated_at: Optional[datetime] = None
