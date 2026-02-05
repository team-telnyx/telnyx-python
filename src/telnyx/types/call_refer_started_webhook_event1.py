# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_refer_started import CallReferStarted

__all__ = ["CallReferStartedWebhookEvent"]


class CallReferStartedWebhookEvent(BaseModel):
    data: Optional[CallReferStarted] = None
