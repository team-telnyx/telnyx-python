# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_refer_completed import CallReferCompleted

__all__ = ["CallReferCompletedWebhookEvent"]


class CallReferCompletedWebhookEvent(BaseModel):
    data: Optional[CallReferCompleted] = None
