# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_speak_ended import ConferenceSpeakEnded

__all__ = ["ConferenceSpeakEndedWebhookEvent"]


class ConferenceSpeakEndedWebhookEvent(BaseModel):
    data: Optional[ConferenceSpeakEnded] = None
