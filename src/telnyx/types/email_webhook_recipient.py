# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmailWebhookRecipient"]


class EmailWebhookRecipient(BaseModel):
    email: str

    kind: Optional[Literal["to", "cc", "bcc"]] = None

    name: Optional[str] = None
