# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .email_inboxes.email_message import EmailMessage

__all__ = ["EmailMessageRetrieveResponse", "Data"]


class Data(EmailMessage):
    html_body: Optional[str] = None
    """HTML body submitted for the message."""

    text_body: Optional[str] = None
    """Plain-text body submitted for the message."""


class EmailMessageRetrieveResponse(BaseModel):
    data: Data
