# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_streaming_stopped import CallStreamingStopped

__all__ = ["CallStreamingStoppedWebhookEvent"]


class CallStreamingStoppedWebhookEvent(BaseModel):
    data: Optional[CallStreamingStopped] = None
