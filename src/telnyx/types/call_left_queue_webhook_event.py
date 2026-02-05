# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_left_queue import CallLeftQueue

__all__ = ["CallLeftQueueWebhookEvent"]


class CallLeftQueueWebhookEvent(BaseModel):
    data: Optional[CallLeftQueue] = None
