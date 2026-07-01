# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .call_dtmf_received import CallDtmfReceived

__all__ = ["CallDtmfReceivedWebhookEvent"]


class CallDtmfReceivedWebhookEvent(BaseModel):
    data: Optional[CallDtmfReceived] = None
