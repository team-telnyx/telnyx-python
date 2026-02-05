# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_speak_started import ConferenceSpeakStarted

__all__ = ["ConferenceSpeakStartedWebhookEvent"]


class ConferenceSpeakStartedWebhookEvent(BaseModel):
    data: Optional[ConferenceSpeakStarted] = None
