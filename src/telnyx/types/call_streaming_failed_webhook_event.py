# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .call_streaming_failed import CallStreamingFailed

__all__ = ["CallStreamingFailedWebhookEvent"]


class CallStreamingFailedWebhookEvent(BaseModel):
    data: Optional[CallStreamingFailed] = None
