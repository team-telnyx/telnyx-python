# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_participant_playback_started import ConferenceParticipantPlaybackStarted

__all__ = ["ConferenceParticipantPlaybackStartedWebhookEvent"]


class ConferenceParticipantPlaybackStartedWebhookEvent(BaseModel):
    data: Optional[ConferenceParticipantPlaybackStarted] = None
