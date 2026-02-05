# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_participant_playback_ended import ConferenceParticipantPlaybackEnded

__all__ = ["ConferenceParticipantPlaybackEndedWebhookEvent"]


class ConferenceParticipantPlaybackEndedWebhookEvent(BaseModel):
    data: Optional[ConferenceParticipantPlaybackEnded] = None
