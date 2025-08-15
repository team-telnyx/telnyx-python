# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .recording_transcription import RecordingTranscription

__all__ = ["RecordingTranscriptionRetrieveResponse"]


class RecordingTranscriptionRetrieveResponse(BaseModel):
    data: Optional[RecordingTranscription] = None
