# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference_recording_saved import ConferenceRecordingSaved

__all__ = ["ConferenceRecordingSavedWebhookEvent"]


class ConferenceRecordingSavedWebhookEvent(BaseModel):
    data: Optional[ConferenceRecordingSaved] = None
