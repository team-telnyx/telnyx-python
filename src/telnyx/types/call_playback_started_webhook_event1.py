# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_playback_started import CallPlaybackStarted

__all__ = ["CallPlaybackStartedWebhookEvent"]


class CallPlaybackStartedWebhookEvent(BaseModel):
    data: Optional[CallPlaybackStarted] = None
