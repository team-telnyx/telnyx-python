# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_participant import ConferenceParticipant

__all__ = ["ConferenceRetrieveParticipantResponse"]


class ConferenceRetrieveParticipantResponse(BaseModel):
    data: Optional[ConferenceParticipant] = None
