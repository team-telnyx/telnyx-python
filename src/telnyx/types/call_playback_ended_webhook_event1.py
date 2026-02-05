# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_playback_ended import CallPlaybackEnded

__all__ = ["CallPlaybackEndedWebhookEvent"]


class CallPlaybackEndedWebhookEvent(BaseModel):
    data: Optional[CallPlaybackEnded] = None
