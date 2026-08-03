# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .email_inbox import EmailInbox

__all__ = ["EmailInboxResponse"]


class EmailInboxResponse(BaseModel):
    data: EmailInbox
