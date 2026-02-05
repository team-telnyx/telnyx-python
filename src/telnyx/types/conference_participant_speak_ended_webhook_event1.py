# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_participant_speak_ended import ConferenceParticipantSpeakEnded

__all__ = ["ConferenceParticipantSpeakEndedWebhookEvent"]


class ConferenceParticipantSpeakEndedWebhookEvent(BaseModel):
    data: Optional[ConferenceParticipantSpeakEnded] = None
