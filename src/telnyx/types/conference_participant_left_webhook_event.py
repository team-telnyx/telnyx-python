# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_participant_left import ConferenceParticipantLeft

__all__ = ["ConferenceParticipantLeftWebhookEvent"]


class ConferenceParticipantLeftWebhookEvent(BaseModel):
    data: Optional[ConferenceParticipantLeft] = None
