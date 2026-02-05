# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_siprec_failed import CallSiprecFailed

__all__ = ["CallSiprecFailedWebhookEvent"]


class CallSiprecFailedWebhookEvent(BaseModel):
    data: Optional[CallSiprecFailed] = None
