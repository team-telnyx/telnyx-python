# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_participant_speak_started import ConferenceParticipantSpeakStarted

__all__ = ["ConferenceParticipantSpeakStartedWebhookEvent"]


class ConferenceParticipantSpeakStartedWebhookEvent(BaseModel):
    data: Optional[ConferenceParticipantSpeakStarted] = None
