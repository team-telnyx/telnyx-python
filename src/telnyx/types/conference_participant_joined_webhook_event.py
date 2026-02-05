# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_participant_joined import ConferenceParticipantJoined

__all__ = ["ConferenceParticipantJoinedWebhookEvent"]


class ConferenceParticipantJoinedWebhookEvent(BaseModel):
    data: Optional[ConferenceParticipantJoined] = None
