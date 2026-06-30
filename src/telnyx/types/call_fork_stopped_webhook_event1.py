# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .call_fork_stopped import CallForkStopped

__all__ = ["CallForkStoppedWebhookEvent"]


class CallForkStoppedWebhookEvent(BaseModel):
    data: Optional[CallForkStopped] = None
