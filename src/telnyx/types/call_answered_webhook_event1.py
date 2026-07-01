# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .call_answered import CallAnswered

__all__ = ["CallAnsweredWebhookEvent"]


class CallAnsweredWebhookEvent(BaseModel):
    data: Optional[CallAnswered] = None
