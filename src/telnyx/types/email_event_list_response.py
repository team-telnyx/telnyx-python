# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .email_event_type import EmailEventType
from .email_inboxes.email_address import EmailAddress

__all__ = ["EmailEventListResponse", "Email"]


class Email(BaseModel):
    """Summary of the associated email message.

    Present when the email_message preload is available.
    """

    cc: List[EmailAddress]

    from_: EmailAddress = FieldInfo(alias="from")

    subject: str

    to: List[EmailAddress]


class EmailEventListResponse(BaseModel):
    id: str

    email_id: str

    occurred_at: datetime

    record_type: Literal["email_event"]

    type: EmailEventType

    email: Optional[Email] = None
    """Summary of the associated email message.

    Present when the email_message preload is available.
    """

    payload: Optional[Dict[str, object]] = None
