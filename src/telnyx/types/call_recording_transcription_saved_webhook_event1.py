# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .call_recording_transcription_saved import CallRecordingTranscriptionSaved

__all__ = ["CallRecordingTranscriptionSavedWebhookEvent"]


class CallRecordingTranscriptionSavedWebhookEvent(BaseModel):
    data: Optional[CallRecordingTranscriptionSaved] = None
