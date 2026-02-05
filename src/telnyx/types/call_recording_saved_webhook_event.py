# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_recording_saved import CallRecordingSaved

__all__ = ["CallRecordingSavedWebhookEvent"]


class CallRecordingSavedWebhookEvent(BaseModel):
    data: Optional[CallRecordingSaved] = None
