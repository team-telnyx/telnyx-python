# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_recording_error import CallRecordingError

__all__ = ["CallRecordingErrorWebhookEvent"]


class CallRecordingErrorWebhookEvent(BaseModel):
    data: Optional[CallRecordingError] = None
