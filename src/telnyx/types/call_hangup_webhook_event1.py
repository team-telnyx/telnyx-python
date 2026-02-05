# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_hangup import CallHangup

__all__ = ["CallHangupWebhookEvent"]


class CallHangupWebhookEvent(BaseModel):
    data: Optional[CallHangup] = None
