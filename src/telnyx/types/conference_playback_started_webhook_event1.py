# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .conference_playback_started import ConferencePlaybackStarted

__all__ = ["ConferencePlaybackStartedWebhookEvent"]


class ConferencePlaybackStartedWebhookEvent(BaseModel):
    data: Optional[ConferencePlaybackStarted] = None
