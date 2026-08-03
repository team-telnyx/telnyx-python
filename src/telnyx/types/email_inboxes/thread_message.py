# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .inbound_email_address import InboundEmailAddress

__all__ = ["ThreadMessage"]


class ThreadMessage(BaseModel):
    id: str

    attachments: List[Dict[str, object]]

    bcc: List[InboundEmailAddress]

    cc: List[InboundEmailAddress]

    created_at: datetime

    direction: Literal["inbound", "outbound"]

    from_: InboundEmailAddress = FieldInfo(alias="from")

    has_quoted_text: bool
    """Whether conservative plain-text extraction detected a quoted tail.

    False does not prove that the source contains no quoted content.
    """

    headers: Dict[str, object]

    html_body_url: Optional[str] = None
    """URL for an offloaded HTML body.

    Null means the body is not offloaded to a URL; an inline HTML body may still
    exist but is not returned on list reads. Reply extraction uses only the
    plain-text body during ingest.
    """

    in_reply_to: Optional[str] = None

    inbox_id: str

    inline_files: List[Dict[str, object]]

    labels: List[str]
    """
    Mutable message labels used for agent workflow state (for example `spam`,
    `needs_review`, `processed`). Distinct from the immutable send-time `tags` on
    outbound messages: labels are never propagated to Email Detail Records or
    Mission Control reporting. Always empty for outbound messages. Labels on a
    message are independent of the labels on its thread.
    """

    message_id: Optional[str] = None
    """RFC Message-ID header. Null is possible for legacy outbound messages."""

    read_at: Optional[datetime] = None
    """Time the inbound message was marked read. Null means unread."""

    received_at: Optional[datetime] = None
    """Receipt time for inbound messages; null for outbound messages."""

    record_type: Literal["email_message"]

    references: List[str]
    """Ordered RFC Message-ID values from the References header."""

    reply_text: Optional[str] = None
    """
    Conservatively extracted new-reply content persisted from the plain-text body
    during ingest. Null means no plain-text extraction input was available or
    extraction was skipped or failed; HTML bodies are not parsed.
    """

    reply_to: List[InboundEmailAddress]

    sent_at: Optional[datetime] = None
    """Creation/send-acceptance time for outbound messages; null for inbound messages."""

    status: str
    """Received for inbound messages; the current send status for outbound messages."""

    subject: Optional[str] = None

    text_body_url: Optional[str] = None
    """URL for an offloaded plain-text body.

    Null means the body is not offloaded to a URL; an inline plain-text body may
    still exist but is not returned on list reads. `reply_text` and
    `has_quoted_text` are persisted during ingest before any body offload.
    """

    thread_id: str

    to: List[InboundEmailAddress]

    updated_at: datetime
