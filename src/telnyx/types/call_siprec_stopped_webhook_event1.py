# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_siprec_stopped import CallSiprecStopped

__all__ = ["CallSiprecStoppedWebhookEvent"]


class CallSiprecStoppedWebhookEvent(BaseModel):
    data: Optional[CallSiprecStopped] = None
