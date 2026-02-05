# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_refer_failed import CallReferFailed

__all__ = ["CallReferFailedWebhookEvent"]


class CallReferFailedWebhookEvent(BaseModel):
    data: Optional[CallReferFailed] = None
