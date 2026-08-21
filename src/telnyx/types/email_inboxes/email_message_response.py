# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel
from .email_message import EmailMessage
from ..suppressed_recipient import SuppressedRecipient

__all__ = ["EmailMessageResponse"]


class EmailMessageResponse(BaseModel):
    data: EmailMessage

    suppressed: Optional[List[SuppressedRecipient]] = None
    """
    Recipients removed by suppression checks when at least one recipient remains and
    the message is accepted.
    """
