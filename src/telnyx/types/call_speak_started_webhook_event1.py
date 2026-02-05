# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_speak_started import CallSpeakStarted

__all__ = ["CallSpeakStartedWebhookEvent"]


class CallSpeakStartedWebhookEvent(BaseModel):
    data: Optional[CallSpeakStarted] = None
